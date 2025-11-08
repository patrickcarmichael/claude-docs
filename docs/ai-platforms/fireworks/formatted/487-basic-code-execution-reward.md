---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic Code Execution Reward

```python
from reward_kit import reward_function
from e2b_code_interpreter import CodeInterpreter

@reward_function
def e2b_code_execution_reward(response: str, expected_output: str, **kwargs) -> float:
    """
    Executes code using E2B and compares output to expected result.
    """
    try:
        with CodeInterpreter() as sandbox:
            # Execute the generated code

            execution = sandbox.notebook.exec_cell(response)

            if execution.error:
                return 0.0

            # Get the output

            output = ""
            for result in execution.results:
                if hasattr(result, 'text'):
                    output += result.text
                elif hasattr(result, 'data'):
                    output += str(result.data)

            # Compare with expected output

            if output.strip() == expected_output.strip():
                return 1.0
            else:
                # Partial credit based on similarity

                return calculate_output_similarity(output, expected_output)

    except Exception as e:
        print(f"E2B execution error: {e}")
        return 0.0

def calculate_output_similarity(actual: str, expected: str) -> float:
    """Calculate similarity between outputs."""
    actual = actual.strip()
    expected = expected.strip()

    if not expected:
        return 1.0 if not actual else 0.0

    # Simple word-based similarity

    actual_words = set(actual.lower().split())
    expected_words = set(expected.lower().split())

    if not expected_words:
        return 1.0

    intersection = actual_words & expected_words
    return len(intersection) / len(expected_words)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
