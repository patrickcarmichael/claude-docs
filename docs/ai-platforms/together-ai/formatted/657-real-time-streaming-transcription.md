---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Real-time Streaming Transcription

For applications requiring the lowest latency, use the real-time WebSocket API. This provides streaming transcription with incremental results.

>   **⚠️ Warning**
>
> The WebSocket API is currently only available via raw WebSocket connections. SDK support coming soon.

**Establishing a Connection**

Connect to: `wss://api.together.ai/v1/realtime?model={model}&input_audio_format=pcm_s16le_16000`

**Headers:**
```javascript
{
  'Authorization': 'Bearer YOUR_API_KEY',
  'OpenAI-Beta': 'realtime=v1'
}
```
**Query Parameters**

| Parameter            | Type   | Required | Description                                    |
| :------------------- | :----- | :------- | :--------------------------------------------- |
| model                | string | Yes      | Model to use (e.g., `openai/whisper-large-v3`) |
| input\_audio\_format | string | Yes      | Audio format: `pcm_s16le_16000`                |

**Client → Server Messages**

**1. Append Audio to Buffer**
```json
{
  "type": "input_audio_buffer.append",
  "audio": "base64-encoded-audio-chunk"
}
```
Send audio data in base64-encoded PCM format.

**2. Commit Audio Buffer**
```json
{
  "type": "input_audio_buffer.commit"
}
```
Forces transcription of any remaining audio in the server-side buffer.

**Server → Client Messages**

**Delta Events (Intermediate Results)**
```json
{
  "type": "conversation.item.input_audio_transcription.delta",
  "delta": "The quick brown fox jumps"
}
```
Delta events are intermediate transcriptions. The model is still processing and may revise the output. Each delta message overrides the previous delta.

**Completed Events (Final Results)**
```json
{
  "type": "conversation.item.input_audio_transcription.completed",
  "transcript": "The quick brown fox jumps over the lazy dog"
}
```
Completed events are final transcriptions. The model is confident about this text. The next delta event will continue from where this completed.

**Real-time Example**
```python
  import asyncio
  import websockets
  import json
  import base64
  import os


  async def transcribe_audio():
      api_key = os.environ.get("TOGETHER_API_KEY")
      url = "wss://api.together.ai/v1/realtime?model=openai/whisper-large-v3&input_audio_format=pcm_s16le_16000"

      headers = {"Authorization": f"Bearer {api_key}"}

      async with websockets.connect(url, additional_headers=headers) as ws:
          # Read audio file

          with open("audio.wav", "rb") as f:
              audio_data = f.read()

          # Send audio in chunks with delay to simulate real-time

          chunk_size = 8192
          bytes_per_second = 16000 * 2  # 16kHz * 2 bytes (16-bit)

          delay_per_chunk = chunk_size / bytes_per_second

          for i in range(0, len(audio_data), chunk_size):
              chunk = audio_data[i : i + chunk_size]
              base64_chunk = base64.b64encode(chunk).decode("utf-8")
              await ws.send(
                  json.dumps(
                      {
                          "type": "input_audio_buffer.append",
                          "audio": base64_chunk,
                      }
                  )
              )
              # Simulate real-time streaming

              if i + chunk_size < len(audio_data):
                  await asyncio.sleep(delay_per_chunk)

          # Commit the audio buffer

          await ws.send(json.dumps({"type": "input_audio_buffer.commit"}))

          # Receive transcription results

          async for message in ws:
              data = json.loads(message)
              if (
                  data["type"]
                  == "conversation.item.input_audio_transcription.delta"
              ):
                  print(f"Partial: {data['delta']}")
              elif (
                  data["type"]
                  == "conversation.item.input_audio_transcription.completed"
              ):
                  print(f"Final: {data['transcript']}")
                  break
              elif (
                  data["type"]
                  == "conversation.item.input_audio_transcription.failed"
              ):
                  error = data.get("error", {})
                  print(f"Error: {error.get('message')}")
                  break


  asyncio.run(transcribe_audio())
```
```typescript
  import WebSocket from 'ws';
  import fs from 'fs';

  const apiKey = process.env.TOGETHER_API_KEY;
  const url = 'wss://api.together.ai/v1/realtime?model=openai/whisper-large-v3&input_audio_format=pcm_s16le_16000';

  const ws = new WebSocket(url, {
    headers: {
      'Authorization': `Bearer ${apiKey}`
    }
  });

  ws.on('open', async () => {
    console.log('WebSocket connection established!');

    // Read audio file
    const audioData = fs.readFileSync('audio.wav');

    // Send audio in chunks with delay to simulate real-time
    const chunkSize = 8192;
    const bytesPerSecond = 16000 * 2;  // 16kHz * 2 bytes (16-bit)
    const delayPerChunk = (chunkSize / bytesPerSecond) * 1000;  // Convert to ms

    for (let i = 0; i < audioData.length; i += chunkSize) {
      const chunk = audioData.slice(i, i + chunkSize);
      const base64Chunk = chunk.toString('base64');
      ws.send(JSON.stringify({
        type: 'input_audio_buffer.append',
        audio: base64Chunk
      }));

      // Simulate real-time streaming
      if (i + chunkSize < audioData.length) {
        await new Promise(resolve => setTimeout(resolve, delayPerChunk));
      }
    }

    // Commit audio buffer
    ws.send(JSON.stringify({
      type: 'input_audio_buffer.commit'
    }));
  });

  ws.on('message', (data) => {
    const message = JSON.parse(data.toString());

    if (message.type === 'conversation.item.input_audio_transcription.delta') {
      console.log(`Partial: ${message.delta}`);
    } else if (message.type === 'conversation.item.input_audio_transcription.completed') {
      console.log(`Final: ${message.transcript}`);
      ws.close();
    } else if (message.type === 'conversation.item.input_audio_transcription.failed') {
      const errorMessage = message.error?.message ?? message.message ?? 'Unknown error';
      console.error(`Error: ${errorMessage}`);
      ws.close();
    }
  });

  ws.on('error', (error) => {
    console.error('WebSocket error:', error);
  });
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
