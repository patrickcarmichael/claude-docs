---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Introduction

In this demo, we will demonstrate how thoughtful reward‑function design can steer a language model toward producing clear, 50‑token summaries that balance brevity with relevance. Using Fireworks’ reinforcement‑fine‑tuning workflow, you’ll see how adjusting a few well‑chosen signals can transform raw model outputs into reliable digests suitable for news briefs, chat recaps, and study notes—revealing, along the way, why defeating reward hacking is central to building trustworthy summarizers.

### Goals

Every summarizer will look different. Let’s set up some goals:

* Use `llama-v3p1-8b-instruct` to balance speed and model intelligence
* Summaries should be under 50 tokens
* Summaries should capture relevant information within a much larger text

### Why Reinforcement Fine-Tune?

Reinforcement Fine‑Tuning augments standard supervised training by adding a reward signal that scores each model output after it is generated. Instead of optimizing only for next‑token likelihood, the model learns from these scores—gradually preferring strategies that maximize the reward and discarding those that do not.

Traditional supervised fine‑tuning simply teaches a model to imitate example summaries, but it never checks whether the *finished* output actually satisfies our broader goals—like striking the right balance between brevity and substance. Reinforcement  Fine‑Tuning adds a feedback step after each summary is generated, letting us reward outputs that hit that balance and discourage ones that don’t. Because we can adjust this feedback on the fly, RFT gives us a practical steering mechanism: tweak the reward, observe how the model adapts, and quickly converge on summaries that are both concise and informative. For this sort of summarization task, that end‑to‑end feedback loop is essential—imitation alone can’t capture the nuanced trade‑offs we care about.

For more information on RFT on the Fireworks platform and when to use it, take a look at our examples on Knowledge Distillation

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
