---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 1 - User configures the request to the model

The developer provides a few things to the model:

* A system instruction (preamble) containing instructions about the task and the desired style for the output.
* The user request.
* A list of tools to the model.
* (Optionally) a chat history for the model to work with.

You can specify one or many tools to the model. Every tool needs to be described with a JSON schema, indicating the tool name, description, and parameters (code snippets below).

In our example, we provide two tools to the model: `daily_sales_report` and `product_catalog`.
```python PYTHON
tools = [
    {
        "name": "query_daily_sales_report",
        "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
        "parameter_definitions": {
            "day": {
                "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
                "type": "str",
                "required": True
            }
        }
    },
    {
        "name": "query_product_catalog",
        "description": "Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.",
        "parameter_definitions": {
            "category": {
                "description": "Retrieves product information data for all products in this category.",
                "type": "str",
                "required": True
            }
        }
    }
]
```
Now let's define the user request.

In our example we'll use: "Can you provide a sales summary for 29th September 2023, and also give me the details of all products in the 'Electronics' category that were sold that day, including their prices and stock levels?"

Only a language model with Tool Use can answer this request: it requires looking up information in the right external tools (step 2), and then providing a final answer based on the tool results (step 4).
```python PYTHON
preamble = """

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
