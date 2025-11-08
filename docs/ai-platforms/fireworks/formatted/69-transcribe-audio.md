---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Transcribe audio

Source: https://docs.fireworks.ai/api-reference/audio-transcriptions

post /audio/transcriptions

<CardGroup cols={1}>
  <Card title="Try notebook" icon="rocket" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/audio/audio_prerecorded_speech_to_text/audio_prerecorded_speech_to_text.ipynb">
    Send a sample audio to get a transcription.
  </Card>
</CardGroup>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Fireworks API key, e.g. `Authorization=API_KEY`.
</ParamField>

### Request

##### (multi-part form)

<ParamField query="file" type="file | string" required>
  The input audio file to transcribe or an URL to the public audio file.

  Max audio file size is 1 GB, there is no limit for audio duration. Common file formats such as mp3, flac, and wav are supported. Note that the audio will be resampled to 16kHz, downmixed to mono, and reformatted to 16-bit signed little-endian format before transcription. Pre-converting the file before sending it to the API can improve runtime performance.
</ParamField>

<ParamField query="model" type="string" default="whisper-v3" optional>
  String name of the ASR model to use. Can be one of `whisper-v3` or `whisper-v3-turbo`. Please use the following serverless endpoints:

  * [https://audio-prod.api.fireworks.ai](https://audio-prod.api.fireworks.ai) (for `whisper-v3`);
  * [https://audio-turbo.api.fireworks.ai](https://audio-turbo.api.fireworks.ai) (for `whisper-v3-turbo`);
</ParamField>

<ParamField query="vad_model" type="string" default="silero" optional>
  String name of the voice activity detection (VAD) model to use. Can be one of `silero`, or `whisperx-pyannet`.
</ParamField>

<ParamField query="alignment_model" type="string" default="mms_fa" optional>
  String name of the alignment model to use. Currently supported:

  * `mms_fa` optimal accuracy for multilingual speech.
  * `tdnn_ffn` optimal accuracy for English-only speech.
  * `gentle` best accuracy for English-only speech (requires a dedicated endpoint, contact us at <a href="mailto:inquiries@fireworks.ai">[inquiries@fireworks.ai](mailto:inquiries@fireworks.ai)</a>).
</ParamField>

<ParamField query="language" type="string | null" optional>
  The target language for transcription. See the [Supported Languages](#supported-languages) section below for a complete list of available languages.
</ParamField>

<ParamField query="prompt" type="string | null" optional>
  The input prompt that the model will use when generating the transcription. Can be used to specify custom words or specify the style of the transcription. E.g. `Um, here's, uh, what was recorded.` will make the model to include the filler words into the transcription.
</ParamField>

<ParamField query="temperature" type="float | list[float]" default="0">
  Sampling temperature to use when decoding text tokens during transcription. Alternatively, fallback decoding can be enabled by passing a list of temperatures like `0.0,0.2,0.4,0.6,0.8,1.0`. This can help to improve performance.
</ParamField>

<ParamField query="response_format" type="string" default="json">
  The format in which to return the response. Can be one of `json`, `text`, `srt`, `verbose_json`, or `vtt`.
</ParamField>

<ParamField query="timestamp_granularities" type="string | list[string]" optional>
  The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported. Can be one of `word`, `segment`, or `word,segment`. If not present, defaults to `segment`.
</ParamField>

<ParamField query="diarize" type="string" optional>
  Whether to get speaker diarization for the transcription. Can be one of `true`, or `false`. If not present, defaults to `false`.

  Enabling diarization also requires other fields to hold specific values:

  1. `response_format` must be set `verbose_json`.
  2. `timestamp_granularities` must include `word` to use diarization.
</ParamField>

<ParamField query="min_speakers" type="int" optional>
  The minimum number of speakers to detect for diarization. `diarize` must be set `true` to use `min_speakers`. If not present, defaults to `1`.
</ParamField>

<ParamField query="max_speakers" type="int" optional>
  The maximum number of speakers to detect for diarization. `diarize` must be set `true` to use `max_speakers`. If not present, defaults to `inf`.
</ParamField>

<ParamField query="preprocessing" type="string" optional>
  Audio preprocessing mode. Currently supported:

  * `none` to skip audio preprocessing.
  * `dynamic` for arbitrary audio content with variable loudness.
  * `soft_dynamic` for speech intense recording such as podcasts and voice-overs.
  * `bass_dynamic` for boosting lower frequencies;
</ParamField>

### Response

<Tabs>
  <Tab title="json/text/srt/vtt">
    <ResponseField name="text" type="string" required />
  </Tab>

  <Tab title="verbose_json">
    <ResponseField name="task" type="string" default="transcribe" required>
      The task which was performed. Either `transcribe` or `translate`.
    </ResponseField>

    <ResponseField name="language" type="string" required>
      The language of the transcribed/translated text.
    </ResponseField>

    <ResponseField name="duration" type="number" required>
      The duration of the transcribed/translated audio, in seconds.
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

        <ResponseField name="start" type="number" required>
          Start time of the word in seconds.
        </ResponseField>

        <ResponseField name="end" type="number" required>
          End time of the word in seconds.
        </ResponseField>

        <ResponseField name="speaker_id" type="string" optional>
          Speaker label for the word.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="segments" type="object[] | null" optional>
      Segments of the transcribed/translated text and their corresponding details.

      <Expandable title="Segment properties (partial)">
        <ResponseField name="id" type="number" required>
          The id of the segment.
        </ResponseField>

        <ResponseField name="text" type="string" required>
          The text content of the segment.
        </ResponseField>

        <ResponseField name="start" type="number" required>
          Start time of the segment in seconds.
        </ResponseField>

        <ResponseField name="end" type="number" required>
          End time of the segment in seconds.
        </ResponseField>

        <ResponseField name="speaker_id" type="string" optional>
          Speaker label for the segment.
        </ResponseField>

        <ResponseField name="words" type="object[] | null" optional>
          Extracted words in the segment.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Tab>
</Tabs>

<RequestExample>
```bash
  # Download audio file

  curl -L -o "audio.flac" "https://tinyurl.com/4997djsh"

  # Make request

  curl -X POST "https://audio-prod.api.fireworks.ai/v1/audio/transcriptions" \
  -H "Authorization: <FIREWORKS_API_KEY>" \
  -F "file=@audio.flac"
```
```python fireworks sdk theme={null}
  !pip install fireworks-ai requests python-dotenv

  from fireworks.client.audio import AudioInference
  import requests
  import os
  from dotenv import load_dotenv
  import time

  # Create a .env file with your API key

  load_dotenv()


  # Download audio sample

  audio = requests.get("https://tinyurl.com/4cb74vas").content

  # Prepare client

  client = AudioInference(
      model="whisper-v3",
      base_url="https://audio-prod.api.fireworks.ai",
      # Or for the turbo version

      # model="whisper-v3-turbo",

      # base_url="https://audio-turbo.api.fireworks.ai",

      api_key=os.getenv("FIREWORKS_API_KEY"),
  )

  # Make request

  start = time.time()
  r = await client.transcribe_async(audio=audio)
  print(f"Took: {(time.time() - start):.3f}s. Text: '{r.text}'")
```
```python Python (openai sdk) theme={null}
  !pip install openai requests python-dotenv

  from openai import OpenAI
  import os
  import requests
  from dotenv import load_dotenv

  load_dotenv()

  client = OpenAI(
      base_url="https://audio-prod.api.fireworks.ai/v1",
      api_key=os.getenv("FIREWORKS_API_KEY")
      )
  audio_file= requests.get("https://tinyurl.com/4cb74vas").content
  transcription = client.audio.transcriptions.create(
      model="whisper-v3",
      file=audio_file
  )
  print(transcription.text)
```
</RequestExample>

### Supported Languages

The following languages are supported for transcription:

<Accordion title="Language Code & Name">
  | Language Code | Language Name       |
  | ------------- | ------------------- |
  | en            | English             |
  | zh            | Chinese             |
  | de            | German              |
  | es            | Spanish             |
  | ru            | Russian             |
  | ko            | Korean              |
  | fr            | French              |
  | ja            | Japanese            |
  | pt            | Portuguese          |
  | tr            | Turkish             |
  | pl            | Polish              |
  | ca            | Catalan             |
  | nl            | Dutch               |
  | ar            | Arabic              |
  | sv            | Swedish             |
  | it            | Italian             |
  | id            | Indonesian          |
  | hi            | Hindi               |
  | fi            | Finnish             |
  | vi            | Vietnamese          |
  | he            | Hebrew              |
  | uk            | Ukrainian           |
  | el            | Greek               |
  | ms            | Malay               |
  | cs            | Czech               |
  | ro            | Romanian            |
  | da            | Danish              |
  | hu            | Hungarian           |
  | ta            | Tamil               |
  | no            | Norwegian           |
  | th            | Thai                |
  | ur            | Urdu                |
  | hr            | Croatian            |
  | bg            | Bulgarian           |
  | lt            | Lithuanian          |
  | la            | Latin               |
  | mi            | Maori               |
  | ml            | Malayalam           |
  | cy            | Welsh               |
  | sk            | Slovak              |
  | te            | Telugu              |
  | fa            | Persian             |
  | lv            | Latvian             |
  | bn            | Bengali             |
  | sr            | Serbian             |
  | az            | Azerbaijani         |
  | sl            | Slovenian           |
  | kn            | Kannada             |
  | et            | Estonian            |
  | mk            | Macedonian          |
  | br            | Breton              |
  | eu            | Basque              |
  | is            | Icelandic           |
  | hy            | Armenian            |
  | ne            | Nepali              |
  | mn            | Mongolian           |
  | bs            | Bosnian             |
  | kk            | Kazakh              |
  | sq            | Albanian            |
  | sw            | Swahili             |
  | gl            | Galician            |
  | mr            | Marathi             |
  | pa            | Punjabi             |
  | si            | Sinhala             |
  | km            | Khmer               |
  | sn            | Shona               |
  | yo            | Yoruba              |
  | so            | Somali              |
  | af            | Afrikaans           |
  | oc            | Occitan             |
  | ka            | Georgian            |
  | be            | Belarusian          |
  | tg            | Tajik               |
  | sd            | Sindhi              |
  | gu            | Gujarati            |
  | am            | Amharic             |
  | yi            | Yiddish             |
  | lo            | Lao                 |
  | uz            | Uzbek               |
  | fo            | Faroese             |
  | ht            | Haitian Creole      |
  | ps            | Pashto              |
  | tk            | Turkmen             |
  | nn            | Nynorsk             |
  | mt            | Maltese             |
  | sa            | Sanskrit            |
  | lb            | Luxembourgish       |
  | my            | Myanmar             |
  | bo            | Tibetan             |
  | tl            | Tagalog             |
  | mg            | Malagasy            |
  | as            | Assamese            |
  | tt            | Tatar               |
  | haw           | Hawaiian            |
  | ln            | Lingala             |
  | ha            | Hausa               |
  | ba            | Bashkir             |
  | jw            | Javanese            |
  | su            | Sundanese           |
  | yue           | Cantonese           |
  | zh-hant       | Traditional Chinese |
  | zh-hans       | Simplified Chinese  |
</Accordion>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
