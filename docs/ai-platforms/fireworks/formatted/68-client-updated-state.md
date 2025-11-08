---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Client updated state:

{
    "0": "This is the first sentence",
    "1": "This is the second sentence modified",   # overwritten

    "2": "This is the third sentence",             # new

}
```

### Handling Connection Interruptions & Timeouts

Real-time streaming transcription over WebSockets can run for a long time. The longer a WebSocket session runs, the more likely it is to experience interruptions from network glitches to service hiccups.
It is important to be aware of this and build your client to recover gracefully so the stream keeps going without user impact.

In the following section, we’ll outline recommended practices for handling connection interruptions and timeouts effectively.

#### When a connection drops

Although Fireworks is designed to keep streams running smoothly, occasional interruptions can still occur. If the WebSocket is disrupted (e.g., bandwidth limitation or network failures),
your application must initialize a new WebSocket connection, start a fresh streaming session and begin sending audio as soon as the server confirms the connection is open.

#### Avoid losing audio during reconnects

While you’re reconnecting, audio could be still being produced and you could lose that audio segment if it is not transferred to our API during this period.
To minimize the risk of dropping audio during a reconnect, one effective approach is to store the audio data in a buffer until it can re-establish the connection to our API and then sends the data for transcription.

### Keep timestamps continuous across sessions

When timestamps are enabled, the result will include the start and end time of the segment in seconds. And each new WebSocket session will reset the timestamps to start from 00:00:00.

To keep a continuous timeline, we recommend to maintain a running “stream start offset” in your app and add that offset to timestamps from each new session so they align with the overall audio timeline.

### Example Usage

Check out a brief Python example below or example sources:

* [Python notebook](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/audio/audio_streaming_speech_to_text/audio_streaming_speech_to_text.ipynb)
* [Python sources](https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text/python)
* [Node.js sources](https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text/nodejs)
```python
  !pip3 install requests torch torchaudio websocket-client

  import io
  import time
  import json
  import torch
  import requests
  import torchaudio
  import threading
  import websocket
  import urllib.parse

  lock = threading.Lock()
  state = {}

  def on_open(ws):
      def send_audio_chunks():
          for chunk in audio_chunk_bytes:
              ws.send(chunk, opcode=websocket.ABNF.OPCODE_BINARY)
              time.sleep(chunk_size_ms / 1000)

          final_checkpoint = json.dumps({"checkpoint_id": "final"})
          ws.send(final_checkpoint, opcode=websocket.ABNF.OPCODE_TEXT)

      threading.Thread(target=send_audio_chunks).start()

  def on_message(ws, message):
      message = json.loads(message)
      if message.get("checkpoint_id") == "final":
          ws.close()
          return

      update = {s["id"]: s["text"] for s in message["segments"]}
      with lock:
          state.update(update)
          print("\n".join(f" - {k}: {v}" for k, v in state.items()))

  def on_error(ws, error):
      print(f"WebSocket error: {error}")

  # Open a connection URL with query params

  url = "wss://audio-streaming.api.fireworks.ai/v1/audio/transcriptions/streaming"
  params = urllib.parse.urlencode({
      "language": "en",
  })
  ws = websocket.WebSocketApp(
      f"{url}?{params}",
      header={"Authorization": "<FIREWORKS_API_KEY>"},
      on_open=on_open,
      on_message=on_message,
      on_error=on_error,
  )
  ws.run_forever()
```

### Dedicated endpoint

For fixed throughput and predictable SLAs, you may request a dedicated endpoint for streaming transcription at [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) or [discord](https://www.google.com/url?q=https%3A%2F%2Fdiscord.gg%2Ffireworks-ai).

### Supported Languages

The following languages are supported for transcription:

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


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
