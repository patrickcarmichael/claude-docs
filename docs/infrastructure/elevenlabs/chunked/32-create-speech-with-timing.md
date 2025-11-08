**Navigation:** [← Previous](./31-get-configuration-override.md) | [Index](./index.md) | [Next →](./33-create-dialogue.md)

# Create speech with timing

POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/with-timestamps
Content-Type: application/json

Generate speech from text with precise character-level timing information for audio-text synchronization.

Reference: https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create speech with timing
  version: endpoint_textToSpeech.convert_with_timestamps
paths:
  /v1/text-to-speech/{voice_id}/with-timestamps:
    post:
      operationId: convert-with-timestamps
      summary: Create speech with timing
      description: >-
        Generate speech from text with precise character-level timing
        information for audio-text synchronization.
      tags:
        - - subpackage_textToSpeech
      parameters:
        - name: voice_id
          in: path
          description: >-
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices
            to list all the available voices.
          required: true
          schema:
            type: string
        - name: enable_logging
          in: query
          description: >-
            When enable_logging is set to false zero retention mode will be used
            for the request. This will mean history features are unavailable for
            this request, including request stitching. Zero retention mode may
            only be used by enterprise customers.
          required: false
          schema:
            type: boolean
        - name: optimize_streaming_latency
          in: query
          description: >
            You can turn on latency optimizations at some cost of quality. The
            best possible final latency varies by model. Possible values:

            0 - default mode (no latency optimizations)

            1 - normal latency optimizations (about 50% of possible latency
            improvement of option 3)

            2 - strong latency optimizations (about 75% of possible latency
            improvement of option 3)

            3 - max latency optimizations

            4 - max latency optimizations, but also with text normalizer turned
            off for even more latency savings (best latency, but can
            mispronounce eg numbers and dates).


            Defaults to None.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: output_format
          in: query
          description: >-
            Output format of the generated audio. Formatted as
            codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at
            32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate
            requires you to be subscribed to Creator tier or above. PCM with
            44.1kHz sample rate requires you to be subscribed to Pro tier or
            above. Note that the μ-law format (sometimes written mu-law, often
            approximated as u-law) is commonly used for Twilio audio inputs.
          required: false
          schema:
            $ref: >-
              #/components/schemas/V1TextToSpeechVoiceIdWithTimestampsPostParametersOutputFormat
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AudioWithTimestampsResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Body_text_to_speech_full_with_timestamps'
components:
  schemas:
    V1TextToSpeechVoiceIdWithTimestampsPostParametersOutputFormat:
      type: string
      enum:
        - value: mp3_22050_32
        - value: mp3_24000_48
        - value: mp3_44100_32
        - value: mp3_44100_64
        - value: mp3_44100_96
        - value: mp3_44100_128
        - value: mp3_44100_192
        - value: pcm_8000
        - value: pcm_16000
        - value: pcm_22050
        - value: pcm_24000
        - value: pcm_32000
        - value: pcm_44100
        - value: pcm_48000
        - value: ulaw_8000
        - value: alaw_8000
        - value: opus_48000_32
        - value: opus_48000_64
        - value: opus_48000_96
        - value: opus_48000_128
        - value: opus_48000_192
    VoiceSettingsResponseModel:
      type: object
      properties:
        stability:
          type:
            - number
            - 'null'
          format: double
        use_speaker_boost:
          type:
            - boolean
            - 'null'
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
        style:
          type:
            - number
            - 'null'
          format: double
        speed:
          type:
            - number
            - 'null'
          format: double
    PronunciationDictionaryVersionLocatorRequestModel:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
        version_id:
          type:
            - string
            - 'null'
      required:
        - pronunciation_dictionary_id
    BodyTextToSpeechFullWithTimestampsApplyTextNormalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
    Body_text_to_speech_full_with_timestamps:
      type: object
      properties:
        text:
          type: string
        model_id:
          type: string
        language_code:
          type:
            - string
            - 'null'
        voice_settings:
          oneOf:
            - $ref: '#/components/schemas/VoiceSettingsResponseModel'
            - type: 'null'
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: >-
              #/components/schemas/PronunciationDictionaryVersionLocatorRequestModel
        seed:
          type:
            - integer
            - 'null'
        previous_text:
          type:
            - string
            - 'null'
        next_text:
          type:
            - string
            - 'null'
        previous_request_ids:
          type: array
          items:
            type: string
        next_request_ids:
          type: array
          items:
            type: string
        use_pvc_as_ivc:
          type: boolean
        apply_text_normalization:
          $ref: >-
            #/components/schemas/BodyTextToSpeechFullWithTimestampsApplyTextNormalization
        apply_language_text_normalization:
          type: boolean
      required:
        - text
    CharacterAlignmentResponseModel:
      type: object
      properties:
        characters:
          type: array
          items:
            type: string
        character_start_times_seconds:
          type: array
          items:
            type: number
            format: double
        character_end_times_seconds:
          type: array
          items:
            type: number
            format: double
      required:
        - characters
        - character_start_times_seconds
        - character_end_times_seconds
    AudioWithTimestampsResponseModel:
      type: object
      properties:
        audio_base64:
          type: string
        alignment:
          oneOf:
            - $ref: '#/components/schemas/CharacterAlignmentResponseModel'
            - type: 'null'
        normalized_alignment:
          oneOf:
            - $ref: '#/components/schemas/CharacterAlignmentResponseModel'
            - type: 'null'
      required:
        - audio_base64

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.textToSpeech.convertWithTimestamps("voice_id", {
        text: "This is a test for the API of ElevenLabs.",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_speech.convert_with_timestamps(
    voice_id="voice_id",
    text="This is a test for the API of ElevenLabs."
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/text-to-speech/voice_id/with-timestamps"

	payload := strings.NewReader("{\n  \"text\": \"This is a test for the API of ElevenLabs.\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/text-to-speech/voice_id/with-timestamps")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"This is a test for the API of ElevenLabs.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-speech/voice_id/with-timestamps")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"This is a test for the API of ElevenLabs.\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-speech/voice_id/with-timestamps', [
  'body' => '{
  "text": "This is a test for the API of ElevenLabs."
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-speech/voice_id/with-timestamps");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"This is a test for the API of ElevenLabs.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["text": "This is a test for the API of ElevenLabs."] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-speech/voice_id/with-timestamps")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


# Stream speech

POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream
Content-Type: application/json

Converts text into speech using a voice of your choice and returns audio as an audio stream.

Reference: https://elevenlabs.io/docs/api-reference/text-to-speech/stream


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Stream speech
  version: endpoint_textToSpeech.stream
paths:
  /v1/text-to-speech/{voice_id}/stream:
    post:
      operationId: stream
      summary: Stream speech
      description: >-
        Converts text into speech using a voice of your choice and returns audio
        as an audio stream.
      tags:
        - - subpackage_textToSpeech
      parameters:
        - name: voice_id
          in: path
          description: >-
            ID of the voice to be used. Use the [Get
            voices](/docs/api-reference/voices/search) endpoint list all the
            available voices.
          required: true
          schema:
            type: string
        - name: enable_logging
          in: query
          description: >-
            When enable_logging is set to false zero retention mode will be used
            for the request. This will mean history features are unavailable for
            this request, including request stitching. Zero retention mode may
            only be used by enterprise customers.
          required: false
          schema:
            type: boolean
        - name: optimize_streaming_latency
          in: query
          description: >
            You can turn on latency optimizations at some cost of quality. The
            best possible final latency varies by model. Possible values:

            0 - default mode (no latency optimizations)

            1 - normal latency optimizations (about 50% of possible latency
            improvement of option 3)

            2 - strong latency optimizations (about 75% of possible latency
            improvement of option 3)

            3 - max latency optimizations

            4 - max latency optimizations, but also with text normalizer turned
            off for even more latency savings (best latency, but can
            mispronounce eg numbers and dates).


            Defaults to None.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: output_format
          in: query
          description: >-
            Output format of the generated audio. Formatted as
            codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at
            32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate
            requires you to be subscribed to Creator tier or above. PCM with
            44.1kHz sample rate requires you to be subscribed to Pro tier or
            above. Note that the μ-law format (sometimes written mu-law, often
            approximated as u-law) is commonly used for Twilio audio inputs.
          required: false
          schema:
            $ref: >-
              #/components/schemas/V1TextToSpeechVoiceIdStreamPostParametersOutputFormat
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Streaming audio data
          content:
            text/event-stream:
              schema:
                type: string
                format: binary
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Body_text_to_speech_stream'
components:
  schemas:
    V1TextToSpeechVoiceIdStreamPostParametersOutputFormat:
      type: string
      enum:
        - value: mp3_22050_32
        - value: mp3_24000_48
        - value: mp3_44100_32
        - value: mp3_44100_64
        - value: mp3_44100_96
        - value: mp3_44100_128
        - value: mp3_44100_192
        - value: pcm_8000
        - value: pcm_16000
        - value: pcm_22050
        - value: pcm_24000
        - value: pcm_32000
        - value: pcm_44100
        - value: pcm_48000
        - value: ulaw_8000
        - value: alaw_8000
        - value: opus_48000_32
        - value: opus_48000_64
        - value: opus_48000_96
        - value: opus_48000_128
        - value: opus_48000_192
    VoiceSettingsResponseModel:
      type: object
      properties:
        stability:
          type:
            - number
            - 'null'
          format: double
        use_speaker_boost:
          type:
            - boolean
            - 'null'
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
        style:
          type:
            - number
            - 'null'
          format: double
        speed:
          type:
            - number
            - 'null'
          format: double
    PronunciationDictionaryVersionLocatorRequestModel:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
        version_id:
          type:
            - string
            - 'null'
      required:
        - pronunciation_dictionary_id
    BodyTextToSpeechStreamApplyTextNormalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
    Body_text_to_speech_stream:
      type: object
      properties:
        text:
          type: string
        model_id:
          type: string
        language_code:
          type:
            - string
            - 'null'
        voice_settings:
          oneOf:
            - $ref: '#/components/schemas/VoiceSettingsResponseModel'
            - type: 'null'
        pronunciation_dictionary_locators:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/PronunciationDictionaryVersionLocatorRequestModel
        seed:
          type:
            - integer
            - 'null'
        previous_text:
          type:
            - string
            - 'null'
        next_text:
          type:
            - string
            - 'null'
        previous_request_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        next_request_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        use_pvc_as_ivc:
          type: boolean
        apply_text_normalization:
          $ref: '#/components/schemas/BodyTextToSpeechStreamApplyTextNormalization'
        apply_language_text_normalization:
          type: boolean
      required:
        - text

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.textToSpeech.stream("JBFqnCBsd6RMkjVDRZzb", {
        outputFormat: "mp3_44100_128",
        text: "The first move is what sets everything in motion.",
        modelId: "eleven_multilingual_v2",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_speech.stream(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    output_format="mp3_44100_128",
    text="The first move is what sets everything in motion.",
    model_id="eleven_multilingual_v2"
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb/stream?output_format=mp3_44100_128"

	payload := strings.NewReader("{\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"model_id\": \"eleven_multilingual_v2\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb/stream?output_format=mp3_44100_128")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"model_id\": \"eleven_multilingual_v2\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb/stream?output_format=mp3_44100_128")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"model_id\": \"eleven_multilingual_v2\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb/stream?output_format=mp3_44100_128', [
  'body' => '{
  "text": "The first move is what sets everything in motion.",
  "model_id": "eleven_multilingual_v2"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb/stream?output_format=mp3_44100_128");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"model_id\": \"eleven_multilingual_v2\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "text": "The first move is what sets everything in motion.",
  "model_id": "eleven_multilingual_v2"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb/stream?output_format=mp3_44100_128")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


# Stream speech with timing

POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream/with-timestamps
Content-Type: application/json

Converts text into speech using a voice of your choice and returns a stream of JSONs containing audio as a base64 encoded string together with information on when which character was spoken.

Reference: https://elevenlabs.io/docs/api-reference/text-to-speech/stream-with-timestamps


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Stream speech with timing
  version: endpoint_textToSpeech.stream_with_timestamps
paths:
  /v1/text-to-speech/{voice_id}/stream/with-timestamps:
    post:
      operationId: stream-with-timestamps
      summary: Stream speech with timing
      description: >-
        Converts text into speech using a voice of your choice and returns a
        stream of JSONs containing audio as a base64 encoded string together
        with information on when which character was spoken.
      tags:
        - - subpackage_textToSpeech
      parameters:
        - name: voice_id
          in: path
          description: >-
            ID of the voice to be used. Use the [Get
            voices](/docs/api-reference/voices/search) endpoint list all the
            available voices.
          required: true
          schema:
            type: string
        - name: enable_logging
          in: query
          description: >-
            When enable_logging is set to false zero retention mode will be used
            for the request. This will mean history features are unavailable for
            this request, including request stitching. Zero retention mode may
            only be used by enterprise customers.
          required: false
          schema:
            type: boolean
        - name: optimize_streaming_latency
          in: query
          description: >
            You can turn on latency optimizations at some cost of quality. The
            best possible final latency varies by model. Possible values:

            0 - default mode (no latency optimizations)

            1 - normal latency optimizations (about 50% of possible latency
            improvement of option 3)

            2 - strong latency optimizations (about 75% of possible latency
            improvement of option 3)

            3 - max latency optimizations

            4 - max latency optimizations, but also with text normalizer turned
            off for even more latency savings (best latency, but can
            mispronounce eg numbers and dates).


            Defaults to None.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: output_format
          in: query
          description: >-
            Output format of the generated audio. Formatted as
            codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at
            32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate
            requires you to be subscribed to Creator tier or above. PCM with
            44.1kHz sample rate requires you to be subscribed to Pro tier or
            above. Note that the μ-law format (sometimes written mu-law, often
            approximated as u-law) is commonly used for Twilio audio inputs.
          required: false
          schema:
            $ref: >-
              #/components/schemas/V1TextToSpeechVoiceIdStreamWithTimestampsPostParametersOutputFormat
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Stream of transcription chunks
          content:
            text/event-stream:
              schema:
                $ref: >-
                  #/components/schemas/StreamingAudioChunkWithTimestampsResponseModel
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Body_text_to_speech_stream_with_timestamps'
components:
  schemas:
    V1TextToSpeechVoiceIdStreamWithTimestampsPostParametersOutputFormat:
      type: string
      enum:
        - value: mp3_22050_32
        - value: mp3_24000_48
        - value: mp3_44100_32
        - value: mp3_44100_64
        - value: mp3_44100_96
        - value: mp3_44100_128
        - value: mp3_44100_192
        - value: pcm_8000
        - value: pcm_16000
        - value: pcm_22050
        - value: pcm_24000
        - value: pcm_32000
        - value: pcm_44100
        - value: pcm_48000
        - value: ulaw_8000
        - value: alaw_8000
        - value: opus_48000_32
        - value: opus_48000_64
        - value: opus_48000_96
        - value: opus_48000_128
        - value: opus_48000_192
    VoiceSettingsResponseModel:
      type: object
      properties:
        stability:
          type:
            - number
            - 'null'
          format: double
        use_speaker_boost:
          type:
            - boolean
            - 'null'
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
        style:
          type:
            - number
            - 'null'
          format: double
        speed:
          type:
            - number
            - 'null'
          format: double
    PronunciationDictionaryVersionLocatorRequestModel:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
        version_id:
          type:
            - string
            - 'null'
      required:
        - pronunciation_dictionary_id
    BodyTextToSpeechStreamWithTimestampsApplyTextNormalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
    Body_text_to_speech_stream_with_timestamps:
      type: object
      properties:
        text:
          type: string
        model_id:
          type: string
        language_code:
          type:
            - string
            - 'null'
        voice_settings:
          oneOf:
            - $ref: '#/components/schemas/VoiceSettingsResponseModel'
            - type: 'null'
        pronunciation_dictionary_locators:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/PronunciationDictionaryVersionLocatorRequestModel
        seed:
          type:
            - integer
            - 'null'
        previous_text:
          type:
            - string
            - 'null'
        next_text:
          type:
            - string
            - 'null'
        previous_request_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        next_request_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        use_pvc_as_ivc:
          type: boolean
        apply_text_normalization:
          $ref: >-
            #/components/schemas/BodyTextToSpeechStreamWithTimestampsApplyTextNormalization
        apply_language_text_normalization:
          type: boolean
      required:
        - text
    CharacterAlignmentResponseModel:
      type: object
      properties:
        characters:
          type: array
          items:
            type: string
        character_start_times_seconds:
          type: array
          items:
            type: number
            format: double
        character_end_times_seconds:
          type: array
          items:
            type: number
            format: double
      required:
        - characters
        - character_start_times_seconds
        - character_end_times_seconds
    StreamingAudioChunkWithTimestampsResponseModel:
      type: object
      properties:
        audio_base64:
          type: string
        alignment:
          oneOf:
            - $ref: '#/components/schemas/CharacterAlignmentResponseModel'
            - type: 'null'
        normalized_alignment:
          oneOf:
            - $ref: '#/components/schemas/CharacterAlignmentResponseModel'
            - type: 'null'
      required:
        - audio_base64

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.textToSpeech.streamWithTimestamps("JBFqnCBsd6RMkjVDRZzb", {
        outputFormat: "mp3_44100_128",
        text: "The first move is what sets everything in motion.",
        modelId: "eleven_multilingual_v2",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_speech.stream_with_timestamps(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    output_format="mp3_44100_128",
    text="The first move is what sets everything in motion.",
    model_id="eleven_multilingual_v2"
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb/stream/with-timestamps?output_format=mp3_44100_128"

	payload := strings.NewReader("{\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"model_id\": \"eleven_multilingual_v2\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb/stream/with-timestamps?output_format=mp3_44100_128")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"model_id\": \"eleven_multilingual_v2\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb/stream/with-timestamps?output_format=mp3_44100_128")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"model_id\": \"eleven_multilingual_v2\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb/stream/with-timestamps?output_format=mp3_44100_128', [
  'body' => '{
  "text": "The first move is what sets everything in motion.",
  "model_id": "eleven_multilingual_v2"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb/stream/with-timestamps?output_format=mp3_44100_128");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"model_id\": \"eleven_multilingual_v2\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "text": "The first move is what sets everything in motion.",
  "model_id": "eleven_multilingual_v2"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb/stream/with-timestamps?output_format=mp3_44100_128")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


# Get transcript

GET https://api.elevenlabs.io/v1/speech-to-text/transcripts/{transcription_id}

Retrieve a previously generated transcript by its ID.

Reference: https://elevenlabs.io/docs/api-reference/speech-to-text/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Transcript By Id
  version: endpoint_speechToText/transcripts.get
paths:
  /v1/speech-to-text/transcripts/{transcription_id}:
    get:
      operationId: get
      summary: Get Transcript By Id
      description: Retrieve a previously generated transcript by its ID.
      tags:
        - - subpackage_speechToText
          - subpackage_speechToText/transcripts
      parameters:
        - name: transcription_id
          in: path
          description: The unique ID of the transcript to retrieve
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: The transcript data
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/speech_to_text_transcripts_get_Response_200
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    SpeechToTextWordResponseModelType:
      type: string
      enum:
        - value: word
        - value: spacing
        - value: audio_event
    SpeechToTextCharacterResponseModel:
      type: object
      properties:
        text:
          type: string
        start:
          type:
            - number
            - 'null'
          format: double
        end:
          type:
            - number
            - 'null'
          format: double
      required:
        - text
    SpeechToTextWordResponseModel:
      type: object
      properties:
        text:
          type: string
        start:
          type:
            - number
            - 'null'
          format: double
        end:
          type:
            - number
            - 'null'
          format: double
        type:
          $ref: '#/components/schemas/SpeechToTextWordResponseModelType'
        speaker_id:
          type:
            - string
            - 'null'
        logprob:
          type: number
          format: double
        characters:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/SpeechToTextCharacterResponseModel'
      required:
        - text
        - type
        - logprob
    AdditionalFormatResponseModel:
      type: object
      properties:
        requested_format:
          type: string
        file_extension:
          type: string
        content_type:
          type: string
        is_base64_encoded:
          type: boolean
        content:
          type: string
      required:
        - requested_format
        - file_extension
        - content_type
        - is_base64_encoded
        - content
    SpeechToTextChunkResponseModel:
      type: object
      properties:
        language_code:
          type: string
        language_probability:
          type: number
          format: double
        text:
          type: string
        words:
          type: array
          items:
            $ref: '#/components/schemas/SpeechToTextWordResponseModel'
        channel_index:
          type:
            - integer
            - 'null'
        additional_formats:
          type:
            - array
            - 'null'
          items:
            oneOf:
              - $ref: '#/components/schemas/AdditionalFormatResponseModel'
              - type: 'null'
        transcription_id:
          type:
            - string
            - 'null'
      required:
        - language_code
        - language_probability
        - text
        - words
    MultichannelSpeechToTextResponseModel:
      type: object
      properties:
        transcripts:
          type: array
          items:
            $ref: '#/components/schemas/SpeechToTextChunkResponseModel'
        transcription_id:
          type:
            - string
            - 'null'
      required:
        - transcripts
    speech_to_text_transcripts_get_Response_200:
      oneOf:
        - $ref: '#/components/schemas/SpeechToTextChunkResponseModel'
        - $ref: '#/components/schemas/MultichannelSpeechToTextResponseModel'
        - $ref: '#/components/schemas/SpeechToTextChunkResponseModel'
        - $ref: '#/components/schemas/MultichannelSpeechToTextResponseModel'

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.speechToText.transcripts.get("transcription_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.speech_to_text.transcripts.get(
    transcription_id="transcription_id"
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("xi-api-key", "xi-api-key")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


# Delete transcript

DELETE https://api.elevenlabs.io/v1/speech-to-text/transcripts/{transcription_id}

Delete a previously generated transcript by its ID.

Reference: https://elevenlabs.io/docs/api-reference/speech-to-text/delete


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete Transcript By Id
  version: endpoint_speechToText/transcripts.delete
paths:
  /v1/speech-to-text/transcripts/{transcription_id}:
    delete:
      operationId: delete
      summary: Delete Transcript By Id
      description: Delete a previously generated transcript by its ID.
      tags:
        - - subpackage_speechToText
          - subpackage_speechToText/transcripts
      parameters:
        - name: transcription_id
          in: path
          description: The unique ID of the transcript to delete
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Delete completed successfully.
          content:
            application/json:
              schema:
                description: Any type
        '422':
          description: Validation Error
          content: {}

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.speechToText.transcripts.delete("transcription_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.speech_to_text.transcripts.delete(
    transcription_id="transcription_id"
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id"

	req, _ := http.NewRequest("DELETE", url, nil)

	req.Header.Add("xi-api-key", "xi-api-key")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


# Create transcript

POST https://api.elevenlabs.io/v1/speech-to-text
Content-Type: multipart/form-data

Transcribe an audio or video file. If webhook is set to true, the request will be processed asynchronously and results sent to configured webhooks. When use_multi_channel is true and the provided audio has multiple channels, a 'transcripts' object with separate transcripts for each channel is returned. Otherwise, returns a single transcript. The optional webhook_metadata parameter allows you to attach custom data that will be included in webhook responses for request correlation and tracking.

Reference: https://elevenlabs.io/docs/api-reference/speech-to-text/convert


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create transcript
  version: endpoint_speechToText.convert
paths:
  /v1/speech-to-text:
    post:
      operationId: convert
      summary: Create transcript
      description: >-
        Transcribe an audio or video file. If webhook is set to true, the
        request will be processed asynchronously and results sent to configured
        webhooks. When use_multi_channel is true and the provided audio has
        multiple channels, a 'transcripts' object with separate transcripts for
        each channel is returned. Otherwise, returns a single transcript. The
        optional webhook_metadata parameter allows you to attach custom data
        that will be included in webhook responses for request correlation and
        tracking.
      tags:
        - - subpackage_speechToText
      parameters:
        - name: enable_logging
          in: query
          description: >-
            When enable_logging is set to false zero retention mode will be used
            for the request. This will mean log and transcript storage features
            are unavailable for this request. Zero retention mode may only be
            used by enterprise customers.
          required: false
          schema:
            type: boolean
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Synchronous transcription result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/speech_to_text_convert_Response_200'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                model_id:
                  type: string
                language_code:
                  type:
                    - string
                    - 'null'
                tag_audio_events:
                  type: boolean
                num_speakers:
                  type:
                    - integer
                    - 'null'
                timestamps_granularity:
                  $ref: >-
                    #/components/schemas/V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaTimestampsGranularity
                diarize:
                  type: boolean
                diarization_threshold:
                  type:
                    - number
                    - 'null'
                  format: double
                additional_formats:
                  $ref: '#/components/schemas/AdditionalFormats'
                file_format:
                  $ref: >-
                    #/components/schemas/V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaFileFormat
                cloud_storage_url:
                  type:
                    - string
                    - 'null'
                webhook:
                  type: boolean
                webhook_id:
                  type:
                    - string
                    - 'null'
                temperature:
                  type:
                    - number
                    - 'null'
                  format: double
                seed:
                  type:
                    - integer
                    - 'null'
                use_multi_channel:
                  type: boolean
                webhook_metadata:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaWebhookMetadata
                    - type: 'null'
components:
  schemas:
    V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaTimestampsGranularity:
      type: string
      enum:
        - value: none
        - value: word
        - value: character
    SegmentedJsonExportOptions:
      type: object
      properties:
        include_speakers:
          type: boolean
        include_timestamps:
          type: boolean
        format:
          type: string
          enum:
            - type: stringLiteral
              value: segmented_json
        segment_on_silence_longer_than_s:
          type:
            - number
            - 'null'
          format: double
        max_segment_duration_s:
          type:
            - number
            - 'null'
          format: double
        max_segment_chars:
          type:
            - integer
            - 'null'
      required:
        - format
    DocxExportOptions:
      type: object
      properties:
        include_speakers:
          type: boolean
        include_timestamps:
          type: boolean
        format:
          type: string
          enum:
            - type: stringLiteral
              value: docx
        segment_on_silence_longer_than_s:
          type:
            - number
            - 'null'
          format: double
        max_segment_duration_s:
          type:
            - number
            - 'null'
          format: double
        max_segment_chars:
          type:
            - integer
            - 'null'
      required:
        - format
    PdfExportOptions:
      type: object
      properties:
        include_speakers:
          type: boolean
        include_timestamps:
          type: boolean
        format:
          type: string
          enum:
            - type: stringLiteral
              value: pdf
        segment_on_silence_longer_than_s:
          type:
            - number
            - 'null'
          format: double
        max_segment_duration_s:
          type:
            - number
            - 'null'
          format: double
        max_segment_chars:
          type:
            - integer
            - 'null'
      required:
        - format
    TxtExportOptions:
      type: object
      properties:
        max_characters_per_line:
          type:
            - integer
            - 'null'
        include_speakers:
          type: boolean
        include_timestamps:
          type: boolean
        format:
          type: string
          enum:
            - type: stringLiteral
              value: txt
        segment_on_silence_longer_than_s:
          type:
            - number
            - 'null'
          format: double
        max_segment_duration_s:
          type:
            - number
            - 'null'
          format: double
        max_segment_chars:
          type:
            - integer
            - 'null'
      required:
        - format
    HtmlExportOptions:
      type: object
      properties:
        include_speakers:
          type: boolean
        include_timestamps:
          type: boolean
        format:
          type: string
          enum:
            - type: stringLiteral
              value: html
        segment_on_silence_longer_than_s:
          type:
            - number
            - 'null'
          format: double
        max_segment_duration_s:
          type:
            - number
            - 'null'
          format: double
        max_segment_chars:
          type:
            - integer
            - 'null'
      required:
        - format
    SrtExportOptions:
      type: object
      properties:
        max_characters_per_line:
          type:
            - integer
            - 'null'
        include_speakers:
          type: boolean
        include_timestamps:
          type: boolean
        format:
          type: string
          enum:
            - type: stringLiteral
              value: srt
        segment_on_silence_longer_than_s:
          type:
            - number
            - 'null'
          format: double
        max_segment_duration_s:
          type:
            - number
            - 'null'
          format: double
        max_segment_chars:
          type:
            - integer
            - 'null'
      required:
        - format
    ExportOptions:
      oneOf:
        - $ref: '#/components/schemas/SegmentedJsonExportOptions'
        - $ref: '#/components/schemas/DocxExportOptions'
        - $ref: '#/components/schemas/PdfExportOptions'
        - $ref: '#/components/schemas/TxtExportOptions'
        - $ref: '#/components/schemas/HtmlExportOptions'
        - $ref: '#/components/schemas/SrtExportOptions'
    AdditionalFormats:
      type: array
      items:
        $ref: '#/components/schemas/ExportOptions'
    V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaFileFormat:
      type: string
      enum:
        - value: pcm_s16le_16
        - value: other
    V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaWebhookMetadata:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
    SpeechToTextWordResponseModelType:
      type: string
      enum:
        - value: word
        - value: spacing
        - value: audio_event
    SpeechToTextCharacterResponseModel:
      type: object
      properties:
        text:
          type: string
        start:
          type:
            - number
            - 'null'
          format: double
        end:
          type:
            - number
            - 'null'
          format: double
      required:
        - text
    SpeechToTextWordResponseModel:
      type: object
      properties:
        text:
          type: string
        start:
          type:
            - number
            - 'null'
          format: double
        end:
          type:
            - number
            - 'null'
          format: double
        type:
          $ref: '#/components/schemas/SpeechToTextWordResponseModelType'
        speaker_id:
          type:
            - string
            - 'null'
        logprob:
          type: number
          format: double
        characters:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/SpeechToTextCharacterResponseModel'
      required:
        - text
        - type
        - logprob
    AdditionalFormatResponseModel:
      type: object
      properties:
        requested_format:
          type: string
        file_extension:
          type: string
        content_type:
          type: string
        is_base64_encoded:
          type: boolean
        content:
          type: string
      required:
        - requested_format
        - file_extension
        - content_type
        - is_base64_encoded
        - content
    SpeechToTextChunkResponseModel:
      type: object
      properties:
        language_code:
          type: string
        language_probability:
          type: number
          format: double
        text:
          type: string
        words:
          type: array
          items:
            $ref: '#/components/schemas/SpeechToTextWordResponseModel'
        channel_index:
          type:
            - integer
            - 'null'
        additional_formats:
          type:
            - array
            - 'null'
          items:
            oneOf:
              - $ref: '#/components/schemas/AdditionalFormatResponseModel'
              - type: 'null'
        transcription_id:
          type:
            - string
            - 'null'
      required:
        - language_code
        - language_probability
        - text
        - words
    MultichannelSpeechToTextResponseModel:
      type: object
      properties:
        transcripts:
          type: array
          items:
            $ref: '#/components/schemas/SpeechToTextChunkResponseModel'
        transcription_id:
          type:
            - string
            - 'null'
      required:
        - transcripts
    SpeechToTextWebhookResponseModel:
      type: object
      properties:
        message:
          type: string
        request_id:
          type: string
        transcription_id:
          type:
            - string
            - 'null'
      required:
        - message
        - request_id
    speech_to_text_convert_Response_200:
      oneOf:
        - $ref: '#/components/schemas/SpeechToTextChunkResponseModel'
        - $ref: '#/components/schemas/MultichannelSpeechToTextResponseModel'
        - $ref: '#/components/schemas/SpeechToTextWebhookResponseModel'

```


## SDK Code Examples

```typescript Single channel response
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.speechToText.convert({});
}
main();

```

```python Single channel response
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.speech_to_text.convert()

```

```go Single channel response
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/speech-to-text"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Single channel response
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/speech-to-text")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java Single channel response
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/speech-to-text")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php Single channel response
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/speech-to-text', [
  'multipart' => [
    [
        'name' => 'model_id',
        'contents' => 'string'
    ],
    [
        'name' => 'file',
        'filename' => '<file1>',
        'contents' => null
    ]
  ]
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp Single channel response
var client = new RestClient("https://api.elevenlabs.io/v1/speech-to-text");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Single channel response
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
]
let parameters = [
  [
    "name": "model_id",
    "value": "string"
  ],
  [
    "name": "file",
    "fileName": "<file1>"
  ],
  [
    "name": "language_code",
    "value": 
  ],
  [
    "name": "tag_audio_events",
    "value": 
  ],
  [
    "name": "num_speakers",
    "value": 
  ],
  [
    "name": "timestamps_granularity",
    "value": 
  ],
  [
    "name": "diarize",
    "value": 
  ],
  [
    "name": "diarization_threshold",
    "value": 
  ],
  [
    "name": "additional_formats",
    "value": 
  ],
  [
    "name": "file_format",
    "value": 
  ],
  [
    "name": "cloud_storage_url",
    "value": 
  ],
  [
    "name": "webhook",
    "value": 
  ],
  [
    "name": "webhook_id",
    "value": 
  ],
  [
    "name": "temperature",
    "value": 
  ],
  [
    "name": "seed",
    "value": 
  ],
  [
    "name": "use_multi_channel",
    "value": 
  ],
  [
    "name": "webhook_metadata",
    "value": 
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-to-text")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```typescript Multichannel response
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.speechToText.convert({});
}
main();

```

```python Multichannel response
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.speech_to_text.convert()

```

```go Multichannel response
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/speech-to-text"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Multichannel response
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/speech-to-text")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java Multichannel response
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/speech-to-text")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php Multichannel response
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/speech-to-text', [
  'multipart' => [
    [
        'name' => 'model_id',
        'contents' => 'string'
    ],
    [
        'name' => 'file',
        'filename' => '<file1>',
        'contents' => null
    ]
  ]
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp Multichannel response
var client = new RestClient("https://api.elevenlabs.io/v1/speech-to-text");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Multichannel response
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
]
let parameters = [
  [
    "name": "model_id",
    "value": "string"
  ],
  [
    "name": "file",
    "fileName": "<file1>"
  ],
  [
    "name": "language_code",
    "value": 
  ],
  [
    "name": "tag_audio_events",
    "value": 
  ],
  [
    "name": "num_speakers",
    "value": 
  ],
  [
    "name": "timestamps_granularity",
    "value": 
  ],
  [
    "name": "diarize",
    "value": 
  ],
  [
    "name": "diarization_threshold",
    "value": 
  ],
  [
    "name": "additional_formats",
    "value": 
  ],
  [
    "name": "file_format",
    "value": 
  ],
  [
    "name": "cloud_storage_url",
    "value": 
  ],
  [
    "name": "webhook",
    "value": 
  ],
  [
    "name": "webhook_id",
    "value": 
  ],
  [
    "name": "temperature",
    "value": 
  ],
  [
    "name": "seed",
    "value": 
  ],
  [
    "name": "use_multi_channel",
    "value": 
  ],
  [
    "name": "webhook_metadata",
    "value": 
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-to-text")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.speechToText.convert({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.speech_to_text.convert()

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/speech-to-text"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/speech-to-text")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/speech-to-text")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/speech-to-text', [
  'multipart' => [
    [
        'name' => 'model_id',
        'contents' => 'string'
    ],
    [
        'name' => 'file',
        'filename' => '<file1>',
        'contents' => null
    ]
  ]
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/speech-to-text");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
]
let parameters = [
  [
    "name": "model_id",
    "value": "string"
  ],
  [
    "name": "file",
    "fileName": "<file1>"
  ],
  [
    "name": "language_code",
    "value": 
  ],
  [
    "name": "tag_audio_events",
    "value": 
  ],
  [
    "name": "num_speakers",
    "value": 
  ],
  [
    "name": "timestamps_granularity",
    "value": 
  ],
  [
    "name": "diarize",
    "value": 
  ],
  [
    "name": "diarization_threshold",
    "value": 
  ],
  [
    "name": "additional_formats",
    "value": 
  ],
  [
    "name": "file_format",
    "value": 
  ],
  [
    "name": "cloud_storage_url",
    "value": 
  ],
  [
    "name": "webhook",
    "value": 
  ],
  [
    "name": "webhook_id",
    "value": 
  ],
  [
    "name": "temperature",
    "value": 
  ],
  [
    "name": "seed",
    "value": 
  ],
  [
    "name": "use_multi_channel",
    "value": 
  ],
  [
    "name": "webhook_metadata",
    "value": 
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-to-text")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


---
**Navigation:** [← Previous](./31-get-configuration-override.md) | [Index](./index.md) | [Next →](./33-create-dialogue.md)
