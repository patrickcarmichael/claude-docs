**Navigation:** [← Previous](./33-create-dialogue.md) | [Index](./index.md) | [Next →](./35-update-a-segment.md)

# Voice changer stream

POST https://api.elevenlabs.io/v1/speech-to-speech/{voice_id}/stream
Content-Type: multipart/form-data

Stream audio from one voice to another. Maintain full control over emotion, timing and delivery.

Reference: https://elevenlabs.io/docs/api-reference/speech-to-speech/stream


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Voice changer stream
  version: endpoint_speechToSpeech.stream
paths:
  /v1/speech-to-speech/{voice_id}/stream:
    post:
      operationId: stream
      summary: Voice changer stream
      description: >-
        Stream audio from one voice to another. Maintain full control over
        emotion, timing and delivery.
      tags:
        - - subpackage_speechToSpeech
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
              #/components/schemas/V1SpeechToSpeechVoiceIdStreamPostParametersOutputFormat
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
          multipart/form-data:
            schema:
              type: object
              properties:
                model_id:
                  type: string
                voice_settings:
                  type:
                    - string
                    - 'null'
                seed:
                  type:
                    - integer
                    - 'null'
                remove_background_noise:
                  type: boolean
                file_format:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1SpeechToSpeechVoiceIdStreamPostRequestBodyContentMultipartFormDataSchemaFileFormat
                    - type: 'null'
components:
  schemas:
    V1SpeechToSpeechVoiceIdStreamPostParametersOutputFormat:
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
    V1SpeechToSpeechVoiceIdStreamPostRequestBodyContentMultipartFormDataSchemaFileFormat:
      type: string
      enum:
        - value: pcm_s16le_16
        - value: other

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.speechToSpeech.stream("JBFqnCBsd6RMkjVDRZzb", {
        outputFormat: "mp3_44100_128",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.speech_to_speech.stream(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    output_format="mp3_44100_128"
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

	url := "https://api.elevenlabs.io/v1/speech-to-speech/JBFqnCBsd6RMkjVDRZzb/stream?output_format=mp3_44100_128"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\neleven_multilingual_sts_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/speech-to-speech/JBFqnCBsd6RMkjVDRZzb/stream?output_format=mp3_44100_128")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\neleven_multilingual_sts_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/speech-to-speech/JBFqnCBsd6RMkjVDRZzb/stream?output_format=mp3_44100_128")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\neleven_multilingual_sts_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/speech-to-speech/JBFqnCBsd6RMkjVDRZzb/stream?output_format=mp3_44100_128', [
  'multipart' => [
    [
        'name' => 'audio',
        'filename' => '<file1>',
        'contents' => null
    ],
    [
        'name' => 'model_id',
        'contents' => 'eleven_multilingual_sts_v2'
    ]
  ]
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/speech-to-speech/JBFqnCBsd6RMkjVDRZzb/stream?output_format=mp3_44100_128");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\neleven_multilingual_sts_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
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
    "name": "audio",
    "fileName": "<file1>"
  ],
  [
    "name": "model_id",
    "value": "eleven_multilingual_sts_v2"
  ],
  [
    "name": "voice_settings",
    "value": 
  ],
  [
    "name": "seed",
    "value": 
  ],
  [
    "name": "remove_background_noise",
    "value": 
  ],
  [
    "name": "file_format",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-to-speech/JBFqnCBsd6RMkjVDRZzb/stream?output_format=mp3_44100_128")! as URL,
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


# Create sound effect

POST https://api.elevenlabs.io/v1/sound-generation
Content-Type: application/json

Turn text into sound effects for your videos, voice-overs or video games using the most advanced sound effects models in the world.

Reference: https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create sound effect
  version: endpoint_textToSoundEffects.convert
paths:
  /v1/sound-generation:
    post:
      operationId: convert
      summary: Create sound effect
      description: >-
        Turn text into sound effects for your videos, voice-overs or video games
        using the most advanced sound effects models in the world.
      tags:
        - - subpackage_textToSoundEffects
      parameters:
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
            $ref: '#/components/schemas/V1SoundGenerationPostParametersOutputFormat'
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: The generated sound effect as an MP3 file
          content:
            application/octet-stream:
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
              $ref: >-
                #/components/schemas/Body_Sound_Generation_v1_sound_generation_post
components:
  schemas:
    V1SoundGenerationPostParametersOutputFormat:
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
    Body_Sound_Generation_v1_sound_generation_post:
      type: object
      properties:
        text:
          type: string
        loop:
          type: boolean
        duration_seconds:
          type:
            - number
            - 'null'
          format: double
        prompt_influence:
          type:
            - number
            - 'null'
          format: double
        model_id:
          type: string
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
    await client.textToSoundEffects.convert({
        text: "Spacious braam suitable for high-impact movie trailer moments",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_sound_effects.convert(
    text="Spacious braam suitable for high-impact movie trailer moments"
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

	url := "https://api.elevenlabs.io/v1/sound-generation"

	payload := strings.NewReader("{\n  \"text\": \"Spacious braam suitable for high-impact movie trailer moments\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/sound-generation")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"Spacious braam suitable for high-impact movie trailer moments\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/sound-generation")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"Spacious braam suitable for high-impact movie trailer moments\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/sound-generation', [
  'body' => '{
  "text": "Spacious braam suitable for high-impact movie trailer moments"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/sound-generation");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"Spacious braam suitable for high-impact movie trailer moments\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["text": "Spacious braam suitable for high-impact movie trailer moments"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/sound-generation")! as URL,
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


# Audio isolation

POST https://api.elevenlabs.io/v1/audio-isolation
Content-Type: multipart/form-data

Removes background noise from audio.

Reference: https://elevenlabs.io/docs/api-reference/audio-isolation/convert


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Audio isolation
  version: endpoint_audioIsolation.convert
paths:
  /v1/audio-isolation:
    post:
      operationId: convert
      summary: Audio isolation
      description: Removes background noise from audio.
      tags:
        - - subpackage_audioIsolation
      parameters:
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
                $ref: '#/components/schemas/audio_isolation_convert_Response_200'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file_format:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1AudioIsolationPostRequestBodyContentMultipartFormDataSchemaFileFormat
                    - type: 'null'
                preview_b64:
                  type:
                    - string
                    - 'null'
components:
  schemas:
    V1AudioIsolationPostRequestBodyContentMultipartFormDataSchemaFileFormat:
      type: string
      enum:
        - value: pcm_s16le_16
        - value: other
    audio_isolation_convert_Response_200:
      type: object
      properties: {}

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.audioIsolation.convert({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.audio_isolation.convert()

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

	url := "https://api.elevenlabs.io/v1/audio-isolation"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"preview_b64\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/audio-isolation")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"preview_b64\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/audio-isolation")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"preview_b64\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/audio-isolation', [
  'multipart' => [
    [
        'name' => 'audio',
        'filename' => 'string',
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
var client = new RestClient("https://api.elevenlabs.io/v1/audio-isolation");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"preview_b64\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
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
    "name": "audio",
    "fileName": "string"
  ],
  [
    "name": "file_format",
    "value": 
  ],
  [
    "name": "preview_b64",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/audio-isolation")! as URL,
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


# Audio isolation stream

POST https://api.elevenlabs.io/v1/audio-isolation/stream
Content-Type: multipart/form-data

Removes background noise from audio.

Reference: https://elevenlabs.io/docs/api-reference/audio-isolation/stream


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Audio isolation stream
  version: endpoint_audioIsolation.stream
paths:
  /v1/audio-isolation/stream:
    post:
      operationId: stream
      summary: Audio isolation stream
      description: Removes background noise from audio.
      tags:
        - - subpackage_audioIsolation
      parameters:
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file_format:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1AudioIsolationStreamPostRequestBodyContentMultipartFormDataSchemaFileFormat
                    - type: 'null'
components:
  schemas:
    V1AudioIsolationStreamPostRequestBodyContentMultipartFormDataSchemaFileFormat:
      type: string
      enum:
        - value: pcm_s16le_16
        - value: other

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.audioIsolation.stream({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.audio_isolation.stream()

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

	url := "https://api.elevenlabs.io/v1/audio-isolation/stream"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/audio-isolation/stream")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/audio-isolation/stream")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/audio-isolation/stream', [
  'multipart' => [
    [
        'name' => 'audio',
        'filename' => 'string',
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
var client = new RestClient("https://api.elevenlabs.io/v1/audio-isolation/stream");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
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
    "name": "audio",
    "fileName": "string"
  ],
  [
    "name": "file_format",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/audio-isolation/stream")! as URL,
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


# Design a voice

POST https://api.elevenlabs.io/v1/text-to-voice/design
Content-Type: application/json

Design a voice via a prompt. This method returns a list of voice previews. Each preview has a generated_voice_id and a sample of the voice as base64 encoded mp3 audio. To create a voice use the generated_voice_id of the preferred preview with the /v1/text-to-voice endpoint.

Reference: https://elevenlabs.io/docs/api-reference/text-to-voice/design


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Design A Voice.
  version: endpoint_textToVoice.design
paths:
  /v1/text-to-voice/design:
    post:
      operationId: design
      summary: Design A Voice.
      description: >-
        Design a voice via a prompt. This method returns a list of voice
        previews. Each preview has a generated_voice_id and a sample of the
        voice as base64 encoded mp3 audio. To create a voice use the
        generated_voice_id of the preferred preview with the /v1/text-to-voice
        endpoint.
      tags:
        - - subpackage_textToVoice
      parameters:
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
            $ref: '#/components/schemas/V1TextToVoiceDesignPostParametersOutputFormat'
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
                $ref: '#/components/schemas/VoicePreviewsResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VoiceDesignRequestModel'
components:
  schemas:
    V1TextToVoiceDesignPostParametersOutputFormat:
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
    VoiceDesignRequestModelModelId:
      type: string
      enum:
        - value: eleven_multilingual_ttv_v2
        - value: eleven_ttv_v3
    VoiceDesignRequestModel:
      type: object
      properties:
        voice_description:
          type: string
        model_id:
          $ref: '#/components/schemas/VoiceDesignRequestModelModelId'
        text:
          type:
            - string
            - 'null'
        auto_generate_text:
          type: boolean
        loudness:
          type: number
          format: double
        seed:
          type:
            - integer
            - 'null'
        guidance_scale:
          type: number
          format: double
        stream_previews:
          type: boolean
        remixing_session_id:
          type:
            - string
            - 'null'
        remixing_session_iteration_id:
          type:
            - string
            - 'null'
        quality:
          type:
            - number
            - 'null'
          format: double
        reference_audio_base64:
          type:
            - string
            - 'null'
        prompt_strength:
          type:
            - number
            - 'null'
          format: double
      required:
        - voice_description
    VoicePreviewResponseModel:
      type: object
      properties:
        audio_base_64:
          type: string
        generated_voice_id:
          type: string
        media_type:
          type: string
        duration_secs:
          type: number
          format: double
        language:
          type:
            - string
            - 'null'
      required:
        - audio_base_64
        - generated_voice_id
        - media_type
        - duration_secs
        - language
    VoicePreviewsResponseModel:
      type: object
      properties:
        previews:
          type: array
          items:
            $ref: '#/components/schemas/VoicePreviewResponseModel'
        text:
          type: string
      required:
        - previews
        - text

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.textToVoice.design({
        voiceDescription: "A sassy squeaky mouse",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_voice.design(
    voice_description="A sassy squeaky mouse"
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

	url := "https://api.elevenlabs.io/v1/text-to-voice/design"

	payload := strings.NewReader("{\n  \"voice_description\": \"A sassy squeaky mouse\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-voice/design")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"voice_description\": \"A sassy squeaky mouse\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-voice/design")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"voice_description\": \"A sassy squeaky mouse\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-voice/design', [
  'body' => '{
  "voice_description": "A sassy squeaky mouse"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-voice/design");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"voice_description\": \"A sassy squeaky mouse\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["voice_description": "A sassy squeaky mouse"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-voice/design")! as URL,
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


# Create a voice

POST https://api.elevenlabs.io/v1/text-to-voice
Content-Type: application/json

Create a voice from previously generated voice preview. This endpoint should be called after you fetched a generated_voice_id using POST /v1/text-to-voice/design or POST /v1/text-to-voice/:voice_id/remix.

Reference: https://elevenlabs.io/docs/api-reference/text-to-voice/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create A New Voice From Voice Preview
  version: endpoint_textToVoice.create
paths:
  /v1/text-to-voice:
    post:
      operationId: create
      summary: Create A New Voice From Voice Preview
      description: >-
        Create a voice from previously generated voice preview. This endpoint
        should be called after you fetched a generated_voice_id using POST
        /v1/text-to-voice/design or POST /v1/text-to-voice/:voice_id/remix.
      tags:
        - - subpackage_textToVoice
      parameters:
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
                $ref: '#/components/schemas/VoiceResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Create_a_new_voice_from_voice_preview_v1_text_to_voice_post
components:
  schemas:
    Body_Create_a_new_voice_from_voice_preview_v1_text_to_voice_post:
      type: object
      properties:
        voice_name:
          type: string
        voice_description:
          type: string
        generated_voice_id:
          type: string
        labels:
          type:
            - object
            - 'null'
          additionalProperties:
            type: string
        played_not_selected_voice_ids:
          type:
            - array
            - 'null'
          items:
            type: string
      required:
        - voice_name
        - voice_description
        - generated_voice_id
    SpeakerSeparationResponseModelStatus:
      type: string
      enum:
        - value: not_started
        - value: pending
        - value: completed
        - value: failed
    UtteranceResponseModel:
      type: object
      properties:
        start:
          type: number
          format: double
        end:
          type: number
          format: double
      required:
        - start
        - end
    SpeakerResponseModel:
      type: object
      properties:
        speaker_id:
          type: string
        duration_secs:
          type: number
          format: double
        utterances:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/UtteranceResponseModel'
      required:
        - speaker_id
        - duration_secs
    SpeakerSeparationResponseModel:
      type: object
      properties:
        voice_id:
          type: string
        sample_id:
          type: string
        status:
          $ref: '#/components/schemas/SpeakerSeparationResponseModelStatus'
        speakers:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/SpeakerResponseModel'
        selected_speaker_ids:
          type:
            - array
            - 'null'
          items:
            type: string
      required:
        - voice_id
        - sample_id
        - status
    SampleResponseModel:
      type: object
      properties:
        sample_id:
          type: string
        file_name:
          type: string
        mime_type:
          type: string
        size_bytes:
          type: integer
        hash:
          type: string
        duration_secs:
          type:
            - number
            - 'null'
          format: double
        remove_background_noise:
          type:
            - boolean
            - 'null'
        has_isolated_audio:
          type:
            - boolean
            - 'null'
        has_isolated_audio_preview:
          type:
            - boolean
            - 'null'
        speaker_separation:
          oneOf:
            - $ref: '#/components/schemas/SpeakerSeparationResponseModel'
            - type: 'null'
        trim_start:
          type:
            - integer
            - 'null'
        trim_end:
          type:
            - integer
            - 'null'
    VoiceResponseModelCategory:
      type: string
      enum:
        - value: generated
        - value: cloned
        - value: premade
        - value: professional
        - value: famous
        - value: high_quality
    FineTuningResponseModelState:
      type: string
      enum:
        - value: not_started
        - value: queued
        - value: fine_tuning
        - value: fine_tuned
        - value: failed
        - value: delayed
    RecordingResponseModel:
      type: object
      properties:
        recording_id:
          type: string
        mime_type:
          type: string
        size_bytes:
          type: integer
        upload_date_unix:
          type: integer
        transcription:
          type: string
      required:
        - recording_id
        - mime_type
        - size_bytes
        - upload_date_unix
        - transcription
    VerificationAttemptResponseModel:
      type: object
      properties:
        text:
          type: string
        date_unix:
          type: integer
        accepted:
          type: boolean
        similarity:
          type: number
          format: double
        levenshtein_distance:
          type: number
          format: double
        recording:
          oneOf:
            - $ref: '#/components/schemas/RecordingResponseModel'
            - type: 'null'
      required:
        - text
        - date_unix
        - accepted
        - similarity
        - levenshtein_distance
    ManualVerificationFileResponseModel:
      type: object
      properties:
        file_id:
          type: string
        file_name:
          type: string
        mime_type:
          type: string
        size_bytes:
          type: integer
        upload_date_unix:
          type: integer
      required:
        - file_id
        - file_name
        - mime_type
        - size_bytes
        - upload_date_unix
    ManualVerificationResponseModel:
      type: object
      properties:
        extra_text:
          type: string
        request_time_unix:
          type: integer
        files:
          type: array
          items:
            $ref: '#/components/schemas/ManualVerificationFileResponseModel'
      required:
        - extra_text
        - request_time_unix
        - files
    FineTuningResponseModel:
      type: object
      properties:
        is_allowed_to_fine_tune:
          type: boolean
        state:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/FineTuningResponseModelState'
        verification_failures:
          type: array
          items:
            type: string
        verification_attempts_count:
          type: integer
        manual_verification_requested:
          type: boolean
        language:
          type:
            - string
            - 'null'
        progress:
          type:
            - object
            - 'null'
          additionalProperties:
            type: number
            format: double
        message:
          type:
            - object
            - 'null'
          additionalProperties:
            type: string
        dataset_duration_seconds:
          type:
            - number
            - 'null'
          format: double
        verification_attempts:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VerificationAttemptResponseModel'
        slice_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        manual_verification:
          oneOf:
            - $ref: '#/components/schemas/ManualVerificationResponseModel'
            - type: 'null'
        max_verification_attempts:
          type:
            - integer
            - 'null'
        next_max_verification_attempts_reset_unix_ms:
          type:
            - integer
            - 'null'
        finetuning_state:
          description: Any type
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
    voice_sharing_state:
      type: string
      enum:
        - value: enabled
        - value: disabled
        - value: copied
        - value: copied_disabled
    VoiceSharingResponseModelCategory:
      type: string
      enum:
        - value: generated
        - value: cloned
        - value: premade
        - value: professional
        - value: famous
        - value: high_quality
    review_status:
      type: string
      enum:
        - value: not_requested
        - value: pending
        - value: declined
        - value: allowed
        - value: allowed_with_changes
    VoiceSharingModerationCheckResponseModel:
      type: object
      properties:
        date_checked_unix:
          type:
            - integer
            - 'null'
        name_value:
          type:
            - string
            - 'null'
        name_check:
          type:
            - boolean
            - 'null'
        description_value:
          type:
            - string
            - 'null'
        description_check:
          type:
            - boolean
            - 'null'
        sample_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        sample_checks:
          type:
            - array
            - 'null'
          items:
            type: number
            format: double
        captcha_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        captcha_checks:
          type:
            - array
            - 'null'
          items:
            type: number
            format: double
    ReaderResourceResponseModelResourceType:
      type: string
      enum:
        - value: read
        - value: collection
    ReaderResourceResponseModel:
      type: object
      properties:
        resource_type:
          $ref: '#/components/schemas/ReaderResourceResponseModelResourceType'
        resource_id:
          type: string
      required:
        - resource_type
        - resource_id
    VoiceSharingResponseModel:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/voice_sharing_state'
        history_item_sample_id:
          type:
            - string
            - 'null'
        date_unix:
          type: integer
        whitelisted_emails:
          type: array
          items:
            type: string
        public_owner_id:
          type: string
        original_voice_id:
          type: string
        financial_rewards_enabled:
          type: boolean
        free_users_allowed:
          type: boolean
        live_moderation_enabled:
          type: boolean
        rate:
          type:
            - number
            - 'null'
          format: double
        fiat_rate:
          type:
            - number
            - 'null'
          format: double
        notice_period:
          type: integer
        disable_at_unix:
          type:
            - integer
            - 'null'
        voice_mixing_allowed:
          type: boolean
        featured:
          type: boolean
        category:
          $ref: '#/components/schemas/VoiceSharingResponseModelCategory'
        reader_app_enabled:
          type:
            - boolean
            - 'null'
        image_url:
          type:
            - string
            - 'null'
        ban_reason:
          type:
            - string
            - 'null'
        liked_by_count:
          type: integer
        cloned_by_count:
          type: integer
        name:
          type: string
        description:
          type:
            - string
            - 'null'
        labels:
          type: object
          additionalProperties:
            type: string
        review_status:
          $ref: '#/components/schemas/review_status'
        review_message:
          type:
            - string
            - 'null'
        enabled_in_library:
          type: boolean
        instagram_username:
          type:
            - string
            - 'null'
        twitter_username:
          type:
            - string
            - 'null'
        youtube_username:
          type:
            - string
            - 'null'
        tiktok_username:
          type:
            - string
            - 'null'
        moderation_check:
          oneOf:
            - $ref: '#/components/schemas/VoiceSharingModerationCheckResponseModel'
            - type: 'null'
        reader_restricted_on:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ReaderResourceResponseModel'
    VerifiedVoiceLanguageResponseModel:
      type: object
      properties:
        language:
          type: string
        model_id:
          type: string
        accent:
          type:
            - string
            - 'null'
        locale:
          type:
            - string
            - 'null'
        preview_url:
          type:
            - string
            - 'null'
      required:
        - language
        - model_id
    VoiceResponseModelSafetyControl:
      type: string
      enum:
        - value: NONE
        - value: BAN
        - value: CAPTCHA
        - value: ENTERPRISE_BAN
        - value: ENTERPRISE_CAPTCHA
    VoiceVerificationResponseModel:
      type: object
      properties:
        requires_verification:
          type: boolean
        is_verified:
          type: boolean
        verification_failures:
          type: array
          items:
            type: string
        verification_attempts_count:
          type: integer
        language:
          type:
            - string
            - 'null'
        verification_attempts:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VerificationAttemptResponseModel'
      required:
        - requires_verification
        - is_verified
        - verification_failures
        - verification_attempts_count
    VoiceResponseModel:
      type: object
      properties:
        voice_id:
          type: string
        name:
          type: string
        samples:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/SampleResponseModel'
        category:
          $ref: '#/components/schemas/VoiceResponseModelCategory'
        fine_tuning:
          oneOf:
            - $ref: '#/components/schemas/FineTuningResponseModel'
            - type: 'null'
        labels:
          type: object
          additionalProperties:
            type: string
        description:
          type:
            - string
            - 'null'
        preview_url:
          type:
            - string
            - 'null'
        available_for_tiers:
          type: array
          items:
            type: string
        settings:
          oneOf:
            - $ref: '#/components/schemas/VoiceSettingsResponseModel'
            - type: 'null'
        sharing:
          oneOf:
            - $ref: '#/components/schemas/VoiceSharingResponseModel'
            - type: 'null'
        high_quality_base_model_ids:
          type: array
          items:
            type: string
        verified_languages:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VerifiedVoiceLanguageResponseModel'
        safety_control:
          oneOf:
            - $ref: '#/components/schemas/VoiceResponseModelSafetyControl'
            - type: 'null'
        voice_verification:
          oneOf:
            - $ref: '#/components/schemas/VoiceVerificationResponseModel'
            - type: 'null'
        permission_on_resource:
          type:
            - string
            - 'null'
        is_owner:
          type:
            - boolean
            - 'null'
        is_legacy:
          type: boolean
        is_mixed:
          type: boolean
        favorited_at_unix:
          type:
            - integer
            - 'null'
        created_at_unix:
          type:
            - integer
            - 'null'
      required:
        - voice_id

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.textToVoice.create({
        voiceName: "Sassy squeaky mouse",
        voiceDescription: "A sassy squeaky mouse",
        generatedVoiceId: "37HceQefKmEi3bGovXjL",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_voice.create(
    voice_name="Sassy squeaky mouse",
    voice_description="A sassy squeaky mouse",
    generated_voice_id="37HceQefKmEi3bGovXjL"
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

	url := "https://api.elevenlabs.io/v1/text-to-voice"

	payload := strings.NewReader("{\n  \"voice_name\": \"Sassy squeaky mouse\",\n  \"voice_description\": \"A sassy squeaky mouse\",\n  \"generated_voice_id\": \"37HceQefKmEi3bGovXjL\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-voice")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"voice_name\": \"Sassy squeaky mouse\",\n  \"voice_description\": \"A sassy squeaky mouse\",\n  \"generated_voice_id\": \"37HceQefKmEi3bGovXjL\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-voice")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"voice_name\": \"Sassy squeaky mouse\",\n  \"voice_description\": \"A sassy squeaky mouse\",\n  \"generated_voice_id\": \"37HceQefKmEi3bGovXjL\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-voice', [
  'body' => '{
  "voice_name": "Sassy squeaky mouse",
  "voice_description": "A sassy squeaky mouse",
  "generated_voice_id": "37HceQefKmEi3bGovXjL"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-voice");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"voice_name\": \"Sassy squeaky mouse\",\n  \"voice_description\": \"A sassy squeaky mouse\",\n  \"generated_voice_id\": \"37HceQefKmEi3bGovXjL\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "voice_name": "Sassy squeaky mouse",
  "voice_description": "A sassy squeaky mouse",
  "generated_voice_id": "37HceQefKmEi3bGovXjL"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-voice")! as URL,
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


# Remix a voice

POST https://api.elevenlabs.io/v1/text-to-voice/{voice_id}/remix
Content-Type: application/json

Remix an existing voice via a prompt. This method returns a list of voice previews. Each preview has a generated_voice_id and a sample of the voice as base64 encoded mp3 audio. To create a voice use the generated_voice_id of the preferred preview with the /v1/text-to-voice endpoint.

Reference: https://elevenlabs.io/docs/api-reference/text-to-voice/remix


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Remix A Voice.
  version: endpoint_textToVoice.remix
paths:
  /v1/text-to-voice/{voice_id}/remix:
    post:
      operationId: remix
      summary: Remix A Voice.
      description: >-
        Remix an existing voice via a prompt. This method returns a list of
        voice previews. Each preview has a generated_voice_id and a sample of
        the voice as base64 encoded mp3 audio. To create a voice use the
        generated_voice_id of the preferred preview with the /v1/text-to-voice
        endpoint.
      tags:
        - - subpackage_textToVoice
      parameters:
        - name: voice_id
          in: path
          description: >-
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices
            to list all the available voices.
          required: true
          schema:
            type: string
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
              #/components/schemas/V1TextToVoiceVoiceIdRemixPostParametersOutputFormat
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
                $ref: '#/components/schemas/VoicePreviewsResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VoiceRemixRequestModel'
components:
  schemas:
    V1TextToVoiceVoiceIdRemixPostParametersOutputFormat:
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
    VoiceRemixRequestModel:
      type: object
      properties:
        voice_description:
          type: string
        text:
          type:
            - string
            - 'null'
        auto_generate_text:
          type: boolean
        loudness:
          type: number
          format: double
        seed:
          type:
            - integer
            - 'null'
        guidance_scale:
          type: number
          format: double
        stream_previews:
          type: boolean
        remixing_session_id:
          type:
            - string
            - 'null'
        remixing_session_iteration_id:
          type:
            - string
            - 'null'
        prompt_strength:
          type:
            - number
            - 'null'
          format: double
      required:
        - voice_description
    VoicePreviewResponseModel:
      type: object
      properties:
        audio_base_64:
          type: string
        generated_voice_id:
          type: string
        media_type:
          type: string
        duration_secs:
          type: number
          format: double
        language:
          type:
            - string
            - 'null'
      required:
        - audio_base_64
        - generated_voice_id
        - media_type
        - duration_secs
        - language
    VoicePreviewsResponseModel:
      type: object
      properties:
        previews:
          type: array
          items:
            $ref: '#/components/schemas/VoicePreviewResponseModel'
        text:
          type: string
      required:
        - previews
        - text

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.textToVoice.remix("voice_id", {
        voiceDescription: "Make the voice have a higher pitch.",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_voice.remix(
    voice_id="voice_id",
    voice_description="Make the voice have a higher pitch."
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

	url := "https://api.elevenlabs.io/v1/text-to-voice/voice_id/remix"

	payload := strings.NewReader("{\n  \"voice_description\": \"Make the voice have a higher pitch.\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-voice/voice_id/remix")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"voice_description\": \"Make the voice have a higher pitch.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-voice/voice_id/remix")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"voice_description\": \"Make the voice have a higher pitch.\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-voice/voice_id/remix', [
  'body' => '{
  "voice_description": "Make the voice have a higher pitch."
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-voice/voice_id/remix");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"voice_description\": \"Make the voice have a higher pitch.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["voice_description": "Make the voice have a higher pitch."] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-voice/voice_id/remix")! as URL,
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


# Stream voice preview

GET https://api.elevenlabs.io/v1/text-to-voice/{generated_voice_id}/stream

Stream a voice preview that was created via the /v1/text-to-voice/design endpoint.

Reference: https://elevenlabs.io/docs/api-reference/text-to-voice/stream


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Text To Voice Preview Streaming
  version: endpoint_textToVoice/preview.stream
paths:
  /v1/text-to-voice/{generated_voice_id}/stream:
    get:
      operationId: stream
      summary: Text To Voice Preview Streaming
      description: >-
        Stream a voice preview that was created via the /v1/text-to-voice/design
        endpoint.
      tags:
        - - subpackage_textToVoice
          - subpackage_textToVoice/preview
      parameters:
        - name: generated_voice_id
          in: path
          description: The generated_voice_id to stream.
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
          description: Streaming audio data
          content:
            text/event-stream:
              schema:
                type: string
                format: binary
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
    await client.textToVoice.preview.stream("generated_voice_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_voice.preview.stream(
    generated_voice_id="generated_voice_id"
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

	url := "https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream"

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

url = URI("https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream")! as URL,
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


# Get dubbing resource

GET https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}

Given a dubbing ID generated from the '/v1/dubbing' endpoint with studio enabled, returns the dubbing resource.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/resources/get-resource


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get dubbing resource
  version: endpoint_dubbing/resource.get
paths:
  /v1/dubbing/resource/{dubbing_id}:
    get:
      operationId: get
      summary: Get dubbing resource
      description: >-
        Given a dubbing ID generated from the '/v1/dubbing' endpoint with studio
        enabled, returns the dubbing resource.
      tags:
        - - subpackage_dubbing
          - subpackage_dubbing/resource
      parameters:
        - name: dubbing_id
          in: path
          description: ID of the dubbing project.
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
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DubbingResource'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    DubbingMediaReference:
      type: object
      properties:
        src:
          type: string
        content_type:
          type: string
        bucket_name:
          type: string
        random_path_slug:
          type: string
        duration_secs:
          type: number
          format: double
        is_audio:
          type: boolean
        url:
          type: string
      required:
        - src
        - content_type
        - bucket_name
        - random_path_slug
        - duration_secs
        - is_audio
        - url
    SpeakerTrack:
      type: object
      properties:
        id:
          type: string
        media_ref:
          $ref: '#/components/schemas/DubbingMediaReference'
        speaker_name:
          type: string
        voices:
          type: object
          additionalProperties:
            type: string
        segments:
          type: array
          items:
            type: string
      required:
        - id
        - media_ref
        - speaker_name
        - voices
        - segments
    SegmentSubtitleFrame:
      type: object
      properties:
        start_time:
          type: number
          format: double
        end_time:
          type: number
          format: double
        lines:
          type: array
          items:
            type: string
      required:
        - start_time
        - end_time
        - lines
    DubbedSegment:
      type: object
      properties:
        start_time:
          type: number
          format: double
        end_time:
          type: number
          format: double
        text:
          type:
            - string
            - 'null'
        subtitles:
          type: array
          items:
            $ref: '#/components/schemas/SegmentSubtitleFrame'
        audio_stale:
          type: boolean
        media_ref:
          oneOf:
            - $ref: '#/components/schemas/DubbingMediaReference'
            - type: 'null'
      required:
        - start_time
        - end_time
        - text
        - subtitles
        - audio_stale
        - media_ref
    SpeakerSegment:
      type: object
      properties:
        id:
          type: string
        start_time:
          type: number
          format: double
        end_time:
          type: number
          format: double
        text:
          type: string
        subtitles:
          type: array
          items:
            $ref: '#/components/schemas/SegmentSubtitleFrame'
        dubs:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/DubbedSegment'
      required:
        - id
        - start_time
        - end_time
        - text
        - subtitles
        - dubs
    RenderType:
      type: string
      enum:
        - value: mp4
        - value: aac
        - value: mp3
        - value: wav
        - value: aaf
        - value: tracks_zip
        - value: clips_zip
    RenderStatus:
      type: string
      enum:
        - value: complete
        - value: processing
        - value: failed
    Render:
      type: object
      properties:
        id:
          type: string
        version:
          type: integer
        language:
          type:
            - string
            - 'null'
        type:
          oneOf:
            - $ref: '#/components/schemas/RenderType'
            - type: 'null'
        media_ref:
          oneOf:
            - $ref: '#/components/schemas/DubbingMediaReference'
            - type: 'null'
        status:
          $ref: '#/components/schemas/RenderStatus'
      required:
        - id
        - version
        - language
        - type
        - media_ref
        - status
    DubbingResource:
      type: object
      properties:
        id:
          type: string
        version:
          type: integer
        source_language:
          type: string
        target_languages:
          type: array
          items:
            type: string
        input:
          $ref: '#/components/schemas/DubbingMediaReference'
        background:
          $ref: '#/components/schemas/DubbingMediaReference'
        foreground:
          $ref: '#/components/schemas/DubbingMediaReference'
        speaker_tracks:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/SpeakerTrack'
        speaker_segments:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/SpeakerSegment'
        renders:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/Render'
      required:
        - id
        - version
        - source_language
        - target_languages
        - input
        - background
        - foreground
        - speaker_tracks
        - speaker_segments
        - renders

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.dubbing.resource.get("dubbing_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.resource.get(
    dubbing_id="dubbing_id"
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id")! as URL,
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


# Create segment

POST https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}/segment
Content-Type: application/json

Creates a new segment in dubbing resource with a start and end time for the speaker in every available language. Does not automatically generate transcripts/translations/audio.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/resources/create-segment


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Add speaker segment to dubbing resource
  version: endpoint_dubbing/resource/speaker/segment.create
paths:
  /v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}/segment:
    post:
      operationId: create
      summary: Add speaker segment to dubbing resource
      description: >-
        Creates a new segment in dubbing resource with a start and end time for
        the speaker in every available language. Does not automatically generate
        transcripts/translations/audio.
      tags:
        - - subpackage_dubbing
          - subpackage_dubbing/resource
          - subpackage_dubbing/resource/speaker
          - subpackage_dubbing/resource/speaker/segment
      parameters:
        - name: dubbing_id
          in: path
          description: ID of the dubbing project.
          required: true
          schema:
            type: string
        - name: speaker_id
          in: path
          description: ID of the speaker.
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '201':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SegmentCreateResponse'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SegmentCreatePayload'
components:
  schemas:
    SegmentCreatePayload:
      type: object
      properties:
        start_time:
          type: number
          format: double
        end_time:
          type: number
          format: double
        text:
          type:
            - string
            - 'null'
        translations:
          type:
            - object
            - 'null'
          additionalProperties:
            type: string
      required:
        - start_time
        - end_time
    SegmentCreateResponse:
      type: object
      properties:
        version:
          type: integer
        new_segment:
          type: string
      required:
        - version
        - new_segment

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.dubbing.resource.speaker.segment.create("dubbing_id", "speaker_id", {
        startTime: 1.1,
        endTime: 1.1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.resource.speaker.segment.create(
    dubbing_id="dubbing_id",
    speaker_id="speaker_id",
    start_time=1.1,
    end_time=1.1
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/segment"

	payload := strings.NewReader("{\n  \"start_time\": 1.1,\n  \"end_time\": 1.1\n}")

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/segment")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"start_time\": 1.1,\n  \"end_time\": 1.1\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/segment")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"start_time\": 1.1,\n  \"end_time\": 1.1\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/segment', [
  'body' => '{
  "start_time": 1.1,
  "end_time": 1.1
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/segment");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"start_time\": 1.1,\n  \"end_time\": 1.1\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "start_time": 1.1,
  "end_time": 1.1
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/segment")! as URL,
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


# Delete a segment

DELETE https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/segment/{segment_id}

Deletes a single segment from the dubbing.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/resources/delete-segment


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete a segment
  version: endpoint_dubbing/resource/segment.delete
paths:
  /v1/dubbing/resource/{dubbing_id}/segment/{segment_id}:
    delete:
      operationId: delete
      summary: Delete a segment
      description: Deletes a single segment from the dubbing.
      tags:
        - - subpackage_dubbing
          - subpackage_dubbing/resource
          - subpackage_dubbing/resource/segment
      parameters:
        - name: dubbing_id
          in: path
          description: ID of the dubbing project.
          required: true
          schema:
            type: string
        - name: segment_id
          in: path
          description: ID of the segment
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
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SegmentDeleteResponse'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    SegmentDeleteResponse:
      type: object
      properties:
        version:
          type: integer
      required:
        - version

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.dubbing.resource.segment.delete("dubbing_id", "segment_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.resource.segment.delete(
    dubbing_id="dubbing_id",
    segment_id="segment_id"
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/segment/segment_id"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/segment/segment_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/segment/segment_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/segment/segment_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/segment/segment_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/segment/segment_id")! as URL,
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


---
**Navigation:** [← Previous](./33-create-dialogue.md) | [Index](./index.md) | [Next →](./35-update-a-segment.md)
