# Lab 5 — Test-Driven Prompting

**Generative AI & Prompt Engineering — A Mechanistic Approach**

Module 5: LLMs for Software Engineering | Duration: 90 minutes

---

## Overview

In this lab you practice **Test-Driven Prompting (TDP)**: write tests first, prompt the model to generate implementations, run tests, iterate until they pass. You'll also use the model for test generation and guided refactoring — always with tests as the external oracle.

**Core principle:** *The model proposes, tests dispose. "Probable" code is not "correct" code.*

---

## Repository Structure

```
genai-lab5-test-driven-prompting/
├── lab5_test_driven_prompting.ipynb    # ← YOUR MAIN WORKSPACE
├── taskflow/
│   ├── __init__.py
│   ├── intervals.py                    # Part 1: YOUR generated merge_intervals()
│   ├── stats.py                        # Part 2: find_second_largest (has subtle edge)
│   └── formatting.py                   # Part 3: format_task_summary (refactoring target)
├── tests/
│   ├── test_intervals.py              # Part 1: YOUR tests (write before prompting)
│   ├── test_stats.py                  # Part 2: AI-generated tests (review critically)
│   ├── test_formatting.py             # Part 3: Provided tests (safety net for refactoring)
│   ├── test_taskflow_functions.py     # Auto-graded: checks implementations pass
│   └── test_deliverables.py           # Auto-graded: checks files exist
├── utils/
│   ├── generation_utils.py
│   └── code_runner.py                 # run_tests() — execute pytest programmatically
├── data/
│   └── precomputed_outputs.json
├── review.md                          # ← YOUR DELIVERABLE: AI code review
└── iteration_log.md                   # ← YOUR DELIVERABLE: prompt iteration log
```

---

## What to Do

1. **Part 1 (40 min):** TDP cycle on `merge_intervals` — write tests → prompt → run → iterate
2. **Part 2 (25 min):** AI test generation for `find_second_largest` + guided refactoring
3. **Part 3 (10 min):** Refactor `format_task_summary` with existing test safety net
4. Fill in `review.md` and `iteration_log.md`

---

*Lab 5 of 8 — DevAssist / TaskFlow Lab Series*
