---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## API Request

```python
  import anthropic

  client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")

      api_key="my_api_key",
  )
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=0,
      system="Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea."
                  }
              ]
          }
      ]
  )
  print(message.content)
```
```typescript
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
    apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
  });

  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1000,
    temperature: 0,
    system: "Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea."
          }
        ]
      }
    ]
  });
  console.log(msg);
```
```python AWS Bedrock Python theme={null}
  from anthropic import AnthropicBedrock

  # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock

  # for authentication options

  client = AnthropicBedrock()

  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=1000,
      temperature=0,
      system="Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea."
                  }
              ]
          }
      ]
  )
  print(message.content)
```
```typescript AWS Bedrock TypeScript theme={null}
  import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

  // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  // for authentication options
  const client = new AnthropicBedrock();

  const msg = await client.messages.create({
    model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens: 1000,
    temperature: 0,
    system: "Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea."
          }
        ]
      }
    ]
  });
  console.log(msg);
```
```python Vertex AI Python theme={null}
  from anthropic import AnthropicVertex

  client = AnthropicVertex()

  message = client.messages.create(
      model="claude-sonnet-4@20250514",
      max_tokens=1000,
      temperature=0,
      system="Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea."
                  }
              ]
          }
      ]
  )
  print(message.content)
```
```typescript Vertex AI TypeScript theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
  // Additionally goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex();

  const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 1000,
    temperature: 0,
    system: "Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea."
          }
        ]
      }
    ]
  });
  console.log(msg);
```python


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
