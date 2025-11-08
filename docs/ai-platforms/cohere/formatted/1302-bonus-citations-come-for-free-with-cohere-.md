---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Bonus: Citations come for free with Cohere! 🎉

At Cohere, model generations come with... precise citations! 🎉\
The model cites which groups of words, in the tool results, were used to generate the final answer.\
These citations make it easy to check where the model’s generated response claims are coming from.\
They help users gain visibility into the model reasoning, and sanity check the final model generation.\
These citations are optional — you can decide to ignore them.
```python PYTHON
print("Citations that support the final answer:")
for cite in response.citations:
  print(cite)
```
```
Citations that support the final answer:
{'start': 7, 'end': 29, 'text': '29th of September 2023', 'document_ids': ['query_daily_sales_report:0:0']}
{'start': 42, 'end': 75, 'text': '10,000 sales with 250 units sold.', 'document_ids': ['query_daily_sales_report:0:0']}
{'start': 112, 'end': 127, 'text': 'three products.', 'document_ids': ['query_product_catalog:1:0']}
{'start': 234, 'end': 244, 'text': 'Smartphone', 'document_ids': ['query_product_catalog:1:0']}
{'start': 247, 'end': 250, 'text': '500', 'document_ids': ['query_product_catalog:1:0']}
{'start': 253, 'end': 255, 'text': '20', 'document_ids': ['query_product_catalog:1:0']}
{'start': 260, 'end': 266, 'text': 'Laptop', 'document_ids': ['query_product_catalog:1:0']}
{'start': 269, 'end': 273, 'text': '1000', 'document_ids': ['query_product_catalog:1:0']}
{'start': 276, 'end': 278, 'text': '15', 'document_ids': ['query_product_catalog:1:0']}
{'start': 283, 'end': 289, 'text': 'Tablet', 'document_ids': ['query_product_catalog:1:0']}
{'start': 292, 'end': 295, 'text': '300', 'document_ids': ['query_product_catalog:1:0']}
{'start': 298, 'end': 300, 'text': '25', 'document_ids': ['query_product_catalog:1:0']}
```
```python PYTHON
def insert_citations_in_order(text, citations):
    """
    A helper function to pretty print citations.
    """
    offset = 0
    document_id_to_number = {}
    citation_number = 0
    modified_citations = []

    # Process citations, assigning numbers based on unique document_ids

    for citation in citations:
        citation_numbers = []
        for document_id in sorted(citation["document_ids"]):
            if document_id not in document_id_to_number:
                citation_number += 1  # Increment for a new document_id

                document_id_to_number[document_id] = citation_number
            citation_numbers.append(document_id_to_number[document_id])

        # Adjust start/end with offset

        start, end = citation['start'] + offset, citation['end'] + offset
        placeholder = ''.join([f'[{number}]' for number in citation_numbers])
        # Bold the cited text and append the placeholder

        modification = f'**{text[start:end]}**{placeholder}'
        # Replace the cited text with its bolded version + placeholder

        text = text[:start] + modification + text[end:]
        # Update the offset for subsequent replacements

        offset += len(modification) - (end - start)

    # Prepare citations for listing at the bottom, ensuring unique document_ids are listed once

    unique_citations = {number: doc_id for doc_id, number in document_id_to_number.items()}
    citation_list = '\n'.join([f'[{doc_id}] source: {tool_results[doc_id - 1]["outputs"]} \n    based on tool call: {dict(tool_results[doc_id - 1]["call"])}' for doc_id, number in sorted(unique_citations.items(), key=lambda item: item[1])])
    text_with_citations = f'{text}\n\n{citation_list}'

    return text_with_citations


print(insert_citations_in_order(response.text, response.citations))
```
```
On the **29th of September 2023**[1], there were **10,000 sales with 250 units sold.**[1]

The Electronics category contains **three products.**[2] There are details below:

| Product Name | Price | Stock Level |
| ------------ | ----- | ----------- |
| **Smartphone**[2] | **500**[2] | **20**[2] |
| **Laptop**[2] | **1000**[2] | **15**[2] |
| **Tablet**[2] | **300**[2] | **25**[2] |

The total stock level for Electronics items is 50.

[1] source: [{'date': '2023-09-29', 'summary': 'Total Sales Amount: 10000, Total Units Sold: 250'}]
    based on tool call: {'name': 'query_daily_sales_report', 'parameters': {'day': '2023-09-29'}, 'generation_id': 'eaf955e3-623d-4796-bf51-23b07c66ed2c'}
[2] source: [{'category': 'Electronics', 'products': [{'product_id': 'E1001', 'name': 'Smartphone', 'price': 500, 'stock_level': 20}, {'product_id': 'E1002', 'name': 'Laptop', 'price': 1000, 'stock_level': 15}, {'product_id': 'E1003', 'name': 'Tablet', 'price': 300, 'stock_level': 25}]}]
    based on tool call: {'name': 'query_product_catalog', 'parameters': {'category': 'Electronics'}, 'generation_id': 'eaf955e3-623d-4796-bf51-23b07c66ed2c'}
```
Now, you've used Cohere for Tool Use. Tool use opens up a wide range of new use cases. Here are a few examples:

* **Function calling**: It's now possible to ask the model to output a JSON object with specific function parameters.\
  For instance, this allows your chatbot to interact with your CRM to change the status of a deal, or to engage with a Python interpreter to conduct data science analyses.

* **Query transformation**: You can transform a user message into a search query for a vector database or any search engine.\
  For instance, this enables your work assistant to automatically retrieve the appropriate data from your company's documentation by creating the right query for your vector database.

* **Advanced searches**: You can transform a user message into one-or-many queries, to do multiple subtasks based on the content of the message.\
  For instance, this allows your chatbot to search across different databases and platforms to retrieve relevant information or to conduct comparative analysis.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
