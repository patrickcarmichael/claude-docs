**Navigation:** [← Previous](./37-list-voices.md) | [Index](./index.md) | [Next →](./39-delete-studio-project.md)

# Get history item

GET https://api.elevenlabs.io/v1/history/{history_item_id}

Retrieves a history item.

Reference: https://elevenlabs.io/docs/api-reference/history/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get history item
  version: endpoint_history.get
paths:
  /v1/history/{history_item_id}:
    get:
      operationId: get
      summary: Get history item
      description: Retrieves a history item.
      tags:
        - - subpackage_history
      parameters:
        - name: history_item_id
          in: path
          description: >-
            ID of the history item to be used. You can use the [Get generated
            items](/docs/api-reference/history/get-all) endpoint to retrieve a
            list of history items.
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
                $ref: '#/components/schemas/SpeechHistoryItemResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    SpeechHistoryItemResponseModelVoiceCategory:
      type: string
      enum:
        - value: premade
        - value: cloned
        - value: generated
        - value: professional
    SpeechHistoryItemResponseModelSettings:
      type: object
      properties: {}
    FeedbackResponseModel:
      type: object
      properties:
        thumbs_up:
          type: boolean
        feedback:
          type: string
        emotions:
          type: boolean
        inaccurate_clone:
          type: boolean
        glitches:
          type: boolean
        audio_quality:
          type: boolean
        other:
          type: boolean
        review_status:
          type: string
      required:
        - thumbs_up
        - feedback
        - emotions
        - inaccurate_clone
        - glitches
        - audio_quality
        - other
    SpeechHistoryItemResponseModelSource:
      type: string
      enum:
        - value: TTS
        - value: STS
        - value: Projects
        - value: PD
        - value: AN
        - value: Dubbing
        - value: PlayAPI
        - value: ConvAI
        - value: VoiceGeneration
    HistoryAlignmentResponseModel:
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
    HistoryAlignmentsResponseModel:
      type: object
      properties:
        alignment:
          $ref: '#/components/schemas/HistoryAlignmentResponseModel'
        normalized_alignment:
          $ref: '#/components/schemas/HistoryAlignmentResponseModel'
      required:
        - alignment
        - normalized_alignment
    DialogueInputResponseModel:
      type: object
      properties:
        text:
          type: string
        voice_id:
          type: string
        voice_name:
          type: string
      required:
        - text
        - voice_id
        - voice_name
    SpeechHistoryItemResponseModel:
      type: object
      properties:
        history_item_id:
          type: string
        request_id:
          type:
            - string
            - 'null'
        voice_id:
          type:
            - string
            - 'null'
        model_id:
          type:
            - string
            - 'null'
        voice_name:
          type:
            - string
            - 'null'
        voice_category:
          oneOf:
            - $ref: '#/components/schemas/SpeechHistoryItemResponseModelVoiceCategory'
            - type: 'null'
        text:
          type:
            - string
            - 'null'
        date_unix:
          type: integer
        character_count_change_from:
          type: integer
        character_count_change_to:
          type: integer
        content_type:
          type: string
        state:
          description: Any type
        settings:
          oneOf:
            - $ref: '#/components/schemas/SpeechHistoryItemResponseModelSettings'
            - type: 'null'
        feedback:
          oneOf:
            - $ref: '#/components/schemas/FeedbackResponseModel'
            - type: 'null'
        share_link_id:
          type:
            - string
            - 'null'
        source:
          oneOf:
            - $ref: '#/components/schemas/SpeechHistoryItemResponseModelSource'
            - type: 'null'
        alignments:
          oneOf:
            - $ref: '#/components/schemas/HistoryAlignmentsResponseModel'
            - type: 'null'
        dialogue:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/DialogueInputResponseModel'
      required:
        - history_item_id
        - date_unix
        - character_count_change_from
        - character_count_change_to
        - content_type
        - state

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.history.get("history_item_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.history.get(
    history_item_id="history_item_id"
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

	url := "https://api.elevenlabs.io/v1/history/history_item_id"

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

url = URI("https://api.elevenlabs.io/v1/history/history_item_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/history/history_item_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/history/history_item_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/history/history_item_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/history/history_item_id")! as URL,
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


# Delete history item

DELETE https://api.elevenlabs.io/v1/history/{history_item_id}

Delete a history item by its ID

Reference: https://elevenlabs.io/docs/api-reference/history/delete


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete history item
  version: endpoint_history.delete
paths:
  /v1/history/{history_item_id}:
    delete:
      operationId: delete
      summary: Delete history item
      description: Delete a history item by its ID
      tags:
        - - subpackage_history
      parameters:
        - name: history_item_id
          in: path
          description: >-
            ID of the history item to be used. You can use the [Get generated
            items](/docs/api-reference/history/get-all) endpoint to retrieve a
            list of history items.
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
                $ref: '#/components/schemas/DeleteHistoryItemResponse'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    DeleteHistoryItemResponse:
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
    await client.history.delete("history_item_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.history.delete(
    history_item_id="history_item_id"
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

	url := "https://api.elevenlabs.io/v1/history/history_item_id"

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

url = URI("https://api.elevenlabs.io/v1/history/history_item_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/history/history_item_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/history/history_item_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/history/history_item_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/history/history_item_id")! as URL,
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


# Get audio from history item

GET https://api.elevenlabs.io/v1/history/{history_item_id}/audio

Returns the audio of an history item.

Reference: https://elevenlabs.io/docs/api-reference/history/get-audio


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get audio from history item
  version: endpoint_history.get_audio
paths:
  /v1/history/{history_item_id}/audio:
    get:
      operationId: get-audio
      summary: Get audio from history item
      description: Returns the audio of an history item.
      tags:
        - - subpackage_history
      parameters:
        - name: history_item_id
          in: path
          description: >-
            ID of the history item to be used. You can use the [Get generated
            items](/docs/api-reference/history/get-all) endpoint to retrieve a
            list of history items.
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
          description: The audio file of the history item.
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
    await client.history.getAudio("history_item_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.history.get_audio(
    history_item_id="history_item_id"
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

	url := "https://api.elevenlabs.io/v1/history/history_item_id/audio"

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

url = URI("https://api.elevenlabs.io/v1/history/history_item_id/audio")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/history/history_item_id/audio")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/history/history_item_id/audio', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/history/history_item_id/audio");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/history/history_item_id/audio")! as URL,
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


# Download history items

POST https://api.elevenlabs.io/v1/history/download
Content-Type: application/json

Download one or more history items. If one history item ID is provided, we will return a single audio file. If more than one history item IDs are provided, we will provide the history items packed into a .zip file.

Reference: https://elevenlabs.io/docs/api-reference/history/download


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Download history items
  version: endpoint_history.download
paths:
  /v1/history/download:
    post:
      operationId: download
      summary: Download history items
      description: >-
        Download one or more history items. If one history item ID is provided,
        we will return a single audio file. If more than one history item IDs
        are provided, we will provide the history items packed into a .zip file.
      tags:
        - - subpackage_history
      parameters:
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: >-
            The requested audio file, or a zip file containing multiple audio
            files when multiple history items are requested.
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
        '400':
          description: Invalid request
          content: {}
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Download_history_items_v1_history_download_post
components:
  schemas:
    Body_Download_history_items_v1_history_download_post:
      type: object
      properties:
        history_item_ids:
          type: array
          items:
            type: string
        output_format:
          type:
            - string
            - 'null'
      required:
        - history_item_ids

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.history.download({
        historyItemIds: [
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

client.history.download(
    history_item_ids=[
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

	url := "https://api.elevenlabs.io/v1/history/download"

	payload := strings.NewReader("{\n  \"history_item_ids\": [\n    \"string\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/history/download")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"history_item_ids\": [\n    \"string\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/history/download")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"history_item_ids\": [\n    \"string\"\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/history/download', [
  'body' => '{
  "history_item_ids": [
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
var client = new RestClient("https://api.elevenlabs.io/v1/history/download");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"history_item_ids\": [\n    \"string\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["history_item_ids": ["string"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/history/download")! as URL,
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


# List models

GET https://api.elevenlabs.io/v1/models

Gets a list of available models.

Reference: https://elevenlabs.io/docs/api-reference/models/list


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List models
  version: endpoint_models.list
paths:
  /v1/models:
    get:
      operationId: list
      summary: List models
      description: Gets a list of available models.
      tags:
        - - subpackage_models
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
                type: array
                items:
                  $ref: '#/components/schemas/ModelResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    LanguageResponseModel:
      type: object
      properties:
        language_id:
          type: string
        name:
          type: string
      required:
        - language_id
        - name
    ModelRatesResponseModel:
      type: object
      properties:
        character_cost_multiplier:
          type: number
          format: double
      required:
        - character_cost_multiplier
    ModelResponseModel:
      type: object
      properties:
        model_id:
          type: string
        name:
          type: string
        can_be_finetuned:
          type: boolean
        can_do_text_to_speech:
          type: boolean
        can_do_voice_conversion:
          type: boolean
        can_use_style:
          type: boolean
        can_use_speaker_boost:
          type: boolean
        serves_pro_voices:
          type: boolean
        token_cost_factor:
          type: number
          format: double
        description:
          type: string
        requires_alpha_access:
          type: boolean
        max_characters_request_free_user:
          type: integer
        max_characters_request_subscribed_user:
          type: integer
        maximum_text_length_per_request:
          type: integer
        languages:
          type: array
          items:
            $ref: '#/components/schemas/LanguageResponseModel'
        model_rates:
          $ref: '#/components/schemas/ModelRatesResponseModel'
        concurrency_group:
          type: string
      required:
        - model_id

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.models.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.models.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/models"

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

url = URI("https://api.elevenlabs.io/v1/models")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/models")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/models', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/models");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/models")! as URL,
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


# Studio API

> Access the Studio API for programmatic control of your video and audio content creation workflow

<Note>
  The Studio API is only available upon request. To get access, [contact
  sales](https://elevenlabs.io/contact-sales).
</Note>



# List Studio Projects

GET https://api.elevenlabs.io/v1/studio/projects

Returns a list of your Studio projects with metadata.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-projects


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List Studio Projects
  version: endpoint_studio/projects.list
paths:
  /v1/studio/projects:
    get:
      operationId: list
      summary: List Studio Projects
      description: Returns a list of your Studio projects with metadata.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
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
                $ref: '#/components/schemas/GetProjectsResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    ProjectResponseModelTargetAudience:
      type: string
      enum:
        - value: children
        - value: young adult
        - value: adult
        - value: all ages
    ProjectState:
      type: string
      enum:
        - value: creating
        - value: default
        - value: converting
        - value: in_queue
    ProjectResponseModelAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ProjectResponseModelFiction:
      type: string
      enum:
        - value: fiction
        - value: non-fiction
    ProjectCreationMetaResponseModelStatus:
      type: string
      enum:
        - value: pending
        - value: creating
        - value: finished
        - value: failed
    ProjectCreationMetaResponseModelType:
      type: string
      enum:
        - value: blank
        - value: generate_podcast
        - value: auto_assign_voices
    ProjectCreationMetaResponseModel:
      type: object
      properties:
        creation_progress:
          type: number
          format: double
        status:
          $ref: '#/components/schemas/ProjectCreationMetaResponseModelStatus'
        type:
          $ref: '#/components/schemas/ProjectCreationMetaResponseModelType'
      required:
        - creation_progress
        - status
        - type
    ProjectResponseModelSourceType:
      type: string
      enum:
        - value: blank
        - value: book
        - value: article
        - value: genfm
        - value: video
    CaptionStyleTemplateModel:
      type: object
      properties:
        key:
          type: string
        label:
          type: string
        requires_high_fps:
          type: boolean
      required:
        - key
        - label
    CaptionStyleModelTextAlign:
      type: string
      enum:
        - value: start
        - value: center
        - value: end
    CaptionStyleModelTextStyle:
      type: string
      enum:
        - value: normal
        - value: italic
    CaptionStyleModelTextWeight:
      type: string
      enum:
        - value: normal
        - value: bold
    CaptionStyleSectionAnimationModelEnterType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleSectionAnimationModelExitType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleSectionAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleSectionAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleSectionAnimationModelExitType'
      required:
        - enter_type
        - exit_type
    CaptionStyleWordAnimationModelEnterType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleWordAnimationModelExitType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleWordAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleWordAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleWordAnimationModelExitType'
      required:
        - enter_type
        - exit_type
    CaptionStyleCharacterAnimationModelEnterType:
      type: string
      enum:
        - value: none
        - value: fade
    CaptionStyleCharacterAnimationModelExitType:
      type: string
      enum:
        - value: none
        - value: fade
    CaptionStyleCharacterAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleCharacterAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleCharacterAnimationModelExitType'
      required:
        - enter_type
        - exit_type
    CaptionStyleHorizontalPlacementModelAlign:
      type: string
      enum:
        - value: left
        - value: center
        - value: right
    CaptionStyleHorizontalPlacementModel:
      type: object
      properties:
        align:
          $ref: '#/components/schemas/CaptionStyleHorizontalPlacementModelAlign'
        translate_pct:
          type: number
          format: double
      required:
        - align
        - translate_pct
    CaptionStyleVerticalPlacementModelAlign:
      type: string
      enum:
        - value: top
        - value: center
        - value: bottom
    CaptionStyleVerticalPlacementModel:
      type: object
      properties:
        align:
          $ref: '#/components/schemas/CaptionStyleVerticalPlacementModelAlign'
        translate_pct:
          type: number
          format: double
      required:
        - align
        - translate_pct
    CaptionStyleModel:
      type: object
      properties:
        template:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleTemplateModel'
            - type: 'null'
        text_font:
          type:
            - string
            - 'null'
        text_scale:
          type:
            - number
            - 'null'
          format: double
        text_color:
          type:
            - string
            - 'null'
        text_align:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextAlign'
            - type: 'null'
        text_style:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextStyle'
            - type: 'null'
        text_weight:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextWeight'
            - type: 'null'
        background_enabled:
          type:
            - boolean
            - 'null'
        background_color:
          type:
            - string
            - 'null'
        background_opacity:
          type:
            - number
            - 'null'
          format: double
        word_highlights_enabled:
          type:
            - boolean
            - 'null'
        word_highlights_color:
          type:
            - string
            - 'null'
        word_highlights_background_color:
          type:
            - string
            - 'null'
        word_highlights_opacity:
          type:
            - number
            - 'null'
          format: double
        section_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleSectionAnimationModel'
            - type: 'null'
        word_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleWordAnimationModel'
            - type: 'null'
        character_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleCharacterAnimationModel'
            - type: 'null'
        width_pct:
          type:
            - number
            - 'null'
          format: double
        horizontal_placement:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleHorizontalPlacementModel'
            - type: 'null'
        vertical_placement:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleVerticalPlacementModel'
            - type: 'null'
        auto_break_enabled:
          type:
            - boolean
            - 'null'
        max_lines_per_section:
          type:
            - integer
            - 'null'
        max_words_per_line:
          type:
            - integer
            - 'null'
    ProjectResponseModelAspectRatio:
      type: string
      enum:
        - value: '16:9'
        - value: '9:16'
        - value: '4:5'
        - value: '1:1'
    ProjectResponseModel:
      type: object
      properties:
        project_id:
          type: string
        name:
          type: string
        create_date_unix:
          type: integer
        created_by_user_id:
          type:
            - string
            - 'null'
        default_title_voice_id:
          type: string
        default_paragraph_voice_id:
          type: string
        default_model_id:
          type: string
        last_conversion_date_unix:
          type:
            - integer
            - 'null'
        can_be_downloaded:
          type: boolean
        title:
          type:
            - string
            - 'null'
        author:
          type:
            - string
            - 'null'
        description:
          type:
            - string
            - 'null'
        genres:
          type:
            - array
            - 'null'
          items:
            type: string
        cover_image_url:
          type:
            - string
            - 'null'
        target_audience:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelTargetAudience'
            - type: 'null'
        language:
          type:
            - string
            - 'null'
        content_type:
          type:
            - string
            - 'null'
        original_publication_date:
          type:
            - string
            - 'null'
        mature_content:
          type:
            - boolean
            - 'null'
        isbn_number:
          type:
            - string
            - 'null'
        volume_normalization:
          type: boolean
        state:
          $ref: '#/components/schemas/ProjectState'
        access_level:
          $ref: '#/components/schemas/ProjectResponseModelAccessLevel'
        fiction:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelFiction'
            - type: 'null'
        quality_check_on:
          type: boolean
        quality_check_on_when_bulk_convert:
          type: boolean
        creation_meta:
          oneOf:
            - $ref: '#/components/schemas/ProjectCreationMetaResponseModel'
            - type: 'null'
        source_type:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelSourceType'
            - type: 'null'
        chapters_enabled:
          type:
            - boolean
            - 'null'
        captions_enabled:
          type:
            - boolean
            - 'null'
        caption_style:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModel'
            - type: 'null'
        public_share_id:
          type:
            - string
            - 'null'
        aspect_ratio:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelAspectRatio'
            - type: 'null'
      required:
        - project_id
        - name
        - create_date_unix
        - created_by_user_id
        - default_title_voice_id
        - default_paragraph_voice_id
        - default_model_id
        - can_be_downloaded
        - volume_normalization
        - state
        - access_level
        - quality_check_on
        - quality_check_on_when_bulk_convert
    GetProjectsResponseModel:
      type: object
      properties:
        projects:
          type: array
          items:
            $ref: '#/components/schemas/ProjectResponseModel'
      required:
        - projects

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects")! as URL,
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


# Update Studio Project

POST https://api.elevenlabs.io/v1/studio/projects/{project_id}
Content-Type: application/json

Updates the specified Studio project by setting the values of the parameters passed.

Reference: https://elevenlabs.io/docs/api-reference/studio/edit-project


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update Studio Project
  version: endpoint_studio/projects.update
paths:
  /v1/studio/projects/{project_id}:
    post:
      operationId: update
      summary: Update Studio Project
      description: >-
        Updates the specified Studio project by setting the values of the
        parameters passed.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
      parameters:
        - name: project_id
          in: path
          description: >-
            The ID of the project to be used. You can use the [List
            projects](/docs/api-reference/studio/get-projects) endpoint to list
            all the available projects.
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
                $ref: '#/components/schemas/EditProjectResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Update_Studio_project_v1_studio_projects__project_id__post
components:
  schemas:
    Body_Update_Studio_project_v1_studio_projects__project_id__post:
      type: object
      properties:
        name:
          type: string
        default_title_voice_id:
          type: string
        default_paragraph_voice_id:
          type: string
        title:
          type:
            - string
            - 'null'
        author:
          type:
            - string
            - 'null'
        isbn_number:
          type:
            - string
            - 'null'
        volume_normalization:
          type: boolean
      required:
        - name
        - default_title_voice_id
        - default_paragraph_voice_id
    ProjectResponseModelTargetAudience:
      type: string
      enum:
        - value: children
        - value: young adult
        - value: adult
        - value: all ages
    ProjectState:
      type: string
      enum:
        - value: creating
        - value: default
        - value: converting
        - value: in_queue
    ProjectResponseModelAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ProjectResponseModelFiction:
      type: string
      enum:
        - value: fiction
        - value: non-fiction
    ProjectCreationMetaResponseModelStatus:
      type: string
      enum:
        - value: pending
        - value: creating
        - value: finished
        - value: failed
    ProjectCreationMetaResponseModelType:
      type: string
      enum:
        - value: blank
        - value: generate_podcast
        - value: auto_assign_voices
    ProjectCreationMetaResponseModel:
      type: object
      properties:
        creation_progress:
          type: number
          format: double
        status:
          $ref: '#/components/schemas/ProjectCreationMetaResponseModelStatus'
        type:
          $ref: '#/components/schemas/ProjectCreationMetaResponseModelType'
      required:
        - creation_progress
        - status
        - type
    ProjectResponseModelSourceType:
      type: string
      enum:
        - value: blank
        - value: book
        - value: article
        - value: genfm
        - value: video
    CaptionStyleTemplateModel:
      type: object
      properties:
        key:
          type: string
        label:
          type: string
        requires_high_fps:
          type: boolean
      required:
        - key
        - label
    CaptionStyleModelTextAlign:
      type: string
      enum:
        - value: start
        - value: center
        - value: end
    CaptionStyleModelTextStyle:
      type: string
      enum:
        - value: normal
        - value: italic
    CaptionStyleModelTextWeight:
      type: string
      enum:
        - value: normal
        - value: bold
    CaptionStyleSectionAnimationModelEnterType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleSectionAnimationModelExitType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleSectionAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleSectionAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleSectionAnimationModelExitType'
      required:
        - enter_type
        - exit_type
    CaptionStyleWordAnimationModelEnterType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleWordAnimationModelExitType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleWordAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleWordAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleWordAnimationModelExitType'
      required:
        - enter_type
        - exit_type
    CaptionStyleCharacterAnimationModelEnterType:
      type: string
      enum:
        - value: none
        - value: fade
    CaptionStyleCharacterAnimationModelExitType:
      type: string
      enum:
        - value: none
        - value: fade
    CaptionStyleCharacterAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleCharacterAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleCharacterAnimationModelExitType'
      required:
        - enter_type
        - exit_type
    CaptionStyleHorizontalPlacementModelAlign:
      type: string
      enum:
        - value: left
        - value: center
        - value: right
    CaptionStyleHorizontalPlacementModel:
      type: object
      properties:
        align:
          $ref: '#/components/schemas/CaptionStyleHorizontalPlacementModelAlign'
        translate_pct:
          type: number
          format: double
      required:
        - align
        - translate_pct
    CaptionStyleVerticalPlacementModelAlign:
      type: string
      enum:
        - value: top
        - value: center
        - value: bottom
    CaptionStyleVerticalPlacementModel:
      type: object
      properties:
        align:
          $ref: '#/components/schemas/CaptionStyleVerticalPlacementModelAlign'
        translate_pct:
          type: number
          format: double
      required:
        - align
        - translate_pct
    CaptionStyleModel:
      type: object
      properties:
        template:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleTemplateModel'
            - type: 'null'
        text_font:
          type:
            - string
            - 'null'
        text_scale:
          type:
            - number
            - 'null'
          format: double
        text_color:
          type:
            - string
            - 'null'
        text_align:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextAlign'
            - type: 'null'
        text_style:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextStyle'
            - type: 'null'
        text_weight:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextWeight'
            - type: 'null'
        background_enabled:
          type:
            - boolean
            - 'null'
        background_color:
          type:
            - string
            - 'null'
        background_opacity:
          type:
            - number
            - 'null'
          format: double
        word_highlights_enabled:
          type:
            - boolean
            - 'null'
        word_highlights_color:
          type:
            - string
            - 'null'
        word_highlights_background_color:
          type:
            - string
            - 'null'
        word_highlights_opacity:
          type:
            - number
            - 'null'
          format: double
        section_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleSectionAnimationModel'
            - type: 'null'
        word_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleWordAnimationModel'
            - type: 'null'
        character_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleCharacterAnimationModel'
            - type: 'null'
        width_pct:
          type:
            - number
            - 'null'
          format: double
        horizontal_placement:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleHorizontalPlacementModel'
            - type: 'null'
        vertical_placement:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleVerticalPlacementModel'
            - type: 'null'
        auto_break_enabled:
          type:
            - boolean
            - 'null'
        max_lines_per_section:
          type:
            - integer
            - 'null'
        max_words_per_line:
          type:
            - integer
            - 'null'
    ProjectResponseModelAspectRatio:
      type: string
      enum:
        - value: '16:9'
        - value: '9:16'
        - value: '4:5'
        - value: '1:1'
    ProjectResponseModel:
      type: object
      properties:
        project_id:
          type: string
        name:
          type: string
        create_date_unix:
          type: integer
        created_by_user_id:
          type:
            - string
            - 'null'
        default_title_voice_id:
          type: string
        default_paragraph_voice_id:
          type: string
        default_model_id:
          type: string
        last_conversion_date_unix:
          type:
            - integer
            - 'null'
        can_be_downloaded:
          type: boolean
        title:
          type:
            - string
            - 'null'
        author:
          type:
            - string
            - 'null'
        description:
          type:
            - string
            - 'null'
        genres:
          type:
            - array
            - 'null'
          items:
            type: string
        cover_image_url:
          type:
            - string
            - 'null'
        target_audience:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelTargetAudience'
            - type: 'null'
        language:
          type:
            - string
            - 'null'
        content_type:
          type:
            - string
            - 'null'
        original_publication_date:
          type:
            - string
            - 'null'
        mature_content:
          type:
            - boolean
            - 'null'
        isbn_number:
          type:
            - string
            - 'null'
        volume_normalization:
          type: boolean
        state:
          $ref: '#/components/schemas/ProjectState'
        access_level:
          $ref: '#/components/schemas/ProjectResponseModelAccessLevel'
        fiction:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelFiction'
            - type: 'null'
        quality_check_on:
          type: boolean
        quality_check_on_when_bulk_convert:
          type: boolean
        creation_meta:
          oneOf:
            - $ref: '#/components/schemas/ProjectCreationMetaResponseModel'
            - type: 'null'
        source_type:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelSourceType'
            - type: 'null'
        chapters_enabled:
          type:
            - boolean
            - 'null'
        captions_enabled:
          type:
            - boolean
            - 'null'
        caption_style:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModel'
            - type: 'null'
        public_share_id:
          type:
            - string
            - 'null'
        aspect_ratio:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelAspectRatio'
            - type: 'null'
      required:
        - project_id
        - name
        - create_date_unix
        - created_by_user_id
        - default_title_voice_id
        - default_paragraph_voice_id
        - default_model_id
        - can_be_downloaded
        - volume_normalization
        - state
        - access_level
        - quality_check_on
        - quality_check_on_when_bulk_convert
    EditProjectResponseModel:
      type: object
      properties:
        project:
          $ref: '#/components/schemas/ProjectResponseModel'
      required:
        - project

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.update("project_id", {
        name: "Project 1",
        defaultTitleVoiceId: "21m00Tcm4TlvDq8ikWAM",
        defaultParagraphVoiceId: "21m00Tcm4TlvDq8ikWAM",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.update(
    project_id="project_id",
    name="Project 1",
    default_title_voice_id="21m00Tcm4TlvDq8ikWAM",
    default_paragraph_voice_id="21m00Tcm4TlvDq8ikWAM"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id"

	payload := strings.NewReader("{\n  \"name\": \"Project 1\",\n  \"default_title_voice_id\": \"21m00Tcm4TlvDq8ikWAM\",\n  \"default_paragraph_voice_id\": \"21m00Tcm4TlvDq8ikWAM\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Project 1\",\n  \"default_title_voice_id\": \"21m00Tcm4TlvDq8ikWAM\",\n  \"default_paragraph_voice_id\": \"21m00Tcm4TlvDq8ikWAM\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Project 1\",\n  \"default_title_voice_id\": \"21m00Tcm4TlvDq8ikWAM\",\n  \"default_paragraph_voice_id\": \"21m00Tcm4TlvDq8ikWAM\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id', [
  'body' => '{
  "name": "Project 1",
  "default_title_voice_id": "21m00Tcm4TlvDq8ikWAM",
  "default_paragraph_voice_id": "21m00Tcm4TlvDq8ikWAM"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Project 1\",\n  \"default_title_voice_id\": \"21m00Tcm4TlvDq8ikWAM\",\n  \"default_paragraph_voice_id\": \"21m00Tcm4TlvDq8ikWAM\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "name": "Project 1",
  "default_title_voice_id": "21m00Tcm4TlvDq8ikWAM",
  "default_paragraph_voice_id": "21m00Tcm4TlvDq8ikWAM"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id")! as URL,
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


# Get Studio Project

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}

Returns information about a specific Studio project. This endpoint returns more detailed information about a project than `GET /v1/studio`.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-project


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Studio Project
  version: endpoint_studio/projects.get
paths:
  /v1/studio/projects/{project_id}:
    get:
      operationId: get
      summary: Get Studio Project
      description: >-
        Returns information about a specific Studio project. This endpoint
        returns more detailed information about a project than `GET /v1/studio`.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
      parameters:
        - name: project_id
          in: path
          description: >-
            The ID of the project to be used. You can use the [List
            projects](/docs/api-reference/studio/get-projects) endpoint to list
            all the available projects.
          required: true
          schema:
            type: string
        - name: share_id
          in: query
          description: The share ID of the project
          required: false
          schema:
            type:
              - string
              - 'null'
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
                $ref: '#/components/schemas/ProjectExtendedResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    ProjectExtendedResponseModelTargetAudience:
      type: string
      enum:
        - value: children
        - value: young adult
        - value: adult
        - value: all ages
    ProjectState:
      type: string
      enum:
        - value: creating
        - value: default
        - value: converting
        - value: in_queue
    ProjectExtendedResponseModelAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ProjectExtendedResponseModelFiction:
      type: string
      enum:
        - value: fiction
        - value: non-fiction
    ProjectCreationMetaResponseModelStatus:
      type: string
      enum:
        - value: pending
        - value: creating
        - value: finished
        - value: failed
    ProjectCreationMetaResponseModelType:
      type: string
      enum:
        - value: blank
        - value: generate_podcast
        - value: auto_assign_voices
    ProjectCreationMetaResponseModel:
      type: object
      properties:
        creation_progress:
          type: number
          format: double
        status:
          $ref: '#/components/schemas/ProjectCreationMetaResponseModelStatus'
        type:
          $ref: '#/components/schemas/ProjectCreationMetaResponseModelType'
      required:
        - creation_progress
        - status
        - type
    ProjectExtendedResponseModelSourceType:
      type: string
      enum:
        - value: blank
        - value: book
        - value: article
        - value: genfm
        - value: video
    CaptionStyleTemplateModel:
      type: object
      properties:
        key:
          type: string
        label:
          type: string
        requires_high_fps:
          type: boolean
      required:
        - key
        - label
    CaptionStyleModelTextAlign:
      type: string
      enum:
        - value: start
        - value: center
        - value: end
    CaptionStyleModelTextStyle:
      type: string
      enum:
        - value: normal
        - value: italic
    CaptionStyleModelTextWeight:
      type: string
      enum:
        - value: normal
        - value: bold
    CaptionStyleSectionAnimationModelEnterType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleSectionAnimationModelExitType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleSectionAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleSectionAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleSectionAnimationModelExitType'
      required:
        - enter_type
        - exit_type
    CaptionStyleWordAnimationModelEnterType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleWordAnimationModelExitType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleWordAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleWordAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleWordAnimationModelExitType'
      required:
        - enter_type
        - exit_type
    CaptionStyleCharacterAnimationModelEnterType:
      type: string
      enum:
        - value: none
        - value: fade
    CaptionStyleCharacterAnimationModelExitType:
      type: string
      enum:
        - value: none
        - value: fade
    CaptionStyleCharacterAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleCharacterAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleCharacterAnimationModelExitType'
      required:
        - enter_type
        - exit_type
    CaptionStyleHorizontalPlacementModelAlign:
      type: string
      enum:
        - value: left
        - value: center
        - value: right
    CaptionStyleHorizontalPlacementModel:
      type: object
      properties:
        align:
          $ref: '#/components/schemas/CaptionStyleHorizontalPlacementModelAlign'
        translate_pct:
          type: number
          format: double
      required:
        - align
        - translate_pct
    CaptionStyleVerticalPlacementModelAlign:
      type: string
      enum:
        - value: top
        - value: center
        - value: bottom
    CaptionStyleVerticalPlacementModel:
      type: object
      properties:
        align:
          $ref: '#/components/schemas/CaptionStyleVerticalPlacementModelAlign'
        translate_pct:
          type: number
          format: double
      required:
        - align
        - translate_pct
    CaptionStyleModel:
      type: object
      properties:
        template:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleTemplateModel'
            - type: 'null'
        text_font:
          type:
            - string
            - 'null'
        text_scale:
          type:
            - number
            - 'null'
          format: double
        text_color:
          type:
            - string
            - 'null'
        text_align:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextAlign'
            - type: 'null'
        text_style:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextStyle'
            - type: 'null'
        text_weight:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextWeight'
            - type: 'null'
        background_enabled:
          type:
            - boolean
            - 'null'
        background_color:
          type:
            - string
            - 'null'
        background_opacity:
          type:
            - number
            - 'null'
          format: double
        word_highlights_enabled:
          type:
            - boolean
            - 'null'
        word_highlights_color:
          type:
            - string
            - 'null'
        word_highlights_background_color:
          type:
            - string
            - 'null'
        word_highlights_opacity:
          type:
            - number
            - 'null'
          format: double
        section_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleSectionAnimationModel'
            - type: 'null'
        word_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleWordAnimationModel'
            - type: 'null'
        character_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleCharacterAnimationModel'
            - type: 'null'
        width_pct:
          type:
            - number
            - 'null'
          format: double
        horizontal_placement:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleHorizontalPlacementModel'
            - type: 'null'
        vertical_placement:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleVerticalPlacementModel'
            - type: 'null'
        auto_break_enabled:
          type:
            - boolean
            - 'null'
        max_lines_per_section:
          type:
            - integer
            - 'null'
        max_words_per_line:
          type:
            - integer
            - 'null'
    ProjectExtendedResponseModelAspectRatio:
      type: string
      enum:
        - value: '16:9'
        - value: '9:16'
        - value: '4:5'
        - value: '1:1'
    ProjectExtendedResponseModelQualityPreset:
      type: string
      enum:
        - value: standard
        - value: high
        - value: highest
        - value: ultra
        - value: ultra_lossless
    ChapterState:
      type: string
      enum:
        - value: default
        - value: converting
    ChapterStatisticsResponseModel:
      type: object
      properties:
        characters_unconverted:
          type: integer
        characters_converted:
          type: integer
        paragraphs_converted:
          type: integer
        paragraphs_unconverted:
          type: integer
      required:
        - characters_unconverted
        - characters_converted
        - paragraphs_converted
        - paragraphs_unconverted
    ChapterResponseModel:
      type: object
      properties:
        chapter_id:
          type: string
        name:
          type: string
        last_conversion_date_unix:
          type:
            - integer
            - 'null'
        conversion_progress:
          type:
            - number
            - 'null'
          format: double
        can_be_downloaded:
          type: boolean
        state:
          $ref: '#/components/schemas/ChapterState'
        has_video:
          type:
            - boolean
            - 'null'
        statistics:
          oneOf:
            - $ref: '#/components/schemas/ChapterStatisticsResponseModel'
            - type: 'null'
        last_conversion_error:
          type:
            - string
            - 'null'
      required:
        - chapter_id
        - name
        - can_be_downloaded
        - state
    PronunciationDictionaryVersionResponseModelPermissionOnResource:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    PronunciationDictionaryVersionResponseModel:
      type: object
      properties:
        version_id:
          type: string
        version_rules_num:
          type: integer
        pronunciation_dictionary_id:
          type: string
        dictionary_name:
          type: string
        version_name:
          type: string
        permission_on_resource:
          oneOf:
            - $ref: >-
                #/components/schemas/PronunciationDictionaryVersionResponseModelPermissionOnResource
            - type: 'null'
        created_by:
          type: string
        creation_time_unix:
          type: integer
        archived_time_unix:
          type:
            - integer
            - 'null'
      required:
        - version_id
        - version_rules_num
        - pronunciation_dictionary_id
        - dictionary_name
        - version_name
        - permission_on_resource
        - created_by
        - creation_time_unix
    PronunciationDictionaryLocatorResponseModel:
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
        - version_id
    ProjectExtendedResponseModelApplyTextNormalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
        - value: apply_english
    ProjectExtendedResponseModelExperimental:
      type: object
      properties: {}
    ProjectVideoThumbnailSheetResponseModel:
      type: object
      properties:
        start_thumbnail_index:
          type: integer
        thumbnail_count:
          type: integer
        signed_cloud_url:
          type: string
      required:
        - start_thumbnail_index
        - thumbnail_count
        - signed_cloud_url
    ProjectVideoResponseModel:
      type: object
      properties:
        video_id:
          type: string
        filename:
          type: string
        signed_url:
          type: string
        signed_preview_url:
          type:
            - string
            - 'null'
        offset_ms:
          type: integer
        duration_ms:
          type: integer
        volume_gain_db:
          type: number
          format: double
        muted:
          type: boolean
        width:
          type: integer
        height:
          type: integer
        codec:
          type: string
        order:
          type: string
        preview_job_progress:
          type: number
          format: double
        created_at_ms:
          type: integer
        updated_at_ms:
          type: integer
        error:
          type:
            - string
            - 'null'
        thumbnail_interval_seconds:
          type: number
          format: double
        thumbnail_size:
          type: array
          items:
            type: integer
        thumbnail_sheets:
          type: array
          items:
            $ref: '#/components/schemas/ProjectVideoThumbnailSheetResponseModel'
        start_time_ms:
          type: integer
        end_time_ms:
          type: integer
        asset_preview_signed_url:
          type:
            - string
            - 'null'
        source_video_id:
          type:
            - string
            - 'null'
        source_asset_id:
          type:
            - string
            - 'null'
        pending_block_ids:
          type: array
          items:
            type: string
        import_speech_progress:
          type:
            - number
            - 'null'
          format: double
        speech_imported:
          type: boolean
        current_snapshot_id:
          type:
            - string
            - 'null'
        type:
          type: string
          enum:
            - type: stringLiteral
              value: video
      required:
        - video_id
        - filename
        - signed_url
        - signed_preview_url
        - offset_ms
        - duration_ms
        - volume_gain_db
        - muted
        - width
        - height
        - codec
        - order
        - preview_job_progress
        - created_at_ms
        - updated_at_ms
        - thumbnail_interval_seconds
        - thumbnail_size
        - thumbnail_sheets
        - start_time_ms
        - end_time_ms
        - pending_block_ids
    ProjectExternalAudioResponseModel:
      type: object
      properties:
        external_audio_id:
          type: string
        filename:
          type: string
        signed_url:
          type: string
        offset_ms:
          type: integer
        duration_ms:
          type: integer
        start_time_ms:
          type: integer
        end_time_ms:
          type: integer
        order:
          type: string
        track_id:
          type: string
        created_at_ms:
          type: integer
        updated_at_ms:
          type: integer
        volume_gain_db:
          type: number
          format: double
        muted:
          type: boolean
        fade_in_ms:
          type: integer
        fade_out_ms:
          type: integer
        source_external_audio_id:
          type:
            - string
            - 'null'
        source_asset_id:
          type:
            - string
            - 'null'
        pending_block_ids:
          type: array
          items:
            type: string
        import_speech_progress:
          type:
            - number
            - 'null'
          format: double
        speech_imported:
          type: boolean
        current_snapshot_id:
          type:
            - string
            - 'null'
        type:
          type: string
          enum:
            - type: stringLiteral
              value: audio
      required:
        - external_audio_id
        - filename
        - signed_url
        - offset_ms
        - duration_ms
        - start_time_ms
        - end_time_ms
        - order
        - track_id
        - created_at_ms
        - updated_at_ms
        - pending_block_ids
    ProjectExtendedResponseModelAssetsItems:
      oneOf:
        - $ref: '#/components/schemas/ProjectVideoResponseModel'
        - $ref: '#/components/schemas/ProjectExternalAudioResponseModel'
    ProjectExtendedResponseModel:
      type: object
      properties:
        project_id:
          type: string
        name:
          type: string
        create_date_unix:
          type: integer
        created_by_user_id:
          type:
            - string
            - 'null'
        default_title_voice_id:
          type: string
        default_paragraph_voice_id:
          type: string
        default_model_id:
          type: string
        last_conversion_date_unix:
          type:
            - integer
            - 'null'
        can_be_downloaded:
          type: boolean
        title:
          type:
            - string
            - 'null'
        author:
          type:
            - string
            - 'null'
        description:
          type:
            - string
            - 'null'
        genres:
          type:
            - array
            - 'null'
          items:
            type: string
        cover_image_url:
          type:
            - string
            - 'null'
        target_audience:
          oneOf:
            - $ref: '#/components/schemas/ProjectExtendedResponseModelTargetAudience'
            - type: 'null'
        language:
          type:
            - string
            - 'null'
        content_type:
          type:
            - string
            - 'null'
        original_publication_date:
          type:
            - string
            - 'null'
        mature_content:
          type:
            - boolean
            - 'null'
        isbn_number:
          type:
            - string
            - 'null'
        volume_normalization:
          type: boolean
        state:
          $ref: '#/components/schemas/ProjectState'
        access_level:
          $ref: '#/components/schemas/ProjectExtendedResponseModelAccessLevel'
        fiction:
          oneOf:
            - $ref: '#/components/schemas/ProjectExtendedResponseModelFiction'
            - type: 'null'
        quality_check_on:
          type: boolean
        quality_check_on_when_bulk_convert:
          type: boolean
        creation_meta:
          oneOf:
            - $ref: '#/components/schemas/ProjectCreationMetaResponseModel'
            - type: 'null'
        source_type:
          oneOf:
            - $ref: '#/components/schemas/ProjectExtendedResponseModelSourceType'
            - type: 'null'
        chapters_enabled:
          type:
            - boolean
            - 'null'
        captions_enabled:
          type:
            - boolean
            - 'null'
        caption_style:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModel'
            - type: 'null'
        public_share_id:
          type:
            - string
            - 'null'
        aspect_ratio:
          oneOf:
            - $ref: '#/components/schemas/ProjectExtendedResponseModelAspectRatio'
            - type: 'null'
        quality_preset:
          $ref: '#/components/schemas/ProjectExtendedResponseModelQualityPreset'
        chapters:
          type: array
          items:
            $ref: '#/components/schemas/ChapterResponseModel'
        pronunciation_dictionary_versions:
          type: array
          items:
            $ref: '#/components/schemas/PronunciationDictionaryVersionResponseModel'
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: '#/components/schemas/PronunciationDictionaryLocatorResponseModel'
        apply_text_normalization:
          $ref: >-
            #/components/schemas/ProjectExtendedResponseModelApplyTextNormalization
        experimental:
          $ref: '#/components/schemas/ProjectExtendedResponseModelExperimental'
        assets:
          type: array
          items:
            $ref: '#/components/schemas/ProjectExtendedResponseModelAssetsItems'
      required:
        - project_id
        - name
        - create_date_unix
        - created_by_user_id
        - default_title_voice_id
        - default_paragraph_voice_id
        - default_model_id
        - can_be_downloaded
        - volume_normalization
        - state
        - access_level
        - quality_check_on
        - quality_check_on_when_bulk_convert
        - quality_preset
        - chapters
        - pronunciation_dictionary_versions
        - pronunciation_dictionary_locators
        - apply_text_normalization
        - assets

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.get("project_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.get(
    project_id="project_id"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id")! as URL,
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


# Create Studio Project

POST https://api.elevenlabs.io/v1/studio/projects
Content-Type: multipart/form-data

Creates a new Studio project, it can be either initialized as blank, from a document or from a URL.

Reference: https://elevenlabs.io/docs/api-reference/studio/add-project


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create Studio Project
  version: endpoint_studio/projects.create
paths:
  /v1/studio/projects:
    post:
      operationId: create
      summary: Create Studio Project
      description: >-
        Creates a new Studio project, it can be either initialized as blank,
        from a document or from a URL.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
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
                $ref: '#/components/schemas/AddProjectResponseModel'
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
                default_title_voice_id:
                  type:
                    - string
                    - 'null'
                default_paragraph_voice_id:
                  type:
                    - string
                    - 'null'
                default_model_id:
                  type:
                    - string
                    - 'null'
                from_url:
                  type:
                    - string
                    - 'null'
                from_content_json:
                  type: string
                quality_preset:
                  type: string
                title:
                  type:
                    - string
                    - 'null'
                author:
                  type:
                    - string
                    - 'null'
                description:
                  type:
                    - string
                    - 'null'
                genres:
                  type: array
                  items:
                    type: string
                target_audience:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaTargetAudience
                    - type: 'null'
                language:
                  type:
                    - string
                    - 'null'
                content_type:
                  type:
                    - string
                    - 'null'
                original_publication_date:
                  type:
                    - string
                    - 'null'
                mature_content:
                  type:
                    - boolean
                    - 'null'
                isbn_number:
                  type:
                    - string
                    - 'null'
                acx_volume_normalization:
                  type: boolean
                volume_normalization:
                  type: boolean
                pronunciation_dictionary_locators:
                  type: array
                  items:
                    type: string
                callback_url:
                  type:
                    - string
                    - 'null'
                fiction:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaFiction
                    - type: 'null'
                apply_text_normalization:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaApplyTextNormalization
                    - type: 'null'
                auto_convert:
                  type: boolean
                auto_assign_voices:
                  type:
                    - boolean
                    - 'null'
                source_type:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaSourceType
                    - type: 'null'
components:
  schemas:
    V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaTargetAudience:
      type: string
      enum:
        - value: children
        - value: young adult
        - value: adult
        - value: all ages
    V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaFiction:
      type: string
      enum:
        - value: fiction
        - value: non-fiction
    V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaApplyTextNormalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
        - value: apply_english
    V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaSourceType:
      type: string
      enum:
        - value: blank
        - value: book
        - value: article
        - value: genfm
        - value: video
    ProjectResponseModelTargetAudience:
      type: string
      enum:
        - value: children
        - value: young adult
        - value: adult
        - value: all ages
    ProjectState:
      type: string
      enum:
        - value: creating
        - value: default
        - value: converting
        - value: in_queue
    ProjectResponseModelAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ProjectResponseModelFiction:
      type: string
      enum:
        - value: fiction
        - value: non-fiction
    ProjectCreationMetaResponseModelStatus:
      type: string
      enum:
        - value: pending
        - value: creating
        - value: finished
        - value: failed
    ProjectCreationMetaResponseModelType:
      type: string
      enum:
        - value: blank
        - value: generate_podcast
        - value: auto_assign_voices
    ProjectCreationMetaResponseModel:
      type: object
      properties:
        creation_progress:
          type: number
          format: double
        status:
          $ref: '#/components/schemas/ProjectCreationMetaResponseModelStatus'
        type:
          $ref: '#/components/schemas/ProjectCreationMetaResponseModelType'
      required:
        - creation_progress
        - status
        - type
    ProjectResponseModelSourceType:
      type: string
      enum:
        - value: blank
        - value: book
        - value: article
        - value: genfm
        - value: video
    CaptionStyleTemplateModel:
      type: object
      properties:
        key:
          type: string
        label:
          type: string
        requires_high_fps:
          type: boolean
      required:
        - key
        - label
    CaptionStyleModelTextAlign:
      type: string
      enum:
        - value: start
        - value: center
        - value: end
    CaptionStyleModelTextStyle:
      type: string
      enum:
        - value: normal
        - value: italic
    CaptionStyleModelTextWeight:
      type: string
      enum:
        - value: normal
        - value: bold
    CaptionStyleSectionAnimationModelEnterType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleSectionAnimationModelExitType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleSectionAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleSectionAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleSectionAnimationModelExitType'
      required:
        - enter_type
        - exit_type
    CaptionStyleWordAnimationModelEnterType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleWordAnimationModelExitType:
      type: string
      enum:
        - value: none
        - value: fade
        - value: scale
    CaptionStyleWordAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleWordAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleWordAnimationModelExitType'
      required:
        - enter_type
        - exit_type
    CaptionStyleCharacterAnimationModelEnterType:
      type: string
      enum:
        - value: none
        - value: fade
    CaptionStyleCharacterAnimationModelExitType:
      type: string
      enum:
        - value: none
        - value: fade
    CaptionStyleCharacterAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleCharacterAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleCharacterAnimationModelExitType'
      required:
        - enter_type
        - exit_type
    CaptionStyleHorizontalPlacementModelAlign:
      type: string
      enum:
        - value: left
        - value: center
        - value: right
    CaptionStyleHorizontalPlacementModel:
      type: object
      properties:
        align:
          $ref: '#/components/schemas/CaptionStyleHorizontalPlacementModelAlign'
        translate_pct:
          type: number
          format: double
      required:
        - align
        - translate_pct
    CaptionStyleVerticalPlacementModelAlign:
      type: string
      enum:
        - value: top
        - value: center
        - value: bottom
    CaptionStyleVerticalPlacementModel:
      type: object
      properties:
        align:
          $ref: '#/components/schemas/CaptionStyleVerticalPlacementModelAlign'
        translate_pct:
          type: number
          format: double
      required:
        - align
        - translate_pct
    CaptionStyleModel:
      type: object
      properties:
        template:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleTemplateModel'
            - type: 'null'
        text_font:
          type:
            - string
            - 'null'
        text_scale:
          type:
            - number
            - 'null'
          format: double
        text_color:
          type:
            - string
            - 'null'
        text_align:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextAlign'
            - type: 'null'
        text_style:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextStyle'
            - type: 'null'
        text_weight:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextWeight'
            - type: 'null'
        background_enabled:
          type:
            - boolean
            - 'null'
        background_color:
          type:
            - string
            - 'null'
        background_opacity:
          type:
            - number
            - 'null'
          format: double
        word_highlights_enabled:
          type:
            - boolean
            - 'null'
        word_highlights_color:
          type:
            - string
            - 'null'
        word_highlights_background_color:
          type:
            - string
            - 'null'
        word_highlights_opacity:
          type:
            - number
            - 'null'
          format: double
        section_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleSectionAnimationModel'
            - type: 'null'
        word_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleWordAnimationModel'
            - type: 'null'
        character_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleCharacterAnimationModel'
            - type: 'null'
        width_pct:
          type:
            - number
            - 'null'
          format: double
        horizontal_placement:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleHorizontalPlacementModel'
            - type: 'null'
        vertical_placement:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleVerticalPlacementModel'
            - type: 'null'
        auto_break_enabled:
          type:
            - boolean
            - 'null'
        max_lines_per_section:
          type:
            - integer
            - 'null'
        max_words_per_line:
          type:
            - integer
            - 'null'
    ProjectResponseModelAspectRatio:
      type: string
      enum:
        - value: '16:9'
        - value: '9:16'
        - value: '4:5'
        - value: '1:1'
    ProjectResponseModel:
      type: object
      properties:
        project_id:
          type: string
        name:
          type: string
        create_date_unix:
          type: integer
        created_by_user_id:
          type:
            - string
            - 'null'
        default_title_voice_id:
          type: string
        default_paragraph_voice_id:
          type: string
        default_model_id:
          type: string
        last_conversion_date_unix:
          type:
            - integer
            - 'null'
        can_be_downloaded:
          type: boolean
        title:
          type:
            - string
            - 'null'
        author:
          type:
            - string
            - 'null'
        description:
          type:
            - string
            - 'null'
        genres:
          type:
            - array
            - 'null'
          items:
            type: string
        cover_image_url:
          type:
            - string
            - 'null'
        target_audience:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelTargetAudience'
            - type: 'null'
        language:
          type:
            - string
            - 'null'
        content_type:
          type:
            - string
            - 'null'
        original_publication_date:
          type:
            - string
            - 'null'
        mature_content:
          type:
            - boolean
            - 'null'
        isbn_number:
          type:
            - string
            - 'null'
        volume_normalization:
          type: boolean
        state:
          $ref: '#/components/schemas/ProjectState'
        access_level:
          $ref: '#/components/schemas/ProjectResponseModelAccessLevel'
        fiction:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelFiction'
            - type: 'null'
        quality_check_on:
          type: boolean
        quality_check_on_when_bulk_convert:
          type: boolean
        creation_meta:
          oneOf:
            - $ref: '#/components/schemas/ProjectCreationMetaResponseModel'
            - type: 'null'
        source_type:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelSourceType'
            - type: 'null'
        chapters_enabled:
          type:
            - boolean
            - 'null'
        captions_enabled:
          type:
            - boolean
            - 'null'
        caption_style:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModel'
            - type: 'null'
        public_share_id:
          type:
            - string
            - 'null'
        aspect_ratio:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelAspectRatio'
            - type: 'null'
      required:
        - project_id
        - name
        - create_date_unix
        - created_by_user_id
        - default_title_voice_id
        - default_paragraph_voice_id
        - default_model_id
        - can_be_downloaded
        - volume_normalization
        - state
        - access_level
        - quality_check_on
        - quality_check_on_when_bulk_convert
    AddProjectResponseModel:
      type: object
      properties:
        project:
          $ref: '#/components/schemas/ProjectResponseModel'
      required:
        - project

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.create({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.create()

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

	url := "https://api.elevenlabs.io/v1/studio/projects"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/studio/projects")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects', [
  'multipart' => [
    [
        'name' => 'name',
        'contents' => 'Project 1'
    ],
    [
        'name' => 'from_document',
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
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
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
    "value": "Project 1"
  ],
  [
    "name": "default_title_voice_id",
    "value": 
  ],
  [
    "name": "default_paragraph_voice_id",
    "value": 
  ],
  [
    "name": "default_model_id",
    "value": 
  ],
  [
    "name": "from_url",
    "value": 
  ],
  [
    "name": "from_document",
    "fileName": "<file1>"
  ],
  [
    "name": "from_content_json",
    "value": 
  ],
  [
    "name": "quality_preset",
    "value": 
  ],
  [
    "name": "title",
    "value": 
  ],
  [
    "name": "author",
    "value": 
  ],
  [
    "name": "description",
    "value": 
  ],
  [
    "name": "genres",
    "value": 
  ],
  [
    "name": "target_audience",
    "value": 
  ],
  [
    "name": "language",
    "value": 
  ],
  [
    "name": "content_type",
    "value": 
  ],
  [
    "name": "original_publication_date",
    "value": 
  ],
  [
    "name": "mature_content",
    "value": 
  ],
  [
    "name": "isbn_number",
    "value": 
  ],
  [
    "name": "acx_volume_normalization",
    "value": 
  ],
  [
    "name": "volume_normalization",
    "value": 
  ],
  [
    "name": "pronunciation_dictionary_locators",
    "value": 
  ],
  [
    "name": "callback_url",
    "value": 
  ],
  [
    "name": "fiction",
    "value": 
  ],
  [
    "name": "apply_text_normalization",
    "value": 
  ],
  [
    "name": "auto_convert",
    "value": 
  ],
  [
    "name": "auto_assign_voices",
    "value": 
  ],
  [
    "name": "source_type",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects")! as URL,
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
**Navigation:** [← Previous](./37-list-voices.md) | [Index](./index.md) | [Next →](./39-delete-studio-project.md)
