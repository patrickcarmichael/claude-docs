---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Citations

Source: https://docs.claude.com/en/docs/build-with-claude/citations


Claude is capable of providing detailed citations when answering questions about documents, helping you track and verify information sources in responses.

All [active models](/en/docs/about-claude/models/overview) support citations, with the exception of Haiku 3.

>   **⚠️ Warning**
>
>   *Citations with Claude Sonnet 3.7*

  Claude Sonnet 3.7 may be less likely to make citations compared to other Claude models without more explicit instructions from the user. When using citations with Claude Sonnet 3.7, we recommend including additional instructions in the `user` turn, like `"Use citations to back up your answer."` for example.

  We've also observed that when the model is asked to structure its response, it is unlikely to use citations unless explicitly told to use citations within that format. For example, if the model is asked to use `<result>` tags in its response, you should add something like `"Always use citations in your answer, even within <result> tags."`

<Tip>
  Please share your feedback and suggestions about the citations feature using this [form](https://forms.gle/9n9hSrKnKe3rpowH9).
</Tip>

Here's an example of how to use citations with the Messages API:
```bash
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "document",
              "source": {
                "type": "text",
                "media_type": "text/plain",
                "data": "The grass is green. The sky is blue."
              },
              "title": "My Document",
              "context": "This is a trustworthy document.",
              "citations": {"enabled": true}
            },
            {
              "type": "text",
              "text": "What color is the grass and sky?"
            }
          ]
        }
      ]
    }'
```
```python
  import anthropic

  client = anthropic.Anthropic()

  response = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "document",
                      "source": {
                          "type": "text",
                          "media_type": "text/plain",
                          "data": "The grass is green. The sky is blue."
                      },
                      "title": "My Document",
                      "context": "This is a trustworthy document.",
                      "citations": {"enabled": True}
                  },
                  {
                      "type": "text",
                      "text": "What color is the grass and sky?"
                  }
              ]
          }
      ]
  )
  print(response)
```
```java
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.*;

  public class DocumentExample {

      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          PlainTextSource source = PlainTextSource.builder()
                  .data("The grass is green. The sky is blue.")
                  .build();

          DocumentBlockParam documentParam = DocumentBlockParam.builder()
                  .source(source)
                  .title("My Document")
                  .context("This is a trustworthy document.")
                  .citations(CitationsConfigParam.builder().enabled(true).build())
                  .build();
          
          TextBlockParam textBlockParam = TextBlockParam.builder()
                  .text("What color is the grass and sky?")
                  .build();

          MessageCreateParams params = MessageCreateParams.builder()
                  .model(Model.CLAUDE_SONNET_4_20250514)
                  .maxTokens(1024)
                  .addUserMessageOfBlockParams(List.of(ContentBlockParam.ofDocument(documentParam), ContentBlockParam.ofText(textBlockParam)))
                  .build();

          Message message = client.messages().create(params);
          System.out.println(message);
      }
  }
```javascript

<Tip>
  **Comparison with prompt-based approaches**

  In comparison with prompt-based citations solutions, the citations feature has the following advantages:

  * **Cost savings:** If your prompt-based approach asks Claude to output direct quotes, you may see cost savings due to the fact that `cited_text` does not count towards your output tokens.
  * **Better citation reliability:** Because we parse citations into the respective response formats mentioned above and extract `cited_text`, citations are guaranteed to contain valid pointers to the provided documents.
  * **Improved citation quality:** In our evals, we found the citations feature to be significantly more likely to cite the most relevant quotes from documents as compared to purely prompt-based approaches.
</Tip>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
