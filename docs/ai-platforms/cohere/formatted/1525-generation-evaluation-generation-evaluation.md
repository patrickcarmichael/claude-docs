---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generation Evaluation \[#generation-evaluation]

Evaluating grounded generation (the second step of RAG) is notoriously difficult, because generations are usually complex and rich of information, and simply labelling an answer as "good" or "bad" is not enough.
To overcome this issue, we first decompose complex answers into a set of basic *claims*, where a claim is any sentence or part of a sentence in the answer that expresses a verifiable fact. Subsequently, we check the validity of each claim independently, defining the overall quality of the answer based on the correctness of the claims it includes.

We use claims to compute three metrics:

* **Faithfulness**, which measures how many of the claims in the generated response are supported by the retrieved documents. This is a fundamental metric, as it tells us how *grounded* in the documents the response is, and, contextually, it allows us to spot hallucinations

* **Correctness**, which checks which claims in the response also occur in the gold answer

* And **Coverage**, by which we assess how many of the claims in the gold answer are included in the generated response.

Note that Faithfulness and Correctness share the exact same approach, the difference being that the former checks the claims against the supporting docs, while the latter against the golden answer.
Also, while Correctness is measuring the precision of the claims in the response, Coverage can be seen as complementary, as it measures recall.

### Claim Extraction

Let's now see how we implement the evaluation described above using LLMs. Let's start with **claim extraction**.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
