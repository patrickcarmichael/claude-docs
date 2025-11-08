---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Questions in French

```python PYTHON
questions_fr = [
           "À quoi se compare The Whole Earth Catalog ?",
           "Dans quoi Reed College était-il excellent ?",
           "De quoi l'auteur a-t-il été diagnostiqué ?",
           "Quelle est la leçon clé de cet article ?",
           "Que disait l'article sur Michael Jackson ?",
           ]
```
```python PYTHON
```
```python PYTHON

chain_type_kwargs = {"prompt": PROMPT}

qa = RetrievalQA.from_chain_type(llm=Cohere(model="command", temperature=0),
                                 chain_type="stuff",
                                 retriever=db.as_retriever(),
                                 chain_type_kwargs=chain_type_kwargs,
                                 return_source_documents=True)

for question in questions_fr:
  answer = qa({"query": question})
  result = answer["result"].replace("\n","").replace("Answer:","")
  sources = answer['source_documents']
  print("-"*20,"\n")
  print(f"Question: {question}")
  print(f"Answer: {result}")
```
```txt title="Output"
--------------------

Question: À quoi se compare The Whole Earth Catalog ?
Answer: The Whole Earth Catalog was like Google in paperback form, 35 years before Google came along.
--------------------

Question: Dans quoi Reed College était-il excellent ?
Answer: Reed College offered the best calligraphy instruction in the country.
--------------------

Question: De quoi l'auteur a-t-il été diagnostiqué ?
Answer: The author was diagnosed with a very rare form of pancreatic cancer that is curable with surgery.
--------------------

Question: Quelle est la leçon clé de cet article ?
Answer: The key lesson of this article is that remembering that you will die soon is the most important tool to help one make the big choices in life.
--------------------

Question: Que disait l'article sur Michael Jackson ?
Answer: The text does not contain the answer to the question.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
