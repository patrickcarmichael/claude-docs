---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## The system prompt, if present, must always be at the beginning

system_prompt = (
    "Read the story and extract answers for the questions.\nStory: {}"
)


def map_fields(row):
    # Create system prompt

    messages = [
        {"role": "system", "content": system_prompt.format(row["story"])}
    ]

    # Add user and assistant messages

    for q, a in zip(row["questions"], row["answers"]["input_text"]):
        messages.append({"role": "user", "content": q})
        messages.append({"role": "assistant", "content": a})

    return {"messages": messages}


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
