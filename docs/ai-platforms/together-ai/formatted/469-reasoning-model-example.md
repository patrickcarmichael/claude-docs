---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Reasoning model example

You can also extract structured outputs from some reasoning models such as `DeepSeek-R1-0528`.

Below we ask the model to solve a math problem step-by-step showing its work:
```py
import json
import together
from pydantic import BaseModel, Field

client = together.Together()


class Step(BaseModel):
    explanation: str
    output: str


class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str


completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
        },
        {"role": "user", "content": "how can I solve 8x + 7 = -23"},
    ],
    response_format={
        "type": "json_schema",
        "schema": MathReasoning.model_json_schema(),
    },
)

math_reasoning = json.loads(completion.choices[0].message.content)

print(json.dumps(math_reasoning, indent=2))
```

Example output:
```json
{
  "steps": [
    {
      "explanation": "To solve the equation 8x + 7 = -23, I need to isolate the variable x on one side of the equation. That means I'll have to get rid of the constant term and the coefficient of x.",
      "output": ""
    },
    {
      "explanation": "First, I'll eliminate the constant term on the left side. Since it's +7, I can subtract 7 from both sides of the equation. This keeps the equation balanced.",
      "output": "8x + 7 - 7 = -23 - 7"
    },
    {
      "explanation": "Now, simplifying both sides: on the left, 7 - 7 is 0, so I'm left with 8x. On the right, -23 - 7 is -30.",
      "output": "8x = -30"
    },
    {
      "explanation": "Next, I need to solve for x. Since x is multiplied by 8, I should divide both sides by 8 to isolate x.",
      "output": "8x / 8 = -30 / 8"
    },
    {
      "explanation": "Simplifying that, 8x divided by 8 is just x. And -30 divided by 8 is -30/8.",
      "output": "x = -30/8"
    },
    {
      "explanation": "I can simplify this fraction. Both 30 and 8 are divisible by 2. So, -30 divided by 2 is -15, and 8 divided by 2 is 4.",
      "output": "x = -15/4"
    },
    {
      "explanation": "I can also write this as a mixed number or decimal, but the fraction is already simplified. -15/4 is -3.75, but I'll keep it as a fraction since it's exact.",
      "output": "x = -15/4"
    }
  ],
  "final_answer": "x = -\\frac{15}{4}"
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
