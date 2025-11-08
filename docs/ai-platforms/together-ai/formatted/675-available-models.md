---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Available Models

Together AI supports multiple text-to-speech models:

| Organization | Model Name       | Model String for API         | API Endpoint Support       |
| :----------- | :--------------- | :--------------------------- | :------------------------- |
| Canopy Labs  | Orpheus 3B       | canopylabs/orpheus-3b-0.1-ft | Rest, Streaming, WebSocket |
| Kokoro       | Kokoro           | hexgrad/Kokoro-82M           | Rest, Streaming, WebSocket |
| Cartesia     | Cartesia Sonic 2 | cartesia/sonic-2             | Rest                       |
| Cartesia     | Cartesia Sonic   | cartesia/sonic               | Rest                       |

>   **📝 Note**
>
>   * Orpheus and Kokoro models support real-time WebSocket streaming for lowest latency applications.
  * To use Cartesia models, you need to be at Build Tier 2 or higher.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
