---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## File-based Code Evaluation

```python
@reward_function
def file_based_code_reward(response: str, file_operations: list, **kwargs) -> float:
    """
    Evaluates code that performs file operations.
    """
    try:
        with CodeInterpreter() as sandbox:
            # Execute the code

            execution = sandbox.notebook.exec_cell(response)

            if execution.error:
                return 0.0

            score = 0.0
            total_operations = len(file_operations)

            # Check each expected file operation

            for operation in file_operations:
                file_path = operation.get('path', '')
                expected_content = operation.get('content', '')
                operation_type = operation.get('type', 'create')

                if operation_type == 'create':
                    # Check if file was created with correct content

                    try:
                        # Read the file

                        read_execution = sandbox.notebook.exec_cell(f"""
with open('{file_path}', 'r') as f:
    content = f.read()
print(content)
                        """)

                        if not read_execution.error:
                            actual_content = ""
                            for result in read_execution.results:
                                if hasattr(result, 'text'):
                                    actual_content += result.text

                            if actual_content.strip() == expected_content.strip():
                                score += 1.0

                    except Exception:
                        pass

                elif operation_type == 'exists':
                    # Check if file exists

                    check_execution = sandbox.notebook.exec_cell(f"""
import os
print(os.path.exists('{file_path}'))
                    """)

                    if not check_execution.error:
                        for result in check_execution.results:
                            if hasattr(result, 'text') and 'True' in result.text:
                                score += 1.0
                                break

            return score / total_operations if total_operations > 0 else 0.0

    except Exception as e:
        print(f"E2B execution error: {e}")
        return 0.0
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
