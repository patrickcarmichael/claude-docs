---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## API Request

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
      temperature=0.5,
      system="Your task is to generate a series of thoughtful, open-ended questions for an interview based on the given context. The questions should be designed to elicit insightful and detailed responses from the interviewee, allowing them to showcase their knowledge, experience, and critical thinking skills. Avoid yes/no questions or those with obvious answers. Instead, focus on questions that encourage reflection, self-assessment, and the sharing of specific examples or anecdotes.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "You are interviewing a candidate for a marketing manager position at a well-established e-commerce company. The ideal candidate should have experience developing and executing multi-channel marketing campaigns, strong analytical skills, and the ability to collaborate effectively with cross-functional teams. They should also be passionate about staying up-to-date with the latest marketing trends and technologies."
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
      temperature: 0.5,
      system: "Your task is to generate a series of thoughtful, open-ended questions for an interview based on the given context. The questions should be designed to elicit insightful and detailed responses from the interviewee, allowing them to showcase their knowledge, experience, and critical thinking skills. Avoid yes/no questions or those with obvious answers. Instead, focus on questions that encourage reflection, self-assessment, and the sharing of specific examples or anecdotes.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "You are interviewing a candidate for a marketing manager position at a well-established e-commerce company. The ideal candidate should have experience developing and executing multi-channel marketing campaigns, strong analytical skills, and the ability to collaborate effectively with cross-functional teams. They should also be passionate about staying up-to-date with the latest marketing trends and technologies."
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
        temperature=0.5,
        system="Your task is to generate a series of thoughtful, open-ended questions for an interview based on the given context. The questions should be designed to elicit insightful and detailed responses from the interviewee, allowing them to showcase their knowledge, experience, and critical thinking skills. Avoid yes/no questions or those with obvious answers. Instead, focus on questions that encourage reflection, self-assessment, and the sharing of specific examples or anecdotes.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "You are interviewing a candidate for a marketing manager position at a well-established e-commerce company. The ideal candidate should have experience developing and executing multi-channel marketing campaigns, strong analytical skills, and the ability to collaborate effectively with cross-functional teams. They should also be passionate about staying up-to-date with the latest marketing trends and technologies."
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
    temperature: 0.5,
    system: "Your task is to generate a series of thoughtful, open-ended questions for an interview based on the given context. The questions should be designed to elicit insightful and detailed responses from the interviewee, allowing them to showcase their knowledge, experience, and critical thinking skills. Avoid yes/no questions or those with obvious answers. Instead, focus on questions that encourage reflection, self-assessment, and the sharing of specific examples or anecdotes.",
    messages: [
    {
    "role": "user",
    "content": [
    {
    "type": "text",
    "text": "You are interviewing a candidate for a marketing manager position at a well-established e-commerce company. The ideal candidate should have experience developing and executing multi-channel marketing campaigns, strong analytical skills, and the ability to collaborate effectively with cross-functional teams. They should also be passionate about staying up-to-date with the latest marketing trends and technologies."
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
        temperature=0.5,
        system="Your task is to generate a series of thoughtful, open-ended questions for an interview based on the given context. The questions should be designed to elicit insightful and detailed responses from the interviewee, allowing them to showcase their knowledge, experience, and critical thinking skills. Avoid yes/no questions or those with obvious answers. Instead, focus on questions that encourage reflection, self-assessment, and the sharing of specific examples or anecdotes.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "You are interviewing a candidate for a marketing manager position at a well-established e-commerce company. The ideal candidate should have experience developing and executing multi-channel marketing campaigns, strong analytical skills, and the ability to collaborate effectively with cross-functional teams. They should also be passionate about staying up-to-date with the latest marketing trends and technologies."
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
      temperature: 0.5,
      system: "Your task is to generate a series of thoughtful, open-ended questions for an interview based on the given context. The questions should be designed to elicit insightful and detailed responses from the interviewee, allowing them to showcase their knowledge, experience, and critical thinking skills. Avoid yes/no questions or those with obvious answers. Instead, focus on questions that encourage reflection, self-assessment, and the sharing of specific examples or anecdotes.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "You are interviewing a candidate for a marketing manager position at a well-established e-commerce company. The ideal candidate should have experience developing and executing multi-channel marketing campaigns, strong analytical skills, and the ability to collaborate effectively with cross-functional teams. They should also be passionate about staying up-to-date with the latest marketing trends and technologies."
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
