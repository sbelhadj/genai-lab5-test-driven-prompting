"""
Tests for format_task_summary — Lab 5, Part 3 (PROVIDED)

These tests serve as a safety net for the refactoring exercise.
After refactoring format_task_summary, ALL these tests must still pass.
DO NOT MODIFY these tests.
"""

import pytest
from taskflow.formatting import format_task_summary


class TestFormatTaskSummary:

    def test_full_task(self):
        task = {"title": "Fix login bug", "status": "open",
                "assignee": "Alice", "priority": "high", "due_date": "2025-03-15"}
        result = format_task_summary(task)
        assert "[HIGH] Fix login bug" in result
        assert "Assigned to: Alice" in result
        assert "Status: open" in result
        assert "Due: 2025-03-15" in result

    def test_critical_priority(self):
        task = {"title": "Server down", "priority": "critical",
                "assignee": "Bob", "status": "in_progress"}
        result = format_task_summary(task)
        assert "[CRITICAL]" in result
        assert "Server down" in result

    def test_low_priority(self):
        task = {"title": "Update docs", "priority": "low",
                "assignee": "Carol", "status": "todo"}
        result = format_task_summary(task)
        assert "[LOW]" in result

    def test_medium_priority(self):
        task = {"title": "Refactor utils", "priority": "medium",
                "assignee": "Dave", "status": "open"}
        result = format_task_summary(task)
        assert "[MEDIUM]" in result

    def test_missing_priority_defaults_medium(self):
        task = {"title": "Some task", "assignee": "Eve", "status": "open"}
        result = format_task_summary(task)
        assert "[MEDIUM]" in result

    def test_missing_title_defaults(self):
        task = {"priority": "high", "assignee": "Frank", "status": "open"}
        result = format_task_summary(task)
        assert "Untitled Task" in result

    def test_missing_assignee_defaults(self):
        task = {"title": "Test task", "priority": "high", "status": "open"}
        result = format_task_summary(task)
        assert "Unassigned" in result

    def test_missing_status_defaults_open(self):
        task = {"title": "Test task", "priority": "high", "assignee": "Grace"}
        result = format_task_summary(task)
        assert "Status: open" in result

    def test_no_due_date(self):
        task = {"title": "No deadline", "priority": "low",
                "assignee": "Heidi", "status": "open"}
        result = format_task_summary(task)
        assert "Due:" not in result

    def test_null_due_date(self):
        task = {"title": "Null deadline", "priority": "low",
                "assignee": "Ivan", "status": "open", "due_date": None}
        result = format_task_summary(task)
        assert "Due:" not in result

    def test_empty_task(self):
        result = format_task_summary({})
        assert "[MEDIUM]" in result
        assert "Untitled Task" in result
        assert "Unassigned" in result
        assert "Status: open" in result

    def test_unknown_priority(self):
        task = {"title": "Weird", "priority": "urgent", "assignee": "Jo", "status": "open"}
        result = format_task_summary(task)
        assert "[URGENT]" in result

    def test_multiline_output(self):
        task = {"title": "Test", "priority": "high",
                "assignee": "Kate", "status": "done", "due_date": "2025-04-01"}
        result = format_task_summary(task)
        lines = result.strip().split("\n")
        assert len(lines) == 4  # title, assignee, status, due
