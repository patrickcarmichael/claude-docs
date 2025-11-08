---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1. Setup \[#setup]

```python PYTHON
%%capture

import cohere
import networkx as nx
import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize
import numpy as np
import spacy

from collections import deque
from getpass import getpass
import re
from typing import List, Tuple

co_api_key = getpass("Enter your Cohere API key: ")
co_model = "command-a-03-2025"
co = cohere.Client(co_api_key)
```
```python PYTHON

from google.colab import drive
drive.mount("/content/drive", force_remount=True)

fpath = "drive/Shareddrives/FDE/Cookbooks/Long-form summarisation/ai_and_future_of_work.txt"
with open(fpath, "r") as f:
  text = f.read()

num_tokens = co.tokenize(text).length
print(f"Loaded IMF report with {num_tokens} tokens")
```

### Aside: define utils

```python PYTHON

def split_text_into_sentences(text: str) -> List[str]:
    sentences =  sent_tokenize(text)
    return sentences

def group_sentences_into_passages(sentence_list: List[str], n_sentences_per_passage: int = 10):
    """
    Group sentences into passages of n_sentences sentences.
    """
    passages = []
    passage = ""
    for i, sentence in enumerate(sentence_list):
        passage += sentence + " "
        if (i + 1) % n_sentences_per_passage == 0:
            passages.append(passage)
            passage = ""
    return passages

def build_simple_chunks(text, n_sentences: int = 10):
    """
    Build chunks of text from the input text.
    """
    sentences = split_text_into_sentences(text)
    chunks = group_sentences_into_passages(sentences, n_sentences_per_passage=n_sentences)
    return chunks


def insert_citations(text: str, citations: List[dict]):
    """
    A helper function to pretty print citations.
    """
    offset = 0
    # Process citations in the order they were provided

    for citation in citations:
        # Adjust start/end with offset

        start, end = citation['start'] + offset, citation['end'] + offset
        placeholder = "[" + ", ".join(doc[4:] for doc in citation["document_ids"]) + "]"
        # ^ doc[4:] removes the 'doc_' prefix, and leaves the quoted document

        modification = f'{text[start:end]} {placeholder}'
        # Replace the cited text with its bolded version + placeholder

        text = text[:start] + modification + text[end:]
        # Update the offset for subsequent replacements

        offset += len(modification) - (end - start)

    return text


def textrank(text: str, co, max_tokens: int, n_sentences_per_passage: int) -> str:
    """
    Shortens `text` by extracting key units of text from `text` based on their centrality and concatenating them.
    The output is the concatenation of those key units, in their original order. Centrality is graph-theoretic
    measure of connectedness of a node; the more connected a node is to surrounding nodes (and the more sparsely
    those neighbours are connected), the higher centrality.

    Key passages are identified via clustering in a three-step process:
    1. Break up `long` into chunks (either sentences or passages, based on `unit`)
    2. Embed each chunk using Cohere's embedding model and construct a similarity matrix
    3. Compute the centrality of each chunk
    4. Keep the highest-centrality chunks until `max_tokens` is reached
    5. Put together shorterned text by reordering chunks in their original order

    This approach is based on summarise.long_doc_summarization.extraction::extract_single_doc with sorting by
    centrality. Adapted here because installing the `summarise` repo would have added a lot of unused functionalities
    and dependencies.
    """

    # 1. Chunk text into units

    chunks = build_simple_chunks(text, n_sentences_per_passage)

    # 2. Embed and construct similarity matrix

    embeddings = np.array(
        co.embed(
            texts=chunks,
            model="embed-v4.0",
            input_type="clustering",
        ).embeddings
    )
    similarities = np.dot(embeddings, embeddings.T)

    # 3. Compute centrality and sort sentences by centrality

    # Easiest to use networkx's `degree` function with similarity as weight

    g = nx.from_numpy_array(similarities, edge_attr="weight")
    centralities = g.degree(weight="weight")
    idcs_sorted_by_centrality = [node for node, degree in sorted(centralities, key=lambda item: item[1], reverse=True)]

    # 4. Add chunks back in order of centrality

    selected = _add_chunks_by_priority(co, chunks, idcs_sorted_by_centrality, max_tokens)

    # 5. Put condensed text back in original order

    separator = "\n"
    short = separator.join([chunk for index, chunk in sorted(selected, key=lambda item: item[0], reverse=False)])

    return short


def _add_chunks_by_priority(
    co, chunks: List[str], idcs_sorted_by_priority: List[int], max_tokens: int
) -> List[Tuple[int, str]]:
    """
    Given chunks of text and their indices sorted by priority (highest priority first), this function
    fills the model context window with as many highest-priority chunks as possible.

    The output is a list of (index, chunk) pairs, ordered by priority. To stitch back the chunks into
    a cohesive text that preserves chronological order, sort the output on its index.
    """

    selected = []
    num_tokens = 0
    idcs_queue = deque(idcs_sorted_by_priority)

    while num_tokens < max_tokens and len(idcs_queue) > 0:
        next_idx = idcs_queue.popleft()
        num_tokens += co.tokenize(chunks[next_idx]).length - 2
        # num_tokens += len(tokenizer.encode(chunks[next_idx]).ids) - 2

        # ^ removing BOS and EOS tokens from count

        selected.append((next_idx, chunks[next_idx]))
        # ^ keep index and chunk, to reorder chronologically

    if num_tokens > max_tokens:
        selected.pop()

    return selected
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
