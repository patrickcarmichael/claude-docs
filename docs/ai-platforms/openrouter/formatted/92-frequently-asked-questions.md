---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Can I mix different modalities in one request?">
    Yes! You can send text, images, PDFs, audio, and video in the same request. The model will process all inputs together.
  </Accordion>

  <Accordion title="How is multimodal content priced?">
    * **Images**: Typically priced per image or as input tokens
    * **PDFs**: Free text extraction, paid OCR processing, or native model pricing
    * **Audio**: Priced as input tokens based on duration
    * **Video**: Priced as input tokens based on duration and resolution
  </Accordion>

  <Accordion title="Which models support video input?">
    Video support varies by model. Use the [Models page](/models?fmt=cards\&input_modalities=video) to filter for video-capable models. Check each model's documentation for specific video format and duration limits.
  </Accordion>
</AccordionGroup>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
