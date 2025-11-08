---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Advanced Features

**Temperature Control**

Adjust randomness in the output (0.0 = deterministic, 1.0 = creative):
```python
  response = client.audio.transcriptions.create(
      file="audio.mp3",
      model="openai/whisper-large-v3",
      temperature=0.0,  # Most deterministic

  )

  print(f"Text: {response.text}")
```
```shell
  together audio transcribe audio.mp3 \
    --model openai/whisper-large-v3 \
    --temperature 0.0
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
