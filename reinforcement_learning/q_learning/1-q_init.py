#!/usr/bin/env python3
"""Module to initialize the Q-table for Q-learning."""
import numpy as np


def q_init(env):
    """Initialize the Q-table as a matrix of zeros.

    Args:
        env: The FrozenLakeEnv instance.

    Returns:
        Q-table as a numpy.ndarray of zeros with shape
        (num_states, num_actions).
    """
    return np.zeros((env.observation_space.n, env.action_space.n))
