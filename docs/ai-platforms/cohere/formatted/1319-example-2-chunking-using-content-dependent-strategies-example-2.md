---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example 2: Chunking using content-dependent strategies \[#example-2]

In the previous experiment, we provided an example of how using or not using overlapping can affect a model's performance, particularly in documents such as call transcripts where subjects change frequently. Ensuring that each chunk contains all relevant information is crucial. While we managed to retrieve the correct information by introducing overlapping into the chunking strategy, this might still not be the optimal approach for transcripts with longer speaker speeches.

Therefore, in this experiment, we will adopt a content-dependent strategy.

Our proposed approach entails segmenting the text whenever a new speaker begins speaking, which requires preprocessing the text accordingly.

### Preprocess the text

Firstly, let's observe that in the HTML text, each time the speaker changes, their name is enclosed within `<p><strong>Name</strong></p>` tags, denoting the speaker's name in bold letters.

To facilitate our text chunking process, we'll use the above observation and introduce a unique character sequence `###`, which we'll utilize as a marker for splitting the text.
```python PYTHON
print('HTML text')
print(target_divs[:3])
print('-------------------\n')

text_custom = []
for div in target_divs:
  if div.get_text() is None:
    continue
  if str(div).startswith('<p><strong>'):
    text_custom.append(f'### {div.get_text()}')

  else:
    text_custom.append(div.get_text())

text_custom = '\n'.join(text_custom)
print(text_custom[:500])
```
```txt title="Output"
HTML text
[<p><strong>Martin Viecha</strong></p>, <p>Good afternoon, everyone, and welcome to Tesla's fourth-quarter 2023 Q&amp;A webcast. My name is Martin Viecha, VP of investor relations, and I'm joined today by Elon Musk, Vaibhav Taneja, and a number of other executives. Our Q4 results were announced at about 3 p.m. Central Time in the update that we published at the same link as this webcast.</p>, <p>During this call, we will discuss our business outlook and make forward-looking statements. These comments are based on our predictions and expectations as of today. Actual events or results could differ materially due to a number of risks and uncertainties, including those mentioned in our most recent filings with the SEC. [Operator instructions] But before we jump into Q&amp;A, Elon has some opening remarks.</p>]
-------------------

### Martin Viecha

Good afternoon, everyone, and welcome to Tesla's fourth-quarter 2023 Q&amp;A webcast. My name is Martin Viecha, VP of investor relations, and I'm joined today by Elon Musk, Vaibhav Taneja, and a number of other executives. Our Q4 results were announced at about 3 p.m. Central Time in the update that we published at the same link as this webcast.
During this call, we will discuss our business outlook and make forward-looking statements. These comments are based on our predictions an
```
In this approach, we prioritize splitting the text at the appropriate separator, `###.` To ensure this behavior, we'll use `CharacterTextSplitter` from [LangChain](https://python.langchain.com/docs/get_started/introduction), guaranteeing such behavior. From our analysis of the text and the fact that we aim to preserve entire speaker speeches intact, we anticipate that most of them will exceed a length of 500. Hence, we'll increase the chunk size to 1000.
```python PYTHON
separator = "###"
chunk_size = 1000
chunk_overlap = 0

text_splitter = CharacterTextSplitter(
    separator = separator,
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    length_function=len,
    is_separator_regex=False,
)

documents = text_splitter.create_documents([text_custom])
documents = [Document(text=doc.page_content) for doc in documents]

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
WARNING:langchain_text_splitters.base:Created a chunk of size 5946, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 4092, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 1782, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 1392, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 2046, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 1152, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 1304, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 1295, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 2090, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 1251, which is longer than the specified 1000


Number of docuemnts:  5
Elon Musk mentions Jonathan Nolan. Musk is friends with the creators of Westworld, Jonathan Nolan and Lisa Joy Nolan.
```
Below we validate the answer using citations.
```python PYTHON
print(insert_citations(response.text, response.citations))
```
```txt title="Output"
Elon Musk [0] mentions Jonathan Nolan. [0] Musk is friends [0] with the creators of Westworld [0], Jonathan Nolan [0] and Lisa Joy Nolan. [0]
```
```python PYTHON
source_nodes[0]
```
```python title="Output"
{'text': "Elon Musk -- Chief Executive Officer and Product Architect\nYeah. The creators of Westworld, Jonathan Nolan, Lisa Joy Nolan, are friends -- are all friends of mine, actually. And I invited them to come see the lab and, like, well, come see it, hopefully soon. It's pretty well -- especially the sort of subsystem test stands where you've just got like one leg on a test stand just doing repetitive exercises and one arm on a test stand pretty well.\nYeah.\n### Unknown speaker\nWe're not entering Westworld anytime soon.\n### Elon Musk -- Chief Executive Officer and Product Architect\nRight, right. Yeah. I take -- take safety very very seriously.\n### Martin Viecha\nThank you. The next question from Norman is: How many Cybertruck orders are in the queue? And when do you anticipate to be able to fulfill existing orders?"}

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
