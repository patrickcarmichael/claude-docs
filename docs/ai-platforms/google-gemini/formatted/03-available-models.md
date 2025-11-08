---
title: "Google Gemini Documentation"
description: "Formatted documentation for Google Gemini"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Available Models

### Current Generation (2.5 Series)

#### Gemini 2.5 Pro

- **Model ID**: `gemini-2.5-pro`
- **Description**: State-of-the-art thinking model, capable of reasoning over complex problems in code, math, and STEM
- **Context Window**: 1,048,576 input tokens | 65,536 output tokens
- **Input Types**: Audio, images, video, text, PDF
- **Output**: Text only
- **Knowledge Cutoff**: January 2025
- **Capabilities**: Batch API, caching, code execution, file search, function calling, Maps grounding, search grounding, structured outputs, thinking mode, URL context
- **Best For**: Complex reasoning, problem-solving, STEM applications

#### Gemini 2.5 Flash

- **Model ID**: `gemini-2.5-flash`
- **Description**: Best model in terms of price-performance, offering well-rounded capabilities for large-scale processing and agentic use cases
- **Context Window**: 1,048,576 input tokens | 65,536 output tokens
- **Input Types**: Text, images, video, audio
- **Output**: Text only
- **Knowledge Cutoff**: January 2025
- **Capabilities**: Batch API, caching, code execution, file search, function calling, Maps grounding, search grounding, structured outputs, URL context
- **Best For**: Production deployments, agent systems, balanced use cases

#### Gemini 2.5 Flash-Lite

- **Model ID**: `gemini-2.5-flash-lite`
- **Description**: Fastest flash model optimized for cost-efficiency and high throughput
- **Context Window**: 1,048,576 input tokens | 65,536 output tokens
- **Input Types**: Text, image, video, audio, PDF
- **Output**: Text only
- **Knowledge Cutoff**: January 2025
- **Capabilities**: Batch API, caching, code execution, function calling, Maps grounding, search grounding, structured outputs, URL context
- **Best For**: High-volume applications, cost-sensitive deployments

### Previous Generation

- **Gemini 2.0 Flash**: Available with 1M token context window
- **Gemini 2.0 Flash-Lite**: Available with 1M token context window
(Note: Newer versions recommended for production applications)

### Specialized Models

#### Veo 3.1

- **Type**: Video generation model with native audio support
- **Capabilities**: Video generation with synchronized audio

#### Gemini 2.5 Flash Image

- **Type**: Native image generation model
- **Alternative Name**: "Nano Banana"
- **Capabilities**: Image creation and generation

#### Gemini Embeddings

- **Type**: Embedding/vector generation model
- **Use Case**: RAG (Retrieval Augmented Generation) workflows
- **Status**: Production-ready

---

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
