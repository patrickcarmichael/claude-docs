---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Data Analysis Code Evaluation

```python
@reward_function
def data_analysis_reward(response: str, dataset_path: str, expected_insights: list, **kwargs) -> float:
    """
    Evaluates data analysis code by checking insights and outputs.
    """
    try:
        with CodeInterpreter() as sandbox:
            # Upload dataset to sandbox

            with open(dataset_path, 'rb') as f:
                data_file = sandbox.files.write('dataset.csv', f.read())

            # Execute the analysis code

            execution = sandbox.notebook.exec_cell(response)

            if execution.error:
                return 0.0

            score = 0.0

            # Check for expected insights

            output_text = ""
            for result in execution.results:
                if hasattr(result, 'text'):
                    output_text += result.text.lower()

            # Check each expected insight

            for insight in expected_insights:
                if insight.lower() in output_text:
                    score += 1.0

            # Bonus for plots/visualizations

            has_plot = any(
                hasattr(result, 'formats') and 'image/png' in result.formats
                for result in execution.results
            )

            if has_plot:
                score += 0.5

            return min(score / len(expected_insights), 1.0) if expected_insights else 0.0

    except Exception as e:
        print(f"E2B execution error: {e}")
        return 0.0
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
