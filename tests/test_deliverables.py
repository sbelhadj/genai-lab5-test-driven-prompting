"""Auto-grading: Lab 5 deliverable checks."""
import pytest, json, os

BASE = os.path.join(os.path.dirname(__file__), "..")

class TestFiles:
    def test_notebook(self):
        assert os.path.exists(os.path.join(BASE, "lab5_test_driven_prompting.ipynb"))
    def test_review(self):
        assert os.path.exists(os.path.join(BASE, "review.md"))
    def test_iteration_log(self):
        assert os.path.exists(os.path.join(BASE, "iteration_log.md"))

class TestReview:
    def test_not_template(self):
        with open(os.path.join(BASE, "review.md")) as f:
            content = f.read()
        assert content.count("TODO") <= 3, "review.md still has TODOs"
    def test_has_analysis(self):
        with open(os.path.join(BASE, "review.md")) as f:
            content = f.read().lower()
        found = [t for t in ["token","attention","probable","test","oracle"] if t in content]
        assert len(found) >= 2

class TestIterationLog:
    def test_not_template(self):
        with open(os.path.join(BASE, "iteration_log.md")) as f:
            content = f.read()
        assert content.count("TODO") <= 3
    def test_has_iterations(self):
        with open(os.path.join(BASE, "iteration_log.md")) as f:
            content = f.read().lower()
        assert "v1" in content or "iteration 1" in content
