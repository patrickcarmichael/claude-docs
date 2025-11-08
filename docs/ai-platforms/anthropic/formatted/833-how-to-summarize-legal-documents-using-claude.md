---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to summarize legal documents using Claude

### Select the right Claude model

Model accuracy is extremely important when summarizing legal documents. Claude Sonnet 4.5 is an excellent choice for use cases such as this where high accuracy is required. If the size and quantity of your documents is large such that costs start to become a concern, you can also try using a smaller model like Claude Haiku 4.5.

To help estimate these costs, below is a comparison of the cost to summarize 1,000 sublease agreements using both Sonnet and Haiku:

* **Content size**
  * Number of agreements: 1,000
  * Characters per agreement: 300,000
  * Total characters: 300M

* **Estimated tokens**
  * Input tokens: 86M (assuming 1 token per 3.5 characters)
  * Output tokens per summary: 350
  * Total output tokens: 350,000

* **Claude Sonnet 4.5 estimated cost**
  * Input token cost: 86 MTok \* \$3.00/MTok = \$258
  * Output token cost: 0.35 MTok \* \$15.00/MTok = \$5.25
  * Total cost: \$258.00 + \$5.25 = \$263.25

* **Claude Haiku 3 estimated cost**
  * Input token cost: 86 MTok \* \$0.25/MTok = \$21.50
  * Output token cost: 0.35 MTok \* \$1.25/MTok = \$0.44
  * Total cost: \$21.50 + \$0.44 = \$21.96

<Tip>Actual costs may differ from these estimates. These estimates are based on the example highlighted in the section on [prompting](#build-a-strong-prompt).</Tip>

### Transform documents into a format that Claude can process

Before you begin summarizing documents, you need to prepare your data. This involves extracting text from PDFs, cleaning the text, and ensuring it's ready to be processed by Claude.

Here is a demonstration of this process on a sample pdf:
```python
from io import BytesIO
import re

import pypdf
import requests

def get_llm_text(pdf_file):
    reader = pypdf.PdfReader(pdf_file)
    text = "\n".join([page.extract_text() for page in reader.pages])

    # Remove extra whitespace

    text = re.sub(r'\s+', ' ', text) 

    # Remove page numbers

    text = re.sub(r'\n\s*\d+\s*\n', '\n', text) 

    return text


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
