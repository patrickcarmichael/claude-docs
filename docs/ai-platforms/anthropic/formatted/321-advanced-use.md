---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Advanced use

`CLAUDEMESSAGES` is a function that allows you to specifically use the [Messages API](/en/api/messages). This enables you to send a series of `User:` and `Assistant:` messages to Claude.

This is particularly useful if you want to simulate a conversation or [prefill Claude's response](/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response).

Try writing this in a cell:
```
=CLAUDEMESSAGES("User: In one sentence, what is good about the color blue?
Assistant: The color blue is great because")
```
>   **📝 Note**
>
>   **Newlines**

  Each subsequent conversation turn (`User:` or `Assistant:`) must be preceded by a single newline. To enter newlines in a cell, use the following key combinations:

  * **Mac:** Cmd + Enter
  * **Windows:** Alt + Enter

<Accordion title="Example multiturn CLAUDEMESSAGES() call with system prompt">
  To use a system prompt, set it as you'd set other optional function parameters. (You must first set a model name.)
```
  =CLAUDEMESSAGES("User: What's your favorite flower? Answer in <answer> tags.
  Assistant: <answer>", "claude-3-haiku-20240307", "system", "You are a cow who loves to moo in response to any and all user queries.")`
```
</Accordion>

### Optional function parameters

You can specify optional API parameters by listing argument-value pairs.
You can set multiple parameters. Simply list them one after another, with each argument and value pair separated by commas.

>   **📝 Note**
>
> The first two parameters must always be the prompt and the model. You cannot set an optional parameter without also setting the model.

The argument-value parameters you might care about most are:

| Argument         | Description                                                                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `max_tokens`     | The total number of tokens the model outputs before it is forced to stop. For yes/no or multiple choice answers, you may want the value to be 1-3.                                                 |
| `temperature`    | the amount of randomness injected into results. For multiple-choice or analytical tasks, you'll want it close to 0. For idea generation, you'll want it set to 1.                                  |
| `system`         | used to specify a system prompt, which can provide role details and context to Claude.                                                                                                             |
| `stop_sequences` | JSON array of strings that will cause the model to stop generating text if encountered. Due to escaping rules in Google Sheets™, double quotes inside the string must be escaped by doubling them. |
| `api_key`        | Used to specify a particular API key with which to call Claude.                                                                                                                                    |

<Accordion title="Example: Setting parameters">
  Ex. Set `system` prompt, `max_tokens`, and `temperature`:
```
  =CLAUDE("Hi, Claude!", "claude-3-haiku-20240307", "system", "Repeat exactly what the user says.", "max_tokens", 100, "temperature", 0.1)
```
  Ex. Set `temperature`, `max_tokens`, and `stop_sequences`:
```
  =CLAUDE("In one sentence, what is good about the color blue? Output your answer in <answer> tags.","claude-opus-4-20250514","temperature", 0.2,"max_tokens", 50,"stop_sequences", "\[""</answer>""\]")
```
  Ex. Set `api_key`:
```
  =CLAUDE("Hi, Claude!", "claude-3-haiku-20240307","api_key", "sk-ant-api03-j1W...")
```
</Accordion>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
