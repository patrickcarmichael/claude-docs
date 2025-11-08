---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## First we will just generate the prompts and examine them


def generate_prompts(document: str, chunks: List[str]) -> List[str]:
    prompts = []
    for chunk in chunks:
        prompt = CONTEXTUAL_RAG_PROMPT.format(
            WHOLE_DOCUMENT=document,
            CHUNK_CONTENT=chunk,
        )
        prompts.append(prompt)
    return prompts


prompts = generate_prompts(pg_essay, chunks)


def generate_context(prompt: str):
    """
    Generates a contextual response based on the given prompt using the specified language model.
    Args:
        prompt (str): The input prompt to generate a response for.
    Returns:
        str: The generated response content from the language model.
    """
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
    )
    return response.choices[0].message.content
```

We can now use the functions above to generate context for each chunk and append it to the chunk itself:
```py

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
