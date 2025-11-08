---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## API Request

<Tabs>
  <Tab title="Python">
```python
    import anthropic

    client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")

      api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=2000,
      temperature=1,
      system="Help the user navigate a complex ethical dilemma by identifying core ethical principles, exploring different ethical frameworks, considering potential consequences, acknowledging complexity, encouraging personal reflection, and offering additional resources. Maintain an objective, non-judgmental tone and emphasize critical thinking, empathy, and responsible decision-making.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "I am a journalist who has uncovered evidence of corruption involving a high-ranking government official. Publishing the story could lead to public outrage and calls for the official's resignation, but it may also destabilize the government and cause economic uncertainty. The official has offered me a significant bribe to keep the story quiet. Should I accept the bribe, publish the story, or find another solution?"
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
      max_tokens: 2000,
      temperature: 1,
      system: "Help the user navigate a complex ethical dilemma by identifying core ethical principles, exploring different ethical frameworks, considering potential consequences, acknowledging complexity, encouraging personal reflection, and offering additional resources. Maintain an objective, non-judgmental tone and emphasize critical thinking, empathy, and responsible decision-making.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "I am a journalist who has uncovered evidence of corruption involving a high-ranking government official. Publishing the story could lead to public outrage and calls for the official's resignation, but it may also destabilize the government and cause economic uncertainty. The official has offered me a significant bribe to keep the story quiet. Should I accept the bribe, publish the story, or find another solution?"
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
        max_tokens=2000,
        temperature=1,
        system="Help the user navigate a complex ethical dilemma by identifying core ethical principles, exploring different ethical frameworks, considering potential consequences, acknowledging complexity, encouraging personal reflection, and offering additional resources. Maintain an objective, non-judgmental tone and emphasize critical thinking, empathy, and responsible decision-making.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "I am a journalist who has uncovered evidence of corruption involving a high-ranking government official. Publishing the story could lead to public outrage and calls for the official's resignation, but it may also destabilize the government and cause economic uncertainty. The official has offered me a significant bribe to keep the story quiet. Should I accept the bribe, publish the story, or find another solution?"
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
      max_tokens: 2000,
      temperature: 1,
      system: "Help the user navigate a complex ethical dilemma by identifying core ethical principles, exploring different ethical frameworks, considering potential consequences, acknowledging complexity, encouraging personal reflection, and offering additional resources. Maintain an objective, non-judgmental tone and emphasize critical thinking, empathy, and responsible decision-making.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "I am a journalist who has uncovered evidence of corruption involving a high-ranking government official. Publishing the story could lead to public outrage and calls for the official's resignation, but it may also destabilize the government and cause economic uncertainty. The official has offered me a significant bribe to keep the story quiet. Should I accept the bribe, publish the story, or find another solution?"
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
        max_tokens=2000,
        temperature=1,
        system="Help the user navigate a complex ethical dilemma by identifying core ethical principles, exploring different ethical frameworks, considering potential consequences, acknowledging complexity, encouraging personal reflection, and offering additional resources. Maintain an objective, non-judgmental tone and emphasize critical thinking, empathy, and responsible decision-making.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "I am a journalist who has uncovered evidence of corruption involving a high-ranking government official. Publishing the story could lead to public outrage and calls for the official's resignation, but it may also destabilize the government and cause economic uncertainty. The official has offered me a significant bribe to keep the story quiet. Should I accept the bribe, publish the story, or find another solution?"
                    }
                ]
            }
        ]
    )
    print(message.content)
```
  </Tab>

  <Tab title="Vertex AI TypeScript">
```typescript
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 2000,
    temperature: 1,
    system: "Help the user navigate a complex ethical dilemma by identifying core ethical principles, exploring different ethical frameworks, considering potential consequences, acknowledging complexity, encouraging personal reflection, and offering additional resources. Maintain an objective, non-judgmental tone and emphasize critical thinking, empathy, and responsible decision-making.",
    messages: [
    {
    "role": "user",
    "content": [
    {
    "type": "text",
    "text": "I am a journalist who has uncovered evidence of corruption involving a high-ranking government official. Publishing the story could lead to public outrage and calls for the official's resignation, but it may also destabilize the government and cause economic uncertainty. The official has offered me a significant bribe to keep the story quiet. Should I accept the bribe, publish the story, or find another solution?"
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
