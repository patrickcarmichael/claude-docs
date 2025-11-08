---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define the chunking function

def get_chunks(text, chunk_size, chunk_overlap):
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    length_function=len,
    is_separator_regex=False,
  )

  documents = text_splitter.create_documents([text])
  documents = [Document(text=doc.page_content) for doc in documents]

  return documents
```

### Experiment 1 - no overlap

In our first experiment we define the chunk size as 500 and allow **no overlap between consecutive chunks**.

Subsequently, we implement the standard RAG pipeline. We feed the chunks into a retriever, selecting the `top_n` most pertinent to the query chunks, and supply them as context to the generation model. Throughout this pipeline, we leverage [Cohere's endpoints](https://docs.cohere.com/reference/about), specifically, `co.embed`, `co.re.rank`, and finally, `co.chat`.
```python PYTHON
chunk_size = 500
chunk_overlap = 0
documents = get_chunks(text, chunk_size, chunk_overlap)
retriever = build_retriever(documents)

source_nodes = retriever.retrieve(question)
print('Number of docuemnts: ',len(source_nodes))
source_nodes= [{"text": ni.get_content()}for ni in source_nodes]


response = co.chat(
  message=question,
  documents=source_nodes,
  model=co_model
)
response = response
print(response.text)
```
```txt title="Output"
Number of docuemnts:  5
An unknown speaker mentions Jonathan Nolan in a conversation about the creators of Westworld. They mention that Jonathan Nolan and Lisa Joy Nolan are friends of theirs, and that they have invited them to visit the lab.
```
A notable feature of [`co.chat`](https://docs.cohere.com/reference/chat) is its ability to ground the model's answer within the context. This means we can identify which chunks were used to generate the answer. Below, we show the previous output of the model together with the citation reference, where `[num]` represents the index of the chunk.
```python PYTHON
print(insert_citations(response.text, response.citations))
```
```txt title="Output"
An unknown speaker [0] mentions Jonathan Nolan in a conversation about the creators of Westworld. [0] They mention that Jonathan Nolan and Lisa Joy Nolan [0] are friends [0] of theirs, and that they have invited them to visit the lab. [0]
```
Indeed, by printing the cited chunk, we can validate that the text was divided so that the generation model could not provide the correct response. Notably, the speaker's name is not included in the context, which is why the model refes to an `unknown speaker`.
```python PYTHON
print(source_nodes[0])
```
```python title="Output"
{'text': "Yeah. The creators of Westworld, Jonathan Nolan, Lisa Joy Nolan, are friends -- are all friends of mine, actually. And I invited them to come see the lab and, like, well, come see it, hopefully soon. It's pretty well -- especially the sort of subsystem test stands where you've just got like one leg on a test stand just doing repetitive exercises and one arm on a test stand pretty well.\n\nYeah.\n\nUnknown speaker\n\nWe're not entering Westworld anytime soon."}
```

### Experiment 2 - allow overlap

In the previous experiment, we discovered that the chunks were generated in a way that made it impossible to generate the correct answer. The name of the speaker was not included in the relevant chunk.

Therefore, this time to mitigate this issue, we **allow for overlap between consecutive chunks**.
```python PYTHON
chunk_size = 500
chunk_overlap = 100
documents = get_chunks(text,chunk_size, chunk_overlap)
retriever = build_retriever(documents)

source_nodes = retriever.retrieve(question)
print('Number of docuemnts: ',len(source_nodes))
source_nodes= [{"text": ni.get_content()}for ni in source_nodes]


response = co.chat(
  message=question,
  documents=source_nodes,
  model=co_model
)
response = response
print(response.text)
```
```txt title="Output"
Number of docuemnts:  5
Elon Musk mentions Jonathan Nolan. Musk is the CEO and Product Architect of the lab that resembles the set of Westworld, a show created by Jonathan Nolan and Lisa Joy Nolan.
```
Again, we can print the text along with the citations.
```python PYTHON
print(insert_citations(response.text, response.citations))
```
```txt title="Output"
Elon Musk [0] mentions Jonathan Nolan. Musk is the CEO and Product Architect [0] of the lab [0] that resembles the set of Westworld [0], a show created by Jonathan Nolan [0] and Lisa Joy Nolan. [0]
```
And investigate the chunks which were used as context to answer the query.
```python PYTHON
source_nodes[0]
```
```python title="Output"
{'text': "Yeah, not the best reference.\n\nElon Musk -- Chief Executive Officer and Product Architect\n\nYeah. The creators of Westworld, Jonathan Nolan, Lisa Joy Nolan, are friends -- are all friends of mine, actually. And I invited them to come see the lab and, like, well, come see it, hopefully soon. It's pretty well -- especially the sort of subsystem test stands where you've just got like one leg on a test stand just doing repetitive exercises and one arm on a test stand pretty well.\n\nYeah."}
```
As we can see, by allowing overlap we managed to get the correct answer to our question.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
