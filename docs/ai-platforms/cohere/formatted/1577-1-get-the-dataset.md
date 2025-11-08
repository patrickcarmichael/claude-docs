---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1. Get the dataset

```python PYTHON
import cohere
from sklearn.model_selection import train_test_split

import pandas as pd
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('https://github.com/clairett/pytorch-sentiment-classification/raw/master/data/SST2/train.tsv', delimiter='\t', header=None)
```
```python PYTHON
df.head()
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          0
        </th>

        <th>
          1
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          a stirring , funny and finally transporting re imagining of beauty and
          the beast and 1930s horror films
        </td>

        <td>
          1
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          apparently reassembled from the cutting room floor of any given
          daytime soap
        </td>

        <td>
          0
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          they presume their audience wo n't sit still for a sociology lesson ,
          however entertainingly presented , so they trot out the conventional
          science fiction elements of bug eyed monsters and futuristic women in
          skimpy clothes
        </td>

        <td>
          0
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          this is a visually stunning rumination on love , memory , history and
          the war between art and commerce
        </td>

        <td>
          1
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          jonathan parker 's bartleby should have been the be all end all of the
          modern office anomie films
        </td>

        <td>
          1
        </td>
      </tr>
    </tbody>
  </table>
</div>

We'll only use a subset of the training and testing datasets in this example. We'll only use 500 examples since this is a toy example. You'll want to increase the number to get better performance and evaluation.

The `train_test_split` method splits arrays or matrices into random train and test subsets.
```python PYTHON
num_examples = 500
df_sample = df.sample(num_examples)

sentences_train, sentences_test, labels_train, labels_test = train_test_split(
            list(df_sample[0]), list(df_sample[1]), test_size=0.25, random_state=0)


sentences_train = sentences_train[:95]
sentences_test = sentences_test[:95]

labels_train = labels_train[:95]
labels_test = labels_test[:95]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
