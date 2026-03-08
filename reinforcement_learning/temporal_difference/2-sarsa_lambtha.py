#!/usr/bin/env python3
"""SARSA(lambda) algorithm"""
import numpy as np


def sarsa_lambtha(env, Q, lambtha, episodes=5000, max_steps=100,
                  alpha=0.1, gamma=0.99, epsilon=1,
                  min_epsilon=0.1, epsilon_decay=0.05):
    """Performs SARSA(lambda)
    Returns: Q, the updated Q table
    """
    def epsilon_greedy(state):
        """Selects action using epsilon-greedy policy"""
        if np.random.uniform() < epsilon:
            return env.action_space.sample()
        return np.argmax(Q[state])

    for _ in range(episodes):
        state = env.reset()
        action = epsilon_greedy(state)
        eligibility = np.zeros_like(Q)

        for _ in range(max_steps):
            next_state, reward, done, _ = env.step(action)
            next_action = epsilon_greedy(next_state)

            delta = reward + gamma * Q[next_state, next_action] - \
                Q[state, action]
            eligibility[state, action] += 1
            Q += alpha * delta * eligibility
            eligibility *= gamma * lambtha

            state = next_state
            action = next_action
            if done:
                break

        epsilon = max(min_epsilon, epsilon - epsilon_decay)

    return Q
