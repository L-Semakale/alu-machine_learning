#!/usr/bin/env python3
"""Module to load the FrozenLake environment from OpenAI Gym."""
import gym


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """Load the pre-made FrozenLakeEnv environment from OpenAI's gym.

    Args:
        desc: None or a list of lists containing a custom description
              of the map to load for the environment.
        map_name: None or a string containing the pre-made map to load.
        is_slippery: Boolean to determine if the ice is slippery.

    Returns:
        The FrozenLake environment instance.
    """
    env = gym.make(
        'FrozenLake-v0',
        desc=desc,
        map_name=map_name,
        is_slippery=is_slippery
    )
    return env
