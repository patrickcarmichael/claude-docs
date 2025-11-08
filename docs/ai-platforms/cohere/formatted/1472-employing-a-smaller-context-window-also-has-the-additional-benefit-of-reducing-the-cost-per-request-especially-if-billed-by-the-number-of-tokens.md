---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Employing a smaller context window also has the additional benefit of reducing the cost per request, especially if billed by the number of tokens.

MAX_TOKENS = 40000

def truncate(long: str, max_tokens: int) -> str:
    """
    Shortens `long` by brutally truncating it to the first `max_tokens` tokens.
    This can break up sentences, passages, etc.
    """

    tokenized = co.tokenize(text=long, model=co_model).token_strings
    truncated = tokenized[:max_tokens]
    short = "".join(truncated)
    return short
```
```python PYTHON
short_text = truncate(long_text, MAX_TOKENS)

prompt = prompt_template.format(document=short_text)
print(generate_response(message=prompt))
```
The document discusses the impact of a specific protein, p53, on the process of angiogenesis, which is the growth of new blood vessels. Angiogenesis plays a critical role in various physiological processes, including wound healing and embryonic development. The presence of the p53 protein can inhibit angiogenesis by regulating the expression of certain genes and proteins. This inhibition can have significant implications for tumor growth, as angiogenesis is essential for tumor progression. Therefore, understanding the role of p53 in angiogenesis can contribute to our knowledge of tumor suppression and potential therapeutic interventions.

Additionally, the document mentions that the regulation of angiogenesis by p53 occurs independently of the protein's role in cell cycle arrest and apoptosis, which are other key functions of p53 in tumor suppression. This suggests that p53 has a complex and multifaceted impact on cellular processes.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
