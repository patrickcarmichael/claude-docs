---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1.1: Get articles

Throughout this article, we'll use the [BBC news article dataset](https://www.kaggle.com/competitions/learn-ai-bbc/data?select=BBC+News+Train.csv) as an example [\[Source\]](http://mlg.ucd.ie/datasets/bbc.html). This dataset consists of articles from a few categories: business, politics, tech, entertainment, and sport.

We'll extract a subset of the data and in Step 1, use the first 100 data points.
```python PYTHON
df = pd.read_csv('https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/notebooks/data/bbc_news_subset.csv', delimiter=',')

INP_START = 0
INP_END = 100
df_inputs = df.iloc[INP_START:INP_END]
df_inputs = df_inputs.copy()

df_inputs.drop(['ArticleId','Category'],axis=1,inplace=True)

df_inputs.head()
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          Text
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          worldcom ex-boss launches defence lawyers defe...
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          german business confidence slides german busin...
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          bbc poll indicates economic gloom citizens in ...
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          lifestyle governs mobile choice faster bett...
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          enron bosses in $168m payout eighteen former e...
        </td>
      </tr>
    </tbody>
  </table>
</div>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
