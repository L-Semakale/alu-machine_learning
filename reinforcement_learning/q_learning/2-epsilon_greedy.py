#!/usr/bin/env python3
"""Module for epsilon-greedy action selection."""
import numpy as np


def epsilon_greedy(Q, state, epsilon):
    """Use epsilon-greedy to determine the next action.

    Args:
        Q: numpy.ndarray containing the Q-table.
        state: The current state.
        epsilon: The epsilon value for exploration vs exploitation.

    Returns:
        The next action index.
    """
    p = np.random.uniform(0, 1)
    if p > epsilon:
        action = np.argmax(Q[state, :])
    else:
        action = np.random.randint(0, Q.shape[1])
    return action
