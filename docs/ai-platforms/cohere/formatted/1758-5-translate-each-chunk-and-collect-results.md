---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 5. Translate each chunk and collect results

translated_chunks = []
for chunk in chunks:
    prompt = prompt_template.format(target_language=target_language) + chunk
    response = co.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    translated = response.message.content[0].text
    translated_chunks.append(translated)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
