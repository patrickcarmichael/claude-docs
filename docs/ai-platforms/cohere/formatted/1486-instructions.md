---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## instructions

Your task is to assist a user in writing a short biography for social media.
The length of the text should be no more than 100 words.
Write the summary in first person.'''
```
```python PYTHON
response = co.chat(
    message=original_prompt,
    model='command-r',
)
```
```python PYTHON
print(response.text)
```
```txt
    I'm a Senior Software Engineer at GlobalSolTech, with over 15 years of experience in AI and machine learning. My expertise lies in developing innovative algorithms for natural language processing, computer vision, and recommendation systems. I hold a B.Sc. in Physics and a Ph.D. in Statistics and enjoy hiking, free diving, and collecting vintage watches in my spare time. I'm passionate about using my skills to contribute to cutting-edge AI research and development. At GlobalSolTech, I'm proud to be part of a dynamic team driving technological advancement.
```
Using Command-R, we can automatically upgrade the original prompt to a RAG-style prompt to get more faithful adherence to the instructions, a clearer and more concise prompt, and in-line citations for free. Consider the following meta-prompt:
```python PYTHON
meta_prompt = f'''Below is a task for an LLM delimited with ## Original Task. Your task is to split that task into two parts: (1) the context; and (2) the instructions.

The context should be split into several separate parts and returned as a JSON object where each part has a name describing its contents and the value is the contents itself.
Make sure to include all of the context contained in the original task description and do not change its meaning.
The instructions should be re-written so that they are very clear and concise. Do not change the meaning of the instructions or task, just make sure they are very direct and clear.
Return everything in a JSON object with the following structure:

{{
  "context": [{{"<description 1="" of="" part="">": "<content 1="" of="" part="">"}}, ...],
  "instructions": "<the instructions="" re-written="">"
}}

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
