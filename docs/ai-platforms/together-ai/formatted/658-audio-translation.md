---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Audio Translation

Audio translation converts speech from any language to English text.
```python
  response = client.audio.translations.create(
      file="french_audio.mp3",
      model="openai/whisper-large-v3",
  )
  print(f"English translation: {response.text}")
```
```typescript
  const response = await together.audio.translations.create({
    file: 'french_audio.mp3',
    model: 'openai/whisper-large-v3',
  });
  console.log(`English translation: ${response.text}`);
```
```shell
  together audio translate french_audio.mp3 \
    --model openai/whisper-large-v3
```

**Translation with Context**
```python
  response = client.audio.translations.create(
      file="business_meeting_spanish.mp3",
      model="openai/whisper-large-v3",
      prompt="This is a business meeting discussing quarterly sales results.",
  )
```
```shell
  together audio translate business_meeting_spanish.mp3 \
    --model openai/whisper-large-v3 \
    --prompt "This is a business meeting discussing quarterly sales results."
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
