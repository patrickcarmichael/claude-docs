---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting Started

You can perform translation of a text into another language with a simple prompt asking the model to translate a piece of text. In the sample below, we are doing this 'programmatically' by passing both the target language and content to translate as variables, but you can also just pass in a `message` saying `"Please translate this into <target_language> for me."`
```python PYTHON 
from cohere import ClientV2

co = ClientV2(api_key="<YOUR API KEY>")

target_language = "Spanish"
content_to_translate = "Enterprises rely on translation for some of their most sensitive and business-critical documents and cannot risk data leakage, compliance violations, or misunderstandings. Mistranslated documents can reduce trust and have strategic implications."

message = f"Translate everything that follows into {target_language}:\n\n{content_to_translate}"
response = co.chat(
    model="command-a-translate-08-2025",
    messages=[{"role": "user", "content": message}],
)
print(response.message.content[0].text)
```
Here’s a sample output:
```mdx
Las empresas dependen de la traducción para algunos de sus documentos más sensibles y críticos para su negocio y no pueden permitirse el riesgo de fugas de datos, incumplimientos normativos o malentendidos. Los documentos mal traducidos pueden reducir la confianza y tener implicaciones estratégicas.
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
