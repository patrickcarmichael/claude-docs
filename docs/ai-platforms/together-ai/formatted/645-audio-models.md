---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Audio models

Use our [Audio](/reference/audio-speech) endpoint for text-to-speech models. For speech-to-text models see [Transcription](/reference/audio-transcriptions) and [Translations](/reference/audio-translations)

| Organization | Modality       | Model Name       | Model String for API           |
| :----------- | :------------- | :--------------- | :----------------------------- |
| Canopy Labs  | Text-to-Speech | Orpheus 3B       | canopylabs/orpheus-3b-0.1-ft   |
| Kokoro       | Text-to-Speech | Kokoro           | hexgrad/Kokoro-82M             |
| Cartesia     | Text-to-Speech | Cartesia Sonic 2 | cartesia/sonic-2               |
| Cartesia     | Text-to-Speech | Cartesia Sonic   | cartesia/sonic                 |
| OpenAI       | Speech-to-Text | Whisper Large v3 | openai/whisper-large-v3        |
| Mistral AI   | Speech-to-Text | Voxtral Mini 3B  | mistralai/Voxtral-Mini-3B-2507 |

**Audio Model Examples**

* [PDF to Podcast Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/PDF_to_Podcast.ipynb) - Generate a NotebookLM style podcast given a PDF
* [Audio Podcast Agent Workflow](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Serial_Chain_Agent_Workflow.ipynb) - Agent workflow to generate audio files given input content

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
