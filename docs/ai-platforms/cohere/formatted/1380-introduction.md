---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Introduction

The bread and butter of natural language processing technology is text. Once we can reduce a set of data into text, we can do all kinds of things with it: question answering, summarization, classification, sentiment analysis, searching and indexing, and more.

In the context of enterprise Retrieval Augmented Generation (RAG), the information is often locked in complex file types such as PDFs. These formats are made for sharing information between humans, but not so much with language models.

In this notebook, we will use a real-world pharmaceutical drug label to test out various performant approaches to parsing PDFs. This will allow us to use [Cohere's Command-R model](https://cohere.com/blog/command-r/) in a RAG setting to answer questions and asks about this label, such as "I need a succinct summary of the compound name, indication, route of administration, and mechanism of action of" a given pharmaceutical.

<img alt="Document Parsing Result" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/document-parsing-2.png" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
