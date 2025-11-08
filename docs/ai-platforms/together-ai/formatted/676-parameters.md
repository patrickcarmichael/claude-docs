---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Parameters

| Parameter        | Type   | Required | Description                                                    |
| :--------------- | :----- | :------- | :------------------------------------------------------------- |
| model            | string | Yes      | The TTS model to use                                           |
| input            | string | Yes      | The text to generate audio for                                 |
| voice            | string | Yes      | The voice to use for generation. See [Voices](#voices) section |
| response\_format | string | No       | Output format: `mp3`, `wav`, or `raw` (PCM). Default: `wav`    |

For the full set of parameters refer to the API reference for [/audio/speech](/reference/audio-speech).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
