---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. Get The Archive of Questions

We'll use the [trec](https://www.tensorflow.org/datasets/catalog/trec) dataset which is made up of questions and their categories.
```python PYTHON
dataset = load_dataset("trec", split="train")

df = pd.DataFrame(dataset)[:1000]

df.head(10)
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          label-coarse
        </th>

        <th>
          label-fine
        </th>

        <th>
          text
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          0
        </td>

        <td>
          0
        </td>

        <td>
          How did serfdom develop in and then leave Russia ?
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          1
        </td>

        <td>
          1
        </td>

        <td>
          What films featured the character Popeye Doyle ?
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          0
        </td>

        <td>
          0
        </td>

        <td>
          How can I find a list of celebrities ' real names ?
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          1
        </td>

        <td>
          2
        </td>

        <td>
          What fowl grabs the spotlight after the Chinese Year of the Monkey ?
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          2
        </td>

        <td>
          3
        </td>

        <td>
          What is the full form of .com ?
        </td>
      </tr>

      <tr>
        <th>
          5
        </th>

        <td>
          3
        </td>

        <td>
          4
        </td>

        <td>
          What contemptible scoundrel stole the cork from my lunch ?
        </td>
      </tr>

      <tr>
        <th>
          6
        </th>

        <td>
          3
        </td>

        <td>
          5
        </td>

        <td>
          What team did baseball 's St. Louis Browns become ?
        </td>
      </tr>

      <tr>
        <th>
          7
        </th>

        <td>
          3
        </td>

        <td>
          6
        </td>

        <td>
          What is the oldest profession ?
        </td>
      </tr>

      <tr>
        <th>
          8
        </th>

        <td>
          0
        </td>

        <td>
          7
        </td>

        <td>
          What are liver enzymes ?
        </td>
      </tr>

      <tr>
        <th>
          9
        </th>

        <td>
          3
        </td>

        <td>
          4
        </td>

        <td>
          Name the scar-faced bounty hunter of The Old West .
        </td>
      </tr>
    </tbody>
  </table>
</div>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
