---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Set up a WebSocket connection.

ws = client_cartesia.tts.websocket()
```

We can loop through the lines in the script and generate them by a call to the TTS model with specific voice and lines configurations. The lines all appended to the same buffer and once the script finishes we write this out to a wav file, ready to be played.
```py

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
