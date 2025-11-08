---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Best Practices

**Choosing the Right Method**

* **Batch Transcription:** Best for pre-recorded audio files, podcasts, or any non-real-time use case
* **Real-time Streaming:** Best for live conversations, voice assistants, or applications requiring immediate feedback

**Audio Quality Tips**

* Use high-quality audio files for better transcription accuracy
* Minimize background noise
* Ensure clear speech with good volume levels
* Use appropriate sample rates (16kHz or higher recommended)
* For WebSocket streaming, use PCM format: `pcm_s16le_16000`
* Consider file size limits for uploads
* For long audio files, consider splitting into smaller chunks
* Use streaming for real-time applications when available

**Diarization Best Practices**

* Works best with clear audio and distinct speakers
* Speakers are labeled as SPEAKER\_00, SPEAKER\_01, etc.
* Use with `verbose_json` format to get segment-level speaker information

**Next Steps**

* Explore our [API Reference](/reference/audio-transcriptions) for detailed parameter documentation
* Learn about [Text-to-Speech](/docs/text-to-speech) for the reverse operation
* Check out our [Real-time Audio Transcription App guide](/docs/how-to-build-real-time-audio-transcription-app)


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
