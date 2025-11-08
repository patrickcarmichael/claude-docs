---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## API request

<Tabs>
  <Tab title="Python">
```Python
    import anthropic

    client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")

      api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=0,
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints."
            }
          ]
        }
      ]
    )
    print(message.content)
```
  </Tab>

  <Tab title="TypeScript">
```TypeScript
    import Anthropic from "@anthropic-ai/sdk";

    const anthropic = new Anthropic({
      apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
    });

    const msg = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1000,
      temperature: 0,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints."
            }
          ]
        }
      ]
    });
    console.log(msg);
```
  </Tab>

  <Tab title="AWS Bedrock Python">
```Python
    from anthropic import AnthropicBedrock

    # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock

    # for authentication options

    client = AnthropicBedrock()

    message = client.messages.create(
        model="anthropic.claude-sonnet-4-5-20250929-v1:0",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints."
                    }
                ]
            }
        ]
    )
    print(message.content)
```
  </Tab>

  <Tab title="AWS Bedrock TypeScript">
```TypeScript
    import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

    // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    // for authentication options
    const client = new AnthropicBedrock();

    const msg = await client.messages.create({
      model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens: 1000,
      temperature: 0,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints."
            }
          ]
        }
      ]
    });
    console.log(msg);
```
  </Tab>

  <Tab title="Vertex AI Python">
```Python
    from anthropic import AnthropicVertex

    client = AnthropicVertex()

    message = client.messages.create(
        model="claude-sonnet-4@20250514",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints."
                    }
                ]
            }
        ]
    )
    print(message.content)
```
  </Tab>

  <Tab title="Vertex AI TypeScript">
```TypeScript
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
      model: "claude-sonnet-4@20250514",
      max_tokens: 1000,
      temperature: 0,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints."
            }
          ]
        }
      ]
    });
    console.log(msg);
```
  </Tab>
</Tabs>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
