---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Document Parsing Solutions

For demonstration purposes, we have collected and saved the parsed documents from each solution in this notebook. Skip to the [next section](#document-questions) to run RAG with Command-A on the pre-fetched versions. You can find all parsed resources in detail at the link [here](https://github.com/gchatz22/temp-cohere-resources/tree/main/data).

### Solution 1: Google Cloud Document AI [\[Back to Solutions\]](#top) \[#gcp]

Document AI helps developers create high-accuracy processors to extract, classify, and split documents.

External documentation: [https://cloud.google.com/document-ai](https://cloud.google.com/document-ai)

#### Parsing the document

The following block can be executed in one of two ways:

* Inside a Google Vertex AI environment
  * No authentication needed
* From this notebook
  * Authentication is needed
  * There are pointers inside the code on which lines to uncomment in order to make this work

**Note: You can skip to the next block if you want to use the pre-existing parsed version.**
```python PYTHON
"""
Extracted from https://cloud.google.com/document-ai/docs/samples/documentai-batch-process-document
"""

import re
from typing import Optional

from google.api_core.client_options import ClientOptions
from google.api_core.exceptions import InternalServerError
from google.api_core.exceptions import RetryError
from google.cloud import documentai  # type: ignore

from google.cloud import storage

project_id = ""
location = ""
processor_id = ""
gcs_output_uri = ""

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
