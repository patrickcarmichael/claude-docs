---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate and stream audio.

for line in script.dialogue:
    if line.speaker == "Guest":
        voice_id = guest_id
    else:
        voice_id = host_id

    for output in ws.send(
        model_id=model_id,
        transcript="-"
        + line.text,  # the "-"" is to add a pause between speakers

        voice_id=voice_id,
        stream=True,
        output_format=output_format,
    ):
        buffer = output["audio"]  # buffer contains raw PCM audio bytes

        f.write(buffer)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
