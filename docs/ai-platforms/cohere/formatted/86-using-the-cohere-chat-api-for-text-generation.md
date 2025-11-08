---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using the Cohere Chat API for Text Generation

> How to use the Chat API endpoint with Cohere LLMs to generate text responses in a conversational interface

The Chat API endpoint is used to generate text with Cohere LLMs. This endpoint facilitates a conversational interface, allowing users to send messages to the model and receive text responses.

Every message comes with a `content` field and an associated `role`, which indicates who that message is sent from. Roles can be `user`, `assistant`, `system` and `tool`.

<CodeBlocks>
```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="<YOUR API KEY>")

  res = co.chat(
      model="command-a-03-2025",
      messages=[
          {
              "role": "user",
              "content": "Write a title for a blog post about API design. Only output the title text.",
          }
      ],
  )

  print(res.message.content[0].text)
  # "The Ultimate Guide to API Design: Best Practices for Building Robust and Scalable APIs"

```
```java JAVA
  package chatv2post;

  import com.cohere.api.Cohere;
  import com.cohere.api.resources.v2.requests.V2ChatRequest;
  import com.cohere.api.types.*;
  import java.util.List;

  public class Default {
      public static void main(String[] args) {
          Cohere cohere = Cohere.builder().token("<<apiKey>>").clientName("snippet").build();

          ChatResponse response =
                  cohere.v2()
                          .chat(
                                  V2ChatRequest.builder()
                                      .model("command-a-03-2025")
                                      .messages(
                                          List.of(
                                              ChatMessageV2.user(
                                                  UserMessage.builder()
                                                      .content(
                                                          UserMessageContent
                                                                  .of("Hello world!"))
                                                      .build())))
                                      .build());

          System.out.println(response);
      }
  }
```
```typescript TYPESCRIPT
  const { CohereClientV2 } = require('cohere-ai');

  const cohere = new CohereClientV2({
    token: '<<apiKey>>',
  });

  (async () => {
    const response = await cohere.chat({
      model: 'command-a-03-2025',
      messages: [
        {
          role: 'user',
          content: 'hello world!',
        },
      ],
    });

    console.log(response);
  })();
```
```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-03-2025",
      "messages": [
        {
          "role": "user",
          "content": "Write a title for a blog post about API design. Only output the title text."
        }
      ]
    }'
```
</CodeBlocks>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
