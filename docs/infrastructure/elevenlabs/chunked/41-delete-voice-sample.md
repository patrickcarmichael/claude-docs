**Navigation:** [← Previous](./40-create-pronunciation-dictionaries.md) | [Index](./index.md) | [Next →](./42-invite-user.md)

# Delete voice sample

DELETE https://api.elevenlabs.io/v1/voices/{voice_id}/samples/{sample_id}

Removes a sample by its ID.

Reference: https://elevenlabs.io/docs/api-reference/samples/delete


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete voice sample
  version: endpoint_samples.delete
paths:
  /v1/voices/{voice_id}/samples/{sample_id}:
    delete:
      operationId: delete
      summary: Delete voice sample
      description: Removes a sample by its ID.
      tags:
        - - subpackage_samples
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
                $ref: '#/components/schemas/DeleteSampleResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    DeleteSampleResponseModel:
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
    await client.samples.delete("voice_id", "sample_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.samples.delete(
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

	url := "https://api.elevenlabs.io/v1/voices/voice_id/samples/sample_id"

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

url = URI("https://api.elevenlabs.io/v1/voices/voice_id/samples/sample_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/voices/voice_id/samples/sample_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/voices/voice_id/samples/sample_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/voices/voice_id/samples/sample_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/voice_id/samples/sample_id")! as URL,
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


# Get character usage metrics

GET https://api.elevenlabs.io/v1/usage/character-stats

Returns the usage metrics for the current user or the entire workspace they are part of. The response provides a time axis based on the specified aggregation interval (default: day), with usage values for each interval along that axis. Usage is broken down by the selected breakdown type. For example, breakdown type "voice" will return the usage of each voice for each interval along the time axis.

Reference: https://elevenlabs.io/docs/api-reference/usage/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get character usage metrics
  version: endpoint_usage.get
paths:
  /v1/usage/character-stats:
    get:
      operationId: get
      summary: Get character usage metrics
      description: >-
        Returns the usage metrics for the current user or the entire workspace
        they are part of. The response provides a time axis based on the
        specified aggregation interval (default: day), with usage values for
        each interval along that axis. Usage is broken down by the selected
        breakdown type. For example, breakdown type "voice" will return the
        usage of each voice for each interval along the time axis.
      tags:
        - - subpackage_usage
      parameters:
        - name: start_unix
          in: query
          description: >-
            UTC Unix timestamp for the start of the usage window, in
            milliseconds. To include the first day of the window, the timestamp
            should be at 00:00:00 of that day.
          required: true
          schema:
            type: integer
        - name: end_unix
          in: query
          description: >-
            UTC Unix timestamp for the end of the usage window, in milliseconds.
            To include the last day of the window, the timestamp should be at
            23:59:59 of that day.
          required: true
          schema:
            type: integer
        - name: include_workspace_metrics
          in: query
          description: Whether or not to include the statistics of the entire workspace.
          required: false
          schema:
            type: boolean
        - name: breakdown_type
          in: query
          description: >-
            How to break down the information. Cannot be "user" if
            include_workspace_metrics is False.
          required: false
          schema:
            $ref: '#/components/schemas/BreakdownTypes'
        - name: aggregation_interval
          in: query
          description: >-
            How to aggregate usage data over time. Can be "hour", "day", "week",
            "month", or "cumulative".
          required: false
          schema:
            $ref: '#/components/schemas/UsageAggregationInterval'
        - name: aggregation_bucket_size
          in: query
          description: >-
            Aggregation bucket size in seconds. Overrides the aggregation
            interval.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: metric
          in: query
          description: Which metric to aggregate.
          required: false
          schema:
            $ref: '#/components/schemas/MetricType'
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
                $ref: '#/components/schemas/UsageCharactersResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    BreakdownTypes:
      type: string
      enum:
        - value: none
        - value: voice
        - value: voice_multiplier
        - value: user
        - value: groups
        - value: api_keys
        - value: all_api_keys
        - value: product_type
        - value: model
        - value: resource
        - value: request_queue
        - value: region
        - value: subresource_id
        - value: reporting_workspace_id
        - value: has_api_key
        - value: request_source
    UsageAggregationInterval:
      type: string
      enum:
        - value: hour
        - value: day
        - value: week
        - value: month
        - value: cumulative
    MetricType:
      type: string
      enum:
        - value: credits
        - value: tts_characters
        - value: minutes_used
        - value: request_count
        - value: ttfb_avg
        - value: ttfb_p95
        - value: fiat_units_spent
        - value: concurrency
        - value: concurrency_average
    UsageCharactersResponseModel:
      type: object
      properties:
        time:
          type: array
          items:
            type: integer
        usage:
          type: object
          additionalProperties:
            type: array
            items:
              type: number
              format: double
      required:
        - time
        - usage

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.usage.get({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.usage.get(
    start_unix=,
    end_unix=
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

	url := "https://api.elevenlabs.io/v1/usage/character-stats?start_unix=1685574000&end_unix=1688165999"

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

url = URI("https://api.elevenlabs.io/v1/usage/character-stats?start_unix=1685574000&end_unix=1688165999")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/usage/character-stats?start_unix=1685574000&end_unix=1688165999")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/usage/character-stats?start_unix=1685574000&end_unix=1688165999', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/usage/character-stats?start_unix=1685574000&end_unix=1688165999");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/usage/character-stats?start_unix=1685574000&end_unix=1688165999")! as URL,
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


# Get user

GET https://api.elevenlabs.io/v1/user

Gets information about the user

Reference: https://elevenlabs.io/docs/api-reference/user/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get user
  version: endpoint_user.get
paths:
  /v1/user:
    get:
      operationId: get
      summary: Get user
      description: Gets information about the user
      tags:
        - - subpackage_user
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
                $ref: '#/components/schemas/UserResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    SubscriptionResponseModelCurrency:
      type: string
      enum:
        - value: usd
        - value: eur
        - value: inr
    SubscriptionStatusType:
      type: string
      enum:
        - value: trialing
        - value: active
        - value: incomplete
        - value: past_due
        - value: free
        - value: free_disabled
    SubscriptionResponseModelBillingPeriod:
      type: string
      enum:
        - value: monthly_period
        - value: annual_period
    SubscriptionResponseModelCharacterRefreshPeriod:
      type: string
      enum:
        - value: monthly_period
        - value: annual_period
    SubscriptionResponseModel:
      type: object
      properties:
        tier:
          type: string
        character_count:
          type: integer
        character_limit:
          type: integer
        max_character_limit_extension:
          type:
            - integer
            - 'null'
        can_extend_character_limit:
          type: boolean
        allowed_to_extend_character_limit:
          type: boolean
        next_character_count_reset_unix:
          type:
            - integer
            - 'null'
        voice_slots_used:
          type: integer
        professional_voice_slots_used:
          type: integer
        voice_limit:
          type: integer
        max_voice_add_edits:
          type:
            - integer
            - 'null'
        voice_add_edit_counter:
          type: integer
        professional_voice_limit:
          type: integer
        can_extend_voice_limit:
          type: boolean
        can_use_instant_voice_cloning:
          type: boolean
        can_use_professional_voice_cloning:
          type: boolean
        currency:
          oneOf:
            - $ref: '#/components/schemas/SubscriptionResponseModelCurrency'
            - type: 'null'
        status:
          $ref: '#/components/schemas/SubscriptionStatusType'
        billing_period:
          oneOf:
            - $ref: '#/components/schemas/SubscriptionResponseModelBillingPeriod'
            - type: 'null'
        character_refresh_period:
          oneOf:
            - $ref: >-
                #/components/schemas/SubscriptionResponseModelCharacterRefreshPeriod
            - type: 'null'
      required:
        - tier
        - character_count
        - character_limit
        - max_character_limit_extension
        - can_extend_character_limit
        - allowed_to_extend_character_limit
        - voice_slots_used
        - professional_voice_slots_used
        - voice_limit
        - voice_add_edit_counter
        - professional_voice_limit
        - can_extend_voice_limit
        - can_use_instant_voice_cloning
        - can_use_professional_voice_cloning
        - status
    UserResponseModel:
      type: object
      properties:
        user_id:
          type: string
        subscription:
          $ref: '#/components/schemas/SubscriptionResponseModel'
        is_new_user:
          type: boolean
        xi_api_key:
          type:
            - string
            - 'null'
        can_use_delayed_payment_methods:
          type: boolean
        is_onboarding_completed:
          type: boolean
        is_onboarding_checklist_completed:
          type: boolean
        first_name:
          type:
            - string
            - 'null'
        is_api_key_hashed:
          type: boolean
        xi_api_key_preview:
          type:
            - string
            - 'null'
        referral_link_code:
          type:
            - string
            - 'null'
        partnerstack_partner_default_link:
          type:
            - string
            - 'null'
        created_at:
          type: integer
      required:
        - user_id
        - subscription
        - is_new_user
        - can_use_delayed_payment_methods
        - is_onboarding_completed
        - is_onboarding_checklist_completed
        - created_at

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.user.get();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.user.get()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/user"

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

url = URI("https://api.elevenlabs.io/v1/user")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/user")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/user', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/user");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/user")! as URL,
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


# Get user subscription

GET https://api.elevenlabs.io/v1/user/subscription

Gets extended information about the users subscription

Reference: https://elevenlabs.io/docs/api-reference/user/subscription/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get user subscription
  version: endpoint_user/subscription.get
paths:
  /v1/user/subscription:
    get:
      operationId: get
      summary: Get user subscription
      description: Gets extended information about the users subscription
      tags:
        - - subpackage_user
          - subpackage_user/subscription
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
                $ref: '#/components/schemas/ExtendedSubscriptionResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    ExtendedSubscriptionResponseModelCurrency:
      type: string
      enum:
        - value: usd
        - value: eur
        - value: inr
    SubscriptionStatusType:
      type: string
      enum:
        - value: trialing
        - value: active
        - value: incomplete
        - value: past_due
        - value: free
        - value: free_disabled
    ExtendedSubscriptionResponseModelBillingPeriod:
      type: string
      enum:
        - value: monthly_period
        - value: annual_period
    ExtendedSubscriptionResponseModelCharacterRefreshPeriod:
      type: string
      enum:
        - value: monthly_period
        - value: annual_period
    DiscountResposneModel:
      type: object
      properties:
        discount_percent_off:
          type:
            - number
            - 'null'
          format: double
        discount_amount_off:
          type:
            - number
            - 'null'
          format: double
    InvoiceResponseModelPaymentIntentStatus:
      type: string
      enum:
        - value: canceled
        - value: processing
        - value: requires_action
        - value: requires_capture
        - value: requires_confirmation
        - value: requires_payment_method
        - value: succeeded
    InvoiceResponseModel:
      type: object
      properties:
        amount_due_cents:
          type: integer
        subtotal_cents:
          type:
            - integer
            - 'null'
        tax_cents:
          type:
            - integer
            - 'null'
        discount_percent_off:
          type:
            - number
            - 'null'
          format: double
        discount_amount_off:
          type:
            - number
            - 'null'
          format: double
        discounts:
          type: array
          items:
            $ref: '#/components/schemas/DiscountResposneModel'
        next_payment_attempt_unix:
          type: integer
        payment_intent_status:
          oneOf:
            - $ref: '#/components/schemas/InvoiceResponseModelPaymentIntentStatus'
            - type: 'null'
      required:
        - amount_due_cents
        - discounts
        - next_payment_attempt_unix
        - payment_intent_status
    PendingSubscriptionSwitchResponseModelNextTier:
      type: string
      enum:
        - value: free
        - value: starter
        - value: creator
        - value: pro
        - value: growing_business
        - value: scale_2024_08_10
        - value: grant_tier_1_2025_07_23
        - value: grant_tier_2_2025_07_23
        - value: trial
        - value: enterprise
    PendingSubscriptionSwitchResponseModelNextBillingPeriod:
      type: string
      enum:
        - value: monthly_period
        - value: annual_period
    PendingSubscriptionSwitchResponseModel:
      type: object
      properties:
        kind:
          type: string
          enum:
            - type: stringLiteral
              value: change
        next_tier:
          $ref: '#/components/schemas/PendingSubscriptionSwitchResponseModelNextTier'
        next_billing_period:
          $ref: >-
            #/components/schemas/PendingSubscriptionSwitchResponseModelNextBillingPeriod
        timestamp_seconds:
          type: integer
      required:
        - next_tier
        - next_billing_period
        - timestamp_seconds
    PendingCancellationResponseModel:
      type: object
      properties:
        kind:
          type: string
          enum:
            - type: stringLiteral
              value: cancellation
        timestamp_seconds:
          type: integer
      required:
        - timestamp_seconds
    ExtendedSubscriptionResponseModelPendingChange:
      oneOf:
        - $ref: '#/components/schemas/PendingSubscriptionSwitchResponseModel'
        - $ref: '#/components/schemas/PendingCancellationResponseModel'
    ExtendedSubscriptionResponseModel:
      type: object
      properties:
        tier:
          type: string
        character_count:
          type: integer
        character_limit:
          type: integer
        max_character_limit_extension:
          type:
            - integer
            - 'null'
        can_extend_character_limit:
          type: boolean
        allowed_to_extend_character_limit:
          type: boolean
        next_character_count_reset_unix:
          type:
            - integer
            - 'null'
        voice_slots_used:
          type: integer
        professional_voice_slots_used:
          type: integer
        voice_limit:
          type: integer
        max_voice_add_edits:
          type:
            - integer
            - 'null'
        voice_add_edit_counter:
          type: integer
        professional_voice_limit:
          type: integer
        can_extend_voice_limit:
          type: boolean
        can_use_instant_voice_cloning:
          type: boolean
        can_use_professional_voice_cloning:
          type: boolean
        currency:
          oneOf:
            - $ref: '#/components/schemas/ExtendedSubscriptionResponseModelCurrency'
            - type: 'null'
        status:
          $ref: '#/components/schemas/SubscriptionStatusType'
        billing_period:
          oneOf:
            - $ref: >-
                #/components/schemas/ExtendedSubscriptionResponseModelBillingPeriod
            - type: 'null'
        character_refresh_period:
          oneOf:
            - $ref: >-
                #/components/schemas/ExtendedSubscriptionResponseModelCharacterRefreshPeriod
            - type: 'null'
        next_invoice:
          oneOf:
            - $ref: '#/components/schemas/InvoiceResponseModel'
            - type: 'null'
        open_invoices:
          type: array
          items:
            $ref: '#/components/schemas/InvoiceResponseModel'
        has_open_invoices:
          type: boolean
        pending_change:
          oneOf:
            - $ref: >-
                #/components/schemas/ExtendedSubscriptionResponseModelPendingChange
            - type: 'null'
      required:
        - tier
        - character_count
        - character_limit
        - max_character_limit_extension
        - can_extend_character_limit
        - allowed_to_extend_character_limit
        - voice_slots_used
        - professional_voice_slots_used
        - voice_limit
        - voice_add_edit_counter
        - professional_voice_limit
        - can_extend_voice_limit
        - can_use_instant_voice_cloning
        - can_use_professional_voice_cloning
        - status
        - open_invoices
        - has_open_invoices

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.user.subscription.get();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.user.subscription.get()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/user/subscription"

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

url = URI("https://api.elevenlabs.io/v1/user/subscription")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/user/subscription")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/user/subscription', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/user/subscription");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/user/subscription")! as URL,
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


# Get shared voices

GET https://api.elevenlabs.io/v1/shared-voices

Retrieves a list of shared voices.

Reference: https://elevenlabs.io/docs/api-reference/voice-library/get-shared


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get shared voices
  version: endpoint_voices.get_shared
paths:
  /v1/shared-voices:
    get:
      operationId: get-shared
      summary: Get shared voices
      description: Retrieves a list of shared voices.
      tags:
        - - subpackage_voices
      parameters:
        - name: page_size
          in: query
          description: >-
            How many shared voices to return at maximum. Can not exceed 100,
            defaults to 30.
          required: false
          schema:
            type: integer
        - name: category
          in: query
          description: Voice category used for filtering
          required: false
          schema:
            $ref: '#/components/schemas/V1SharedVoicesGetParametersCategory'
        - name: gender
          in: query
          description: Gender used for filtering
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: age
          in: query
          description: Age used for filtering
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: accent
          in: query
          description: Accent used for filtering
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: language
          in: query
          description: Language used for filtering
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: locale
          in: query
          description: Locale used for filtering
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: search
          in: query
          description: Search term used for filtering
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: use_cases
          in: query
          description: Use-case used for filtering
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: descriptives
          in: query
          description: Search term used for filtering
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: featured
          in: query
          description: Filter featured voices
          required: false
          schema:
            type: boolean
        - name: min_notice_period_days
          in: query
          description: >-
            Filter voices with a minimum notice period of the given number of
            days.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: include_custom_rates
          in: query
          description: Include/exclude voices with custom rates
          required: false
          schema:
            type:
              - boolean
              - 'null'
        - name: include_live_moderated
          in: query
          description: Include/exclude voices that are live moderated
          required: false
          schema:
            type:
              - boolean
              - 'null'
        - name: reader_app_enabled
          in: query
          description: Filter voices that are enabled for the reader app
          required: false
          schema:
            type: boolean
        - name: owner_id
          in: query
          description: Filter voices by public owner ID
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: sort
          in: query
          description: Sort criteria
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: page
          in: query
          required: false
          schema:
            type: integer
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
components:
  schemas:
    V1SharedVoicesGetParametersCategory:
      type: string
      enum:
        - value: professional
        - value: famous
        - value: high_quality
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
    await client.voices.getShared({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.voices.get_shared()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/shared-voices"

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

url = URI("https://api.elevenlabs.io/v1/shared-voices")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/shared-voices")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/shared-voices', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/shared-voices");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/shared-voices")! as URL,
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


# Add shared voice

POST https://api.elevenlabs.io/v1/voices/add/{public_user_id}/{voice_id}
Content-Type: application/json

Add a shared voice to your collection of Voices

Reference: https://elevenlabs.io/docs/api-reference/voice-library/share


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Add shared voice
  version: endpoint_voices.share
paths:
  /v1/voices/add/{public_user_id}/{voice_id}:
    post:
      operationId: share
      summary: Add shared voice
      description: Add a shared voice to your collection of Voices
      tags:
        - - subpackage_voices
      parameters:
        - name: public_user_id
          in: path
          description: Public user ID used to publicly identify ElevenLabs users.
          required: true
          schema:
            type: string
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
                $ref: '#/components/schemas/AddVoiceResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Add_shared_voice_v1_voices_add__public_user_id___voice_id__post
components:
  schemas:
    Body_Add_shared_voice_v1_voices_add__public_user_id___voice_id__post:
      type: object
      properties:
        new_name:
          type: string
      required:
        - new_name
    AddVoiceResponseModel:
      type: object
      properties:
        voice_id:
          type: string
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
    await client.voices.share("public_user_id", "voice_id", {
        newName: "John Smith",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.voices.share(
    public_user_id="public_user_id",
    voice_id="voice_id",
    new_name="John Smith"
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

	url := "https://api.elevenlabs.io/v1/voices/add/public_user_id/voice_id"

	payload := strings.NewReader("{\n  \"new_name\": \"John Smith\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/voices/add/public_user_id/voice_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"new_name\": \"John Smith\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/voices/add/public_user_id/voice_id")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"new_name\": \"John Smith\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/voices/add/public_user_id/voice_id', [
  'body' => '{
  "new_name": "John Smith"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/voices/add/public_user_id/voice_id");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"new_name\": \"John Smith\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["new_name": "John Smith"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/add/public_user_id/voice_id")! as URL,
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


# Get service accounts

GET https://api.elevenlabs.io/v1/service-accounts

List all service accounts in the workspace

Reference: https://elevenlabs.io/docs/api-reference/service-accounts/list


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get service accounts
  version: endpoint_serviceAccounts.list
paths:
  /v1/service-accounts:
    get:
      operationId: list
      summary: Get service accounts
      description: List all service accounts in the workspace
      tags:
        - - subpackage_serviceAccounts
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
                $ref: '#/components/schemas/WorkspaceServiceAccountListResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    WorkspaceApiKeyResponseModelPermissionsItems:
      type: string
      enum:
        - value: text_to_speech
        - value: speech_to_speech
        - value: speech_to_text
        - value: models_read
        - value: models_write
        - value: voices_read
        - value: voices_write
        - value: speech_history_read
        - value: speech_history_write
        - value: sound_generation
        - value: audio_isolation
        - value: voice_generation
        - value: dubbing_read
        - value: dubbing_write
        - value: pronunciation_dictionaries_read
        - value: pronunciation_dictionaries_write
        - value: user_read
        - value: user_write
        - value: projects_read
        - value: projects_write
        - value: audio_native_read
        - value: audio_native_write
        - value: workspace_read
        - value: workspace_write
        - value: forced_alignment
        - value: convai_read
        - value: convai_write
        - value: music_generation
    WorkspaceApiKeyResponseModel:
      type: object
      properties:
        name:
          type: string
        hint:
          type: string
        key_id:
          type: string
        service_account_user_id:
          type: string
        created_at_unix:
          type:
            - integer
            - 'null'
        is_disabled:
          type: boolean
        permissions:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/WorkspaceApiKeyResponseModelPermissionsItems'
        character_limit:
          type:
            - integer
            - 'null'
        character_count:
          type:
            - integer
            - 'null'
      required:
        - name
        - hint
        - key_id
        - service_account_user_id
    WorkspaceServiceAccountResponseModel:
      type: object
      properties:
        service_account_user_id:
          type: string
        name:
          type: string
        created_at_unix:
          type:
            - integer
            - 'null'
        api-keys:
          type: array
          items:
            $ref: '#/components/schemas/WorkspaceApiKeyResponseModel'
      required:
        - service_account_user_id
        - name
        - api-keys
    WorkspaceServiceAccountListResponseModel:
      type: object
      properties:
        service-accounts:
          type: array
          items:
            $ref: '#/components/schemas/WorkspaceServiceAccountResponseModel'
      required:
        - service-accounts

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.serviceAccounts.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.service_accounts.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/service-accounts"

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

url = URI("https://api.elevenlabs.io/v1/service-accounts")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/service-accounts")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/service-accounts', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/service-accounts");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/service-accounts")! as URL,
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


# Get API keys

GET https://api.elevenlabs.io/v1/service-accounts/{service_account_user_id}/api-keys

Get all API keys for a service account

Reference: https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/list


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get API keys
  version: endpoint_serviceAccounts/apiKeys.list
paths:
  /v1/service-accounts/{service_account_user_id}/api-keys:
    get:
      operationId: list
      summary: Get API keys
      description: Get all API keys for a service account
      tags:
        - - subpackage_serviceAccounts
          - subpackage_serviceAccounts/apiKeys
      parameters:
        - name: service_account_user_id
          in: path
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
                $ref: '#/components/schemas/WorkspaceApiKeyListResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    WorkspaceApiKeyResponseModelPermissionsItems:
      type: string
      enum:
        - value: text_to_speech
        - value: speech_to_speech
        - value: speech_to_text
        - value: models_read
        - value: models_write
        - value: voices_read
        - value: voices_write
        - value: speech_history_read
        - value: speech_history_write
        - value: sound_generation
        - value: audio_isolation
        - value: voice_generation
        - value: dubbing_read
        - value: dubbing_write
        - value: pronunciation_dictionaries_read
        - value: pronunciation_dictionaries_write
        - value: user_read
        - value: user_write
        - value: projects_read
        - value: projects_write
        - value: audio_native_read
        - value: audio_native_write
        - value: workspace_read
        - value: workspace_write
        - value: forced_alignment
        - value: convai_read
        - value: convai_write
        - value: music_generation
    WorkspaceApiKeyResponseModel:
      type: object
      properties:
        name:
          type: string
        hint:
          type: string
        key_id:
          type: string
        service_account_user_id:
          type: string
        created_at_unix:
          type:
            - integer
            - 'null'
        is_disabled:
          type: boolean
        permissions:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/WorkspaceApiKeyResponseModelPermissionsItems'
        character_limit:
          type:
            - integer
            - 'null'
        character_count:
          type:
            - integer
            - 'null'
      required:
        - name
        - hint
        - key_id
        - service_account_user_id
    WorkspaceApiKeyListResponseModel:
      type: object
      properties:
        api-keys:
          type: array
          items:
            $ref: '#/components/schemas/WorkspaceApiKeyResponseModel'
      required:
        - api-keys

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.serviceAccounts.apiKeys.list("service_account_user_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.service_accounts.api_keys.list(
    service_account_user_id="service_account_user_id"
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

	url := "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys"

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

url = URI("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")! as URL,
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


# Create API key

POST https://api.elevenlabs.io/v1/service-accounts/{service_account_user_id}/api-keys
Content-Type: application/json

Create a new API key for a service account

Reference: https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create API key
  version: endpoint_serviceAccounts/apiKeys.create
paths:
  /v1/service-accounts/{service_account_user_id}/api-keys:
    post:
      operationId: create
      summary: Create API key
      description: Create a new API key for a service account
      tags:
        - - subpackage_serviceAccounts
          - subpackage_serviceAccounts/apiKeys
      parameters:
        - name: service_account_user_id
          in: path
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
                $ref: '#/components/schemas/WorkspaceCreateApiKeyResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_create_service_account_api_key_v1_service_accounts__service_account_user_id__api_keys_post
components:
  schemas:
    BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissionsOneOf0Items:
      type: string
      enum:
        - value: text_to_speech
        - value: speech_to_speech
        - value: speech_to_text
        - value: models_read
        - value: models_write
        - value: voices_read
        - value: voices_write
        - value: speech_history_read
        - value: speech_history_write
        - value: sound_generation
        - value: audio_isolation
        - value: voice_generation
        - value: dubbing_read
        - value: dubbing_write
        - value: pronunciation_dictionaries_read
        - value: pronunciation_dictionaries_write
        - value: user_read
        - value: user_write
        - value: projects_read
        - value: projects_write
        - value: audio_native_read
        - value: audio_native_write
        - value: workspace_read
        - value: workspace_write
        - value: forced_alignment
        - value: convai_read
        - value: convai_write
        - value: music_generation
    BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions0:
      type: array
      items:
        $ref: >-
          #/components/schemas/BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissionsOneOf0Items
    BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions:
      oneOf:
        - $ref: >-
            #/components/schemas/BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions0
        - type: string
          enum:
            - type: stringLiteral
              value: all
    Body_create_service_account_api_key_v1_service_accounts__service_account_user_id__api_keys_post:
      type: object
      properties:
        name:
          type: string
        permissions:
          $ref: >-
            #/components/schemas/BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions
        character_limit:
          type:
            - integer
            - 'null'
      required:
        - name
        - permissions
    WorkspaceCreateApiKeyResponseModel:
      type: object
      properties:
        xi-api-key:
          type: string
      required:
        - xi-api-key

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.serviceAccounts.apiKeys.create("service_account_user_id", {
        name: "string",
        permissions: [
            "text_to_speech",
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

client.service_accounts.api_keys.create(
    service_account_user_id="service_account_user_id",
    name="string",
    permissions=[
        "text_to_speech"
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

	url := "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys"

	payload := strings.NewReader("{\n  \"name\": \"string\",\n  \"permissions\": [\n    \"text_to_speech\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"string\",\n  \"permissions\": [\n    \"text_to_speech\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"string\",\n  \"permissions\": [\n    \"text_to_speech\"\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys', [
  'body' => '{
  "name": "string",
  "permissions": [
    "text_to_speech"
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
var client = new RestClient("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"string\",\n  \"permissions\": [\n    \"text_to_speech\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "name": "string",
  "permissions": ["text_to_speech"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")! as URL,
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


# Delete API key

DELETE https://api.elevenlabs.io/v1/service-accounts/{service_account_user_id}/api-keys/{api_key_id}

Delete an existing API key for a service account

Reference: https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/delete


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete API key
  version: endpoint_serviceAccounts/apiKeys.delete
paths:
  /v1/service-accounts/{service_account_user_id}/api-keys/{api_key_id}:
    delete:
      operationId: delete
      summary: Delete API key
      description: Delete an existing API key for a service account
      tags:
        - - subpackage_serviceAccounts
          - subpackage_serviceAccounts/apiKeys
      parameters:
        - name: service_account_user_id
          in: path
          required: true
          schema:
            type: string
        - name: api_key_id
          in: path
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
    await client.serviceAccounts.apiKeys.delete("service_account_user_id", "api_key_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.service_accounts.api_keys.delete(
    service_account_user_id="service_account_user_id",
    api_key_id="api_key_id"
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

	url := "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id"

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

url = URI("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id")! as URL,
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


# Update API key

PATCH https://api.elevenlabs.io/v1/service-accounts/{service_account_user_id}/api-keys/{api_key_id}
Content-Type: application/json

Update an existing API key for a service account

Reference: https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/update


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update API key
  version: endpoint_serviceAccounts/apiKeys.update
paths:
  /v1/service-accounts/{service_account_user_id}/api-keys/{api_key_id}:
    patch:
      operationId: update
      summary: Update API key
      description: Update an existing API key for a service account
      tags:
        - - subpackage_serviceAccounts
          - subpackage_serviceAccounts/apiKeys
      parameters:
        - name: service_account_user_id
          in: path
          required: true
          schema:
            type: string
        - name: api_key_id
          in: path
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
                description: Any type
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_edit_service_account_api_key_v1_service_accounts__service_account_user_id__api_keys__api_key_id__patch
components:
  schemas:
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissionsOneOf0Items:
      type: string
      enum:
        - value: text_to_speech
        - value: speech_to_speech
        - value: speech_to_text
        - value: models_read
        - value: models_write
        - value: voices_read
        - value: voices_write
        - value: speech_history_read
        - value: speech_history_write
        - value: sound_generation
        - value: audio_isolation
        - value: voice_generation
        - value: dubbing_read
        - value: dubbing_write
        - value: pronunciation_dictionaries_read
        - value: pronunciation_dictionaries_write
        - value: user_read
        - value: user_write
        - value: projects_read
        - value: projects_write
        - value: audio_native_read
        - value: audio_native_write
        - value: workspace_read
        - value: workspace_write
        - value: forced_alignment
        - value: convai_read
        - value: convai_write
        - value: music_generation
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions0:
      type: array
      items:
        $ref: >-
          #/components/schemas/BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissionsOneOf0Items
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions:
      oneOf:
        - $ref: >-
            #/components/schemas/BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions0
        - type: string
          enum:
            - type: stringLiteral
              value: all
    Body_edit_service_account_api_key_v1_service_accounts__service_account_user_id__api_keys__api_key_id__patch:
      type: object
      properties:
        is_enabled:
          type: boolean
        name:
          type: string
        permissions:
          $ref: >-
            #/components/schemas/BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions
        character_limit:
          type:
            - integer
            - 'null'
      required:
        - is_enabled
        - name
        - permissions

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.serviceAccounts.apiKeys.update("service_account_user_id", "api_key_id", {
        isEnabled: true,
        name: "Sneaky Fox",
        permissions: [
            "text_to_speech",
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

client.service_accounts.api_keys.update(
    service_account_user_id="service_account_user_id",
    api_key_id="api_key_id",
    is_enabled=True,
    name="Sneaky Fox",
    permissions=[
        "text_to_speech"
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

	url := "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id"

	payload := strings.NewReader("{\n  \"is_enabled\": true,\n  \"name\": \"Sneaky Fox\",\n  \"permissions\": [\n    \"text_to_speech\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"is_enabled\": true,\n  \"name\": \"Sneaky Fox\",\n  \"permissions\": [\n    \"text_to_speech\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"is_enabled\": true,\n  \"name\": \"Sneaky Fox\",\n  \"permissions\": [\n    \"text_to_speech\"\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id', [
  'body' => '{
  "is_enabled": true,
  "name": "Sneaky Fox",
  "permissions": [
    "text_to_speech"
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
var client = new RestClient("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"is_enabled\": true,\n  \"name\": \"Sneaky Fox\",\n  \"permissions\": [\n    \"text_to_speech\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "is_enabled": true,
  "name": "Sneaky Fox",
  "permissions": ["text_to_speech"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id")! as URL,
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


# Search user group

GET https://api.elevenlabs.io/v1/workspace/groups/search

Searches for user groups in the workspace. Multiple or no groups may be returned.

Reference: https://elevenlabs.io/docs/api-reference/workspace/groups/search


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Search user group
  version: endpoint_workspace/groups.search
paths:
  /v1/workspace/groups/search:
    get:
      operationId: search
      summary: Search user group
      description: >-
        Searches for user groups in the workspace. Multiple or no groups may be
        returned.
      tags:
        - - subpackage_workspace
          - subpackage_workspace/groups
      parameters:
        - name: name
          in: query
          description: Name of the target group.
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
                type: array
                items:
                  $ref: '#/components/schemas/WorkspaceGroupByNameResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    WorkspaceGroupByNameResponseModel:
      type: object
      properties:
        name:
          type: string
        id:
          type: string
        members_emails:
          type: array
          items:
            type: string
      required:
        - name
        - id
        - members_emails

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.workspace.groups.search({
        name: "name",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.workspace.groups.search(
    name="name"
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

	url := "https://api.elevenlabs.io/v1/workspace/groups/search?name=name"

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

url = URI("https://api.elevenlabs.io/v1/workspace/groups/search?name=name")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/workspace/groups/search?name=name")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/groups/search?name=name', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/workspace/groups/search?name=name");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/groups/search?name=name")! as URL,
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


# Remove member from user group

POST https://api.elevenlabs.io/v1/workspace/groups/{group_id}/members/remove
Content-Type: application/json

Removes a member from the specified group. This endpoint may only be called by workspace administrators.

Reference: https://elevenlabs.io/docs/api-reference/workspace/groups/members/remove


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Remove member from user group
  version: endpoint_workspace/groups/members.remove
paths:
  /v1/workspace/groups/{group_id}/members/remove:
    post:
      operationId: remove
      summary: Remove member from user group
      description: >-
        Removes a member from the specified group. This endpoint may only be
        called by workspace administrators.
      tags:
        - - subpackage_workspace
          - subpackage_workspace/groups
          - subpackage_workspace/groups/members
      parameters:
        - name: group_id
          in: path
          description: The ID of the target group.
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
                $ref: '#/components/schemas/DeleteWorkspaceGroupMemberResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Delete_member_from_user_group_v1_workspace_groups__group_id__members_remove_post
components:
  schemas:
    Body_Delete_member_from_user_group_v1_workspace_groups__group_id__members_remove_post:
      type: object
      properties:
        email:
          type: string
      required:
        - email
    DeleteWorkspaceGroupMemberResponseModel:
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
    await client.workspace.groups.members.remove("group_id", {
        email: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.workspace.groups.members.remove(
    group_id="group_id",
    email="string"
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

	url := "https://api.elevenlabs.io/v1/workspace/groups/group_id/members/remove"

	payload := strings.NewReader("{\n  \"email\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/workspace/groups/group_id/members/remove")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/groups/group_id/members/remove")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"string\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/groups/group_id/members/remove', [
  'body' => '{
  "email": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/workspace/groups/group_id/members/remove");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"email\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["email": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/groups/group_id/members/remove")! as URL,
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


# Add member to user group

POST https://api.elevenlabs.io/v1/workspace/groups/{group_id}/members
Content-Type: application/json

Adds a member of your workspace to the specified group. This endpoint may only be called by workspace administrators.

Reference: https://elevenlabs.io/docs/api-reference/workspace/groups/members/add


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Add member to user group
  version: endpoint_workspace/groups/members.add
paths:
  /v1/workspace/groups/{group_id}/members:
    post:
      operationId: add
      summary: Add member to user group
      description: >-
        Adds a member of your workspace to the specified group. This endpoint
        may only be called by workspace administrators.
      tags:
        - - subpackage_workspace
          - subpackage_workspace/groups
          - subpackage_workspace/groups/members
      parameters:
        - name: group_id
          in: path
          description: The ID of the target group.
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
                $ref: '#/components/schemas/AddWorkspaceGroupMemberResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Add_member_to_user_group_v1_workspace_groups__group_id__members_post
components:
  schemas:
    Body_Add_member_to_user_group_v1_workspace_groups__group_id__members_post:
      type: object
      properties:
        email:
          type: string
      required:
        - email
    AddWorkspaceGroupMemberResponseModel:
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
    await client.workspace.groups.members.add("group_id", {
        email: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.workspace.groups.members.add(
    group_id="group_id",
    email="string"
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

	url := "https://api.elevenlabs.io/v1/workspace/groups/group_id/members"

	payload := strings.NewReader("{\n  \"email\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/workspace/groups/group_id/members")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/groups/group_id/members")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"string\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/groups/group_id/members', [
  'body' => '{
  "email": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/workspace/groups/group_id/members");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"email\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["email": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/groups/group_id/members")! as URL,
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
**Navigation:** [← Previous](./40-create-pronunciation-dictionaries.md) | [Index](./index.md) | [Next →](./42-invite-user.md)
