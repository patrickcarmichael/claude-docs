---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming Audio

For real-time applications where Time-To-First-Byte (TTFB) is critical, use streaming mode:
```python
  from together import Together

  client = Together()

  response = client.audio.speech.create(
      model="canopylabs/orpheus-3b-0.1-ft",
      input="The quick brown fox jumps over the lazy dog",
      voice="tara",
      stream=True,
      response_format="raw",  # Required for streaming

      response_encoding="pcm_s16le",  # 16-bit PCM for clean audio

  )

  # Save the streamed audio to a file

  response.stream_to_file("speech_streaming.wav", response_format="wav")
```
```typescript
  import Together from 'together-ai';

  const together = new Together();

  async function streamAudio() {
    const response = await together.audio.speech.create({
      model: 'canopylabs/orpheus-3b-0.1-ft',
      input: 'The quick brown fox jumps over the lazy dog',
      voice: 'tara',
      stream: true,
      response_format: 'raw',  // Required for streaming
      response_encoding: 'pcm_s16le'  // 16-bit PCM for clean audio
    });

    // Process streaming chunks
    const chunks = [];
    for await (const chunk of response) {
      chunks.push(chunk);
    }

    console.log('Streaming complete!');
  }

  streamAudio();
```
```bash
  curl -X POST "https://api.together.xyz/v1/audio/speech" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "canopylabs/orpheus-3b-0.1-ft",
         "input": "The quick brown fox jumps over the lazy dog",
         "voice": "tara",
         "stream": true
       }'
```

**Streaming Response Format:**

When `stream: true`, the API returns a stream of events:

**Delta Event:**
```json
{
  "type": "delta",
  "audio": "base64-encoded-audio-data"
}
```
**Completion Event:**
```json
{
  "type": "done"
}
```
**Note:** When streaming is enabled, only `raw` (PCM) format is supported. For non-streaming, you can use `mp3`, `wav`, or `raw`.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
