---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## API Request

```python
  import anthropic

  client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")

      api_key="my_api_key",
  )
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=2000,
      temperature=0,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Write me a fully complete web app as a single HTML file. The app should contain a simple side-scrolling game where I use WASD to move around.  When moving around the world, occasionally the character/sprite will encounter words. When a word is encountered, the player must correctly type the word as fast as possible.The faster the word is successfully typed, the more point the player gets. We should have a counter in the top-right to keep track of points. Words should be random and highly variable to keep the game interesting.  \n  \nYou should make the website very aesthetic and use Tailwind."
                  }
              ]
          }
      ]
  )
  print(message.content)
```
```typescript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: 'my_api_key', // defaults to process.env["ANTHROPIC_API_KEY"]
  });

  const msg = await anthropic.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 2000,
    temperature: 0,
    messages: [
      {
        role: 'user',
        content: [
          {
            type: 'text',
            text: 'Write me a fully complete web app as a single HTML file. The app should contain a simple side-scrolling game where I use WASD to move around.  When moving around the world, occasionally the character/sprite will encounter words. When a word is encountered, the player must correctly type the word as fast as possible.The faster the word is successfully typed, the more point the player gets. We should have a counter in the top-right to keep track of points. Words should be random and highly variable to keep the game interesting.  \n  \nYou should make the website very aesthetic and use Tailwind.',
          },
        ],
      },
    ],
  });
  console.log(msg);
```
```python AWS Bedrock Python theme={null}
  from anthropic import AnthropicBedrock

  # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock

  # for authentication options

  client = AnthropicBedrock()

  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=2000,
      temperature=0,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Write me a fully complete web app as a single HTML file. The app should contain a simple side-scrolling game where I use WASD to move around.  When moving around the world, occasionally the character/sprite will encounter words. When a word is encountered, the player must correctly type the word as fast as possible.The faster the word is successfully typed, the more point the player gets. We should have a counter in the top-right to keep track of points. Words should be random and highly variable to keep the game interesting.  \n  \nYou should make the website very aesthetic and use Tailwind."
                  }
              ]
          }
      ]
  )
  print(message.content)
```
```typescript AWS Bedrock TypeScript theme={null}
  import AnthropicBedrock from '@anthropic-ai/bedrock-sdk';

  // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  // for authentication options
  const client = new AnthropicBedrock();

  const msg = await client.messages.create({
    model: 'anthropic.claude-sonnet-4-5-20250929-v1:0',
    max_tokens: 2000,
    temperature: 0,
    messages: [
      {
        role: 'user',
        content: [
          {
            type: 'text',
            text: 'Write me a fully complete web app as a single HTML file. The app should contain a simple side-scrolling game where I use WASD to move around.  When moving around the world, occasionally the character/sprite will encounter words. When a word is encountered, the player must correctly type the word as fast as possible.The faster the word is successfully typed, the more point the player gets. We should have a counter in the top-right to keep track of points. Words should be random and highly variable to keep the game interesting.  \n  \nYou should make the website very aesthetic and use Tailwind.',
          },
        ],
      },
    ],
  });
  console.log(msg);
```


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
