---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Async Support

All transcription and translation operations support async/await:

**Async Transcription**
```python
import asyncio
from together import AsyncTogether


async def transcribe_audio():
    client = AsyncTogether()

    response = await client.audio.transcriptions.create(
        file="audio.mp3",
        model="openai/whisper-large-v3",
        language="en",
    )

    return response.text


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
