---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## WebSocket API

For the lowest latency and most interactive applications, use the WebSocket API. This allows you to stream text input and receive audio chunks in real-time.

>   **⚠️ Warning**
>
> The WebSocket API is currently only available via raw WebSocket connections. SDK support coming soon.

**Establishing a Connection**

Connect to: `wss://api.together.xyz/v1/audio/speech/websocket`

**Authentication:**

* Include your API key as a query parameter: `?api_key=YOUR_API_KEY`
* Or use the `Authorization` header when establishing the WebSocket connection

**Client → Server Messages**

**1. Append Text to Buffer**
```json
{
  "type": "input_text_buffer.append",
  "text": "Hello, this is a test sentence."
}
```
Appends text to the input buffer. Text is buffered until sentence completion or maximum length is reached.

**2. Commit Buffer**
```json
{
  "type": "input_text_buffer.commit"
}
```
Forces processing of all buffered text. Use this at the end of your input stream.

**3. Clear Buffer**
```json
{
  "type": "input_text_buffer.clear"
}
```
Clears all buffered text without processing (except text already being processed by the model).

**4. Update Session Parameters**
```json
{
  "type": "tts_session.updated",
  "session": {
    "voice": "new_voice_id"
  }
}
```
Updates TTS session settings like voice in real-time.

**Server → Client Messages**

**Session Created**
```json
{
  "event_id": "uuid-string",
  "type": "session.created",
  "session": {
    "id": "session-uuid",
    "object": "realtime.tts.session",
    "modalities": ["text", "audio"],
    "model": "canopylabs/orpheus-3b-0.1-ft",
    "voice": "tara"
  }
}
```
**Text Received Acknowledgment**
```json
{
  "type": "conversation.item.input_text.received",
  "text": "Hello, this is a test sentence."
}
```
**Audio Delta (Streaming Chunks)**
```json
{
  "type": "conversation.item.audio_output.delta",
  "item_id": "tts_1",
  "delta": "base64-encoded-audio-chunk"
}
```
**Audio Complete**
```json
{
  "type": "conversation.item.audio_output.done",
  "item_id": "tts_1"
}
```
**TTS Error**
```json
{
  "type": "conversation.item.tts.failed",
  "error": {
    "message": "Error description",
    "type": "error_type",
    "code": "error_code"
  }
}
```
**WebSocket Example**
```python
  import asyncio
  import websockets
  import json
  import base64
  import os


  async def generate_speech():
      api_key = os.environ.get("TOGETHER_API_KEY")
      url = "wss://api.together.ai/v1/audio/speech/websocket?model=hexgrad/Kokoro-82M&voice=af_alloy"

      headers = {"Authorization": f"Bearer {api_key}"}

      async with websockets.connect(url, additional_headers=headers) as ws:
          # Wait for session created

          session_msg = await ws.recv()
          session_data = json.loads(session_msg)
          print(f"Session created: {session_data['session']['id']}")

          # Send text for TTS

          text_chunks = [
              "Hello, this is a test.",
              "This is the second sentence.",
              "And this is the final one.",
          ]

          async def send_text():
              for chunk in text_chunks:
                  await ws.send(
                      json.dumps(
                          {"type": "input_text_buffer.append", "text": chunk}
                      )
                  )
                  await asyncio.sleep(0.5)  # Simulate typing

              # Commit to process any remaining text

              await ws.send(json.dumps({"type": "input_text_buffer.commit"}))

          async def receive_audio():
              audio_data = bytearray()
              async for message in ws:
                  data = json.loads(message)

                  if data["type"] == "conversation.item.input_text.received":
                      print(f"Text received: {data['text']}")
                  elif data["type"] == "conversation.item.audio_output.delta":
                      # Decode base64 audio chunk

                      audio_chunk = base64.b64decode(data["delta"])
                      audio_data.extend(audio_chunk)
                      print(f"Received audio chunk for item {data['item_id']}")
                  elif data["type"] == "conversation.item.audio_output.done":
                      print(
                          f"Audio generation complete for item {data['item_id']}"
                      )
                  elif data["type"] == "conversation.item.tts.failed":
                      error = data.get("error", {})
                      print(f"Error: {error.get('message')}")
                      break

              # Save the audio to a file

              with open("output.wav", "wb") as f:
                  f.write(audio_data)
              print("Audio saved to output.wav")

          # Run send and receive concurrently

          await asyncio.gather(send_text(), receive_audio())


  asyncio.run(generate_speech())
```
```typescript
  import WebSocket from 'ws';
  import fs from 'fs';

  const apiKey = process.env.TOGETHER_API_KEY;
  const url = 'wss://api.together.ai/v1/audio/speech/websocket?model=hexgrad/Kokoro-82M&voice=af_alloy';

  const ws = new WebSocket(url, {
    headers: {
      'Authorization': `Bearer ${apiKey}`
    }
  });

  const audioData: Buffer[] = [];

  ws.on('open', () => {
    console.log('WebSocket connection established!');
  });

  ws.on('message', (data) => {
    const message = JSON.parse(data.toString());

    if (message.type === 'session.created') {
      console.log(`Session created: ${message.session.id}`);
      
      // Send text chunks
      const textChunks = [
        "Hello, this is a test.",
        "This is the second sentence.",
        "And this is the final one."
      ];

      textChunks.forEach((text, index) => {
        setTimeout(() => {
          ws.send(JSON.stringify({
            type: 'input_text_buffer.append',
            text: text
          }));
        }, index * 500);
      });

      // Commit after all chunks
      setTimeout(() => {
        ws.send(JSON.stringify({
          type: 'input_text_buffer.commit'
        }));
      }, textChunks.length * 500 + 100);

    } else if (message.type === 'conversation.item.input_text.received') {
      console.log(`Text received: ${message.text}`);
    } else if (message.type === 'conversation.item.audio_output.delta') {
      // Decode base64 audio chunk
      const audioChunk = Buffer.from(message.delta, 'base64');
      audioData.push(audioChunk);
      console.log(`Received audio chunk for item ${message.item_id}`);
    } else if (message.type === 'conversation.item.audio_output.done') {
      console.log(`Audio generation complete for item ${message.item_id}`);
    } else if (message.type === 'conversation.item.tts.failed') {
      const errorMessage = message.error?.message ?? 'Unknown error';
      console.error(`Error: ${errorMessage}`);
      ws.close();
    }
  });

  ws.on('close', () => {
    // Save the audio to a file
    if (audioData.length > 0) {
      const completeAudio = Buffer.concat(audioData);
      fs.writeFileSync('output.wav', completeAudio);
      console.log('Audio saved to output.wav');
    }
  });

  ws.on('error', (error) => {
    console.error('WebSocket error:', error);
  });
```

**WebSocket Parameters**

When establishing a WebSocket connection, you can configure:

| Parameter            | Type    | Description                                                 |
| :------------------- | :------ | :---------------------------------------------------------- |
| model\_id            | string  | The TTS model to use                                        |
| voice                | string  | The voice for generation                                    |
| response\_format     | string  | Audio format: `mp3`, `opus`, `aac`, `flac`, `wav`, or `pcm` |
| speed                | float   | Playback speed (default: 1.0)                               |
| max\_partial\_length | integer | Character buffer length before triggering TTS generation    |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
