---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Pre-recorded Translation

Translate audio from any of our supported languages to English. Supports files up to 1GB in formats like MP3, FLAC, and WAV.

### Quick Start

```python Python (fireworks sdk) theme={null}
  !pip install fireworks-ai requests

  from fireworks.client.audio import AudioInference
  import requests
  import time
  from dotenv import load_dotenv
  import os

  load_dotenv()

  # Prepare client

  audio = requests.get("https://tinyurl.com/3cy7x44v").content
  client = AudioInference(
      model="whisper-v3",
      base_url="https://audio-prod.api.fireworks.ai",
      #
      # Or for the turbo version

      # model="whisper-v3-turbo",

      # base_url="https://audio-turbo.api.fireworks.ai",

      api_key=os.getenv("FIREWORKS_API_KEY")
  )

  # Make request

  start = time.time()
  r = await client.translate_async(audio=audio)
  print(f"Took: {(time.time() - start):.3f}s. Text: '{r.text}'")
```
```python Python (openai sdk) theme={null}
  !pip install openai requests
  from openai import OpenAI
  import requests
  from dotenv import load_dotenv
  import os

  load_dotenv()

  client = OpenAI(
              base_url="https://audio-prod.api.fireworks.ai/v1",
              api_key=os.getenv("FIREWORKS_API_KEY"),
          )
  audio_file= requests.get("https://tinyurl.com/3cy7x44v").content

  translation = client.audio.translations.create(
      model="whisper-v3",
      file=audio_file,
  )

  print(translation.text)
```
```bash

  # Download audio file

  curl -L -o "audio.flac" "https://tinyurl.com/4997djsh"

  # Make request

  curl -X POST "https://audio-prod.api.fireworks.ai/v1/audio/translations" \
  -H "Authorization: <FIREWORKS_API_KEY>" \
  -F "file=@audio.flac"
```

For more detailed information, see the [full translation API documentation](/api-reference/audio-translations)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
