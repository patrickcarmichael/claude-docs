---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 4. Evaluate model performance

We want to test our model performance on two dimensions:

1. How good is the final answer? We'll compare our model answer to the golden answer using Command A as a judge.
2. How good is the retrieval? We'll use the rank of the golden document within the retrieved documents to this end.

Note that this pipeline is for illustration only. To measure performance in practice, we would want to run more in-depths tests on a broader, representative dataset.
```python PYTHON
results = pd.DataFrame()
results["answer"] = answers
results["golden_answer"] = qa_pairs["Answer_True"]
results["rank"] = ranks
```

### 4.1 Compare answer to golden answer

We'll use Command A as a judge of whether the answers produced by our model convey the same information as the golden answers. Since we've defined the grading prompts earlier, we can simply ask our LLM judge to evaluate that grading prompt. After a little bit of postprocessing, we can then extract our model scores.
````python PYTHON
scores = []
reasonings = []

def remove_backticks(text: str) -> str:
  """
  Some models are trained to output JSON in Markdown formatting:
```json {json object}```
  Remove the backticks from those model responses so that they become
  parasable by json.loads.
  """
  if text.startswith("```json"):
      text = text[7:]
  if text.endswith("```"):
      text = text[:-3]
  return text


for prompt in tqdm(grading_prompts, total=len(grading_prompts)):
  resp = co.chat(message=prompt, model="command-a-03-2025", temperature=0.)
  # Convert response to JSON to extract the `score` and `reasoning` fields

  # We remove backticks for compatibility with different LLMs

  parsed = json.loads(remove_backticks(resp.text))
  scores.append(parsed["score"])
  reasonings.append(parsed["reasoning"])
````
```python PYTHON
results["score"] = scores
results["reasoning"] = reasonings
```
```python PYTHON
print(f"Average score: {results['score'].mean():.3f}")
```

### 4.2 Compute rank

We've already computed the rank of the golden documents using `get_rank_of_golden_within_retrieved`. Here, we'll plot the histogram of ranks, using blue when the answer scored a 1, and red when the answer scored a 0.
```python PYTHON
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid", rc={"grid.color": ".8"})

results["rank_shifted_left"] = results["rank"] - 0.1
results["rank_shifted_right"] = results["rank"] + 0.1

f, ax = plt.subplots(figsize=(5, 3))
sns.histplot(data=results.loc[results["score"] == 1], x="rank_shifted_left", color="skyblue", label="Correct answer", binwidth=1)
sns.histplot(data=results.loc[results["score"] == 0], x="rank_shifted_right", color="red", label="False answer", binwidth=1)

ax.set_xticks([1, 5, 0, 10, 15, 20])
ax.set_title("Rank of golden document (max means golden doc. wasn't retrieved)")
ax.set_xlabel("Rank")
ax.legend();
```
We see that retrieval works well overall: for 80% of questions, the golden document is within the top 5 documents. However, we also notice that approx. half the false answers come from instances where the golden document wasn't retrieved (`rank = top_k = 20`). This should be improved, e.g. by adding metadata to the documents such as their section headings, or altering the chunking strategy.

There is also a non-negligible instance of false answers where the top document was retrieved. On closer inspection, many of these are due to the model phrasing its answers more verbosely than the (very laconic) golden documents. This highlights the importance of checking eval results before jumping to conclusions about model performance.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
