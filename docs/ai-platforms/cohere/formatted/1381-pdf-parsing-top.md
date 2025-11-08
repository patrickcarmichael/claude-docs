---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## PDF Parsing \[#top]

We will go over five proprietary as well as open source options for processing PDFs. The parsing mechanisms demonstrated in the following sections are

* [Google Document AI](#gcp)
* [AWS Textract](#aws)
* [Unstructured.io](#unstructured)
* [LlamaParse](#llama)
* [pdf2image + pytesseract](#pdf2image)

By way of example, we will be parsing a [21-page PDF](https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/215500s000lbl.pdf) containing the label for a recent FDA drug approval, the beginning of which is shown below. Then, we will perform a series of basic RAG tasks with our different parsings and evaluate their performance.

<img alt="Drug Label Snippet" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/document-parsing-1.png" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
