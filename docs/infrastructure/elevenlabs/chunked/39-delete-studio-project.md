**Navigation:** [← Previous](./38-get-history-item.md) | [Index](./index.md) | [Next →](./40-create-pronunciation-dictionaries.md)

# Delete Studio Project

DELETE https://api.elevenlabs.io/v1/studio/projects/{project_id}

Deletes a Studio project.

Reference: https://elevenlabs.io/docs/api-reference/studio/delete-project


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete Studio Project
  version: endpoint_studio/projects.delete
paths:
  /v1/studio/projects/{project_id}:
    delete:
      operationId: delete
      summary: Delete Studio Project
      description: Deletes a Studio project.
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
                $ref: '#/components/schemas/DeleteProjectResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    DeleteProjectResponseModel:
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
    await client.studio.projects.delete("project_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.delete(
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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/studio/projects/project_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/studio/projects/project_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id")! as URL,
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


# Convert Studio Project

POST https://api.elevenlabs.io/v1/studio/projects/{project_id}/convert

Starts conversion of a Studio project and all of its chapters.

Reference: https://elevenlabs.io/docs/api-reference/studio/convert-project


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Convert Studio Project
  version: endpoint_studio/projects.convert
paths:
  /v1/studio/projects/{project_id}/convert:
    post:
      operationId: convert
      summary: Convert Studio Project
      description: Starts conversion of a Studio project and all of its chapters.
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
                $ref: '#/components/schemas/ConvertProjectResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    ConvertProjectResponseModel:
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
    await client.studio.projects.convert("project_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.convert(
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/convert"

	req, _ := http.NewRequest("POST", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/convert")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/convert")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/convert', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/convert");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/convert")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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


# Update Studio Project Content

POST https://api.elevenlabs.io/v1/studio/projects/{project_id}/content
Content-Type: multipart/form-data

Updates Studio project content.

Reference: https://elevenlabs.io/docs/api-reference/studio/update-content


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update Studio Project Content
  version: endpoint_studio/projects/content.update
paths:
  /v1/studio/projects/{project_id}/content:
    post:
      operationId: update
      summary: Update Studio Project Content
      description: Updates Studio project content.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/content
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
          multipart/form-data:
            schema:
              type: object
              properties:
                from_url:
                  type:
                    - string
                    - 'null'
                from_content_json:
                  type: string
                auto_convert:
                  type: boolean
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
    await client.studio.projects.content.update("project_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.content.update(
    project_id="project_id"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/content"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/content")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/content")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/content', [
  'multipart' => [
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
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/content");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
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
    "name": "auto_convert",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/content")! as URL,
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


# List Studio Project Snapshots

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}/snapshots

Retrieves a list of snapshots for a Studio project.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-snapshots


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List Studio Project Snapshots
  version: endpoint_studio/projects/snapshots.list
paths:
  /v1/studio/projects/{project_id}/snapshots:
    get:
      operationId: list
      summary: List Studio Project Snapshots
      description: Retrieves a list of snapshots for a Studio project.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/snapshots
      parameters:
        - name: project_id
          in: path
          description: The ID of the Studio project.
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
                $ref: '#/components/schemas/ProjectSnapshotsResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    ProjectSnapshotResponseModelAudioUpload:
      type: object
      properties: {}
    ProjectSnapshotResponseModelZipUpload:
      type: object
      properties: {}
    ProjectSnapshotResponseModel:
      type: object
      properties:
        project_snapshot_id:
          type: string
        project_id:
          type: string
        created_at_unix:
          type: integer
        name:
          type: string
        audio_upload:
          oneOf:
            - $ref: '#/components/schemas/ProjectSnapshotResponseModelAudioUpload'
            - type: 'null'
        zip_upload:
          oneOf:
            - $ref: '#/components/schemas/ProjectSnapshotResponseModelZipUpload'
            - type: 'null'
      required:
        - project_snapshot_id
        - project_id
        - created_at_unix
        - name
    ProjectSnapshotsResponseModel:
      type: object
      properties:
        snapshots:
          type: array
          items:
            $ref: '#/components/schemas/ProjectSnapshotResponseModel'
      required:
        - snapshots

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.snapshots.list("project_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.snapshots.list(
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots")! as URL,
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


# Stream Studio Project Audio

POST https://api.elevenlabs.io/v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}/stream
Content-Type: application/json

Stream the audio from a Studio project snapshot.

Reference: https://elevenlabs.io/docs/api-reference/studio/stream-snapshot


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Stream Studio Project Audio
  version: endpoint_studio/projects/snapshots.stream
paths:
  /v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}/stream:
    post:
      operationId: stream
      summary: Stream Studio Project Audio
      description: Stream the audio from a Studio project snapshot.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/snapshots
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
        - name: project_snapshot_id
          in: path
          description: The ID of the Studio project snapshot.
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
            text/event-stream:
              schema:
                type: string
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Stream_Studio_project_audio_v1_studio_projects__project_id__snapshots__project_snapshot_id__stream_post
components:
  schemas:
    Body_Stream_Studio_project_audio_v1_studio_projects__project_id__snapshots__project_snapshot_id__stream_post:
      type: object
      properties:
        convert_to_mpeg:
          type: boolean

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.snapshots.stream("project_id", "project_snapshot_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.snapshots.stream(
    project_id="project_id",
    project_snapshot_id="project_snapshot_id"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id/stream"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id/stream")

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
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id/stream")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id/stream', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id/stream");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id/stream")! as URL,
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


# Stream Archive With Studio Project Audio

POST https://api.elevenlabs.io/v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}/archive

Returns a compressed archive of the Studio project's audio.

Reference: https://elevenlabs.io/docs/api-reference/studio/archive-snapshot


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Stream Archive With Studio Project Audio
  version: endpoint_studio/projects/snapshots.stream_archive
paths:
  /v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}/archive:
    post:
      operationId: stream-archive
      summary: Stream Archive With Studio Project Audio
      description: Returns a compressed archive of the Studio project's audio.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/snapshots
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
        - name: project_snapshot_id
          in: path
          description: The ID of the Studio project snapshot.
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
          description: Streaming archive data
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
    await client.studio.projects.snapshots.streamArchive("project_id", "project_snapshot_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.snapshots.stream_archive(
    project_id="project_id",
    project_snapshot_id="project_snapshot_id"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id/archive"

	req, _ := http.NewRequest("POST", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id/archive")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id/archive")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id/archive', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id/archive");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id/archive")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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


# List Chapters

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters

Returns a list of a Studio project's chapters.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-chapters


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List Chapters
  version: endpoint_studio/projects/chapters.list
paths:
  /v1/studio/projects/{project_id}/chapters:
    get:
      operationId: list
      summary: List Chapters
      description: Returns a list of a Studio project's chapters.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/chapters
      parameters:
        - name: project_id
          in: path
          description: The ID of the Studio project.
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
                $ref: '#/components/schemas/GetChaptersResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
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
    GetChaptersResponseModel:
      type: object
      properties:
        chapters:
          type: array
          items:
            $ref: '#/components/schemas/ChapterResponseModel'
      required:
        - chapters

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.chapters.list("project_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.chapters.list(
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")! as URL,
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


# Get Chapter

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters/{chapter_id}

Returns information about a specific chapter.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-chapter


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Chapter
  version: endpoint_studio/projects/chapters.get
paths:
  /v1/studio/projects/{project_id}/chapters/{chapter_id}:
    get:
      operationId: get
      summary: Get Chapter
      description: Returns information about a specific chapter.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/chapters
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
        - name: chapter_id
          in: path
          description: >-
            The ID of the chapter to be used. You can use the [List project
            chapters](/docs/api-reference/studio/get-chapters) endpoint to list
            all the available chapters.
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
                $ref: '#/components/schemas/ChapterWithContentResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    ChapterWithContentResponseModelState:
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
    ChapterContentBlockTtsNodeResponseModel:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: tts_node
        voice_id:
          type: string
        text:
          type: string
      required:
        - type
        - voice_id
        - text
    ChapterContentBlockExtendableNodeResponseModel:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: _other
      required:
        - type
    ChapterContentBlockResponseModelNodesItems:
      oneOf:
        - $ref: '#/components/schemas/ChapterContentBlockTtsNodeResponseModel'
        - $ref: '#/components/schemas/ChapterContentBlockExtendableNodeResponseModel'
    ChapterContentBlockResponseModel:
      type: object
      properties:
        block_id:
          type: string
        nodes:
          type: array
          items:
            $ref: '#/components/schemas/ChapterContentBlockResponseModelNodesItems'
      required:
        - block_id
        - nodes
    ChapterContentResponseModel:
      type: object
      properties:
        blocks:
          type: array
          items:
            $ref: '#/components/schemas/ChapterContentBlockResponseModel'
      required:
        - blocks
    ChapterWithContentResponseModel:
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
          $ref: '#/components/schemas/ChapterWithContentResponseModelState'
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
        content:
          $ref: '#/components/schemas/ChapterContentResponseModel'
      required:
        - chapter_id
        - name
        - can_be_downloaded
        - state
        - content

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.chapters.get("project_id", "chapter_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.chapters.get(
    project_id="project_id",
    chapter_id="chapter_id"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")! as URL,
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


# Create Chapter

POST https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters
Content-Type: application/json

Creates a new chapter either as blank or from a URL.

Reference: https://elevenlabs.io/docs/api-reference/studio/add-chapter


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create Chapter
  version: endpoint_studio/projects/chapters.create
paths:
  /v1/studio/projects/{project_id}/chapters:
    post:
      operationId: create
      summary: Create Chapter
      description: Creates a new chapter either as blank or from a URL.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/chapters
      parameters:
        - name: project_id
          in: path
          description: The ID of the Studio project.
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
                $ref: '#/components/schemas/AddChapterResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Create_chapter_v1_studio_projects__project_id__chapters_post
components:
  schemas:
    Body_Create_chapter_v1_studio_projects__project_id__chapters_post:
      type: object
      properties:
        name:
          type: string
        from_url:
          type:
            - string
            - 'null'
      required:
        - name
    ChapterWithContentResponseModelState:
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
    ChapterContentBlockTtsNodeResponseModel:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: tts_node
        voice_id:
          type: string
        text:
          type: string
      required:
        - type
        - voice_id
        - text
    ChapterContentBlockExtendableNodeResponseModel:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: _other
      required:
        - type
    ChapterContentBlockResponseModelNodesItems:
      oneOf:
        - $ref: '#/components/schemas/ChapterContentBlockTtsNodeResponseModel'
        - $ref: '#/components/schemas/ChapterContentBlockExtendableNodeResponseModel'
    ChapterContentBlockResponseModel:
      type: object
      properties:
        block_id:
          type: string
        nodes:
          type: array
          items:
            $ref: '#/components/schemas/ChapterContentBlockResponseModelNodesItems'
      required:
        - block_id
        - nodes
    ChapterContentResponseModel:
      type: object
      properties:
        blocks:
          type: array
          items:
            $ref: '#/components/schemas/ChapterContentBlockResponseModel'
      required:
        - blocks
    ChapterWithContentResponseModel:
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
          $ref: '#/components/schemas/ChapterWithContentResponseModelState'
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
        content:
          $ref: '#/components/schemas/ChapterContentResponseModel'
      required:
        - chapter_id
        - name
        - can_be_downloaded
        - state
        - content
    AddChapterResponseModel:
      type: object
      properties:
        chapter:
          $ref: '#/components/schemas/ChapterWithContentResponseModel'
      required:
        - chapter

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.chapters.create("project_id", {
        name: "Chapter 1",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.chapters.create(
    project_id="project_id",
    name="Chapter 1"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters"

	payload := strings.NewReader("{\n  \"name\": \"Chapter 1\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Chapter 1\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Chapter 1\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters', [
  'body' => '{
  "name": "Chapter 1"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Chapter 1\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["name": "Chapter 1"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")! as URL,
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


# Update Chapter

POST https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters/{chapter_id}
Content-Type: application/json

Updates a chapter.

Reference: https://elevenlabs.io/docs/api-reference/studio/update-chapter


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update Chapter
  version: endpoint_studio/projects/chapters.update
paths:
  /v1/studio/projects/{project_id}/chapters/{chapter_id}:
    post:
      operationId: update
      summary: Update Chapter
      description: Updates a chapter.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/chapters
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
        - name: chapter_id
          in: path
          description: >-
            The ID of the chapter to be used. You can use the [List project
            chapters](/docs/api-reference/studio/get-chapters) endpoint to list
            all the available chapters.
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
                $ref: '#/components/schemas/EditChapterResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Update_chapter_v1_studio_projects__project_id__chapters__chapter_id__post
components:
  schemas:
    ChapterContentBlockInputModelSubType:
      type: string
      enum:
        - value: p
        - value: h1
        - value: h2
        - value: h3
    ChapterContentParagraphTtsNodeInputModel:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: tts_node
        text:
          type: string
        voice_id:
          type: string
      required:
        - type
        - text
        - voice_id
    ChapterContentBlockInputModel:
      type: object
      properties:
        sub_type:
          oneOf:
            - $ref: '#/components/schemas/ChapterContentBlockInputModelSubType'
            - type: 'null'
        nodes:
          type: array
          items:
            $ref: '#/components/schemas/ChapterContentParagraphTtsNodeInputModel'
        block_id:
          type:
            - string
            - 'null'
      required:
        - nodes
    ChapterContentInputModel:
      type: object
      properties:
        blocks:
          type: array
          items:
            $ref: '#/components/schemas/ChapterContentBlockInputModel'
      required:
        - blocks
    Body_Update_chapter_v1_studio_projects__project_id__chapters__chapter_id__post:
      type: object
      properties:
        name:
          type:
            - string
            - 'null'
        content:
          oneOf:
            - $ref: '#/components/schemas/ChapterContentInputModel'
            - type: 'null'
    ChapterWithContentResponseModelState:
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
    ChapterContentBlockTtsNodeResponseModel:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: tts_node
        voice_id:
          type: string
        text:
          type: string
      required:
        - type
        - voice_id
        - text
    ChapterContentBlockExtendableNodeResponseModel:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: _other
      required:
        - type
    ChapterContentBlockResponseModelNodesItems:
      oneOf:
        - $ref: '#/components/schemas/ChapterContentBlockTtsNodeResponseModel'
        - $ref: '#/components/schemas/ChapterContentBlockExtendableNodeResponseModel'
    ChapterContentBlockResponseModel:
      type: object
      properties:
        block_id:
          type: string
        nodes:
          type: array
          items:
            $ref: '#/components/schemas/ChapterContentBlockResponseModelNodesItems'
      required:
        - block_id
        - nodes
    ChapterContentResponseModel:
      type: object
      properties:
        blocks:
          type: array
          items:
            $ref: '#/components/schemas/ChapterContentBlockResponseModel'
      required:
        - blocks
    ChapterWithContentResponseModel:
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
          $ref: '#/components/schemas/ChapterWithContentResponseModelState'
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
        content:
          $ref: '#/components/schemas/ChapterContentResponseModel'
      required:
        - chapter_id
        - name
        - can_be_downloaded
        - state
        - content
    EditChapterResponseModel:
      type: object
      properties:
        chapter:
          $ref: '#/components/schemas/ChapterWithContentResponseModel'
      required:
        - chapter

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.chapters.update("project_id", "chapter_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.chapters.update(
    project_id="project_id",
    chapter_id="chapter_id"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")

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
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")! as URL,
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


# Delete Chapter

DELETE https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters/{chapter_id}

Deletes a chapter.

Reference: https://elevenlabs.io/docs/api-reference/studio/delete-chapter


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete Chapter
  version: endpoint_studio/projects/chapters.delete
paths:
  /v1/studio/projects/{project_id}/chapters/{chapter_id}:
    delete:
      operationId: delete
      summary: Delete Chapter
      description: Deletes a chapter.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/chapters
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
        - name: chapter_id
          in: path
          description: >-
            The ID of the chapter to be used. You can use the [List project
            chapters](/docs/api-reference/studio/get-chapters) endpoint to list
            all the available chapters.
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
                $ref: '#/components/schemas/DeleteChapterResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    DeleteChapterResponseModel:
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
    await client.studio.projects.chapters.delete("project_id", "chapter_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.chapters.delete(
    project_id="project_id",
    chapter_id="chapter_id"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")! as URL,
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


# Convert Chapter

POST https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters/{chapter_id}/convert

Starts conversion of a specific chapter.

Reference: https://elevenlabs.io/docs/api-reference/studio/convert-chapter


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Convert Chapter
  version: endpoint_studio/projects/chapters.convert
paths:
  /v1/studio/projects/{project_id}/chapters/{chapter_id}/convert:
    post:
      operationId: convert
      summary: Convert Chapter
      description: Starts conversion of a specific chapter.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/chapters
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
        - name: chapter_id
          in: path
          description: >-
            The ID of the chapter to be used. You can use the [List project
            chapters](/docs/api-reference/studio/get-chapters) endpoint to list
            all the available chapters.
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
                $ref: '#/components/schemas/ConvertChapterResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    ConvertChapterResponseModel:
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
    await client.studio.projects.chapters.convert("project_id", "chapter_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.chapters.convert(
    project_id="project_id",
    chapter_id="chapter_id"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/convert"

	req, _ := http.NewRequest("POST", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/convert")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/convert")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/convert', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/convert");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/convert")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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


# List Chapter Snapshots

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots

Gets information about all the snapshots of a chapter. Each snapshot can be downloaded as audio. Whenever a chapter is converted a snapshot will automatically be created.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-chapter-snapshots


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List Chapter Snapshots
  version: endpoint_studio/projects/chapters/snapshots.list
paths:
  /v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots:
    get:
      operationId: list
      summary: List Chapter Snapshots
      description: >-
        Gets information about all the snapshots of a chapter. Each snapshot can
        be downloaded as audio. Whenever a chapter is converted a snapshot will
        automatically be created.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/chapters
          - subpackage_studio/projects/chapters/snapshots
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
        - name: chapter_id
          in: path
          description: >-
            The ID of the chapter to be used. You can use the [List project
            chapters](/docs/api-reference/studio/get-chapters) endpoint to list
            all the available chapters.
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
                $ref: '#/components/schemas/ChapterSnapshotsResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    ChapterSnapshotResponseModel:
      type: object
      properties:
        chapter_snapshot_id:
          type: string
        project_id:
          type: string
        chapter_id:
          type: string
        created_at_unix:
          type: integer
        name:
          type: string
      required:
        - chapter_snapshot_id
        - project_id
        - chapter_id
        - created_at_unix
        - name
    ChapterSnapshotsResponseModel:
      type: object
      properties:
        snapshots:
          type: array
          items:
            $ref: '#/components/schemas/ChapterSnapshotResponseModel'
      required:
        - snapshots

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.chapters.snapshots.list("project_id", "chapter_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.chapters.snapshots.list(
    project_id="project_id",
    chapter_id="chapter_id"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots")! as URL,
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


# Stream Chapter Audio

POST https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots/{chapter_snapshot_id}/stream
Content-Type: application/json

Stream the audio from a chapter snapshot. Use `GET /v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots` to return the snapshots of a chapter.

Reference: https://elevenlabs.io/docs/api-reference/studio/stream-chapter-snapshot


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Stream Chapter Audio
  version: endpoint_studio/projects/chapters/snapshots.stream
paths:
  /v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots/{chapter_snapshot_id}/stream:
    post:
      operationId: stream
      summary: Stream Chapter Audio
      description: >-
        Stream the audio from a chapter snapshot. Use `GET
        /v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots` to
        return the snapshots of a chapter.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/chapters
          - subpackage_studio/projects/chapters/snapshots
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
        - name: chapter_id
          in: path
          description: >-
            The ID of the chapter to be used. You can use the [List project
            chapters](/docs/api-reference/studio/get-chapters) endpoint to list
            all the available chapters.
          required: true
          schema:
            type: string
        - name: chapter_snapshot_id
          in: path
          description: >-
            The ID of the chapter snapshot to be used. You can use the [List
            project chapter snapshots](/docs/api-reference/studio/get-snapshots)
            endpoint to list all the available snapshots.
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
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Stream_chapter_audio_v1_studio_projects__project_id__chapters__chapter_id__snapshots__chapter_snapshot_id__stream_post
components:
  schemas:
    Body_Stream_chapter_audio_v1_studio_projects__project_id__chapters__chapter_id__snapshots__chapter_snapshot_id__stream_post:
      type: object
      properties:
        convert_to_mpeg:
          type: boolean

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.chapters.snapshots.stream("project_id", "chapter_id", "chapter_snapshot_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.chapters.snapshots.stream(
    project_id="project_id",
    chapter_id="chapter_id",
    chapter_snapshot_id="chapter_snapshot_id"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id/stream"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id/stream")

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
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id/stream")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id/stream', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id/stream");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id/stream")! as URL,
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
**Navigation:** [← Previous](./38-get-history-item.md) | [Index](./index.md) | [Next →](./40-create-pronunciation-dictionaries.md)
