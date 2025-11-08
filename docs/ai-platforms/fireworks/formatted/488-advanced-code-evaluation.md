---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Advanced Code Evaluation

```python
@reward_function
def advanced_code_evaluation(response: str, test_cases: list, **kwargs) -> float:
    """
    Evaluates code against multiple test cases using E2B.
    """
    if not test_cases:
        return 0.0

    passed_tests = 0
    total_tests = len(test_cases)

    try:
        with CodeInterpreter() as sandbox:
            # First, execute the response code to define functions/variables

            setup_execution = sandbox.notebook.exec_cell(response)

            if setup_execution.error:
                return 0.0

            # Run each test case

            for test_case in test_cases:
                test_code = test_case.get('code', '')
                expected_output = test_case.get('expected', '')

                test_execution = sandbox.notebook.exec_cell(test_code)

                if test_execution.error:
                    continue

                # Check output

                actual_output = ""
                for result in test_execution.results:
                    if hasattr(result, 'text'):
                        actual_output += result.text

                if actual_output.strip() == expected_output.strip():
                    passed_tests += 1

    except Exception as e:
        print(f"E2B execution error: {e}")
        return 0.0

    return passed_tests / total_tests
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
