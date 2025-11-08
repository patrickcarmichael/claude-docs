---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2- Given a query that we write, retrieve the most similar posts

We're not limited to searching using existing items. If we get a query, we can embed it and find its nearest neighbors from the dataset.
```python PYTHON
query = "How can I improve my knowledge of calculus?"

query_embed = co.embed(texts=[query],
                       model="embed-v4.0",
                       truncate="RIGHT",
                       input_type="search_query").embeddings

similar_item_ids = search_index.get_nns_by_vector(query_embed[0], 10, include_distances=True)

results = pd.DataFrame(data={'texts': df.iloc[similar_item_ids[0]]['title'],
                             'distance': similar_item_ids[1]})
print(f"Query:'{query}'\nNearest neighbors:")
results
```
```
Query:'How can I improve my knowledge of calculus?'
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
          2457
        </th>

        <td>
          How do I improve my command of mathematical language?
        </td>

        <td>
          0.931286
        </td>
      </tr>

      <tr>
        <th>
          1235
        </th>

        <td>
          How to learn new things better?
        </td>

        <td>
          1.024635
        </td>
      </tr>

      <tr>
        <th>
          145
        </th>

        <td>
          How to self-learn math?
        </td>

        <td>
          1.044135
        </td>
      </tr>

      <tr>
        <th>
          1317
        </th>

        <td>
          How can I learn to read mathematical notation?
        </td>

        <td>
          1.050976
        </td>
      </tr>

      <tr>
        <th>
          910
        </th>

        <td>
          How Do You Learn?
        </td>

        <td>
          1.061253
        </td>
      </tr>

      <tr>
        <th>
          2432
        </th>

        <td>
          How did you learn math notation?
        </td>

        <td>
          1.070800
        </td>
      </tr>

      <tr>
        <th>
          1994
        </th>

        <td>
          How do I become smarter?
        </td>

        <td>
          1.083434
        </td>
      </tr>

      <tr>
        <th>
          1529
        </th>

        <td>
          How do you personally learn?
        </td>

        <td>
          1.086088
        </td>
      </tr>

      <tr>
        <th>
          796
        </th>

        <td>
          How do you keep improving?
        </td>

        <td>
          1.087251
        </td>
      </tr>

      <tr>
        <th>
          1286
        </th>

        <td>
          How do I learn drawing?
        </td>

        <td>
          1.088468
        </td>
      </tr>
    </tbody>
  </table>
</div>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
