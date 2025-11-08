---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Word-level Timestamps

Get word-level timing information:
```python
  response = client.audio.transcriptions.create(
      file="audio.mp3",
      model="openai/whisper-large-v3",
      response_format="verbose_json",
      timestamp_granularities="word",
  )

  print(f"Text: {response.text}")
  print(f"Language: {response.language}")
  print(f"Duration: {response.duration}s")

  ## Access individual words with timestamps

  if response.words:
      for word in response.words:
          print(f"'{word.word}' [{word.start:.2f}s - {word.end:.2f}s]")
```
```shell
  together audio transcribe audio.mp3 \
    --model openai/whisper-large-v3 \
    --response-format verbose_json \
    --timestamp-granularities word \
    --pretty
```

**Example Output:**
```text
Text: It is certain that Jack Pumpkinhead might have had a much finer house to live in.
Language: en
Duration: 7.2562358276643995s
Task: None

'It' [0.00s - 0.36s]
'is' [0.42s - 0.47s]
'certain' [0.51s - 0.74s]
'that' [0.79s - 0.86s]
'Jack' [0.90s - 1.11s]
'Pumpkinhead' [1.15s - 1.66s]
'might' [1.81s - 2.00s]
'have' [2.04s - 2.13s]
'had' [2.16s - 2.26s]
'a' [2.30s - 2.32s]
'much' [2.36s - 2.48s]
'finer' [2.54s - 2.74s]
'house' [2.78s - 2.93s]
'to' [2.96s - 3.03s]
'live' [3.07s - 3.21s]
'in.' [3.26s - 7.27s]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
