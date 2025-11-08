---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Feel free to fill in some other EDGAR path

url = "https://www.sec.gov/Archives/edgar/data/1559720/000155972024000006/abnb-20231231.htm"
loader = UnstructuredURLLoader(urls=[url], headers={"User-Agent": "cohere cohere@cohere.com"})
documents = loader.load()

edgar_10k = documents[0].page_content

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
