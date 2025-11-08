---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Best Practices

**Choosing the Right Delivery Method**

* **Basic HTTP API:** Best for batch processing or when you need complete audio files
* **Streaming HTTP API:** Best for real-time applications where TTFB matters
* **WebSocket API:** Best for interactive applications requiring lowest latency (chatbots, live assistants)

**Performance Tips**

* Use streaming when you need the fastest time-to-first-byte
* Use WebSocket API for conversational applications
* Buffer text appropriately - sentence boundaries work best for natural speech
* Use the `max_partial_length` parameter in WebSocket to control buffer behavior
* Consider using `raw` (PCM) format for lowest latency, then encode client-side if needed

**Voice Selection**

* Test different voices to find the best match for your application
* Some voices are better suited for specific content types (narration vs conversation)
* Use the Voices API to discover all available options

**Next Steps**

* Explore our [API Reference](/reference/audio-speech) for detailed parameter documentation
* Learn about [Speech-to-Text](/docs/speech-to-text) for the reverse operation
* Check out our [PDF to Podcast guide](/docs/open-notebooklm-pdf-to-podcast) for a complete example

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
