---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Quick Start

Here's how to get started with basic text-to-speech:
```python
  from together import Together

  client = Together()

  speech_file_path = "speech.mp3"

  response = client.audio.speech.create(
      model="canopylabs/orpheus-3b-0.1-ft",
      input="Today is a wonderful day to build something people love!",
      voice="tara",
  )

  response.stream_to_file(speech_file_path)
```
```typescript
  import Together from 'together-ai';

  const together = new Together();

  async function generateAudio() {
    const res = await together.audio.create({
      input: 'Hello, how are you today?',
      voice: 'tara',
      response_format: 'mp3',
      sample_rate: 44100,
      stream: false,
      model: 'canopylabs/orpheus-3b-0.1-ft',
    });

    if (res.body) {
      console.log(res.body);
      const nodeStream = Readable.from(res.body as ReadableStream);
      const fileStream = createWriteStream('./speech.mp3');

      nodeStream.pipe(fileStream);
    }
  }

  generateAudio();
```
```bash
  curl -X POST "https://api.together.xyz/v1/audio/speech" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "canopylabs/orpheus-3b-0.1-ft",
         "input": "The quick brown fox jumps over the lazy dog",
         "voice": "tara"
       }' \
       --output speech.wav
```

This will output a `speech.mp3` file.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
