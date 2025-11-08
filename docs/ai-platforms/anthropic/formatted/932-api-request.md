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
        temperature=1,
        system="Your task is to compose a comprehensive company memo based on the provided key points. The memo should be written in a professional tone, addressing all the relevant information in a clear and concise manner. Use appropriate formatting, such as headings, subheadings, and bullet points, to organize the content effectively. Ensure that the memo is well-structured, coherent, and easy to understand for the intended audience.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "- Announcement of a new employee wellness program: \"Fit4Success\"  \n- Program objectives: promote physical and mental well-being, reduce stress, and increase productivity  \n- Components: on-site fitness classes, healthy meal options, mental health resources, and wellness workshops  \n- Partnership with local gyms and wellness centers for discounted memberships  \n- Incentives for participation: fitness trackers, wellness points, and prize drawings  \n- Program launch date: June 1, 2023  \n- Enrollment process: online registration through company intranet  \n- Program coordinators: Human Resources and Employee Engagement teams"
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
      temperature: 1,
      system: "Your task is to compose a comprehensive company memo based on the provided key points. The memo should be written in a professional tone, addressing all the relevant information in a clear and concise manner. Use appropriate formatting, such as headings, subheadings, and bullet points, to organize the content effectively. Ensure that the memo is well-structured, coherent, and easy to understand for the intended audience.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "- Announcement of a new employee wellness program: \"Fit4Success\"  \n- Program objectives: promote physical and mental well-being, reduce stress, and increase productivity  \n- Components: on-site fitness classes, healthy meal options, mental health resources, and wellness workshops  \n- Partnership with local gyms and wellness centers for discounted memberships  \n- Incentives for participation: fitness trackers, wellness points, and prize drawings  \n- Program launch date: June 1, 2023  \n- Enrollment process: online registration through company intranet  \n- Program coordinators: Human Resources and Employee Engagement teams"
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
    temperature=1,
    system="Your task is to compose a comprehensive company memo based on the provided key points. The memo should be written in a professional tone, addressing all the relevant information in a clear and concise manner. Use appropriate formatting, such as headings, subheadings, and bullet points, to organize the content effectively. Ensure that the memo is well-structured, coherent, and easy to understand for the intended audience.",
    messages=[
    {
    "role": "user",
    "content": [
    {
    "type": "text",
    "text": "- Announcement of a new employee wellness program: \"Fit4Success\" \n- Program objectives: promote physical and mental well-being, reduce stress, and increase productivity \n- Components: on-site fitness classes, healthy meal options, mental health resources, and wellness workshops \n- Partnership with local gyms and wellness centers for discounted memberships \n- Incentives for participation: fitness trackers, wellness points, and prize drawings \n- Program launch date: June 1, 2023 \n- Enrollment process: online registration through company intranet \n- Program coordinators: Human Resources and Employee Engagement teams"
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
      temperature: 1,
      system: "Your task is to compose a comprehensive company memo based on the provided key points. The memo should be written in a professional tone, addressing all the relevant information in a clear and concise manner. Use appropriate formatting, such as headings, subheadings, and bullet points, to organize the content effectively. Ensure that the memo is well-structured, coherent, and easy to understand for the intended audience.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "- Announcement of a new employee wellness program: \"Fit4Success\"  \n- Program objectives: promote physical and mental well-being, reduce stress, and increase productivity  \n- Components: on-site fitness classes, healthy meal options, mental health resources, and wellness workshops  \n- Partnership with local gyms and wellness centers for discounted memberships  \n- Incentives for participation: fitness trackers, wellness points, and prize drawings  \n- Program launch date: June 1, 2023  \n- Enrollment process: online registration through company intranet  \n- Program coordinators: Human Resources and Employee Engagement teams"
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
        temperature=1,
        system="Your task is to compose a comprehensive company memo based on the provided key points. The memo should be written in a professional tone, addressing all the relevant information in a clear and concise manner. Use appropriate formatting, such as headings, subheadings, and bullet points, to organize the content effectively. Ensure that the memo is well-structured, coherent, and easy to understand for the intended audience.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "- Announcement of a new employee wellness program: \"Fit4Success\"  \n- Program objectives: promote physical and mental well-being, reduce stress, and increase productivity  \n- Components: on-site fitness classes, healthy meal options, mental health resources, and wellness workshops  \n- Partnership with local gyms and wellness centers for discounted memberships  \n- Incentives for participation: fitness trackers, wellness points, and prize drawings  \n- Program launch date: June 1, 2023  \n- Enrollment process: online registration through company intranet  \n- Program coordinators: Human Resources and Employee Engagement teams"
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
      temperature: 1,
      system: "Your task is to compose a comprehensive company memo based on the provided key points. The memo should be written in a professional tone, addressing all the relevant information in a clear and concise manner. Use appropriate formatting, such as headings, subheadings, and bullet points, to organize the content effectively. Ensure that the memo is well-structured, coherent, and easy to understand for the intended audience.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "- Announcement of a new employee wellness program: \"Fit4Success\"  \n- Program objectives: promote physical and mental well-being, reduce stress, and increase productivity  \n- Components: on-site fitness classes, healthy meal options, mental health resources, and wellness workshops  \n- Partnership with local gyms and wellness centers for discounted memberships  \n- Incentives for participation: fitness trackers, wellness points, and prize drawings  \n- Program launch date: June 1, 2023  \n- Enrollment process: online registration through company intranet  \n- Program coordinators: Human Resources and Employee Engagement teams"
            }
          ]
        }
      ]
    });
    console.log(msg);
```javascript
  </Tab>
</Tabs>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
