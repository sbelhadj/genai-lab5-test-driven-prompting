# Lab 5 — Test-Driven Prompting

## Student Instructions

**Module:** 5 — LLMs for Software Engineering | **Duration:** 90 min | **Pair programming**

---

## Context

DevAssist needs to help the TaskFlow team add features and improve code quality. You'll practice **Test-Driven Prompting**: tests are the oracle, the model is the proposal engine. You write specs + tests first, prompt the model to generate implementations, run tests, iterate until they pass.

---

## Lab Structure

| Phase | Time | Activity |
|-------|------|----------|
| Part 1: TDP — merge_intervals | 40 min | Write tests → prompt → run → iterate |
| Part 2: AI test gen + refactoring | 25 min | Generate tests for existing code + refactor |
| Part 3: Refactor with safety net | 10 min | Refactor format_task_summary, existing tests must pass |
| Wrap-up | 15 min | Complete review.md + iteration_log.md |

---

## Deliverables

| # | What | Where |
|---|------|-------|
| 1 | Completed notebook | `lab5_test_driven_prompting.ipynb` |
| 2 | Your test suite for merge_intervals | `tests/test_intervals.py` |
| 3 | Working implementation | `taskflow/intervals.py` |
| 4 | AI code review | `review.md` |
| 5 | Prompt iteration log | `iteration_log.md` |

---

## Evaluation Criteria

| Criterion | Weight |
|-----------|--------|
| Mechanistic understanding (why AI code fails, token ≠ semantic correctness) | 25% |
| Prompt quality (TDP prompts, iteration reasoning) | 25% |
| Evaluation & verification (test quality, coverage, critical review of AI tests) | 20% |
| Software engineering (tests-first discipline, clean code, git hygiene) | 20% |
| Responsibility & security (AI code review honesty, limitations awareness) | 10% |

---

*Lab 5 of 8 — DevAssist / TaskFlow Lab Series*
