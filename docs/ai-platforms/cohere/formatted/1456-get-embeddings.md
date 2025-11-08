---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Get embeddings

Here we have a list of 50 top web search keywords about Hello, World! taken from a keyword tool. Let’s look at a few examples:
```python PYTHON
df = pd.read_csv("https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/data/hello-world-kw.csv", names=["search_term"])
df.head()
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          search_term
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          how to print hello world in python
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          what is hello world
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          how do you write hello world in an alert box
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          how to print hello world in java
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          how to write hello world in eclipse
        </td>
      </tr>
    </tbody>
  </table>
</div>

We use the Embed endpoint to get the embeddings for each of these keywords.
```python PYTHON
def embed_text(texts, input_type):
  """
  Turns a piece of text into embeddings
  Arguments:
    text(str): the text to be turned into embeddings
  Returns:
    embedding(list): the embeddings
  """
  # Embed text by calling the Embed endpoint

  response = co.embed(
                model="embed-v4.0",
                input_type=input_type,
                texts=texts)

  return response.embeddings
```
```python PYTHON
df["search_term_embeds"] = embed_text(texts=df["search_term"].tolist(),
                                      input_type="search_document")
doc_embeds = np.array(df["search_term_embeds"].tolist())
```

### Semantic Search

We’ll look at a couple of example applications. The first example is semantic search. Given a new query, our "search engine" must return the most similar FAQs, where the FAQs are the 50 search terms we uploaded earlier.
```python PYTHON
query = "what is the history of hello world"

query_embeds = embed_text(texts=[query],
                          input_type="search_query")[0]
```
We use cosine similarity to compare the similarity of the new query with each of the FAQs
```python PYTHON

from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(target, candidates):
  """
  Computes the similarity between a target text and a list of other texts
  Arguments:
    target(list[float]): the target text
    candidates(list[list[float]]): a list of other texts, or candidates
  Returns:
    sim(list[tuple]): candidate IDs and the similarity scores
  """
  # Turn list into array

  candidates = np.array(candidates)
  target = np.expand_dims(np.array(target),axis=0)

  # Calculate cosine similarity

  sim = cosine_similarity(target,candidates)
  sim = np.squeeze(sim).tolist()

  # Sort by descending order in similarity

  sim = list(enumerate(sim))
  sim = sorted(sim, key=lambda x:x[1], reverse=True)

  # Return similarity scores

  return sim
```
Finally, we display the top 5 FAQs that match the new query
```python PYTHON
similarity = get_similarity(query_embeds,doc_embeds)

print("New query:")
print(new_query,'\n')

print("Similar queries:")
for idx,score in similarity[:5]:
  print(f"Similarity: {score:.2f};", df.iloc[idx]["search_term"])
```
```
New query:
what is the history of hello world

Similar queries:
Similarity: 0.58; how did hello world originate
Similarity: 0.56; where did hello world come from
Similarity: 0.54; why hello world
Similarity: 0.53; why is hello world so famous
Similarity: 0.53; what is hello world
```

### Semantic Exploration

In the second example, we take the same idea as semantic search and take a broader look, which is exploring huge volumes of text and analyzing their semantic relationships.

We'll use the same 50 top web search terms about Hello, World! There are different techniques we can use to compress the embeddings down to just 2 dimensions while retaining as much information as possible. We'll use a technique called UMAP. And once we can get it down to 2 dimensions, we can plot these embeddings on a 2D chart.
```python PYTHON
import umap
reducer = umap.UMAP(n_neighbors=49)
umap_embeds = reducer.fit_transform(doc_embeds)

df['x'] = umap_embeds[:,0]
df['y'] = umap_embeds[:,1]
```
```python PYTHON
chart = alt.Chart(df).mark_circle(size=500).encode(
  x=
  alt.X('x',
      scale=alt.Scale(zero=False),
      axis=alt.Axis(labels=False, ticks=False, domain=False)
  ),

  y=
  alt.Y('y',
      scale=alt.Scale(zero=False),
      axis=alt.Axis(labels=False, ticks=False, domain=False)
  ),

  tooltip=['search_term']
  )

text = chart.mark_text(align='left', dx=15, size=12, color='black'
          ).encode(text='search_term', color= alt.value('black'))

result = (chart + text).configure(background="#FDF7F0"
      ).properties(
      width=1000,
      height=700,
      title="2D Embeddings"
      )

result
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
