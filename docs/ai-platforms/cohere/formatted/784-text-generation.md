---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Text generation

Let's explore basic text generation as our first use case. The model takes a prompt as input and produces a relevant response as output.

Consider a scenario where a customer support agent uses an LLM to help draft responses to customer inquiries. The agent provides technical support FAQs as context along with the customer's question. The prompt is structured to include three components: the instruction, the context (FAQs), and the specific customer inquiry.

After passing this prompt to our `generate_text` function, we receive a response object. The actual generated text can be accessed through the `response.text` attribute.
```python PYTHON
inquiry = "I've noticed some fluctuations in my mobile network's performance recently. The connection seems stable most of the time, but every now and then, I experience brief periods of slow data speeds. It happens a few times a day and is quite inconvenient."

prompt = f"""Use the FAQs below to provide a concise response to this customer inquiry.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
