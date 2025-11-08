---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting Set Up

Before we dive into the technical weeds, we need to set up the notebook's runtime and filesystem environments. The code cells below do the following:

* Install required libraries
* Confirm that data dependencies from the GitHub repo have been downloaded. These will be under `data/document-parsing` and contain the following:
  * the PDF document that we will be working with, `fda-approved-drug.pdf` (this can also be found here: [https://www.accessdata.fda.gov/drugsatfda\_docs/label/2023/215500s000lbl.pdf](https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/215500s000lbl.pdf))
  * precomputed parsed documents for each parsing solution. While the point of this notebook is to illustrate how this is done, we provide the parsed final results to allow readers to skip ahead to the RAG section without having to set up the required infrastructure for each solution.)
* Add utility functions needed for later sections
```python PYTHON
%%capture
! sudo apt install tesseract-ocr poppler-utils
! pip install "cohere<5" fsspec hnswlib google-cloud-documentai google-cloud-storage boto3 langchain-text-splitters llama_parse pytesseract pdf2image pandas
```
```python PYTHON
data_dir = "data/document-parsing"
source_filename = "fda-approved-drug"
extension = "pdf"
```
```python PYTHON
from pathlib import Path

sources = ["gcp", "aws", "unstructured-io", "llamaparse-text", "llamaparse-markdown", "pytesseract"]

filenames = ["{}-parsed-fda-approved-drug.txt".format(source) for source in sources]
filenames.append("fda-approved-drug.pdf")

for filename in filenames:
    file_path = Path(f"{data_dir}/{filename}")
    if file_path.is_file() == False:
        print(f"File {filename} not found at {data_dir}!")
```

### Utility Functions

Make sure to include the notebook's utility functions in the runtime.
```python PYTHON
def store_document(path: str, doc_content: str):
    with open(path, 'w') as f:
      f.write(doc_content)
```
```python PYTHON
import json

def insert_citations_in_order(text, citations, documents):
    """
    A helper function to pretty print citations.
    """

    citations_reference = {}
    for index, doc in enumerate(documents):
        citations_reference[index] = doc

    offset = 0
    # Process citations in the order they were provided

    for citation in citations:
        # Adjust start/end with offset

        start, end = citation['start'] + offset, citation['end'] + offset
        citation_numbers = []
        for doc_id in citation["document_ids"]:
            for citation_index, doc in citations_reference.items():
                if doc["id"] == doc_id:
                    citation_numbers.append(citation_index)
        references = "(" + ", ".join("[{}]".format(num) for num in citation_numbers) + ")"
        modification = f'{text[start:end]} {references}'
        # Replace the cited text with its bolded version + placeholder

        text = text[:start] + modification + text[end:]
        # Update the offset for subsequent replacements

        offset += len(modification) - (end - start)

    # Add the citations at the bottom of the text

    text_with_citations = f'{text}'
    citations_reference = ["[{}]: {}".format(x["id"], x["text"]) for x in citations_reference.values()]

    return text_with_citations, "\n".join(citations_reference)
```
```python PYTHON
def format_docs_for_chat(documents):
  return [{"id": str(index), "text": x} for index, x in enumerate(documents)]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
