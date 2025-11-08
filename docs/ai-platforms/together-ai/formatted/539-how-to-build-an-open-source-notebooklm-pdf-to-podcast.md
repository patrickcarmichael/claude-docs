---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How To Build An Open Source NotebookLM: PDF To Podcast

Source: https://docs.together.ai/docs/open-notebooklm-pdf-to-podcast

In this guide we will see how to create a podcast like the one below from a PDF input!

Inspired by [NotebookLM's podcast generation](https://notebooklm.google/) feature and a recent open source implementation of [Open Notebook LM](https://github.com/gabrielchua/open-notebooklm). In this guide we will implement a walkthrough of how you can build a PDF to podcast pipeline.

Given any PDF we will generate a conversation between a host and a guest discussing and explaining the contents of the PDF.

In doing so we will learn the following:

1. How we can use JSON mode and structured generation with open models like Llama 3 70b to extract a script for the Podcast given text from the PDF.
2. How we can use TTS models to bring this script to life as a conversation.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
