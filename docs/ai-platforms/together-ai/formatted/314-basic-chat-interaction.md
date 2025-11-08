---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic Chat Interaction

Let's start with a simple loop that takes user input, sends it to a language model (LLM) using the Together AI client, and prints the LLM's response. We'll maintain a `messages_history` to keep track of the conversation context.
```python
  def chat():
      while True:
          user_input = input("Enter something (type 'exit' to quit): ")
          if user_input.lower() == "exit":
              break
          messages_history.append({"role": "user", "content": user_input})
          print(f"You: {user_input}")
          # Process user_input here

          completion = client.chat.completions.create(
              model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
              messages=messages_history,
          )
          print(f"LLM: {completion.choices[0].message.content}")
          messages_history.append(
              {
                  "role": "assistant",
                  "content": completion.choices[0].message.content,
              }
          )


  chat()
```

Usage:
```
You: Hey! I'm Zain! How are you?

LLM: Nice to meet you, Zain. I'm doing well, thanks for asking. I'm a large language model, so I don't have feelings or emotions like humans do, but I'm always happy to chat and help with any questions or topics you'd like to discuss. How about you? How's your day going?

You: Can you come up with any horse-related nicknames that make fun of my first name?

LLM: I can try to come up with some horse-related nicknames that poke fun at your name. Keep in mind that these are lighthearted and meant in a playful spirit.

Here are a few ideas:

1. Zain Stallion (a playful take on the idea of a strong, majestic horse)
2. Zainy McMane (a silly name that adds a fun twist to your name)
3. Zain the Reiner (a reference to the reining horse discipline, with a nod to your name)
4. Zainy Horseface (a goofy nickname that's sure to bring a smile)
5. Zain the Colt (a playful reference to a young, energetic horse)

Remember, these are just for fun, and I'm sure you're more than just a nickname!
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
