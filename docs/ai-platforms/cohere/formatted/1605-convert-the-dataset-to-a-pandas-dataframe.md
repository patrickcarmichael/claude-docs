---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Convert the dataset to a pandas dataframe

dataset_df = pd.DataFrame(dataset_df)
dataset_df.head(5)
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
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          \[{'date': '2024-07-06', 'headline': 'BioTech I...
        </td>

        <td>
          \[{'author': 'Riley Smith, Senior Tech Analyst...
        </td>

        <td>
          BioTech Innovations
        </td>

        <td>
          BTCI
        </td>

        <td>
          \{'52_week_range': {'high': 366.55, 'low': 124...
        </td>

        <td>
          Information Technology
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
          \{'52_week_range': {'high': 231.91, 'low': 159...
        </td>

        <td>
          Information Technology
        </td>
      </tr>
    </tbody>
  </table>
</div>
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
