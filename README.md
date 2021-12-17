# PressurePlate


[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

<p align="center">
 <img width="185px" src="imgs/repo-4p.gif" align="center" alt="Four Agent, Linear Layout" />
</p>


# Description
Pressure Plate is a multi-agent environment that requires agents to cooperate during the traveral of a gridworld.

Currently, Pressure Plate supports four-, five-, and six-player linear levels, but is easily configurable for
custom scenarios. See [Customizing Scenarios](#customizing-scenarios) for more information.

## Observation Space

## Action Space
Pressure Plate's action space is discrete and has four options: up, down, left, right, no-op.

## Reward Function


# Installation
After cloning the repo, ```cd``` into ```pressureplate``` and:
```cli
pip install -e .
```

# Using Pressure Plate
Within your Python script, access the three currently available tasks as follows:
```python
env = gym.make('pressureplate-linear-4p-v0')
env = gym.make('pressureplate-linear-5p-v0')
env = gym.make('pressureplate-linear-6p-v0')
```
## Customizing Scenarios
To create a custom Pressure Plate layout, you can add a layout dictionary to the ```pressureplate/assets.py``` file. 
The dictionary must contain lists of ```(x,y)``` coordinates of the following elements:
* A unique identifier (e.g., ```'FOUR_PLAYERS'```)
* ```'WALLS'```
* ```'DOORS'```
* ```'PLATES'```
* ```'AGENTS'```
* ```'GOAL'```

Additionally, you will need to register the new task as a gym environment within ```pressureplate/__init__.py```
For detailed instructions,
please refer to the docstring within ```pressureplate/assets.py```.

# Citation


