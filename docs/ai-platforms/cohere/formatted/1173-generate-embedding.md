---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## generate embedding

embeddings = co.embed(
    texts=db.combined.tolist(), model="embed-v4.0", input_type="search_document"
)
db["embeddings"] = embeddings.embeddings
```
```python PYTHON
db
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          title
        </th>

        <th>
          body
        </th>

        <th>
          combined
        </th>

        <th>
          embeddings
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          Bicycle law
        </td>

        <td>
          \n Traffic Infractions and fees - For a...
        </td>

        <td>
          Title: Bicycle law\nBody: \n Traffic In...
        </td>

        <td>
          \[-0.024673462, -0.034729004, 0.0418396, 0.0121...
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          Bicycle helmet requirement
        </td>

        <td>
          Currently, there is no state law requiring hel...
        </td>

        <td>
          Title: Bicycle helmet requirement\nBody: Curre...
        </td>

        <td>
          \[-0.019180298, -0.037384033, 0.0027389526, -0....
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          Section 21a
        </td>

        <td>
          helmet rules by location: These are city and c...
        </td>

        <td>
          Title: Section 21a\nBody: helmet rules by loca...
        </td>

        <td>
          \[0.031097412, 0.0007619858, -0.023010254, -0.0...
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          Section 3b
        </td>

        <td>
          Traffic infraction - A person operating a bicy...
        </td>

        <td>
          Title: Section 3b\nBody: Traffic infraction - ...
        </td>

        <td>
          \[0.015602112, -0.016143799, 0.032958984, 0.000...
        </td>
      </tr>
    </tbody>
  </table>
</div>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
