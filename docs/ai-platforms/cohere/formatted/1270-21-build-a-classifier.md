---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2.1: Build a classifier

We use Cohere's [Classify endpoint](https://docs.cohere.com/reference/classify) to build a news category classifier, classifying articles into five categories: Business, Politics, Tech, Entertainment, and Sport.

A typical text classification model requires hundreds/thousands of data points to train, but with this endpoint, we can build a classifier with a few as five examples per class.

To build the classifier, we need a set of examples consisting of text (news text) and labels (news category). The BBC News dataset happens to have both (columns 'Text' and 'Category'), so this time we’ll use the categories for building our examples. For this, we will set aside another portion of dataset.
```python PYTHON
EX_START = 100
EX_END = 200
df_examples = df.iloc[EX_START:EX_END]
df_examples = df_examples.copy()

df_examples.drop(['ArticleId'],axis=1,inplace=True)

df_examples.head()
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          Text
        </th>

        <th>
          Category
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          100
        </th>

        <td>
          honda wins china copyright ruling japan s hond...
        </td>

        <td>
          business
        </td>
      </tr>

      <tr>
        <th>
          101
        </th>

        <td>
          ukip could sue veritas defectors the uk indepe...
        </td>

        <td>
          politics
        </td>
      </tr>

      <tr>
        <th>
          102
        </th>

        <td>
          security warning over fbi virus the us feder...
        </td>

        <td>
          tech
        </td>
      </tr>

      <tr>
        <th>
          103
        </th>

        <td>
          europe backs digital tv lifestyle how people r...
        </td>

        <td>
          tech
        </td>
      </tr>

      <tr>
        <th>
          104
        </th>

        <td>
          celebrities get to stay in jungle all four con...
        </td>

        <td>
          entertainment
        </td>
      </tr>
    </tbody>
  </table>
</div>

With the Classify endpoint, there is a limit of 512 tokens per input. This means full articles won't be able to fit in the examples, so we will approximate and limit each article to its first 300 characters.
```python PYTHON
MAX_CHARS = 300

def shorten_text(text):
  return text[:MAX_CHARS]

df_examples['Text'] = df_examples['Text'].apply(shorten_text)
```
The Classify endpoint needs a minimum of 2 examples for each category. We'll have 5 examples each, sampled randomly from the dataset. We have 5 categories, so we will have a total of 25 examples.
```python PYTHON
EX_PER_CAT = 5

categories = df_examples['Category'].unique().tolist()

ex_texts = []
ex_labels = []
for category in categories:
  df_category = df_examples[df_examples['Category'] == category]
  samples = df_category.sample(n=EX_PER_CAT, random_state=42)
  ex_texts += samples['Text'].tolist()
  ex_labels += samples['Category'].tolist()

print(f'Number of examples per category: {EX_PER_CAT}')
print(f'List of categories: {categories}')
print(f'Number of categories: {len(categories)}')
print(f'Total number of examples: {len(ex_texts)}')
```
```
Number of examples per category: 5
List of categories: ['business', 'politics', 'tech', 'entertainment', 'sport']
Number of categories: 5
Total number of examples: 25
```
Once the examples are ready, we can now get the classifications. Here is a function that returns the classification given an input.
```python PYTHON

from cohere import ClassifyExample

examples = []
for txt, lbl in zip(ex_texts,ex_labels):
  examples.append(ClassifyExample(text=txt, label=lbl))

def classify_text(texts, examples):
    classifications = co.classify(
        inputs=texts,
        examples=examples
    )

    return [c.prediction for c in classifications.classifications]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
