---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1- Given an existing post title, retrieve the most similar posts (nearest neighbor search using embeddings)

We can query neighbors of a specific post using `get_nns_by_item`.
```python PYTHON
example_id = 50

similar_item_ids = search_index.get_nns_by_item(example_id,
                                                10, # Number of results to retrieve

                                                include_distances=True)
results = pd.DataFrame(data={'post titles': df.iloc[similar_item_ids[0]]['title'],
                             'distance': similar_item_ids[1]}).drop(example_id)

print(f"Query post:'{df.iloc[example_id]['title']}'\nNearest neighbors:")
results
```
```
Query post:'Pick startups for YC to fund'
Nearest neighbors:
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          post titles
        </th>

        <th>
          distance
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          2991
        </th>

        <td>
          Best Bank for Startups?
        </td>

        <td>
          0.883494
        </td>
      </tr>

      <tr>
        <th>
          2910
        </th>

        <td>
          Who's looking for a cofounder?
        </td>

        <td>
          0.885087
        </td>
      </tr>

      <tr>
        <th>
          31
        </th>

        <td>
          What startup/technology is on your 'to watch' list?
        </td>

        <td>
          0.887212
        </td>
      </tr>

      <tr>
        <th>
          685
        </th>

        <td>
          What startup/technology is on your 'to watch' list?
        </td>

        <td>
          0.887212
        </td>
      </tr>

      <tr>
        <th>
          2123
        </th>

        <td>
          Who is seeking a cofounder?
        </td>

        <td>
          0.889451
        </td>
      </tr>

      <tr>
        <th>
          727
        </th>

        <td>
          Agriculture startups doing interesting work?
        </td>

        <td>
          0.899192
        </td>
      </tr>

      <tr>
        <th>
          2972
        </th>

        <td>
          How should I evaluate a startup as I job hunt?
        </td>

        <td>
          0.901621
        </td>
      </tr>

      <tr>
        <th>
          2589
        </th>

        <td>
          What methods do you use to gain early customers for your startup?
        </td>

        <td>
          0.903065
        </td>
      </tr>

      <tr>
        <th>
          2708
        </th>

        <td>
          Is there VC appetite for defense related startups?
        </td>

        <td>
          0.904016
        </td>
      </tr>
    </tbody>
  </table>
</div>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
