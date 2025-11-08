---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Apply the embedding function with a progress bar

tqdm.pandas(desc="Generating embeddings")
dataset_df["embedding"] = dataset_df[
    "combined_attributes"
].progress_apply(get_embedding)

print(f"We just computed {len(dataset_df['embedding'])} embeddings.")
```
We just computed 63 embeddings.
```python
dataset_df.head()
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          recent_news
        </th>

        <th>
          reports
        </th>

        <th>
          company
        </th>

        <th>
          ticker
        </th>

        <th>
          key_metrics
        </th>

        <th>
          sector
        </th>

        <th>
          combined_attributes
        </th>

        <th>
          embedding
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          \[{'date': '2024-06-09', 'headline': 'CyberDefe...
        </td>

        <td>
          \[{'author': 'Taylor Smith, Technology Sector L...
        </td>

        <td>
          CyberDefense Dynamics
        </td>

        <td>
          CDDY
        </td>

        <td>
          \{'52_week_range': {'high': 387.3, 'low': 41.63...
        </td>

        <td>
          Information Technology
        </td>

        <td>
          CyberDefense Dynamics Information Technology 2...
        </td>

        <td>
          \[0.01210022, -0.03466797, -0.017562866, -0.025...
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          \[{'date': '2024-07-04', 'headline': 'CloudComp...
        </td>

        <td>
          \[{'author': 'Casey Jones, Chief Market Strateg...
        </td>

        <td>
          CloudCompute Pro
        </td>

        <td>
          CCPR
        </td>

        <td>
          \{'52_week_range': {'high': 524.23, 'low': 171....
        </td>

        <td>
          Information Technology
        </td>

        <td>
          CloudCompute Pro Information Technology 2023 C...
        </td>

        <td>
          \[-0.058563232, -0.06323242, -0.037139893, -0.0...
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          \[{'date': '2024-06-27', 'headline': 'VirtualRe...
        </td>

        <td>
          \[{'author': 'Sam Brown, Head of Equity Researc...
        </td>

        <td>
          VirtualReality Systems
        </td>

        <td>
          VRSY
        </td>

        <td>
          \{'52_week_range': {'high': 530.59, 'low': 56.4...
        </td>

        <td>
          Information Technology
        </td>

        <td>
          VirtualReality Systems Information Technology ...
        </td>

        <td>
          \[0.024154663, -0.022872925, -0.01751709, -0.05...
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          \[{'date': '2024-07-06', 'headline': 'BioTech I...
        </td>

        <td>
          \[{'author': 'Riley Smith, Senior Tech Analyst'...
        </td>

        <td>
          BioTech Innovations
        </td>

        <td>
          BTCI
        </td>

        <td>
          \{'52_week_range': {'high': 366.55, 'low': 124....
        </td>

        <td>
          Information Technology
        </td>

        <td>
          BioTech Innovations Information Technology 202...
        </td>

        <td>
          \[0.020736694, -0.041046143, -0.0029773712, -0....
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          \[{'date': '2024-06-26', 'headline': 'QuantumCo...
        </td>

        <td>
          \[{'author': 'Riley Garcia, Senior Tech Analyst...
        </td>

        <td>
          QuantumComputing Inc
        </td>

        <td>
          QCMP
        </td>

        <td>
          \{'52_week_range': {'high': 231.91, 'low': 159....
        </td>

        <td>
          Information Technology
        </td>

        <td>
          QuantumComputing Inc Information Technology 20...
        </td>

        <td>
          \[-0.009757996, -0.04815674, 0.039611816, 0.023...
        </td>
      </tr>
    </tbody>
  </table>
</div>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
