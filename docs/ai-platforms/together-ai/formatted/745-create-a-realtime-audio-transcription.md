---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a realtime audio transcription

Source: https://docs.together.ai/reference/audio-transcriptions-realtime

GET /realtime
Establishes a WebSocket connection for real-time audio transcription. This endpoint uses WebSocket protocol (wss://api.together.ai/v1/realtime) for bidirectional streaming communication.

**Connection Setup:**
- Protocol: WebSocket (wss://)
- Authentication: Pass API key as Bearer token in Authorization header
- Parameters: Sent as query parameters (model, input_audio_format)

**Client Events:**
- `input_audio_buffer.append`: Send audio chunks as base64-encoded data
```json
  {
    "type": "input_audio_buffer.append",
    "audio": "<base64_encoded_audio_chunk>"
  }
```
- `input_audio_buffer.commit`: Signal end of audio stream
```json
  {
    "type": "input_audio_buffer.commit"
  }
```
**Server Events:**
- `session.created`: Initial session confirmation (sent first)
```json
  {
    "type": "session.created",
    "session": {
      "id": "session-id",
      "object": "realtime.session",
      "modalities": ["audio"],
      "model": "openai/whisper-large-v3"
    }
  }
```
- `conversation.item.input_audio_transcription.delta`: Partial transcription results
```json
  {
    "type": "conversation.item.input_audio_transcription.delta",
    "delta": "The quick brown"
  }
```
- `conversation.item.input_audio_transcription.completed`: Final transcription
```json
  {
    "type": "conversation.item.input_audio_transcription.completed",
    "transcript": "The quick brown fox jumps over the lazy dog"
  }
```
- `conversation.item.input_audio_transcription.failed`: Error occurred
```json
  {
    "type": "conversation.item.input_audio_transcription.failed",
    "error": {
      "message": "Error description",
      "type": "invalid_request_error",
      "param": null,
      "code": "invalid_api_key"
    }
  }
```
**Error Codes:**
- `invalid_api_key`: Invalid API key provided (401)
- `missing_api_key`: Authorization header missing (401)
- `model_not_available`: Invalid or unavailable model (400)
- Unsupported audio format errors (400)


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
