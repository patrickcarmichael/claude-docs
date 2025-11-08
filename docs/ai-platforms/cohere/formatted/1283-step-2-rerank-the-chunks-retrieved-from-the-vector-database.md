---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2 - Rerank the chunks retrieved from the vector database

We rerank the 10 chunks retrieved from the vector database. Reranking boosts retrieval accuracy.

Reranking lets us go from 10 chunks retrieved from the vector database, to the 3 most relevant chunks.
```python PYTHON
response = co.rerank(
    query=query,
    documents=top_chunks_after_retrieval,
    top_n=3,
    model="rerank-english-v2.0",
)

top_chunks_after_rerank = [result.document['text'] for result in response]
print("Here are the top 3 chunks after rerank: ")
for t in top_chunks_after_rerank:
    print("== " + t)
```
```txt title="Output"
Here are the top 3 chunks after rerank:
== Dune: Part Two is a 2024 American epic science fiction film directed and produced by Denis Villeneuve, who co-wrote the screenplay with Jon Spaihts. The sequel to Dune (2021) adapts the 1965 novel Dune by Frank Herbert and follows Paul Atreides as he unites with the Fremen people of the desert planet Arrakis to wage war against House Harkonnen. Timothée Chalamet, Rebecca Ferguson, Josh Brolin, Stellan Skarsgård, Dave Bautista, Zendaya, Charlotte Rampling, and Javier Bardem reprise their roles from the first
== stunt coordinator. Dune: Part Two was produced by Villeneuve, Mary Parent, and Cale Boyter, with Tanya Lapointe, Brian Herbert, Byron Merritt, Kim Herbert, Thomas Tull, Jon Spaihts, Richard P. Rubinstein, John Harrison, and Herbert W. Gain serving as executive producers and Kevin J. Anderson as creative consultant. Legendary CEO Joshua Grode confirmed in April 2019 that they plan to make a sequel, adding that "there's a logical place to stop the [first] movie before the book is over".In December 2020,
== series. Villeneuve ultimately secured a two-film deal with Warner Bros. Pictures, in the same style as the two-part adaption of Stephen King's It in 2017 and 2019. In January 2019, Joe Walker was confirmed to be serving as the film's editor. Other crew included Brad Riker as supervising art director, Patrice Vermette as production designer, Paul Lambert as visual effects supervisor, Gerd Nefzer as special effects supervisor, and Thomas Struthers as stunt coordinator. Dune: Part Two was produced by
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
