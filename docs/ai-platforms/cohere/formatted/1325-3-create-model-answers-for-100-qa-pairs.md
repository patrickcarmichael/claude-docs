---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3. Create model answers for 100 QA pairs

Now that we have a running pipeline, we need to assess its performance.

The author of the repository provides 100 QA pairs that we can test the model on. Let's download these questions, then run inference on all 100 questions. Later, we will use Command A -- Cohere's largest and most powerful model -- to measure performance.
```python PYTHON
url = "https://github.com/siagholami/aws-documentation/blob/main/QA_true.csv?raw=true"
qa_pairs = pd.read_csv(url)
qa_pairs.sample(2)
```
We'll use the fields as follows:

* `Question`: the user question, passed to `co.chat` to generate the answer
* `Answer_True`: treat as the ground gruth; compare to the model-generated answer to determine its correctness
* `Document_True`: treat as the (single) golden document; check the rank of this document inside the model's retrieved documents

We'll loop over each question and generate our model answer. We'll also complete two steps that will be useful for evaluating our model next:

1. We compute the rank of the golden document amid the retrieved documents -- this will inform how well our retrieval system performs
2. We prepare the grading prompts -- these will be sent to an LLM scorer to compute the goodness of responses
```python PYTHON

LLM_EVAL_TEMPLATE = """## References

{references}

QUESTION: based on the above reference documents, answer the following question: {question}
ANSWER: {answer}
STUDENT RESPONSE: {completion}

Based on the question and answer above, grade the studen't reponse. A correct response will contain exactly \
the same information as in the answer, even if it is worded differently. If the student's reponse is correct, \
give it a score of 1. Otherwise, give it a score of 0. Let's think step by step. Return your answer as \
as a compilable JSON with the following structure:
{{
    "reasoning": <reasoning>,
    "score: <score 0="" 1="" of="" or="">,
}}"""


def get_rank_of_golden_within_retrieved(golden: str, retrieved: List[dict]) -> int:
    """
    Returns the rank that the golden document (single) has within the retrieved documents
    * `golden` contains the source of the document, e.g. 'amazon-ec2-user-guide/EBSEncryption.md'
    * `retrieved` has a list of responses with key 'llamaindex_id', which links back to document sources
    """
    # Create {document: rank} map using llamaindex_id (count first occurrence of any document; they can

    # appear multiple times because they're chunked)

    doc_to_rank = {}
    for rank, doc in enumerate(retrieved):
        # retrieve source of document

        _id = doc["llamaindex_id"]
        source = data["train"][map_id2index[_id]]["source"]
        # format as in dataset

        source = source[stub_len:]  # remove stub

        source = source.replace("/doc_source", "")  # remove /doc_source/

        if source not in doc_to_rank:
            doc_to_rank[source] = rank + 1

    # Return rank of `golden`, defaulting to len(retrieved) + 1 if it's absent

    return doc_to_rank.get(golden, len(retrieved) + 1)
```
```python PYTHON
from tqdm import tqdm

answers = []
golden_answers = []
ranks = []
grading_prompts = []  # best computed in batch

for _, row in tqdm(qa_pairs.iterrows(), total=len(qa_pairs)):
    query, golden_answer, golden_doc = row["Question"], row["Answer_True"], row["Document_True"]
    golden_answers.append(golden_answer)

    # --- Produce answer using retriever ---

    documents = retriever.retrieve(query, top_n=top_n)
    resp = co.chat(message=query, model="command-r-08-2024", temperature=0., documents=documents)
    answer = resp.text
    answers.append(answer)

    # --- Do some prework for evaluation later ---

    # Rank

    rank = get_rank_of_golden_within_retrieved(golden_doc, documents)
    ranks.append(rank)
    # Score: construct the grading prompts for LLM evals, then evaluate in batch

    # Need to reformat documents slightly

    documents = [{"index": str(i), "text": doc["text"]} for i, doc in enumerate(documents)]
    references_text = "\n\n".join("\n".join([f"{k}: {v}" for k, v in doc.items()]) for doc in documents)
    # ^ snippet looks complicated, but all it does it unpack all kwargs from `documents`

    # into text separated by \n\n

    grading_prompt = LLM_EVAL_TEMPLATE.format(
        references=references_text, question=query, answer=golden_answer, completion=answer,
    )
    grading_prompts.append(grading_prompt)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
