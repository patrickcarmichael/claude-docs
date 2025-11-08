---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## question

{question}"""

full_context_prompt = prompt_template.format(tenk=edgar_10k, question=PROMPT)
```
```python PYTHON
r1 = get_response(PROMPT, rag=True)
r2 = get_response(full_context_prompt, rag=False)
```
```python PYTHON
def get_price(r):
    return (r.token_count["prompt_tokens"] * 0.5 / 10e6) + (r.token_count["response_tokens"] * 1.5 / 10e6)
```
```python PYTHON
rag_price = get_price(r1)
full_context_price = get_price(r2)

print(f"RAG is {(full_context_price - rag_price) / full_context_price:.0%} cheaper than full context")
```
```txt title="Output"
RAG is 93% cheaper than full context
```
```python PYTHON
%timeit get_response(PROMPT, rag=True)
```
```txt title="Output"
14.9 s ± 1.4 s per loop (mean ± std. dev. of 7 runs, 1 loop each)
```
```python PYTHON
%timeit get_response(full_context_prompt, rag=False)
```
```txt title="Output"
22.7 s ± 7.43 s per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
