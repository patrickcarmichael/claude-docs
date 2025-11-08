---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Structured Outputs

```python
from pydantic import BaseModel
from openai import OpenAI
import os, json

client = OpenAI(
    api_key=os.environ.get("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1",
)


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday. Answer in JSON",
        },
    ],
    response_format={
        "type": "json_schema",
        "schema": CalendarEvent.model_json_schema(),
    },
)

output = json.loads(completion.choices[0].message.content)
print(json.dumps(output, indent=2))
```

Output:
```text
{
  "name": "Alice and Bob",
  "date": "Friday",
  "participants": [
    "Alice",
    "Bob"
  ]
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
