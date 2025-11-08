---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1.3: Pick one article and find the most similar articles

Next, we pick any one article to be the one the reader is currently reading (let's call this the target) and find other articles with the most similar embeddings (let's call these candidates) using cosine similarity.

[Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) is a metric that measures how similar sequences of numbers are (embeddings in our case), and we compute it for each target-candidate pair.
```python PYTHON
print(f'Choose one article ID between {INP_START} and {INP_END-1} below...')
```
```
Choose one article ID between 0 and 99 below...
```
```python PYTHON
READING_IDX = 70

reading = embeds[READING_IDX]
```
```python PYTHON

from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(target,candidates):
  # Turn list into array

  candidates = np.array(candidates)
  target = np.expand_dims(np.array(target),axis=0)

  # Calculate cosine similarity

  similarity_scores = cosine_similarity(target,candidates)
  similarity_scores = np.squeeze(similarity_scores).tolist()

  # Sort by descending order in similarity

  similarity_scores = list(enumerate(similarity_scores))
  similarity_scores = sorted(similarity_scores, key=lambda x:x[1], reverse=True)

  # Return similarity scores

  return similarity_scores
```
```python PYTHON
similarity = get_similarity(reading,embeds)

print('Target:')
print(f'[ID {READING_IDX}]',df_inputs['Text'][READING_IDX][:100],'...','\n')

print('Candidates:')
for i in similarity[1:6]: # Exclude the target article

  print(f'[ID {i[0]}]',df_inputs['Text'][i[0]][:100],'...')
```
```
Target:
[ID 70] aragones angered by racism fine spain coach luis aragones is furious after being fined by the spanis ...

Candidates:
[ID 23] ferguson urges henry punishment sir alex ferguson has called on the football association to punish a ...
[ID 51] mourinho defiant on chelsea form chelsea boss jose mourinho has insisted that sir alex ferguson and  ...
[ID 73] balco case trial date pushed back the trial date for the bay area laboratory cooperative (balco) ste ...
[ID 41] mcleish ready for criticism rangers manager alex mcleish accepts he is going to be criticised after  ...
[ID 42] premier league planning cole date the premier league is attempting to find a mutually convenient dat ...
```
<img alt="Step 2 - Classify" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/article-recommender/article-rec-3.png" />

Two articles may be similar but they may not necessarily belong to the same category. For example, an article about a sports team manager facing a fine may be similar to another about a business entity facing a fine, but they are not of the same category.

Perhaps we can make the system better by only recommending articles of the same category. For this, let's build a news category classifier.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
