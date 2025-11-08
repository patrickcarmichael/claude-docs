**Navigation:** [← Previous](./32-create-speech-with-timing.md) | [Index](./index.md) | [Next →](./34-voice-changer-stream.md)

# Create dialogue

POST https://api.elevenlabs.io/v1/text-to-dialogue
Content-Type: application/json

Converts a list of text and voice ID pairs into speech (dialogue) and returns audio.

Reference: https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create dialogue
  version: endpoint_textToDialogue.convert
paths:
  /v1/text-to-dialogue:
    post:
      operationId: convert
      summary: Create dialogue
      description: >-
        Converts a list of text and voice ID pairs into speech (dialogue) and
        returns audio.
      tags:
        - - subpackage_textToDialogue
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
            $ref: '#/components/schemas/V1TextToDialoguePostParametersOutputFormat'
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: The generated audio file
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
                #/components/schemas/Body_Text_to_dialogue__multi_voice__v1_text_to_dialogue_post
components:
  schemas:
    V1TextToDialoguePostParametersOutputFormat:
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
    DialogueInput:
      type: object
      properties:
        text:
          type: string
        voice_id:
          type: string
      required:
        - text
        - voice_id
    ModelSettingsResponseModel:
      type: object
      properties:
        stability:
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
    BodyTextToDialogueMultiVoiceV1TextToDialoguePostApplyTextNormalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
    Body_Text_to_dialogue__multi_voice__v1_text_to_dialogue_post:
      type: object
      properties:
        inputs:
          type: array
          items:
            $ref: '#/components/schemas/DialogueInput'
        model_id:
          type: string
        language_code:
          type:
            - string
            - 'null'
        settings:
          oneOf:
            - $ref: '#/components/schemas/ModelSettingsResponseModel'
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
        apply_text_normalization:
          $ref: >-
            #/components/schemas/BodyTextToDialogueMultiVoiceV1TextToDialoguePostApplyTextNormalization
      required:
        - inputs

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.textToDialogue.convert({
        inputs: [
            {
                text: "Knock knock",
                voiceId: "JBFqnCBsd6RMkjVDRZzb",
            },
            {
                text: "Who is there?",
                voiceId: "Aw4FAjKCGjjNkVhN1Xmq",
            },
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_dialogue.convert(
    inputs=[
        {
            "text": "Knock knock",
            "voice_id": "JBFqnCBsd6RMkjVDRZzb"
        },
        {
            "text": "Who is there?",
            "voice_id": "Aw4FAjKCGjjNkVhN1Xmq"
        }
    ]
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

	url := "https://api.elevenlabs.io/v1/text-to-dialogue"

	payload := strings.NewReader("{\n  \"inputs\": [\n    {\n      \"text\": \"Knock knock\",\n      \"voice_id\": \"JBFqnCBsd6RMkjVDRZzb\"\n    },\n    {\n      \"text\": \"Who is there?\",\n      \"voice_id\": \"Aw4FAjKCGjjNkVhN1Xmq\"\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-dialogue")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"inputs\": [\n    {\n      \"text\": \"Knock knock\",\n      \"voice_id\": \"JBFqnCBsd6RMkjVDRZzb\"\n    },\n    {\n      \"text\": \"Who is there?\",\n      \"voice_id\": \"Aw4FAjKCGjjNkVhN1Xmq\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-dialogue")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"inputs\": [\n    {\n      \"text\": \"Knock knock\",\n      \"voice_id\": \"JBFqnCBsd6RMkjVDRZzb\"\n    },\n    {\n      \"text\": \"Who is there?\",\n      \"voice_id\": \"Aw4FAjKCGjjNkVhN1Xmq\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-dialogue', [
  'body' => '{
  "inputs": [
    {
      "text": "Knock knock",
      "voice_id": "JBFqnCBsd6RMkjVDRZzb"
    },
    {
      "text": "Who is there?",
      "voice_id": "Aw4FAjKCGjjNkVhN1Xmq"
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-dialogue");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"inputs\": [\n    {\n      \"text\": \"Knock knock\",\n      \"voice_id\": \"JBFqnCBsd6RMkjVDRZzb\"\n    },\n    {\n      \"text\": \"Who is there?\",\n      \"voice_id\": \"Aw4FAjKCGjjNkVhN1Xmq\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["inputs": [
    [
      "text": "Knock knock",
      "voice_id": "JBFqnCBsd6RMkjVDRZzb"
    ],
    [
      "text": "Who is there?",
      "voice_id": "Aw4FAjKCGjjNkVhN1Xmq"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-dialogue")! as URL,
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


# Stream dialogue

POST https://api.elevenlabs.io/v1/text-to-dialogue/stream
Content-Type: application/json

Converts a list of text and voice ID pairs into speech (dialogue) and returns an audio stream.

Reference: https://elevenlabs.io/docs/api-reference/text-to-dialogue/stream


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Stream dialogue
  version: endpoint_textToDialogue.stream
paths:
  /v1/text-to-dialogue/stream:
    post:
      operationId: stream
      summary: Stream dialogue
      description: >-
        Converts a list of text and voice ID pairs into speech (dialogue) and
        returns an audio stream.
      tags:
        - - subpackage_textToDialogue
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
            $ref: >-
              #/components/schemas/V1TextToDialogueStreamPostParametersOutputFormat
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
              $ref: >-
                #/components/schemas/Body_Text_to_dialogue__multi_voice__streaming_v1_text_to_dialogue_stream_post
components:
  schemas:
    V1TextToDialogueStreamPostParametersOutputFormat:
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
    DialogueInput:
      type: object
      properties:
        text:
          type: string
        voice_id:
          type: string
      required:
        - text
        - voice_id
    ModelSettingsResponseModel:
      type: object
      properties:
        stability:
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
    BodyTextToDialogueMultiVoiceStreamingV1TextToDialogueStreamPostApplyTextNormalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
    Body_Text_to_dialogue__multi_voice__streaming_v1_text_to_dialogue_stream_post:
      type: object
      properties:
        inputs:
          type: array
          items:
            $ref: '#/components/schemas/DialogueInput'
        model_id:
          type: string
        language_code:
          type:
            - string
            - 'null'
        settings:
          oneOf:
            - $ref: '#/components/schemas/ModelSettingsResponseModel'
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
        apply_text_normalization:
          $ref: >-
            #/components/schemas/BodyTextToDialogueMultiVoiceStreamingV1TextToDialogueStreamPostApplyTextNormalization
      required:
        - inputs

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.textToDialogue.stream({
        inputs: [
            {
                text: "Knock knock",
                voiceId: "JBFqnCBsd6RMkjVDRZzb",
            },
            {
                text: "Who is there?",
                voiceId: "Aw4FAjKCGjjNkVhN1Xmq",
            },
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_dialogue.stream(
    inputs=[
        {
            "text": "Knock knock",
            "voice_id": "JBFqnCBsd6RMkjVDRZzb"
        },
        {
            "text": "Who is there?",
            "voice_id": "Aw4FAjKCGjjNkVhN1Xmq"
        }
    ]
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

	url := "https://api.elevenlabs.io/v1/text-to-dialogue/stream"

	payload := strings.NewReader("{\n  \"inputs\": [\n    {\n      \"text\": \"Knock knock\",\n      \"voice_id\": \"JBFqnCBsd6RMkjVDRZzb\"\n    },\n    {\n      \"text\": \"Who is there?\",\n      \"voice_id\": \"Aw4FAjKCGjjNkVhN1Xmq\"\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-dialogue/stream")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"inputs\": [\n    {\n      \"text\": \"Knock knock\",\n      \"voice_id\": \"JBFqnCBsd6RMkjVDRZzb\"\n    },\n    {\n      \"text\": \"Who is there?\",\n      \"voice_id\": \"Aw4FAjKCGjjNkVhN1Xmq\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-dialogue/stream")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"inputs\": [\n    {\n      \"text\": \"Knock knock\",\n      \"voice_id\": \"JBFqnCBsd6RMkjVDRZzb\"\n    },\n    {\n      \"text\": \"Who is there?\",\n      \"voice_id\": \"Aw4FAjKCGjjNkVhN1Xmq\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-dialogue/stream', [
  'body' => '{
  "inputs": [
    {
      "text": "Knock knock",
      "voice_id": "JBFqnCBsd6RMkjVDRZzb"
    },
    {
      "text": "Who is there?",
      "voice_id": "Aw4FAjKCGjjNkVhN1Xmq"
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-dialogue/stream");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"inputs\": [\n    {\n      \"text\": \"Knock knock\",\n      \"voice_id\": \"JBFqnCBsd6RMkjVDRZzb\"\n    },\n    {\n      \"text\": \"Who is there?\",\n      \"voice_id\": \"Aw4FAjKCGjjNkVhN1Xmq\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["inputs": [
    [
      "text": "Knock knock",
      "voice_id": "JBFqnCBsd6RMkjVDRZzb"
    ],
    [
      "text": "Who is there?",
      "voice_id": "Aw4FAjKCGjjNkVhN1Xmq"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-dialogue/stream")! as URL,
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


# Create dialogue with timestamps

POST https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps
Content-Type: application/json

Generate dialogue from text with precise character-level timing information for audio-text synchronization.

Reference: https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert-with-timestamps


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Text To Dialogue With Timestamps
  version: endpoint_textToDialogue.convert_with_timestamps
paths:
  /v1/text-to-dialogue/with-timestamps:
    post:
      operationId: convert-with-timestamps
      summary: Text To Dialogue With Timestamps
      description: >-
        Generate dialogue from text with precise character-level timing
        information for audio-text synchronization.
      tags:
        - - subpackage_textToDialogue
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
            $ref: >-
              #/components/schemas/V1TextToDialogueWithTimestampsPostParametersOutputFormat
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
                $ref: >-
                  #/components/schemas/AudioWithTimestampsAndVoiceSegmentsResponseModel
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Body_text_to_dialogue_full_with_timestamps'
components:
  schemas:
    V1TextToDialogueWithTimestampsPostParametersOutputFormat:
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
    DialogueInput:
      type: object
      properties:
        text:
          type: string
        voice_id:
          type: string
      required:
        - text
        - voice_id
    ModelSettingsResponseModel:
      type: object
      properties:
        stability:
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
    BodyTextToDialogueFullWithTimestampsApplyTextNormalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
    Body_text_to_dialogue_full_with_timestamps:
      type: object
      properties:
        inputs:
          type: array
          items:
            $ref: '#/components/schemas/DialogueInput'
        model_id:
          type: string
        language_code:
          type:
            - string
            - 'null'
        settings:
          oneOf:
            - $ref: '#/components/schemas/ModelSettingsResponseModel'
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
        apply_text_normalization:
          $ref: >-
            #/components/schemas/BodyTextToDialogueFullWithTimestampsApplyTextNormalization
      required:
        - inputs
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
    VoiceSegment:
      type: object
      properties:
        voice_id:
          type: string
        start_time_seconds:
          type: number
          format: double
        end_time_seconds:
          type: number
          format: double
        character_start_index:
          type: integer
        character_end_index:
          type: integer
        dialogue_input_index:
          type: integer
      required:
        - voice_id
        - start_time_seconds
        - end_time_seconds
        - character_start_index
        - character_end_index
        - dialogue_input_index
    AudioWithTimestampsAndVoiceSegmentsResponseModel:
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
        voice_segments:
          type: array
          items:
            $ref: '#/components/schemas/VoiceSegment'
      required:
        - audio_base64
        - voice_segments

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.textToDialogue.convertWithTimestamps({
        inputs: [
            {
                text: "string",
                voiceId: "string",
            },
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_dialogue.convert_with_timestamps(
    inputs=[
        {
            "text": "string",
            "voice_id": "string"
        }
    ]
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

	url := "https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps"

	payload := strings.NewReader("{\n  \"inputs\": [\n    {\n      \"text\": \"string\",\n      \"voice_id\": \"string\"\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"inputs\": [\n    {\n      \"text\": \"string\",\n      \"voice_id\": \"string\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"inputs\": [\n    {\n      \"text\": \"string\",\n      \"voice_id\": \"string\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps', [
  'body' => '{
  "inputs": [
    {
      "text": "string",
      "voice_id": "string"
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"inputs\": [\n    {\n      \"text\": \"string\",\n      \"voice_id\": \"string\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["inputs": [
    [
      "text": "string",
      "voice_id": "string"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps")! as URL,
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


# Stream dialogue with timestamps

POST https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps
Content-Type: application/json

Converts a list of text and voice ID pairs into speech (dialogue) and returns a stream of JSON blobs containing audio as a base64 encoded string and timestamps

Reference: https://elevenlabs.io/docs/api-reference/text-to-dialogue/stream-with-timestamps


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Text To Dialogue Streaming With Timestamps
  version: endpoint_textToDialogue.stream_with_timestamps
paths:
  /v1/text-to-dialogue/stream/with-timestamps:
    post:
      operationId: stream-with-timestamps
      summary: Text To Dialogue Streaming With Timestamps
      description: >-
        Converts a list of text and voice ID pairs into speech (dialogue) and
        returns a stream of JSON blobs containing audio as a base64 encoded
        string and timestamps
      tags:
        - - subpackage_textToDialogue
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
            $ref: >-
              #/components/schemas/V1TextToDialogueStreamWithTimestampsPostParametersOutputFormat
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
                  #/components/schemas/StreamingAudioChunkWithTimestampsAndVoiceSegmentsResponseModel
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_text_to_dialogue_stream_with_timestamps
components:
  schemas:
    V1TextToDialogueStreamWithTimestampsPostParametersOutputFormat:
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
    DialogueInput:
      type: object
      properties:
        text:
          type: string
        voice_id:
          type: string
      required:
        - text
        - voice_id
    ModelSettingsResponseModel:
      type: object
      properties:
        stability:
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
    BodyTextToDialogueStreamWithTimestampsApplyTextNormalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
    Body_text_to_dialogue_stream_with_timestamps:
      type: object
      properties:
        inputs:
          type: array
          items:
            $ref: '#/components/schemas/DialogueInput'
        model_id:
          type: string
        language_code:
          type:
            - string
            - 'null'
        settings:
          oneOf:
            - $ref: '#/components/schemas/ModelSettingsResponseModel'
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
        apply_text_normalization:
          $ref: >-
            #/components/schemas/BodyTextToDialogueStreamWithTimestampsApplyTextNormalization
      required:
        - inputs
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
    VoiceSegment:
      type: object
      properties:
        voice_id:
          type: string
        start_time_seconds:
          type: number
          format: double
        end_time_seconds:
          type: number
          format: double
        character_start_index:
          type: integer
        character_end_index:
          type: integer
        dialogue_input_index:
          type: integer
      required:
        - voice_id
        - start_time_seconds
        - end_time_seconds
        - character_start_index
        - character_end_index
        - dialogue_input_index
    StreamingAudioChunkWithTimestampsAndVoiceSegmentsResponseModel:
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
        voice_segments:
          type: array
          items:
            $ref: '#/components/schemas/VoiceSegment'
      required:
        - audio_base64
        - voice_segments

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.textToDialogue.streamWithTimestamps({
        inputs: [
            {
                text: "string",
                voiceId: "string",
            },
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_dialogue.stream_with_timestamps(
    inputs=[
        {
            "text": "string",
            "voice_id": "string"
        }
    ]
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

	url := "https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps"

	payload := strings.NewReader("{\n  \"inputs\": [\n    {\n      \"text\": \"string\",\n      \"voice_id\": \"string\"\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"inputs\": [\n    {\n      \"text\": \"string\",\n      \"voice_id\": \"string\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"inputs\": [\n    {\n      \"text\": \"string\",\n      \"voice_id\": \"string\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps', [
  'body' => '{
  "inputs": [
    {
      "text": "string",
      "voice_id": "string"
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"inputs\": [\n    {\n      \"text\": \"string\",\n      \"voice_id\": \"string\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["inputs": [
    [
      "text": "string",
      "voice_id": "string"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps")! as URL,
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


# Compose music

POST https://api.elevenlabs.io/v1/music
Content-Type: application/json

Compose a song from a prompt or a composition plan.

Reference: https://elevenlabs.io/docs/api-reference/music/compose


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Compose Music
  version: endpoint_music.compose
paths:
  /v1/music:
    post:
      operationId: compose
      summary: Compose Music
      description: Compose a song from a prompt or a composition plan.
      tags:
        - - subpackage_music
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
            $ref: '#/components/schemas/V1MusicPostParametersOutputFormat'
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: The generated audio file in the format specified
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
              $ref: '#/components/schemas/Body_Compose_music_v1_music_post'
components:
  schemas:
    V1MusicPostParametersOutputFormat:
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
    TimeRange:
      type: object
      properties:
        start_ms:
          type: integer
        end_ms:
          type: integer
      required:
        - start_ms
        - end_ms
    SectionSource:
      type: object
      properties:
        song_id:
          type: string
        range:
          $ref: '#/components/schemas/TimeRange'
        negative_ranges:
          type: array
          items:
            $ref: '#/components/schemas/TimeRange'
      required:
        - song_id
        - range
    SongSection:
      type: object
      properties:
        section_name:
          type: string
        positive_local_styles:
          type: array
          items:
            type: string
        negative_local_styles:
          type: array
          items:
            type: string
        duration_ms:
          type: integer
        lines:
          type: array
          items:
            type: string
        source_from:
          oneOf:
            - $ref: '#/components/schemas/SectionSource'
            - type: 'null'
      required:
        - section_name
        - positive_local_styles
        - negative_local_styles
        - duration_ms
        - lines
    MusicPrompt:
      type: object
      properties:
        positive_global_styles:
          type: array
          items:
            type: string
        negative_global_styles:
          type: array
          items:
            type: string
        sections:
          type: array
          items:
            $ref: '#/components/schemas/SongSection'
      required:
        - positive_global_styles
        - negative_global_styles
        - sections
    BodyComposeMusicV1MusicPostModelId:
      type: string
      enum:
        - value: music_v1
    Body_Compose_music_v1_music_post:
      type: object
      properties:
        prompt:
          type:
            - string
            - 'null'
        composition_plan:
          oneOf:
            - $ref: '#/components/schemas/MusicPrompt'
            - type: 'null'
        music_length_ms:
          type:
            - integer
            - 'null'
        model_id:
          $ref: '#/components/schemas/BodyComposeMusicV1MusicPostModelId'
        force_instrumental:
          type: boolean
        respect_sections_durations:
          type: boolean
        store_for_inpainting:
          type: boolean

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.music.compose({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.music.compose()

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

	url := "https://api.elevenlabs.io/v1/music"

	payload := strings.NewReader("{}")

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

url = URI("https://api.elevenlabs.io/v1/music")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/music");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music")! as URL,
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


# Stream music

POST https://api.elevenlabs.io/v1/music/stream
Content-Type: application/json

Stream a composed song from a prompt or a composition plan.

Reference: https://elevenlabs.io/docs/api-reference/music/stream


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Stream Composed Music
  version: endpoint_music.stream
paths:
  /v1/music/stream:
    post:
      operationId: stream
      summary: Stream Composed Music
      description: Stream a composed song from a prompt or a composition plan.
      tags:
        - - subpackage_music
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
            $ref: '#/components/schemas/V1MusicStreamPostParametersOutputFormat'
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Streaming audio data in the format specified
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
              $ref: >-
                #/components/schemas/Body_Stream_composed_music_v1_music_stream_post
components:
  schemas:
    V1MusicStreamPostParametersOutputFormat:
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
    TimeRange:
      type: object
      properties:
        start_ms:
          type: integer
        end_ms:
          type: integer
      required:
        - start_ms
        - end_ms
    SectionSource:
      type: object
      properties:
        song_id:
          type: string
        range:
          $ref: '#/components/schemas/TimeRange'
        negative_ranges:
          type: array
          items:
            $ref: '#/components/schemas/TimeRange'
      required:
        - song_id
        - range
    SongSection:
      type: object
      properties:
        section_name:
          type: string
        positive_local_styles:
          type: array
          items:
            type: string
        negative_local_styles:
          type: array
          items:
            type: string
        duration_ms:
          type: integer
        lines:
          type: array
          items:
            type: string
        source_from:
          oneOf:
            - $ref: '#/components/schemas/SectionSource'
            - type: 'null'
      required:
        - section_name
        - positive_local_styles
        - negative_local_styles
        - duration_ms
        - lines
    MusicPrompt:
      type: object
      properties:
        positive_global_styles:
          type: array
          items:
            type: string
        negative_global_styles:
          type: array
          items:
            type: string
        sections:
          type: array
          items:
            $ref: '#/components/schemas/SongSection'
      required:
        - positive_global_styles
        - negative_global_styles
        - sections
    BodyStreamComposedMusicV1MusicStreamPostModelId:
      type: string
      enum:
        - value: music_v1
    Body_Stream_composed_music_v1_music_stream_post:
      type: object
      properties:
        prompt:
          type:
            - string
            - 'null'
        composition_plan:
          oneOf:
            - $ref: '#/components/schemas/MusicPrompt'
            - type: 'null'
        music_length_ms:
          type:
            - integer
            - 'null'
        model_id:
          $ref: '#/components/schemas/BodyStreamComposedMusicV1MusicStreamPostModelId'
        force_instrumental:
          type: boolean
        store_for_inpainting:
          type: boolean

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.music.stream({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.music.stream()

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

	url := "https://api.elevenlabs.io/v1/music/stream"

	payload := strings.NewReader("{}")

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

url = URI("https://api.elevenlabs.io/v1/music/stream")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music/stream")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music/stream', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/music/stream");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/stream")! as URL,
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


# Compose music with details

POST https://api.elevenlabs.io/v1/music/detailed
Content-Type: application/json

Compose a song from a prompt or a composition plan.

Reference: https://elevenlabs.io/docs/api-reference/music/compose-detailed


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Compose Music With A Detailed Response
  version: endpoint_music.compose_detailed
paths:
  /v1/music/detailed:
    post:
      operationId: compose-detailed
      summary: Compose Music With A Detailed Response
      description: Compose a song from a prompt or a composition plan.
      tags:
        - - subpackage_music
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
            $ref: '#/components/schemas/V1MusicDetailedPostParametersOutputFormat'
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Multipart/mixed response with JSON metadata and binary audio file
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/music_compose_detailed_Response_200'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Compose_Music_with_a_detailed_response_v1_music_detailed_post
components:
  schemas:
    V1MusicDetailedPostParametersOutputFormat:
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
    TimeRange:
      type: object
      properties:
        start_ms:
          type: integer
        end_ms:
          type: integer
      required:
        - start_ms
        - end_ms
    SectionSource:
      type: object
      properties:
        song_id:
          type: string
        range:
          $ref: '#/components/schemas/TimeRange'
        negative_ranges:
          type: array
          items:
            $ref: '#/components/schemas/TimeRange'
      required:
        - song_id
        - range
    SongSection:
      type: object
      properties:
        section_name:
          type: string
        positive_local_styles:
          type: array
          items:
            type: string
        negative_local_styles:
          type: array
          items:
            type: string
        duration_ms:
          type: integer
        lines:
          type: array
          items:
            type: string
        source_from:
          oneOf:
            - $ref: '#/components/schemas/SectionSource'
            - type: 'null'
      required:
        - section_name
        - positive_local_styles
        - negative_local_styles
        - duration_ms
        - lines
    MusicPrompt:
      type: object
      properties:
        positive_global_styles:
          type: array
          items:
            type: string
        negative_global_styles:
          type: array
          items:
            type: string
        sections:
          type: array
          items:
            $ref: '#/components/schemas/SongSection'
      required:
        - positive_global_styles
        - negative_global_styles
        - sections
    BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId:
      type: string
      enum:
        - value: music_v1
    Body_Compose_Music_with_a_detailed_response_v1_music_detailed_post:
      type: object
      properties:
        prompt:
          type:
            - string
            - 'null'
        composition_plan:
          oneOf:
            - $ref: '#/components/schemas/MusicPrompt'
            - type: 'null'
        music_length_ms:
          type:
            - integer
            - 'null'
        model_id:
          $ref: >-
            #/components/schemas/BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId
        force_instrumental:
          type: boolean
        store_for_inpainting:
          type: boolean
    music_compose_detailed_Response_200:
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
    await client.music.composeDetailed({
        prompt: "A prompt for music generation",
        musicLengthMs: 10000,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.music.compose_detailed(
    prompt="A prompt for music generation",
    music_length_ms=10000
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

	url := "https://api.elevenlabs.io/v1/music/detailed"

	payload := strings.NewReader("{\n  \"prompt\": \"A prompt for music generation\",\n  \"music_length_ms\": 10000\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/music/detailed")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"prompt\": \"A prompt for music generation\",\n  \"music_length_ms\": 10000\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music/detailed")
  .header("Content-Type", "application/json")
  .body("{\n  \"prompt\": \"A prompt for music generation\",\n  \"music_length_ms\": 10000\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music/detailed', [
  'body' => '{
  "prompt": "A prompt for music generation",
  "music_length_ms": 10000
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/music/detailed");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"prompt\": \"A prompt for music generation\",\n  \"music_length_ms\": 10000\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "prompt": "A prompt for music generation",
  "music_length_ms": 10000
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/detailed")! as URL,
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


# Create composition plan

POST https://api.elevenlabs.io/v1/music/plan
Content-Type: application/json

Create a composition plan for music generation. Usage of this endpoint does not cost any credits but is subject to rate limiting depending on your tier.

Reference: https://elevenlabs.io/docs/api-reference/music/create-composition-plan


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Generate Composition Plan
  version: endpoint_music/compositionPlan.create
paths:
  /v1/music/plan:
    post:
      operationId: create
      summary: Generate Composition Plan
      description: >-
        Create a composition plan for music generation. Usage of this endpoint
        does not cost any credits but is subject to rate limiting depending on
        your tier.
      tags:
        - - subpackage_music
          - subpackage_music/compositionPlan
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
                $ref: '#/components/schemas/MusicPrompt'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Generate_composition_plan_v1_music_plan_post
components:
  schemas:
    TimeRange:
      type: object
      properties:
        start_ms:
          type: integer
        end_ms:
          type: integer
      required:
        - start_ms
        - end_ms
    SectionSource:
      type: object
      properties:
        song_id:
          type: string
        range:
          $ref: '#/components/schemas/TimeRange'
        negative_ranges:
          type: array
          items:
            $ref: '#/components/schemas/TimeRange'
      required:
        - song_id
        - range
    SongSection:
      type: object
      properties:
        section_name:
          type: string
        positive_local_styles:
          type: array
          items:
            type: string
        negative_local_styles:
          type: array
          items:
            type: string
        duration_ms:
          type: integer
        lines:
          type: array
          items:
            type: string
        source_from:
          oneOf:
            - $ref: '#/components/schemas/SectionSource'
            - type: 'null'
      required:
        - section_name
        - positive_local_styles
        - negative_local_styles
        - duration_ms
        - lines
    MusicPrompt:
      type: object
      properties:
        positive_global_styles:
          type: array
          items:
            type: string
        negative_global_styles:
          type: array
          items:
            type: string
        sections:
          type: array
          items:
            $ref: '#/components/schemas/SongSection'
      required:
        - positive_global_styles
        - negative_global_styles
        - sections
    BodyGenerateCompositionPlanV1MusicPlanPostModelId:
      type: string
      enum:
        - value: music_v1
    Body_Generate_composition_plan_v1_music_plan_post:
      type: object
      properties:
        prompt:
          type: string
        music_length_ms:
          type:
            - integer
            - 'null'
        source_composition_plan:
          oneOf:
            - $ref: '#/components/schemas/MusicPrompt'
            - type: 'null'
        model_id:
          $ref: >-
            #/components/schemas/BodyGenerateCompositionPlanV1MusicPlanPostModelId
      required:
        - prompt

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.music.compositionPlan.create({
        prompt: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.music.composition_plan.create(
    prompt="string"
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

	url := "https://api.elevenlabs.io/v1/music/plan"

	payload := strings.NewReader("{\n  \"prompt\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/music/plan")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"prompt\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music/plan")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"prompt\": \"string\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music/plan', [
  'body' => '{
  "prompt": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/music/plan");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"prompt\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["prompt": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/plan")! as URL,
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


# Stem Separation

POST https://api.elevenlabs.io/v1/music/stem-separation
Content-Type: multipart/form-data

Separate an audio file into individual stems. This endpoint might have high latency, depending on the length of the audio file.

Reference: https://elevenlabs.io/docs/api-reference/music/separate-stems


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Stem Separation
  version: endpoint_music.separate_stems
paths:
  /v1/music/stem-separation:
    post:
      operationId: separate-stems
      summary: Stem Separation
      description: >-
        Separate an audio file into individual stems. This endpoint might have
        high latency, depending on the length of the audio file.
      tags:
        - - subpackage_music
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
            $ref: >-
              #/components/schemas/V1MusicStemSeparationPostParametersOutputFormat
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: >-
            ZIP archive containing separated audio stems. Each stem is provided
            as a separate audio file in the requested output format.
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
          multipart/form-data:
            schema:
              type: object
              properties:
                stem_variation_id:
                  $ref: >-
                    #/components/schemas/V1MusicStemSeparationPostRequestBodyContentMultipartFormDataSchemaStemVariationId
components:
  schemas:
    V1MusicStemSeparationPostParametersOutputFormat:
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
    V1MusicStemSeparationPostRequestBodyContentMultipartFormDataSchemaStemVariationId:
      type: string
      enum:
        - value: two_stems_v1
        - value: six_stems_v1

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.music.separateStems({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.music.separate_stems()

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

	url := "https://api.elevenlabs.io/v1/music/stem-separation"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"stem_variation_id\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/music/stem-separation")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"stem_variation_id\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music/stem-separation")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"stem_variation_id\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music/stem-separation', [
  'multipart' => [
    [
        'name' => 'file',
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
var client = new RestClient("https://api.elevenlabs.io/v1/music/stem-separation");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"stem_variation_id\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
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
    "name": "file",
    "fileName": "string"
  ],
  [
    "name": "stem_variation_id",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/stem-separation")! as URL,
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


# Voice changer

POST https://api.elevenlabs.io/v1/speech-to-speech/{voice_id}
Content-Type: multipart/form-data

Transform audio from one voice to another. Maintain full control over emotion, timing and delivery.

Reference: https://elevenlabs.io/docs/api-reference/speech-to-speech/convert


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Voice changer
  version: endpoint_speechToSpeech.convert
paths:
  /v1/speech-to-speech/{voice_id}:
    post:
      operationId: convert
      summary: Voice changer
      description: >-
        Transform audio from one voice to another. Maintain full control over
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
              #/components/schemas/V1SpeechToSpeechVoiceIdPostParametersOutputFormat
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: The generated audio file
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
                        #/components/schemas/V1SpeechToSpeechVoiceIdPostRequestBodyContentMultipartFormDataSchemaFileFormat
                    - type: 'null'
components:
  schemas:
    V1SpeechToSpeechVoiceIdPostParametersOutputFormat:
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
    V1SpeechToSpeechVoiceIdPostRequestBodyContentMultipartFormDataSchemaFileFormat:
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
    await client.speechToSpeech.convert("JBFqnCBsd6RMkjVDRZzb", {
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

client.speech_to_speech.convert(
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

	url := "https://api.elevenlabs.io/v1/speech-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128"

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

url = URI("https://api.elevenlabs.io/v1/speech-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128")

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
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/speech-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\neleven_multilingual_sts_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/speech-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128', [
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
var client = new RestClient("https://api.elevenlabs.io/v1/speech-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128")! as URL,
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
**Navigation:** [← Previous](./32-create-speech-with-timing.md) | [Index](./index.md) | [Next →](./34-voice-changer-stream.md)
