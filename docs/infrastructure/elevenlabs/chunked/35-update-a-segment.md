**Navigation:** [← Previous](./34-voice-changer-stream.md) | [Index](./index.md) | [Next →](./36-get-audio-native-project-settings.md)

# Update a segment

PATCH https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/segment/{segment_id}/{language}
Content-Type: application/json

Modifies a single segment with new text and/or start/end times. Will update the values for only a specific language of a segment. Does not automatically regenerate the dub.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/resources/update-segment


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Modify a segment
  version: endpoint_dubbing/resource/segment.update
paths:
  /v1/dubbing/resource/{dubbing_id}/segment/{segment_id}/{language}:
    patch:
      operationId: update
      summary: Modify a segment
      description: >-
        Modifies a single segment with new text and/or start/end times. Will
        update the values for only a specific language of a segment. Does not
        automatically regenerate the dub.
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
        - name: language
          in: path
          description: ID of the language.
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
                $ref: '#/components/schemas/SegmentUpdateResponse'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SegmentUpdatePayload'
components:
  schemas:
    SegmentUpdatePayload:
      type: object
      properties:
        start_time:
          type:
            - number
            - 'null'
          format: double
        end_time:
          type:
            - number
            - 'null'
          format: double
        text:
          type:
            - string
            - 'null'
    SegmentUpdateResponse:
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
    await client.dubbing.resource.segment.update("dubbing_id", "segment_id", "language", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.resource.segment.update(
    dubbing_id="dubbing_id",
    segment_id="segment_id",
    language="language"
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/segment/segment_id/language"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/segment/segment_id/language")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/segment/segment_id/language")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/segment/segment_id/language', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/segment/segment_id/language");
var request = new RestRequest(Method.PATCH);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/segment/segment_id/language")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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


# Transcribe segment

POST https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/transcribe
Content-Type: application/json

Regenerate the transcriptions for the specified segments. Does not automatically regenerate translations or dubs.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/resources/transcribe-segment


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Transcribe segments
  version: endpoint_dubbing/resource.transcribe
paths:
  /v1/dubbing/resource/{dubbing_id}/transcribe:
    post:
      operationId: transcribe
      summary: Transcribe segments
      description: >-
        Regenerate the transcriptions for the specified segments. Does not
        automatically regenerate translations or dubs.
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
                $ref: '#/components/schemas/SegmentTranscriptionResponse'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Transcribes_segments_v1_dubbing_resource__dubbing_id__transcribe_post
components:
  schemas:
    Body_Transcribes_segments_v1_dubbing_resource__dubbing_id__transcribe_post:
      type: object
      properties:
        segments:
          type: array
          items:
            type: string
      required:
        - segments
    SegmentTranscriptionResponse:
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
    await client.dubbing.resource.transcribe("dubbing_id", {
        segments: [
            "string",
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

client.dubbing.resource.transcribe(
    dubbing_id="dubbing_id",
    segments=[
        "string"
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/transcribe"

	payload := strings.NewReader("{\n  \"segments\": [\n    \"string\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/transcribe")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"segments\": [\n    \"string\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/transcribe")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"segments\": [\n    \"string\"\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/transcribe', [
  'body' => '{
  "segments": [
    "string"
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
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/transcribe");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"segments\": [\n    \"string\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["segments": ["string"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/transcribe")! as URL,
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


# Translate segment

POST https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/translate
Content-Type: application/json

Regenerate the translations for either the entire resource or the specified segments/languages. Will automatically transcribe missing transcriptions. Will not automatically regenerate the dubs.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/resources/translate-segment


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Translate segments
  version: endpoint_dubbing/resource.translate
paths:
  /v1/dubbing/resource/{dubbing_id}/translate:
    post:
      operationId: translate
      summary: Translate segments
      description: >-
        Regenerate the translations for either the entire resource or the
        specified segments/languages. Will automatically transcribe missing
        transcriptions. Will not automatically regenerate the dubs.
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
                $ref: '#/components/schemas/SegmentTranslationResponse'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Translates_all_or_some_segments_and_languages_v1_dubbing_resource__dubbing_id__translate_post
components:
  schemas:
    Body_Translates_all_or_some_segments_and_languages_v1_dubbing_resource__dubbing_id__translate_post:
      type: object
      properties:
        segments:
          type: array
          items:
            type: string
        languages:
          type:
            - array
            - 'null'
          items:
            type: string
      required:
        - segments
        - languages
    SegmentTranslationResponse:
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
    await client.dubbing.resource.translate("dubbing_id", {
        segments: [
            "string",
        ],
        languages: [
            "string",
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

client.dubbing.resource.translate(
    dubbing_id="dubbing_id",
    segments=[
        "string"
    ],
    languages=[
        "string"
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate"

	payload := strings.NewReader("{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate', [
  'body' => '{
  "segments": [
    "string"
  ],
  "languages": [
    "string"
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
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "segments": ["string"],
  "languages": ["string"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate")! as URL,
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


# Dub segment

POST https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/dub
Content-Type: application/json

Regenerate the dubs for either the entire resource or the specified segments/languages. Will automatically transcribe and translate any missing transcriptions and translations.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/resources/dub-segment


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Dub segments
  version: endpoint_dubbing/resource.dub
paths:
  /v1/dubbing/resource/{dubbing_id}/dub:
    post:
      operationId: dub
      summary: Dub segments
      description: >-
        Regenerate the dubs for either the entire resource or the specified
        segments/languages. Will automatically transcribe and translate any
        missing transcriptions and translations.
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
                $ref: '#/components/schemas/SegmentDubResponse'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Dubs_all_or_some_segments_and_languages_v1_dubbing_resource__dubbing_id__dub_post
components:
  schemas:
    Body_Dubs_all_or_some_segments_and_languages_v1_dubbing_resource__dubbing_id__dub_post:
      type: object
      properties:
        segments:
          type: array
          items:
            type: string
        languages:
          type:
            - array
            - 'null'
          items:
            type: string
      required:
        - segments
        - languages
    SegmentDubResponse:
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
    await client.dubbing.resource.dub("dubbing_id", {
        segments: [
            "string",
        ],
        languages: [
            "string",
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

client.dubbing.resource.dub(
    dubbing_id="dubbing_id",
    segments=[
        "string"
    ],
    languages=[
        "string"
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/dub"

	payload := strings.NewReader("{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/dub")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/dub")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/dub', [
  'body' => '{
  "segments": [
    "string"
  ],
  "languages": [
    "string"
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
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/dub");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "segments": ["string"],
  "languages": ["string"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/dub")! as URL,
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


# Render project

POST https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/render/{language}
Content-Type: application/json

Regenerate the output media for a language using the latest Studio state. Please ensure all segments have been dubbed before rendering, otherwise they will be omitted. Renders are generated asynchronously, and to check the status of all renders please use the 'Get Dubbing Resource' endpoint.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/resources/render-project


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Render Audio Or Video For The Given Language
  version: endpoint_dubbing/resource.render
paths:
  /v1/dubbing/resource/{dubbing_id}/render/{language}:
    post:
      operationId: render
      summary: Render Audio Or Video For The Given Language
      description: >-
        Regenerate the output media for a language using the latest Studio
        state. Please ensure all segments have been dubbed before rendering,
        otherwise they will be omitted. Renders are generated asynchronously,
        and to check the status of all renders please use the 'Get Dubbing
        Resource' endpoint.
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
        - name: language
          in: path
          description: Render this language
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
                $ref: '#/components/schemas/DubbingRenderResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Render_audio_or_video_for_the_given_language_v1_dubbing_resource__dubbing_id__render__language__post
components:
  schemas:
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
    Body_Render_audio_or_video_for_the_given_language_v1_dubbing_resource__dubbing_id__render__language__post:
      type: object
      properties:
        render_type:
          $ref: '#/components/schemas/RenderType'
        normalize_volume:
          type:
            - boolean
            - 'null'
      required:
        - render_type
    DubbingRenderResponseModel:
      type: object
      properties:
        version:
          type: integer
        render_id:
          type: string
      required:
        - version
        - render_id

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.dubbing.resource.render("dubbing_id", "language", {
        renderType: "mp4",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.resource.render(
    dubbing_id="dubbing_id",
    language="language",
    render_type="mp4"
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/render/language"

	payload := strings.NewReader("{\n  \"render_type\": \"mp4\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/render/language")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"render_type\": \"mp4\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/render/language")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"render_type\": \"mp4\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/render/language', [
  'body' => '{
  "render_type": "mp4"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/render/language");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"render_type\": \"mp4\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["render_type": "mp4"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/render/language")! as URL,
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


# Add language to resource

POST https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/language
Content-Type: application/json

Adds the given ElevenLab Turbo V2/V2.5 language code to the resource. Does not automatically generate transcripts/translations/audio.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/resources/add-language


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Add language to dubbing resource
  version: endpoint_dubbing/resource/language.add
paths:
  /v1/dubbing/resource/{dubbing_id}/language:
    post:
      operationId: add
      summary: Add language to dubbing resource
      description: >-
        Adds the given ElevenLab Turbo V2/V2.5 language code to the resource.
        Does not automatically generate transcripts/translations/audio.
      tags:
        - - subpackage_dubbing
          - subpackage_dubbing/resource
          - subpackage_dubbing/resource/language
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
        '201':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LanguageAddedResponse'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Add_a_language_to_the_resource_v1_dubbing_resource__dubbing_id__language_post
components:
  schemas:
    Body_Add_a_language_to_the_resource_v1_dubbing_resource__dubbing_id__language_post:
      type: object
      properties:
        language:
          type:
            - string
            - 'null'
      required:
        - language
    LanguageAddedResponse:
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
    await client.dubbing.resource.language.add("dubbing_id", {
        language: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.resource.language.add(
    dubbing_id="dubbing_id",
    language="string"
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/language"

	payload := strings.NewReader("{\n  \"language\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/language")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"language\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/language")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"language\": \"string\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/language', [
  'body' => '{
  "language": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/language");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"language\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["language": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/language")! as URL,
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


# Update speaker

PATCH https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}
Content-Type: application/json

Amend the metadata associated with a speaker, such as their voice. Both voice cloning and using voices from the ElevenLabs library are supported.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/resources/update-speaker


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update Metadata For A Speaker
  version: endpoint_dubbing/resource/speaker.update
paths:
  /v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}:
    patch:
      operationId: update
      summary: Update Metadata For A Speaker
      description: >-
        Amend the metadata associated with a speaker, such as their voice. Both
        voice cloning and using voices from the ElevenLabs library are
        supported.
      tags:
        - - subpackage_dubbing
          - subpackage_dubbing/resource
          - subpackage_dubbing/resource/speaker
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
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SpeakerUpdatedResponse'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Update_metadata_for_a_speaker_v1_dubbing_resource__dubbing_id__speaker__speaker_id__patch
components:
  schemas:
    Body_Update_metadata_for_a_speaker_v1_dubbing_resource__dubbing_id__speaker__speaker_id__patch:
      type: object
      properties:
        voice_id:
          type:
            - string
            - 'null'
        languages:
          type:
            - array
            - 'null'
          items:
            type: string
    SpeakerUpdatedResponse:
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
    await client.dubbing.resource.speaker.update("dubbing_id", "speaker_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.resource.speaker.update(
    dubbing_id="dubbing_id",
    speaker_id="speaker_id"
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id");
var request = new RestRequest(Method.PATCH);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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


# Get similar voices

GET https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}/similar-voices

Fetch the top 10 similar voices to a speaker, including the voice IDs, names, descriptions, and, where possible, a sample audio recording.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/resources/get-similar-voices


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Search The Elevenlabs Library For Voices Similar To A Speaker.
  version: endpoint_dubbing/resource/speaker.find_similar_voices
paths:
  /v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}/similar-voices:
    get:
      operationId: find-similar-voices
      summary: Search The Elevenlabs Library For Voices Similar To A Speaker.
      description: >-
        Fetch the top 10 similar voices to a speaker, including the voice IDs,
        names, descriptions, and, where possible, a sample audio recording.
      tags:
        - - subpackage_dubbing
          - subpackage_dubbing/resource
          - subpackage_dubbing/resource/speaker
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
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SimilarVoicesForSpeakerResponse'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    SimilarVoiceCategory:
      type: string
      enum:
        - value: premade
        - value: cloned
        - value: generated
        - value: professional
        - value: famous
    SimilarVoice:
      type: object
      properties:
        voice_id:
          type: string
        name:
          type: string
        category:
          $ref: '#/components/schemas/SimilarVoiceCategory'
        description:
          type:
            - string
            - 'null'
        preview_url:
          type:
            - string
            - 'null'
      required:
        - voice_id
        - name
        - category
    SimilarVoicesForSpeakerResponse:
      type: object
      properties:
        voices:
          type: array
          items:
            $ref: '#/components/schemas/SimilarVoice'
      required:
        - voices

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.dubbing.resource.speaker.findSimilarVoices("dubbing_id", "speaker_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.resource.speaker.find_similar_voices(
    dubbing_id="dubbing_id",
    speaker_id="speaker_id"
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/similar-voices"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/similar-voices")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/similar-voices")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/similar-voices', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/similar-voices");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/similar-voices")! as URL,
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


# List Dubs

GET https://api.elevenlabs.io/v1/dubbing

List the dubs you have access to.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/list


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List Dubs
  version: endpoint_dubbing.list
paths:
  /v1/dubbing:
    get:
      operationId: list
      summary: List Dubs
      description: List the dubs you have access to.
      tags:
        - - subpackage_dubbing
      parameters:
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: page_size
          in: query
          description: >-
            How many dubs to return at maximum. Can not exceed 200, defaults to
            100.
          required: false
          schema:
            type: integer
        - name: dubbing_status
          in: query
          description: What state the dub is currently in.
          required: false
          schema:
            $ref: '#/components/schemas/V1DubbingGetParametersDubbingStatus'
        - name: filter_by_creator
          in: query
          description: >-
            Filters who created the resources being listed, whether it was the
            user running the request or someone else that shared the resource
            with them.
          required: false
          schema:
            $ref: '#/components/schemas/V1DubbingGetParametersFilterByCreator'
        - name: order_by
          in: query
          description: The field to use for ordering results from this query.
          required: false
          schema:
            type: string
            enum:
              - type: stringLiteral
                value: created_at
        - name: order_direction
          in: query
          description: The order direction to use for results from this query.
          required: false
          schema:
            $ref: '#/components/schemas/V1DubbingGetParametersOrderDirection'
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
                $ref: '#/components/schemas/DubbingMetadataPageResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    V1DubbingGetParametersDubbingStatus:
      type: string
      enum:
        - value: dubbing
        - value: dubbed
        - value: failed
    V1DubbingGetParametersFilterByCreator:
      type: string
      enum:
        - value: personal
        - value: others
        - value: all
    V1DubbingGetParametersOrderDirection:
      type: string
      enum:
        - value: DESCENDING
        - value: ASCENDING
    DubbingMediaMetadata:
      type: object
      properties:
        content_type:
          type: string
        duration:
          type: number
          format: double
      required:
        - content_type
        - duration
    DubbingMetadataResponse:
      type: object
      properties:
        dubbing_id:
          type: string
        name:
          type: string
        status:
          type: string
        target_languages:
          type: array
          items:
            type: string
        editable:
          type: boolean
        created_at:
          type: string
          format: date-time
        media_metadata:
          oneOf:
            - $ref: '#/components/schemas/DubbingMediaMetadata'
            - type: 'null'
        error:
          type:
            - string
            - 'null'
      required:
        - dubbing_id
        - name
        - status
        - target_languages
        - created_at
    DubbingMetadataPageResponseModel:
      type: object
      properties:
        dubs:
          type: array
          items:
            $ref: '#/components/schemas/DubbingMetadataResponse'
        next_cursor:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
      required:
        - dubs
        - next_cursor
        - has_more

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.dubbing.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/dubbing"

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

url = URI("https://api.elevenlabs.io/v1/dubbing")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing")! as URL,
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


# Dub a video or audio file

POST https://api.elevenlabs.io/v1/dubbing
Content-Type: multipart/form-data

Dubs a provided audio or video file into given language.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Dub a video or audio file
  version: endpoint_dubbing.create
paths:
  /v1/dubbing:
    post:
      operationId: create
      summary: Dub a video or audio file
      description: Dubs a provided audio or video file into given language.
      tags:
        - - subpackage_dubbing
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
                $ref: '#/components/schemas/DoDubbingResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                name:
                  type:
                    - string
                    - 'null'
                source_url:
                  type:
                    - string
                    - 'null'
                source_lang:
                  type: string
                target_lang:
                  type:
                    - string
                    - 'null'
                target_accent:
                  type:
                    - string
                    - 'null'
                num_speakers:
                  type: integer
                watermark:
                  type: boolean
                start_time:
                  type:
                    - integer
                    - 'null'
                end_time:
                  type:
                    - integer
                    - 'null'
                highest_resolution:
                  type: boolean
                drop_background_audio:
                  type: boolean
                use_profanity_filter:
                  type:
                    - boolean
                    - 'null'
                dubbing_studio:
                  type: boolean
                disable_voice_cloning:
                  type: boolean
                mode:
                  $ref: >-
                    #/components/schemas/V1DubbingPostRequestBodyContentMultipartFormDataSchemaMode
                csv_fps:
                  type:
                    - number
                    - 'null'
                  format: double
components:
  schemas:
    V1DubbingPostRequestBodyContentMultipartFormDataSchemaMode:
      type: string
      enum:
        - value: automatic
        - value: manual
    DoDubbingResponseModel:
      type: object
      properties:
        dubbing_id:
          type: string
        expected_duration_sec:
          type: number
          format: double
      required:
        - dubbing_id
        - expected_duration_sec

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.dubbing.create({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.create()

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

	url := "https://api.elevenlabs.io/v1/dubbing"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"csv_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"foreground_audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"background_audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_lang\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_lang\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_accent\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"watermark\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"start_time\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"end_time\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"highest_resolution\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"drop_background_audio\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_profanity_filter\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"dubbing_studio\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"disable_voice_cloning\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"csv_fps\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/dubbing")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"csv_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"foreground_audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"background_audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_lang\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_lang\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_accent\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"watermark\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"start_time\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"end_time\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"highest_resolution\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"drop_background_audio\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_profanity_filter\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"dubbing_studio\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"disable_voice_cloning\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"csv_fps\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"csv_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"foreground_audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"background_audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_lang\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_lang\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_accent\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"watermark\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"start_time\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"end_time\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"highest_resolution\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"drop_background_audio\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_profanity_filter\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"dubbing_studio\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"disable_voice_cloning\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"csv_fps\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing', [
  'multipart' => [
    [
        'name' => 'file',
        'filename' => '<file1>',
        'contents' => null
    ],
    [
        'name' => 'csv_file',
        'filename' => '<file1>',
        'contents' => null
    ],
    [
        'name' => 'foreground_audio_file',
        'filename' => '<file1>',
        'contents' => null
    ],
    [
        'name' => 'background_audio_file',
        'filename' => '<file1>',
        'contents' => null
    ],
    [
        'name' => 'target_lang',
        'contents' => 'string'
    ]
  ]
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"csv_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"foreground_audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"background_audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_lang\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_lang\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_accent\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"watermark\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"start_time\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"end_time\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"highest_resolution\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"drop_background_audio\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_profanity_filter\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"dubbing_studio\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"disable_voice_cloning\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"csv_fps\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
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
    "fileName": "<file1>"
  ],
  [
    "name": "csv_file",
    "fileName": "<file1>"
  ],
  [
    "name": "foreground_audio_file",
    "fileName": "<file1>"
  ],
  [
    "name": "background_audio_file",
    "fileName": "<file1>"
  ],
  [
    "name": "name",
    "value": 
  ],
  [
    "name": "source_url",
    "value": 
  ],
  [
    "name": "source_lang",
    "value": 
  ],
  [
    "name": "target_lang",
    "value": "string"
  ],
  [
    "name": "target_accent",
    "value": 
  ],
  [
    "name": "num_speakers",
    "value": 
  ],
  [
    "name": "watermark",
    "value": 
  ],
  [
    "name": "start_time",
    "value": 
  ],
  [
    "name": "end_time",
    "value": 
  ],
  [
    "name": "highest_resolution",
    "value": 
  ],
  [
    "name": "drop_background_audio",
    "value": 
  ],
  [
    "name": "use_profanity_filter",
    "value": 
  ],
  [
    "name": "dubbing_studio",
    "value": 
  ],
  [
    "name": "disable_voice_cloning",
    "value": 
  ],
  [
    "name": "mode",
    "value": 
  ],
  [
    "name": "csv_fps",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing")! as URL,
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


# Get dubbing

GET https://api.elevenlabs.io/v1/dubbing/{dubbing_id}

Returns metadata about a dubbing project, including whether it's still in progress or not

Reference: https://elevenlabs.io/docs/api-reference/dubbing/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get dubbing
  version: endpoint_dubbing.get
paths:
  /v1/dubbing/{dubbing_id}:
    get:
      operationId: get
      summary: Get dubbing
      description: >-
        Returns metadata about a dubbing project, including whether it's still
        in progress or not
      tags:
        - - subpackage_dubbing
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
                $ref: '#/components/schemas/DubbingMetadataResponse'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    DubbingMediaMetadata:
      type: object
      properties:
        content_type:
          type: string
        duration:
          type: number
          format: double
      required:
        - content_type
        - duration
    DubbingMetadataResponse:
      type: object
      properties:
        dubbing_id:
          type: string
        name:
          type: string
        status:
          type: string
        target_languages:
          type: array
          items:
            type: string
        editable:
          type: boolean
        created_at:
          type: string
          format: date-time
        media_metadata:
          oneOf:
            - $ref: '#/components/schemas/DubbingMediaMetadata'
            - type: 'null'
        error:
          type:
            - string
            - 'null'
      required:
        - dubbing_id
        - name
        - status
        - target_languages
        - created_at

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.dubbing.get("dubbing_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.get(
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

	url := "https://api.elevenlabs.io/v1/dubbing/dubbing_id"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/dubbing_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/dubbing_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/dubbing_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/dubbing_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/dubbing_id")! as URL,
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


# Delete dubbing

DELETE https://api.elevenlabs.io/v1/dubbing/{dubbing_id}

Deletes a dubbing project.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/delete


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete dubbing
  version: endpoint_dubbing.delete
paths:
  /v1/dubbing/{dubbing_id}:
    delete:
      operationId: delete
      summary: Delete dubbing
      description: Deletes a dubbing project.
      tags:
        - - subpackage_dubbing
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
                $ref: '#/components/schemas/DeleteDubbingResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    DeleteDubbingResponseModel:
      type: object
      properties:
        status:
          type: string
      required:
        - status

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.dubbing.delete("dubbing_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.delete(
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

	url := "https://api.elevenlabs.io/v1/dubbing/dubbing_id"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/dubbing_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/dubbing/dubbing_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/dubbing/dubbing_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/dubbing_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/dubbing_id")! as URL,
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


# Get dubbed audio

GET https://api.elevenlabs.io/v1/dubbing/{dubbing_id}/audio/{language_code}

Returns dub as a streamed MP3 or MP4 file. If this dub has been edited using Dubbing Studio you need to use the resource render endpoint as this endpoint only returns the original automatic dub result.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/audio/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get dubbed audio
  version: endpoint_dubbing/audio.get
paths:
  /v1/dubbing/{dubbing_id}/audio/{language_code}:
    get:
      operationId: get
      summary: Get dubbed audio
      description: >-
        Returns dub as a streamed MP3 or MP4 file. If this dub has been edited
        using Dubbing Studio you need to use the resource render endpoint as
        this endpoint only returns the original automatic dub result.
      tags:
        - - subpackage_dubbing
          - subpackage_dubbing/audio
      parameters:
        - name: dubbing_id
          in: path
          description: ID of the dubbing project.
          required: true
          schema:
            type: string
        - name: language_code
          in: path
          description: ID of the language.
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
          description: The dubbed audio or video file
          content:
            application/octet-stream:
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
    await client.dubbing.audio.get("dubbing_id", "language_code");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.audio.get(
    dubbing_id="dubbing_id",
    language_code="language_code"
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

	url := "https://api.elevenlabs.io/v1/dubbing/dubbing_id/audio/language_code"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/dubbing_id/audio/language_code")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/dubbing_id/audio/language_code")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/dubbing_id/audio/language_code', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/dubbing_id/audio/language_code");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/dubbing_id/audio/language_code")! as URL,
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


# Get dubbed transcript

GET https://api.elevenlabs.io/v1/dubbing/{dubbing_id}/transcript/{language_code}

Returns transcript for the dub as an SRT or WEBVTT file.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/transcript/get-transcript-for-dub


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get dubbed transcript
  version: endpoint_dubbing/transcript.get_transcript_for_dub
paths:
  /v1/dubbing/{dubbing_id}/transcript/{language_code}:
    get:
      operationId: get-transcript-for-dub
      summary: Get dubbed transcript
      description: Returns transcript for the dub as an SRT or WEBVTT file.
      tags:
        - - subpackage_dubbing
          - subpackage_dubbing/transcript
      parameters:
        - name: dubbing_id
          in: path
          description: ID of the dubbing project.
          required: true
          schema:
            type: string
        - name: language_code
          in: path
          description: ID of the language.
          required: true
          schema:
            type: string
        - name: format_type
          in: query
          description: Format to use for the subtitle file, either 'srt' or 'webvtt'
          required: false
          schema:
            $ref: >-
              #/components/schemas/V1DubbingDubbingIdTranscriptLanguageCodeGetParametersFormatType
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Response with status 200
          content:
            application/json:
              schema:
                type: object
                properties: {}
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    V1DubbingDubbingIdTranscriptLanguageCodeGetParametersFormatType:
      type: string
      enum:
        - value: srt
        - value: webvtt

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.dubbing.transcript.getTranscriptForDub("dubbing_id", "language_code", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.dubbing.transcript.get_transcript_for_dub(
    dubbing_id="dubbing_id",
    language_code="language_code"
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

	url := "https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code")! as URL,
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


# Create audio native project

POST https://api.elevenlabs.io/v1/audio-native
Content-Type: multipart/form-data

Creates Audio Native enabled project, optionally starts conversion and returns project ID and embeddable HTML snippet.

Reference: https://elevenlabs.io/docs/api-reference/audio-native/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create audio native project
  version: endpoint_audioNative.create
paths:
  /v1/audio-native:
    post:
      operationId: create
      summary: Create audio native project
      description: >-
        Creates Audio Native enabled project, optionally starts conversion and
        returns project ID and embeddable HTML snippet.
      tags:
        - - subpackage_audioNative
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
                $ref: '#/components/schemas/AudioNativeCreateProjectResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                name:
                  type: string
                image:
                  type:
                    - string
                    - 'null'
                author:
                  type:
                    - string
                    - 'null'
                title:
                  type:
                    - string
                    - 'null'
                small:
                  type: boolean
                text_color:
                  type:
                    - string
                    - 'null'
                background_color:
                  type:
                    - string
                    - 'null'
                sessionization:
                  type: integer
                voice_id:
                  type:
                    - string
                    - 'null'
                model_id:
                  type:
                    - string
                    - 'null'
                auto_convert:
                  type: boolean
                apply_text_normalization:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1AudioNativePostRequestBodyContentMultipartFormDataSchemaApplyTextNormalization
                    - type: 'null'
                pronunciation_dictionary_locators:
                  type: array
                  items:
                    type: string
components:
  schemas:
    V1AudioNativePostRequestBodyContentMultipartFormDataSchemaApplyTextNormalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
        - value: apply_english
    AudioNativeCreateProjectResponseModel:
      type: object
      properties:
        project_id:
          type: string
        converting:
          type: boolean
        html_snippet:
          type: string
      required:
        - project_id
        - converting
        - html_snippet

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.audioNative.create({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.audio_native.create()

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

	url := "https://api.elevenlabs.io/v1/audio-native"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"small\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"background_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"sessionization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/audio-native")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"small\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"background_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"sessionization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/audio-native")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"small\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"background_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"sessionization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/audio-native', [
  'multipart' => [
    [
        'name' => 'name',
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
var client = new RestClient("https://api.elevenlabs.io/v1/audio-native");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"small\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"background_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"sessionization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
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
    "name": "name",
    "value": "string"
  ],
  [
    "name": "image",
    "value": 
  ],
  [
    "name": "author",
    "value": 
  ],
  [
    "name": "title",
    "value": 
  ],
  [
    "name": "small",
    "value": 
  ],
  [
    "name": "text_color",
    "value": 
  ],
  [
    "name": "background_color",
    "value": 
  ],
  [
    "name": "sessionization",
    "value": 
  ],
  [
    "name": "voice_id",
    "value": 
  ],
  [
    "name": "model_id",
    "value": 
  ],
  [
    "name": "file",
    "fileName": "<file1>"
  ],
  [
    "name": "auto_convert",
    "value": 
  ],
  [
    "name": "apply_text_normalization",
    "value": 
  ],
  [
    "name": "pronunciation_dictionary_locators",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/audio-native")! as URL,
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
**Navigation:** [← Previous](./34-voice-changer-stream.md) | [Index](./index.md) | [Next →](./36-get-audio-native-project-settings.md)
