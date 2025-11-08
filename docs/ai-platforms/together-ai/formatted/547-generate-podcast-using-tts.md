---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate Podcast Using TTS

Below we read through the script and parse choose the TTS voice depending on the speaker. We define a speaker and guest voice id.
```py
import subprocess
import ffmpeg
from cartesia import Cartesia

client_cartesia = Cartesia(api_key="CARTESIA_API_KEY")

host_id = "694f9389-aac1-45b6-b726-9d9369183238"  # Jane - host voice

guest_id = "a0e99841-438c-4a64-b679-ae501e7d6091"  # Guest voice

model_id = "sonic-english"  # The Sonic Cartesia model for English TTS

output_format = {
    "container": "raw",
    "encoding": "pcm_f32le",
    "sample_rate": 44100,
}

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
