---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Best Practices

### Resizing Large Images

If you’re working with images that are larger than the model can handle, consider resizing them yourself, as this will have positive impacts on latency, cost, and performance.

### Structured Outputs and JSON Mode

Many use cases (such as OCR) work best with Cohere's structured output capabilities. To learn more about this, consult the [structured output guide](https://docs.cohere.com/v2/docs/structured-outputs).

### Getting the best Results out of the Model

Here are some techniques for optimizing model outputs:

* Apply prompt techniques that work well for text-based interactions.
* Reduce network latency by shrinking large images on the client before sending them via the API.
* Enlarge small text in images to improve readability and model performance.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
