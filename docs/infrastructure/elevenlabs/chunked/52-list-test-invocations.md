**Navigation:** [← Previous](./51-get-test-invocation.md) | [Index](./index.md) | [Next →](./53-delete-secret.md)

# List test invocations

GET https://api.elevenlabs.io/v1/convai/test-invocations

Lists all test invocations with pagination support and optional search filtering.

Reference: https://elevenlabs.io/docs/api-reference/tests/test-invocations/list


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List Test Invocations
  version: endpoint_conversationalAi/tests/invocations.list
paths:
  /v1/convai/test-invocations:
    get:
      operationId: list
      summary: List Test Invocations
      description: >-
        Lists all test invocations with pagination support and optional search
        filtering.
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/tests
          - subpackage_conversationalAi/tests/invocations
      parameters:
        - name: agent_id
          in: query
          description: Filter by agent ID
          required: true
          schema:
            type: string
        - name: page_size
          in: query
          description: >-
            How many Tests to return at maximum. Can not exceed 100, defaults to
            30.
          required: false
          schema:
            type: integer
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
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
                $ref: '#/components/schemas/GetTestInvocationsPageResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    ListResponseMeta:
      type: object
      properties:
        total:
          type:
            - integer
            - 'null'
        page:
          type:
            - integer
            - 'null'
        page_size:
          type:
            - integer
            - 'null'
    ResourceAccessInfoRole:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
        creator_name:
          type: string
        creator_email:
          type: string
        role:
          $ref: '#/components/schemas/ResourceAccessInfoRole'
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
    TestInvocationSummaryResponseModel:
      type: object
      properties:
        id:
          type: string
        created_at_unix_secs:
          type: integer
        test_run_count:
          type: integer
        passed_count:
          type: integer
        failed_count:
          type: integer
        pending_count:
          type: integer
        title:
          type: string
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
      required:
        - id
        - created_at_unix_secs
        - test_run_count
        - passed_count
        - failed_count
        - pending_count
        - title
    GetTestInvocationsPageResponseModel:
      type: object
      properties:
        meta:
          $ref: '#/components/schemas/ListResponseMeta'
        results:
          type: array
          items:
            $ref: '#/components/schemas/TestInvocationSummaryResponseModel'
        next_cursor:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
      required:
        - results
        - has_more

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.tests.invocations.list({
        agentId: "agent_id",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.tests.invocations.list(
    agent_id="agent_id"
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

	url := "https://api.elevenlabs.io/v1/convai/test-invocations?agent_id=agent_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/test-invocations?agent_id=agent_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/test-invocations?agent_id=agent_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/test-invocations?agent_id=agent_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/test-invocations?agent_id=agent_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/test-invocations?agent_id=agent_id")! as URL,
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


# Import phone number

POST https://api.elevenlabs.io/v1/convai/phone-numbers
Content-Type: application/json

Import Phone Number from provider configuration (Twilio or SIP trunk)

Reference: https://elevenlabs.io/docs/api-reference/phone-numbers/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Import Phone Number
  version: endpoint_conversationalAi/phoneNumbers.create
paths:
  /v1/convai/phone-numbers:
    post:
      operationId: create
      summary: Import Phone Number
      description: Import Phone Number from provider configuration (Twilio or SIP trunk)
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/phoneNumbers
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
                $ref: '#/components/schemas/CreatePhoneNumberResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/conversational_ai_phone_numbers_create_Request
components:
  schemas:
    TwilioRegionId:
      type: string
      enum:
        - value: us1
        - value: ie1
        - value: au1
    TwilioEdgeLocation:
      type: string
      enum:
        - value: ashburn
        - value: dublin
        - value: frankfurt
        - value: sao-paulo
        - value: singapore
        - value: sydney
        - value: tokyo
        - value: umatilla
        - value: roaming
    RegionConfigRequest:
      type: object
      properties:
        region_id:
          $ref: '#/components/schemas/TwilioRegionId'
        token:
          type: string
        edge_location:
          $ref: '#/components/schemas/TwilioEdgeLocation'
      required:
        - region_id
        - token
        - edge_location
    CreateTwilioPhoneNumberRequest:
      type: object
      properties:
        phone_number:
          type: string
        label:
          type: string
        supports_inbound:
          type: boolean
        supports_outbound:
          type: boolean
        provider:
          type: string
          enum:
            - type: stringLiteral
              value: twilio
        sid:
          type: string
        token:
          type: string
        region_config:
          oneOf:
            - $ref: '#/components/schemas/RegionConfigRequest'
            - type: 'null'
      required:
        - phone_number
        - label
        - sid
        - token
    SIPMediaEncryptionEnum:
      type: string
      enum:
        - value: disabled
        - value: allowed
        - value: required
    SIPTrunkCredentialsRequestModel:
      type: object
      properties:
        username:
          type: string
        password:
          type:
            - string
            - 'null'
      required:
        - username
    InboundSIPTrunkConfigRequestModel:
      type: object
      properties:
        allowed_addresses:
          type:
            - array
            - 'null'
          items:
            type: string
        allowed_numbers:
          type:
            - array
            - 'null'
          items:
            type: string
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
        credentials:
          oneOf:
            - $ref: '#/components/schemas/SIPTrunkCredentialsRequestModel'
            - type: 'null'
        remote_domains:
          type:
            - array
            - 'null'
          items:
            type: string
    SIPTrunkTransportEnum:
      type: string
      enum:
        - value: auto
        - value: udp
        - value: tcp
        - value: tls
    OutboundSIPTrunkConfigRequestModel:
      type: object
      properties:
        address:
          type: string
        transport:
          $ref: '#/components/schemas/SIPTrunkTransportEnum'
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
        headers:
          type: object
          additionalProperties:
            type: string
        credentials:
          oneOf:
            - $ref: '#/components/schemas/SIPTrunkCredentialsRequestModel'
            - type: 'null'
      required:
        - address
    CreateSIPTrunkPhoneNumberRequestV2:
      type: object
      properties:
        phone_number:
          type: string
        label:
          type: string
        supports_inbound:
          type: boolean
        supports_outbound:
          type: boolean
        provider:
          type: string
          enum:
            - type: stringLiteral
              value: sip_trunk
        inbound_trunk_config:
          oneOf:
            - $ref: '#/components/schemas/InboundSIPTrunkConfigRequestModel'
            - type: 'null'
        outbound_trunk_config:
          oneOf:
            - $ref: '#/components/schemas/OutboundSIPTrunkConfigRequestModel'
            - type: 'null'
      required:
        - phone_number
        - label
    conversational_ai_phone_numbers_create_Request:
      oneOf:
        - $ref: '#/components/schemas/CreateTwilioPhoneNumberRequest'
        - $ref: '#/components/schemas/CreateSIPTrunkPhoneNumberRequestV2'
    CreatePhoneNumberResponseModel:
      type: object
      properties:
        phone_number_id:
          type: string
      required:
        - phone_number_id

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.phoneNumbers.create();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.phone_numbers.create(
    request=
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

	url := "https://api.elevenlabs.io/v1/convai/phone-numbers"

	payload := strings.NewReader("{\n  \"phone_number\": \"string\",\n  \"label\": \"string\",\n  \"sid\": \"string\",\n  \"token\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/phone-numbers")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"phone_number\": \"string\",\n  \"label\": \"string\",\n  \"sid\": \"string\",\n  \"token\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/phone-numbers")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"phone_number\": \"string\",\n  \"label\": \"string\",\n  \"sid\": \"string\",\n  \"token\": \"string\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/phone-numbers', [
  'body' => '{
  "phone_number": "string",
  "label": "string",
  "sid": "string",
  "token": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/phone-numbers");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"phone_number\": \"string\",\n  \"label\": \"string\",\n  \"sid\": \"string\",\n  \"token\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "phone_number": "string",
  "label": "string",
  "sid": "string",
  "token": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/phone-numbers")! as URL,
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


# List phone numbers

GET https://api.elevenlabs.io/v1/convai/phone-numbers

Retrieve all Phone Numbers

Reference: https://elevenlabs.io/docs/api-reference/phone-numbers/list


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List Phone Numbers
  version: endpoint_conversationalAi/phoneNumbers.list
paths:
  /v1/convai/phone-numbers:
    get:
      operationId: list
      summary: List Phone Numbers
      description: Retrieve all Phone Numbers
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/phoneNumbers
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
                  $ref: >-
                    #/components/schemas/V1ConvaiPhoneNumbersGetResponsesContentApplicationJsonSchemaItems
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    PhoneNumberAgentInfo:
      type: object
      properties:
        agent_id:
          type: string
        agent_name:
          type: string
      required:
        - agent_id
        - agent_name
    GetPhoneNumberTwilioResponseModel:
      type: object
      properties:
        phone_number:
          type: string
        label:
          type: string
        supports_inbound:
          type: boolean
        supports_outbound:
          type: boolean
        phone_number_id:
          type: string
        assigned_agent:
          oneOf:
            - $ref: '#/components/schemas/PhoneNumberAgentInfo'
            - type: 'null'
        provider:
          type: string
          enum:
            - type: stringLiteral
              value: twilio
      required:
        - phone_number
        - label
        - phone_number_id
    SIPTrunkTransportEnum:
      type: string
      enum:
        - value: auto
        - value: udp
        - value: tcp
        - value: tls
    SIPMediaEncryptionEnum:
      type: string
      enum:
        - value: disabled
        - value: allowed
        - value: required
    GetPhoneNumberOutboundSIPTrunkConfigResponseModel:
      type: object
      properties:
        address:
          type: string
        transport:
          $ref: '#/components/schemas/SIPTrunkTransportEnum'
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
        headers:
          type: object
          additionalProperties:
            type: string
        has_auth_credentials:
          type: boolean
        username:
          type:
            - string
            - 'null'
        has_outbound_trunk:
          type: boolean
      required:
        - address
        - transport
        - media_encryption
        - has_auth_credentials
    GetPhoneNumberInboundSIPTrunkConfigResponseModel:
      type: object
      properties:
        allowed_addresses:
          type: array
          items:
            type: string
        allowed_numbers:
          type:
            - array
            - 'null'
          items:
            type: string
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
        has_auth_credentials:
          type: boolean
        username:
          type:
            - string
            - 'null'
        remote_domains:
          type:
            - array
            - 'null'
          items:
            type: string
      required:
        - allowed_addresses
        - allowed_numbers
        - media_encryption
        - has_auth_credentials
    LivekitStackType:
      type: string
      enum:
        - value: standard
        - value: static
    GetPhoneNumberSIPTrunkResponseModel:
      type: object
      properties:
        phone_number:
          type: string
        label:
          type: string
        supports_inbound:
          type: boolean
        supports_outbound:
          type: boolean
        phone_number_id:
          type: string
        assigned_agent:
          oneOf:
            - $ref: '#/components/schemas/PhoneNumberAgentInfo'
            - type: 'null'
        provider:
          type: string
          enum:
            - type: stringLiteral
              value: sip_trunk
        provider_config:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPhoneNumberOutboundSIPTrunkConfigResponseModel
            - type: 'null'
        outbound_trunk:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPhoneNumberOutboundSIPTrunkConfigResponseModel
            - type: 'null'
        inbound_trunk:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPhoneNumberInboundSIPTrunkConfigResponseModel
            - type: 'null'
        livekit_stack:
          $ref: '#/components/schemas/LivekitStackType'
      required:
        - phone_number
        - label
        - phone_number_id
        - livekit_stack
    V1ConvaiPhoneNumbersGetResponsesContentApplicationJsonSchemaItems:
      oneOf:
        - $ref: '#/components/schemas/GetPhoneNumberTwilioResponseModel'
        - $ref: '#/components/schemas/GetPhoneNumberSIPTrunkResponseModel'

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.phoneNumbers.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.phone_numbers.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/phone-numbers"

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

url = URI("https://api.elevenlabs.io/v1/convai/phone-numbers")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/phone-numbers")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/phone-numbers', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/phone-numbers");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/phone-numbers")! as URL,
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


# Get phone number

GET https://api.elevenlabs.io/v1/convai/phone-numbers/{phone_number_id}

Retrieve Phone Number details by ID

Reference: https://elevenlabs.io/docs/api-reference/phone-numbers/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Phone Number
  version: endpoint_conversationalAi/phoneNumbers.get
paths:
  /v1/convai/phone-numbers/{phone_number_id}:
    get:
      operationId: get
      summary: Get Phone Number
      description: Retrieve Phone Number details by ID
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/phoneNumbers
      parameters:
        - name: phone_number_id
          in: path
          description: The id of an agent. This is returned on agent creation.
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
                  #/components/schemas/conversational_ai_phone_numbers_get_Response_200
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    PhoneNumberAgentInfo:
      type: object
      properties:
        agent_id:
          type: string
        agent_name:
          type: string
      required:
        - agent_id
        - agent_name
    GetPhoneNumberTwilioResponseModel:
      type: object
      properties:
        phone_number:
          type: string
        label:
          type: string
        supports_inbound:
          type: boolean
        supports_outbound:
          type: boolean
        phone_number_id:
          type: string
        assigned_agent:
          oneOf:
            - $ref: '#/components/schemas/PhoneNumberAgentInfo'
            - type: 'null'
        provider:
          type: string
          enum:
            - type: stringLiteral
              value: twilio
      required:
        - phone_number
        - label
        - phone_number_id
    SIPTrunkTransportEnum:
      type: string
      enum:
        - value: auto
        - value: udp
        - value: tcp
        - value: tls
    SIPMediaEncryptionEnum:
      type: string
      enum:
        - value: disabled
        - value: allowed
        - value: required
    GetPhoneNumberOutboundSIPTrunkConfigResponseModel:
      type: object
      properties:
        address:
          type: string
        transport:
          $ref: '#/components/schemas/SIPTrunkTransportEnum'
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
        headers:
          type: object
          additionalProperties:
            type: string
        has_auth_credentials:
          type: boolean
        username:
          type:
            - string
            - 'null'
        has_outbound_trunk:
          type: boolean
      required:
        - address
        - transport
        - media_encryption
        - has_auth_credentials
    GetPhoneNumberInboundSIPTrunkConfigResponseModel:
      type: object
      properties:
        allowed_addresses:
          type: array
          items:
            type: string
        allowed_numbers:
          type:
            - array
            - 'null'
          items:
            type: string
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
        has_auth_credentials:
          type: boolean
        username:
          type:
            - string
            - 'null'
        remote_domains:
          type:
            - array
            - 'null'
          items:
            type: string
      required:
        - allowed_addresses
        - allowed_numbers
        - media_encryption
        - has_auth_credentials
    LivekitStackType:
      type: string
      enum:
        - value: standard
        - value: static
    GetPhoneNumberSIPTrunkResponseModel:
      type: object
      properties:
        phone_number:
          type: string
        label:
          type: string
        supports_inbound:
          type: boolean
        supports_outbound:
          type: boolean
        phone_number_id:
          type: string
        assigned_agent:
          oneOf:
            - $ref: '#/components/schemas/PhoneNumberAgentInfo'
            - type: 'null'
        provider:
          type: string
          enum:
            - type: stringLiteral
              value: sip_trunk
        provider_config:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPhoneNumberOutboundSIPTrunkConfigResponseModel
            - type: 'null'
        outbound_trunk:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPhoneNumberOutboundSIPTrunkConfigResponseModel
            - type: 'null'
        inbound_trunk:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPhoneNumberInboundSIPTrunkConfigResponseModel
            - type: 'null'
        livekit_stack:
          $ref: '#/components/schemas/LivekitStackType'
      required:
        - phone_number
        - label
        - phone_number_id
        - livekit_stack
    conversational_ai_phone_numbers_get_Response_200:
      oneOf:
        - $ref: '#/components/schemas/GetPhoneNumberTwilioResponseModel'
        - $ref: '#/components/schemas/GetPhoneNumberSIPTrunkResponseModel'

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.phoneNumbers.get("phone_number_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.phone_numbers.get(
    phone_number_id="phone_number_id"
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

	url := "https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id")! as URL,
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


# Update phone number

PATCH https://api.elevenlabs.io/v1/convai/phone-numbers/{phone_number_id}
Content-Type: application/json

Update assigned agent of a phone number

Reference: https://elevenlabs.io/docs/api-reference/phone-numbers/update


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update Phone Number
  version: endpoint_conversationalAi/phoneNumbers.update
paths:
  /v1/convai/phone-numbers/{phone_number_id}:
    patch:
      operationId: update
      summary: Update Phone Number
      description: Update assigned agent of a phone number
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/phoneNumbers
      parameters:
        - name: phone_number_id
          in: path
          description: The id of an agent. This is returned on agent creation.
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
                  #/components/schemas/conversational_ai_phone_numbers_update_Response_200
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdatePhoneNumberRequest'
components:
  schemas:
    SIPMediaEncryptionEnum:
      type: string
      enum:
        - value: disabled
        - value: allowed
        - value: required
    SIPTrunkCredentialsRequestModel:
      type: object
      properties:
        username:
          type: string
        password:
          type:
            - string
            - 'null'
      required:
        - username
    InboundSIPTrunkConfigRequestModel:
      type: object
      properties:
        allowed_addresses:
          type:
            - array
            - 'null'
          items:
            type: string
        allowed_numbers:
          type:
            - array
            - 'null'
          items:
            type: string
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
        credentials:
          oneOf:
            - $ref: '#/components/schemas/SIPTrunkCredentialsRequestModel'
            - type: 'null'
        remote_domains:
          type:
            - array
            - 'null'
          items:
            type: string
    SIPTrunkTransportEnum:
      type: string
      enum:
        - value: auto
        - value: udp
        - value: tcp
        - value: tls
    OutboundSIPTrunkConfigRequestModel:
      type: object
      properties:
        address:
          type: string
        transport:
          $ref: '#/components/schemas/SIPTrunkTransportEnum'
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
        headers:
          type: object
          additionalProperties:
            type: string
        credentials:
          oneOf:
            - $ref: '#/components/schemas/SIPTrunkCredentialsRequestModel'
            - type: 'null'
      required:
        - address
    LivekitStackType:
      type: string
      enum:
        - value: standard
        - value: static
    UpdatePhoneNumberRequest:
      type: object
      properties:
        agent_id:
          type:
            - string
            - 'null'
        inbound_trunk_config:
          oneOf:
            - $ref: '#/components/schemas/InboundSIPTrunkConfigRequestModel'
            - type: 'null'
        outbound_trunk_config:
          oneOf:
            - $ref: '#/components/schemas/OutboundSIPTrunkConfigRequestModel'
            - type: 'null'
        livekit_stack:
          oneOf:
            - $ref: '#/components/schemas/LivekitStackType'
            - type: 'null'
    PhoneNumberAgentInfo:
      type: object
      properties:
        agent_id:
          type: string
        agent_name:
          type: string
      required:
        - agent_id
        - agent_name
    GetPhoneNumberTwilioResponseModel:
      type: object
      properties:
        phone_number:
          type: string
        label:
          type: string
        supports_inbound:
          type: boolean
        supports_outbound:
          type: boolean
        phone_number_id:
          type: string
        assigned_agent:
          oneOf:
            - $ref: '#/components/schemas/PhoneNumberAgentInfo'
            - type: 'null'
        provider:
          type: string
          enum:
            - type: stringLiteral
              value: twilio
      required:
        - phone_number
        - label
        - phone_number_id
    GetPhoneNumberOutboundSIPTrunkConfigResponseModel:
      type: object
      properties:
        address:
          type: string
        transport:
          $ref: '#/components/schemas/SIPTrunkTransportEnum'
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
        headers:
          type: object
          additionalProperties:
            type: string
        has_auth_credentials:
          type: boolean
        username:
          type:
            - string
            - 'null'
        has_outbound_trunk:
          type: boolean
      required:
        - address
        - transport
        - media_encryption
        - has_auth_credentials
    GetPhoneNumberInboundSIPTrunkConfigResponseModel:
      type: object
      properties:
        allowed_addresses:
          type: array
          items:
            type: string
        allowed_numbers:
          type:
            - array
            - 'null'
          items:
            type: string
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
        has_auth_credentials:
          type: boolean
        username:
          type:
            - string
            - 'null'
        remote_domains:
          type:
            - array
            - 'null'
          items:
            type: string
      required:
        - allowed_addresses
        - allowed_numbers
        - media_encryption
        - has_auth_credentials
    GetPhoneNumberSIPTrunkResponseModel:
      type: object
      properties:
        phone_number:
          type: string
        label:
          type: string
        supports_inbound:
          type: boolean
        supports_outbound:
          type: boolean
        phone_number_id:
          type: string
        assigned_agent:
          oneOf:
            - $ref: '#/components/schemas/PhoneNumberAgentInfo'
            - type: 'null'
        provider:
          type: string
          enum:
            - type: stringLiteral
              value: sip_trunk
        provider_config:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPhoneNumberOutboundSIPTrunkConfigResponseModel
            - type: 'null'
        outbound_trunk:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPhoneNumberOutboundSIPTrunkConfigResponseModel
            - type: 'null'
        inbound_trunk:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPhoneNumberInboundSIPTrunkConfigResponseModel
            - type: 'null'
        livekit_stack:
          $ref: '#/components/schemas/LivekitStackType'
      required:
        - phone_number
        - label
        - phone_number_id
        - livekit_stack
    conversational_ai_phone_numbers_update_Response_200:
      oneOf:
        - $ref: '#/components/schemas/GetPhoneNumberTwilioResponseModel'
        - $ref: '#/components/schemas/GetPhoneNumberSIPTrunkResponseModel'

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.phoneNumbers.update("phone_number_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.phone_numbers.update(
    phone_number_id="phone_number_id"
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

	url := "https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id")

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
HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id")! as URL,
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


# Delete phone number

DELETE https://api.elevenlabs.io/v1/convai/phone-numbers/{phone_number_id}

Delete Phone Number by ID

Reference: https://elevenlabs.io/docs/api-reference/phone-numbers/delete


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete Phone Number
  version: endpoint_conversationalAi/phoneNumbers.delete
paths:
  /v1/convai/phone-numbers/{phone_number_id}:
    delete:
      operationId: delete
      summary: Delete Phone Number
      description: Delete Phone Number by ID
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/phoneNumbers
      parameters:
        - name: phone_number_id
          in: path
          description: The id of an agent. This is returned on agent creation.
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
    await client.conversationalAi.phoneNumbers.delete("phone_number_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.phone_numbers.delete(
    phone_number_id="phone_number_id"
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

	url := "https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id")! as URL,
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


# Get widget

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/widget

Retrieve the widget configuration for an agent

Reference: https://elevenlabs.io/docs/api-reference/widget/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Agent Widget Config
  version: endpoint_conversationalAi/agents/widget.get
paths:
  /v1/convai/agents/{agent_id}/widget:
    get:
      operationId: get
      summary: Get Agent Widget Config
      description: Retrieve the widget configuration for an agent
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/agents
          - subpackage_conversationalAi/agents/widget
      parameters:
        - name: agent_id
          in: path
          description: The id of an agent. This is returned on agent creation.
          required: true
          schema:
            type: string
        - name: conversation_signature
          in: query
          description: >-
            An expiring token that enables a websocket conversation to start.
            These can be generated for an agent using the
            /v1/convai/conversation/get-signed-url endpoint
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
                $ref: '#/components/schemas/GetAgentEmbedResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    EmbedVariant:
      type: string
      enum:
        - value: tiny
        - value: compact
        - value: full
        - value: expandable
    WidgetPlacement:
      type: string
      enum:
        - value: top-left
        - value: top
        - value: top-right
        - value: bottom-left
        - value: bottom
        - value: bottom-right
    WidgetExpandable:
      type: string
      enum:
        - value: never
        - value: mobile
        - value: desktop
        - value: always
    OrbAvatar:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: orb
        color_1:
          type: string
        color_2:
          type: string
    URLAvatar:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: url
        custom_url:
          type: string
    ImageAvatar:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: image
        url:
          type: string
    WidgetConfigResponseModelAvatar:
      oneOf:
        - $ref: '#/components/schemas/OrbAvatar'
        - $ref: '#/components/schemas/URLAvatar'
        - $ref: '#/components/schemas/ImageAvatar'
    WidgetFeedbackMode:
      type: string
      enum:
        - value: none
        - value: during
        - value: end
    WidgetEndFeedbackType:
      type: string
      enum:
        - value: rating
    WidgetEndFeedbackConfig:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/WidgetEndFeedbackType'
    WidgetTextContents:
      type: object
      properties:
        main_label:
          type:
            - string
            - 'null'
        start_call:
          type:
            - string
            - 'null'
        start_chat:
          type:
            - string
            - 'null'
        new_call:
          type:
            - string
            - 'null'
        end_call:
          type:
            - string
            - 'null'
        mute_microphone:
          type:
            - string
            - 'null'
        change_language:
          type:
            - string
            - 'null'
        collapse:
          type:
            - string
            - 'null'
        expand:
          type:
            - string
            - 'null'
        copied:
          type:
            - string
            - 'null'
        accept_terms:
          type:
            - string
            - 'null'
        dismiss_terms:
          type:
            - string
            - 'null'
        listening_status:
          type:
            - string
            - 'null'
        speaking_status:
          type:
            - string
            - 'null'
        connecting_status:
          type:
            - string
            - 'null'
        chatting_status:
          type:
            - string
            - 'null'
        input_label:
          type:
            - string
            - 'null'
        input_placeholder:
          type:
            - string
            - 'null'
        input_placeholder_text_only:
          type:
            - string
            - 'null'
        input_placeholder_new_conversation:
          type:
            - string
            - 'null'
        user_ended_conversation:
          type:
            - string
            - 'null'
        agent_ended_conversation:
          type:
            - string
            - 'null'
        conversation_id:
          type:
            - string
            - 'null'
        error_occurred:
          type:
            - string
            - 'null'
        copy_id:
          type:
            - string
            - 'null'
    WidgetStyles:
      type: object
      properties:
        base:
          type:
            - string
            - 'null'
        base_hover:
          type:
            - string
            - 'null'
        base_active:
          type:
            - string
            - 'null'
        base_border:
          type:
            - string
            - 'null'
        base_subtle:
          type:
            - string
            - 'null'
        base_primary:
          type:
            - string
            - 'null'
        base_error:
          type:
            - string
            - 'null'
        accent:
          type:
            - string
            - 'null'
        accent_hover:
          type:
            - string
            - 'null'
        accent_active:
          type:
            - string
            - 'null'
        accent_border:
          type:
            - string
            - 'null'
        accent_subtle:
          type:
            - string
            - 'null'
        accent_primary:
          type:
            - string
            - 'null'
        overlay_padding:
          type:
            - number
            - 'null'
          format: double
        button_radius:
          type:
            - number
            - 'null'
          format: double
        input_radius:
          type:
            - number
            - 'null'
          format: double
        bubble_radius:
          type:
            - number
            - 'null'
          format: double
        sheet_radius:
          type:
            - number
            - 'null'
          format: double
        compact_sheet_radius:
          type:
            - number
            - 'null'
          format: double
        dropdown_sheet_radius:
          type:
            - number
            - 'null'
          format: double
    WidgetLanguagePresetResponse:
      type: object
      properties:
        first_message:
          type:
            - string
            - 'null'
        text_contents:
          oneOf:
            - $ref: '#/components/schemas/WidgetTextContents'
            - type: 'null'
    WidgetConfigResponseModel:
      type: object
      properties:
        variant:
          $ref: '#/components/schemas/EmbedVariant'
        placement:
          $ref: '#/components/schemas/WidgetPlacement'
        expandable:
          $ref: '#/components/schemas/WidgetExpandable'
        avatar:
          $ref: '#/components/schemas/WidgetConfigResponseModelAvatar'
        feedback_mode:
          $ref: '#/components/schemas/WidgetFeedbackMode'
        end_feedback:
          oneOf:
            - $ref: '#/components/schemas/WidgetEndFeedbackConfig'
            - type: 'null'
        bg_color:
          type: string
        text_color:
          type: string
        btn_color:
          type: string
        btn_text_color:
          type: string
        border_color:
          type: string
        focus_color:
          type: string
        border_radius:
          type:
            - integer
            - 'null'
        btn_radius:
          type:
            - integer
            - 'null'
        action_text:
          type:
            - string
            - 'null'
        start_call_text:
          type:
            - string
            - 'null'
        end_call_text:
          type:
            - string
            - 'null'
        expand_text:
          type:
            - string
            - 'null'
        listening_text:
          type:
            - string
            - 'null'
        speaking_text:
          type:
            - string
            - 'null'
        shareable_page_text:
          type:
            - string
            - 'null'
        shareable_page_show_terms:
          type: boolean
        terms_text:
          type:
            - string
            - 'null'
        terms_html:
          type:
            - string
            - 'null'
        terms_key:
          type:
            - string
            - 'null'
        show_avatar_when_collapsed:
          type:
            - boolean
            - 'null'
        disable_banner:
          type: boolean
        override_link:
          type:
            - string
            - 'null'
        mic_muting_enabled:
          type: boolean
        transcript_enabled:
          type: boolean
        text_input_enabled:
          type: boolean
        default_expanded:
          type: boolean
        always_expanded:
          type: boolean
        text_contents:
          $ref: '#/components/schemas/WidgetTextContents'
        styles:
          $ref: '#/components/schemas/WidgetStyles'
        language:
          type: string
        supported_language_overrides:
          type:
            - array
            - 'null'
          items:
            type: string
        language_presets:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/WidgetLanguagePresetResponse'
        text_only:
          type: boolean
        supports_text_only:
          type: boolean
        first_message:
          type:
            - string
            - 'null'
        use_rtc:
          type:
            - boolean
            - 'null'
      required:
        - language
    GetAgentEmbedResponseModel:
      type: object
      properties:
        agent_id:
          type: string
        widget_config:
          $ref: '#/components/schemas/WidgetConfigResponseModel'
      required:
        - agent_id
        - widget_config

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.agents.widget.get("agent_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.agents.widget.get(
    agent_id="agent_id"
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/widget"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/widget")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_id/widget")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/widget', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/widget");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/widget")! as URL,
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


# Create widget avatar

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/avatar
Content-Type: multipart/form-data

Sets the avatar for an agent displayed in the widget

Reference: https://elevenlabs.io/docs/api-reference/widget/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Post Agent Avatar
  version: endpoint_conversationalAi/agents/widget/avatar.create
paths:
  /v1/convai/agents/{agent_id}/avatar:
    post:
      operationId: create
      summary: Post Agent Avatar
      description: Sets the avatar for an agent displayed in the widget
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/agents
          - subpackage_conversationalAi/agents/widget
          - subpackage_conversationalAi/agents/widget/avatar
      parameters:
        - name: agent_id
          in: path
          description: The id of an agent. This is returned on agent creation.
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
                $ref: '#/components/schemas/PostAgentAvatarResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties: {}
components:
  schemas:
    PostAgentAvatarResponseModel:
      type: object
      properties:
        agent_id:
          type: string
        avatar_url:
          type:
            - string
            - 'null'
      required:
        - agent_id

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.agents.widget.avatar.create("agent_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.agents.widget.avatar.create(
    agent_id="agent_id"
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/avatar"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"avatar_file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/avatar")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"avatar_file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_id/avatar")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"avatar_file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/avatar', [
  'multipart' => [
    [
        'name' => 'avatar_file',
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
var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/avatar");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"avatar_file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
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
    "name": "avatar_file",
    "fileName": "string"
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/avatar")! as URL,
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


# Get settings

GET https://api.elevenlabs.io/v1/convai/settings

Retrieve Convai settings for the workspace

Reference: https://elevenlabs.io/docs/api-reference/workspace/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Convai Settings
  version: endpoint_conversationalAi/settings.get
paths:
  /v1/convai/settings:
    get:
      operationId: get
      summary: Get Convai Settings
      description: Retrieve Convai settings for the workspace
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/settings
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
                $ref: '#/components/schemas/GetConvAISettingsResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
    ConversationInitiationClientDataWebhookRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
    ConversationInitiationClientDataWebhook:
      type: object
      properties:
        url:
          type: string
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/ConversationInitiationClientDataWebhookRequestHeaders
      required:
        - url
        - request_headers
    WebhookEventType:
      type: string
      enum:
        - value: transcript
        - value: audio
        - value: call_initiation_failure
    ConvAIWebhooks:
      type: object
      properties:
        post_call_webhook_id:
          type:
            - string
            - 'null'
        events:
          type: array
          items:
            $ref: '#/components/schemas/WebhookEventType'
        send_audio:
          type:
            - boolean
            - 'null'
    LivekitStackType:
      type: string
      enum:
        - value: standard
        - value: static
    GetConvAISettingsResponseModel:
      type: object
      properties:
        conversation_initiation_client_data_webhook:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationClientDataWebhook'
            - type: 'null'
        webhooks:
          $ref: '#/components/schemas/ConvAIWebhooks'
        can_use_mcp_servers:
          type: boolean
        rag_retention_period_days:
          type: integer
        default_livekit_stack:
          $ref: '#/components/schemas/LivekitStackType'

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.settings.get();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.settings.get()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/settings"

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

url = URI("https://api.elevenlabs.io/v1/convai/settings")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/settings")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/settings', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/settings");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/settings")! as URL,
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


# Update settings

PATCH https://api.elevenlabs.io/v1/convai/settings
Content-Type: application/json

Update Convai settings for the workspace

Reference: https://elevenlabs.io/docs/api-reference/workspace/update


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update Convai Settings
  version: endpoint_conversationalAi/settings.update
paths:
  /v1/convai/settings:
    patch:
      operationId: update
      summary: Update Convai Settings
      description: Update Convai settings for the workspace
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/settings
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
                $ref: '#/components/schemas/GetConvAISettingsResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchConvAISettingsRequest'
components:
  schemas:
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
    ConversationInitiationClientDataWebhookRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
    ConversationInitiationClientDataWebhook:
      type: object
      properties:
        url:
          type: string
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/ConversationInitiationClientDataWebhookRequestHeaders
      required:
        - url
        - request_headers
    WebhookEventType:
      type: string
      enum:
        - value: transcript
        - value: audio
        - value: call_initiation_failure
    ConvAIWebhooks:
      type: object
      properties:
        post_call_webhook_id:
          type:
            - string
            - 'null'
        events:
          type: array
          items:
            $ref: '#/components/schemas/WebhookEventType'
        send_audio:
          type:
            - boolean
            - 'null'
    LivekitStackType:
      type: string
      enum:
        - value: standard
        - value: static
    PatchConvAISettingsRequest:
      type: object
      properties:
        conversation_initiation_client_data_webhook:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationClientDataWebhook'
            - type: 'null'
        webhooks:
          $ref: '#/components/schemas/ConvAIWebhooks'
        can_use_mcp_servers:
          type: boolean
        rag_retention_period_days:
          type: integer
        default_livekit_stack:
          $ref: '#/components/schemas/LivekitStackType'
    GetConvAISettingsResponseModel:
      type: object
      properties:
        conversation_initiation_client_data_webhook:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationClientDataWebhook'
            - type: 'null'
        webhooks:
          $ref: '#/components/schemas/ConvAIWebhooks'
        can_use_mcp_servers:
          type: boolean
        rag_retention_period_days:
          type: integer
        default_livekit_stack:
          $ref: '#/components/schemas/LivekitStackType'

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.settings.update({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.settings.update()

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

	url := "https://api.elevenlabs.io/v1/convai/settings"

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

url = URI("https://api.elevenlabs.io/v1/convai/settings")

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
HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/settings")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/settings', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/settings");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/settings")! as URL,
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


# Get secrets

GET https://api.elevenlabs.io/v1/convai/secrets

Get all workspace secrets for the user

Reference: https://elevenlabs.io/docs/api-reference/workspace/secrets/list


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Convai Workspace Secrets
  version: endpoint_conversationalAi/secrets.list
paths:
  /v1/convai/secrets:
    get:
      operationId: list
      summary: Get Convai Workspace Secrets
      description: Get all workspace secrets for the user
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/secrets
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
                $ref: '#/components/schemas/GetWorkspaceSecretsResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    DependentAvailableToolIdentifierAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    DependentAvailableToolIdentifier:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: available
        created_at_unix_secs:
          type: integer
        access_level:
          $ref: '#/components/schemas/DependentAvailableToolIdentifierAccessLevel'
      required:
        - id
        - name
        - created_at_unix_secs
        - access_level
    DependentUnknownToolIdentifier:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: unknown
    ConvAiStoredSecretDependenciesToolsItems:
      oneOf:
        - $ref: '#/components/schemas/DependentAvailableToolIdentifier'
        - $ref: '#/components/schemas/DependentUnknownToolIdentifier'
    DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    DependentAvailableAgentIdentifier:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: available
        created_at_unix_secs:
          type: integer
        access_level:
          $ref: '#/components/schemas/DependentAvailableAgentIdentifierAccessLevel'
      required:
        - id
        - name
        - created_at_unix_secs
        - access_level
    DependentUnknownAgentIdentifier:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: unknown
    ConvAiStoredSecretDependenciesAgentsItems:
      oneOf:
        - $ref: '#/components/schemas/DependentAvailableAgentIdentifier'
        - $ref: '#/components/schemas/DependentUnknownAgentIdentifier'
    SecretDependencyType:
      type: string
      enum:
        - value: conversation_initiation_webhook
    TelephonyProvider:
      type: string
      enum:
        - value: twilio
        - value: sip_trunk
    DependentPhoneNumberIdentifier:
      type: object
      properties:
        phone_number_id:
          type: string
        phone_number:
          type: string
        label:
          type: string
        provider:
          $ref: '#/components/schemas/TelephonyProvider'
      required:
        - phone_number_id
        - phone_number
        - label
        - provider
    ConvAIStoredSecretDependencies:
      type: object
      properties:
        tools:
          type: array
          items:
            $ref: '#/components/schemas/ConvAiStoredSecretDependenciesToolsItems'
        agents:
          type: array
          items:
            $ref: '#/components/schemas/ConvAiStoredSecretDependenciesAgentsItems'
        others:
          type: array
          items:
            $ref: '#/components/schemas/SecretDependencyType'
        phone_numbers:
          type: array
          items:
            $ref: '#/components/schemas/DependentPhoneNumberIdentifier'
      required:
        - tools
        - agents
        - others
    ConvAIWorkspaceStoredSecretConfig:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: stored
        secret_id:
          type: string
        name:
          type: string
        used_by:
          $ref: '#/components/schemas/ConvAIStoredSecretDependencies'
      required:
        - type
        - secret_id
        - name
        - used_by
    GetWorkspaceSecretsResponseModel:
      type: object
      properties:
        secrets:
          type: array
          items:
            $ref: '#/components/schemas/ConvAIWorkspaceStoredSecretConfig'
      required:
        - secrets

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.secrets.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.secrets.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/secrets"

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/secrets")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets")! as URL,
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


# Create secret

POST https://api.elevenlabs.io/v1/convai/secrets
Content-Type: application/json

Create a new secret for the workspace

Reference: https://elevenlabs.io/docs/api-reference/workspace/secrets/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create Convai Workspace Secret
  version: endpoint_conversationalAi/secrets.create
paths:
  /v1/convai/secrets:
    post:
      operationId: create
      summary: Create Convai Workspace Secret
      description: Create a new secret for the workspace
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/secrets
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
                $ref: '#/components/schemas/PostWorkspaceSecretResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PostWorkspaceSecretRequest'
components:
  schemas:
    PostWorkspaceSecretRequest:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: new
        name:
          type: string
        value:
          type: string
      required:
        - type
        - name
        - value
    PostWorkspaceSecretResponseModel:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: stored
        secret_id:
          type: string
        name:
          type: string
      required:
        - type
        - secret_id
        - name

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.secrets.create({
        type: "string",
        name: "string",
        value: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.secrets.create(
    type="string",
    name="string",
    value="string"
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

	url := "https://api.elevenlabs.io/v1/convai/secrets"

	payload := strings.NewReader("{\n  \"type\": \"string\",\n  \"name\": \"string\",\n  \"value\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"string\",\n  \"name\": \"string\",\n  \"value\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/secrets")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"string\",\n  \"name\": \"string\",\n  \"value\": \"string\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/secrets', [
  'body' => '{
  "type": "string",
  "name": "string",
  "value": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"type\": \"string\",\n  \"name\": \"string\",\n  \"value\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "type": "string",
  "name": "string",
  "value": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets")! as URL,
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


# Update secret

PATCH https://api.elevenlabs.io/v1/convai/secrets/{secret_id}
Content-Type: application/json

Update an existing secret for the workspace

Reference: https://elevenlabs.io/docs/api-reference/workspace/secrets/update


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update Convai Workspace Secret
  version: endpoint_conversationalAi/secrets.update
paths:
  /v1/convai/secrets/{secret_id}:
    patch:
      operationId: update
      summary: Update Convai Workspace Secret
      description: Update an existing secret for the workspace
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/secrets
      parameters:
        - name: secret_id
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
                $ref: '#/components/schemas/PostWorkspaceSecretResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchWorkspaceSecretRequest'
components:
  schemas:
    PatchWorkspaceSecretRequest:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: update
        name:
          type: string
        value:
          type: string
      required:
        - type
        - name
        - value
    PostWorkspaceSecretResponseModel:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: stored
        secret_id:
          type: string
        name:
          type: string
      required:
        - type
        - secret_id
        - name

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.secrets.update("secret_id", {
        type: "string",
        name: "string",
        value: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.secrets.update(
    secret_id="secret_id",
    type="string",
    name="string",
    value="string"
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

	url := "https://api.elevenlabs.io/v1/convai/secrets/secret_id"

	payload := strings.NewReader("{\n  \"type\": \"string\",\n  \"name\": \"string\",\n  \"value\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets/secret_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"string\",\n  \"name\": \"string\",\n  \"value\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/secrets/secret_id")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"string\",\n  \"name\": \"string\",\n  \"value\": \"string\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/secrets/secret_id', [
  'body' => '{
  "type": "string",
  "name": "string",
  "value": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets/secret_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"type\": \"string\",\n  \"name\": \"string\",\n  \"value\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "type": "string",
  "name": "string",
  "value": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets/secret_id")! as URL,
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


---
**Navigation:** [← Previous](./51-get-test-invocation.md) | [Index](./index.md) | [Next →](./53-delete-secret.md)
