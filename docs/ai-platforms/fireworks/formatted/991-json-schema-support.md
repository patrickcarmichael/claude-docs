---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## JSON Schema Support

Fireworks supports most [JSON schema specification](https://json-schema.org/specification) constructs:

**Supported:**

* Types: `string`, `number`, `integer`, `boolean`, `object`, `array`, `null`
* Object constraints: `properties`, `required`
* Array constraints: `items`
* Nested schemas: `anyOf`, `$ref`

**Not yet supported:**

* `oneOf` composition
* Length/size constraints (`minLength`, `maxLength`, `minItems`, `maxItems`)
* Regular expressions (`pattern`)

<Tip>
  Fireworks automatically prevents hallucinated fields by treating schemas with `properties` as if `"unevaluatedProperties": false` is set.
</Tip>

<Accordion title="Advanced: Reasoning Model JSON Mode">
  Some models support generating structured JSON outputs with visible reasoning. In this mode, the model's response includes a `<think>...</think>` section showing its reasoning process, followed by the JSON output.

  #### Example Usage

```python
  import os
  import re
  from openai import OpenAI
  from pydantic import BaseModel

  client = OpenAI(
      api_key=os.environ.get("FIREWORKS_API_KEY"),
      base_url="https://api.fireworks.ai/inference/v1"
  )

  # Define the output schema

  class QAResult(BaseModel):
      question: str
      answer: str

  # Make the request

  response = client.chat.completions.create(
      model="accounts/fireworks/models/deepseek-v3p1",
      messages=[{"role": "user", "content": "Who wrote 'Pride and Prejudice'?"}],
      response_format={
          "type": "json_schema",
          "json_schema": {
              "name": "QAResult",
              "schema": QAResult.model_json_schema()
          }
      },
      max_tokens=1000
  )

  # Extract the response content

  response_content = response.choices[0].message.content

  # Extract reasoning (if present)

  reasoning_match = re.search(r"<think>(.*?)</think>", response_content, re.DOTALL)
  reasoning = reasoning_match.group(1).strip() if reasoning_match else None

  # Extract JSON

  json_match = re.search(r"</think>\s*(\{.*\})", response_content, re.DOTALL) if reasoning else re.search(r"(\{.*\})", response_content, re.DOTALL)
  json_str = json_match.group(1).strip() if json_match else "{}"

  # Parse into Pydantic model

  qa_result = QAResult.model_validate_json(json_str)

  if reasoning:
      print("Reasoning:", reasoning)
  print("Result:", qa_result.model_dump_json(indent=2))
```
  #### Use Cases

  Reasoning mode is useful for:

  * **Debugging**: Understanding why the model generated specific outputs
  * **Auditing**: Documenting the decision-making process
  * **Complex tasks**: Scenarios where the reasoning is as valuable as the final answer

  #### Additional Examples

  <CardGroup cols={2}>
    <Card title="Computer Specs with Reasoning" icon="square-1" href="https://colab.research.google.com/drive/1zBK1nDITDNOx7oRWxh19C5_sNSh64PKM?usp=sharing">
      Generate structured PC specifications with reasoning
    </Card>

    <Card title="Healthcare Records with Reasoning" icon="square-2" href="https://colab.research.google.com/drive/1njzOgHWgguSuA732RYROJDiCua3hGO_R?usp=sharing">
      Structure patient records with AI-generated reasoning
    </Card>
  </CardGroup>
</Accordion>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
