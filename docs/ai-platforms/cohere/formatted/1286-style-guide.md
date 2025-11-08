---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Style Guide

Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.
"""
```
```python PYTHON
documents = [
    {"title": "chunk 0", "snippet": top_chunks_after_rerank[0]},
    {"title": "chunk 1", "snippet": top_chunks_after_rerank[1]},
    {"title": "chunk 2", "snippet": top_chunks_after_rerank[2]},
  ]

response = co.chat(
  message=query,
  documents=documents,
  preamble=preamble,
  model="command-r",
  temperature=0.3
)

print("Final answer:")
print(response.text)
```
```txt title="Output"
Final answer:
Here are the key crew members involved in 'Dune: Part Two':

- Denis Villeneuve: director and producer
- Jon Spaihts: co-writer of the screenplay
- Mary Parent and Cale Boyter: producers
- Tanya Lapointe, Brian Herbert, Byron Merritt, Kim Herbert, Thomas Tull, Richard P. Rubinstein, John Harrison, Herbert W. Gain and Kevin J. Anderson: executive producers
- Joe Walker: editor
- Brad Riker: supervising art director
- Patrice Vermette: production designer
- Paul Lambert: visual effects supervisor
- Gerd Nefzer: special effects supervisor
- Thomas Struthers: stunt coordinator.

A number of crew members from the first film returned for the sequel, which is set to be released in 2024.
```
Note: this is indeed the answer you'd expect, and here was the passage of text in wikipedia explaining it!

" \[...] Dune: Part Two was originally scheduled to be released on October 20, 2023, but was delayed to November 17, 2023, before moving forward two weeks to November 3, 2023, to adjust to changes in release schedules from other studios. It was later postponed by over four months to March 15, 2024, due to the 2023 Hollywood labor disputes. After the strikes were resolved, the film moved once more up two weeks to March 1, 2024. \[...]"

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
