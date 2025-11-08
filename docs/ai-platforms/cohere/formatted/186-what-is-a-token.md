---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## What is a Token?

Our language models understand "tokens" rather than characters or bytes. One token can be a part of a word, an entire word, or punctuation. Very common words like "water" will have their own unique tokens. A longer, less frequent word might be encoded into 2-3 tokens, e.g. "waterfall" gets encoded into two tokens, one for "water" and one for "fall". Note that tokenization is sensitive to whitespace and capitalization.

Here are some references to calibrate how many tokens are in a text:

* One word tends to be about 2-3 tokens.
* A paragraph is about 128 tokens.
* This short article you're reading now has about 300 tokens.

The number of tokens per word depends on the complexity of the text. Simple text may approach one token per word on average, while complex texts may use less common words that require 3-4 tokens per word on average.

Our vocabulary of tokens is created using byte pair encoding, which you can read more about [here](https://en.wikipedia.org/wiki/Byte_pair_encoding).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
