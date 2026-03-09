"""
TaskFlow Formatting Module — Lab 5, Part 3

This module formats task summaries for display in DevAssist.
The function works but is poorly structured — a refactoring target.
"""


def format_task_summary(task: dict) -> str:
    """
    Format a TaskFlow task dict into a human-readable summary string.

    Args:
        task: A dict with keys: title, status, assignee, priority, due_date.
              Missing keys should use defaults. due_date may be None.

    Returns:
        A formatted multi-line string summary.

    Example:
        >>> format_task_summary({"title": "Fix login bug", "status": "open",
        ...     "assignee": "Alice", "priority": "high", "due_date": "2025-03-15"})
        '[HIGH] Fix login bug\\nAssigned to: Alice\\nStatus: open\\nDue: 2025-03-15'
    """
    # This code works but is messy — good refactoring target
    result = ""
    if "priority" in task:
        p = task["priority"]
        if p == "critical":
            result += "[CRITICAL] "
        elif p == "high":
            result += "[HIGH] "
        elif p == "medium":
            result += "[MEDIUM] "
        elif p == "low":
            result += "[LOW] "
        else:
            result += "[" + str(p).upper() + "] "
    else:
        result += "[MEDIUM] "

    if "title" in task:
        result += task["title"]
    else:
        result += "Untitled Task"

    result += "\n"

    if "assignee" in task:
        result += "Assigned to: " + task["assignee"]
    else:
        result += "Assigned to: Unassigned"

    result += "\n"

    if "status" in task:
        result += "Status: " + task["status"]
    else:
        result += "Status: open"

    if "due_date" in task and task["due_date"] is not None:
        result += "\n" + "Due: " + task["due_date"]

    return result
