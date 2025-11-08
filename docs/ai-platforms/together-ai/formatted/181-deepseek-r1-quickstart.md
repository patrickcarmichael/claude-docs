---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## DeepSeek R1 Quickstart

Source: https://docs.together.ai/docs/deepseek-r1

How to get the most out of reasoning models like DeepSeek-R1.

Reasoning models like DeepSeek-R1 have been trained to think step-by-step before responding with an answer. As a result they excel at complex reasoning tasks such as coding, mathematics, planning, puzzles, and agent workflows.

Given a question in the form of an input prompt DeepSeek-R1 outputs both its chain of thought/reasoning process in the form of thinking tokens between `<think>` tags and the answer.

Because these models use more computation/tokens to perform better reasoning they produce longer outputs and can be slower and more expensive than their non-reasoning counterparts.

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=f6f0a54c08e17e7d3015f4b2840f3cde" data-og-width="2946" width="2946" data-og-height="846" height="846" data-path="images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a2a20a5084ecf855f6f32d15295f7805 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=79fffaa220583da7c6e63b59dfd13843 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=99521c4258f5bc9c2cff61095b1a6f71 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=06feffe542ddcaa3aa39ee699e5f35a4 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=4f3da12e9eb0145ffe794abf093a0d6b 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=e9e70a0268295c5bb127bbe2e852d1d8 2500w" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
