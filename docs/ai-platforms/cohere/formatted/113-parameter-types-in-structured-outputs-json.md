---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Parameter Types in Structured Outputs (JSON)

> This page shows usage examples of the JSON Schema parameter types supported in Structured Outputs (JSON).

This page provides usage examples of the JSON Schema parameters that are supported in [Structured Outputs (JSON)](https://docs.cohere.com/v2/docs/structured-outputs).

Note: Using Structured Outputs (JSON), the outputs are guaranteed to follow the schema for the tool name, parameter name, parameter data types, and the list of required parameters.

<Accordion title="Helper code">
  The examples on this page each provide a `response_format` schema and a `message` (the user message). To get an output, pass those values to a Chat endpoint call, as shown in the helper code below.
```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="YOUR API KEY")

  res = co.chat(
      # The model name. Example: command-a-03-2025

      model="MODEL_NAME",
      # The user message. Optional - you can first add a `system_message` role

      messages=[
          {
              "role": "user",
              "content": message,
          }
      ],
      # The schema that you define

      response_format=response_format,
      # Typically, you'll need a low temperature for more deterministic outputs

      temperature=0,
  )

  print(res.message.content[0].text)
```
</Accordion>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
