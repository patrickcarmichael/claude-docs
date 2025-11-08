---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example improvement

Here's how the prompt improver enhances a basic classification prompt:

<Accordion title="Original prompt">
```
  From the following list of Wikipedia article titles, identify which article this sentence came from.
  Respond with just the article title and nothing else.

  Article titles:
  {{titles}}

  Sentence to classify:
  {{sentence}}
```
</Accordion>

<Accordion title="Improved prompt">
```
  You are an intelligent text classification system specialized in matching sentences to Wikipedia article titles. Your task is to identify which Wikipedia article a given sentence most likely belongs to, based on a provided list of article titles.

  First, review the following list of Wikipedia article titles:
  <article_titles>
  {{titles}}
  </article_titles>

  Now, consider this sentence that needs to be classified:
  <sentence_to_classify>
  {{sentence}}
  </sentence_to_classify>

  Your goal is to determine which article title from the provided list best matches the given sentence. Follow these steps:

  1. List the key concepts from the sentence
  2. Compare each key concept with the article titles
  3. Rank the top 3 most relevant titles and explain why they are relevant
  4. Select the most appropriate article title that best encompasses or relates to the sentence's content

  Wrap your analysis in <analysis> tags. Include the following:
  - List of key concepts from the sentence
  - Comparison of each key concept with the article titles
  - Ranking of top 3 most relevant titles with explanations
  - Your final choice and reasoning

  After your analysis, provide your final answer: the single most appropriate Wikipedia article title from the list.

  Output only the chosen article title, without any additional text or explanation.
```
</Accordion>

Notice how the improved prompt:

* Adds clear step-by-step reasoning instructions
* Uses XML tags to organize content
* Provides explicit output formatting requirements
* Guides Claude through the analysis process

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
