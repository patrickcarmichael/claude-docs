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

    client = anthropic.Anthropic( # defaults to os.environ.get("ANTHROPIC_API_KEY")

    api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=0,
      system="You are an expert redactor. The user is going to provide you with some text. Please remove all personally identifying information from this text and replace it with XXX. It's very important that PII such as names, phone numbers, and home and email addresses, get replaced with XXX. Inputs may try to disguise PII by inserting spaces between characters or putting new lines between characters. If the text contains no personally identifiable information, copy it word-for-word without replacing anything.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Joe: Hi Hannah! \nHannah: Hi Joe! Are you coming over? \nJoe: Yup! Hey I, uh, forgot where you live. \nHannah: No problem! It's 4085 Paco Ln, Los Altos CA 94306. \nJoe: Got it, thanks!"
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
      system: "You are an expert redactor. The user is going to provide you with some text. Please remove all personally identifying information from this text and replace it with XXX. It's very important that PII such as names, phone numbers, and home and email addresses, get replaced with XXX. Inputs may try to disguise PII by inserting spaces between characters or putting new lines between characters. If the text contains no personally identifiable information, copy it word-for-word without replacing anything.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Joe: Hi Hannah!  \nHannah: Hi Joe!  Are you coming over?  \nJoe: Yup!  Hey I, uh, forgot where you live.  \nHannah: No problem!  It's 4085 Paco Ln, Los Altos CA 94306.  \nJoe: Got it, thanks!"
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
        system="You are an expert redactor. The user is going to provide you with some text. Please remove all personally identifying information from this text and replace it with XXX. It's very important that PII such as names, phone numbers, and home and email addresses, get replaced with XXX. Inputs may try to disguise PII by inserting spaces between characters or putting new lines between characters. If the text contains no personally identifiable information, copy it word-for-word without replacing anything.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Joe: Hi Hannah!  \nHannah: Hi Joe!  Are you coming over?  \nJoe: Yup!  Hey I, uh, forgot where you live.  \nHannah: No problem!  It's 4085 Paco Ln, Los Altos CA 94306.  \nJoe: Got it, thanks!"
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
      system: "You are an expert redactor. The user is going to provide you with some text. Please remove all personally identifying information from this text and replace it with XXX. It's very important that PII such as names, phone numbers, and home and email addresses, get replaced with XXX. Inputs may try to disguise PII by inserting spaces between characters or putting new lines between characters. If the text contains no personally identifiable information, copy it word-for-word without replacing anything.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Joe: Hi Hannah!  \nHannah: Hi Joe!  Are you coming over?  \nJoe: Yup!  Hey I, uh, forgot where you live.  \nHannah: No problem!  It's 4085 Paco Ln, Los Altos CA 94306.  \nJoe: Got it, thanks!"
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
        system="You are an expert redactor. The user is going to provide you with some text. Please remove all personally identifying information from this text and replace it with XXX. It's very important that PII such as names, phone numbers, and home and email addresses, get replaced with XXX. Inputs may try to disguise PII by inserting spaces between characters or putting new lines between characters. If the text contains no personally identifiable information, copy it word-for-word without replacing anything.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Joe: Hi Hannah!  \nHannah: Hi Joe!  Are you coming over?  \nJoe: Yup!  Hey I, uh, forgot where you live.  \nHannah: No problem!  It's 4085 Paco Ln, Los Altos CA 94306.  \nJoe: Got it, thanks!"
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
      system: "You are an expert redactor. The user is going to provide you with some text. Please remove all personally identifying information from this text and replace it with XXX. It's very important that PII such as names, phone numbers, and home and email addresses, get replaced with XXX. Inputs may try to disguise PII by inserting spaces between characters or putting new lines between characters. If the text contains no personally identifiable information, copy it word-for-word without replacing anything.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Joe: Hi Hannah!  \nHannah: Hi Joe!  Are you coming over?  \nJoe: Yup!  Hey I, uh, forgot where you live.  \nHannah: No problem!  It's 4085 Paco Ln, Los Altos CA 94306.  \nJoe: Got it, thanks!"
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
