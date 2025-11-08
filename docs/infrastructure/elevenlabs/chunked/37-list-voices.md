**Navigation:** [← Previous](./36-get-audio-native-project-settings.md) | [Index](./index.md) | [Next →](./38-get-history-item.md)

# List voices

GET https://api.elevenlabs.io/v2/voices

Gets a list of all available voices for a user with search, filtering and pagination.

Reference: https://elevenlabs.io/docs/api-reference/voices/search


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List voices
  version: endpoint_voices.search
paths:
  /v2/voices:
    get:
      operationId: search
      summary: List voices
      description: >-
        Gets a list of all available voices for a user with search, filtering
        and pagination.
      tags:
        - - subpackage_voices
      parameters:
        - name: next_page_token
          in: query
          description: >-
            The next page token to use for pagination. Returned from the
            previous request.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: page_size
          in: query
          description: >-
            How many voices to return at maximum. Can not exceed 100, defaults
            to 10. Page 0 may include more voices due to default voices being
            included.
          required: false
          schema:
            type: integer
        - name: search
          in: query
          description: >-
            Search term to filter voices by. Searches in name, description,
            labels, category.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: sort
          in: query
          description: >-
            Which field to sort by, one of 'created_at_unix' or 'name'.
            'created_at_unix' may not be available for older voices.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: sort_direction
          in: query
          description: Which direction to sort the voices in. 'asc' or 'desc'.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: voice_type
          in: query
          description: >-
            Type of the voice to filter by. One of 'personal', 'community',
            'default', 'workspace', 'non-default'. 'non-default' is equal to all
            but 'default'.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: category
          in: query
          description: >-
            Category of the voice to filter by. One of 'premade', 'cloned',
            'generated', 'professional'
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: fine_tuning_state
          in: query
          description: >-
            State of the voice's fine tuning to filter by. Applicable only to
            professional voices clones. One of 'draft', 'not_verified',
            'not_started', 'queued', 'fine_tuning', 'fine_tuned', 'failed',
            'delayed'
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: collection_id
          in: query
          description: Collection ID to filter voices by.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: include_total_count
          in: query
          description: >-
            Whether to include the total count of voices found in the response.
            Incurs a performance cost.
          required: false
          schema:
            type: boolean
        - name: voice_ids
          in: query
          description: Voice IDs to lookup by. Maximum 100 voice IDs.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
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
                $ref: '#/components/schemas/GetVoicesV2ResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
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
    GetVoicesV2ResponseModel:
      type: object
      properties:
        voices:
          type: array
          items:
            $ref: '#/components/schemas/VoiceResponseModel'
        has_more:
          type: boolean
        total_count:
          type: integer
        next_page_token:
          type:
            - string
            - 'null'
      required:
        - voices
        - has_more
        - total_count

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.voices.search({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.voices.search()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v2/voices"

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

url = URI("https://api.elevenlabs.io/v2/voices")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v2/voices")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v2/voices', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v2/voices");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v2/voices")! as URL,
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


# Get voice

GET https://api.elevenlabs.io/v1/voices/{voice_id}

Returns metadata about a specific voice.

Reference: https://elevenlabs.io/docs/api-reference/voices/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get voice
  version: endpoint_voices.get
paths:
  /v1/voices/{voice_id}:
    get:
      operationId: get
      summary: Get voice
      description: Returns metadata about a specific voice.
      tags:
        - - subpackage_voices
      parameters:
        - name: voice_id
          in: path
          description: >-
            ID of the voice to be used. You can use the [Get
            voices](/docs/api-reference/voices/search) endpoint list all the
            available voices.
          required: true
          schema:
            type: string
        - name: with_settings
          in: query
          description: >-
            This parameter is now deprecated. It is ignored and will be removed
            in a future version.
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
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VoiceResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
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
    await client.voices.get("voice_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.voices.get(
    voice_id="voice_id"
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

	url := "https://api.elevenlabs.io/v1/voices/voice_id"

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

url = URI("https://api.elevenlabs.io/v1/voices/voice_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices/voice_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/voice_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/voices/voice_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/voice_id")! as URL,
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


# Delete voice

DELETE https://api.elevenlabs.io/v1/voices/{voice_id}

Deletes a voice by its ID.

Reference: https://elevenlabs.io/docs/api-reference/voices/delete


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete voice
  version: endpoint_voices.delete
paths:
  /v1/voices/{voice_id}:
    delete:
      operationId: delete
      summary: Delete voice
      description: Deletes a voice by its ID.
      tags:
        - - subpackage_voices
      parameters:
        - name: voice_id
          in: path
          description: >-
            ID of the voice to be used. You can use the [Get
            voices](/docs/api-reference/voices/search) endpoint list all the
            available voices.
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
                $ref: '#/components/schemas/DeleteVoiceResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    DeleteVoiceResponseModel:
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
    await client.voices.delete("voice_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.voices.delete(
    voice_id="voice_id"
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

	url := "https://api.elevenlabs.io/v1/voices/voice_id"

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

url = URI("https://api.elevenlabs.io/v1/voices/voice_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/voices/voice_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/voices/voice_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/voices/voice_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/voice_id")! as URL,
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


# Edit voice

POST https://api.elevenlabs.io/v1/voices/{voice_id}/edit
Content-Type: multipart/form-data

Edit a voice created by you.

Reference: https://elevenlabs.io/docs/api-reference/voices/update


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Edit voice
  version: endpoint_voices.update
paths:
  /v1/voices/{voice_id}/edit:
    post:
      operationId: update
      summary: Edit voice
      description: Edit a voice created by you.
      tags:
        - - subpackage_voices
      parameters:
        - name: voice_id
          in: path
          description: >-
            ID of the voice to be used. You can use the [Get
            voices](/docs/api-reference/voices/search) endpoint list all the
            available voices.
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
                $ref: '#/components/schemas/EditVoiceResponseModel'
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
                remove_background_noise:
                  type: boolean
                description:
                  type:
                    - string
                    - 'null'
                labels:
                  type:
                    - string
                    - 'null'
components:
  schemas:
    EditVoiceResponseModel:
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
    await client.voices.update("voice_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.voices.update(
    voice_id="voice_id"
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

	url := "https://api.elevenlabs.io/v1/voices/voice_id/edit"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nJohn Smith\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"labels\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/voices/voice_id/edit")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nJohn Smith\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"labels\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/voices/voice_id/edit")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nJohn Smith\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"labels\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/voices/voice_id/edit', [
  'multipart' => [
    [
        'name' => 'name',
        'contents' => 'John Smith'
    ]
  ]
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/voices/voice_id/edit");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nJohn Smith\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"labels\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
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
    "value": "John Smith"
  ],
  [
    "name": "remove_background_noise",
    "value": 
  ],
  [
    "name": "description",
    "value": 
  ],
  [
    "name": "labels",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/voice_id/edit")! as URL,
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


# List similar voices

POST https://api.elevenlabs.io/v1/similar-voices
Content-Type: multipart/form-data

Returns a list of shared voices similar to the provided audio sample. If neither similarity_threshold nor top_k is provided, we will apply default values.

Reference: https://elevenlabs.io/docs/api-reference/voices/find-similar-voices


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List similar voices
  version: endpoint_voices.find_similar_voices
paths:
  /v1/similar-voices:
    post:
      operationId: find-similar-voices
      summary: List similar voices
      description: >-
        Returns a list of shared voices similar to the provided audio sample. If
        neither similarity_threshold nor top_k is provided, we will apply
        default values.
      tags:
        - - subpackage_voices
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
                $ref: '#/components/schemas/GetLibraryVoicesResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                similarity_threshold:
                  type:
                    - number
                    - 'null'
                  format: double
                top_k:
                  type:
                    - integer
                    - 'null'
components:
  schemas:
    LibraryVoiceResponseModelCategory:
      type: string
      enum:
        - value: generated
        - value: cloned
        - value: premade
        - value: professional
        - value: famous
        - value: high_quality
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
    LibraryVoiceResponseModel:
      type: object
      properties:
        public_owner_id:
          type: string
        voice_id:
          type: string
        date_unix:
          type: integer
        name:
          type: string
        accent:
          type: string
        gender:
          type: string
        age:
          type: string
        descriptive:
          type: string
        use_case:
          type: string
        category:
          $ref: '#/components/schemas/LibraryVoiceResponseModelCategory'
        language:
          type:
            - string
            - 'null'
        locale:
          type:
            - string
            - 'null'
        description:
          type:
            - string
            - 'null'
        preview_url:
          type:
            - string
            - 'null'
        usage_character_count_1y:
          type: integer
        usage_character_count_7d:
          type: integer
        play_api_usage_character_count_1y:
          type: integer
        cloned_by_count:
          type: integer
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
        free_users_allowed:
          type: boolean
        live_moderation_enabled:
          type: boolean
        featured:
          type: boolean
        verified_languages:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VerifiedVoiceLanguageResponseModel'
        notice_period:
          type:
            - integer
            - 'null'
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
        image_url:
          type:
            - string
            - 'null'
        is_added_by_user:
          type:
            - boolean
            - 'null'
      required:
        - public_owner_id
        - voice_id
        - date_unix
        - name
        - accent
        - gender
        - age
        - descriptive
        - use_case
        - category
        - usage_character_count_1y
        - usage_character_count_7d
        - play_api_usage_character_count_1y
        - cloned_by_count
        - free_users_allowed
        - live_moderation_enabled
        - featured
    GetLibraryVoicesResponseModel:
      type: object
      properties:
        voices:
          type: array
          items:
            $ref: '#/components/schemas/LibraryVoiceResponseModel'
        has_more:
          type: boolean
        last_sort_id:
          type:
            - string
            - 'null'
      required:
        - voices
        - has_more

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.voices.findSimilarVoices({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.voices.find_similar_voices()

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

	url := "https://api.elevenlabs.io/v1/similar-voices"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"similarity_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"top_k\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/similar-voices")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"similarity_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"top_k\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/similar-voices")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"similarity_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"top_k\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/similar-voices', [
  'multipart' => [
    [
        'name' => 'audio_file',
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
var client = new RestClient("https://api.elevenlabs.io/v1/similar-voices");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"similarity_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"top_k\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
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
    "name": "audio_file",
    "fileName": "<file1>"
  ],
  [
    "name": "similarity_threshold",
    "value": 
  ],
  [
    "name": "top_k",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/similar-voices")! as URL,
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


# Get audio from sample

GET https://api.elevenlabs.io/v1/voices/{voice_id}/samples/{sample_id}/audio

Returns the audio corresponding to a sample attached to a voice.

Reference: https://elevenlabs.io/docs/api-reference/voices/samples/audio/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get audio from sample
  version: endpoint_voices/samples/audio.get
paths:
  /v1/voices/{voice_id}/samples/{sample_id}/audio:
    get:
      operationId: get
      summary: Get audio from sample
      description: Returns the audio corresponding to a sample attached to a voice.
      tags:
        - - subpackage_voices
          - subpackage_voices/samples
          - subpackage_voices/samples/audio
      parameters:
        - name: voice_id
          in: path
          description: >-
            ID of the voice to be used. You can use the [Get
            voices](/docs/api-reference/voices/search) endpoint list all the
            available voices.
          required: true
          schema:
            type: string
        - name: sample_id
          in: path
          description: >-
            ID of the sample to be used. You can use the [Get
            voices](/docs/api-reference/voices/get) endpoint list all the
            available samples for a voice.
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
                $ref: '#/components/schemas/voices_samples_audio_get_Response_200'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    voices_samples_audio_get_Response_200:
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
    await client.voices.samples.audio.get("voice_id", "sample_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.voices.samples.audio.get(
    voice_id="voice_id",
    sample_id="sample_id"
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

	url := "https://api.elevenlabs.io/v1/voices/voice_id/samples/sample_id/audio"

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

url = URI("https://api.elevenlabs.io/v1/voices/voice_id/samples/sample_id/audio")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices/voice_id/samples/sample_id/audio")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/voice_id/samples/sample_id/audio', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/voices/voice_id/samples/sample_id/audio");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/voice_id/samples/sample_id/audio")! as URL,
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


# Get default voice settings

GET https://api.elevenlabs.io/v1/voices/settings/default

Gets the default settings for voices. "similarity_boost" corresponds to"Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app.

Reference: https://elevenlabs.io/docs/api-reference/voices/settings/get-default


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get default voice settings
  version: endpoint_voices/settings.get_default
paths:
  /v1/voices/settings/default:
    get:
      operationId: get-default
      summary: Get default voice settings
      description: >-
        Gets the default settings for voices. "similarity_boost" corresponds
        to"Clarity + Similarity Enhancement" in the web app and "stability"
        corresponds to "Stability" slider in the web app.
      tags:
        - - subpackage_voices
          - subpackage_voices/settings
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
                $ref: '#/components/schemas/VoiceSettingsResponseModel'
components:
  schemas:
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

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.voices.settings.getDefault();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.voices.settings.get_default()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/voices/settings/default"

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

url = URI("https://api.elevenlabs.io/v1/voices/settings/default")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices/settings/default")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/settings/default', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/voices/settings/default");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/settings/default")! as URL,
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


# Get voice settings

GET https://api.elevenlabs.io/v1/voices/{voice_id}/settings

Returns the settings for a specific voice. "similarity_boost" corresponds to"Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app.

Reference: https://elevenlabs.io/docs/api-reference/voices/settings/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get voice settings
  version: endpoint_voices/settings.get
paths:
  /v1/voices/{voice_id}/settings:
    get:
      operationId: get
      summary: Get voice settings
      description: >-
        Returns the settings for a specific voice. "similarity_boost"
        corresponds to"Clarity + Similarity Enhancement" in the web app and
        "stability" corresponds to "Stability" slider in the web app.
      tags:
        - - subpackage_voices
          - subpackage_voices/settings
      parameters:
        - name: voice_id
          in: path
          description: >-
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices
            to list all the available voices.
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
                $ref: '#/components/schemas/VoiceSettingsResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
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

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.voices.settings.get("voice_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.voices.settings.get(
    voice_id="voice_id"
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

	url := "https://api.elevenlabs.io/v1/voices/voice_id/settings"

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

url = URI("https://api.elevenlabs.io/v1/voices/voice_id/settings")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices/voice_id/settings")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/voice_id/settings', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/voices/voice_id/settings");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/voice_id/settings")! as URL,
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


# Edit voice settings

POST https://api.elevenlabs.io/v1/voices/{voice_id}/settings/edit
Content-Type: application/json

Edit your settings for a specific voice. "similarity_boost" corresponds to "Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app.

Reference: https://elevenlabs.io/docs/api-reference/voices/settings/update


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Edit voice settings
  version: endpoint_voices/settings.update
paths:
  /v1/voices/{voice_id}/settings/edit:
    post:
      operationId: update
      summary: Edit voice settings
      description: >-
        Edit your settings for a specific voice. "similarity_boost" corresponds
        to "Clarity + Similarity Enhancement" in the web app and "stability"
        corresponds to "Stability" slider in the web app.
      tags:
        - - subpackage_voices
          - subpackage_voices/settings
      parameters:
        - name: voice_id
          in: path
          description: >-
            ID of the voice to be used. You can use the [Get
            voices](/docs/api-reference/voices/search) endpoint list all the
            available voices.
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
                $ref: '#/components/schemas/EditVoiceSettingsResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VoiceSettingsResponseModel'
components:
  schemas:
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
    EditVoiceSettingsResponseModel:
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
    await client.voices.settings.update("voice_id", {
        stability: 1,
        useSpeakerBoost: true,
        similarityBoost: 1,
        style: 0,
        speed: 1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.voices.settings.update(
    voice_id="voice_id",
    stability=1,
    use_speaker_boost=True,
    similarity_boost=1,
    style=0,
    speed=1
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

	url := "https://api.elevenlabs.io/v1/voices/voice_id/settings/edit"

	payload := strings.NewReader("{\n  \"stability\": 1,\n  \"use_speaker_boost\": true,\n  \"similarity_boost\": 1,\n  \"style\": 0,\n  \"speed\": 1\n}")

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

url = URI("https://api.elevenlabs.io/v1/voices/voice_id/settings/edit")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stability\": 1,\n  \"use_speaker_boost\": true,\n  \"similarity_boost\": 1,\n  \"style\": 0,\n  \"speed\": 1\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/voices/voice_id/settings/edit")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"stability\": 1,\n  \"use_speaker_boost\": true,\n  \"similarity_boost\": 1,\n  \"style\": 0,\n  \"speed\": 1\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/voices/voice_id/settings/edit', [
  'body' => '{
  "stability": 1,
  "use_speaker_boost": true,
  "similarity_boost": 1,
  "style": 0,
  "speed": 1
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/voices/voice_id/settings/edit");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stability\": 1,\n  \"use_speaker_boost\": true,\n  \"similarity_boost\": 1,\n  \"style\": 0,\n  \"speed\": 1\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "stability": 1,
  "use_speaker_boost": true,
  "similarity_boost": 1,
  "style": 0,
  "speed": 1
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/voice_id/settings/edit")! as URL,
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


# Create Forced Alignment

POST https://api.elevenlabs.io/v1/forced-alignment
Content-Type: multipart/form-data

Force align an audio file to text. Use this endpoint to get the timing information for each character and word in an audio file based on a provided text transcript.

Reference: https://elevenlabs.io/docs/api-reference/forced-alignment/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create Forced Alignment
  version: endpoint_forcedAlignment.create
paths:
  /v1/forced-alignment:
    post:
      operationId: create
      summary: Create Forced Alignment
      description: >-
        Force align an audio file to text. Use this endpoint to get the timing
        information for each character and word in an audio file based on a
        provided text transcript.
      tags:
        - - subpackage_forcedAlignment
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
                $ref: '#/components/schemas/ForcedAlignmentResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                text:
                  type: string
                enabled_spooled_file:
                  type: boolean
components:
  schemas:
    ForcedAlignmentCharacterResponseModel:
      type: object
      properties:
        text:
          type: string
        start:
          type: number
          format: double
        end:
          type: number
          format: double
      required:
        - text
        - start
        - end
    ForcedAlignmentWordResponseModel:
      type: object
      properties:
        text:
          type: string
        start:
          type: number
          format: double
        end:
          type: number
          format: double
        loss:
          type: number
          format: double
      required:
        - text
        - start
        - end
        - loss
    ForcedAlignmentResponseModel:
      type: object
      properties:
        characters:
          type: array
          items:
            $ref: '#/components/schemas/ForcedAlignmentCharacterResponseModel'
        words:
          type: array
          items:
            $ref: '#/components/schemas/ForcedAlignmentWordResponseModel'
        loss:
          type: number
          format: double
      required:
        - characters
        - words
        - loss

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.forcedAlignment.create({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.forced_alignment.create()

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

	url := "https://api.elevenlabs.io/v1/forced-alignment"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"enabled_spooled_file\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/forced-alignment")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"enabled_spooled_file\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/forced-alignment")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"enabled_spooled_file\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/forced-alignment', [
  'multipart' => [
    [
        'name' => 'file',
        'filename' => 'string',
        'contents' => null
    ],
    [
        'name' => 'text',
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
var client = new RestClient("https://api.elevenlabs.io/v1/forced-alignment");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"enabled_spooled_file\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
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
    "name": "text",
    "value": "string"
  ],
  [
    "name": "enabled_spooled_file",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/forced-alignment")! as URL,
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


# Get generated items

GET https://api.elevenlabs.io/v1/history

Returns a list of your generated audio.

Reference: https://elevenlabs.io/docs/api-reference/history/list


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get generated items
  version: endpoint_history.list
paths:
  /v1/history:
    get:
      operationId: list
      summary: Get generated items
      description: Returns a list of your generated audio.
      tags:
        - - subpackage_history
      parameters:
        - name: page_size
          in: query
          description: >-
            How many history items to return at maximum. Can not exceed 1000,
            defaults to 100.
          required: false
          schema:
            type: integer
        - name: start_after_history_item_id
          in: query
          description: >-
            After which ID to start fetching, use this parameter to paginate
            across a large collection of history items. In case this parameter
            is not provided history items will be fetched starting from the most
            recently created one ordered descending by their creation date.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: voice_id
          in: query
          description: >-
            ID of the voice to be filtered for. You can use the [Get
            voices](/docs/api-reference/voices/search) endpoint list all the
            available voices.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: model_id
          in: query
          description: >-
            Search term used for filtering history items. If provided, source
            becomes required.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: date_before_unix
          in: query
          description: Unix timestamp to filter history items before this date (exclusive).
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: date_after_unix
          in: query
          description: Unix timestamp to filter history items after this date (inclusive).
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: sort_direction
          in: query
          description: Sort direction for the results.
          required: false
          schema:
            oneOf:
              - $ref: '#/components/schemas/V1HistoryGetParametersSortDirectionSchema'
              - type: 'null'
        - name: search
          in: query
          description: search term used for filtering
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: source
          in: query
          description: Source of the generated history item
          required: false
          schema:
            oneOf:
              - $ref: '#/components/schemas/V1HistoryGetParametersSourceSchema'
              - type: 'null'
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
                $ref: '#/components/schemas/GetSpeechHistoryResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    V1HistoryGetParametersSortDirectionSchema:
      type: string
      enum:
        - value: asc
        - value: desc
    V1HistoryGetParametersSourceSchema:
      type: string
      enum:
        - value: TTS
        - value: STS
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
    GetSpeechHistoryResponseModel:
      type: object
      properties:
        history:
          type: array
          items:
            $ref: '#/components/schemas/SpeechHistoryItemResponseModel'
        last_history_item_id:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
        scanned_until:
          type:
            - integer
            - 'null'
      required:
        - history
        - has_more

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.history.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.history.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/history"

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

url = URI("https://api.elevenlabs.io/v1/history")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/history")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/history', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/history");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/history")! as URL,
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


---
**Navigation:** [← Previous](./36-get-audio-native-project-settings.md) | [Index](./index.md) | [Next →](./38-get-history-item.md)
