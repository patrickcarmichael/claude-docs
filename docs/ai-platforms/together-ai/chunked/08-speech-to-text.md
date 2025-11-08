**Navigation:** [← Previous](./07-parallel-workflow.md) | [Index](./index.md) | [Next →](./09-together-cookbooks-example-apps.md)

---

# Speech-to-Text
Source: https://docs.together.ai/docs/speech-to-text

Learn how to transcribe and translate audio into text!

Together AI provides comprehensive audio transcription and translation capabilities powered by state-of-the-art speech recognition models including OpenAI's Whisper and Voxtral. This guide covers everything from batch transcription to real-time streaming for low-latency applications.

## Quick Start

Here's how to get started with basic transcription and translation:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  ## Basic transcription

  response = client.audio.transcriptions.create(
      file="path/to/audio.mp3",
      model="openai/whisper-large-v3",
      language="en",
  )
  print(response.text)

  ## Basic translation

  response = client.audio.translations.create(
      file="path/to/foreign_audio.mp3",
      model="openai/whisper-large-v3",
  )
  print(response.text)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  // Basic transcription
  const transcription = await together.audio.transcriptions.create({
    file: 'path/to/audio.mp3',
    model: 'openai/whisper-large-v3',
    language: 'en',
  });
  console.log(transcription.text);

  // Basic translation
  const translation = await together.audio.translations.create({
    file: 'path/to/foreign_audio.mp3',
    model: 'openai/whisper-large-v3',
  });
  console.log(translation.text);
  ```

  ```curl cURL theme={null}
  ## Transcription
  curl -X POST "https://api.together.xyz/v1/audio/transcriptions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -F "file=@audio.mp3" \
       -F "model=openai/whisper-large-v3" \
       -F "language=en"

  ## Translation
  curl -X POST "https://api.together.xyz/v1/audio/translations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -F "file=@foreign_audio.mp3" \
       -F "model=openai/whisper-large-v3"
  ```

  ```shell Shell theme={null}
  ## Transcription
  together audio transcribe audio.mp3 \
    --model openai/whisper-large-v3 \
    --language en

  ## Translation
  together audio translate foreign_audio.mp3 \
    --model openai/whisper-large-v3
  ```
</CodeGroup>

## Available Models

Together AI supports multiple speech-to-text models:

| Organization | Model Name       | Model String for API           | Capabilities                        |
| :----------- | :--------------- | :----------------------------- | :---------------------------------- |
| OpenAI       | Whisper Large v3 | openai/whisper-large-v3        | Real-time, Translation, Diarization |
| Mistral AI   | Voxtral Mini 3B  | mistralai/Voxtral-Mini-3B-2507 |                                     |

## Audio Transcription

Audio transcription converts speech to text in the same language as the source audio.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.audio.transcriptions.create(
      file="meeting_recording.mp3",
      model="openai/whisper-large-v3",
      language="en",
      response_format="json",
  )

  print(f"Transcription: {response.text}")
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  const response = await together.audio.transcriptions.create({
    file: 'meeting_recording.mp3',
    model: 'openai/whisper-large-v3',
    language: 'en',
    response_format: 'json',
  });

  console.log(`Transcription: ${response.text}`);
  ```

  ```shell Shell theme={null}
  together audio transcribe meeting_recording.mp3 \
    --model openai/whisper-large-v3 \
    --language en \
    --response-format json
  ```
</CodeGroup>

The API supports the following audio formats:

* `.wav` (audio/wav)
* `.mp3` (audio/mpeg)
* `.m4a` (audio/mp4)
* `.webm` (audio/webm)
* `.flac` (audio/flac)

**Input Methods**

**Local File Path**

```python Python theme={null}
response = client.audio.transcriptions.create(
    file="/path/to/audio.mp3",
    model="openai/whisper-large-v3",
)
```

**Path Object**

```python Python theme={null}
from pathlib import Path

audio_file = Path("recordings/interview.wav")
response = client.audio.transcriptions.create(
    file=audio_file,
    model="openai/whisper-large-v3",
)
```

**URL**

```python Python theme={null}
response = client.audio.transcriptions.create(
    file="https://example.com/audio.mp3", model="openai/whisper-large-v3"
)
```

**File-like Object**

```python Python theme={null}
with open("audio.mp3", "rb") as audio_file:
    response = client.audio.transcriptions.create(
        file=audio_file,
        model="openai/whisper-large-v3",
    )
```

**Language Support**

Specify the audio language using ISO 639-1 language codes:

```python Python theme={null}
response = client.audio.transcriptions.create(
    file="spanish_audio.mp3",
    model="openai/whisper-large-v3",
    language="es",  # Spanish
)
```

Common specifiable language codes:

* "en" - English
* "es" - Spanish
* "fr" - French
* "de" - German
* "ja" - Japanese
* "zh" - Chinese
* "auto" - Auto-detect (default)

**Custom Prompts**

Use prompts to improve transcription accuracy for specific contexts:

<CodeGroup>
  ```python Python theme={null}
  response = client.audio.transcriptions.create(
      file="medical_consultation.mp3",
      model="openai/whisper-large-v3",
      language="en",
      prompt="This is a medical consultation discussing patient symptoms, diagnosis, and treatment options.",
  )
  ```

  ```shell Shell theme={null}
  together audio transcribe medical_consultation.mp3 \
    --model openai/whisper-large-v3 \
    --language en \
    --prompt "This is a medical consultation discussing patient symptoms, diagnosis, and treatment options."
  ```
</CodeGroup>

## Real-time Streaming Transcription

For applications requiring the lowest latency, use the real-time WebSocket API. This provides streaming transcription with incremental results.

<Warning>
  The WebSocket API is currently only available via raw WebSocket connections. SDK support coming soon.
</Warning>

**Establishing a Connection**

Connect to: `wss://api.together.ai/v1/realtime?model={model}&input_audio_format=pcm_s16le_16000`

**Headers:**

```javascript  theme={null}
{
  'Authorization': 'Bearer YOUR_API_KEY',
  'OpenAI-Beta': 'realtime=v1'
}
```

**Query Parameters**

| Parameter            | Type   | Required | Description                                    |
| :------------------- | :----- | :------- | :--------------------------------------------- |
| model                | string | Yes      | Model to use (e.g., `openai/whisper-large-v3`) |
| input\_audio\_format | string | Yes      | Audio format: `pcm_s16le_16000`                |

**Client → Server Messages**

**1. Append Audio to Buffer**

```json  theme={null}
{
  "type": "input_audio_buffer.append",
  "audio": "base64-encoded-audio-chunk"
}
```

Send audio data in base64-encoded PCM format.

**2. Commit Audio Buffer**

```json  theme={null}
{
  "type": "input_audio_buffer.commit"
}
```

Forces transcription of any remaining audio in the server-side buffer.

**Server → Client Messages**

**Delta Events (Intermediate Results)**

```json  theme={null}
{
  "type": "conversation.item.input_audio_transcription.delta",
  "delta": "The quick brown fox jumps"
}
```

Delta events are intermediate transcriptions. The model is still processing and may revise the output. Each delta message overrides the previous delta.

**Completed Events (Final Results)**

```json  theme={null}
{
  "type": "conversation.item.input_audio_transcription.completed",
  "transcript": "The quick brown fox jumps over the lazy dog"
}
```

Completed events are final transcriptions. The model is confident about this text. The next delta event will continue from where this completed.

**Real-time Example**

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import websockets
  import json
  import base64
  import os


  async def transcribe_audio():
      api_key = os.environ.get("TOGETHER_API_KEY")
      url = "wss://api.together.ai/v1/realtime?model=openai/whisper-large-v3&input_audio_format=pcm_s16le_16000"

      headers = {"Authorization": f"Bearer {api_key}"}

      async with websockets.connect(url, additional_headers=headers) as ws:
          # Read audio file
          with open("audio.wav", "rb") as f:
              audio_data = f.read()

          # Send audio in chunks with delay to simulate real-time
          chunk_size = 8192
          bytes_per_second = 16000 * 2  # 16kHz * 2 bytes (16-bit)
          delay_per_chunk = chunk_size / bytes_per_second

          for i in range(0, len(audio_data), chunk_size):
              chunk = audio_data[i : i + chunk_size]
              base64_chunk = base64.b64encode(chunk).decode("utf-8")
              await ws.send(
                  json.dumps(
                      {
                          "type": "input_audio_buffer.append",
                          "audio": base64_chunk,
                      }
                  )
              )
              # Simulate real-time streaming
              if i + chunk_size < len(audio_data):
                  await asyncio.sleep(delay_per_chunk)

          # Commit the audio buffer
          await ws.send(json.dumps({"type": "input_audio_buffer.commit"}))

          # Receive transcription results
          async for message in ws:
              data = json.loads(message)
              if (
                  data["type"]
                  == "conversation.item.input_audio_transcription.delta"
              ):
                  print(f"Partial: {data['delta']}")
              elif (
                  data["type"]
                  == "conversation.item.input_audio_transcription.completed"
              ):
                  print(f"Final: {data['transcript']}")
                  break
              elif (
                  data["type"]
                  == "conversation.item.input_audio_transcription.failed"
              ):
                  error = data.get("error", {})
                  print(f"Error: {error.get('message')}")
                  break


  asyncio.run(transcribe_audio())
  ```

  ```typescript TypeScript theme={null}
  import WebSocket from 'ws';
  import fs from 'fs';

  const apiKey = process.env.TOGETHER_API_KEY;
  const url = 'wss://api.together.ai/v1/realtime?model=openai/whisper-large-v3&input_audio_format=pcm_s16le_16000';

  const ws = new WebSocket(url, {
    headers: {
      'Authorization': `Bearer ${apiKey}`
    }
  });

  ws.on('open', async () => {
    console.log('WebSocket connection established!');

    // Read audio file
    const audioData = fs.readFileSync('audio.wav');

    // Send audio in chunks with delay to simulate real-time
    const chunkSize = 8192;
    const bytesPerSecond = 16000 * 2;  // 16kHz * 2 bytes (16-bit)
    const delayPerChunk = (chunkSize / bytesPerSecond) * 1000;  // Convert to ms

    for (let i = 0; i < audioData.length; i += chunkSize) {
      const chunk = audioData.slice(i, i + chunkSize);
      const base64Chunk = chunk.toString('base64');
      ws.send(JSON.stringify({
        type: 'input_audio_buffer.append',
        audio: base64Chunk
      }));

      // Simulate real-time streaming
      if (i + chunkSize < audioData.length) {
        await new Promise(resolve => setTimeout(resolve, delayPerChunk));
      }
    }

    // Commit audio buffer
    ws.send(JSON.stringify({
      type: 'input_audio_buffer.commit'
    }));
  });

  ws.on('message', (data) => {
    const message = JSON.parse(data.toString());

    if (message.type === 'conversation.item.input_audio_transcription.delta') {
      console.log(`Partial: ${message.delta}`);
    } else if (message.type === 'conversation.item.input_audio_transcription.completed') {
      console.log(`Final: ${message.transcript}`);
      ws.close();
    } else if (message.type === 'conversation.item.input_audio_transcription.failed') {
      const errorMessage = message.error?.message ?? message.message ?? 'Unknown error';
      console.error(`Error: ${errorMessage}`);
      ws.close();
    }
  });

  ws.on('error', (error) => {
    console.error('WebSocket error:', error);
  });
  ```
</CodeGroup>

## Audio Translation

Audio translation converts speech from any language to English text.

<CodeGroup>
  ```python Python theme={null}
  response = client.audio.translations.create(
      file="french_audio.mp3",
      model="openai/whisper-large-v3",
  )
  print(f"English translation: {response.text}")
  ```

  ```typescript TypeScript theme={null}
  const response = await together.audio.translations.create({
    file: 'french_audio.mp3',
    model: 'openai/whisper-large-v3',
  });
  console.log(`English translation: ${response.text}`);
  ```

  ```shell Shell theme={null}
  together audio translate french_audio.mp3 \
    --model openai/whisper-large-v3
  ```
</CodeGroup>

**Translation with Context**

<CodeGroup>
  ```python Python theme={null}
  response = client.audio.translations.create(
      file="business_meeting_spanish.mp3",
      model="openai/whisper-large-v3",
      prompt="This is a business meeting discussing quarterly sales results.",
  )
  ```

  ```shell Shell theme={null}
  together audio translate business_meeting_spanish.mp3 \
    --model openai/whisper-large-v3 \
    --prompt "This is a business meeting discussing quarterly sales results."
  ```
</CodeGroup>

## Speaker Diarization

Enable diarization to identify who is speaking when:

<CodeGroup>
  ```python Python theme={null}
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

  ```typescript TypeScript theme={null}
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

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/audio/transcriptions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -F "file=@meeting.mp3" \
       -F "model=openai/whisper-large-v3" \
       -F "diarize=true"
  ```
</CodeGroup>

**Example Response with Diarization:**

```json  theme={null}
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

## Word-level Timestamps

Get word-level timing information:

<CodeGroup>
  ```python Python theme={null}
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

  ```shell Shell theme={null}
  together audio transcribe audio.mp3 \
    --model openai/whisper-large-v3 \
    --response-format verbose_json \
    --timestamp-granularities word \
    --pretty
  ```
</CodeGroup>

**Example Output:**

```text Text theme={null}
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

## Response Formats

**JSON Format (Default)**

Returns only the transcribed/translated text:

```python Python theme={null}
response = client.audio.transcriptions.create(
    file="audio.mp3",
    model="openai/whisper-large-v3",
    response_format="json",
)

print(response.text)  # "Hello, this is a test recording."
```

**Verbose JSON Format**

Returns detailed information including timestamps:

<CodeGroup>
  ```python Python theme={null}
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

  ```shell Shell theme={null}
  together audio transcribe audio.mp3 \
    --model openai/whisper-large-v3 \
    --response-format verbose_json \
    --timestamp-granularities segment \
    --pretty
  ```
</CodeGroup>

**Example Output:**

```text Text theme={null}
[0.11s - 10.85s]: Call is now being recorded. Parker Scarves, how may I help you? Online for my wife, and it turns out they shipped the wrong... Oh, I am so sorry, sir. I got it for her birthday, which is tonight, and now I'm not 100% sure what I need to do. Okay, let me see if I can help. Do you have the item number of the Parker Scarves? I don't think so. Call the New Yorker, I... Excellent. What color do...

[10.88s - 21.73s]: Blue. The one they shipped was light blue. I wanted the darker one. What's the difference? The royal blue is a bit brighter. What zip code are you located in? One nine.

[22.04s - 32.62s]: Karen's Boutique, Termall. Is that close? I'm in my office. Okay, um, what is your name, sir? Charlie. Charlie Johnson. Is that J-O-H-N-S-O-N? And Mr. Johnson, do you have the Parker scarf in light blue with you now? I do. They shipped it to my office. It came in not that long ago. What I will do is make arrangements with Karen's Boutique for...

[32.62s - 41.03s]: you to Parker Scarf at no additional cost. And in addition, I was able to look up your order in our system, and I'm going to send out a special gift to you to make up for the inconvenience. Thank you. You're welcome. And thank you for calling Parker Scarf, and I hope your wife enjoys her birthday gift. Thank you. You're very welcome. Goodbye.

[43.50s - 44.20s]: you
```

## Advanced Features

**Temperature Control**

Adjust randomness in the output (0.0 = deterministic, 1.0 = creative):

<CodeGroup>
  ```python Python theme={null}
  response = client.audio.transcriptions.create(
      file="audio.mp3",
      model="openai/whisper-large-v3",
      temperature=0.0,  # Most deterministic
  )

  print(f"Text: {response.text}")
  ```

  ```shell Shell theme={null}
  together audio transcribe audio.mp3 \
    --model openai/whisper-large-v3 \
    --temperature 0.0
  ```
</CodeGroup>

## Async Support

All transcription and translation operations support async/await:

**Async Transcription**

```python Python theme={null}
import asyncio
from together import AsyncTogether


async def transcribe_audio():
    client = AsyncTogether()

    response = await client.audio.transcriptions.create(
        file="audio.mp3",
        model="openai/whisper-large-v3",
        language="en",
    )

    return response.text


## Run async function
result = asyncio.run(transcribe_audio())
print(result)
```

**Async Translation**

```python Python theme={null}
async def translate_audio():
    client = AsyncTogether()

    response = await client.audio.translations.create(
        file="foreign_audio.mp3",
        model="openai/whisper-large-v3",
    )

    return response.text


result = asyncio.run(translate_audio())
print(result)
```

**Concurrent Processing**

Process multiple audio files concurrently:

```python Python theme={null}
import asyncio
from together import AsyncTogether


async def process_multiple_files():
    client = AsyncTogether()

    files = ["audio1.mp3", "audio2.mp3", "audio3.mp3"]

    tasks = [
        client.audio.transcriptions.create(
            file=file,
            model="openai/whisper-large-v3",
        )
        for file in files
    ]

    responses = await asyncio.gather(*tasks)

    for i, response in enumerate(responses):
        print(f"File {files[i]}: {response.text}")


asyncio.run(process_multiple_files())
```

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


# SSO Lite
Source: https://docs.together.ai/docs/sso-lite



## What is SSO Lite?

<Warning>
  SSO Lite is only available for Scale and Enterprise accounts. If you would like to upgrade your account to use SSO please contact our [sales team](https://www.together.ai/contact-sales)
</Warning>

SSO Lite enables a secure multi-member collaboration model within a single Together account. With SSO Lite you can:

* Securely connect Together accounts with an existing Identity Provider (IdP). Our currently supported platforms include Google Workspace, Okta, Microsoft Entra, and JumpCloud.
* Onboard and offboard members through your IdP.
* Share access to organizational resources like fine-tuned models, inference analytics, and billing.

<Note>
  SSO Lite is currently in early access. Fine-grained role-based access and spend controls are on our roadmap and will be added to the SSO Lite experience in the future.
</Note>

## Benefits of SSO Lite

**Access the newest collaboration features:** SSO Lite unlocks multi-member org features, including shared resources and billing. Upcoming capabilities like spend controls, granular permissions, and advanced analytics will only be available in SSO Lite.

**Stronger security and compliance:** Individualized authentication via your IdP eliminates shared passwords, reduces risk, and makes onboarding/offboarding seamless.

## FAQs

### What does the setup process involve?

To get started, reach out to Customer Support or your Account Executive to let them know you'd like to enable SSO Lite.

Please include the following information with your request:

* Legal company name
* Email domain(s) used by your team (e.g., @company.com)
* Identity Provider (IdP) (e.g., Google Workspace, Okta, etc.)
* Account to use as the initial owner (this should be the account with the most Together usage)

### How long does setup take?

If you have an existing account/contract with Together, we aim to have SSO fully set up within 24–48 working hours of receiving your request. Complex configurations may take longer.

### Why are we moving away from shared username/password enterprise sign on accounts?

Our legacy "enterprise sign-on" required teams to share a single username/password account. This approach has several downsides:

* **Security risk** – shared credentials increase the chance of unauthorized access.
* **No scalability** – no way to onboard/offboard at the individual level.
* **No collaboration** – all activity is tied to one account, making it impossible to eventually share work or manage usage by members.
* **No future features** – we are retiring enterprise sign-on within the next 1–2 months and will not roll out any new improvements to it.

Going forward, we will not be recommending enterprise sign-on as the default path for team collaboration.

### I have a shared username/password enterprise sign on account, why should I migrate?

Enterprise sign-on will be deprecated in the coming months. Migrating now can prevent disruptive and time-consuming manual transitions later when your team has accumulated models, analytics, and billing history that are difficult to re-map.

### Does Together use my IdP's default session timeout?

No, Together sessions will have their own session timeout.


# Customer Ticket Portal
Source: https://docs.together.ai/docs/support-ticket-portal



The Customer Ticket Portal allows you to view all your support tickets and their status.

## Accessing the portal

To access your portal, first navigate and login to api.together.ai and click on "Help Center"

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/43.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=75a97fe05e25a0f71a332ada613b3705" alt="" data-og-width="1694" width="1694" data-og-height="806" height="806" data-path="images/guides/43.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/43.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=deee0e8d3457d9dd34f810b2ed4a1095 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/43.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=e260851a6a9246b9ba6894a2a3cb6040 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/43.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=56ac5b9a006bf0cd5f86824c0a2907b5 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/43.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=1166737b4c5f1dc35d8457b485661b3f 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/43.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d0b96e77f73c18618e88ae5ecdba27d6 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/43.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=0daba4480c1e8987cb3548c6c8047dcc 2500w" />
</Frame>

After being redirected, you will land in our help center:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/44.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=b079b31d3f0668a4232ab6cf2f6bff55" alt="" data-og-width="2580" width="2580" data-og-height="1180" height="1180" data-path="images/guides/44.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/44.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=8150c3e62487e0791d1543b5f64a4c28 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/44.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=3beaefee305a1246326c5defcce69254 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/44.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=743510340ae58d6b62e0ae78bd4fff51 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/44.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=2c08140f4a4ca4c3053e452647ea63ae 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/44.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d76797699de9ee9808b730a038513fe1 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/44.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=3cc8e6f1da6845bb75e633a5863273ba 2500w" />
</Frame>

Clicking on "Tickets portal" will show you all tickets related to or logged by your company. You can check the status of any ticket, and message us directly if you have further questions.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/45.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=3d45e5eaf764792f96e81f93e8ad7db7" alt="" data-og-width="2652" width="2652" data-og-height="1650" height="1650" data-path="images/guides/45.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/45.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=ef418a9c3458be4d7b7818c5c1d7ee68 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/45.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=6a4458ec9868e461feeb4d156edfbf51 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/45.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=a830f4300c60f0841612fce768c53d8d 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/45.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=6c9eb3707f7e2658e8b933c5ddc06dc3 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/45.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=00fdad53e54970622cebdbfb316f5cdb 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/45.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=9a060b3d7bc511b17fbcc208e8f839c4 2500w" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/46.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=e6ce9589fec63c128fddee175c37fa8f" alt="" data-og-width="2598" width="2598" data-og-height="1536" height="1536" data-path="images/guides/46.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/46.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=28a11a0e220bae7f09b412406f6b4846 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/46.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=968f4b6a8b0cbbb92ad5a806a2786c3b 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/46.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d9af911562beabd87b7d6d09da0fcfab 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/46.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=5e994e3677036d840d495a79c1f7d6bf 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/46.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=5b56db39321d88544bcb65d215f9482f 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/46.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=c466b559513ee4b4936021b6e8572d9f 2500w" />
</Frame>

## FAQs

### I can't find the ticket portal in the help center, what should I do?

1. Ensure you are authenticated by visiting api.together.ai before navigating to the help center.
2. If the portal is still not visible, it might not be set up for you yet. Please contact us at [support@together.ai](mailto:support@together.ai). Please note that the portal is only available to customers of GPU clusters or monthly reserved dedicated endpoints.

### The ticket I filed is not showing up in the portal, what should I do?

1. It may take up to 5 minutes for your ticket to appear in the portal.
2. If the ticket is still not visible after 5 minutes, please contact us at [support@together.ai](mailto:support@together.ai), and we will investigate.


# Text-to-Speech
Source: https://docs.together.ai/docs/text-to-speech

Learn how to use the text-to-speech functionality supported by Together AI.

Together AI provides comprehensive text-to-speech capabilities with multiple models and delivery methods. This guide covers everything from basic audio generation to real-time streaming via WebSockets.

## Quick Start

Here's how to get started with basic text-to-speech:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  speech_file_path = "speech.mp3"

  response = client.audio.speech.create(
      model="canopylabs/orpheus-3b-0.1-ft",
      input="Today is a wonderful day to build something people love!",
      voice="tara",
  )

  response.stream_to_file(speech_file_path)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  async function generateAudio() {
    const res = await together.audio.create({
      input: 'Hello, how are you today?',
      voice: 'tara',
      response_format: 'mp3',
      sample_rate: 44100,
      stream: false,
      model: 'canopylabs/orpheus-3b-0.1-ft',
    });

    if (res.body) {
      console.log(res.body);
      const nodeStream = Readable.from(res.body as ReadableStream);
      const fileStream = createWriteStream('./speech.mp3');

      nodeStream.pipe(fileStream);
    }
  }

  generateAudio();
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/audio/speech" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "canopylabs/orpheus-3b-0.1-ft",
         "input": "The quick brown fox jumps over the lazy dog",
         "voice": "tara"
       }' \
       --output speech.wav
  ```
</CodeGroup>

This will output a `speech.mp3` file.

## Available Models

Together AI supports multiple text-to-speech models:

| Organization | Model Name       | Model String for API         | API Endpoint Support       |
| :----------- | :--------------- | :--------------------------- | :------------------------- |
| Canopy Labs  | Orpheus 3B       | canopylabs/orpheus-3b-0.1-ft | Rest, Streaming, WebSocket |
| Kokoro       | Kokoro           | hexgrad/Kokoro-82M           | Rest, Streaming, WebSocket |
| Cartesia     | Cartesia Sonic 2 | cartesia/sonic-2             | Rest                       |
| Cartesia     | Cartesia Sonic   | cartesia/sonic               | Rest                       |

<Note>
  * Orpheus and Kokoro models support real-time WebSocket streaming for lowest latency applications.
  * To use Cartesia models, you need to be at Build Tier 2 or higher.
</Note>

## Parameters

| Parameter        | Type   | Required | Description                                                    |
| :--------------- | :----- | :------- | :------------------------------------------------------------- |
| model            | string | Yes      | The TTS model to use                                           |
| input            | string | Yes      | The text to generate audio for                                 |
| voice            | string | Yes      | The voice to use for generation. See [Voices](#voices) section |
| response\_format | string | No       | Output format: `mp3`, `wav`, or `raw` (PCM). Default: `wav`    |

For the full set of parameters refer to the API reference for [/audio/speech](/reference/audio-speech).

## Streaming Audio

For real-time applications where Time-To-First-Byte (TTFB) is critical, use streaming mode:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.audio.speech.create(
      model="canopylabs/orpheus-3b-0.1-ft",
      input="The quick brown fox jumps over the lazy dog",
      voice="tara",
      stream=True,
      response_format="raw",  # Required for streaming
      response_encoding="pcm_s16le",  # 16-bit PCM for clean audio
  )

  # Save the streamed audio to a file
  response.stream_to_file("speech_streaming.wav", response_format="wav")
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  async function streamAudio() {
    const response = await together.audio.speech.create({
      model: 'canopylabs/orpheus-3b-0.1-ft',
      input: 'The quick brown fox jumps over the lazy dog',
      voice: 'tara',
      stream: true,
      response_format: 'raw',  // Required for streaming
      response_encoding: 'pcm_s16le'  // 16-bit PCM for clean audio
    });

    // Process streaming chunks
    const chunks = [];
    for await (const chunk of response) {
      chunks.push(chunk);
    }

    console.log('Streaming complete!');
  }

  streamAudio();
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/audio/speech" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "canopylabs/orpheus-3b-0.1-ft",
         "input": "The quick brown fox jumps over the lazy dog",
         "voice": "tara",
         "stream": true
       }'
  ```
</CodeGroup>

**Streaming Response Format:**

When `stream: true`, the API returns a stream of events:

**Delta Event:**

```json  theme={null}
{
  "type": "delta",
  "audio": "base64-encoded-audio-data"
}
```

**Completion Event:**

```json  theme={null}
{
  "type": "done"
}
```

**Note:** When streaming is enabled, only `raw` (PCM) format is supported. For non-streaming, you can use `mp3`, `wav`, or `raw`.

## WebSocket API

For the lowest latency and most interactive applications, use the WebSocket API. This allows you to stream text input and receive audio chunks in real-time.

<Warning>
  The WebSocket API is currently only available via raw WebSocket connections. SDK support coming soon.
</Warning>

**Establishing a Connection**

Connect to: `wss://api.together.xyz/v1/audio/speech/websocket`

**Authentication:**

* Include your API key as a query parameter: `?api_key=YOUR_API_KEY`
* Or use the `Authorization` header when establishing the WebSocket connection

**Client → Server Messages**

**1. Append Text to Buffer**

```json  theme={null}
{
  "type": "input_text_buffer.append",
  "text": "Hello, this is a test sentence."
}
```

Appends text to the input buffer. Text is buffered until sentence completion or maximum length is reached.

**2. Commit Buffer**

```json  theme={null}
{
  "type": "input_text_buffer.commit"
}
```

Forces processing of all buffered text. Use this at the end of your input stream.

**3. Clear Buffer**

```json  theme={null}
{
  "type": "input_text_buffer.clear"
}
```

Clears all buffered text without processing (except text already being processed by the model).

**4. Update Session Parameters**

```json  theme={null}
{
  "type": "tts_session.updated",
  "session": {
    "voice": "new_voice_id"
  }
}
```

Updates TTS session settings like voice in real-time.

**Server → Client Messages**

**Session Created**

```json  theme={null}
{
  "event_id": "uuid-string",
  "type": "session.created",
  "session": {
    "id": "session-uuid",
    "object": "realtime.tts.session",
    "modalities": ["text", "audio"],
    "model": "canopylabs/orpheus-3b-0.1-ft",
    "voice": "tara"
  }
}
```

**Text Received Acknowledgment**

```json  theme={null}
{
  "type": "conversation.item.input_text.received",
  "text": "Hello, this is a test sentence."
}
```

**Audio Delta (Streaming Chunks)**

```json  theme={null}
{
  "type": "conversation.item.audio_output.delta",
  "item_id": "tts_1",
  "delta": "base64-encoded-audio-chunk"
}
```

**Audio Complete**

```json  theme={null}
{
  "type": "conversation.item.audio_output.done",
  "item_id": "tts_1"
}
```

**TTS Error**

```json  theme={null}
{
  "type": "conversation.item.tts.failed",
  "error": {
    "message": "Error description",
    "type": "error_type",
    "code": "error_code"
  }
}
```

**WebSocket Example**

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import websockets
  import json
  import base64
  import os


  async def generate_speech():
      api_key = os.environ.get("TOGETHER_API_KEY")
      url = "wss://api.together.ai/v1/audio/speech/websocket?model=hexgrad/Kokoro-82M&voice=af_alloy"

      headers = {"Authorization": f"Bearer {api_key}"}

      async with websockets.connect(url, additional_headers=headers) as ws:
          # Wait for session created
          session_msg = await ws.recv()
          session_data = json.loads(session_msg)
          print(f"Session created: {session_data['session']['id']}")

          # Send text for TTS
          text_chunks = [
              "Hello, this is a test.",
              "This is the second sentence.",
              "And this is the final one.",
          ]

          async def send_text():
              for chunk in text_chunks:
                  await ws.send(
                      json.dumps(
                          {"type": "input_text_buffer.append", "text": chunk}
                      )
                  )
                  await asyncio.sleep(0.5)  # Simulate typing

              # Commit to process any remaining text
              await ws.send(json.dumps({"type": "input_text_buffer.commit"}))

          async def receive_audio():
              audio_data = bytearray()
              async for message in ws:
                  data = json.loads(message)

                  if data["type"] == "conversation.item.input_text.received":
                      print(f"Text received: {data['text']}")
                  elif data["type"] == "conversation.item.audio_output.delta":
                      # Decode base64 audio chunk
                      audio_chunk = base64.b64decode(data["delta"])
                      audio_data.extend(audio_chunk)
                      print(f"Received audio chunk for item {data['item_id']}")
                  elif data["type"] == "conversation.item.audio_output.done":
                      print(
                          f"Audio generation complete for item {data['item_id']}"
                      )
                  elif data["type"] == "conversation.item.tts.failed":
                      error = data.get("error", {})
                      print(f"Error: {error.get('message')}")
                      break

              # Save the audio to a file
              with open("output.wav", "wb") as f:
                  f.write(audio_data)
              print("Audio saved to output.wav")

          # Run send and receive concurrently
          await asyncio.gather(send_text(), receive_audio())


  asyncio.run(generate_speech())
  ```

  ```typescript TypeScript theme={null}
  import WebSocket from 'ws';
  import fs from 'fs';

  const apiKey = process.env.TOGETHER_API_KEY;
  const url = 'wss://api.together.ai/v1/audio/speech/websocket?model=hexgrad/Kokoro-82M&voice=af_alloy';

  const ws = new WebSocket(url, {
    headers: {
      'Authorization': `Bearer ${apiKey}`
    }
  });

  const audioData: Buffer[] = [];

  ws.on('open', () => {
    console.log('WebSocket connection established!');
  });

  ws.on('message', (data) => {
    const message = JSON.parse(data.toString());

    if (message.type === 'session.created') {
      console.log(`Session created: ${message.session.id}`);
      
      // Send text chunks
      const textChunks = [
        "Hello, this is a test.",
        "This is the second sentence.",
        "And this is the final one."
      ];

      textChunks.forEach((text, index) => {
        setTimeout(() => {
          ws.send(JSON.stringify({
            type: 'input_text_buffer.append',
            text: text
          }));
        }, index * 500);
      });

      // Commit after all chunks
      setTimeout(() => {
        ws.send(JSON.stringify({
          type: 'input_text_buffer.commit'
        }));
      }, textChunks.length * 500 + 100);

    } else if (message.type === 'conversation.item.input_text.received') {
      console.log(`Text received: ${message.text}`);
    } else if (message.type === 'conversation.item.audio_output.delta') {
      // Decode base64 audio chunk
      const audioChunk = Buffer.from(message.delta, 'base64');
      audioData.push(audioChunk);
      console.log(`Received audio chunk for item ${message.item_id}`);
    } else if (message.type === 'conversation.item.audio_output.done') {
      console.log(`Audio generation complete for item ${message.item_id}`);
    } else if (message.type === 'conversation.item.tts.failed') {
      const errorMessage = message.error?.message ?? 'Unknown error';
      console.error(`Error: ${errorMessage}`);
      ws.close();
    }
  });

  ws.on('close', () => {
    // Save the audio to a file
    if (audioData.length > 0) {
      const completeAudio = Buffer.concat(audioData);
      fs.writeFileSync('output.wav', completeAudio);
      console.log('Audio saved to output.wav');
    }
  });

  ws.on('error', (error) => {
    console.error('WebSocket error:', error);
  });
  ```
</CodeGroup>

**WebSocket Parameters**

When establishing a WebSocket connection, you can configure:

| Parameter            | Type    | Description                                                 |
| :------------------- | :------ | :---------------------------------------------------------- |
| model\_id            | string  | The TTS model to use                                        |
| voice                | string  | The voice for generation                                    |
| response\_format     | string  | Audio format: `mp3`, `opus`, `aac`, `flac`, `wav`, or `pcm` |
| speed                | float   | Playback speed (default: 1.0)                               |
| max\_partial\_length | integer | Character buffer length before triggering TTS generation    |

## Output Raw Bytes

If you want to extract out raw audio bytes use the settings below:

<CodeGroup>
  ```python Python theme={null}
  import requests
  import os

  url = "https://api.together.xyz/v1/audio/speech"
  api_key = os.environ.get("TOGETHER_API_KEY")

  headers = {"Authorization": f"Bearer {api_key}"}

  data = {
      "input": "This is a test of raw PCM audio output.",
      "voice": "tara",
      "response_format": "raw",
      "response_encoding": "pcm_f32le",
      "sample_rate": 44100,
      "stream": False,
      "model": "canopylabs/orpheus-3b-0.1-ft",
  }

  response = requests.post(url, headers=headers, json=data)

  with open("output_raw.pcm", "wb") as f:
      f.write(response.content)

  print(f"✅ Raw PCM audio saved to output_raw.pcm")
  print(f"   Size: {len(response.content)} bytes")
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  async function generateRawBytes() {
    const res = await together.audio.create({
      input: 'Hello, how are you today?',
      voice: 'tara',
      response_format: 'raw',
      response_encoding: 'pcm_f32le',
      sample_rate: 44100,
      stream: false,
      model: 'canopylabs/orpheus-3b-0.1-ft',
    });

    console.log(res.body);
  }

  generateRawBytes();
  ```

  ```curl cURL theme={null}
  curl --location 'https://api.together.xyz/v1/audio/speech' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer $TOGETHER_API_KEY' \
  --output test2.pcm \
  --data '{
      "input": text,
      "voice": "tara",
      "response_format": "raw",
      "response_encoding": "pcm_f32le",
      "sample_rate": 44100,
      "stream": false,
      "model": "canopylabs/orpheus-3b-0.1-ft"
  }'
  ```
</CodeGroup>

This will output a raw bytes `test2.pcm` file.

## Response Formats

Together AI supports multiple audio formats:

| Format | Extension | Description                           | Streaming Support |
| :----- | :-------- | :------------------------------------ | :---------------- |
| wav    | .wav      | Uncompressed audio (larger file size) | No                |
| mp3    | .mp3      | Compressed audio (smaller file size)  | No                |
| raw    | .pcm      | Raw PCM audio data                    | Yes               |

## Best Practices

**Choosing the Right Delivery Method**

* **Basic HTTP API:** Best for batch processing or when you need complete audio files
* **Streaming HTTP API:** Best for real-time applications where TTFB matters
* **WebSocket API:** Best for interactive applications requiring lowest latency (chatbots, live assistants)

**Performance Tips**

* Use streaming when you need the fastest time-to-first-byte
* Use WebSocket API for conversational applications
* Buffer text appropriately - sentence boundaries work best for natural speech
* Use the `max_partial_length` parameter in WebSocket to control buffer behavior
* Consider using `raw` (PCM) format for lowest latency, then encode client-side if needed

**Voice Selection**

* Test different voices to find the best match for your application
* Some voices are better suited for specific content types (narration vs conversation)
* Use the Voices API to discover all available options

**Next Steps**

* Explore our [API Reference](/reference/audio-speech) for detailed parameter documentation
* Learn about [Speech-to-Text](/docs/speech-to-text) for the reverse operation
* Check out our [PDF to Podcast guide](/docs/open-notebooklm-pdf-to-podcast) for a complete example

## Supported Voices

Different models support different voices. Use the Voices API to discover available voices for each model.

**Voices API**

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  # List all available voices
  response = client.audio.voices.list()

  for model_voices in response.data:
      print(f"Model: {model_voices.model}")
      for voice in model_voices.voices:
          print(f"  - Voice: {voice['name']}")
  ```

  ```typescript TypeScript theme={null}
  import fetch from 'node-fetch';

  async function getVoices() {
    const apiKey = process.env.TOGETHER_API_KEY;
    const model = 'canopylabs/orpheus-3b-0.1-ft';
    const url = `https://api.together.xyz/v1/voices?model=${model}`;

    const response = await fetch(url, {
      headers: {
        'Authorization': `Bearer ${apiKey}`
      }
    });

    const data = await response.json();
    
    console.log(`Available voices for ${model}:`);
    console.log('='.repeat(50));
    
    // List available voices
    for (const voice of data.voices || []) {
      console.log(voice.name || 'Unknown voice');
    }
  }

  getVoices();
  ```

  ```curl cURL theme={null}
  curl -X GET "https://api.together.xyz/v1/voices?model=canopylabs/orpheus-3b-0.1-ft" \
       -H "Authorization: Bearer $TOGETHER_API_KEY"
  ```
</CodeGroup>

**Available Voices**

**Orpheus Model:**

Sample voices include:

```text Text theme={null}
`tara`
`leah`
`jess`
`leo`
`dan`
`mia`
`zac`
`zoe`
```

For a complete list, query the `/v1/voices` endpoint or see the [Kokoro voice documentation](https://github.com/remsky/Kokoro-FastAPI).

**Kokoro Model:**

```text Text theme={null}
af_heart
af_alloy
af_aoede
af_bella
af_jessica
af_kore
af_nicole
af_nova
af_river
af_sarah
af_sky
am_adam
am_echo
am_eric
am_fenrir
am_liam
am_michael
am_onyx
am_puck
am_santa
bf_alice
bf_emma
bf_isabella
bf_lily
bm_daniel
bm_fable
bm_george
bm_lewis
jf_alpha
jf_gongitsune
jf_nezumi
jf_tebukuro
jm_kumo
zf_xiaobei
zf_xiaoni
zf_xiaoxiao
zf_xiaoyi
zm_yunjian
zm_yunxi
zm_yunxia
zm_yunyang
ef_dora
em_alex
em_santa
ff_siwis
hf_alpha
hf_beta
hm_omega
hm_psi
if_sara
im_nicola
pf_dora
pm_alex
pm_santa
```

**Cartesia Models:**

All valid voice model strings:

```text Text theme={null}
'german conversational woman',
'nonfiction man',
'friendly sidekick',
'french conversational lady',
'french narrator lady',
'german reporter woman',
'indian lady',
'british reading lady',
'british narration lady',
'japanese children book',
'japanese woman conversational',
'japanese male conversational',
'reading lady',
'newsman',
'child',
'meditation lady',
'maria',
"1920's radioman",
'newslady',
'calm lady',
'helpful woman',
'mexican woman',
'korean narrator woman',
'russian calm lady',
'russian narrator man 1',
'russian narrator man 2',
'russian narrator woman',
'hinglish speaking lady',
'italian narrator woman',
'polish narrator woman',
'chinese female conversational',
'pilot over intercom',
'chinese commercial man',
'french narrator man',
'spanish narrator man',
'reading man',
'new york man',
'friendly french man',
'barbershop man',
'indian man',
'australian customer support man',
'friendly australian man',
'wise man',
'friendly reading man',
'customer support man',
'dutch confident man',
'dutch man',
'hindi reporter man',
'italian calm man',
'italian narrator man',
'swedish narrator man',
'polish confident man',
'spanish-speaking storyteller man',
'kentucky woman',
'chinese commercial woman',
'middle eastern woman',
'hindi narrator woman',
'sarah',
'sarah curious',
'laidback woman',
'reflective woman',
'helpful french lady',
'pleasant brazilian lady',
'customer support lady',
'british lady',
'wise lady',
'australian narrator lady',
'indian customer support lady',
'swedish calm lady',
'spanish narrator lady',
'salesman',
'yogaman',
'movieman',
'wizardman',
'australian woman',
'korean calm woman',
'friendly german man',
'announcer man',
'wise guide man',
'midwestern man',
'kentucky man',
'brazilian young man',
'chinese call center man',
'german reporter man',
'confident british man',
'southern man',
'classy british man',
'polite man',
'mexican man',
'korean narrator man',
'turkish narrator man',
'turkish calm man',
'hindi calm man',
'hindi narrator man',
'polish narrator man',
'polish young man',
'alabama male',
'australian male',
'anime girl',
'japanese man book',
'sweet lady',
'commercial lady',
'teacher lady',
'princess',
'commercial man',
'asmr lady',
'professional woman',
'tutorial man',
'calm french woman',
'new york woman',
'spanish-speaking lady',
'midwestern woman',
'sportsman',
'storyteller lady',
'spanish-speaking man',
'doctor mischief',
'spanish-speaking reporter man',
'young spanish-speaking woman',
'the merchant',
'stern french man',
'madame mischief',
'german storyteller man',
'female nurse',
'german conversation man',
'friendly brazilian man',
'german woman',
'southern woman',
'british customer support lady',
'chinese woman narrator',
'pleasant man',
'california girl',
'john',
'anna'
```

## Pricing

| Model            | Price                         |
| :--------------- | :---------------------------- |
| Orpheus 3B       | TBD                           |
| Kokoro           | TBD                           |
| Cartesia Sonic 2 | \$65 per 1 Million characters |


# QuickStart: LlamaRank
Source: https://docs.together.ai/docs/together-and-llamarank

Try out Salesforce's LlamaRank exclusively on Together's Rerank API

The Together AI platform makes it easy to run state-of-the-art models using only a few lines of code. [LlamaRank](https://blog.salesforceairesearch.com/llamarank/) is a proprietary reranker model developed by Salesforce AI Research that has been shown to outperform competitive reranker models like Cohere Rerank v3 and Mistral-7B QLM on accuracy.

Reranker models **improve search relevancy** by reassessing and reordering a set of retrieved documents based on their relevance to a given query. It takes a `query` and a set of text inputs (called `documents`), and returns a relevancy score for each document relative to the given query. In RAG pipelines, the reranking step sits between the initial retrieval step and the final generation phase, enhancing the quality of information fed into language models.

Try out Salesforce's LlamaRank *exclusively* on Together's serverless Rerank API endpoint. Together's Rerank API is **Cohere compatible**, making it easy to integrate into your existing applications.

## Key specs of Together Rerank + LlamaRank

LlamaRank along with Together Rerank has the following key specs:

* Support for JSON and tabular data
* Long 8000 token context per document
* LlamaRank has been shown to outperform other models on accuracy for general docs and code.
* Compatible with Cohere's Rerank API
* Low latency for fast search queries
* Linear relevancy scores, making it easier to interpret

## Quickstart

### 1. Get your Together API key

First, [register for an account](https://api.together.ai/settings/api-keys?utm_source=docs\&utm_medium=quickstart\&utm_campaign=salesforce-llamarank) to get an API key.

Once you've registered, set your account's API key to an environment variable named `TOGETHER_API_KEY`:

```sh Shell theme={null}
export TOGETHER_API_KEY=xxxxx
```

### 2. Install your preferred library

Together provides an official library for Python:

```sh  theme={null}
pip install together --upgrade
```

As well as an official library for TypeScript/JavaScript:

```sh  theme={null}
npm install together-ai
```

You can also call our HTTP API directly using any language you like.

### 3. Run your first reranking query against LlamaRank

In the example below, we use the Rerank API endpoint to index the list of `documents` from most to least relevant to the query `What animals can I find near Peru?`.

```py Python theme={null}
from together import Together

client = Together()

query = "What animals can I find near Peru?"

documents = [
    "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China.",
    "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
    "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia.",
    "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations.",
]

response = client.rerank.create(
    model="Salesforce/Llama-Rank-V1",
    query=query,
    documents=documents,
    top_n=2,
)

for result in response.results:
    print(f"Document Index: {result.index}")
    print(f"Document: {documents[result.index]}")
    print(f"Relevance Score: {result.relevance_score}")
```

In the example above, the documents being passed in are a list of strings, but Together's Rerank API also supports JSON data.

## Cohere Rerank compatibility

The Together Rerank endpoint is compatible with Cohere Rerank, making it easy to test out LlamaRank for your existing applications. Simply switch it out by updating the `URL`, `API key` and `model`.

```py Python theme={null}
import cohere

co = cohere.Client(
    base_url="https://api.together.xyz/v1",
    api_key=TOGETHER_API_KEY,
)
docs = [
    "Carson City is the capital city of the American state of Nevada.",
    "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
    "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
    "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
    "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
]
response = co.rerank(
    model="Salesforce/Llama-Rank-V1",
    query="What is the capital of the United States?",
    documents=docs,
    top_n=3,
)
```

## Interpreting Results

LlamaRank produces linear and calibrated scores across all (doc, query) pairs, normalized on a scale of 0-1, making it easier to interpret relevancy scores:

* 0.9 — Highly Relevant
* 0.8 \~ 0.7 — Relevant
* 0.6 \~ 0.5 — Somewhat Relevant
* 0.4 \~ 0.3 — Marginally Relevant
* 0.2 \~ 0.1 — Slightly Relevant
* \~ 0.0 — Irrelevant

## Next steps

* Learn more about [reranking and Together's Rerank endpoint](/docs/rerank-overview)
* Get started by [signing up for a free together.ai account](https://api.together.ai/settings/api-keys?utm_source=docs\&utm_medium=quickstart\&utm_campaign=salesforce-llamarank), and get your API key.
* If you'd like to discuss your production reranking use case, [contact our sales team](https://www.together.ai/forms/contact-sales).
* Check out our [playground](https://api.together.ai/playground) to try out other models on the Together Platform for chat, images, languages or code.


# Together Code Interpreter
Source: https://docs.together.ai/docs/together-code-interpreter

Execute LLM-generated code seamlessly with a simple API call.

Together Code Interpreter (TCI) enables you to execute Python code in a sandboxed environment.

The Code Interpreter currently only supports Python. We plan to expand the language options in the future.

> ℹ️ MCP Server
>
> TCI is also available as an MCP server through [Smithery](https://smithery.ai/server/@togethercomputer/mcp-server-tci). This makes it easier to add code interpreting abilities to any MCP client like Cursor, Windsurf, or your own chat app.

## Run your first query using the TCI

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  ## Run a simple print statement in the code interpreter
  response = client.code_interpreter.run(
      code='print("Welcome to Together Code Interpreter!")',
      language="python",
  )


  print(f"Status: {response.data.status}")


  for output in response.data.outputs:
      print(f"{output.type}: {output.data}")
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const client = new Together();

  const response = await client.codeInterpreter.execute({
    code: 'print("Welcome to Together Code Interpreter!")',
    language: 'python',
  });

  if (response.errors) {
    console.log(`Errors: ${response.errors}`);
  } else {
    for (const output of response.data.outputs) {
      console.log(`${output.type}: ${output.data}`);
    }
  }
  ```

  ```powershell Powershell theme={null}
  curl -X POST "https://api.together.ai/tci/execute" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "language": "python",
      "code": "print(\"Welcome to Together Code Interpreter!\")"
    }'
  ```
</CodeGroup>

Output

```text Text theme={null}
Status: completed
stdout: Welcome to Together Code Interpreter!
```

> ℹ️ Pricing information
>
> TCI usage is billed at **\$0.03/session**. As detailed below, sessions have a lifespan of 60 minutes and can be used multiple times.

## Example Use Cases

<img src="https://files.readme.io/6913d2c0f1b008027125934d85555f9a16ff5d7914dce9d62e57d1b0e2221676-TCI_workflow.png" alt="Overview of how Together Code Interpreter can be used in a code generation, execution and improvement iteration." style={{display: 'block', margin: '0 auto'}} />

* **Reinforcement learning (RL) training**: TCI transforms code execution into an interactive RL environment where generated code is run and evaluated in real time, providing reward signals from successes or failures, integrating automated pass/fail tests, and scaling easily across parallel workers—thus creating a powerful feedback loop that refines coding models over many trials.
* **Developing agentic workflows**: TCI allows AI agents to seamlessly write and execute Python code, enabling robust, iterative, and secure computations within a closed-loop system.

## Response Format

The API returns:

* `session_id`: Identifier for the current session
* `outputs`: Array of execution outputs, which can include:
  * Execution output (the return value of your snippet)
  * Standard output (`stdout`)
  * Standard error (`stderr`)
  * Error messages
  * Rich display data (images, HTML, etc.)
    Example

```json JSON theme={null}
{
  "data": {
    "outputs": [
      {
        "data": "Hello, world!\n",
        "type": "stdout"
      },
      {
        "data": {
          "image/png": "iVBORw0KGgoAAAANSUhEUgAAA...",
          "text/plain": "<Figure size 640x480 with 1 Axes>"
        },
        "type": "display_data"
      }
    ],
    "session_id": "ses_CM42NfvvzCab123"
  },
  "errors": null
}
```

## Usage overview

Together AI has created sessions to measure TCI usage.

A session is an active code execution environment that can be called to execute code, they can be used multiple times and have a lifespan of 60 minutes.

Typical TCI usage follows this workflow:

1. Start a session (create a TCI instance).
2. Call that session to execute code; TCI outputs `stdout` and `stderr`.
3. Optionally reuse an existing session by calling its `session_id`.

## Reusing sessions and maintaining state between runs

The `session_id` can be used to access a previously initialized session. All packages, variables, and memory will be retained.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  ## set a variable x to 42
  response1 = client.code_interpreter.run(code="x = 42", language="python")

  session_id = response1.data.session_id

  ## print the value of x
  response2 = client.code_interpreter.run(
      code='print(f"The value of x is {x}")',
      language="python",
      session_id=session_id,
  )

  for output in response2.data.outputs:
      print(f"{output.type}: {output.data}")
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const client = new Together();

   // Run the first session
  const response1 = await client.codeInterpreter.execute({
    code: 'x = 42',
    language: 'python',
  });

  if (response1.errors) {
    console.log(`Response 1 errors: ${response1.errors}`);
    return;
  }

  // Save the session_id
  const sessionId = response1.data.session_id;

  // Resuse the first session
  const response2 = await client.codeInterpreter.execute({
    code: 'print(f"The value of x is {x}")',
    language: 'python',
    session_id: sessionId,
  });

  if (response2.errors) {
    console.log(`Response 2 errors: ${response2.errors}`);
    return;
  }

  for (const output of response2.data.outputs) {
    console.log(`${output.type}: ${output.data}`);
  }
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.ai/tci/execute" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "language": "python",
      "code": "x = 42"
    }'

    curl -X POST "https://api.together.ai/tci/execute" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "language": "python",
      "code": "print(f\"The value of x is {x}\")",
      "session_id": "YOUR_SESSION_ID_FROM_FIRST_RESPONSE"
    }'
  ```
</CodeGroup>

Output

```text Text theme={null}
stdout: The value of x is 42
```

## Using the TCI for Data analysis

Together Code Interpreter is a very powerful tool and gives you access to a fully functional coding environment. You can install Python libraries and conduct fully fledged data analysis experiments.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  ## Create a code interpreter instance
  code_interpreter = client.code_interpreter

  code = """
  !pip install numpy
  import numpy as np

  ## Create a random matrix
  matrix = np.random.rand(3, 3)
  print("Random matrix:")
  print(matrix)

  ## Calculate eigenvalues
  eigenvalues = np.linalg.eigvals(matrix)
  print("\\nEigenvalues:")
  print(eigenvalues)
  """

  response = code_interpreter.run(code=code, language="python")

  for output in response.data.outputs:
      print(f"{output.type}: {output.data}")
  if response.data.errors:
      print(f"Errors: {response.data.errors}")
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const client = new Together();

  // Data analysis
  const code = `
    !pip install numpy
    import numpy as np

    # Create a random matrix
    matrix = np.random.rand(3, 3)
    print("Random matrix:")
    print(matrix)

    # Calculate eigenvalues
    eigenvalues = np.linalg.eigvals(matrix)
    print("\\nEigenvalues:")
    print(eigenvalues)
  `;

  const response = await client.codeInterpreter.execute({
    code,
    language: 'python',
  });

  if (response.errors) {
    console.log(`Errors: ${response.errors}`);
  } else {
    for (const output of response.data.outputs) {
      console.log(`${output.type}: ${output.data}`);
    }
  }
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.ai/tci/execute" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "language": "python",
      "code": "!pip install numpy\nimport numpy as np\n# Create a random matrix\nmatrix = np.random.rand(3, 3)\nprint(\"Random matrix:\")\nprint(matrix)\n# Calculate eigenvalues\neigenvalues = np.linalg.eigvals(matrix)\nprint(\"\\nEigenvalues:\")\nprint(eigenvalues)"
    }'
  ```
</CodeGroup>

## Uploading and using files with TCI

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  ## Create a code interpreter instance
  code_interpreter = client.code_interpreter

  script_content = "import sys\nprint(f'Hello from inside {sys.argv[0]}!')"

  ## Define the script file as a dictionary
  script_file = {
      "name": "myscript.py",
      "encoding": "string",
      "content": script_content,
  }

  code_to_run_script = "!python myscript.py"

  response = code_interpreter.run(
      code=code_to_run_script,
      language="python",
      files=[script_file],  # Pass the script dictionary in a list
  )

  ## Print results
  print(f"Status: {response.data.status}")
  for output in response.data.outputs:
      print(f"{output.type}: {output.data}")
  if response.data.errors:
      print(f"Errors: {response.data.errors}")
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  // Initialize the Together client
  const client = new Together();

  // Create a code interpreter instance
  const codeInterpreter = client.codeInterpreter;

  // Define the script content
  const scriptContent = "import sys\nprint(f'Hello from inside {sys.argv[0]}!')";

  // Define the script file as an object
  const scriptFile = {
    name: "myscript.py",
    encoding: "string",
    content: scriptContent,
  };

  // Define the code to run the script
  const codeToRunScript = "!python myscript.py";

  // Run the code interpreter
  async function runScript() {
    const response = await codeInterpreter.run({
      code: codeToRunScript,
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.ai/tci/execute" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "language": "python",
      "files": [
        {
          "name": "myscript.py",
          "encoding": "string",
          "content": "import sys\nprint(f'\''Hello from inside {sys.argv[0]}!'\'')"
        }
      ],
      "code": "!python myscript.py"
    }'
  ```
</CodeGroup>

Output

```text Text theme={null}
Status: completed
stdout: Hello from inside myscript.py!
```

## Pre-installed dependencies

TCI's Python sessions come pre-installed with the following dependencies, any other dependencies can be installed using a `!pip install` command in the python code.

```text Text theme={null}
- aiohttp
- beautifulsoup4
- bokeh
- gensim
- imageio
- joblib
- librosa
- matplotlib
- nltk
- numpy
- opencv-python
- openpyxl
- pandas
- plotly
- pytest
- python-docx
- pytz
- requests
- scikit-image
- scikit-learn
- scipy
- seaborn
- soundfile
- spacy
- textblob
- tornado
- urllib3
- xarray
- xlrd
- sympy
```

## List Active Sessions

To retrieve all your active sessions:

```curl cURL theme={null}
curl -X GET "https://api.together.ai/tci/sessions" \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json"
```

Output:

```json JSON theme={null}
{
  "data": {
  "sessions": [
    {
      "id":"ses_CM3zokEcfkdh5G8UiKApw",
      "started_at":"2025-03-12T10:34:22.125248Z",
      "execute_count":2,
      "last_execute_at":"2025-03-12T10:37:24.145685Z",
      "expires_at":"2025-03-12T11:04:22.125248Z"
    }
    ]
  },
  "errors": null
}
```

## Further reading

[TCI API Reference docs](/reference/tci-execute)

[Together Code Interpreter Cookbook](https://github.com/togethercomputer/together-cookbook/blob/main/Together_Code_Interpreter.ipynb)

## Troubleshooting & questions

If you have questions about integrating TCI into your workflow or encounter any issues, please [contact us](https://www.together.ai/contact).


# Together Code Sandbox
Source: https://docs.together.ai/docs/together-code-sandbox

Level-up generative code tooling with fast, secure code sandboxes at scale

Together Code Sandbox offers a fully configurable development environment with fast start-up times, robust snapshotting, and a suite of mature dev tools.

Together Code Sandbox can spin up a sandbox by cloning a template in under 3 seconds. Inside this VM, you can run any code, install any dependencies and even run servers.

Under the hood, the SDK uses the microVM infrastructure of CodeSandbox to spin up sandboxes. It supports:

* Memory snapshot/restore (checkpointing) at any point in time
* Resume/clone VMs from a snapshot in 3 seconds
* VM FS persistence (with git version control)
* Environment customization using Docker & Docker Compose (Dev Containers)

## Accessing Together Code Sandbox

Code Sandbox is a Together product that is currently available on our [custom plans](https://www.together.ai/contact-sales).\
A self-serve option is possible by creating an account with [CodeSandbox](https://codesandbox.io/pricing).

> 📌 About CodeSandbox.io
>
> [CodeSandbox](https://codesandbox.io/blog/joining-together-ai-introducing-codesandbox-sdk) is a Together company that is in process of migrating all relevant products to the Together platform. In the coming months, all Code Sandbox features will be fully migrated into your Together account.
>
> Note that Together Code Sandbox is referred to as the SDK within the CodeSandbox.io

## Getting Started

To get started, install the SDK:

```text Text theme={null}
npm install @codesandbox/sdk
```

Then, create an API token by going to [https://codesandbox.io/t/api](https://codesandbox.io/t/api), and clicking on the "Create API Token" button. You can then use this token to authenticate with the SDK:

```typescript TypeScript theme={null}
import { CodeSandbox } from "@codesandbox/sdk";
 
const sdk = new CodeSandbox(process.env.CSB_API_KEY!);
 
const sandbox = await sdk.sandboxes.create();
 
const session = await sandbox.connect();
 
const output = await session.commands.run("echo 'Hello World'");
 
console.log(output) // Hello World
```

<br />

## Sandbox life-cycle

By default a Sandbox will be created from a template. A template is a memory/fs snapshot of a Sandbox, meaning it will be a direct continuation of the template. If the template was running a dev server, that dev server is running when the Sandbox is created.

When you create, resume or restart a Sandbox you can access its `bootupType`. This value indicates how the Sandbox was started.

**FORK**: The Sandbox was created from a template. This happens when you call `create` successfully.\
**RUNNING**: The Sandbox was already running. This happens when you call `resume` and the Sandbox was already running.\
**RESUME**: The Sandbox was resumed from hibernation. This happens when you call `resume` and the Sandbox was hibernated.\
**CLEAN**: The Sandbox was created or resumed from scratch. This happens when you call `create` or `resume` and the Sandbox was not running and was missing a snapshot. This can happen if the Sandbox was shut down, restarted, the snapshot was expired (old snapshot) or if something went wrong.

## Managing CLEAN bootups

Whenever we boot a sandbox from scratch, we'll:

1. Start the Firecracker VM
2. Create a default user (called pitcher-host)
3. (optional) Build the Docker image specified in the .devcontainer/devcontainer.json file
4. Start the Docker container
5. Mount the /project/sandbox directory as a volume inside the Docker container

You will be able to connect to the Sandbox during this process and track its progress.

```javascript JavaScript theme={null}
const sandbox = await sdk.sandboxes.create()
 
const setupSteps = sandbox.setup.getSteps()
 
for (const step of setupSteps) {
  console.log(`Step: ${step.name}`);
  console.log(`Command: ${step.command}`);
  console.log(`Status: ${step.status}`);
 
  const output = await step.open()
 
  output.onOutput((output) => {
    console.log(output)
  })
 
  await step.waitUntilComplete()
}
```

<br />

## Using templates

Code Sandbox has default templates that you can use to create sandboxes. These templates are available in the Template Library and by default we use the "Universal" template. To create your own template you will need to use our CLI.

## Creating the template

Create a new folder in your project and add the files you want to have available inside your Sandbox. For example set up a Vite project:

```text Text theme={null}
npx create-vite@latest my-template
```

Now we need to configure the template with tasks so that it will install dependencies and start the dev server. Create a my-template/.codesandbox/tasks.json file with the following content:

```json JSON theme={null}
{  
    "setupTasks": [  
        "npm install"  
    ],  
    "tasks": {  
        "dev-server": {  
            "name": "Dev Server",  
            "command": "npm run dev",  
            "runAtStart": true  
        }  
    }  
}
```

The `setupTasks` will run after the Sandbox has started, before any other tasks.

Now we are ready to deploy the template to our clusters, run:

```text Text theme={null}
$ CSB_API_KEY=your-api-key npx @codesandbox/sdk build ./my-template --ports 5173
```

<br />

<Tip>
  ### Note

  The template will by default be built with Micro VM Tier unless you pass --vmTier to the build command.
</Tip>

This will start the process of creating Sandboxes for each of our clusters, write files, restart, wait for port 5173 to be available and then hibernate. This generates the snapshot that allows you to quickly create Sandboxes already running a dev server from the template.

When all clusters are updated successfully you will get a "Template Tag" back which you can use when you create your sandboxes.

```javascript JavaScript theme={null}
const sandbox = await sdk.sandboxes.create({  
    source: 'template',  
    id: 'some-template-tag'  
})
```

<br />

## Connecting Sandboxes in the browser

In addition to running your Sandbox in the server, you can also connect it to the browser. This requires some collaboration with the server.

```javascript JavaScript theme={null}
app.post('/api/sandboxes', async (req, res) => {
  const sandbox = await sdk.sandboxes.create();
  const session = await sandbox.createBrowserSession({
    // Create isolated sessions by using a unique reference to the user
    id: req.session.username,
  });
 
  res.json(session)
})
 
app.get('/api/sandboxes/:sandboxId', async (req, res) => {
  const sandbox = await sdk.sandboxes.resume(req.params.sandboxId);
  const session = await sandbox.createBrowserSession({
    // Resume any existing session by using the same user reference
    id: req.session.username,
  });
 
  res.json(session)
})
```

Then in the browser:

```javascript JavaScript theme={null}
import { connectToSandbox } from '@codesandbox/sdk/browser';
 
const sandbox = await connectToSandbox({
  // The session object you either passed on page load or fetched from the server
  session: initialSessionFromServer,
  // When reconnecting to the sandbox, fetch the session from the server
  getSession: (id) => fetchJson(`/api/sandboxes/${id}`)
});
 
await sandbox.fs.writeTextFile('test.txt', 'Hello World');
```

The browser session automatically manages the connection and will reconnect if the connection is lost. This is controlled by an option called `onFocusChange` and by default it will reconnect when the page is visible.

```javascript JavaScript theme={null}
const sandbox = await connectToSandbox({
  session: initialSessionFromServer,
  getSession: (id) => fetchJson(`/api/sandboxes/${id}`),
  onFocusChange: (notify) => {
    const onVisibilityChange = () => {
      notify(document.visibilityState === 'visible');
    }
 
    document.addEventListener('visibilitychange', onVisibilityChange);
 
    return () => {
      document.removeEventListener('visibilitychange', onVisibilityChange);
    }
  }
});
```

If you tell the browser session when it is in focus it will automatically reconnect when hibernated. Unless you explicitly disconnect the session.

While the `connectToSandbox` promise is resolving you can also listen to initialization events to show a loading state:

```javascript JavaScript theme={null}
const sandbox = await connectToSandbox({
  session: initialSessionFromServer,
  getSession: (id) => fetchJson(`/api/sandboxes/${id}`),
  onInitCb: (event) => {}
});
```

## Disconnecting the Sandbox

Disconnecting the session will end the session and automatically hibernate the sandbox after a timeout. You can also hibernate the sandbox explicitly from the server.

```javascript JavaScript theme={null}
import { connectToSandbox } from '@codesandbox/sdk/browser'
 
const sandbox = await connectToSandbox({
  session: initialSessionFromServer,
  getSession: (id) => fetchJson(`/api/sandboxes/${id}`),
})
 
// Disconnect returns a promise that resolves when the session is disconnected
sandbox.disconnect();
 
// Optionally hibernate the sandbox explicitly by creating an endpoint on your server
fetch('/api/sandboxes/' + sandbox.id + '/hibernate', {
  method: 'POST'
})
 
// You can reconnect explicitly from the browser by
sandbox.reconnect()
```

<br />

## Pricing

The self-serve option for running Code Sandbox is priced according to the CodeSandbox SDK plans which follows two main pricing components:

VM credits: Credits serve as the unit of measurement for VM runtime. One credit equates to a specific amount of resources used per hour, depending on the specs of the VM you are using. VM credits follow a pay-as-you-go approach and are priced at \$0.01486 per credit. Learn more about credits here.

VM concurrency: This defines the maximum number of VMs you can run simultaneously with the SDK. As explored below, each CodeSandbox plan has a different VM concurrency limit.

<Tip>
  ### Note

  We use minutes as the smallest unit of measurement for VM credits. E.g.: if a VM runs for 3 minutes and 25 seconds, we bill the equivalent of 4 minutes of VM runtime.
</Tip>

<br />

## VM credit prices by VM size

Below is a summary of how many VM credits are used per hour of runtime in each of our available VM sizes. Note that, by default, we recommend using the Nano VM size, as it should provide enough resources for most simple workflows (Pico is mostly suitable for very simple code execution jobs) .

| VM size | Credits / hour | Cost / hour | CPU      | RAM    |
| :------ | :------------- | :---------- | :------- | :----- |
| Pico    | 5 credits      | \$0.0743    | 2 cores  | 1 GB   |
| Nano    | 10 credits     | \$0.1486    | 2 cores  | 4 GB   |
| Micro   | 20 credits     | \$0.2972    | 4 cores  | 8 GB   |
| Small   | 40 credits     | \$0.5944    | 8 cores  | 16 GB  |
| Medium  | 80 credits     | \$1.1888    | 16 cores | 32 GB  |
| Large   | 160 credits    | \$2.3776    | 32 cores | 64 GB  |
| XLarge  | 320 credits    | \$4.7552    | 64 cores | 128 GB |

<br />

### Concurrent VMs

To pick the most suitable plan for your use case, consider how many concurrent VMs you require and pick the corresponding plan:

* Build (free) plan: 10 concurrent VMs
* Scale plan: 250 concurrent VMs
* Enterprise plan: custom concurrent VMs

In case you expect a a high volume of VM runtime, our Enterprise plan also provides special discounts on VM credits.

<Tip>
  ### For enterprise

  Please [contact Sales](https://www.together.ai/contact-sales)
</Tip>

### Estimating your bill

To estimate your bill, you must consider:

* The base price of your CodeSandbox plan.
* The number of included VM credits on that plan.
* How many VM credits you expect to require.

As an example, let's say you are planning to run 80 concurrent VMs on average, each running 3 hours per day, every day, on the Nano VM size. Here's the breakdown:

* You will need a Scale plan (which allows up to 100 concurrent VMs).
* You will use a total of 72,000 VM credits per month (80 VMs x 3 hours/day x 30 days x 10 credits/hour).
* Your Scale plan includes 1100 free VM credits each month, so you will purchase 70,900 VM credits (72,000 - 1100).

Based on this, your expected bill for that month is:

* Base price of Scale plan: \$170
* Total price of VM credits: $1053.57 (70,900 VM credits * $0.01486/credit)
* Total bill: \$1223.57

<br />

## Further reading

Learn more about Sandbox configurations and features on the [CodeSandbox SDK documentation page](https://codesandbox.io/docs/sdk/sandboxes)


# Quickstart: Using Mastra with Together AI
Source: https://docs.together.ai/docs/using-together-with-mastra

This guide will walk you through how to use Together models with Mastra.

[Mastra](https://mastra.ai) is a framework for building and deploying AI-powered features using a modern JavaScript stack powered by the [Vercel AI SDK](/docs/ai-sdk). Integrating with Together AI provides access to a wide range of models for building intelligent agents.

## Getting started

1. ### Create a new Mastra project

   First, create a new Mastra project using the CLI:

   ```bash  theme={null}
   pnpm dlx create-mastra@latest
   ```

   During the setup, the system prompts you to name your project, choose a default provider, and more. Feel free to use the default settings.

2. ### Install dependencies

   To use Together AI with Mastra, install the required packages:

   <CodeGroup>
     ```bash npm theme={null}
     npm i @ai-sdk/togetherai
     ```

     ```bash yarn theme={null}
     yarn add @ai-sdk/togetherai
     ```

     ```bash pnpm theme={null}
     pnpm add @ai-sdk/togetherai
     ```
   </CodeGroup>

3. ### Configure environment variables

   Create or update your `.env` file with your Together AI API key:

   ```bash  theme={null}
   TOGETHER_API_KEY=your-api-key-here
   ```

4. ### Configure your agent to use Together AI

   Now, update your agent configuration file, typically `src/mastra/agents/weather-agent.ts`, to use Together AI models:

   ```typescript src/mastra/agents/weather-agent.ts theme={null}
   import 'dotenv/config';
   import { Agent } from '@mastra/core/agent';
   import { createTogetherAI } from '@ai-sdk/togetherai';

   const together = createTogetherAI({
     apiKey: process.env.TOGETHER_API_KEY ?? "",
   });

   export const weatherAgent = new Agent({
     name: 'Weather Agent',
     instructions: `
         You are a helpful weather assistant that provides accurate weather information and can help planning activities based on the weather.
         Use the weatherTool to fetch current weather data.
   `,
     model: together("zai-org/GLM-4.5-Air-FP8"),
     tools: { weatherTool },
    // ... other configuration
   });

   (async () => {
     try {
       const response = await weatherAgent.generate(
         "What's the weather in San Francisco today?",
       );
       console.log('Weather Agent Response:', response.text);
     } catch (error) {
       console.error('Error invoking weather agent:', error);
     }
   })();
   ```

5. ### Running the application

   Since your agent is now configured to use Together AI, run the Mastra development server:

   <CodeGroup>
     ```bash npm theme={null}
     npm run dev
     ```

     ```bash yarn theme={null}
     yarn dev
     ```

     ```bash pnpm theme={null}
     pnpm dev
     ```
   </CodeGroup>

   Open the [Mastra Playground and Mastra API](https://mastra.ai/en/docs/server-db/local-dev-playground) to test your agents, workflows, and tools.

## Next Steps

* Explore the [Mastra documentation](https://mastra.ai) for more advanced features
* Check out [Together AI's model documentation](https://docs.together.ai/docs/serverless-models) for the latest available models
* Learn about building workflows and tools in Mastra


# Quickstart: Using Vercel AI SDK With Together AI
Source: https://docs.together.ai/docs/using-together-with-vercels-ai-sdk

This guide will walk you through how to use Together models with the Vercel AI SDK.

The Vercel AI SDK is a powerful Typescript library designed to help developers build AI-powered applications. Using Together AI and the Vercel AI SDK, you can easily integrate AI into your TypeScript, React, or Next.js project. In this tutorial, we'll look into how easy it is to use Together AI's models and the Vercel AI SDK.

## QuickStart: 15 lines of code

1. Install both the Vercel AI SDK and Together.ai's Vercel package.

<CodeGroup>
  ```bash npm theme={null}
  npm i ai @ai-sdk/togetherai
  ```

  ```bash yarn theme={null}
  yarn add ai @ai-sdk/togetherai
  ```

  ```bash pnpm  theme={null}
  pnpm add ai @ai-sdk/togetherai
  ```
</CodeGroup>

2. Import the Together.ai provider and call the `generateText` function with Kimi K2 to generate some text.

```js TypeScript theme={null}
import { generateText } from "ai";
import { createTogetherAI } from '@ai-sdk/togetherai';

const together = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

async function main() {
  const { text } = await generateText({
    model: together("moonshotai/Kimi-K2-Instruct-0905"),
    prompt: "Write a vegetarian lasagna recipe for 4 people.",
  });

  console.log(text);
}

main();
```

### Output

```
Here's a delicious vegetarian lasagna recipe for 4 people:

**Ingredients:**

- 8-10 lasagna noodles
- 2 cups marinara sauce (homemade or store-bought)
- 1 cup ricotta cheese
- 1 cup shredded mozzarella cheese
- 1 cup grated Parmesan cheese
- 1 cup frozen spinach, thawed and drained
- 1 cup sliced mushrooms
- 1 cup sliced bell peppers
- 1 cup sliced zucchini
- 1 small onion, chopped
- 2 cloves garlic, minced
- 1 cup chopped fresh basil
- Salt and pepper to taste
- Olive oil for greasing the baking dish

**Instructions:**

1. **Preheat the oven:** Preheat the oven to 375°F (190°C).
2. **Prepare the vegetables:** Sauté the mushrooms, bell peppers, zucchini, and onion in a little olive oil until they're tender. Add the garlic and cook for another minute.
3. **Prepare the spinach:** Squeeze out as much water as possible from the thawed spinach. Mix it with the ricotta cheese and a pinch of salt and pepper.
4. **Assemble the lasagna:** Grease a 9x13-inch baking dish with olive oil. Spread a layer of marinara sauce on the bottom. Arrange 4 lasagna noodles on top.
5. **Layer 1:** Spread half of the spinach-ricotta mixture on top of the noodles. Add half of the sautéed vegetables and half of the shredded mozzarella cheese.
6. **Layer 2:** Repeat the layers: marinara sauce, noodles, spinach-ricotta mixture, sautéed vegetables, and mozzarella cheese.
7. **Top layer:** Spread the remaining marinara sauce on top of the noodles. Sprinkle with Parmesan cheese and a pinch of salt and pepper.
8. **Bake the lasagna:** Cover the baking dish with aluminum foil and bake for 30 minutes. Remove the foil and bake for another 10-15 minutes, or until the cheese is melted and bubbly.
9. **Let it rest:** Remove the lasagna from the oven and let it rest for 10-15 minutes before slicing and serving.

**Tips and Variations:**

- Use a variety of vegetables to suit your taste and dietary preferences.
- Add some chopped olives or artichoke hearts for extra flavor.
- Use a mixture of mozzarella and Parmesan cheese for a richer flavor.
- Serve with a side salad or garlic bread for a complete meal.

**Nutrition Information (approximate):**

Per serving (serves 4):

- Calories: 450
- Protein: 25g
- Fat: 20g
- Saturated fat: 8g
- Cholesterol: 30mg
- Carbohydrates: 40g
- Fiber: 5g
- Sugar: 10g
- Sodium: 400mg

Enjoy your delicious vegetarian lasagna!
```

## Streaming with the Vercel AI SDK

To stream from Together AI models using the Vercel AI SDK, simply use `streamText` as seen below.

```js TypeScript theme={null}
import { streamText } from "ai";
import { createTogetherAI } from '@ai-sdk/togetherai';

const together = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

async function main() {
  const result = await streamText({
    model: together("moonshotai/Kimi-K2-Instruct-0905"),
    prompt: "Invent a new holiday and describe its traditions.",
  });

  for await (const textPart of result.textStream) {
    process.stdout.write(textPart);
  }
}

main();
```

### Output

```
Introducing "Luminaria Day" - a joyous holiday celebrated on the spring equinox, marking the return of warmth and light to the world. This festive occasion is a time for family, friends, and community to come together, share stories, and bask in the radiance of the season.

**Date:** Luminaria Day is observed on the spring equinox, typically around March 20th or 21st.

**Traditions:**

1. **The Lighting of the Lanterns:** As the sun rises on Luminaria Day, people gather in their neighborhoods, parks, and public spaces to light lanterns made of paper, wood, or other sustainable materials. These lanterns are adorned with intricate designs, symbols, and messages of hope and renewal.
2. **The Storytelling Circle:** Families and friends gather around a central fire or candlelight to share stories of resilience, courage, and triumph. These tales are passed down through generations, serving as a reminder of the power of human connection and the importance of learning from the past.
3. **The Luminaria Procession:** As the sun sets, communities come together for a vibrant procession, carrying their lanterns and sharing music, dance, and laughter. The procession winds its way through the streets, symbolizing the return of light and life to the world.
4. **The Feast of Renewal:** After the procession, people gather for a festive meal, featuring dishes made with seasonal ingredients and traditional recipes. The feast is a time for gratitude, reflection, and celebration of the cycle of life.
5. **The Gift of Kindness:** On Luminaria Day, people are encouraged to perform acts of kindness and generosity for others. This can take the form of volunteering, donating to charity, or simply offering a helping hand to a neighbor in need.

**Symbolism:**

* The lanterns represent the light of hope and guidance, illuminating the path forward.
* The storytelling circle symbolizes the power of shared experiences and the importance of learning from one another.
* The procession represents the return of life and energy to the world, as the seasons shift from winter to spring.
* The feast of renewal celebrates the cycle of life, death, and rebirth.
* The gift of kindness embodies the spirit of generosity and compassion that defines Luminaria Day.

**Activities:**

* Create your own lanterns using recycled materials and decorate them with symbols, messages, or stories.
* Share your own stories of resilience and triumph with family and friends.
* Participate in the Luminaria Procession and enjoy the music, dance, and laughter.
* Prepare traditional dishes for the Feast of Renewal and share them with loved ones.
* Perform acts of kindness and generosity for others, spreading joy and positivity throughout your community.

Luminaria Day is a time to come together, celebrate the return of light and life, and honor the power of human connection.
```

## Image Generation

> This feature is still marked as experimental with Vercel SDK

To generate images with Together AI models using the Vercel AI SDK, use the `.image()` factory method. For more on image generation with the AI SDK see [generateImage()](/docs/reference/ai-sdk-core/generate-image).

```js TypeScript theme={null}
import { createTogetherAI } from '@ai-sdk/togetherai';
import { experimental_generateImage as generateImage } from 'ai';

const togetherai = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

const { images } = await generateImage({
  model: togetherai.image('black-forest-labs/FLUX.1-dev'),
  prompt: 'A delighted resplendent quetzal mid flight amidst raindrops',
});

// The images array contains base64-encoded image data by default
```

You can pass optional provider-specific request parameters using the `providerOptions` argument.

```js TypeScript theme={null}
import { createTogetherAI } from '@ai-sdk/togetherai';
import { experimental_generateImage as generateImage } from 'ai';

const togetherai = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

const { images } = await generateImage({
  model: togetherai.image('black-forest-labs/FLUX.1-dev'),
  prompt: 'A delighted resplendent quetzal mid flight amidst raindrops',
  size: '512x512',
  // Optional additional provider-specific request parameters
  providerOptions: {
    togetherai: {
      steps: 40,
    },
  },
});
```

Together.ai image models support various image dimensions that vary by model. Common sizes include 512x512, 768x768, and 1024x1024, with some models supporting up to 1792x1792. The default size is 1024x1024.

Available Models:

* `black-forest-labs/FLUX.1-schnell-Free` (free)
* `black-forest-labs/FLUX.1-schnell` (Turbo)
* `black-forest-labs/FLUX.1-dev`
* `black-forest-labs/FLUX.1.1-pro`
* `black-forest-labs/FLUX.1-kontext-pro`
* `black-forest-labs/FLUX.1-kontext-max`
* `black-forest-labs/FLUX.1-kontext-dev`
* `black-forest-labs/FLUX.1-krea-dev`

Please see the [Together.ai models page](https://docs.together.ai/docs/serverless-models#image-models) for a full list of available image models and their capabilities.

## Embedding Models

To embed text with Together AI models using the Vercel AI SDK, use the `.textEmbedding()` factory method.
For more on embedding models with the AI SDK see [embed()](/docs/reference/ai-sdk-core/embed).

```js TypeScript theme={null}
import { createTogetherAI } from '@ai-sdk/togetherai';
import { embed } from 'ai';

const togetherai = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

const { embedding } = await embed({
  model: togetherai.textEmbedding('togethercomputer/m2-bert-80M-2k-retrieval'),
  value: 'sunny day at the beach',
});
```

<Note>
  For a complete list of available embedding models and their model IDs, see the [Together.ai models
  page](https://docs.together.ai/docs/serverless-models#embedding-models).
</Note>

Some available model IDs include:

* `BAAI/bge-large-en-v1.5`
* `BAAI/bge-base-en-v1.5`
* `Alibaba-NLP/gte-modernbert-base`
* `intfloat/multilingual-e5-large-instruct`

***


# Videos
Source: https://docs.together.ai/docs/videos-overview

Generate high-quality videos from text and image prompts.

## Generating a video

Video generation is asynchronous. You create a job, receive a job ID, and poll for completion.

<CodeGroup>
  ```py Python theme={null}
  import time
  from together import Together

  client = Together()

  # Create a video generation job
  job = client.videos.create(
      prompt="A serene sunset over the ocean with gentle waves",
      model="minimax/video-01-director",
      width=1366,
      height=768,
  )

  print(f"Job ID: {job.id}")

  # Poll until completion
  while True:
      status = client.videos.retrieve(job.id)
      print(f"Status: {status.status}")

      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          break
      elif status.status == "failed":
          print("Video generation failed")
          break

      # Wait before checking again
      time.sleep(5)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    // Create a video generation job
    const job = await together.videos.create({
      prompt: "A serene sunset over the ocean with gentle waves",
      model: "minimax/video-01-director",
      width: 1366,
      height: 768,
    });

    console.log(`Job ID: ${job.id}`);

    // Poll until completion
    while (true) {
      const status = await together.videos.retrieve(job.id);
      console.log(`Status: ${status.status}`);

      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        break;
      } else if (status.status === "failed") {
        console.log("Video generation failed");
        break;
      }

      // Wait before checking again
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  }

  main();
  ```
</CodeGroup>

Example output when the job is complete:

```json  theme={null}
{
  "id": "019a0068-794a-7213-90f6-cc4eb62e3da7",
  "model": "minimax/video-01-director",
  "status": "completed",
  "info": {
    "user_id": "66f0bd504fb9511df3489b9a",
    "errors": null
  },
  "inputs": {
    "fps": null,
    "guidance_scale": null,
    "height": 768,
    "metadata": {},
    "model": "minimax/video-01-director",
    "output_quality": null,
    "prompt": "A serene sunset over the ocean with gentle waves",
    "seconds": null,
    "seed": null,
    "steps": null,
    "width": 1366
  },
  "outputs": {
    "cost": 0.28,
    "video_url": "https://api.together.ai/shrt/DwlaBdSakNRFlBxN"
  },
  "created_at": "2025-10-20T06:57:18.154804Z",
  "claimed_at": "0001-01-01T00:00:00Z",
  "done_at": "2025-10-20T07:00:12.234472Z"
}
```

**Job Status Reference:**

| Status        | Description                            |
| ------------- | -------------------------------------- |
| `queued`      | Job is waiting in queue                |
| `in_progress` | Video is being generated               |
| `completed`   | Generation successful, video available |
| `failed`      | Generation failed, check `info.errors` |
| `cancelled`   | Job was cancelled                      |

## Parameters

| Parameter         | Type    | Description                                                                                                                                                              | Default      |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| `prompt`          | string  | Text description of the video to generate                                                                                                                                | **Required** |
| `model`           | string  | Model identifier                                                                                                                                                         | **Required** |
| `width`           | integer | Video width in pixels                                                                                                                                                    | 1366         |
| `height`          | integer | Video height in pixels                                                                                                                                                   | 768          |
| `seconds`         | integer | Length of video (1-10)                                                                                                                                                   | 6            |
| `fps`             | integer | Frames per second                                                                                                                                                        | 15-60        |
| `steps`           | integer | Diffusion steps (higher = better quality, slower)                                                                                                                        | 10-50        |
| `guidance_scale`  | float   | How closely to follow prompt                                                                                                                                             | 6.0-10.0     |
| `seed`            | integer | Random seed for reproducibility                                                                                                                                          | any          |
| `output_format`   | string  | Video format (MP4, GIF)                                                                                                                                                  | MP4          |
| `output_quality`  | integer | Bitrate/quality (lower = higher quality)                                                                                                                                 | 20           |
| `negative_prompt` | string  | What to avoid in generation                                                                                                                                              | -            |
| `frame_images`    | Array   | Array of images to guide video generation, like keyframes.  If size 1, starting frame, if size 2, starting and ending frame, if more than 2 then frame must be specified |              |

* `prompt` is required for all models except Kling
* `width` and `height` will rely on defaults unless otherwise specified - options for dimensions vary by model

These parameters vary by model, please refer to the [models table](/docs/videos-overview#supported-model-details) for details.

Generate customized videos using the above parameters:

<CodeGroup>
  ```py Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A futuristic city at night with neon lights reflecting on wet streets",
      model="minimax/hailuo-02",
      width=1366,
      height=768,
      seconds=6,
      fps=30,
      steps=30,
      guidance_scale=8.0,
      output_format="MP4",
      output_quality=20,
      seed=42,
      negative_prompt="blurry, low quality, distorted",
  )

  print(f"Job ID: {job.id}")

  # Poll until completion
  while True:
      status = client.videos.retrieve(job.id)
      print(f"Status: {status.status}")

      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          print(f"Cost: ${status.outputs.cost}")
          break
      elif status.status == "failed":
          print("Video generation failed")
          break

      # Wait before checking again
      time.sleep(5)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "A futuristic city at night with neon lights reflecting on wet streets",
      model: "minimax/hailuo-02",
      width: 1366,
      height: 768,
      seconds: 6,
      fps: 30,
      steps: 30,
      guidance_scale: 8.0,
      output_format: "MP4",
      output_quality: 20,
      seed: 42,
      negative_prompt: "blurry, low quality, distorted"
    });

    console.log(`Job ID: ${job.id}`);

    // Poll until completion
    while (true) {
      const status = await together.videos.retrieve(job.id);
      console.log(`Status: ${status.status}`);

      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        console.log(`Cost: $${status.outputs.cost}`);
        break;
      } else if (status.status === "failed") {
        console.log("Video generation failed");
        break;
      }

      // Wait before checking again
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  }

  main();
  ```
</CodeGroup>

## Reference Images

Guide your video's visual style with reference images:

<CodeGroup>
  ```py Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A cat dancing energetically",
      model="minimax/hailuo-02",
      width=1366,
      height=768,
      seconds=6,
      reference_images=[
          "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
      ],
  )

  print(f"Job ID: {job.id}")

  # Poll until completion
  while True:
      status = client.videos.retrieve(job.id)
      print(f"Status: {status.status}")

      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          break
      elif status.status == "failed":
          print("Video generation failed")
          break

      # Wait before checking again
      time.sleep(5)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "A cat dancing energetically",
      model: "minimax/hailuo-02",
      width: 1366,
      height: 768,
      seconds: 6,
      reference_images: [
        "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
      ]
    });

    console.log(`Job ID: ${job.id}`);

    // Poll until completion
    while (true) {
      const status = await together.videos.retrieve(job.id);
      console.log(`Status: ${status.status}`);

      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        break;
      } else if (status.status === "failed") {
        console.log("Video generation failed");
        break;
      }

      // Wait before checking again
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  }

  main();
  ```
</CodeGroup>

## Keyframe Control

Control specific frames in your video for precise transitions.

**Single Keyframe:** Set a single(for the example below this is the first frame) frame to a specific image.

Depending on the model you can also specify to set multiple keyframes please refer to the [models table](/docs/videos-overview#supported-model-details) for details.

<CodeGroup>
  ```py Python theme={null}
  import base64
  import requests
  import time
  from together import Together

  client = Together()

  # Download image and encode to base64
  image_url = (
      "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg"
  )
  response = requests.get(image_url)
  base64_image = base64.b64encode(response.content).decode("utf-8")

  # Single keyframe at start
  job = client.videos.create(
      prompt="Smooth transition from day to night",
      model="minimax/hailuo-02",
      width=1366,
      height=768,
      fps=24,
      frame_images=[{"input_image": base64_image, "frame": 0}],  # Starting frame
  )

  print(f"Job ID: {job.id}")

  # Poll until completion
  while True:
      status = client.videos.retrieve(job.id)
      print(f"Status: {status.status}")

      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          break
      elif status.status == "failed":
          print("Video generation failed")
          break

      # Wait before checking again
      time.sleep(5)
  ```

  ```ts TypeScript theme={null}
  import * as fs from 'fs';
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    // Load and encode your image
    const imageBuffer = fs.readFileSync('keyframe.jpg');
    const base64Image = imageBuffer.toString('base64');

    // Single keyframe at start
    const job = await together.videos.create({
      prompt: "Smooth transition from day to night",
      model: "minimax/hailuo-02",
      width: 1366,
      height: 768,
      fps: 24,
      frame_images: [
        {
          input_image: base64Image,
          frame: 0  // Starting frame
        }
      ]
    });

    console.log(`Job ID: ${job.id}`);

    // Poll until completion
    while (true) {
      const status = await together.videos.retrieve(job.id);
      console.log(`Status: ${status.status}`);

      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        break;
      } else if (status.status === "failed") {
        console.log("Video generation failed");
        break;
      }

      // Wait before checking again
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  }

  main();
  ```
</CodeGroup>

**💡 Tip:** Frame number = seconds × fps

## Guidance Scale

Controls how closely the model follows your prompt:

* **6.0-7.0**: More creative, less literal
* **7.0-9.0**: Sweet spot for most use cases
* **9.0-10.0**: Strict adherence to prompt
* **>12.0**: Avoid - may cause artifacts

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  # Low guidance - more creative interpretation
  job_creative = client.videos.create(
      prompt="an astronaut riding a horse on the moon",
      model="minimax/hailuo-02",
      guidance_scale=6.0,
      seed=100,
  )

  # High guidance - closer to literal prompt
  job_literal = client.videos.create(
      prompt="an astronaut riding a horse on the moon",
      model="minimax/hailuo-02",
      guidance_scale=10.0,
      seed=100,
  )
  ```

  ```ts TypeScript theme={null}
  // Low guidance - more creative interpretation
  import Together from "together-ai";

  const together = new Together();

  const jobCreative = await together.videos.create({
    prompt: "an astronaut riding a horse on the moon",
    model: "minimax/hailuo-02",
    guidance_scale: 6.0,
    seed: 100
  });

  // High guidance - closer to literal prompt
  const jobLiteral = await together.videos.create({
    prompt: "an astronaut riding a horse on the moon",
    model: "minimax/hailuo-02",
    guidance_scale: 10.0,
    seed: 100
  });
  ```
</CodeGroup>

## Quality Control with Steps

Trade off between generation time and quality:

* **10 steps**: Quick testing, lower quality
* **20 steps**: Standard quality, good balance
* **30-40 steps**: Production quality, slower
* **>50 steps**: Diminishing returns

<CodeGroup>
  ```py Python theme={null}
  # Quick preview
  job_quick = client.videos.create(
      prompt="A person walking through a forest",
      model="minimax/hailuo-02",
      steps=10,
  )

  # Production quality
  job_production = client.videos.create(
      prompt="A person walking through a forest",
      model="minimax/hailuo-02",
      steps=40,
  )
  ```

  ```ts TypeScript theme={null}
  // Quick preview
  import Together from "together-ai";

  const together = new Together();

  const jobQuick = await together.videos.create({
    prompt: "A person walking through a forest",
    model: "minimax/hailuo-02",
    steps: 10
  });

  // Production quality
  const jobProduction = await together.videos.create({
    prompt: "A person walking through a forest",
    model: "minimax/hailuo-02",
    steps: 40
  });
  ```
</CodeGroup>

## Supported Model Details

See our supported video models and relevant parameters below.

| **Organization** | **Name**             | **Model API String**          | **Duration** | **Dimensions**                                                                                      | **FPS** | **Keyframes** | **Prompt**  |
| :--------------- | :------------------- | :---------------------------- | :----------- | :-------------------------------------------------------------------------------------------------- | :------ | :------------ | :---------- |
| **MiniMax**      | MiniMax 01 Director  | `minimax/video-01-director`   | 5s           | 1366×768                                                                                            | 25      | First         | 2-3000 char |
| **MiniMax**      | MiniMax Hailuo 02    | `minimax/hailuo-02`           | 10s          | 1366×768, 1920×1080                                                                                 | 25      | First         | 2-3000 char |
| **Google**       | Veo 2.0              | `google/veo-2.0`              | 5s           | 1280×720, 720×1280                                                                                  | 24      | First, Last   | 2-3000 char |
| **Google**       | Veo 3.0              | `google/veo-3.0`              | 8s           | 1280×720, 720×1280, 1920×1080, 1080×1920                                                            | 24      | First         | 2-3000 char |
| **Google**       | Veo 3.0 + Audio      | `google/veo-3.0-audio`        | 8s           | 1280×720, 720×1280, 1920×1080, 1080×1920                                                            | 24      | First         | 2-3000 char |
| **Google**       | Veo 3.0 Fast         | `google/veo-3.0-fast`         | 8s           | 1280×720, 720×1280, 1920×1080, 1080×1920                                                            | 24      | First         | 2-3000 char |
| **Google**       | Veo 3.0 Fast + Audio | `google/veo-3.0-fast-audio`   | 8s           | 1280×720, 720×1280, 1920×1080, 1080×1920                                                            | 24      | First         | 2-3000 char |
| **ByteDance**    | Seedance 1.0 Lite    | `ByteDance/Seedance-1.0-lite` | 5s           | 864×480, 736×544, 640×640, 960×416, 416×960, 1248×704, 1120×832, 960×960, 1504×640, 640×1504        | 24      | First, Last   | 2-3000 char |
| **ByteDance**    | Seedance 1.0 Pro     | `ByteDance/Seedance-1.0-pro`  | 5s           | 864×480, 736×544, 640×640, 960×416, 416×960, 1248×704, 1120×832, 960×960, 1504×640, 640×1504        | 24      | First, Last   | 2-3000 char |
| **PixVerse**     | PixVerse v5          | `pixverse/pixverse-v5`        | 5s           | 640×360, 480×360, 360×360, 270×360, 360×640, 960×540, 720×540, 540×540, 405×540, 540×960, 1280×720, |         |               |             |
|                  |                      |                               |              | 960×720, 720×720, 540×720, 720×1280, 1920×1080, 1440×1080, 1080×1080, 810×1080, 1080×1920           | 16, 24  | First, Last   | 2-2048 char |
| **Kuaishou**     | Kling 2.1 Master     | `kwaivgI/kling-2.1-master`    | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First         | 2-2500 char |
| **Kuaishou**     | Kling 2.1 Standard   | `kwaivgI/kling-2.1-standard`  | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First         | ❌           |
| **Kuaishou**     | Kling 2.1 Pro        | `kwaivgI/kling-2.1-pro`       | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First, Last   | ❌           |
| **Kuaishou**     | Kling 2.0 Master     | `kwaivgI/kling-2.0-master`    | 5s           | 1280×720, 720×720, 720×1280                                                                         | 24      | First         | 2-2500 char |
| **Kuaishou**     | Kling 1.6 Standard   | `kwaivgI/kling-1.6-standard`  | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 30, 24  | First         | 2-2500 char |
| **Kuaishou**     | Kling 1.6 Pro        | `kwaivgI/kling-1.6-pro`       | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First         | ❌           |
| **Wan-AI**       | Wan 2.2 I2V          | `Wan-AI/Wan2.2-I2V-A14B`      | -            | -                                                                                                   | -       | -             | -           |
| **Wan-AI**       | Wan 2.2 T2V          | `Wan-AI/Wan2.2-T2V-A14B`      | -            | -                                                                                                   | -       | -             | -           |
| **Vidu**         | Vidu 2.0             | `vidu/vidu-2.0`               | 8s           | 1920×1080, 1080×1080, 1080×1920, 1280×720, 720×720, 720×1280, 640×360, 360×360, 360×640             | 24      | First, Last   | 2-3000 char |
| **Vidu**         | Vidu Q1              | `vidu/vidu-q1`                | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First, Last   | 2-3000 char |
| **OpenAI**       | Sora 2               | `openai/sora-2`               | 8s           | 1280×720, 720×1280                                                                                  | -       | First         | 1-4000 char |
| **OpenAI**       | Sora 2 Pro           | `openai/sora-2-pro`           | 8s           | 1280×720, 720×1280                                                                                  | -       | First         | 1-4000 char |

## Troubleshooting

**Video doesn't match prompt well:**

* Increase `guidance_scale` to 8-10
* Make prompt more descriptive and specific
* Add `negative_prompt` to exclude unwanted elements

**Video has artifacts:**

* Reduce `guidance_scale` (keep below 12)
* Increase `steps` to 30-40
* Adjust `fps` if motion looks unnatural

**Generation is too slow:**

* Reduce `steps` (try 10-20 for testing)
* Use shorter `seconds` during development
* Lower `fps` for slower-paced scenes

**URLs expire:**

* Download videos immediately after completion
* Don't rely on URLs for long-term storage


# Vision
Source: https://docs.together.ai/docs/vision-overview

Learn how to use the vision models supported by Together AI.

We support language vision models from multiple providers:

* [Llama 4 Scout Instruct](https://api.together.ai/playground/meta-llama/Llama-4-Scout-17B-16E-Instruct)
* [Llama 4 Maverick Instruct](https://api.together.ai/playground/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8)
* [Qwen2.5-VL (72B) Instruct](https://api.together.ai/playground/Qwen/Qwen2.5-VL-72B-Instruct)

Here's how to get started with the Together API in a few lines of code.

## Quickstart

### 1. Register for an account

First, [register for an account](https://api.together.xyz/settings/api-keys) to get an API key.

Once you've registered, set your account's API key to an environment variable named `TOGETHER_API_KEY`:

```bash  theme={null}
export TOGETHER_API_KEY=xxxxx
```

### 2. Install your preferred library

Together provides an official library for Python:

```bash  theme={null}
pip install together
```

As well as an official library for TypeScript/JavaScript:

```bash  theme={null}
npm install together-ai
```

You can also call our HTTP API directly using any language you like.

### 3. Query the models via our API

In this example, we're giving it a picture of a trello board and asking the model to describe it to us.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  getDescriptionPrompt = "You are a UX/UI designer. Describe the attached screenshot or UI mockup in detail. I will feed in the output you give me to a coding model that will attempt to recreate this mockup, so please think step by step and describe the UI in detail. Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. Match the colors and sizes exactly. Make sure to mention every part of the screenshot including any headers, footers, etc. Use the exact text from the screenshot."

  imageUrl = "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png"

  stream = client.chat.completions.create(
      model="meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": getDescriptionPrompt},
                  {"type": "image_url", "image_url": {"url": imageUrl}},
              ],
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(
          chunk.choices[0].delta.content or "" if chunk.choices else "",
          end="",
          flush=True,
      )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  let getDescriptionPrompt = `You are a UX/UI designer. Describe the attached screenshot or UI mockup in detail. I will feed in the output you give me to a coding model that will attempt to recreate this mockup, so please think step by step and describe the UI in detail.

  - Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. Match the colors and sizes exactly.
  - Make sure to mention every part of the screenshot including any headers, footers, etc.
  - Use the exact text from the screenshot.
  `;
  let imageUrl =
    "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png";

  async function main() {
    const stream = await together.chat.completions.create({
      model: "meta-llama/Llama-4-Scout-17B-16E-Instruct",
      temperature: 0.2,
      stream: true,
      max_tokens: 500,
      messages: [
        {
          role: "user",
          // @ts-expect-error Need to fix the TypeScript library type
          content: [
            { type: "text", text: getDescriptionPrompt },
            {
              type: "image_url",
              image_url: {
                url: imageUrl,
              },
            },
          ],
        },
      ],
    });

    for await (const chunk of stream) {
      process.stdout.write(chunk.choices[0]?.delta?.content || "");
    }
  }

  main();
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct",
         "messages": [
           {
             "role": "user",
             "content": [
               {
                 "type": "text",
                 "text": "You are a UX/UI designer. Describe the attached screenshot or UI mockup in detail. I will feed in the output you give me to a coding model that will attempt to recreate this mockup, so please think step by step and describe the UI in detail. Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. Match the colors and sizes exactly. Make sure to mention every part of the screenshot including any headers, footers, etc. Use the exact text from the screenshot."
               },
               {
                 "type": "image_url",
                 "image_url": {
                   "url": "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png"
                 }
               }
             ]
           }
         ]
       }'
  ```
</CodeGroup>

#### Output

```
The attached screenshot appears to be a Trello board, a project management tool used for organizing tasks and projects into boards. Below is a detailed breakdown of the UI:

**Header**
-----------------

* A blue bar spanning the top of the page
* White text reading "Trello" in the top-left corner
* White text reading "Workspaces", "Recent", "Starred", "Templates", and "Create" in the top-right corner, separated by small white dots
* A white box with a blue triangle and the word "Board" inside it

**Top Navigation Bar**
----------------------

* A blue bar with white text reading "Project A"
* A dropdown menu with options "Workspace visible" and "Board"
* A search bar with a magnifying glass icon

**Main Content**
-----------------

* Three columns of cards with various tasks and projects
* Each column has a header with a title
* Cards are white with gray text and a blue border
* Each card has a checkbox, a title, and a description
* Some cards have additional details such as a yellow or green status indicator, a due date, and comments

**Footer**
------------

* A blue bar with white text reading "Add a card"
* A button to add a new card to the board

**Color Scheme**
-----------------

* Blue and white are the primary colors used in the UI
* Yellow and green are used as status indicators
* Gray is used for text and borders

**Font Family**
----------------

* The font family used throughout the UI is clean and modern, with a sans-serif font

**Iconography**
----------------

* The UI features several icons, including:
        + A magnifying glass icon for the search bar
        + A triangle icon for the "Board" dropdown menu
        + A checkbox icon for each card
        + A status indicator icon (yellow or green)
        + A comment icon (a speech bubble)

**Layout**
------------

* The UI is divided into three columns: "To Do", "In Progress", and "Done"
* Each column has a header with a title
* Cards are arranged in a vertical list within each column
* The cards are spaced evenly apart, with a small gap between each card

**Overall Design**
-------------------

* The UI is clean and modern, with a focus on simplicity and ease of use
* The use of blue and white creates a sense of calmness and professionalism
* The icons and graphics are simple and intuitive, making it easy to navigate the UI

This detailed breakdown provides a comprehensive understanding of the UI mockup, including its layout, color scheme, and components.
```

### Query models with a local image

If you want to query models with a local image, here is an example:

<CodeGroup>
  ```python Python theme={null}
  from together import Together
  import base64

  client = Together()

  getDescriptionPrompt = "what is in the image"

  imagePath = "/home/Desktop/dog.jpeg"


  def encode_image(image_path):
      with open(image_path, "rb") as image_file:
          return base64.b64encode(image_file.read()).decode("utf-8")


  base64_image = encode_image(imagePath)

  stream = client.chat.completions.create(
      model="meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": getDescriptionPrompt},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": f"data:image/jpeg;base64,{base64_image}"
                      },
                  },
              ],
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(
          chunk.choices[0].delta.content or "" if chunk.choices else "",
          end="",
          flush=True,
      )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import fs from "fs/promises";

  const together = new Together();

  const getDescriptionPrompt = "what is in the image";

  const imagePath = "./dog.jpeg";

  async function main() {
    const imageUrl = await fs.readFile(imagePath, { encoding: "base64" });

    const stream = await together.chat.completions.create({
      model: "meta-llama/Llama-4-Scout-17B-16E-Instruct",
      stream: true,
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: getDescriptionPrompt },
            {
              type: "image_url",
              image_url: {
                url: `data:image/jpeg;base64,${imageUrl}`,
              },
            },
          ],
        },
      ],
    });

    for await (const chunk of stream) {
      process.stdout.write(chunk.choices[0]?.delta?.content || "");
    }
  }

  main();
  ```

  ```curl cURL theme={null}
  # Note: Replace BASE64_IMAGE with your base64-encoded image data
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct",
         "messages": [
           {
             "role": "user",
             "content": [
               {
                 "type": "text",
                 "text": "what is in the image"
               },
               {
                 "type": "image_url",
                 "image_url": {
                   "url": "data:image/jpeg;base64,BASE64_IMAGE"
                 }
               }
             ]
           }
         ]
       }'
  ```
</CodeGroup>

#### Output

```
The Image contains two dogs sitting close to each other
```

### Query models with video input

<CodeGroup>
  ```python Python theme={null}
  # Multi-modal message with text and video

  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What's happening in this video?"},
                  {
                      "type": "video_url",
                      "video_url": {
                          "url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"
                      },
                  },
              ],
          }
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  // Multi-modal message with text and video

  async function main() {
    const response = await together.chat.completions.create({
      model: "meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "What's happening in this video?" },
            {
              type: "video_url",
              video_url: {
                url: "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4",
              },
            },
          ],
        },
      ],
    });
    
    process.stdout.write(response.choices[0]?.message?.content || "");
  }

  main();
  ```
</CodeGroup>

#### Output

```
The video appears to be a promotional advertisement for Google Chromecast. It showcases various scenes of people using the device in different settings, such as classrooms and offices. The video highlights the versatility and ease of use of Chromecast by demonstrating how it can be used to cast content from laptops and other devices onto larger screens like TVs or monitors. The final frame displays the Chromecast logo and website URL, indicating the product being advertised.
```

### Query models with multiple images

<CodeGroup>
  ```python python theme={null}
  # Multi-modal message with multiple images
  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Compare these two images."},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
                      },
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/slack.png"
                      },
                  },
              ],
          }
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  // Multi-modal message with multiple images

  async function main() {
    const response = await together.chat.completions.create({
      model: "meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Compare these two images." },
            {
              type: "image_url",
              image_url: {
                url: "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png",
              },
            },
            {
              type: "image_url",
              image_url: {
                url: "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/slack.png",
              },
            },
          ],
        },
      ],
    });
    
    process.stdout.write(response.choices[0]?.message?.content || "");
  }

  main();
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct",
         "messages": [
           {
             "role": "user",
             "content": [
               {
                 "type": "text",
                 "text": "Compare these two images."
               },
               {
                 "type": "image_url",
                 "image_url": {
                   "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
                 }
               },
               {
                 "type": "image_url",
                 "image_url": {
                   "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/slack.png"
                 }
               }
             ]
           }
         ]
       }'
  ```
</CodeGroup>

#### Output

```
The first image is a collage of multiple identical landscape photos showing a natural scene with rocks, trees, and a stream under a blue sky. The second image is a screenshot of a mobile app interface, specifically the navigation menu of the Canva app, which includes icons for Home, DMs (Direct Messages), Activity, Later, Canvases, and More.

#### Comparison:
1. **Content**:
   - The first image focuses on a natural landscape.
   - The second image shows a digital interface from an app.

2. **Purpose**:
   - The first image could be used for showcasing nature, design elements in graphic work, or as a background.
   - The second image represents the functionality and layout of the Canva app's navigation system.

3. **Visual Style**:
   - The first image has vibrant colors and realistic textures typical of outdoor photography.
   - The second image uses flat design icons with a simple color palette suited for user interface design.

4. **Context**:
   - The first image is likely intended for artistic or environmental contexts.
   - The second image is relevant to digital design and app usability discussions.
```

### Pricing

For vision models images are converted to 1,601 to 6,404 tokens depending on image size. We currently used this formula to calculate the number of tokens in an image:

```
T = min(2, max(H // 560, 1)) * min(2, max(W // 560, 1)) * 1601
```

*(T= tokens, H=height, W=width)*


# Agent Workflows
Source: https://docs.together.ai/docs/workflows

Orchestrating together multiple language model calls to solve complex tasks.

In order to solve complex tasks a single LLM call might not be enough, here we'll see how you can solve complex problems by orchestrating multiple language models.

The execution pattern of actions within an agent workflow is determined by its control flow. Various control flow types enable different capabilities:

## Sequential

Tasks execute one after another when later steps depend on earlier ones. For example, a SQL query can only run after being translated from natural language.

Learn more about [Sequential Workflows](/docs/sequential-agent-workflow)

## Parallel

Multiple tasks execute simultaneously. For instance, retrieving prices for multiple products at once rather than sequentially.

Learn more about [Parallel Workflows](/docs/parallel-workflows)

## Conditional (If statement)

The workflow branches based on evaluation results. An agent might analyze a company's earnings report before deciding to buy or sell its stock.

Learn more about [Conditional Workflows](/docs/conditional-workflows)

## Iterative (For loop)

A task repeats until a condition is met. For example, generating random numbers until finding a prime number.

Learn more about [Iterative Workflows](/docs/iterative-workflow)

When evaluating which workflow to use for a task consider tradeoffs between task complexity, latency and cost. Workflows with parallel execution capabilities can dramatically reduce perceived latency, especially for tasks involving multiple independent operations like scraping several websites. Iterative workflows are great for optimizing for a given task until a termination condition is met but can be costly.



---

**Navigation:** [← Previous](./07-parallel-workflow.md) | [Index](./index.md) | [Next →](./09-together-cookbooks-example-apps.md)
