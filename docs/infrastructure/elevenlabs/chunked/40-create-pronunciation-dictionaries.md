**Navigation:** [← Previous](./39-delete-studio-project.md) | [Index](./index.md) | [Next →](./41-delete-voice-sample.md)

# Create Pronunciation Dictionaries

POST https://api.elevenlabs.io/v1/studio/projects/{project_id}/pronunciation-dictionaries
Content-Type: application/json

Create a set of pronunciation dictionaries acting on a project. This will automatically mark text within this project as requiring reconverting where the new dictionary would apply or the old one no longer does.

Reference: https://elevenlabs.io/docs/api-reference/studio/create-pronunciation-dictionaries


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create Pronunciation Dictionaries
  version: endpoint_studio/projects/pronunciationDictionaries.create
paths:
  /v1/studio/projects/{project_id}/pronunciation-dictionaries:
    post:
      operationId: create
      summary: Create Pronunciation Dictionaries
      description: >-
        Create a set of pronunciation dictionaries acting on a project. This
        will automatically mark text within this project as requiring
        reconverting where the new dictionary would apply or the old one no
        longer does.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/pronunciationDictionaries
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
                $ref: >-
                  #/components/schemas/CreatePronunciationDictionaryResponseModel
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Create_Pronunciation_Dictionaries_v1_studio_projects__project_id__pronunciation_dictionaries_post
components:
  schemas:
    PronunciationDictionaryVersionLocatorDBModel:
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
    Body_Create_Pronunciation_Dictionaries_v1_studio_projects__project_id__pronunciation_dictionaries_post:
      type: object
      properties:
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: '#/components/schemas/PronunciationDictionaryVersionLocatorDBModel'
        invalidate_affected_text:
          type: boolean
      required:
        - pronunciation_dictionary_locators
    CreatePronunciationDictionaryResponseModel:
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
    await client.studio.projects.pronunciationDictionaries.create("project_id", {
        pronunciationDictionaryLocators: [
            {
                pronunciationDictionaryId: "string",
                versionId: "string",
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

client.studio.projects.pronunciation_dictionaries.create(
    project_id="project_id",
    pronunciation_dictionary_locators=[
        {
            "pronunciation_dictionary_id": "string",
            "version_id": "string"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries"

	payload := strings.NewReader("{\n  \"pronunciation_dictionary_locators\": [\n    {\n      \"pronunciation_dictionary_id\": \"string\",\n      \"version_id\": \"string\"\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"pronunciation_dictionary_locators\": [\n    {\n      \"pronunciation_dictionary_id\": \"string\",\n      \"version_id\": \"string\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"pronunciation_dictionary_locators\": [\n    {\n      \"pronunciation_dictionary_id\": \"string\",\n      \"version_id\": \"string\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries', [
  'body' => '{
  "pronunciation_dictionary_locators": [
    {
      "pronunciation_dictionary_id": "string",
      "version_id": "string"
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
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"pronunciation_dictionary_locators\": [\n    {\n      \"pronunciation_dictionary_id\": \"string\",\n      \"version_id\": \"string\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["pronunciation_dictionary_locators": [
    [
      "pronunciation_dictionary_id": "string",
      "version_id": "string"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries")! as URL,
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


# Create Podcast

POST https://api.elevenlabs.io/v1/studio/podcasts
Content-Type: application/json

Create and auto-convert a podcast project. Currently, the LLM cost is covered by us but you will still be charged for the audio generation. In the future, you will be charged for both the LLM and audio generation costs.

Reference: https://elevenlabs.io/docs/api-reference/studio/create-podcast


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create Podcast
  version: endpoint_studio.create_podcast
paths:
  /v1/studio/podcasts:
    post:
      operationId: create-podcast
      summary: Create Podcast
      description: >-
        Create and auto-convert a podcast project. Currently, the LLM cost is
        covered by us but you will still be charged for the audio generation. In
        the future, you will be charged for both the LLM and audio generation
        costs.
      tags:
        - - subpackage_studio
      parameters:
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
        - name: safety-identifier
          in: header
          description: >-
            Used for moderation. Your workspace must be allowlisted to use this
            feature.
          required: false
          schema:
            type:
              - string
              - 'null'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PodcastProjectResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Body_Create_podcast_v1_studio_podcasts_post'
components:
  schemas:
    PodcastConversationModeData:
      type: object
      properties:
        host_voice_id:
          type: string
        guest_voice_id:
          type: string
      required:
        - host_voice_id
        - guest_voice_id
    PodcastConversationMode:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: conversation
        conversation:
          $ref: '#/components/schemas/PodcastConversationModeData'
      required:
        - type
        - conversation
    PodcastBulletinModeData:
      type: object
      properties:
        host_voice_id:
          type: string
      required:
        - host_voice_id
    PodcastBulletinMode:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: bulletin
        bulletin:
          $ref: '#/components/schemas/PodcastBulletinModeData'
      required:
        - type
        - bulletin
    BodyCreatePodcastV1StudioPodcastsPostMode:
      oneOf:
        - $ref: '#/components/schemas/PodcastConversationMode'
        - $ref: '#/components/schemas/PodcastBulletinMode'
    PodcastTextSource:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: text
        text:
          type: string
      required:
        - type
        - text
    PodcastURLSource:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: url
        url:
          type: string
      required:
        - type
        - url
    BodyCreatePodcastV1StudioPodcastsPostSourceOneOf2Items:
      oneOf:
        - $ref: '#/components/schemas/PodcastTextSource'
        - $ref: '#/components/schemas/PodcastURLSource'
    BodyCreatePodcastV1StudioPodcastsPostSource2:
      type: array
      items:
        $ref: >-
          #/components/schemas/BodyCreatePodcastV1StudioPodcastsPostSourceOneOf2Items
    BodyCreatePodcastV1StudioPodcastsPostSource:
      oneOf:
        - $ref: '#/components/schemas/PodcastTextSource'
        - $ref: '#/components/schemas/PodcastURLSource'
        - $ref: '#/components/schemas/BodyCreatePodcastV1StudioPodcastsPostSource2'
    BodyCreatePodcastV1StudioPodcastsPostQualityPreset:
      type: string
      enum:
        - value: standard
        - value: high
        - value: highest
        - value: ultra
        - value: ultra_lossless
    BodyCreatePodcastV1StudioPodcastsPostDurationScale:
      type: string
      enum:
        - value: short
        - value: default
        - value: long
    BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
        - value: apply_english
    Body_Create_podcast_v1_studio_podcasts_post:
      type: object
      properties:
        model_id:
          type: string
        mode:
          $ref: '#/components/schemas/BodyCreatePodcastV1StudioPodcastsPostMode'
        source:
          $ref: '#/components/schemas/BodyCreatePodcastV1StudioPodcastsPostSource'
        quality_preset:
          $ref: >-
            #/components/schemas/BodyCreatePodcastV1StudioPodcastsPostQualityPreset
        duration_scale:
          $ref: >-
            #/components/schemas/BodyCreatePodcastV1StudioPodcastsPostDurationScale
        language:
          type:
            - string
            - 'null'
        intro:
          type:
            - string
            - 'null'
        outro:
          type:
            - string
            - 'null'
        instructions_prompt:
          type:
            - string
            - 'null'
        highlights:
          type:
            - array
            - 'null'
          items:
            type: string
        callback_url:
          type:
            - string
            - 'null'
        apply_text_normalization:
          oneOf:
            - $ref: >-
                #/components/schemas/BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization
            - type: 'null'
      required:
        - model_id
        - mode
        - source
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
    PodcastProjectResponseModel:
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
    await client.studio.createPodcast({
        modelId: "eleven_multilingual_v2",
        source: {
            text: "string",
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.create_podcast(
    model_id="eleven_multilingual_v2",
    mode=,
    source={
        "text": "string"
    }
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

	url := "https://api.elevenlabs.io/v1/studio/podcasts"

	payload := strings.NewReader("{\n  \"model_id\": \"eleven_multilingual_v2\",\n  \"mode\": {\n    \"type\": \"string\",\n    \"conversation\": {\n      \"host_voice_id\": \"string\",\n      \"guest_voice_id\": \"string\"\n    }\n  },\n  \"source\": {\n    \"type\": \"string\",\n    \"text\": \"string\"\n  }\n}")

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

url = URI("https://api.elevenlabs.io/v1/studio/podcasts")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model_id\": \"eleven_multilingual_v2\",\n  \"mode\": {\n    \"type\": \"string\",\n    \"conversation\": {\n      \"host_voice_id\": \"string\",\n      \"guest_voice_id\": \"string\"\n    }\n  },\n  \"source\": {\n    \"type\": \"string\",\n    \"text\": \"string\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/podcasts")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"model_id\": \"eleven_multilingual_v2\",\n  \"mode\": {\n    \"type\": \"string\",\n    \"conversation\": {\n      \"host_voice_id\": \"string\",\n      \"guest_voice_id\": \"string\"\n    }\n  },\n  \"source\": {\n    \"type\": \"string\",\n    \"text\": \"string\"\n  }\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/podcasts', [
  'body' => '{
  "model_id": "eleven_multilingual_v2",
  "mode": {
    "type": "string",
    "conversation": {
      "host_voice_id": "string",
      "guest_voice_id": "string"
    }
  },
  "source": {
    "type": "string",
    "text": "string"
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/podcasts");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model_id\": \"eleven_multilingual_v2\",\n  \"mode\": {\n    \"type\": \"string\",\n    \"conversation\": {\n      \"host_voice_id\": \"string\",\n      \"guest_voice_id\": \"string\"\n    }\n  },\n  \"source\": {\n    \"type\": \"string\",\n    \"text\": \"string\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "model_id": "eleven_multilingual_v2",
  "mode": [
    "type": "string",
    "conversation": [
      "host_voice_id": "string",
      "guest_voice_id": "string"
    ]
  ],
  "source": [
    "type": "string",
    "text": "string"
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/podcasts")! as URL,
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


# Get Chapter Snapshot

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots/{chapter_snapshot_id}

Returns the chapter snapshot.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-chapter-snapshot


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Chapter Snapshot
  version: endpoint_studio/projects/chapters/snapshots.get
paths:
  /v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots/{chapter_snapshot_id}:
    get:
      operationId: get
      summary: Get Chapter Snapshot
      description: Returns the chapter snapshot.
      tags:
        - - subpackage_studio
          - subpackage_studio/projects
          - subpackage_studio/projects/chapters
          - subpackage_studio/projects/chapters/snapshots
      parameters:
        - name: project_id
          in: path
          description: The ID of the Studio project.
          required: true
          schema:
            type: string
        - name: chapter_id
          in: path
          description: The ID of the chapter.
          required: true
          schema:
            type: string
        - name: chapter_snapshot_id
          in: path
          description: The ID of the chapter snapshot.
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
                $ref: '#/components/schemas/ChapterSnapshotExtendedResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    CharacterAlignmentModel:
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
    ChapterSnapshotExtendedResponseModel:
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
        character_alignments:
          type: array
          items:
            $ref: '#/components/schemas/CharacterAlignmentModel'
      required:
        - chapter_snapshot_id
        - project_id
        - chapter_id
        - created_at_unix
        - name
        - character_alignments

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.chapters.snapshots.get("project_id", "chapter_id", "chapter_snapshot_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.chapters.snapshots.get(
    project_id="project_id",
    chapter_id="chapter_id",
    chapter_snapshot_id="chapter_snapshot_id"
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id")! as URL,
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


# Get Project Snapshot

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}

Returns the project snapshot.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-project-snapshot


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Project Snapshot
  version: endpoint_studio/projects/snapshots.get
paths:
  /v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}:
    get:
      operationId: get
      summary: Get Project Snapshot
      description: Returns the project snapshot.
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
            application/json:
              schema:
                $ref: '#/components/schemas/ProjectSnapshotExtendedResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    ProjectSnapshotExtendedResponseModelAudioUpload:
      type: object
      properties: {}
    ProjectSnapshotExtendedResponseModelZipUpload:
      type: object
      properties: {}
    CharacterAlignmentModel:
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
    ProjectSnapshotExtendedResponseModel:
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
            - $ref: >-
                #/components/schemas/ProjectSnapshotExtendedResponseModelAudioUpload
            - type: 'null'
        zip_upload:
          oneOf:
            - $ref: >-
                #/components/schemas/ProjectSnapshotExtendedResponseModelZipUpload
            - type: 'null'
        character_alignments:
          type: array
          items:
            $ref: '#/components/schemas/CharacterAlignmentModel'
      required:
        - project_snapshot_id
        - project_id
        - created_at_unix
        - name
        - character_alignments

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.studio.projects.snapshots.get("project_id", "project_snapshot_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.studio.projects.snapshots.get(
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id")! as URL,
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


# Create a pronunciation dictionary from a file

POST https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file
Content-Type: multipart/form-data

Creates a new pronunciation dictionary from a lexicon .PLS file

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/create-from-file


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create a pronunciation dictionary from a file
  version: endpoint_pronunciationDictionaries.create_from_file
paths:
  /v1/pronunciation-dictionaries/add-from-file:
    post:
      operationId: create-from-file
      summary: Create a pronunciation dictionary from a file
      description: Creates a new pronunciation dictionary from a lexicon .PLS file
      tags:
        - - subpackage_pronunciationDictionaries
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
                $ref: '#/components/schemas/AddPronunciationDictionaryResponseModel'
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
                description:
                  type:
                    - string
                    - 'null'
                workspace_access:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1PronunciationDictionariesAddFromFilePostRequestBodyContentMultipartFormDataSchemaWorkspaceAccess
                    - type: 'null'
components:
  schemas:
    V1PronunciationDictionariesAddFromFilePostRequestBodyContentMultipartFormDataSchemaWorkspaceAccess:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    AddPronunciationDictionaryResponseModelPermissionOnResource:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    AddPronunciationDictionaryResponseModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        created_by:
          type: string
        creation_time_unix:
          type: integer
        version_id:
          type: string
        version_rules_num:
          type: integer
        description:
          type:
            - string
            - 'null'
        permission_on_resource:
          oneOf:
            - $ref: >-
                #/components/schemas/AddPronunciationDictionaryResponseModelPermissionOnResource
            - type: 'null'
      required:
        - id
        - name
        - created_by
        - creation_time_unix
        - version_id
        - version_rules_num
        - permission_on_resource

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.pronunciationDictionaries.createFromFile({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.pronunciation_dictionaries.create_from_file()

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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nMy Dictionary\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"workspace_access\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nMy Dictionary\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"workspace_access\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nMy Dictionary\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"workspace_access\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file', [
  'multipart' => [
    [
        'name' => 'name',
        'contents' => 'My Dictionary'
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
var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nMy Dictionary\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"workspace_access\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
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
    "value": "My Dictionary"
  ],
  [
    "name": "file",
    "fileName": "<file1>"
  ],
  [
    "name": "description",
    "value": 
  ],
  [
    "name": "workspace_access",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file")! as URL,
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


# Create a pronunciation dictionary from rules

POST https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules
Content-Type: application/json

Creates a new pronunciation dictionary from provided rules.

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/create-from-rules


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create a pronunciation dictionary from rules
  version: endpoint_pronunciationDictionaries.create_from_rules
paths:
  /v1/pronunciation-dictionaries/add-from-rules:
    post:
      operationId: create-from-rules
      summary: Create a pronunciation dictionary from rules
      description: Creates a new pronunciation dictionary from provided rules.
      tags:
        - - subpackage_pronunciationDictionaries
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
                $ref: '#/components/schemas/AddPronunciationDictionaryResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Add_a_pronunciation_dictionary_v1_pronunciation_dictionaries_add_from_rules_post
components:
  schemas:
    PronunciationDictionaryAliasRuleRequestModel:
      type: object
      properties:
        string_to_replace:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: alias
        alias:
          type: string
      required:
        - string_to_replace
        - type
        - alias
    PronunciationDictionaryPhonemeRuleRequestModel:
      type: object
      properties:
        string_to_replace:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: phoneme
        phoneme:
          type: string
        alphabet:
          type: string
      required:
        - string_to_replace
        - type
        - phoneme
        - alphabet
    BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItems:
      oneOf:
        - $ref: '#/components/schemas/PronunciationDictionaryAliasRuleRequestModel'
        - $ref: '#/components/schemas/PronunciationDictionaryPhonemeRuleRequestModel'
    BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    Body_Add_a_pronunciation_dictionary_v1_pronunciation_dictionaries_add_from_rules_post:
      type: object
      properties:
        rules:
          type: array
          items:
            $ref: >-
              #/components/schemas/BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItems
        name:
          type: string
        description:
          type:
            - string
            - 'null'
        workspace_access:
          oneOf:
            - $ref: >-
                #/components/schemas/BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess
            - type: 'null'
      required:
        - rules
        - name
    AddPronunciationDictionaryResponseModelPermissionOnResource:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    AddPronunciationDictionaryResponseModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        created_by:
          type: string
        creation_time_unix:
          type: integer
        version_id:
          type: string
        version_rules_num:
          type: integer
        description:
          type:
            - string
            - 'null'
        permission_on_resource:
          oneOf:
            - $ref: >-
                #/components/schemas/AddPronunciationDictionaryResponseModelPermissionOnResource
            - type: 'null'
      required:
        - id
        - name
        - created_by
        - creation_time_unix
        - version_id
        - version_rules_num
        - permission_on_resource

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.pronunciationDictionaries.createFromRules({
        rules: [],
        name: "My Dictionary",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.pronunciation_dictionaries.create_from_rules(
    rules=[],
    name="My Dictionary"
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules"

	payload := strings.NewReader("{\n  \"rules\": [\n    {\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\",\n      \"alias\": \"string\"\n    }\n  ],\n  \"name\": \"My Dictionary\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"rules\": [\n    {\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\",\n      \"alias\": \"string\"\n    }\n  ],\n  \"name\": \"My Dictionary\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"rules\": [\n    {\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\",\n      \"alias\": \"string\"\n    }\n  ],\n  \"name\": \"My Dictionary\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules', [
  'body' => '{
  "rules": [
    {
      "string_to_replace": "string",
      "type": "string",
      "alias": "string"
    }
  ],
  "name": "My Dictionary"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"rules\": [\n    {\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\",\n      \"alias\": \"string\"\n    }\n  ],\n  \"name\": \"My Dictionary\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "rules": [
    [
      "string_to_replace": "string",
      "type": "string",
      "alias": "string"
    ]
  ],
  "name": "My Dictionary"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules")! as URL,
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


# Get pronunciation dictionary

GET https://api.elevenlabs.io/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}

Get metadata for a pronunciation dictionary

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get pronunciation dictionary
  version: endpoint_pronunciationDictionaries.get
paths:
  /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}:
    get:
      operationId: get
      summary: Get pronunciation dictionary
      description: Get metadata for a pronunciation dictionary
      tags:
        - - subpackage_pronunciationDictionaries
      parameters:
        - name: pronunciation_dictionary_id
          in: path
          description: The id of the pronunciation dictionary
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
                $ref: >-
                  #/components/schemas/GetPronunciationDictionaryMetadataResponseModel
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    GetPronunciationDictionaryMetadataResponseModelPermissionOnResource:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    GetPronunciationDictionaryMetadataResponseModel:
      type: object
      properties:
        id:
          type: string
        latest_version_id:
          type: string
        latest_version_rules_num:
          type: integer
        name:
          type: string
        permission_on_resource:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPronunciationDictionaryMetadataResponseModelPermissionOnResource
            - type: 'null'
        created_by:
          type: string
        creation_time_unix:
          type: integer
        archived_time_unix:
          type:
            - integer
            - 'null'
        description:
          type:
            - string
            - 'null'
      required:
        - id
        - latest_version_id
        - latest_version_rules_num
        - name
        - permission_on_resource
        - created_by
        - creation_time_unix

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.pronunciationDictionaries.get("pronunciation_dictionary_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.pronunciation_dictionaries.get(
    pronunciation_dictionary_id="pronunciation_dictionary_id"
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id"

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")! as URL,
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


# Update Pronunciation Dictionary

PATCH https://api.elevenlabs.io/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}
Content-Type: application/json

Partially update the pronunciation dictionary without changing the version

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/update


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update Pronunciation Dictionary
  version: endpoint_pronunciationDictionaries.update
paths:
  /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}:
    patch:
      operationId: update
      summary: Update Pronunciation Dictionary
      description: >-
        Partially update the pronunciation dictionary without changing the
        version
      tags:
        - - subpackage_pronunciationDictionaries
      parameters:
        - name: pronunciation_dictionary_id
          in: path
          description: The id of the pronunciation dictionary
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
                $ref: >-
                  #/components/schemas/GetPronunciationDictionaryMetadataResponseModel
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Update_pronunciation_dictionary_v1_pronunciation_dictionaries__pronunciation_dictionary_id__patch
components:
  schemas:
    Body_Update_pronunciation_dictionary_v1_pronunciation_dictionaries__pronunciation_dictionary_id__patch:
      type: object
      properties:
        archived:
          type: boolean
        name:
          type: string
    GetPronunciationDictionaryMetadataResponseModelPermissionOnResource:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    GetPronunciationDictionaryMetadataResponseModel:
      type: object
      properties:
        id:
          type: string
        latest_version_id:
          type: string
        latest_version_rules_num:
          type: integer
        name:
          type: string
        permission_on_resource:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPronunciationDictionaryMetadataResponseModelPermissionOnResource
            - type: 'null'
        created_by:
          type: string
        creation_time_unix:
          type: integer
        archived_time_unix:
          type:
            - integer
            - 'null'
        description:
          type:
            - string
            - 'null'
      required:
        - id
        - latest_version_id
        - latest_version_rules_num
        - name
        - permission_on_resource
        - created_by
        - creation_time_unix

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.pronunciationDictionaries.update("pronunciation_dictionary_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.pronunciation_dictionaries.update(
    pronunciation_dictionary_id="pronunciation_dictionary_id"
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id"

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")

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
HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")! as URL,
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


# Get pronunciation dictionary by version

GET https://api.elevenlabs.io/v1/pronunciation-dictionaries/{dictionary_id}/{version_id}/download

Get a PLS file with a pronunciation dictionary version rules

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/download


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get pronunciation dictionary by version
  version: endpoint_pronunciationDictionaries.download
paths:
  /v1/pronunciation-dictionaries/{dictionary_id}/{version_id}/download:
    get:
      operationId: download
      summary: Get pronunciation dictionary by version
      description: Get a PLS file with a pronunciation dictionary version rules
      tags:
        - - subpackage_pronunciationDictionaries
      parameters:
        - name: dictionary_id
          in: path
          description: The id of the pronunciation dictionary
          required: true
          schema:
            type: string
        - name: version_id
          in: path
          description: The id of the pronunciation dictionary version
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
          description: The PLS file containing pronunciation dictionary rules
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
    await client.pronunciationDictionaries.download("dictionary_id", "version_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.pronunciation_dictionaries.download(
    dictionary_id="dictionary_id",
    version_id="version_id"
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/dictionary_id/version_id/download"

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/dictionary_id/version_id/download")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/pronunciation-dictionaries/dictionary_id/version_id/download")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/dictionary_id/version_id/download', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/dictionary_id/version_id/download");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/dictionary_id/version_id/download")! as URL,
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


# List pronunciation dictionaries

GET https://api.elevenlabs.io/v1/pronunciation-dictionaries

Get a list of the pronunciation dictionaries you have access to and their metadata

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/list


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List pronunciation dictionaries
  version: endpoint_pronunciationDictionaries.list
paths:
  /v1/pronunciation-dictionaries:
    get:
      operationId: list
      summary: List pronunciation dictionaries
      description: >-
        Get a list of the pronunciation dictionaries you have access to and
        their metadata
      tags:
        - - subpackage_pronunciationDictionaries
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
            How many pronunciation dictionaries to return at maximum. Can not
            exceed 100, defaults to 30.
          required: false
          schema:
            type: integer
        - name: sort
          in: query
          description: Which field to sort by, one of 'created_at_unix' or 'name'.
          required: false
          schema:
            oneOf:
              - $ref: >-
                  #/components/schemas/V1PronunciationDictionariesGetParametersSortSchema
              - type: 'null'
        - name: sort_direction
          in: query
          description: Which direction to sort the voices in. 'ascending' or 'descending'.
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
                $ref: >-
                  #/components/schemas/GetPronunciationDictionariesMetadataResponseModel
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    V1PronunciationDictionariesGetParametersSortSchema:
      type: string
      enum:
        - value: creation_time_unix
        - value: name
    GetPronunciationDictionaryMetadataResponseModelPermissionOnResource:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    GetPronunciationDictionaryMetadataResponseModel:
      type: object
      properties:
        id:
          type: string
        latest_version_id:
          type: string
        latest_version_rules_num:
          type: integer
        name:
          type: string
        permission_on_resource:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPronunciationDictionaryMetadataResponseModelPermissionOnResource
            - type: 'null'
        created_by:
          type: string
        creation_time_unix:
          type: integer
        archived_time_unix:
          type:
            - integer
            - 'null'
        description:
          type:
            - string
            - 'null'
      required:
        - id
        - latest_version_id
        - latest_version_rules_num
        - name
        - permission_on_resource
        - created_by
        - creation_time_unix
    GetPronunciationDictionariesMetadataResponseModel:
      type: object
      properties:
        pronunciation_dictionaries:
          type: array
          items:
            $ref: >-
              #/components/schemas/GetPronunciationDictionaryMetadataResponseModel
        next_cursor:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
      required:
        - pronunciation_dictionaries
        - has_more

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.pronunciationDictionaries.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.pronunciation_dictionaries.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries"

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/pronunciation-dictionaries")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries")! as URL,
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


# Add pronunciation dictionary rules

POST https://api.elevenlabs.io/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/add-rules
Content-Type: application/json

Add rules to the pronunciation dictionary

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/rules/add


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Add pronunciation dictionary rules
  version: endpoint_pronunciationDictionaries/rules.add
paths:
  /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/add-rules:
    post:
      operationId: add
      summary: Add pronunciation dictionary rules
      description: Add rules to the pronunciation dictionary
      tags:
        - - subpackage_pronunciationDictionaries
          - subpackage_pronunciationDictionaries/rules
      parameters:
        - name: pronunciation_dictionary_id
          in: path
          description: The id of the pronunciation dictionary
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
                $ref: '#/components/schemas/PronunciationDictionaryRulesResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Add_rules_to_the_pronunciation_dictionary_v1_pronunciation_dictionaries__pronunciation_dictionary_id__add_rules_post
components:
  schemas:
    PronunciationDictionaryAliasRuleRequestModel:
      type: object
      properties:
        string_to_replace:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: alias
        alias:
          type: string
      required:
        - string_to_replace
        - type
        - alias
    PronunciationDictionaryPhonemeRuleRequestModel:
      type: object
      properties:
        string_to_replace:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: phoneme
        phoneme:
          type: string
        alphabet:
          type: string
      required:
        - string_to_replace
        - type
        - phoneme
        - alphabet
    BodyAddRulesToThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdAddRulesPostRulesItems:
      oneOf:
        - $ref: '#/components/schemas/PronunciationDictionaryAliasRuleRequestModel'
        - $ref: '#/components/schemas/PronunciationDictionaryPhonemeRuleRequestModel'
    Body_Add_rules_to_the_pronunciation_dictionary_v1_pronunciation_dictionaries__pronunciation_dictionary_id__add_rules_post:
      type: object
      properties:
        rules:
          type: array
          items:
            $ref: >-
              #/components/schemas/BodyAddRulesToThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdAddRulesPostRulesItems
      required:
        - rules
    PronunciationDictionaryRulesResponseModel:
      type: object
      properties:
        id:
          type: string
        version_id:
          type: string
        version_rules_num:
          type: integer
      required:
        - id
        - version_id
        - version_rules_num

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.pronunciationDictionaries.rules.add("pronunciation_dictionary_id", {
        rules: [],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.pronunciation_dictionaries.rules.add(
    pronunciation_dictionary_id="pronunciation_dictionary_id",
    rules=[]
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/add-rules"

	payload := strings.NewReader("{\n  \"rules\": [\n    {\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\",\n      \"alias\": \"string\"\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/add-rules")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"rules\": [\n    {\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\",\n      \"alias\": \"string\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/add-rules")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"rules\": [\n    {\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\",\n      \"alias\": \"string\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/add-rules', [
  'body' => '{
  "rules": [
    {
      "string_to_replace": "string",
      "type": "string",
      "alias": "string"
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
var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/add-rules");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"rules\": [\n    {\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\",\n      \"alias\": \"string\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["rules": [
    [
      "string_to_replace": "string",
      "type": "string",
      "alias": "string"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/add-rules")! as URL,
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


# Remove pronunciation dictionary rules

POST https://api.elevenlabs.io/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/remove-rules
Content-Type: application/json

Remove rules from the pronunciation dictionary

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/rules/remove


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Remove pronunciation dictionary rules
  version: endpoint_pronunciationDictionaries/rules.remove
paths:
  /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/remove-rules:
    post:
      operationId: remove
      summary: Remove pronunciation dictionary rules
      description: Remove rules from the pronunciation dictionary
      tags:
        - - subpackage_pronunciationDictionaries
          - subpackage_pronunciationDictionaries/rules
      parameters:
        - name: pronunciation_dictionary_id
          in: path
          description: The id of the pronunciation dictionary
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
                $ref: '#/components/schemas/PronunciationDictionaryRulesResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Remove_rules_from_the_pronunciation_dictionary_v1_pronunciation_dictionaries__pronunciation_dictionary_id__remove_rules_post
components:
  schemas:
    Body_Remove_rules_from_the_pronunciation_dictionary_v1_pronunciation_dictionaries__pronunciation_dictionary_id__remove_rules_post:
      type: object
      properties:
        rule_strings:
          type: array
          items:
            type: string
      required:
        - rule_strings
    PronunciationDictionaryRulesResponseModel:
      type: object
      properties:
        id:
          type: string
        version_id:
          type: string
        version_rules_num:
          type: integer
      required:
        - id
        - version_id
        - version_rules_num

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.pronunciationDictionaries.rules.remove("pronunciation_dictionary_id", {
        ruleStrings: [
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

client.pronunciation_dictionaries.rules.remove(
    pronunciation_dictionary_id="pronunciation_dictionary_id",
    rule_strings=[
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/remove-rules"

	payload := strings.NewReader("{\n  \"rule_strings\": [\n    \"string\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/remove-rules")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"rule_strings\": [\n    \"string\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/remove-rules")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"rule_strings\": [\n    \"string\"\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/remove-rules', [
  'body' => '{
  "rule_strings": [
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
var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/remove-rules");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"rule_strings\": [\n    \"string\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["rule_strings": ["string"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/remove-rules")! as URL,
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
**Navigation:** [← Previous](./39-delete-studio-project.md) | [Index](./index.md) | [Next →](./41-delete-voice-sample.md)
