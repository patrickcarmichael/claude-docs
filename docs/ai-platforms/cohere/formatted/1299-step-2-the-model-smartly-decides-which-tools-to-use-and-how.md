---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2 – The model smartly decides which tool(s) to use and how

The model intelligently selects the right tool(s) to call -- and the right parameters for each tool call -- based on the content of the user message.
```python PYTHON
response = co.chat(
    message=message,
    tools=tools,
    preamble=preamble,
    model="command-r"
)


print("The model recommends doing the following tool calls:")
print("\n".join(str(tool_call) for tool_call in response.tool_calls))
```
```
The model recommends doing the following tool calls:
cohere.ToolCall {
	name: query_daily_sales_report
	parameters: {'day': '2023-09-29'}
	generation_id: eaf955e3-623d-4796-bf51-23b07c66ed2c
}
cohere.ToolCall {
	name: query_product_catalog
	parameters: {'category': 'Electronics'}
	generation_id: eaf955e3-623d-4796-bf51-23b07c66ed2c
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
