---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multilingual Search with Cohere and Langchain

> This page contains a basic tutorial on how to do search across different languages with Cohere's LLM platform.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Multilingual_Search_with_Cohere_and_Langchain.ipynb" />

***Read the accompanying [blog post here](https://cohere.com/blog/search-cohere-langchain/).***

This notebook contains two examples for performing multilingual search using Cohere and Langchain. Langchain is a library that assists the development of applications built on top of large language models (LLMs), such as Cohere's models.

In short, Cohere makes it easy for developers to leverage LLMs and Langchain makes it easy to build applications with these models.

We'll go through the following examples:

* **Example 1 - Basic Multilingual Search**

  This is a simple example of multilingual search over a list of documents.

  The steps in summary:

  * Import a list of documents
  * Embed the documents and store them in an index
  * Enter a query
  * Return the document most similar to the query

* **Example 2 - Search-Based Question Answering**

  This example shows a more involved example where search is combined with text generation to answer questions about long-form documents.

  The steps in summary:

  * Add an article and chunk it into smaller passages
  * Embed the passages and store them in an index
  * Enter a question
  * Answer the question based on the most relevant documents
```python PYTHON
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from langchain.vectorstores import Qdrant
from langchain.document_loaders import TextLoader
import textwrap as tr
import random
import dotenv
import os

dotenv.load_dotenv(".env") # Upload an '.env' file containing an environment variable named 'COHERE_API_KEY' using your Cohere API Key

```
```txt title="Output"
True
```

### Import a list of documents

```python PYTHON
import tensorflow_datasets as tfds
dataset = tfds.load('trec', split='train')
texts = [item['text'].decode('utf-8') for item in tfds.as_numpy(dataset)]
print(f"Number of documents: {len(texts)}")
```
```txt title="Output"
Downloading and preparing dataset 350.79 KiB (download: 350.79 KiB, generated: 636.90 KiB, total: 987.69 KiB) to /root/tensorflow_datasets/trec/1.0.0...


Dl Completed...: 0 url [00:00, ? url/s]


Dl Size...: 0 MiB [00:00, ? MiB/s]


Extraction completed...: 0 file [00:00, ? file/s]


Generating splits...:   0%|          | 0/2 [00:00<?, ? splits/s]


Generating train examples...:   0%|          | 0/5452 [00:00<?, ? examples/s]


Shuffling /root/tensorflow_datasets/trec/1.0.0.incompleteWOR5EP/trec-train.tfrecord*...:   0%|          | 0/54…


Generating test examples...:   0%|          | 0/500 [00:00<?, ? examples/s]


Shuffling /root/tensorflow_datasets/trec/1.0.0.incompleteWOR5EP/trec-test.tfrecord*...:   0%|          | 0/500…


Dataset trec downloaded and prepared to /root/tensorflow_datasets/trec/1.0.0. Subsequent calls will reuse this data.
Number of documents: 5452
```
```python PYTHON
random.seed(11)
for item in random.sample(texts, 5):
  print(item)
```
```txt title="Output"
What is the starting salary for beginning lawyers ?
Where did Bill Gates go to college ?
What task does the Bouvier breed of dog perform ?
What are the top boy names in the U.S. ?
What is a female rabbit called ?
```

### Embed the documents and store them in an index

```python PYTHON
embeddings = CohereEmbeddings(model = "multilingual-22-12")

db = Qdrant.from_texts(texts, embeddings, location=":memory:", collection_name="my_documents", distance_func="Dot")
```

### Enter a query

```python PYTHON
queries = ["How to get in touch with Bill Gates",
           "Comment entrer en contact avec Bill Gates",
           "Cara menghubungi Bill Gates"]

queries_lang = ["English", "French", "Indonesian"]
```

### Return the document most similar to the query

```python PYTHON
answers = []
for query in queries:
  docs = db.similarity_search(query)
  answers.append(docs[0].page_content)
```
```python PYTHON
for idx,query in enumerate(queries):
  print(f"Query language: {queries_lang[idx]}")
  print(f"Query: {query}")
  print(f"Most similar existing question: {answers[idx]}")
  print("-"*20,"\n")
```
```txt title="Output"
Query language: English
Query: How to get in touch with Bill Gates
Most similar existing question: What is Bill Gates of Microsoft E-mail address ?
--------------------

Query language: French
Query: Comment entrer en contact avec Bill Gates
Most similar existing question: What is Bill Gates of Microsoft E-mail address ?
--------------------

Query language: Indonesian
Query: Cara menghubungi Bill Gates
Most similar existing question: What is Bill Gates of Microsoft E-mail address ?
--------------------
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
