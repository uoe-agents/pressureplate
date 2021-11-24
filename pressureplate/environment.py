import gym
from gym import spaces
import numpy as np
from enum import IntEnum
# from .assets import FOUR_PLAYER_WALLS, FOUR_PLAYER_DOORS, FOUR_PLAYER_PLATES, FOUR_PLAYER_AGENTS, FOUR_PLAYER_GOAL
from .assets import LINEAR
# TODO: Handle case where agent is in the cell of a door and then other agent steps off of the plate


# Global elements
_LAYER_AGENTS = 0
_LAYER_WALLS = 1
_LAYER_DOORS = 2
_LAYER_PLATES = 3
_LAYER_GOAL = 4

class Actions(IntEnum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3
    Noop = 4


class Entity:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y


class Agent(Entity):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)


class Plate(Entity):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.pressed = False


class Door(Entity):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.open = False


class Wall(Entity):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)


class Goal(Entity):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.achieved = False


class PressurePlate(gym.Env):
    """
    0 0 0 0 0
    0 0 0 0 G
    w w D w w
    a 0 0 0 p
    a 0 0 0 0
    """
    metadata = {"render.modes": ["human"]}

    def __init__(self, height, width, n_agents, sensor_range, layout):
        self.grid_size = (height, width)
        self.n_agents = n_agents
        self.sensor_range = sensor_range

        self.grid = np.zeros((5, *self.grid_size))

        self.action_space = spaces.Tuple(
            tuple(2 * [spaces.Discrete(len(Actions))])
        )
        self.observation_space

        self.agents = []
        self.plates = []
        self.walls = []
        self.doors = []
        self.goal = None

        self._rendering_initialized = False

        if layout == 'linear':
            self.layout = LINEAR

    def step(self, actions):
        """[up, down, left, right]"""
        for i, a in enumerate(actions):
            # print(f'Current: {[self.agents[i].x, self.agents[i].y]}')
            proposed_pos = [self.agents[i].x, self.agents[i].y]

            if a == 0:
                proposed_pos[1] -= 1
                if not self._detect_collision(proposed_pos):
                    self.agents[i].y -= 1

            elif a == 1:
                proposed_pos[1] += 1
                if not self._detect_collision(proposed_pos):
                    self.agents[i].y += 1

            elif a == 2:
                proposed_pos[0] -= 1
                if not self._detect_collision(proposed_pos):
                    self.agents[i].x -= 1

            elif a == 3:
                proposed_pos[0] += 1
                if not self._detect_collision(proposed_pos):
                    self.agents[i].x += 1

            else:
                # NOOP
                pass

        # Detecting plate pressing
        # Each plate is directly tied to a door. For this, we are using iter indexing
        # e.g., the ith plate is tied to the ith door
        # There is a sub-loop to handle the case where a plate was stood upon in the previous iteration
        # TODO: alter this to tie specific agent to specific plate
        # for i, plate in enumerate(self.plates):
        #
        #     if not plate.pressed:
        #         for agent in self.agents:
        #             if [plate.x, plate.y] == [agent.x, agent.y]:
        #                 plate.pressed = True
        #                 self.doors[i].open = True
        #
        #     if plate.pressed:
        #         standing = []
        #         for agent in self.agents:
        #             standing.append([plate.x, plate.y] == [agent.x, agent.y])
        #
        #         if np.sum(standing) == 0:
        #             plate.pressed = False
        #             self.doors[i].open = False

        for i, plate in enumerate(self.plates):
            if not plate.pressed:
                if [plate.x, plate.y] == [self.agents[plate.id].x, self.agents[plate.id].y]:
                    plate.pressed = True
                    self.doors[plate.id].open = True

            else:
                if [plate.x, plate.y] != [self.agents[plate.id].x, self.agents[plate.id].y]:
                    plate.pressed = False
                    self.doors[plate.id].open = False

        # Detecting reward collision
        r = []
        for agent in self.agents:
            r.append([agent.x, agent.y] == [self.goal.x, self.goal.y])
        got_goal = np.sum(r) > 0

        if got_goal:
            self.goal.achieved = True

    def _detect_collision(self, proposed_position):
        """Need to check for collision with (1) grid edge, (2) walls, (3) closed doors (4) other agents"""
        # Grid edge
        if np.any([
            proposed_position[0] < 0,
            proposed_position[1] < 0,
            proposed_position[0] >= self.grid_size[1],
            proposed_position[1] >= self.grid_size[0]
        ]):
            return True

        # Walls
        for wall in self.walls:
            if proposed_position == [wall.x, wall.y]:
                return True

        # Closed Door
        for door in self.doors:
            if not door.open:
                for j in range(len(door.x)):
                    if proposed_position == [door.x[j], door.y[j]]:
                        return True

        # Other agents
        for agent in self.agents:
            if proposed_position == [agent.x, agent.y]:
                return True

        return False

    def reset(self):
        # Grid wipe
        self.grid = np.zeros((5, *self.grid_size))

        # Agents
        for i, agent in enumerate(self.layout['FOUR_PLAYER_AGENTS']):
            self.agents.append(Agent(i, agent[0], agent[1]))
            self.grid[_LAYER_AGENTS, agent[1], agent[0]] = 1

        # Walls
        for i, wall in enumerate(self.layout['FOUR_PLAYER_WALLS']):
            self.walls.append(Wall(i, wall[0], wall[1]))
            self.grid[_LAYER_WALLS, wall[1], wall[0]] = 1

        # Doors
        for i, door in enumerate(self.layout['FOUR_PLAYER_DOORS']):
            self.doors.append(Door(i, door[0], door[1]))
            for j in range(len(door[0])):
                self.grid[_LAYER_DOORS, door[1][j], door[0][j]] = 1

        # Plate
        for i, plate in enumerate(self.layout['FOUR_PLAYER_PLATES']):
            self.plates.append(Plate(i, plate[0], plate[1]))
            self.grid[_LAYER_PLATES, plate[1], plate[0]] = 1

        # Goal
        self.goal = Goal('goal', self.layout['FOUR_PLAYER_GOAL'][0][0], self.layout['FOUR_PLAYER_GOAL'][0][1])
        self.grid[_LAYER_GOAL, self.layout['FOUR_PLAYER_GOAL'][0][1], self.layout['FOUR_PLAYER_GOAL'][0][0]] = 1

        # return self._get_obs()

    def _get_obs(self):
        obs = []

        for agent in self.agents:
            x, y = agent.x, agent.y
            pad = self.sensor_range // 2

            print(f'{x},{y}')
            print(f'pad: {pad}')

            x_left = max(0, x - pad)
            x_right = min(self.grid_size[1] - 1, x + pad)
            y_up = max(0, y - pad)
            y_down = min(self.grid_size[0] - 1, y + pad)

            print(f'x_left: {x_left}')
            print(f'x_right: {x_right}')
            print(f'y_up: {y_up}')
            print(f'y_down: {y_down}')

            x_left_padding = pad - (x - x_left)
            x_right_padding = pad - (x_right - x)
            y_up_padding = pad - (y - y_up)
            y_down_padding = pad - (y_down - y)

            # Agents
            _agents = self.grid_size[_LAYER_AGENTS, y_up:y_down, x_left:x_right]
            _agents = np.concatenate((np.zeros((self.sensor_range, x_left_padding)), _agents), axis=1)
            _agents = np.concatenate(_agents, np.zeros((self.sensor_range, x_right_padding)), axis=1)
            print(_agents)
            qqqq
            # Walls

            # Doors

            # Plate

            # Goal
        pass # for now

    def _get_flat_grid(self):
        grid = np.zeros(self.grid_size)

        # Plate
        for plate in self.plates:
            grid[plate.y, plate.x] = 2

        # Walls
        for wall in self.walls:
            grid[wall.y, wall.x] = 3

        # Doors
        for door in self.doors:
            if door.open:
                grid[door.y, door.x] = 0
            else:
                grid[door.y, door.x] = 4

        # Goal
        grid[self.goal.y, self.goal.x] = 5

        # Agents
        for agent in self.agents:
            grid[agent.y, agent.x] = 1

        return grid

    def _init_render(self):
        from .rendering import Viewer
        self.viewer = Viewer(self.grid_size)
        self._rendering_initialized = True

    def render(self, mode='human'):
        if not self._rendering_initialized:
            self._init_render()
        return self.viewer.render(self, mode == 'rgb_array')

    def close(self):
        pass
