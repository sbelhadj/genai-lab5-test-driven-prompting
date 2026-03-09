# Lab 5 — Teacher Solution & Answer Key

## Test-Driven Prompting — Instructor Copy

**CONFIDENTIAL**

---

## 1. Part 1: merge_intervals — Reference Solution

### Reference test suite (what students should write)

```python
def test_basic_merge():
    assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]

def test_no_overlap():
    assert merge_intervals([[1,2],[4,5],[7,8]]) == [[1,2],[4,5],[7,8]]

def test_all_overlap():
    assert merge_intervals([[1,4],[2,5],[3,6]]) == [[1,6]]

def test_subset():
    assert merge_intervals([[1,10],[3,5]]) == [[1,10]]

def test_touching():
    assert merge_intervals([[1,3],[3,5]]) == [[1,5]]

def test_single():
    assert merge_intervals([[1,5]]) == [[1,5]]

def test_empty():
    assert merge_intervals([]) == []

def test_unsorted():
    assert merge_intervals([[5,8],[1,3],[2,6]]) == [[1,8]]

def test_duplicates():
    assert merge_intervals([[1,3],[1,3]]) == [[1,3]]

def test_negatives():
    assert merge_intervals([[-5,-1],[0,3],[-3,2]]) == [[-5,3]]
```

### Reference implementation

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

### Common model failures

| Failure | Root Cause | Fix Strategy |
|---------|-----------|-------------|
| Doesn't sort first | Prompt didn't specify unsorted input | Add unsorted example |
| Uses `<` instead of `<=` for touching | Ambiguous spec on touching intervals | Explicitly state touching should merge |
| Chained overlap miss | O(n²) pairwise approach instead of sort-and-scan | Add "sort first" constraint in prompt |
| Mutates input | Model doesn't copy the input | Usually harmless but add constraint if needed |

---

## 2. Part 2: AI Test Generation — Expected Model Behavior

- Model typically generates 5-7 tests, misses: single element, mixed pos/neg
- Common model error in refactoring: forgetting `n != first` check in O(n) version
- The `find_second_largest` function is correct — the refactoring target is algorithmic improvement

---

## 3. Part 3: Refactoring — Expected Outcome

The model should produce something like:
```python
def format_task_summary(task):
    priority = task.get('priority', 'medium').upper()
    title = task.get('title', 'Untitled Task')
    assignee = task.get('assignee', 'Unassigned')
    status = task.get('status', 'open')
    due_date = task.get('due_date')
    lines = [f'[{priority}] {title}', f'Assigned to: {assignee}', f'Status: {status}']
    if due_date is not None:
        lines.append(f'Due: {due_date}')
    return '\n'.join(lines)
```

Common failure: model may not handle the `None` due_date correctly, or may change the priority casing behavior.

---

## 4. Grading Notes

- **Part 1 weight:** 40%. Grade test quality (coverage, edge cases) AND iteration discipline (tests first, not code first). Students who prompt before writing tests should lose points.
- **Part 2 weight:** 30%. Grade critical evaluation — students who blindly accept AI tests score lower than students who identify gaps.
- **Part 3 weight:** 15%. All 13 tests must pass. Grade refactoring quality.
- **Deliverables weight:** 15%. review.md + iteration_log.md quality.

---

*CONFIDENTIAL — Lab 5 Teacher Solution*
