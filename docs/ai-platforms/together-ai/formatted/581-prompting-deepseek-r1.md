---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Prompting DeepSeek R1

Source: https://docs.together.ai/docs/prompting-deepseek-r1

Prompt engineering for DeepSeek-R1.

Prompting DeepSeek-R1, and other reasoning models in general, is quite different from working with non-reasoning models.

Below we provide guidance on how to get the most out of DeepSeek-R1:

* **Clear and specific prompts**: Write your instructions in plain language, clearly stating what you want. Complex, lengthy prompts often lead to less effective results.
* **Sampling parameters**: Set the `temperature` within the range of 0.5-0.7 (0.6 is recommended) to prevent endless repetitions or incoherent outputs. Also, a `top-p` of 0.95 is recommended.
* **No system prompt**: Avoid adding a system prompt; all instructions should be contained within the user prompt.
* **No few-shot prompting**: Do not provide examples in the prompt, as this consistently degrades model performance. Rather, describe in detail the problem, task, and output format you want the model to accomplish. If you do want to provide examples, ensure that they align very closely with your prompt instructions.
* **Structure your prompt**: Break up different parts of your prompt using clear markers like XML tags, markdown formatting, or labeled sections. This organization helps ensure the model correctly interprets and addresses each component of your request.
* **Set clear requirements**: When your request has specific limitations or criteria, state them explicitly (like "Each line should take no more than 5 seconds to say..."). Whether it's budget constraints, time limits, or particular formats, clearly outline these parameters to guide the model's response.
* **Clearly describe output**: Paint a clear picture of your desired outcome. Describe the specific characteristics or qualities that would make the response exactly what you need, allowing the model to work toward meeting those criteria.
* **Majority voting for responses**: When evaluating model performance, it is recommended to generate multiple solutions and then use the most frequent results.
* **No chain-of-thought prompting**: Since these models always reason prior to answering the question, it is not necessary to tell them to "Reason step by step..."
* **Math tasks**: For mathematical problems, it is advisable to include a directive in your prompt such as: "Please reason step by step, and put your final answer within `\boxed{}`."
* **Forcing `<think>`**: On rare occasions, DeepSeek-R1 tends to bypass the thinking pattern, which can adversely affect the model's performance. In this case, the response will not start with a `<think>` tag. If you see this problem, try telling the model to start with the `<think>` tag.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
