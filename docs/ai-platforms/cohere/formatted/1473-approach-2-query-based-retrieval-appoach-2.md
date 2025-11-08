---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Approach 2: Query Based Retrieval \[#appoach-2]

In this section we present how we can leverage a query retriereval based approach to generate an answer to the following question: `Based on the document, are there any risks related to Elon Musk?`.

The solution is outlined below and can be broken down into four functional steps.

1. Chunk the text into units

   * Here we employ a simple chunking algorithm. More information about different chunking strategies can be found \[here]\(TODO: link to chunking post).

2. Use a ranking algorithm to rank chunks against the query

   * We leverage another Cohere endpoint, `co.rerank` ([docs link](https://docs.cohere.com/reference/rerank-1)), to rank each chunk against the query.

3. Keep the most-relevant chunks until context limit is reached

   * `co.rerank` returns a relevance score, facilitating the selection of the most pertinent chunks. We can choose the most relevant chunks based on this score.

4. Put condensed text back in original order
   * Finally, we arrange the chosen chunks in their original sequence as they appear in the document.

See `query_based_retrieval` function for the starting point.

### Query based retrieval implementation

```python PYTHON
def split_text_into_sentences(text) -> List[str]:
    """
    Split the input text into a list of sentences.
    """
    sentences = sent_tokenize(text)

    return sentences

def group_sentences_into_passages(sentence_list, n_sentences_per_passage=5):
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

def build_simple_chunks(text, n_sentences=5):
    """
    Build chunks of text from the input text.
    """
    sentences = split_text_into_sentences(text)
    chunks = group_sentences_into_passages(sentences, n_sentences_per_passage=n_sentences)
    return chunks
```
```python PYTHON
sentences = split_text_into_sentences(long_text)
passages = group_sentences_into_passages(sentences, n_sentences_per_passage=5)
print('Example sentence:', np.random.choice(np.asarray(sentences), size=1, replace=False))
print()
print('Example passage:', np.random.choice(np.asarray(passages), size=1, replace=False))
```
```txt title="Output"
Example sentence: ['4.']

Example passage: ['T echnical robustness and safety means that AI systems are developed  and used in a way that allows robustness in case of problems and resilience against  attempts to alter the use or performance of the AI system so as to allow unlawful use by  third parties, a nd minimise unintended harm. Privacy and data governance means that AI  systems are developed and used in compliance with existing privacy and data protection  rules, while processing data that meets high standards in terms of quality and integrity. Transpar ency means that AI systems are developed and used in a way that allows  appropriate traceability and explainability, while making humans aware that they  communicate or interact with an AI system, as well as duly informing deployers of the  capabilities and l imitations of that AI system and affected persons about their rights. Diversity, non - discrimination and fairness means that AI systems are developed and used  in a way that includes diverse actors and promotes equal access, gender equality and  cultural dive rsity, while avoiding discriminatory impacts and unfair biases that are  prohibited by Union or national law. Social and environmental well - being means that AI  systems are developed and used in a sustainable and environmentally friendly manner as  well as in   a way to benefit all human beings, while monitoring and assessing the long - term  impacts on the individual, society and democracy. ']
```
```python PYTHON
def _add_chunks_by_priority(
    chunks: List[str],
    idcs_sorted_by_priority: List[int],
    max_tokens: int,
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
        num_tokens += len(co.tokenize(text=chunks[next_idx], model=co_model).tokens)
        # keep index and chunk, to reorder chronologically

        selected.append((next_idx, chunks[next_idx]))
    if num_tokens > max_tokens:
        selected.pop()

    return selected

def query_based_retrieval(
    long: str,
    max_tokens: int,
    query: str,
    n_setences_per_passage: int = 5,
) -> str:
    """
    Performs query-based retrieval on a long text document.
    """
    # 1. Chunk text into units

    chunks = build_simple_chunks(long, n_setences_per_passage)

    # 2. Use co.rerank to rank chunks vs. query

    chunks_reranked = co.rerank(query=query, documents=chunks, model="rerank-english-v3.0")
    idcs_sorted_by_relevance = [
        chunk.index for chunk in sorted(chunks_reranked.results, key=lambda c: c.relevance_score, reverse=True)
    ]

    # 3. Add chunks back in order of relevance

    selected = _add_chunks_by_priority(chunks, idcs_sorted_by_relevance, max_tokens)

    # 4. Put condensed text back in original order

    separator = " "
    short = separator.join([chunk for index, chunk in sorted(selected, key=lambda item: item[0], reverse=False)])
    return short
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
