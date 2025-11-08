---
title: "Crewai: Extract text from PDF"
description: "Extract text from PDF section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Extract text from PDF

def extract_text_from_pdf(pdf_path):
    text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text.strip())
    return text

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize OpenAI client](./830-initialize-openai-client.md)

**Next:** [Generate OpenAI embeddings →](./832-generate-openai-embeddings.md)
