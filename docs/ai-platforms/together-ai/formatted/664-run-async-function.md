---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run async function

result = asyncio.run(transcribe_audio())
print(result)
```
**Async Translation**
```python
async def translate_audio():
    client = AsyncTogether()

    response = await client.audio.translations.create(
        file="foreign_audio.mp3",
        model="openai/whisper-large-v3",
    )

    return response.text


result = asyncio.run(translate_audio())
print(result)
```
**Concurrent Processing**

Process multiple audio files concurrently:
```python
import asyncio
from together import AsyncTogether


async def process_multiple_files():
    client = AsyncTogether()

    files = ["audio1.mp3", "audio2.mp3", "audio3.mp3"]

    tasks = [
        client.audio.transcriptions.create(
            file=file,
            model="openai/whisper-large-v3",
        )
        for file in files
    ]

    responses = await asyncio.gather(*tasks)

    for i, response in enumerate(responses):
        print(f"File {files[i]}: {response.text}")


asyncio.run(process_multiple_files())
```javascript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
