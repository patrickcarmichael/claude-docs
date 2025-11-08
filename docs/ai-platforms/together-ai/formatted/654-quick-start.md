---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Quick Start

Here's how to get started with basic transcription and translation:
```python
  from together import Together

  client = Together()

  ## Basic transcription

  response = client.audio.transcriptions.create(
      file="path/to/audio.mp3",
      model="openai/whisper-large-v3",
      language="en",
  )
  print(response.text)

  ## Basic translation

  response = client.audio.translations.create(
      file="path/to/foreign_audio.mp3",
      model="openai/whisper-large-v3",
  )
  print(response.text)
```
```typescript
  import Together from 'together-ai';

  const together = new Together();

  // Basic transcription
  const transcription = await together.audio.transcriptions.create({
    file: 'path/to/audio.mp3',
    model: 'openai/whisper-large-v3',
    language: 'en',
  });
  console.log(transcription.text);

  // Basic translation
  const translation = await together.audio.translations.create({
    file: 'path/to/foreign_audio.mp3',
    model: 'openai/whisper-large-v3',
  });
  console.log(translation.text);
```
```bash
  ## Transcription

  curl -X POST "https://api.together.xyz/v1/audio/transcriptions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -F "file=@audio.mp3" \
       -F "model=openai/whisper-large-v3" \
       -F "language=en"

  ## Translation

  curl -X POST "https://api.together.xyz/v1/audio/translations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -F "file=@foreign_audio.mp3" \
       -F "model=openai/whisper-large-v3"
```
```shell
  ## Transcription

  together audio transcribe audio.mp3 \
    --model openai/whisper-large-v3 \
    --language en

  ## Translation

  together audio translate foreign_audio.mp3 \
    --model openai/whisper-large-v3
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
