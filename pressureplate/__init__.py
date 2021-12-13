from gym.envs.registration import register



register(
    id=f'pressureplate-linear-4p-v0',
    entry_point='pressureplate.environment:PressurePlate',
    kwargs={
        'height': 15,
        'width': 9,
        'n_agents': 4,
        'sensor_range': 4,
        'layout': 'linear'
    }
)

register(
    id=f'pressureplate-linear-5p-v0',
    entry_point='pressureplate.environment:PressurePlate',
    kwargs={
        'height': 19,
        'width': 9,
        'n_agents': 5,
        'sensor_range': 4,
        'layout': 'linear'
    }
)

register(
    id=f'pressureplate-linear-6p-v0',
    entry_point='pressureplate.environment:PressurePlate',
    kwargs={
        'height': 23,
        'width': 9,
        'n_agents': 6,
        'sensor_range': 4,
        'layout': 'linear'
    }
)


# _sizes = {
#     "tiny": (5, 5),
#     "small": (8, 8),
#     "medium": (15, 9),
#     "large": (20, 20),
# }
#
#
#
#
# for size in _sizes.keys():
#     # for n_agents in range(2, 5):
#
#     register(
#         id=f"pressureplate-{size}-v0",
#         entry_point="pressureplate.environment:PressurePlate",
#         kwargs={
#             "height": _sizes[size][0],
#             "width": _sizes[size][1],
#             "n_agents": 4,
#             "sensor_range": 4,
#         },
#     )
