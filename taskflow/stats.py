"""
TaskFlow Statistics Module — Lab 5, Part 2

This module contains utility functions for TaskFlow analytics.
The find_second_largest function works correctly but uses O(n log n) sorting.
Students will use AI to generate tests, then refactor to O(n).
"""


def find_second_largest(numbers: list[int]) -> int:
    """
    Return the second largest unique value in the list.

    Args:
        numbers: A list of integers with at least 2 unique values.

    Returns:
        The second largest unique integer.

    Raises:
        ValueError: If the list has fewer than 2 unique values.

    Examples:
        >>> find_second_largest([3, 1, 4, 1, 5, 9])
        5
        >>> find_second_largest([10, 10, 5])
        5
    """
    if len(set(numbers)) < 2:
        raise ValueError("Need at least 2 unique values")

    unique = sorted(set(numbers), reverse=True)
    return unique[1]
