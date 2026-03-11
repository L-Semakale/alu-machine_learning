#!/usr/bin/env python3
"""Module to have the trained agent play an episode."""
import numpy as np


def play(env, Q, max_steps=100):
    """Have the trained agent play an episode using the Q-table.

    Args:
        env: The FrozenLakeEnv instance.
        Q: numpy.ndarray containing the Q-table.
        max_steps: Maximum number of steps in the episode.

    Returns:
        The total rewards for the episode.
    """
    state = env.reset()
    total_reward = 0
    env.render()

    for step in range(max_steps):
        action = np.argmax(Q[state, :])
        new_state, reward, done, _ = env.step(action)
        env.render()
        total_reward += reward
        state = new_state

        if done:
            break

    return total_reward
