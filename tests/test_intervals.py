"""
Tests for merge_intervals — Lab 5, Part 1

STUDENTS: Write these tests BEFORE prompting the model.
These tests define "correct." The model generates "probable."
Your tests determine if "probable" is also "correct."

Run with: pytest tests/test_intervals.py -v
"""

import pytest
from taskflow.intervals import merge_intervals


# === NORMAL CASES ===

def test_basic_merge():
    """Overlapping intervals should be merged."""
    # TODO: assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    pass


def test_no_overlap():
    """Non-overlapping intervals remain unchanged."""
    # TODO: assert merge_intervals([[1,2],[4,5],[7,8]]) == [[1,2],[4,5],[7,8]]
    pass


def test_all_overlap():
    """All intervals overlap into one."""
    # TODO: assert merge_intervals([[1,4],[2,5],[3,6]]) == [[1,6]]
    pass


def test_subset_interval():
    """One interval is a subset of another."""
    # TODO: assert merge_intervals([[1,10],[3,5]]) == [[1,10]]
    pass


# === EDGE CASES ===

def test_touching_intervals():
    """Touching intervals [1,3] and [3,5] should merge."""
    # TODO: assert merge_intervals([[1,3],[3,5]]) == [[1,5]]
    pass


def test_single_interval():
    """Single interval is returned as-is."""
    # TODO: assert merge_intervals([[1,5]]) == [[1,5]]
    pass


def test_empty_input():
    """Empty list returns empty list."""
    # TODO: assert merge_intervals([]) == []
    pass


def test_unsorted_input():
    """Input intervals are NOT pre-sorted."""
    # TODO: assert merge_intervals([[5,8],[1,3],[2,6]]) == [[1,8]]
    pass


# === ADDITIONAL (students should add more) ===

def test_duplicate_intervals():
    """Duplicate intervals should merge."""
    # TODO
    pass


def test_negative_values():
    """Negative interval values should work."""
    # TODO
    pass
