---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Load the PDF from memory

pdf_file = BytesIO(response.content)

document_text = get_llm_text(pdf_file) 
print(document_text[:50000]) 
```
In this example, we first download a pdf of a sample sublease agreement used in the [summarization cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/summarization/data/Sample%20Sublease%20Agreement.pdf). This agreement was sourced from a publicly available sublease agreement from the [sec.gov website](https://www.sec.gov/Archives/edgar/data/1045425/000119312507044370/dex1032.htm).

We use the pypdf library to extract the contents of the pdf and convert it to text. The text data is then cleaned by removing extra whitespace and page numbers.

### Build a strong prompt

Claude can adapt to various summarization styles. You can change the details of the prompt to guide Claude to be more or less verbose, include more or less technical terminology, or provide a higher or lower level summary of the context at hand.

Here’s an example of how to create a prompt that ensures the generated summaries follow a consistent structure when analyzing sublease agreements:
```python
import anthropic

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
