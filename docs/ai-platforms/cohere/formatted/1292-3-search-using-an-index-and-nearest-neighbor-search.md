---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3. Search using an index and nearest neighbor search

<img alt="Building the search index from the embeddings" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/semantic-search-index.png" />

Let's now use [Annoy](https://github.com/spotify/annoy) to build an index that stores the embeddings in a way that is optimized for fast search. This approach scales well to a large number of texts (other options include [Faiss](https://github.com/facebookresearch/faiss), [ScaNN](https://github.com/google-research/google-research/tree/master/scann), and [PyNNDescent](https://github.com/lmcinnes/pynndescent)).

After building the index, we can use it to retrieve the nearest neighbors either of existing questions (section 3.1), or of new questions that we embed (section 3.2).
```python PYTHON
search_index = AnnoyIndex(embeds.shape[1], 'angular')
for i in range(len(embeds)):
    search_index.add_item(i, embeds[i])

search_index.build(10) # 10 trees

search_index.save('test.ann')
```
```
True
```

### 3.1. Find the neighbors of an example from the dataset

If we're only interested in measuring the distance between the questions in the dataset (no outside queries), a simple way is to calculate the distance between every pair of embeddings we have.
```python PYTHON
example_id = 92

similar_item_ids = search_index.get_nns_by_item(example_id,10,
                                                include_distances=True)
results = pd.DataFrame(data={'texts': df.iloc[similar_item_ids[0]]['text'],
                             'distance': similar_item_ids[1]}).drop(example_id)

print(f"Question:'{df.iloc[example_id]['text']}'\nNearest neighbors:")
results
```
```
Question:'What are bear and bull markets ?'
Nearest neighbors:
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          texts
        </th>

        <th>
          distance
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          614
        </th>

        <td>
          What animals do you find in the stock market ?
        </td>

        <td>
          0.904278
        </td>
      </tr>

      <tr>
        <th>
          137
        </th>

        <td>
          What are equity securities ?
        </td>

        <td>
          0.992819
        </td>
      </tr>

      <tr>
        <th>
          513
        </th>

        <td>
          What do economists do ?
        </td>

        <td>
          1.066583
        </td>
      </tr>

      <tr>
        <th>
          307
        </th>

        <td>
          What does NASDAQ stand for ?
        </td>

        <td>
          1.080738
        </td>
      </tr>

      <tr>
        <th>
          363
        </th>

        <td>
          What does it mean `` Rupee Depreciates '' ?
        </td>

        <td>
          1.086724
        </td>
      </tr>

      <tr>
        <th>
          932
        </th>

        <td>
          Why did the world enter a global depression in 1929 ?
        </td>

        <td>
          1.099370
        </td>
      </tr>

      <tr>
        <th>
          547
        </th>

        <td>
          Where can stocks be traded on-line ?
        </td>

        <td>
          1.105368
        </td>
      </tr>

      <tr>
        <th>
          922
        </th>

        <td>
          What is the difference between a median and a mean ?
        </td>

        <td>
          1.141870
        </td>
      </tr>

      <tr>
        <th>
          601
        </th>

        <td>
          What is `` the bear of beers '' ?
        </td>

        <td>
          1.154140
        </td>
      </tr>
    </tbody>
  </table>
</div>

### 3.2. Find the neighbors of a user query

We're not limited to searching using existing items. If we get a query, we can embed it and find its nearest neighbors from the dataset.
```python PYTHON
query = "What is the tallest mountain in the world?"
input_type_query = "search_query"

query_embed = co.embed(texts=[query],
                  model=model_name,
                  input_type=input_type_query).embeddings

similar_item_ids = search_index.get_nns_by_vector(query_embed[0],10,
                                                include_distances=True)
query_results = pd.DataFrame(data={'texts': df.iloc[similar_item_ids[0]]['text'],
                             'distance': similar_item_ids[1]})


print(f"Query:'{query}'\nNearest neighbors:")
print(query_results) # NOTE: Your results might look slightly different to ours.

```
```
Query:'What is the tallest mountain in the world?'
Nearest neighbors:
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          texts
        </th>

        <th>
          distance
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          236
        </th>

        <td>
          What is the name of the tallest mountain in the world ?
        </td>

        <td>
          0.447309
        </td>
      </tr>

      <tr>
        <th>
          670
        </th>

        <td>
          What is the highest mountain in the world ?
        </td>

        <td>
          0.552254
        </td>
      </tr>

      <tr>
        <th>
          412
        </th>

        <td>
          What was the highest mountain on earth before Mount Everest was
          discovered ?
        </td>

        <td>
          0.801252
        </td>
      </tr>

      <tr>
        <th>
          907
        </th>

        <td>
          What mountain range is traversed by the highest railroad in the world
          ?
        </td>

        <td>
          0.929516
        </td>
      </tr>

      <tr>
        <th>
          435
        </th>

        <td>
          What is the highest peak in Africa ?
        </td>

        <td>
          0.930806
        </td>
      </tr>

      <tr>
        <th>
          109
        </th>

        <td>
          Where is the highest point in Japan ?
        </td>

        <td>
          0.977315
        </td>
      </tr>

      <tr>
        <th>
          901
        </th>

        <td>
          What 's the longest river in the world ?
        </td>

        <td>
          1.064209
        </td>
      </tr>

      <tr>
        <th>
          114
        </th>

        <td>
          What is the largest snake in the world ?
        </td>

        <td>
          1.076390
        </td>
      </tr>

      <tr>
        <th>
          962
        </th>

        <td>
          What 's the second-largest island in the world ?
        </td>

        <td>
          1.088034
        </td>
      </tr>

      <tr>
        <th>
          27
        </th>

        <td>
          What is the highest waterfall in the United States ?
        </td>

        <td>
          1.091145
        </td>
      </tr>
    </tbody>
  </table>
</div>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
