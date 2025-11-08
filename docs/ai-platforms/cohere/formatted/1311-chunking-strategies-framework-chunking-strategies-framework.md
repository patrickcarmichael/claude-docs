---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Chunking strategies framework \[#chunking-strategies-framework]

### Document splitting

By document splitting, we mean deciding on the conditions under which we will break the text. At this stage, we should ask, *"Are there any parts of consecutive text we want to ensure we do not break?"*. If the answer is "no", then, the content-independent splitting strategies are helpful. On the other hand, in scenarios like transcripts or meeting notes, we probably would like to keep the content of one speaker together, which might require us to deploy content-dependent strategies.

#### Content-independent splitting strategies

We split the document based on some content-independent conditions, among the most popular ones are:

* splitting by the number of characters,
* splitting by sentence,
* splitting by a given character, for example, `\n` for paragraphs.

The advantage of this scenario is that we do not need to make any assumptions about the text. However, some considerations remain, like whether we want to preserve some semantic structure, for example, sentences or paragraphs. Sentence splitting is better suited if we are looking for small chunks to ensure accuracy. Conversely, paragraphs preserve more context and might be more useful in open-ended questions.

#### Content-dependent splitting strategies

On the other hand, there are scenarios in which we care about preserving some text structure. Then, we develop custom splitting strategies based on the document's content. A prime example is call transcripts. In such scenarios, we aim to ensure that one person's speech is fully contained within a chunk.

### Creating chunks from the document splits

After the document is split, we need to decide on the desired **size** of our chunks (the split only defines how we break the document, but we can create bigger chunks from multiple splits).

Smaller chunks support more accurate retrieval. However, they might lack context. On the other hand, larger chunks offer more context, but they reduce the effectiveness of the retrieval. It is important to experiment with different settings to find the optimal balance.

### Overlapping chunks

Overlapping chunks is a useful technique to have in the toolbox. Especially when we employ content-independent splitting strategies, it helps us mitigate some of the pitfalls of breaking the document without fully understanding the text. Overlapping guarantees that there is always some buffer between the chunks, and even if an important piece of information might be split in the original splitting strategy, it is more probable that the full information will be captured in the next chunk. The disadvantage of this method is that it creates redundancy.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
