---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Audio Transcription

Audio transcription converts speech to text in the same language as the source audio.
```python
  from together import Together

  client = Together()

  response = client.audio.transcriptions.create(
      file="meeting_recording.mp3",
      model="openai/whisper-large-v3",
      language="en",
      response_format="json",
  )

  print(f"Transcription: {response.text}")
```
```typescript
  import Together from 'together-ai';

  const together = new Together();

  const response = await together.audio.transcriptions.create({
    file: 'meeting_recording.mp3',
    model: 'openai/whisper-large-v3',
    language: 'en',
    response_format: 'json',
  });

  console.log(`Transcription: ${response.text}`);
```
```shell
  together audio transcribe meeting_recording.mp3 \
    --model openai/whisper-large-v3 \
    --language en \
    --response-format json
```

The API supports the following audio formats:

* `.wav` (audio/wav)
* `.mp3` (audio/mpeg)
* `.m4a` (audio/mp4)
* `.webm` (audio/webm)
* `.flac` (audio/flac)

**Input Methods**

**Local File Path**
```python
response = client.audio.transcriptions.create(
    file="/path/to/audio.mp3",
    model="openai/whisper-large-v3",
)
```
**Path Object**
```python
from pathlib import Path

audio_file = Path("recordings/interview.wav")
response = client.audio.transcriptions.create(
    file=audio_file,
    model="openai/whisper-large-v3",
)
```
**URL**
```python
response = client.audio.transcriptions.create(
    file="https://example.com/audio.mp3", model="openai/whisper-large-v3"
)
```
**File-like Object**
```python
with open("audio.mp3", "rb") as audio_file:
    response = client.audio.transcriptions.create(
        file=audio_file,
        model="openai/whisper-large-v3",
    )
```
**Language Support**

Specify the audio language using ISO 639-1 language codes:
```python
response = client.audio.transcriptions.create(
    file="spanish_audio.mp3",
    model="openai/whisper-large-v3",
    language="es",  # Spanish

)
```
Common specifiable language codes:

* "en" - English
* "es" - Spanish
* "fr" - French
* "de" - German
* "ja" - Japanese
* "zh" - Chinese
* "auto" - Auto-detect (default)

**Custom Prompts**

Use prompts to improve transcription accuracy for specific contexts:
```python
  response = client.audio.transcriptions.create(
      file="medical_consultation.mp3",
      model="openai/whisper-large-v3",
      language="en",
      prompt="This is a medical consultation discussing patient symptoms, diagnosis, and treatment options.",
  )
```
```shell
  together audio transcribe medical_consultation.mp3 \
    --model openai/whisper-large-v3 \
    --language en \
    --prompt "This is a medical consultation discussing patient symptoms, diagnosis, and treatment options."
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
