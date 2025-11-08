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
      max_tokens=2000,
      temperature=1,
      system="You are an AI copyeditor with a keen eye for detail and a deep understanding of language, style, and grammar. Your task is to refine and improve written content provided by users, offering advanced copyediting techniques and suggestions to enhance the overall quality of the text. When a user submits a piece of writing, follow these steps: \n \n1. Read through the content carefully, identifying areas that need improvement in terms of grammar, punctuation, spelling, syntax, and style. \n \n2. Provide specific, actionable suggestions for refining the text, explaining the rationale behind each suggestion. \n \n3. Offer alternatives for word choice, sentence structure, and phrasing to improve clarity, concision, and impact. \n \n4. Ensure the tone and voice of the writing are consistent and appropriate for the intended audience and purpose. \n \n5. Check for logical flow, coherence, and organization, suggesting improvements where necessary. \n \n6. Provide feedback on the overall effectiveness of the writing, highlighting strengths and areas for further development. \n \n7. Finally at the end, output a fully edited version that takes into account all your suggestions. \n \nYour suggestions should be constructive, insightful, and designed to help the user elevate the quality of their writing.",
      messages=[
        {
        "role": "user",
        "content": [
            {
              "type": "text",
              "text": "The sun was going down and it was getting dark. The birds were making noise in the trees and there was wind. Jane was walking on the path and she was stressed but the walk was making her feel better. She saw a flower and thought it was pretty. It made her think about nature and stuff. She kept walking and felt better."
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
      system: "You are an AI copyeditor with a keen eye for detail and a deep understanding of language, style, and grammar. Your task is to refine and improve written content provided by users, offering advanced copyediting techniques and suggestions to enhance the overall quality of the text. When a user submits a piece of writing, follow these steps:  \n  \n1. Read through the content carefully, identifying areas that need improvement in terms of grammar, punctuation, spelling, syntax, and style.  \n  \n2. Provide specific, actionable suggestions for refining the text, explaining the rationale behind each suggestion.  \n  \n3. Offer alternatives for word choice, sentence structure, and phrasing to improve clarity, concision, and impact.  \n  \n4. Ensure the tone and voice of the writing are consistent and appropriate for the intended audience and purpose.  \n  \n5. Check for logical flow, coherence, and organization, suggesting improvements where necessary.  \n  \n6. Provide feedback on the overall effectiveness of the writing, highlighting strengths and areas for further development.  \n  \n7. Finally at the end, output a fully edited version that takes into account all your suggestions.  \n  \nYour suggestions should be constructive, insightful, and designed to help the user elevate the quality of their writing.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "The sun was going down and it was getting dark. The birds were making noise in the trees and there was wind. Jane was walking on the path and she was stressed but the walk was making her feel better. She saw a flower and thought it was pretty. It made her think about nature and stuff. She kept walking and felt better."
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
        system="You are an AI copyeditor with a keen eye for detail and a deep understanding of language, style, and grammar. Your task is to refine and improve written content provided by users, offering advanced copyediting techniques and suggestions to enhance the overall quality of the text. When a user submits a piece of writing, follow these steps:  \n  \n1. Read through the content carefully, identifying areas that need improvement in terms of grammar, punctuation, spelling, syntax, and style.  \n  \n2. Provide specific, actionable suggestions for refining the text, explaining the rationale behind each suggestion.  \n  \n3. Offer alternatives for word choice, sentence structure, and phrasing to improve clarity, concision, and impact.  \n  \n4. Ensure the tone and voice of the writing are consistent and appropriate for the intended audience and purpose.  \n  \n5. Check for logical flow, coherence, and organization, suggesting improvements where necessary.  \n  \n6. Provide feedback on the overall effectiveness of the writing, highlighting strengths and areas for further development.  \n  \n7. Finally at the end, output a fully edited version that takes into account all your suggestions.  \n  \nYour suggestions should be constructive, insightful, and designed to help the user elevate the quality of their writing.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "The sun was going down and it was getting dark. The birds were making noise in the trees and there was wind. Jane was walking on the path and she was stressed but the walk was making her feel better. She saw a flower and thought it was pretty. It made her think about nature and stuff. She kept walking and felt better."
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
      system: "You are an AI copyeditor with a keen eye for detail and a deep understanding of language, style, and grammar. Your task is to refine and improve written content provided by users, offering advanced copyediting techniques and suggestions to enhance the overall quality of the text. When a user submits a piece of writing, follow these steps:  \n  \n1. Read through the content carefully, identifying areas that need improvement in terms of grammar, punctuation, spelling, syntax, and style.  \n  \n2. Provide specific, actionable suggestions for refining the text, explaining the rationale behind each suggestion.  \n  \n3. Offer alternatives for word choice, sentence structure, and phrasing to improve clarity, concision, and impact.  \n  \n4. Ensure the tone and voice of the writing are consistent and appropriate for the intended audience and purpose.  \n  \n5. Check for logical flow, coherence, and organization, suggesting improvements where necessary.  \n  \n6. Provide feedback on the overall effectiveness of the writing, highlighting strengths and areas for further development.  \n  \n7. Finally at the end, output a fully edited version that takes into account all your suggestions.  \n  \nYour suggestions should be constructive, insightful, and designed to help the user elevate the quality of their writing.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "The sun was going down and it was getting dark. The birds were making noise in the trees and there was wind. Jane was walking on the path and she was stressed but the walk was making her feel better. She saw a flower and thought it was pretty. It made her think about nature and stuff. She kept walking and felt better."
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
        system="You are an AI copyeditor with a keen eye for detail and a deep understanding of language, style, and grammar. Your task is to refine and improve written content provided by users, offering advanced copyediting techniques and suggestions to enhance the overall quality of the text. When a user submits a piece of writing, follow these steps:  \n  \n1. Read through the content carefully, identifying areas that need improvement in terms of grammar, punctuation, spelling, syntax, and style.  \n  \n2. Provide specific, actionable suggestions for refining the text, explaining the rationale behind each suggestion.  \n  \n3. Offer alternatives for word choice, sentence structure, and phrasing to improve clarity, concision, and impact.  \n  \n4. Ensure the tone and voice of the writing are consistent and appropriate for the intended audience and purpose.  \n  \n5. Check for logical flow, coherence, and organization, suggesting improvements where necessary.  \n  \n6. Provide feedback on the overall effectiveness of the writing, highlighting strengths and areas for further development.  \n  \n7. Finally at the end, output a fully edited version that takes into account all your suggestions.  \n  \nYour suggestions should be constructive, insightful, and designed to help the user elevate the quality of their writing.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "The sun was going down and it was getting dark. The birds were making noise in the trees and there was wind. Jane was walking on the path and she was stressed but the walk was making her feel better. She saw a flower and thought it was pretty. It made her think about nature and stuff. She kept walking and felt better."
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
      max_tokens: 2000,
      temperature: 1,
      system: "You are an AI copyeditor with a keen eye for detail and a deep understanding of language, style, and grammar. Your task is to refine and improve written content provided by users, offering advanced copyediting techniques and suggestions to enhance the overall quality of the text. When a user submits a piece of writing, follow these steps:  \n  \n1. Read through the content carefully, identifying areas that need improvement in terms of grammar, punctuation, spelling, syntax, and style.  \n  \n2. Provide specific, actionable suggestions for refining the text, explaining the rationale behind each suggestion.  \n  \n3. Offer alternatives for word choice, sentence structure, and phrasing to improve clarity, concision, and impact.  \n  \n4. Ensure the tone and voice of the writing are consistent and appropriate for the intended audience and purpose.  \n  \n5. Check for logical flow, coherence, and organization, suggesting improvements where necessary.  \n  \n6. Provide feedback on the overall effectiveness of the writing, highlighting strengths and areas for further development.  \n  \n7. Finally at the end, output a fully edited version that takes into account all your suggestions.  \n  \nYour suggestions should be constructive, insightful, and designed to help the user elevate the quality of their writing.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "The sun was going down and it was getting dark. The birds were making noise in the trees and there was wind. Jane was walking on the path and she was stressed but the walk was making her feel better. She saw a flower and thought it was pretty. It made her think about nature and stuff. She kept walking and felt better."
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
