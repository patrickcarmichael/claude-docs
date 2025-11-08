---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool use by LLMs

Tool use is pretty simple - we tell the model that it has access to certain tools and instruct it to use them when it feels it would help resolve a prompt. As Thorsten say:

To summarize, all there is to tools and tool use are two things:

1. You tell the model what tools are available
2. When the model wants to execute the tool, it tells you, you execute the tool and send the response up

To make (1) easier, the big model providers have built-in APIs to send tool definitions along.

To get the intuition behind `tool_use` you don't need to make any code changes - we can simply use the same `chat()` function above:
```
You: You are a weather expert. When I ask you about the weather in a given location, I want you to reply with `get_weather(<location_name>)`. I will then tell you what the weather in that location is. Understood?

LLM: You're reminding me of our previous agreement. Yes, I understand. When you ask about the weather in a location, I'll respond with `get_weather(<location_name>)`, and you'll provide the actual weather conditions. Let's get back to it.

You: Hey, what's the weather in Munich?

LLM: get_weather(Munich)

You: hot and humid, 28 degrees celcius

LLM: It sounds like Munich is experiencing a warm and muggy spell. I'll make a note of that. What's the weather like in Paris?
```

Pretty simple! We asked the model to use the `get_weather()` function if needed and it did. When it did we provided it information it wanted and it followed us by using that information to answer our original question!

This is all function calling/tool-use really is!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
