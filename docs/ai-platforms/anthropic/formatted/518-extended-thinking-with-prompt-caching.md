---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Extended thinking with prompt caching

[Prompt caching](/en/docs/build-with-claude/prompt-caching) with thinking has several important considerations:

<Tip>
  Extended thinking tasks often take longer than 5 minutes to complete. Consider using the [1-hour cache duration](/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration) to maintain cache hits across longer thinking sessions and multi-step workflows.
</Tip>

**Thinking block context removal**

* Thinking blocks from previous turns are removed from context, which can affect cache breakpoints
* When continuing conversations with tool use, thinking blocks are cached and count as input tokens when read from cache
* This creates a tradeoff: while thinking blocks don't consume context window space visually, they still count toward your input token usage when cached
* If thinking becomes disabled, requests will fail if you pass thinking content in the current tool use turn. In other contexts, thinking content passed to the API is simply ignored

**Cache invalidation patterns**

* Changes to thinking parameters (enabled/disabled or budget allocation) invalidate message cache breakpoints
* [Interleaved thinking](#interleaved-thinking) amplifies cache invalidation, as thinking blocks can occur between multiple [tool calls](#extended-thinking-with-tool-use)
* System prompts and tools remain cached despite thinking parameter changes or block removal

>   **📝 Note**
>
> While thinking blocks are removed for caching and context calculations, they must be preserved when continuing conversations with [tool use](#extended-thinking-with-tool-use), especially with [interleaved thinking](#interleaved-thinking).

### Understanding thinking block caching behavior

When using extended thinking with tool use, thinking blocks exhibit specific caching behavior that affects token counting:

**How it works:**

1. Caching only occurs when you make a subsequent request that includes tool results
2. When the subsequent request is made, the previous conversation history (including thinking blocks) can be cached
3. These cached thinking blocks count as input tokens in your usage metrics when read from the cache
4. When a non-tool-result user block is included, all previous thinking blocks are ignored and stripped from context

**Detailed example flow:**

**Request 1:**
```
User: "What's the weather in Paris?"
```
**Response 1:**
```
[thinking_block_1] + [tool_use block 1]
```
**Request 2:**
```
User: ["What's the weather in Paris?"], 
Assistant: [thinking_block_1] + [tool_use block 1], 
User: [tool_result_1, cache=True]
```
**Response 2:**
```
[thinking_block_2] + [text block 2]
```
Request 2 writes a cache of the request content (not the response). The cache includes the original user message, the first thinking block, tool use block, and the tool result.

**Request 3:**
```
User: ["What's the weather in Paris?"], 
Assistant: [thinking_block_1] + [tool_use block 1], 
User: [tool_result_1, cache=True], 
Assistant: [thinking_block_2] + [text block 2], 
User: [Text response, cache=True]
```
Because a non-tool-result user block was included, all previous thinking blocks are ignored. This request will be processed the same as:
```
User: ["What's the weather in Paris?"], 
Assistant: [tool_use block 1], 
User: [tool_result_1, cache=True], 
Assistant: [text block 2], 
User: [Text response, cache=True]
```
**Key points:**

* This caching behavior happens automatically, even without explicit `cache_control` markers
* This behavior is consistent whether using regular thinking or interleaved thinking

<AccordionGroup>
  <Accordion title="System prompt caching (preserved when thinking changes)">
```python
      from anthropic import Anthropic
      import requests
      from bs4 import BeautifulSoup

      client = Anthropic()

      def fetch_article_content(url):
          response = requests.get(url)
          soup = BeautifulSoup(response.content, 'html.parser')

          # Remove script and style elements

          for script in soup(["script", "style"]):
              script.decompose()

          # Get text

          text = soup.get_text()

          # Break into lines and remove leading and trailing space on each

          lines = (line.strip() for line in text.splitlines())
          # Break multi-headlines into a line each

          chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
          # Drop blank lines

          text = '\n'.join(chunk for chunk in chunks if chunk)

          return text

      # Fetch the content of the article

      book_url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
      book_content = fetch_article_content(book_url)
      # Use just enough text for caching (first few chapters)

      LARGE_TEXT = book_content[:5000]

      SYSTEM_PROMPT=[
          {
              "type": "text",
              "text": "You are an AI assistant that is tasked with literary analysis. Analyze the following text carefully.",
          },
          {
              "type": "text",
              "text": LARGE_TEXT,
              "cache_control": {"type": "ephemeral"}
          }
      ]

      MESSAGES = [
          {
              "role": "user",
              "content": "Analyze the tone of this passage."
          }
      ]

      # First request - establish cache

      print("First request - establishing cache")
      response1 = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=20000,
          thinking={
              "type": "enabled",
              "budget_tokens": 4000
          },
          system=SYSTEM_PROMPT,
          messages=MESSAGES
      )

      print(f"First response usage: {response1.usage}")

      MESSAGES.append({
          "role": "assistant",
          "content": response1.content
      })
      MESSAGES.append({
          "role": "user",
          "content": "Analyze the characters in this passage."
      })
      # Second request - same thinking parameters (cache hit expected)

      print("\nSecond request - same thinking parameters (cache hit expected)")
      response2 = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=20000,
          thinking={
              "type": "enabled",
              "budget_tokens": 4000
          },
          system=SYSTEM_PROMPT,
          messages=MESSAGES
      )

      print(f"Second response usage: {response2.usage}")

      # Third request - different thinking parameters (cache miss for messages)

      print("\nThird request - different thinking parameters (cache miss for messages)")
      response3 = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=20000,
          thinking={
              "type": "enabled",
              "budget_tokens": 8000  # Changed thinking budget

          },
          system=SYSTEM_PROMPT,  # System prompt remains cached

          messages=MESSAGES  # Messages cache is invalidated

      )

      print(f"Third response usage: {response3.usage}")
```
```typescript
      import Anthropic from '@anthropic-ai/sdk';
      import axios from 'axios';
      import * as cheerio from 'cheerio';

      const client = new Anthropic();

      async function fetchArticleContent(url: string): Promise<string> {
        const response = await axios.get(url);
        const $ = cheerio.load(response.data);
        
        // Remove script and style elements
        $('script, style').remove();
        
        // Get text
        let text = $.text();
        
        // Break into lines and remove leading and trailing space on each
        const lines = text.split('\n').map(line => line.trim());
        // Drop blank lines
        text = lines.filter(line => line.length > 0).join('\n');
        
        return text;
      }

      // Fetch the content of the article
      const bookUrl = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt";
      const bookContent = await fetchArticleContent(bookUrl);
      // Use just enough text for caching (first few chapters)
      const LARGE_TEXT = bookContent.slice(0, 5000);

      const SYSTEM_PROMPT = [
        {
          type: "text",
          text: "You are an AI assistant that is tasked with literary analysis. Analyze the following text carefully.",
        },
        {
          type: "text",
          text: LARGE_TEXT,
          cache_control: { type: "ephemeral" }
        }
      ];

      const MESSAGES = [
        {
          role: "user",
          content: "Analyze the tone of this passage."
        }
      ];

      // First request - establish cache
      console.log("First request - establishing cache");
      const response1 = await client.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 20000,
        thinking: {
          type: "enabled",
          budget_tokens: 4000
        },
        system: SYSTEM_PROMPT,
        messages: MESSAGES
      });

      console.log(`First response usage: ${response1.usage}`);

      MESSAGES.push({
        role: "assistant",
        content: response1.content
      });
      MESSAGES.push({
        role: "user",
        content: "Analyze the characters in this passage."
      });

      // Second request - same thinking parameters (cache hit expected)
      console.log("\nSecond request - same thinking parameters (cache hit expected)");
      const response2 = await client.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 20000,
        thinking: {
          type: "enabled",
          budget_tokens: 4000
        },
        system: SYSTEM_PROMPT,
        messages: MESSAGES
      });

      console.log(`Second response usage: ${response2.usage}`);

      // Third request - different thinking parameters (cache miss for messages)
      console.log("\nThird request - different thinking parameters (cache miss for messages)");
      const response3 = await client.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 20000,
        thinking: {
          type: "enabled",
          budget_tokens: 8000  // Changed thinking budget
        },
        system: SYSTEM_PROMPT,  // System prompt remains cached
        messages: MESSAGES  // Messages cache is invalidated
      });

      console.log(`Third response usage: ${response3.usage}`);
```
  </Accordion>

  <Accordion title="Messages caching (invalidated when thinking changes)">
```python
      from anthropic import Anthropic
      import requests
      from bs4 import BeautifulSoup

      client = Anthropic()

      def fetch_article_content(url):
          response = requests.get(url)
          soup = BeautifulSoup(response.content, 'html.parser')

          # Remove script and style elements

          for script in soup(["script", "style"]):
              script.decompose()

          # Get text

          text = soup.get_text()

          # Break into lines and remove leading and trailing space on each

          lines = (line.strip() for line in text.splitlines())
          # Break multi-headlines into a line each

          chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
          # Drop blank lines

          text = '\n'.join(chunk for chunk in chunks if chunk)

          return text

      # Fetch the content of the article

      book_url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
      book_content = fetch_article_content(book_url)
      # Use just enough text for caching (first few chapters)

      LARGE_TEXT = book_content[:5000]

      # No system prompt - caching in messages instead

      MESSAGES = [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": LARGE_TEXT,
                      "cache_control": {"type": "ephemeral"},
                  },
                  {
                      "type": "text",
                      "text": "Analyze the tone of this passage."
                  }
              ]
          }
      ]

      # First request - establish cache

      print("First request - establishing cache")
      response1 = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=20000,
          thinking={
              "type": "enabled",
              "budget_tokens": 4000
          },
          messages=MESSAGES
      )

      print(f"First response usage: {response1.usage}")

      MESSAGES.append({
          "role": "assistant",
          "content": response1.content
      })
      MESSAGES.append({
          "role": "user",
          "content": "Analyze the characters in this passage."
      })
      # Second request - same thinking parameters (cache hit expected)

      print("\nSecond request - same thinking parameters (cache hit expected)")
      response2 = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=20000,
          thinking={
              "type": "enabled",
              "budget_tokens": 4000  # Same thinking budget

          },
          messages=MESSAGES
      )

      print(f"Second response usage: {response2.usage}")

      MESSAGES.append({
          "role": "assistant",
          "content": response2.content
      })
      MESSAGES.append({
          "role": "user",
          "content": "Analyze the setting in this passage."
      })

      # Third request - different thinking budget (cache miss expected)

      print("\nThird request - different thinking budget (cache miss expected)")
      response3 = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=20000,
          thinking={
              "type": "enabled",
              "budget_tokens": 8000  # Different thinking budget breaks cache

          },
          messages=MESSAGES
      )

      print(f"Third response usage: {response3.usage}")
```
```typescript
      import Anthropic from '@anthropic-ai/sdk';
      import axios from 'axios';
      import * as cheerio from 'cheerio';

      const client = new Anthropic();

      async function fetchArticleContent(url: string): Promise<string> {
        const response = await axios.get(url);
        const $ = cheerio.load(response.data);

        // Remove script and style elements
        $('script, style').remove();

        // Get text
        let text = $.text();

        // Clean up text (break into lines, remove whitespace)
        const lines = text.split('\n').map(line => line.trim());
        const chunks = lines.flatMap(line => line.split('  ').map(phrase => phrase.trim()));
        text = chunks.filter(chunk => chunk).join('\n');

        return text;
      }

      async function main() {
        // Fetch the content of the article
        const bookUrl = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt";
        const bookContent = await fetchArticleContent(bookUrl);
        // Use just enough text for caching (first few chapters)
        const LARGE_TEXT = bookContent.substring(0, 5000);

        // No system prompt - caching in messages instead
        let MESSAGES = [
          {
            role: "user",
            content: [
              {
                type: "text",
                text: LARGE_TEXT,
                cache_control: {type: "ephemeral"},
              },
              {
                type: "text",
                text: "Analyze the tone of this passage."
              }
            ]
          }
        ];

        // First request - establish cache
        console.log("First request - establishing cache");
        const response1 = await client.messages.create({
          model: "claude-sonnet-4-5",
          max_tokens: 20000,
          thinking: {
            type: "enabled",
            budget_tokens: 4000
          },
          messages: MESSAGES
        });

        console.log(`First response usage: `, response1.usage);

        MESSAGES = [
          ...MESSAGES,
          {
            role: "assistant",
            content: response1.content
          },
          {
            role: "user",
            content: "Analyze the characters in this passage."
          }
        ];

        // Second request - same thinking parameters (cache hit expected)
        console.log("\nSecond request - same thinking parameters (cache hit expected)");
        const response2 = await client.messages.create({
          model: "claude-sonnet-4-5",
          max_tokens: 20000,
          thinking: {
            type: "enabled",
            budget_tokens: 4000  // Same thinking budget
          },
          messages: MESSAGES
        });

        console.log(`Second response usage: `, response2.usage);

        MESSAGES = [
          ...MESSAGES,
          {
            role: "assistant",
            content: response2.content
          },
          {
            role: "user",
            content: "Analyze the setting in this passage."
          }
        ];

        // Third request - different thinking budget (cache miss expected)
        console.log("\nThird request - different thinking budget (cache miss expected)");
        const response3 = await client.messages.create({
          model: "claude-sonnet-4-5",
          max_tokens: 20000,
          thinking: {
            type: "enabled",
            budget_tokens: 8000  // Different thinking budget breaks cache
          },
          messages: MESSAGES
        });

        console.log(`Third response usage: `, response3.usage);
      }

      main().catch(console.error);
```
```java
      import java.io.IOException;
      import java.io.InputStream;
      import java.util.ArrayList;
      import java.util.List;
      import java.io.BufferedReader;
      import java.io.InputStreamReader;
      import java.net.URL;
      import java.util.Arrays;
      import java.util.regex.Pattern;

      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.models.beta.messages.*;
      import com.anthropic.models.beta.messages.MessageCreateParams;
      import com.anthropic.models.messages.Model;

      import static java.util.stream.Collectors.joining;
      import static java.util.stream.Collectors.toList;

      public class ThinkingCacheExample {
          public static void main(String[] args) throws IOException {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              // Fetch the content of the article
              String bookUrl = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt";
              String bookContent = fetchArticleContent(bookUrl);
              // Use just enough text for caching (first few chapters)
              String largeText = bookContent.substring(0, 5000);

              List<BetaTextBlockParam> systemPrompt = List.of(
                      BetaTextBlockParam.builder()
                              .text("You are an AI assistant that is tasked with literary analysis. Analyze the following text carefully.")
                              .build(),
                      BetaTextBlockParam.builder()
                              .text(largeText)
                              .cacheControl(BetaCacheControlEphemeral.builder().build())
                              .build()
              );

              List<BetaMessageParam> messages = new ArrayList<>();
              messages.add(BetaMessageParam.builder()
                      .role(BetaMessageParam.Role.USER)
                      .content("Analyze the tone of this passage.")
                      .build());

              // First request - establish cache
              System.out.println("First request - establishing cache");
              BetaMessage response1 = client.beta().messages().create(
                      MessageCreateParams.builder()
                              .model(Model.CLAUDE_OPUS_4_0)
                              .maxTokens(20000)
                              .thinking(BetaThinkingConfigEnabled.builder().budgetTokens(4000).build())
                              .systemOfBetaTextBlockParams(systemPrompt)
                              .messages(messages)
                              .build()
              );

              System.out.println("First response usage: " + response1.usage());

              // Second request - same thinking parameters (cache hit expected)
              System.out.println("\nSecond request - same thinking parameters (cache hit expected)");
              BetaMessage response2 = client.beta().messages().create(
                      MessageCreateParams.builder()
                              .model(Model.CLAUDE_OPUS_4_0)
                              .maxTokens(20000)
                              .thinking(BetaThinkingConfigEnabled.builder().budgetTokens(4000).build())
                              .systemOfBetaTextBlockParams(systemPrompt)
                              .addMessage(response1)
                              .addUserMessage("Analyze the characters in this passage.")
                              .messages(messages)
                              .build()
              );

              System.out.println("Second response usage: " + response2.usage());

              // Third request - different thinking budget (cache hit expected because system prompt caching)
              System.out.println("\nThird request - different thinking budget (cache hit expected)");
              BetaMessage response3 = client.beta().messages().create(
                      MessageCreateParams.builder()
                              .model(Model.CLAUDE_OPUS_4_0)
                              .maxTokens(20000)
                              .thinking(BetaThinkingConfigEnabled.builder().budgetTokens(8000).build())
                              .systemOfBetaTextBlockParams(systemPrompt)
                              .addMessage(response1)
                              .addUserMessage("Analyze the characters in this passage.")
                              .addMessage(response2)
                              .addUserMessage("Analyze the setting in this passage.")
                              .build()
              );

              System.out.println("Third response usage: " + response3.usage());
          }

          private static String fetchArticleContent(String url) throws IOException {
              // Fetch HTML content
              String htmlContent = fetchHtml(url);

              // Remove script and style elements
              String noScriptStyle = removeElements(htmlContent, "script", "style");

              // Extract text (simple approach - remove HTML tags)
              String text = removeHtmlTags(noScriptStyle);

              // Clean up text (break into lines, remove whitespace)
              List<String> lines = Arrays.asList(text.split("\n"));
              List<String> trimmedLines = lines.stream()
                      .map(String::trim)
                      .collect(toList());

              // Split on double spaces and flatten
              List<String> chunks = trimmedLines.stream()
                      .flatMap(line -> Arrays.stream(line.split("  "))
                              .map(String::trim))
                      .collect(toList());

              // Filter empty chunks and join with newlines
              return chunks.stream()
                      .filter(chunk -> !chunk.isEmpty())
                      .collect(joining("\n"));
          }

          /**
           * Fetches HTML content from a URL
           */
          private static String fetchHtml(String urlString) throws IOException {
              try (InputStream inputStream = new URL(urlString).openStream()) {
                  StringBuilder content = new StringBuilder();
                  try (BufferedReader reader = new BufferedReader(
                          new InputStreamReader(inputStream))) {
                      String line;
                      while ((line = reader.readLine()) != null) {
                          content.append(line).append("\n");
                      }
                  }
                  return content.toString();
              }
          }

          /**
           * Removes specified HTML elements and their content
           */
          private static String removeElements(String html, String... elementNames) {
              String result = html;
              for (String element : elementNames) {
                  // Pattern to match <element>...</element> and self-closing tags
                  String pattern = "<" + element + "\\s*[^>]*>.*?</" + element + ">|<" + element + "\\s*[^>]*/?>";
                  result = Pattern.compile(pattern, Pattern.DOTALL).matcher(result).replaceAll("");
              }
              return result;
          }

          /**
           * Removes all HTML tags from content
           */
          private static String removeHtmlTags(String html) {
              // Replace <br> and <p> tags with newlines for better text formatting
              String withLineBreaks = html.replaceAll("<br\\s*/?\\s*>|</?p\\s*[^>]*>", "\n");

              // Remove remaining HTML tags
              String noTags = withLineBreaks.replaceAll("<[^>]*>", "");

              // Decode HTML entities (simplified for common entities)
              return decodeHtmlEntities(noTags);
          }

          /**
           * Simple HTML entity decoder for common entities
           */
          private static String decodeHtmlEntities(String text) {
              return text
                      .replaceAll("&nbsp;", " ")
                      .replaceAll("&amp;", "&")
                      .replaceAll("&lt;", "<")
                      .replaceAll("&gt;", ">")
                      .replaceAll("&quot;", "\"")
                      .replaceAll("&#39;", "'")
                      .replaceAll("&hellip;", "...")
                      .replaceAll("&mdash;", "—");
          }

      }
```

    Here is the output of the script (you may see slightly different numbers)
```
    First request - establishing cache
    First response usage: { cache_creation_input_tokens: 1370, cache_read_input_tokens: 0, input_tokens: 17, output_tokens: 700 }

    Second request - same thinking parameters (cache hit expected)

    Second response usage: { cache_creation_input_tokens: 0, cache_read_input_tokens: 1370, input_tokens: 303, output_tokens: 874 }

    Third request - different thinking budget (cache miss expected)
    Third response usage: { cache_creation_input_tokens: 1370, cache_read_input_tokens: 0, input_tokens: 747, output_tokens: 619 }
```
    This example demonstrates that when caching is set up in the messages array, changing the thinking parameters (budget\_tokens increased from 4000 to 8000) **invalidates the cache**. The third request shows no cache hit with `cache_creation_input_tokens=1370` and `cache_read_input_tokens=0`, proving that message-based caching is invalidated when thinking parameters change.
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
