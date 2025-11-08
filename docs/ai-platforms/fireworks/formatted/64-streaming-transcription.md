---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming Transcription

Source: https://docs.fireworks.ai/api-reference/audio-streaming-transcriptions

websocket /audio/transcriptions/streaming

<Steps>
  <Step title="Open a WebSocket">
    Streaming transcription is performed over a WebSocket. Provide the transcription parameters and establish a WebSocket connection to the endpoint.
  </Step>

  <Step title="Stream audio and receive transcriptions">
    Stream short audio chunks (50-400ms) in binary frames of PCM 16-bit little-endian at 16kHz sample rate and single channel (mono). In parallel, receive transcription from the WebSocket.
  </Step>
</Steps>

<CardGroup cols={2}>
  <Card title="Try Python notebook" icon="notebook" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/audio/audio_streaming_speech_to_text/audio_streaming_speech_to_text.ipynb">
    Stream audio to get transcription continuously in real-time.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="Explore Python sources" icon="code" href="https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text/python">
    Stream audio to get transcription continuously in real-time.
  </Card>

  <Card title="Explore Node.js sources" icon="code" href="https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text/nodejs">
    Stream audio to get transcription continuously in real-time.
  </Card>
</CardGroup>

### URLs

Fireworks provides serverless, real-time ASR via WebSocket endpoints. Please select the appropriate version:

#### Streaming ASR v1 (default)

Production-ready and generally recommended for all use cases.
```
wss://audio-streaming.api.fireworks.ai/v1/audio/transcriptions/streaming
```

#### Streaming ASR v2 (preview)

An early-access version of our next-generation streaming transcription service. V2 is good for use cases that require lower latency and higher accuracy in noisy situations.
```
wss://audio-streaming-v2.api.fireworks.ai/v1/audio/transcriptions/streaming
```

### Headers

<ParamField header="Authorization" type="string" required>
  Your Fireworks API key, e.g. `Authorization=API_KEY`. Alternatively, can be provided as a query param.
</ParamField>

### Query Parameters

<ParamField query="Authorization" type="string" optional>
  Your Fireworks API key. Required when headers cannot be set (e.g., browser WebSocket connections). Can alternatively be provided via the Authorization header.
</ParamField>

<ParamField query="response_format" type="string" default="verbose_json" optional>
  The format in which to return the response. Currently only `verbose_json` is recommended for streaming.
</ParamField>

<ParamField query="language" type="string | null" optional>
  The target language for transcription. See the [Supported Languages](#supported-languages) section below for a complete list of available languages.
</ParamField>

<ParamField query="prompt" type="string | null" optional>
  The input prompt that the model will use when generating the transcription. Can be used to specify custom words or specify the style of the transcription. E.g. `Um, here's, uh, what was recorded.` will make the model to include the filler words into the transcription.
</ParamField>

<ParamField query="temperature" type="float" default="0">
  Sampling temperature to use when decoding text tokens during transcription.
</ParamField>

<ParamField query="timestamp_granularities" type="string | list[string] | null" optional>
  The timestamp granularities to populate for this streaming transcription. Defaults to null. Set to `word,segment` to enable timestamp granularities. Use a list for timestamp\_granularities in all client libraries. A comma-separated string like `word,segment` only works when manually included in the URL (e.g. in curl).
</ParamField>

### Client messages

<Tabs>
  <Tab title="binary">
    This field is for client to send audio chunks over to server. Stream short audio chunks (50-400ms) in binary frames of PCM 16-bit little-endian at 16kHz sample rate and single channel (mono).
  </Tab>

  <Tab title="SttStateClear">
    This field is for client event initiating the context clean up.

    <ResponseField name="event_id" type="string">
      A unique identifier for the event.
    </ResponseField>

    <ResponseField name="object" type="string" fixed="stt.state.clear">
      A constant string that identifies the type of event as "stt.state.clear".
    </ResponseField>

    <ResponseField name="reset_id" type="string">
      The ID of the context or session to be cleared.
    </ResponseField>
  </Tab>

  <Tab title="SttInputTrace">
    This field is for client event initiating tracing.

    <ResponseField name="event_id" type="string">
      A unique identifier for the event.
    </ResponseField>

    <ResponseField name="object" type="string" fixed="stt.input.trace">
      A constant string indicating the event type is "stt.input.trace".
    </ResponseField>

    <ResponseField name="trace_id" type="string">
      The ID used to correlate this trace event across systems.
    </ResponseField>
  </Tab>
</Tabs>

### Server messages

<Tabs>
  <Tab title="json">
    <ResponseField name="task" type="string" default="transcribe" required>
      The task that was performed — either `transcribe` or `translate`.
    </ResponseField>

    <ResponseField name="language" type="string" required>
      The language of the transcribed/translated text.
    </ResponseField>

    <ResponseField name="text" type="string" required>
      The transcribed/translated text.
    </ResponseField>

    <ResponseField name="words" type="object[] | null" optional>
      Extracted words and their corresponding timestamps.

      <Expandable title="Word properties">
        <ResponseField name="word" type="string" required>
          The text content of the word.
        </ResponseField>

        <ResponseField name="language" type="string" required>
          The language of the word.
        </ResponseField>

        <ResponseField name="probability" type="number" required>
          The probability of the word.
        </ResponseField>

        <ResponseField name="hallucination_score" type="number" required>
          The hallucination score of the word.
        </ResponseField>

        <ResponseField name="start" type="number" optional>
          Start time of the word in seconds. Appears only when timestamp\_granularities is set to `word,segment`.
        </ResponseField>

        <ResponseField name="end" type="number" optional>
          End time of the word in seconds. Appears only when timestamp\_granularities is set to `word,segment`.
        </ResponseField>

        <ResponseField name="is_final" type="bool" required>
          Indicates whether this word has been finalized.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="segments" type="object[] | null" optional>
      Segments of the transcribed/translated text and their corresponding details.

      <Expandable title="Segment properties (partial)">
        <ResponseField name="id" type="number" required>
          The ID of the segment.
        </ResponseField>

        <ResponseField name="text" type="string" required>
          The text content of the segment.
        </ResponseField>

        <ResponseField name="words" type="object[] | null" optional>
          Extracted words in the segment.
        </ResponseField>

        <ResponseField name="start" type="number" optional>
          Start time of the segment in seconds. Appears only when timestamp\_granularities is set to `word,segment`.
        </ResponseField>

        <ResponseField name="end" type="number" optional>
          End time of the segment in seconds. Appears only when timestamp\_granularities is set to `word,segment`.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Tab>

  <Tab title="SttStateCleared">
    This field is for server to communicate it successfully cleared the context.

    <ResponseField name="event_id" type="string">
      A unique identifier for the event.
    </ResponseField>

    <ResponseField name="object" type="string" fixed="stt.state.cleared">
      A constant string indicating the event type is "stt.state.cleared"
    </ResponseField>

    <ResponseField name="reset_id" type="string">
      The ID of the context or session that has been successfully cleared.
    </ResponseField>
  </Tab>

  <Tab title="SttOutputTrace">
    This field is for server to complete tracing.

    <ResponseField name="event_id" type="string">
      A unique identifier for the event.
    </ResponseField>

    <ResponseField name="object" type="string" fixed="stt.output.trace">
      A constant string indicating the event type is "stt.output.trace".
    </ResponseField>

    <ResponseField name="trace_id" type="string">
      The ID used to correlate this output trace with the corresponding input trace.
    </ResponseField>
  </Tab>
</Tabs>

### Streaming Audio

Stream short audio chunks (50-400ms) in binary frames of PCM 16-bit little-endian at 16kHz sample rate and single channel (mono).  Typically, you will:

1. Resample your audio to 16 kHz if it is not already.
2. Convert it to mono.
3. Send 50ms chunks (16,000 Hz \* 0.05s = 800 samples) of audio in 16-bit PCM (signed, little-endian) format.

### Handling Responses

The client maintains a state dictionary, starting with an empty dictionary `{}`. When the server sends the first transcription message, it contains a list of segments. Each segment has an `id` and `text`:
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
