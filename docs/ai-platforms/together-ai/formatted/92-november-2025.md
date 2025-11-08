---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## November, 2025

<Update label="Nov 3" description="/audio/speech, /audio/transcriptions">
  **Enhanced Audio Capabilities: Real-time Text-to-Speech and Speech-to-Text**

  Together AI expands audio capabilities with real-time streaming for both TTS and STT, new models, and speaker diarization.

  * **Real-time Text-to-Speech**: WebSocket API for lowest-latency interactive applications
  * **New TTS Models**: Orpheus 3B (`canopylabs/orpheus-3b-0.1-ft`) and Kokoro 82M (`hexgrad/Kokoro-82M`) supporting REST, streaming, and WebSocket endpoints
  * **Real-time Speech-to-Text**: WebSocket streaming transcription with Whisper for live audio applications
  * **Voxtral Model**: New Mistral AI speech recognition model (`mistralai/Voxtral-Mini-3B-2507`) for audio transcriptions
  * **Speaker Diarization**: Identify and label different speakers in audio transcriptions with a free `diarize` flag
  * TTS WebSocket endpoint: `/v1/audio/speech/websocket`
  * STT WebSocket endpoint: `/v1/realtime`
  * Check out the [Text-to-Speech guide](/docs/text-to-speech) and [Speech-to-Text guide](/docs/speech-to-text)
</Update>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
