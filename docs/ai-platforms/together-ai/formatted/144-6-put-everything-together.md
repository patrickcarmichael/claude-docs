---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 6. Put everything together

Finally we put everything together and let the AI assistant upload the data, run an analysis, and generate a PNG file with a chart. You can update the task for the assistant in this step. If you decide to change the CSV file you are using, don't forget to update the prompt too.
```py
with CodeInterpreter(api_key=E2B_API_KEY) as code_interpreter:
    # Upload the dataset to the code interpreter sandbox

    upload_dataset(code_interpreter)

    code_results = chat_with_llm(
        code_interpreter,
        "Make a chart showing linear regression of the relationship between GDP per capita and life expectancy from the data. Filter out any missing values or values in wrong format.",
    )
    if code_results:
        first_result = code_results[0]
    else:
        raise Exception("No code interpreter results")


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
