---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example

We can now test out a query. In this example, the final answer can be found on page 12 of the PDF, which aligns with the response provided by the model:
```python PYTHON
query = "what are the charges for services in 2022"
final_answer, final_answer_docs = process_query(query, retriever)
print(final_answer)
print(final_answer_docs)


chat_history=[{'role':"USER", 'message':query},{'role':"CHATBOT", 'message':f'The final answer is: {final_answer}.' + final_answer_docs}]
```
```txt title="Output"
The charges for services in 2022 were $5,266 million.
The final answer is from the documents below:

    [{'id': 'doc_0', 'snippet': 'Program and General Revenues FY 2023 FY 2022 FY 2021 Category (in millions) Charges for Services (CS) $5,769 $5,266 $5,669 Operating Grants and Contributions (OGC) 27,935 31,757 28,109 Capital Grants and Contributions (CGC) 657 656 675 Real Estate Taxes (RET) 31,502 29,507 31,421 Sales and Use Taxes (SUT) 10,577 10,106 7,614 Personal Income Taxes (PIT) 15,313 15,520 15,795 Income Taxes, Other (ITO) 13,181 9,521 9,499 Other Taxes* (OT) 3,680 3,777 2,755 Investment Income* (II) 694 151 226 Unrestricted Federal and State Aid (UFSA) 234 549 108 Other* (O) Total Program and General Revenues - Primary Government 2,305 $110,250 $107,535 $104,176 708 725', 'title': 'chunk 0'}]
```

### Chat History Management

In the example below, we ask a follow up question that relies on the chat history, but does not require a rerun of the RAG pipeline.

We detect questions that do not require RAG by examining the `search_queries` object returned by calling `co.chat` to generate candidate queries to answer our question. If this object is empty, then the model has determined that a document query is not needed to answer the question.

In the example below, the `else` statement is invoked based on `query2`. We still pass in the chat history, allowing the question to be answered with only the prior context.
```python PYTHON
query2='divide this by two'
augmented_queries=co.chat(message=query2,model='command-a-03-2025',temperature=0.2, search_queries_only=True)
if augmented_queries.search_queries:
    print('RAG is needed')
    final_answer, final_answer_docs = process_query(query, retriever)
    print(final_answer)
else:
    print('RAG is not needed')
    response = co.chat(
      message=query2,
      model='command-a-03-2025',
      chat_history=chat_history,
      temperature=0.3
    )

    print("Final answer:")
    print(response.text)
```
```txt title="Output"
    RAG is not needed
    Final answer:
    The result of dividing the charges for services in 2022 by two is $2,633.
```
***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
