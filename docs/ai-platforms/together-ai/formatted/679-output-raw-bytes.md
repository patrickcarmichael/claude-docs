---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Output Raw Bytes

If you want to extract out raw audio bytes use the settings below:
```python
  import requests
  import os

  url = "https://api.together.xyz/v1/audio/speech"
  api_key = os.environ.get("TOGETHER_API_KEY")

  headers = {"Authorization": f"Bearer {api_key}"}

  data = {
      "input": "This is a test of raw PCM audio output.",
      "voice": "tara",
      "response_format": "raw",
      "response_encoding": "pcm_f32le",
      "sample_rate": 44100,
      "stream": False,
      "model": "canopylabs/orpheus-3b-0.1-ft",
  }

  response = requests.post(url, headers=headers, json=data)

  with open("output_raw.pcm", "wb") as f:
      f.write(response.content)

  print(f"✅ Raw PCM audio saved to output_raw.pcm")
  print(f"   Size: {len(response.content)} bytes")
```
```typescript
  import Together from 'together-ai';

  const together = new Together();

  async function generateRawBytes() {
    const res = await together.audio.create({
      input: 'Hello, how are you today?',
      voice: 'tara',
      response_format: 'raw',
      response_encoding: 'pcm_f32le',
      sample_rate: 44100,
      stream: false,
      model: 'canopylabs/orpheus-3b-0.1-ft',
    });

    console.log(res.body);
  }

  generateRawBytes();
```
```bash
  curl --location 'https://api.together.xyz/v1/audio/speech' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer $TOGETHER_API_KEY' \
  --output test2.pcm \
  --data '{
      "input": text,
      "voice": "tara",
      "response_format": "raw",
      "response_encoding": "pcm_f32le",
      "sample_rate": 44100,
      "stream": false,
      "model": "canopylabs/orpheus-3b-0.1-ft"
  }'
```

This will output a raw bytes `test2.pcm` file.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
