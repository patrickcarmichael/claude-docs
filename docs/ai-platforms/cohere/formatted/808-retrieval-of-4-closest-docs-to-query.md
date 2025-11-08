---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Retrieval of 4 closest docs to query

def retrieval(query):
    # Embed query and retrieve results

    query_emb = co.embed(
        model="embed-v4.0",  # Pass a dummy string

        texts=[query],
        input_type="search_query",
        embedding_types=["float"],
    ).embeddings.float

    doc_ids = index.knn_query(query_emb, k=3)[0][
        0
    ]  # we will retrieve 3 closest neighbors

    # Print and append results

    print(f"QUERY: {query.upper()} \n")
    retrieved_docs, translated_retrieved_docs = [], []

    for doc_id in doc_ids:
        # Append results

        retrieved_docs.append(docs[doc_id])
        translated_retrieved_docs.append(translated_docs[doc_id])

        # Print results

        print(f"ORIGINAL ({docs_lang[doc_id]}): {docs[doc_id]}")
        if docs_lang[doc_id] != "English":
            print(f"TRANSLATION: {translated_docs[doc_id]} \n----")
        else:
            print("----")
    print("END OF RESULTS \n\n")
    return retrieved_docs, translated_retrieved_docs
```
Let’s now try to query the index with a couple of examples, one each in English and Danish.
```python PYTHON
queries = [
    "Can data science help meet sustainability goals?",  # English example

    "Hvor kan jeg finde den seneste danske boligplan?",  # Danish example - "Where can I find the latest Danish property plan?"

]

for query in queries:
    retrieval(query)
```
```mdx
QUERY: CAN DATA SCIENCE HELP MEET SUSTAINABILITY GOALS? 

ORIGINAL (English): Using AI to better manage the environment could reduce greenhouse gas emissions, boost global GDP by up to 38m jobs by 2030
----
ORIGINAL (English): Quality of business reporting on the Sustainable Development Goals improves, but has a long way to go to meet and drive targets.
----
ORIGINAL (English): Only 10 years to achieve Sustainable Development Goals but businesses remain on starting blocks for integration and progress
----
END OF RESULTS 


QUERY: HVOR KAN JEG FINDE DEN SENESTE DANSKE BOLIGPLAN? 

ORIGINAL (Danish): Nyt fra CFOdirect: Ny PP&E-guide, FAQs om den nye leasingstandard, podcast om udfordringerne ved implementering af leasingstandarden og meget mere
TRANSLATION: New from CFOdirect: New PP&E guide, FAQs on the new leasing standard, podcast on the challenges of implementing the leasing standard and much more 
----
ORIGINAL (Danish): Lovforslag fremlagt om rentefri lån, udskudt frist for lønsumsafgift, førtidig udbetaling af skattekredit og loft på indestående på skattekontoen
TRANSLATION: Bills presented on interest -free loans, deferred deadline for payroll tax, early payment of tax credit and ceiling on the balance in the tax account 
----
ORIGINAL (Danish): Nyt fra CFOdirect: Shareholder-spørgsmål til ledelsen, SEC cybersikkerhedsguide, den amerikanske skattereform og meget mere
TRANSLATION: New from CFOdirect: Shareholder questions for management, the SEC cybersecurity guide, US tax reform and more 
----
END OF RESULTS 
```
With the first example, notice how the retrieval system was able to surface documents similar in meaning, for example, surfacing documents related to AI when given a query about data science. This is something that keyword-based search will not be able to capture.

As for the second example, this demonstrates the multilingual nature of the model. You can use the same model across different languages. The model can also perform cross-lingual search, such as the example of from the first retrieved document, where “PP\&E guide” is an English term that stands for “property, plant, and equipment,”.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
