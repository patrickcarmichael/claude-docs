---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Response Formats

**JSON Format (Default)**

Returns only the transcribed/translated text:
```python
response = client.audio.transcriptions.create(
    file="audio.mp3",
    model="openai/whisper-large-v3",
    response_format="json",
)

print(response.text)  # "Hello, this is a test recording."

```
**Verbose JSON Format**

Returns detailed information including timestamps:
```python
  response = client.audio.transcriptions.create(
      file="audio.mp3",
      model="openai/whisper-large-v3",
      response_format="verbose_json",
      timestamp_granularities="segment",
  )

  ## Access segments with timestamps

  for segment in response.segments:
      print(f"[{segment.start:.2f}s - {segment.end:.2f}s]: {segment.text}")
```
```shell
  together audio transcribe audio.mp3 \
    --model openai/whisper-large-v3 \
    --response-format verbose_json \
    --timestamp-granularities segment \
    --pretty
```

**Example Output:**
```text
[0.11s - 10.85s]: Call is now being recorded. Parker Scarves, how may I help you? Online for my wife, and it turns out they shipped the wrong... Oh, I am so sorry, sir. I got it for her birthday, which is tonight, and now I'm not 100% sure what I need to do. Okay, let me see if I can help. Do you have the item number of the Parker Scarves? I don't think so. Call the New Yorker, I... Excellent. What color do...

[10.88s - 21.73s]: Blue. The one they shipped was light blue. I wanted the darker one. What's the difference? The royal blue is a bit brighter. What zip code are you located in? One nine.

[22.04s - 32.62s]: Karen's Boutique, Termall. Is that close? I'm in my office. Okay, um, what is your name, sir? Charlie. Charlie Johnson. Is that J-O-H-N-S-O-N? And Mr. Johnson, do you have the Parker scarf in light blue with you now? I do. They shipped it to my office. It came in not that long ago. What I will do is make arrangements with Karen's Boutique for...

[32.62s - 41.03s]: you to Parker Scarf at no additional cost. And in addition, I was able to look up your order in our system, and I'm going to send out a special gift to you to make up for the inconvenience. Thank you. You're welcome. And thank you for calling Parker Scarf, and I hope your wife enjoys her birthday gift. Thank you. You're very welcome. Goodbye.

[43.50s - 44.20s]: you
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
