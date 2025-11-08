---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## What is Together MoA?

Mixture of Agents (MoA) is a novel approach that leverages the collective strengths of multiple LLMs to enhance performance, achieving state-of-the-art results. By employing a layered architecture where each layer comprises several LLM agents, **MoA significantly outperforms** GPT-4 Omni’s 57.5% on AlpacaEval 2.0 with a score of 65.1%, using only open-source models!

The way Together MoA works is that given a prompt, like `tell me the best things to do in SF`, it sends it to 4 different OSS LLMs. It then combines results from all 4, sends it to a final LLM, and asks it to combine all 4 responses into an ideal response. That’s it! It’s just the idea of combining the results of 4 different LLMs to produce a better final output. It’s obviously slower than using a single LLM but it can be great for use cases where latency doesn't matter as much like synthetic data generation.

For a quick summary and 3-minute demo on how to implement MoA with code, watch the video below:

<Frame>
  <iframe class="embedly-embed" src="//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FTvGjgdNC0P8%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DTvGjgdNC0P8&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FTvGjgdNC0P8%2Fhqdefault.jpg&key=7788cb384c9f4d5dbbdbeffd9fe4b92f&type=text%2Fhtml&schema=youtube" width="854" height="480" scrolling="no" title="YouTube embed" frameborder="0" allow="autoplay; fullscreen; encrypted-media; picture-in-picture;" allowfullscreen="true" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
