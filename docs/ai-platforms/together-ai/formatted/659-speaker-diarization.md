---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Speaker Diarization

Enable diarization to identify who is speaking when:
```python
  from together import Together

  client = Together()

  response = client.audio.transcriptions.create(
      file="meeting.mp3",
      model="openai/whisper-large-v3",
      response_format="verbose_json",
      diarize="true",  # Enable speaker diarization

  )

  # Access speaker segments

  print(response.speaker_segments)
```
```typescript
  import Together from 'together-ai';

  const together = new Together();

  async function transcribeWithDiarization() {
    const response = await together.audio.transcriptions.create({
      file: 'meeting.mp3',
      model: 'openai/whisper-large-v3',
      diarize: true  // Enable speaker diarization
    });

    // Access the speaker segments
    console.log(`Speaker Segments: ${response.speaker_segments}\n`);
  }

  transcribeWithDiarization();
```
```bash
  curl -X POST "https://api.together.xyz/v1/audio/transcriptions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -F "file=@meeting.mp3" \
       -F "model=openai/whisper-large-v3" \
       -F "diarize=true"
```

**Example Response with Diarization:**
```json
AudioSpeakerSegment(
    id=1,
    speaker_id='SPEAKER_01',
    start=6.268,
    end=30.776,
    text=(
        "Hello. Oh, hey, Justin. How are you doing? ..."
    ),
    words=[
        AudioTranscriptionWord(
            word='Hello.',
            start=6.268,
            end=11.314,
            id=0,
            speaker_id='SPEAKER_01'
        ),
        AudioTranscriptionWord(
            word='Oh,',
            start=11.834,
            end=11.894,
            id=1,
            speaker_id='SPEAKER_01'
        ),
        AudioTranscriptionWord(
            word='hey,',
            start=11.914,
            end=11.995,
            id=2,
            speaker_id='SPEAKER_01'
        ),
        ...
    ]
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
