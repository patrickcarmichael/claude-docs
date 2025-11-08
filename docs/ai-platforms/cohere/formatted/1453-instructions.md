---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## instructions

Step 1. Read the entire text from the first to the last page.
Step 2. Create a summary of every chapter from the first to the last page.
"""

chunked = build_simple_chunks(text, n_sentences=30)
resp = co.chat(
  preamble=summarize_preamble,
  message=instructions,
  documents=[{"text": chunk} for chunk in chunked],
  model=co_model,
  temperature=0.3,
  return_prompt=True
)

num_tokens_in = co.tokenize(resp.prompt).length
num_tokens_out = resp.meta["billed_units"]["output_tokens"]
print(f"Generated summary with {num_tokens_in} tokens in, {num_tokens_out} tokens out")
print()
print("--- Summary with citations using grounded generation in Command-R ---")
print()
print(resp.text)
```
Let's display the citations inside our answer:
```python PYTHON
print(insert_citations(resp.text, resp.citations))
```
We can now visualise which section of the answer is based on which passage in the main text. Verifying factuality is straightforward: pick a section and verify that the relevant information is contained in the cited chunk.

For instance, let's verify the statement
```
Around 40% of employment worldwide is exposed to AI [1, 6]
```
by checking its chunk:
```python PYTHON
print(chunked[6])
```
Seems convincing!
By repeating such checks, it's straightforward to build trust in your summaries.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
