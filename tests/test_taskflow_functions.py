"""
Auto-grading: Lab 5 — Checks that student implementations exist and work.
"""

import pytest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

INTERVALS_AVAILABLE = False
try:
    from taskflow.intervals import merge_intervals
    merge_intervals([[1, 3], [2, 4]])
    INTERVALS_AVAILABLE = True
except (NotImplementedError, ImportError):
    pass


@pytest.mark.skipif(not INTERVALS_AVAILABLE, reason="merge_intervals not implemented")
class TestMergeIntervalsBasic:
    def test_basic(self):
        assert merge_intervals([[1,3],[2,6],[8,10]]) == [[1,6],[8,10]]
    def test_empty(self):
        assert merge_intervals([]) == []
    def test_single(self):
        assert merge_intervals([[1,5]]) == [[1,5]]
    def test_touching(self):
        assert merge_intervals([[1,3],[3,5]]) == [[1,5]]
    def test_unsorted(self):
        assert merge_intervals([[5,8],[1,3],[2,6]]) == [[1,8]]


class TestFormattingStillWorks:
    """Ensure refactoring didn't break format_task_summary."""
    def test_basic(self):
        from taskflow.formatting import format_task_summary
        result = format_task_summary({"title": "Test", "priority": "high",
                                       "assignee": "A", "status": "open"})
        assert "[HIGH]" in result
        assert "Test" in result

    def test_empty(self):
        from taskflow.formatting import format_task_summary
        result = format_task_summary({})
        assert "Untitled Task" in result
