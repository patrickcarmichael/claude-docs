---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Text mode

text_parser = LlamaParse(
    api_key=llama_index_api_key,
    result_type="text"
)

text_response = text_parser.load_data(input_path)
text_parsed_document = " ".join([parsed_entry.text for parsed_entry in text_response])

print("Parsed {} to text".format(source_filename))
```
```python PYTHON
"""
Post process parsed document and store it locally.
"""

file_path = "{}/{}-text-parsed-fda-approved-drug.txt".format(data_dir, "llamaparse")
store_document(file_path, text_parsed_document)
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
