---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Domain-Specific Evaluation

Create reward functions tailored to specific domains:
```python
@reward_function
def code_quality_reward(response: str, expected_response: str, **kwargs) -> float:
    """
    Evaluates code responses considering multiple quality factors.
    """
    import ast

    score = 0.0

    # Check if code is syntactically valid

    try:
        ast.parse(response)
        score += 0.3  # Syntax correctness

    except SyntaxError:
        return 0.0  # Invalid syntax gets zero score

    # Check for best practices

    if "def " in response:  # Function definition

        score += 0.2

    if "# " in response or '"""' in response:  # Comments/docstrings

        score += 0.1

    # Check for specific patterns

    if "import " in response and "from " in response:
        score += 0.1  # Good import practices

    # Length consideration (not too short, not too long)

    lines = response.split('\n')
    if 5 <= len(lines) <= 50:
        score += 0.1

    # Functional correctness (if test cases available)

    test_cases = kwargs.get('test_cases', [])
    if test_cases:
        correctness_score = evaluate_code_correctness(response, test_cases)
        score += 0.2 * correctness_score

    return min(score, 1.0)

def evaluate_code_correctness(code: str, test_cases: list) -> float:
    """Helper to evaluate code correctness against test cases."""
    # This would implement actual code execution and testing

    # For safety, this is a placeholder

    return 0.8  # Placeholder score

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
