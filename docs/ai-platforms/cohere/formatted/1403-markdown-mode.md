---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Markdown mode

markdown_parser = LlamaParse(
    api_key=llama_index_api_key,
    result_type="markdown"
)

markdown_response = markdown_parser.load_data(input_path)
markdown_parsed_document = " ".join([parsed_entry.text for parsed_entry in markdown_response])

print("Parsed {} to markdown".format(source_filename))
```
```python PYTHON
"""
Post process parsed document and store it locally.
"""

file_path = "{}/{}-markdown-parsed-fda-approved-drug.txt".format(data_dir, "llamaparse")
store_document(file_path, markdown_parsed_document)
```

#### Visualize the parsed document

```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
