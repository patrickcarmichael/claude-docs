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

    client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")

        api_key="my_api_key",
    )
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2000,
        temperature=0,
        system='You are an expert research assistant. Here is a document you will answer questions about: \n<doc> \n[Full text of [Matterport SEC filing 10-K 2023](https://investors.matterport.com/node/9501/html), not pasted here for brevity] \n</doc> \n \nFirst, find the quotes from the document that are most relevant to answering the question, and then print them in numbered order. Quotes should be relatively short. \n \nIf there are no relevant quotes, write "No relevant quotes" instead. \n \nThen, answer the question, starting with "Answer:". Do not include or reference quoted content verbatim in the answer. Don\'t say "According to Quote [1]" when answering. Instead make references to quotes relevant to each section of the answer solely by adding their bracketed numbers at the end of relevant sentences. \n \nThus, the format of your overall response should look like what\'s shown between the <example></example> tags. Make sure to follow the formatting and spacing exactly. \n<example> \nQuotes: \n[1] "Company X reported revenue of \$12 million in 2021." \n[2] "Almost 90% of revenue came from widget sales, with gadget sales making up the remaining 10%." \n \nAnswer: \nCompany X earned \$12 million. [1] Almost 90% of it was from widget sales. [2] \n</example> \n \nIf the question cannot be answered by the document, say so.',
        messages=[
            {
                "role": "user",
                "content": [{"type": "text", "text": "Is Matterport doing well?"}],
            }
        ],
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
      temperature: 0,
      system: "You are an expert research assistant. Here is a document you will answer questions about:  \n<doc>  \n[Full text of [Matterport SEC filing 10-K 2023](https://investors.matterport.com/node/9501/html), not pasted here for brevity]  \n</doc>  \n  \nFirst, find the quotes from the document that are most relevant to answering the question, and then print them in numbered order. Quotes should be relatively short.  \n  \nIf there are no relevant quotes, write \"No relevant quotes\" instead.  \n  \nThen, answer the question, starting with \"Answer:\". Do not include or reference quoted content verbatim in the answer. Don't say \"According to Quote [1]\" when answering. Instead make references to quotes relevant to each section of the answer solely by adding their bracketed numbers at the end of relevant sentences.  \n  \nThus, the format of your overall response should look like what's shown between the <example></example> tags. Make sure to follow the formatting and spacing exactly.  \n<example>  \nQuotes:  \n[1] \"Company X reported revenue of \$12 million in 2021.\"  \n[2] \"Almost 90% of revenue came from widget sales, with gadget sales making up the remaining 10%.\"  \n  \nAnswer:  \nCompany X earned \$12 million. [1] Almost 90% of it was from widget sales. [2]  \n</example>  \n  \nIf the question cannot be answered by the document, say so.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Is Matterport doing well?"
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
        temperature=0,
        system="You are an expert research assistant. Here is a document you will answer questions about:  \n<doc>  \n[Full text of [Matterport SEC filing 10-K 2023](https://investors.matterport.com/node/9501/html), not pasted here for brevity]  \n</doc>  \n  \nFirst, find the quotes from the document that are most relevant to answering the question, and then print them in numbered order. Quotes should be relatively short.  \n  \nIf there are no relevant quotes, write \"No relevant quotes\" instead.  \n  \nThen, answer the question, starting with \"Answer:\". Do not include or reference quoted content verbatim in the answer. Don't say \"According to Quote [1]\" when answering. Instead make references to quotes relevant to each section of the answer solely by adding their bracketed numbers at the end of relevant sentences.  \n  \nThus, the format of your overall response should look like what's shown between the <example></example> tags. Make sure to follow the formatting and spacing exactly.  \n<example>  \nQuotes:  \n[1] \"Company X reported revenue of \$12 million in 2021.\"  \n[2] \"Almost 90% of revenue came from widget sales, with gadget sales making up the remaining 10%.\"  \n  \nAnswer:  \nCompany X earned \$12 million. [1] Almost 90% of it was from widget sales. [2]  \n</example>  \n  \nIf the question cannot be answered by the document, say so.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Is Matterport doing well?"
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
      temperature: 0,
      system: "You are an expert research assistant. Here is a document you will answer questions about:  \n<doc>  \n[Full text of [Matterport SEC filing 10-K 2023](https://investors.matterport.com/node/9501/html), not pasted here for brevity]  \n</doc>  \n  \nFirst, find the quotes from the document that are most relevant to answering the question, and then print them in numbered order. Quotes should be relatively short.  \n  \nIf there are no relevant quotes, write \"No relevant quotes\" instead.  \n  \nThen, answer the question, starting with \"Answer:\". Do not include or reference quoted content verbatim in the answer. Don't say \"According to Quote [1]\" when answering. Instead make references to quotes relevant to each section of the answer solely by adding their bracketed numbers at the end of relevant sentences.  \n  \nThus, the format of your overall response should look like what's shown between the <example></example> tags. Make sure to follow the formatting and spacing exactly.  \n<example>  \nQuotes:  \n[1] \"Company X reported revenue of \$12 million in 2021.\"  \n[2] \"Almost 90% of revenue came from widget sales, with gadget sales making up the remaining 10%.\"  \n  \nAnswer:  \nCompany X earned \$12 million. [1] Almost 90% of it was from widget sales. [2]  \n</example>  \n  \nIf the question cannot be answered by the document, say so.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Is Matterport doing well?"
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
        temperature=0,
        system="You are an expert research assistant. Here is a document you will answer questions about:  \n<doc>  \n[Full text of [Matterport SEC filing 10-K 2023](https://investors.matterport.com/node/9501/html), not pasted here for brevity]  \n</doc>  \n  \nFirst, find the quotes from the document that are most relevant to answering the question, and then print them in numbered order. Quotes should be relatively short.  \n  \nIf there are no relevant quotes, write \"No relevant quotes\" instead.  \n  \nThen, answer the question, starting with \"Answer:\". Do not include or reference quoted content verbatim in the answer. Don't say \"According to Quote [1]\" when answering. Instead make references to quotes relevant to each section of the answer solely by adding their bracketed numbers at the end of relevant sentences.  \n  \nThus, the format of your overall response should look like what's shown between the <example></example> tags. Make sure to follow the formatting and spacing exactly.  \n<example>  \nQuotes:  \n[1] \"Company X reported revenue of \$12 million in 2021.\"  \n[2] \"Almost 90% of revenue came from widget sales, with gadget sales making up the remaining 10%.\"  \n  \nAnswer:  \nCompany X earned \$12 million. [1] Almost 90% of it was from widget sales. [2]  \n</example>  \n  \nIf the question cannot be answered by the document, say so.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Is Matterport doing well?"
                    }
                ]
            }
        ]
    )
    print(message.content)
```
  </Tab>

  <Tab title=" Vertex AI TypeScript">
```TypeScript
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
      model: "claude-sonnet-4@20250514",
      max_tokens: 2000,
      temperature: 0,
      system: "You are an expert research assistant. Here is a document you will answer questions about:  \n<doc>  \n[Full text of [Matterport SEC filing 10-K 2023](https://investors.matterport.com/node/9501/html), not pasted here for brevity]  \n</doc>  \n  \nFirst, find the quotes from the document that are most relevant to answering the question, and then print them in numbered order. Quotes should be relatively short.  \n  \nIf there are no relevant quotes, write \"No relevant quotes\" instead.  \n  \nThen, answer the question, starting with \"Answer:\". Do not include or reference quoted content verbatim in the answer. Don't say \"According to Quote [1]\" when answering. Instead make references to quotes relevant to each section of the answer solely by adding their bracketed numbers at the end of relevant sentences.  \n  \nThus, the format of your overall response should look like what's shown between the <example></example> tags. Make sure to follow the formatting and spacing exactly.  \n<example>  \nQuotes:  \n[1] \"Company X reported revenue of \$12 million in 2021.\"  \n[2] \"Almost 90% of revenue came from widget sales, with gadget sales making up the remaining 10%.\"  \n  \nAnswer:  \nCompany X earned \$12 million. [1] Almost 90% of it was from widget sales. [2]  \n</example>  \n  \nIf the question cannot be answered by the document, say so.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Is Matterport doing well?"
            }
          ]
        }
      ]
    });
    console.log(msg);
```python
  </Tab>
</Tabs>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
