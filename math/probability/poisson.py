#!/usr/bin/env python3
"""Defines Poisson class that represents Poisson distribution"""

from math import exp, factorial


class Poisson:
    """
    Represents a Poisson distribution.

    Attributes:
        lambtha (float): The expected number of occurrences in a given time frame.

    Methods:
        pmf(k): Calculates the probability mass function at k.
        cdf(k): Calculates the cumulative distribution function at k.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the Poisson distribution.

        Args:
            data (list, optional): List of observed data points.
            lambtha (float, optional): Expected number of occurrences (λ).

        Raises:
            TypeError: If data is not a list.
            ValueError: If data has fewer than two values.
            ValueError: If lambtha is not a positive value.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the PMF (probability mass function) for a given number of successes.

        Args:
            k (int): Number of occurrences (successes).

        Returns:
            float: PMF value for given k.
        """
        try:
            k = int(k)
        except (ValueError, TypeError):
            return 0

        if k < 0:
            return 0

        return ((self.lambtha ** k) * exp(-self.lambtha)) / factorial(k)

    def cdf(self, k):
        """
        Calculates the CDF (cumulative distribution function) for a given number of successes.

        Args:
            k (int): Number of occurrences (successes).

        Returns:
            float: CDF value for given k.
        """
        try:
            k = int(k)
        except (ValueError, TypeError):
            return 0

        if k < 0:
            return 0

        return sum(self.pmf(i) for i in range(k + 1))

    def __repr__(self):
        return f"Poisson distribution with λ = {self.lambtha}"

