**Navigation:** [← Previous](./45-delete-agent.md) | [Index](./index.md) | [Next →](./47-get-tool.md)

# Calculate expected LLM usage

POST https://api.elevenlabs.io/v1/convai/agent/{agent_id}/llm-usage/calculate
Content-Type: application/json

Calculates expected number of LLM tokens needed for the specified agent.

Reference: https://elevenlabs.io/docs/api-reference/agents/calculate


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Calculate Expected Llm Usage For An Agent
  version: endpoint_conversationalAi/agents/llmUsage.calculate
paths:
  /v1/convai/agent/{agent_id}/llm-usage/calculate:
    post:
      operationId: calculate
      summary: Calculate Expected Llm Usage For An Agent
      description: Calculates expected number of LLM tokens needed for the specified agent.
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/agents
          - subpackage_conversationalAi/agents/llmUsage
      parameters:
        - name: agent_id
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
                $ref: '#/components/schemas/LLMUsageCalculatorResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LLMUsageCalculatorRequestModel'
components:
  schemas:
    LLMUsageCalculatorRequestModel:
      type: object
      properties:
        prompt_length:
          type:
            - integer
            - 'null'
        number_of_pages:
          type:
            - integer
            - 'null'
        rag_enabled:
          type:
            - boolean
            - 'null'
    LLM:
      type: string
      enum:
        - value: gpt-4o-mini
        - value: gpt-4o
        - value: gpt-4
        - value: gpt-4-turbo
        - value: gpt-4.1
        - value: gpt-4.1-mini
        - value: gpt-4.1-nano
        - value: gpt-5
        - value: gpt-5-mini
        - value: gpt-5-nano
        - value: gpt-3.5-turbo
        - value: gemini-1.5-pro
        - value: gemini-1.5-flash
        - value: gemini-2.0-flash
        - value: gemini-2.0-flash-lite
        - value: gemini-2.5-flash-lite
        - value: gemini-2.5-flash
        - value: claude-sonnet-4-5
        - value: claude-sonnet-4
        - value: claude-haiku-4-5
        - value: claude-3-7-sonnet
        - value: claude-3-5-sonnet
        - value: claude-3-5-sonnet-v1
        - value: claude-3-haiku
        - value: grok-beta
        - value: custom-llm
        - value: qwen3-4b
        - value: qwen3-30b-a3b
        - value: gpt-oss-20b
        - value: gpt-oss-120b
        - value: glm-45-air-fp8
        - value: gemini-2.5-flash-preview-09-2025
        - value: gemini-2.5-flash-lite-preview-09-2025
        - value: gemini-2.5-flash-preview-05-20
        - value: gemini-2.5-flash-preview-04-17
        - value: gemini-2.5-flash-lite-preview-06-17
        - value: gemini-2.0-flash-lite-001
        - value: gemini-2.0-flash-001
        - value: gemini-1.5-flash-002
        - value: gemini-1.5-flash-001
        - value: gemini-1.5-pro-002
        - value: gemini-1.5-pro-001
        - value: claude-sonnet-4@20250514
        - value: claude-sonnet-4-5@20250929
        - value: claude-haiku-4-5@20251001
        - value: claude-3-7-sonnet@20250219
        - value: claude-3-5-sonnet@20240620
        - value: claude-3-5-sonnet-v2@20241022
        - value: claude-3-haiku@20240307
        - value: gpt-5-2025-08-07
        - value: gpt-5-mini-2025-08-07
        - value: gpt-5-nano-2025-08-07
        - value: gpt-4.1-2025-04-14
        - value: gpt-4.1-mini-2025-04-14
        - value: gpt-4.1-nano-2025-04-14
        - value: gpt-4o-mini-2024-07-18
        - value: gpt-4o-2024-11-20
        - value: gpt-4o-2024-08-06
        - value: gpt-4o-2024-05-13
        - value: gpt-4-0613
        - value: gpt-4-0314
        - value: gpt-4-turbo-2024-04-09
        - value: gpt-3.5-turbo-0125
        - value: gpt-3.5-turbo-1106
        - value: watt-tool-8b
        - value: watt-tool-70b
    LLMUsageCalculatorLLMResponseModel:
      type: object
      properties:
        llm:
          $ref: '#/components/schemas/LLM'
        price_per_minute:
          type: number
          format: double
      required:
        - llm
        - price_per_minute
    LLMUsageCalculatorResponseModel:
      type: object
      properties:
        llm_prices:
          type: array
          items:
            $ref: '#/components/schemas/LLMUsageCalculatorLLMResponseModel'
      required:
        - llm_prices

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.agents.llmUsage.calculate("agent_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.agents.llm_usage.calculate(
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

	url := "https://api.elevenlabs.io/v1/convai/agent/agent_id/llm-usage/calculate"

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

url = URI("https://api.elevenlabs.io/v1/convai/agent/agent_id/llm-usage/calculate")

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
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agent/agent_id/llm-usage/calculate")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agent/agent_id/llm-usage/calculate', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent/agent_id/llm-usage/calculate");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent/agent_id/llm-usage/calculate")! as URL,
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


# List conversations

GET https://api.elevenlabs.io/v1/convai/conversations

Get all conversations of agents that user owns. With option to restrict to a specific agent.

Reference: https://elevenlabs.io/docs/api-reference/conversations/list


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List conversations
  version: endpoint_conversationalAi/conversations.list
paths:
  /v1/convai/conversations:
    get:
      operationId: list
      summary: List conversations
      description: >-
        Get all conversations of agents that user owns. With option to restrict
        to a specific agent.
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/conversations
      parameters:
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: agent_id
          in: query
          description: The id of the agent you're taking the action on.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: call_successful
          in: query
          description: The result of the success evaluation
          required: false
          schema:
            oneOf:
              - $ref: '#/components/schemas/EvaluationSuccessResult'
              - type: 'null'
        - name: call_start_before_unix
          in: query
          description: >-
            Unix timestamp (in seconds) to filter conversations up to this start
            date.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: call_start_after_unix
          in: query
          description: >-
            Unix timestamp (in seconds) to filter conversations after to this
            start date.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: user_id
          in: query
          description: Filter conversations by the user ID who initiated them.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: page_size
          in: query
          description: >-
            How many conversations to return at maximum. Can not exceed 100,
            defaults to 30.
          required: false
          schema:
            type: integer
        - name: summary_mode
          in: query
          description: Whether to include transcript summaries in the response.
          required: false
          schema:
            $ref: '#/components/schemas/V1ConvaiConversationsGetParametersSummaryMode'
        - name: search
          in: query
          description: Full-text or fuzzy search over transcript messages
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
                $ref: '#/components/schemas/GetConversationsPageResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    EvaluationSuccessResult:
      type: string
      enum:
        - value: success
        - value: failure
        - value: unknown
    V1ConvaiConversationsGetParametersSummaryMode:
      type: string
      enum:
        - value: exclude
        - value: include
    ConversationSummaryResponseModelStatus:
      type: string
      enum:
        - value: initiated
        - value: in-progress
        - value: processing
        - value: done
        - value: failed
    ConversationSummaryResponseModelDirection:
      type: string
      enum:
        - value: inbound
        - value: outbound
    ConversationSummaryResponseModel:
      type: object
      properties:
        agent_id:
          type: string
        branch_id:
          type:
            - string
            - 'null'
        agent_name:
          type:
            - string
            - 'null'
        conversation_id:
          type: string
        start_time_unix_secs:
          type: integer
        call_duration_secs:
          type: integer
        message_count:
          type: integer
        status:
          $ref: '#/components/schemas/ConversationSummaryResponseModelStatus'
        call_successful:
          $ref: '#/components/schemas/EvaluationSuccessResult'
        transcript_summary:
          type:
            - string
            - 'null'
        call_summary_title:
          type:
            - string
            - 'null'
        direction:
          oneOf:
            - $ref: '#/components/schemas/ConversationSummaryResponseModelDirection'
            - type: 'null'
      required:
        - agent_id
        - conversation_id
        - start_time_unix_secs
        - call_duration_secs
        - message_count
        - status
        - call_successful
    GetConversationsPageResponseModel:
      type: object
      properties:
        conversations:
          type: array
          items:
            $ref: '#/components/schemas/ConversationSummaryResponseModel'
        next_cursor:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
      required:
        - conversations
        - has_more

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.conversations.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.conversations.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/conversations"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations")! as URL,
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


# Get conversation details

GET https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}

Get the details of a particular conversation

Reference: https://elevenlabs.io/docs/api-reference/conversations/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Conversation Details
  version: endpoint_conversationalAi/conversations.get
paths:
  /v1/convai/conversations/{conversation_id}:
    get:
      operationId: get
      summary: Get Conversation Details
      description: Get the details of a particular conversation
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/conversations
      parameters:
        - name: conversation_id
          in: path
          description: The id of the conversation you're taking the action on.
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
                $ref: '#/components/schemas/GetConversationResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    GetConversationResponseModelStatus:
      type: string
      enum:
        - value: initiated
        - value: in-progress
        - value: processing
        - value: done
        - value: failed
    ConversationHistoryTranscriptCommonModelOutputRole:
      type: string
      enum:
        - value: user
        - value: agent
    AgentMetadata:
      type: object
      properties:
        agent_id:
          type: string
        branch_id:
          type:
            - string
            - 'null'
        workflow_node_id:
          type:
            - string
            - 'null'
      required:
        - agent_id
    ConversationHistoryMultivoiceMessagePartModel:
      type: object
      properties:
        text:
          type: string
        voice_label:
          type:
            - string
            - 'null'
        time_in_call_secs:
          type:
            - integer
            - 'null'
      required:
        - text
        - voice_label
        - time_in_call_secs
    ConversationHistoryMultivoiceMessageModel:
      type: object
      properties:
        parts:
          type: array
          items:
            $ref: '#/components/schemas/ConversationHistoryMultivoiceMessagePartModel'
      required:
        - parts
    ToolType:
      type: string
      enum:
        - value: system
        - value: webhook
        - value: client
        - value: mcp
        - value: workflow
        - value: api_integration_webhook
        - value: api_integration_mcp
    ConversationHistoryTranscriptToolCallWebhookDetails:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: webhook
        method:
          type: string
        url:
          type: string
        headers:
          type: object
          additionalProperties:
            type: string
        path_params:
          type: object
          additionalProperties:
            type: string
        query_params:
          type: object
          additionalProperties:
            type: string
        body:
          type:
            - string
            - 'null'
      required:
        - method
        - url
    ConversationHistoryTranscriptToolCallClientDetails:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: client
        parameters:
          type: string
      required:
        - parameters
    ConversationHistoryTranscriptToolCallMCPDetails:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: mcp
        mcp_server_id:
          type: string
        mcp_server_name:
          type: string
        integration_type:
          type: string
        parameters:
          type: object
          additionalProperties:
            type: string
        approval_policy:
          type: string
        requires_approval:
          type: boolean
        mcp_tool_name:
          type: string
        mcp_tool_description:
          type: string
      required:
        - mcp_server_id
        - mcp_server_name
        - integration_type
        - approval_policy
    ConversationHistoryTranscriptToolCallCommonModelToolDetails:
      oneOf:
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptToolCallWebhookDetails
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptToolCallClientDetails
        - $ref: '#/components/schemas/ConversationHistoryTranscriptToolCallMCPDetails'
    ConversationHistoryTranscriptToolCallCommonModel:
      type: object
      properties:
        type:
          oneOf:
            - $ref: '#/components/schemas/ToolType'
            - type: 'null'
        request_id:
          type: string
        tool_name:
          type: string
        params_as_json:
          type: string
        tool_has_been_called:
          type: boolean
        tool_details:
          oneOf:
            - $ref: >-
                #/components/schemas/ConversationHistoryTranscriptToolCallCommonModelToolDetails
            - type: 'null'
      required:
        - request_id
        - tool_name
        - params_as_json
        - tool_has_been_called
    DynamicVariableUpdateCommonModel:
      type: object
      properties:
        variable_name:
          type: string
        old_value:
          type:
            - string
            - 'null'
        new_value:
          type: string
        updated_at:
          type: number
          format: double
        tool_name:
          type: string
        tool_request_id:
          type: string
      required:
        - variable_name
        - old_value
        - new_value
        - updated_at
        - tool_name
        - tool_request_id
    ConversationHistoryTranscriptOtherToolsResultCommonModelType:
      type: string
      enum:
        - value: client
        - value: webhook
        - value: mcp
        - value: api_integration_webhook
    ConversationHistoryTranscriptOtherToolsResultCommonModel:
      type: object
      properties:
        request_id:
          type: string
        tool_name:
          type: string
        result_value:
          type: string
        is_error:
          type: boolean
        tool_has_been_called:
          type: boolean
        tool_latency_secs:
          type: number
          format: double
        dynamic_variable_updates:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableUpdateCommonModel'
        type:
          oneOf:
            - $ref: >-
                #/components/schemas/ConversationHistoryTranscriptOtherToolsResultCommonModelType
            - type: 'null'
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
    EndCallToolResultModel:
      type: object
      properties:
        result_type:
          type: string
          enum:
            - type: stringLiteral
              value: end_call_success
        status:
          type: string
          enum:
            - type: stringLiteral
              value: success
        reason:
          type:
            - string
            - 'null'
        message:
          type:
            - string
            - 'null'
    LanguageDetectionToolResultModel:
      type: object
      properties:
        result_type:
          type: string
          enum:
            - type: stringLiteral
              value: language_detection_success
        status:
          type: string
          enum:
            - type: stringLiteral
              value: success
        reason:
          type:
            - string
            - 'null'
        language:
          type:
            - string
            - 'null'
    TransferToAgentToolResultSuccessModel:
      type: object
      properties:
        result_type:
          type: string
          enum:
            - type: stringLiteral
              value: transfer_to_agent_success
        status:
          type: string
          enum:
            - type: stringLiteral
              value: success
        from_agent:
          type: string
        to_agent:
          type: string
        condition:
          type: string
        delay_ms:
          type: integer
        transfer_message:
          type:
            - string
            - 'null'
        enable_transferred_agent_first_message:
          type: boolean
      required:
        - from_agent
        - to_agent
        - condition
    TransferToAgentToolResultErrorModel:
      type: object
      properties:
        result_type:
          type: string
          enum:
            - type: stringLiteral
              value: transfer_to_agent_error
        status:
          type: string
          enum:
            - type: stringLiteral
              value: error
        from_agent:
          type: string
        error:
          type: string
      required:
        - from_agent
        - error
    TransferToNumberResultTwilioSuccessModel:
      type: object
      properties:
        result_type:
          type: string
          enum:
            - type: stringLiteral
              value: transfer_to_number_twilio_success
        status:
          type: string
          enum:
            - type: stringLiteral
              value: success
        transfer_number:
          type: string
        reason:
          type:
            - string
            - 'null'
        client_message:
          type:
            - string
            - 'null'
        agent_message:
          type: string
        conference_name:
          type: string
        note:
          type:
            - string
            - 'null'
      required:
        - transfer_number
        - agent_message
        - conference_name
    TransferToNumberResultSipSuccessModel:
      type: object
      properties:
        result_type:
          type: string
          enum:
            - type: stringLiteral
              value: transfer_to_number_sip_success
        status:
          type: string
          enum:
            - type: stringLiteral
              value: success
        transfer_number:
          type: string
        reason:
          type:
            - string
            - 'null'
        note:
          type:
            - string
            - 'null'
      required:
        - transfer_number
    TransferToNumberResultErrorModel:
      type: object
      properties:
        result_type:
          type: string
          enum:
            - type: stringLiteral
              value: transfer_to_number_error
        status:
          type: string
          enum:
            - type: stringLiteral
              value: error
        error:
          type: string
        details:
          type:
            - string
            - 'null'
      required:
        - error
    SkipTurnToolResponseModel:
      type: object
      properties:
        result_type:
          type: string
          enum:
            - type: stringLiteral
              value: skip_turn_success
        status:
          type: string
          enum:
            - type: stringLiteral
              value: success
        reason:
          type:
            - string
            - 'null'
    PlayDTMFResultSuccessModel:
      type: object
      properties:
        result_type:
          type: string
          enum:
            - type: stringLiteral
              value: play_dtmf_success
        status:
          type: string
          enum:
            - type: stringLiteral
              value: success
        dtmf_tones:
          type: string
        reason:
          type:
            - string
            - 'null'
      required:
        - dtmf_tones
    PlayDTMFResultErrorModel:
      type: object
      properties:
        result_type:
          type: string
          enum:
            - type: stringLiteral
              value: play_dtmf_error
        status:
          type: string
          enum:
            - type: stringLiteral
              value: error
        error:
          type: string
        details:
          type:
            - string
            - 'null'
      required:
        - error
    VoiceMailDetectionResultSuccessModel:
      type: object
      properties:
        result_type:
          type: string
          enum:
            - type: stringLiteral
              value: voicemail_detection_success
        status:
          type: string
          enum:
            - type: stringLiteral
              value: success
        voicemail_message:
          type:
            - string
            - 'null'
        reason:
          type:
            - string
            - 'null'
    TestToolResultModel:
      type: object
      properties:
        result_type:
          type: string
          enum:
            - type: stringLiteral
              value: testing_tool_result
        status:
          type: string
          enum:
            - type: stringLiteral
              value: success
        reason:
          type: string
    ConversationHistoryTranscriptSystemToolResultCommonModelResult:
      oneOf:
        - $ref: '#/components/schemas/EndCallToolResultModel'
        - $ref: '#/components/schemas/LanguageDetectionToolResultModel'
        - $ref: '#/components/schemas/TransferToAgentToolResultSuccessModel'
        - $ref: '#/components/schemas/TransferToAgentToolResultErrorModel'
        - $ref: '#/components/schemas/TransferToNumberResultTwilioSuccessModel'
        - $ref: '#/components/schemas/TransferToNumberResultSipSuccessModel'
        - $ref: '#/components/schemas/TransferToNumberResultErrorModel'
        - $ref: '#/components/schemas/SkipTurnToolResponseModel'
        - $ref: '#/components/schemas/PlayDTMFResultSuccessModel'
        - $ref: '#/components/schemas/PlayDTMFResultErrorModel'
        - $ref: '#/components/schemas/VoiceMailDetectionResultSuccessModel'
        - $ref: '#/components/schemas/TestToolResultModel'
    ConversationHistoryTranscriptSystemToolResultCommonModel:
      type: object
      properties:
        request_id:
          type: string
        tool_name:
          type: string
        result_value:
          type: string
        is_error:
          type: boolean
        tool_has_been_called:
          type: boolean
        tool_latency_secs:
          type: number
          format: double
        dynamic_variable_updates:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableUpdateCommonModel'
        type:
          type: string
          enum:
            - type: stringLiteral
              value: system
        result:
          oneOf:
            - $ref: >-
                #/components/schemas/ConversationHistoryTranscriptSystemToolResultCommonModelResult
            - type: 'null'
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
        - type
    WorkflowToolEdgeStepModel:
      type: object
      properties:
        step_latency_secs:
          type: number
          format: double
        type:
          type: string
          enum:
            - type: stringLiteral
              value: edge
        edge_id:
          type: string
        target_node_id:
          type: string
      required:
        - step_latency_secs
        - edge_id
        - target_node_id
    WorkflowToolNestedToolsStepModelOutputResultsItems:
      oneOf:
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptOtherToolsResultCommonModel
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptSystemToolResultCommonModel
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptWorkflowToolsResultCommonModel-Output
    WorkflowToolNestedToolsStepModel-Output:
      type: object
      properties:
        step_latency_secs:
          type: number
          format: double
        type:
          type: string
          enum:
            - type: stringLiteral
              value: nested_tools
        node_id:
          type: string
        requests:
          type: array
          items:
            $ref: >-
              #/components/schemas/ConversationHistoryTranscriptToolCallCommonModel
        results:
          type: array
          items:
            $ref: >-
              #/components/schemas/WorkflowToolNestedToolsStepModelOutputResultsItems
        is_successful:
          type: boolean
      required:
        - step_latency_secs
        - node_id
        - requests
        - results
        - is_successful
    WorkflowToolMaxIterationsExceededStepModel:
      type: object
      properties:
        step_latency_secs:
          type: number
          format: double
        type:
          type: string
          enum:
            - type: stringLiteral
              value: max_iterations_exceeded
        max_iterations:
          type: integer
      required:
        - step_latency_secs
        - max_iterations
    WorkflowToolResponseModelOutputStepsItems:
      oneOf:
        - $ref: '#/components/schemas/WorkflowToolEdgeStepModel'
        - $ref: '#/components/schemas/WorkflowToolNestedToolsStepModel-Output'
        - $ref: '#/components/schemas/WorkflowToolMaxIterationsExceededStepModel'
    WorkflowToolResponseModel-Output:
      type: object
      properties:
        steps:
          type: array
          items:
            $ref: '#/components/schemas/WorkflowToolResponseModelOutputStepsItems'
    ConversationHistoryTranscriptWorkflowToolsResultCommonModel-Output:
      type: object
      properties:
        request_id:
          type: string
        tool_name:
          type: string
        result_value:
          type: string
        is_error:
          type: boolean
        tool_has_been_called:
          type: boolean
        tool_latency_secs:
          type: number
          format: double
        dynamic_variable_updates:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableUpdateCommonModel'
        type:
          type: string
          enum:
            - type: stringLiteral
              value: workflow
        result:
          oneOf:
            - $ref: '#/components/schemas/WorkflowToolResponseModel-Output'
            - type: 'null'
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
        - type
    ConversationHistoryTranscriptCommonModelOutputToolResultsItems:
      oneOf:
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptOtherToolsResultCommonModel
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptSystemToolResultCommonModel
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptWorkflowToolsResultCommonModel-Output
    UserFeedbackScore:
      type: string
      enum:
        - value: like
        - value: dislike
    UserFeedback:
      type: object
      properties:
        score:
          $ref: '#/components/schemas/UserFeedbackScore'
        time_in_call_secs:
          type: integer
      required:
        - score
        - time_in_call_secs
    MetricRecord:
      type: object
      properties:
        elapsed_time:
          type: number
          format: double
      required:
        - elapsed_time
    ConversationTurnMetrics:
      type: object
      properties:
        metrics:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/MetricRecord'
    RagChunkMetadata:
      type: object
      properties:
        document_id:
          type: string
        chunk_id:
          type: string
        vector_distance:
          type: number
          format: double
      required:
        - document_id
        - chunk_id
        - vector_distance
    EmbeddingModelEnum:
      type: string
      enum:
        - value: e5_mistral_7b_instruct
        - value: multilingual_e5_large_instruct
    RagRetrievalInfo:
      type: object
      properties:
        chunks:
          type: array
          items:
            $ref: '#/components/schemas/RagChunkMetadata'
        embedding_model:
          $ref: '#/components/schemas/EmbeddingModelEnum'
        retrieval_query:
          type: string
        rag_latency_secs:
          type: number
          format: double
      required:
        - chunks
        - embedding_model
        - retrieval_query
        - rag_latency_secs
    LLMTokensCategoryUsage:
      type: object
      properties:
        tokens:
          type: integer
        price:
          type: number
          format: double
    LLMInputOutputTokensUsage:
      type: object
      properties:
        input:
          $ref: '#/components/schemas/LLMTokensCategoryUsage'
        input_cache_read:
          $ref: '#/components/schemas/LLMTokensCategoryUsage'
        input_cache_write:
          $ref: '#/components/schemas/LLMTokensCategoryUsage'
        output_total:
          $ref: '#/components/schemas/LLMTokensCategoryUsage'
    LLMUsage-Output:
      type: object
      properties:
        model_usage:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LLMInputOutputTokensUsage'
    ConversationHistoryTranscriptCommonModelOutputSourceMedium:
      type: string
      enum:
        - value: audio
        - value: text
    ConversationHistoryTranscriptCommonModel-Output:
      type: object
      properties:
        role:
          $ref: >-
            #/components/schemas/ConversationHistoryTranscriptCommonModelOutputRole
        agent_metadata:
          oneOf:
            - $ref: '#/components/schemas/AgentMetadata'
            - type: 'null'
        message:
          type:
            - string
            - 'null'
        multivoice_message:
          oneOf:
            - $ref: '#/components/schemas/ConversationHistoryMultivoiceMessageModel'
            - type: 'null'
        tool_calls:
          type: array
          items:
            $ref: >-
              #/components/schemas/ConversationHistoryTranscriptToolCallCommonModel
        tool_results:
          type: array
          items:
            $ref: >-
              #/components/schemas/ConversationHistoryTranscriptCommonModelOutputToolResultsItems
        feedback:
          oneOf:
            - $ref: '#/components/schemas/UserFeedback'
            - type: 'null'
        llm_override:
          type:
            - string
            - 'null'
        time_in_call_secs:
          type: integer
        conversation_turn_metrics:
          oneOf:
            - $ref: '#/components/schemas/ConversationTurnMetrics'
            - type: 'null'
        rag_retrieval_info:
          oneOf:
            - $ref: '#/components/schemas/RagRetrievalInfo'
            - type: 'null'
        llm_usage:
          oneOf:
            - $ref: '#/components/schemas/LLMUsage-Output'
            - type: 'null'
        interrupted:
          type: boolean
        original_message:
          type:
            - string
            - 'null'
        source_medium:
          oneOf:
            - $ref: >-
                #/components/schemas/ConversationHistoryTranscriptCommonModelOutputSourceMedium
            - type: 'null'
      required:
        - role
        - time_in_call_secs
    ConversationDeletionSettings:
      type: object
      properties:
        deletion_time_unix_secs:
          type:
            - integer
            - 'null'
        deleted_logs_at_time_unix_secs:
          type:
            - integer
            - 'null'
        deleted_audio_at_time_unix_secs:
          type:
            - integer
            - 'null'
        deleted_transcript_at_time_unix_secs:
          type:
            - integer
            - 'null'
        delete_transcript_and_pii:
          type: boolean
        delete_audio:
          type: boolean
    ConversationFeedbackType:
      type: string
      enum:
        - value: thumbs
        - value: rating
    ConversationHistoryFeedbackCommonModel:
      type: object
      properties:
        type:
          oneOf:
            - $ref: '#/components/schemas/ConversationFeedbackType'
            - type: 'null'
        overall_score:
          oneOf:
            - $ref: '#/components/schemas/UserFeedbackScore'
            - type: 'null'
        likes:
          type: integer
        dislikes:
          type: integer
        rating:
          type:
            - integer
            - 'null'
        comment:
          type:
            - string
            - 'null'
    AuthorizationMethod:
      type: string
      enum:
        - value: invalid
        - value: public
        - value: authorization_header
        - value: signed_url
        - value: shareable_link
        - value: livekit_token
        - value: livekit_token_website
        - value: genesys_api_key
    LLMCategoryUsage:
      type: object
      properties:
        irreversible_generation:
          $ref: '#/components/schemas/LLMUsage-Output'
        initiated_generation:
          $ref: '#/components/schemas/LLMUsage-Output'
    ConversationChargingCommonModel:
      type: object
      properties:
        dev_discount:
          type: boolean
        is_burst:
          type: boolean
        tier:
          type:
            - string
            - 'null'
        llm_usage:
          $ref: '#/components/schemas/LLMCategoryUsage'
        llm_price:
          type:
            - number
            - 'null'
          format: double
        llm_charge:
          type:
            - integer
            - 'null'
        call_charge:
          type:
            - integer
            - 'null'
        free_minutes_consumed:
          type: number
          format: double
        free_llm_dollars_consumed:
          type: number
          format: double
    ConversationHistoryTwilioPhoneCallModelDirection:
      type: string
      enum:
        - value: inbound
        - value: outbound
    ConversationHistoryTwilioPhoneCallModel:
      type: object
      properties:
        direction:
          $ref: >-
            #/components/schemas/ConversationHistoryTwilioPhoneCallModelDirection
        phone_number_id:
          type: string
        agent_number:
          type: string
        external_number:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: twilio
        stream_sid:
          type: string
        call_sid:
          type: string
      required:
        - direction
        - phone_number_id
        - agent_number
        - external_number
        - type
        - stream_sid
        - call_sid
    ConversationHistorySipTrunkingPhoneCallModelDirection:
      type: string
      enum:
        - value: inbound
        - value: outbound
    ConversationHistorySIPTrunkingPhoneCallModel:
      type: object
      properties:
        direction:
          $ref: >-
            #/components/schemas/ConversationHistorySipTrunkingPhoneCallModelDirection
        phone_number_id:
          type: string
        agent_number:
          type: string
        external_number:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: sip_trunking
        call_sid:
          type: string
      required:
        - direction
        - phone_number_id
        - agent_number
        - external_number
        - type
        - call_sid
    ConversationHistoryMetadataCommonModelPhoneCall:
      oneOf:
        - $ref: '#/components/schemas/ConversationHistoryTwilioPhoneCallModel'
        - $ref: '#/components/schemas/ConversationHistorySIPTrunkingPhoneCallModel'
    ConversationHistoryBatchCallModel:
      type: object
      properties:
        batch_call_id:
          type: string
        batch_call_recipient_id:
          type: string
      required:
        - batch_call_id
        - batch_call_recipient_id
    ConversationHistoryErrorCommonModel:
      type: object
      properties:
        code:
          type: integer
        reason:
          type:
            - string
            - 'null'
      required:
        - code
    ConversationHistoryRagUsageCommonModel:
      type: object
      properties:
        usage_count:
          type: integer
        embedding_model:
          type: string
      required:
        - usage_count
        - embedding_model
    FeatureStatusCommonModel:
      type: object
      properties:
        enabled:
          type: boolean
        used:
          type: boolean
    WorkflowFeaturesUsageCommonModel:
      type: object
      properties:
        enabled:
          type: boolean
        tool_node:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        standalone_agent_node:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        phone_number_node:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        end_node:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
    TestsFeatureUsageCommonModel:
      type: object
      properties:
        enabled:
          type: boolean
        tests_ran_after_last_modification:
          type: boolean
        tests_ran_in_last_7_days:
          type: boolean
    FeaturesUsageCommonModel:
      type: object
      properties:
        language_detection:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        transfer_to_agent:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        transfer_to_number:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        multivoice:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        dtmf_tones:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        external_mcp_servers:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        pii_zrm_workspace:
          type: boolean
        pii_zrm_agent:
          type: boolean
        tool_dynamic_variable_updates:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        is_livekit:
          type: boolean
        voicemail_detection:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        workflow:
          $ref: '#/components/schemas/WorkflowFeaturesUsageCommonModel'
        agent_testing:
          $ref: '#/components/schemas/TestsFeatureUsageCommonModel'
    ConversationHistoryElevenAssistantCommonModel:
      type: object
      properties:
        is_eleven_assistant:
          type: boolean
    ConversationInitiationSource:
      type: string
      enum:
        - value: unknown
        - value: android_sdk
        - value: node_js_sdk
        - value: react_native_sdk
        - value: react_sdk
        - value: js_sdk
        - value: python_sdk
        - value: widget
        - value: sip_trunk
        - value: twilio
        - value: genesys
        - value: swift_sdk
        - value: whatsapp
    DefaultConversationInitiationTrigger:
      type: object
      properties:
        trigger_type:
          type: string
          enum:
            - type: stringLiteral
              value: default
    ZendeskConversationInitiationTrigger:
      type: object
      properties:
        trigger_type:
          type: string
          enum:
            - type: stringLiteral
              value: zendesk
        ticket_id:
          type: integer
      required:
        - ticket_id
    ConversationHistoryMetadataCommonModelInitiationTrigger:
      oneOf:
        - $ref: '#/components/schemas/DefaultConversationInitiationTrigger'
        - $ref: '#/components/schemas/ZendeskConversationInitiationTrigger'
    AsyncConversationMetadataDeliveryStatus:
      type: string
      enum:
        - value: pending
        - value: success
        - value: failed
    AsyncConversationMetadata:
      type: object
      properties:
        delivery_status:
          $ref: '#/components/schemas/AsyncConversationMetadataDeliveryStatus'
        delivery_timestamp:
          type: integer
        delivery_error:
          type:
            - string
            - 'null'
        external_system:
          type: string
        external_id:
          type: string
        retry_count:
          type: integer
        last_retry_timestamp:
          type:
            - integer
            - 'null'
      required:
        - delivery_status
        - delivery_timestamp
        - external_system
        - external_id
    WhatsAppConversationInfo:
      type: object
      properties:
        whatsapp_business_account_id:
          type: string
        whatsapp_user_id:
          type: string
      required:
        - whatsapp_business_account_id
        - whatsapp_user_id
    AgentDefinitionSource:
      type: string
      enum:
        - value: cli
        - value: ui
        - value: api
        - value: unknown
    ConversationHistoryMetadataCommonModel:
      type: object
      properties:
        start_time_unix_secs:
          type: integer
        accepted_time_unix_secs:
          type:
            - integer
            - 'null'
        call_duration_secs:
          type: integer
        cost:
          type:
            - integer
            - 'null'
        deletion_settings:
          $ref: '#/components/schemas/ConversationDeletionSettings'
        feedback:
          $ref: '#/components/schemas/ConversationHistoryFeedbackCommonModel'
        authorization_method:
          $ref: '#/components/schemas/AuthorizationMethod'
        charging:
          $ref: '#/components/schemas/ConversationChargingCommonModel'
        phone_call:
          oneOf:
            - $ref: >-
                #/components/schemas/ConversationHistoryMetadataCommonModelPhoneCall
            - type: 'null'
        batch_call:
          oneOf:
            - $ref: '#/components/schemas/ConversationHistoryBatchCallModel'
            - type: 'null'
        termination_reason:
          type: string
        error:
          oneOf:
            - $ref: '#/components/schemas/ConversationHistoryErrorCommonModel'
            - type: 'null'
        main_language:
          type:
            - string
            - 'null'
        rag_usage:
          oneOf:
            - $ref: '#/components/schemas/ConversationHistoryRagUsageCommonModel'
            - type: 'null'
        text_only:
          type: boolean
        features_usage:
          $ref: '#/components/schemas/FeaturesUsageCommonModel'
        eleven_assistant:
          $ref: '#/components/schemas/ConversationHistoryElevenAssistantCommonModel'
        initiator_id:
          type:
            - string
            - 'null'
        conversation_initiation_source:
          $ref: '#/components/schemas/ConversationInitiationSource'
        conversation_initiation_source_version:
          type:
            - string
            - 'null'
        timezone:
          type:
            - string
            - 'null'
        initiation_trigger:
          $ref: >-
            #/components/schemas/ConversationHistoryMetadataCommonModelInitiationTrigger
        async_metadata:
          oneOf:
            - $ref: '#/components/schemas/AsyncConversationMetadata'
            - type: 'null'
        whatsapp:
          oneOf:
            - $ref: '#/components/schemas/WhatsAppConversationInfo'
            - type: 'null'
        agent_created_from:
          $ref: '#/components/schemas/AgentDefinitionSource'
        agent_last_updated_from:
          $ref: '#/components/schemas/AgentDefinitionSource'
      required:
        - start_time_unix_secs
        - call_duration_secs
    EvaluationSuccessResult:
      type: string
      enum:
        - value: success
        - value: failure
        - value: unknown
    ConversationHistoryEvaluationCriteriaResultCommonModel:
      type: object
      properties:
        criteria_id:
          type: string
        result:
          $ref: '#/components/schemas/EvaluationSuccessResult'
        rationale:
          type: string
      required:
        - criteria_id
        - result
        - rationale
    LiteralJsonSchemaPropertyType:
      type: string
      enum:
        - value: boolean
        - value: string
        - value: integer
        - value: number
    LiteralJsonSchemaPropertyConstantValue:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
    LiteralJsonSchemaProperty:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/LiteralJsonSchemaPropertyType'
        description:
          type: string
        enum:
          type:
            - array
            - 'null'
          items:
            type: string
        is_system_provided:
          type: boolean
        dynamic_variable:
          type: string
        constant_value:
          $ref: '#/components/schemas/LiteralJsonSchemaPropertyConstantValue'
      required:
        - type
    DataCollectionResultCommonModel:
      type: object
      properties:
        data_collection_id:
          type: string
        value:
          description: Any type
        json_schema:
          oneOf:
            - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
            - type: 'null'
        rationale:
          type: string
      required:
        - data_collection_id
        - rationale
    ConversationHistoryAnalysisCommonModel:
      type: object
      properties:
        evaluation_criteria_results:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/ConversationHistoryEvaluationCriteriaResultCommonModel
        data_collection_results:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/DataCollectionResultCommonModel'
        call_successful:
          $ref: '#/components/schemas/EvaluationSuccessResult'
        transcript_summary:
          type: string
        call_summary_title:
          type:
            - string
            - 'null'
      required:
        - call_successful
        - transcript_summary
    SoftTimeoutConfigOverride:
      type: object
      properties:
        message:
          type:
            - string
            - 'null'
    TurnConfigOverride:
      type: object
      properties:
        soft_timeout_config:
          oneOf:
            - $ref: '#/components/schemas/SoftTimeoutConfigOverride'
            - type: 'null'
    TTSConversationalConfigOverride:
      type: object
      properties:
        voice_id:
          type:
            - string
            - 'null'
        stability:
          type:
            - number
            - 'null'
          format: double
        speed:
          type:
            - number
            - 'null'
          format: double
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
    ConversationConfigOverride:
      type: object
      properties:
        text_only:
          type:
            - boolean
            - 'null'
    LLM:
      type: string
      enum:
        - value: gpt-4o-mini
        - value: gpt-4o
        - value: gpt-4
        - value: gpt-4-turbo
        - value: gpt-4.1
        - value: gpt-4.1-mini
        - value: gpt-4.1-nano
        - value: gpt-5
        - value: gpt-5-mini
        - value: gpt-5-nano
        - value: gpt-3.5-turbo
        - value: gemini-1.5-pro
        - value: gemini-1.5-flash
        - value: gemini-2.0-flash
        - value: gemini-2.0-flash-lite
        - value: gemini-2.5-flash-lite
        - value: gemini-2.5-flash
        - value: claude-sonnet-4-5
        - value: claude-sonnet-4
        - value: claude-haiku-4-5
        - value: claude-3-7-sonnet
        - value: claude-3-5-sonnet
        - value: claude-3-5-sonnet-v1
        - value: claude-3-haiku
        - value: grok-beta
        - value: custom-llm
        - value: qwen3-4b
        - value: qwen3-30b-a3b
        - value: gpt-oss-20b
        - value: gpt-oss-120b
        - value: glm-45-air-fp8
        - value: gemini-2.5-flash-preview-09-2025
        - value: gemini-2.5-flash-lite-preview-09-2025
        - value: gemini-2.5-flash-preview-05-20
        - value: gemini-2.5-flash-preview-04-17
        - value: gemini-2.5-flash-lite-preview-06-17
        - value: gemini-2.0-flash-lite-001
        - value: gemini-2.0-flash-001
        - value: gemini-1.5-flash-002
        - value: gemini-1.5-flash-001
        - value: gemini-1.5-pro-002
        - value: gemini-1.5-pro-001
        - value: claude-sonnet-4@20250514
        - value: claude-sonnet-4-5@20250929
        - value: claude-haiku-4-5@20251001
        - value: claude-3-7-sonnet@20250219
        - value: claude-3-5-sonnet@20240620
        - value: claude-3-5-sonnet-v2@20241022
        - value: claude-3-haiku@20240307
        - value: gpt-5-2025-08-07
        - value: gpt-5-mini-2025-08-07
        - value: gpt-5-nano-2025-08-07
        - value: gpt-4.1-2025-04-14
        - value: gpt-4.1-mini-2025-04-14
        - value: gpt-4.1-nano-2025-04-14
        - value: gpt-4o-mini-2024-07-18
        - value: gpt-4o-2024-11-20
        - value: gpt-4o-2024-08-06
        - value: gpt-4o-2024-05-13
        - value: gpt-4-0613
        - value: gpt-4-0314
        - value: gpt-4-turbo-2024-04-09
        - value: gpt-3.5-turbo-0125
        - value: gpt-3.5-turbo-1106
        - value: watt-tool-8b
        - value: watt-tool-70b
    PromptAgentAPIModelOverride:
      type: object
      properties:
        prompt:
          type:
            - string
            - 'null'
        llm:
          oneOf:
            - $ref: '#/components/schemas/LLM'
            - type: 'null'
        native_mcp_server_ids:
          type:
            - array
            - 'null'
          items:
            type: string
    AgentConfigOverride-Output:
      type: object
      properties:
        first_message:
          type:
            - string
            - 'null'
        language:
          type:
            - string
            - 'null'
        prompt:
          oneOf:
            - $ref: '#/components/schemas/PromptAgentAPIModelOverride'
            - type: 'null'
    ConversationConfigClientOverride-Output:
      type: object
      properties:
        turn:
          oneOf:
            - $ref: '#/components/schemas/TurnConfigOverride'
            - type: 'null'
        tts:
          oneOf:
            - $ref: '#/components/schemas/TTSConversationalConfigOverride'
            - type: 'null'
        conversation:
          oneOf:
            - $ref: '#/components/schemas/ConversationConfigOverride'
            - type: 'null'
        agent:
          oneOf:
            - $ref: '#/components/schemas/AgentConfigOverride-Output'
            - type: 'null'
    ConversationInitiationClientDataRequestOutputCustomLlmExtraBody:
      type: object
      properties: {}
    ConversationInitiationSourceInfo:
      type: object
      properties:
        source:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationSource'
            - type: 'null'
        version:
          type:
            - string
            - 'null'
    ConversationInitiationClientDataRequestOutputDynamicVariables:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: integer
        - type: boolean
    ConversationInitiationClientDataRequest-Output:
      type: object
      properties:
        conversation_config_override:
          $ref: '#/components/schemas/ConversationConfigClientOverride-Output'
        custom_llm_extra_body:
          $ref: >-
            #/components/schemas/ConversationInitiationClientDataRequestOutputCustomLlmExtraBody
        user_id:
          type:
            - string
            - 'null'
        source_info:
          $ref: '#/components/schemas/ConversationInitiationSourceInfo'
        dynamic_variables:
          type: object
          additionalProperties:
            oneOf:
              - $ref: >-
                  #/components/schemas/ConversationInitiationClientDataRequestOutputDynamicVariables
              - type: 'null'
    GetConversationResponseModel:
      type: object
      properties:
        agent_id:
          type: string
        conversation_id:
          type: string
        status:
          $ref: '#/components/schemas/GetConversationResponseModelStatus'
        user_id:
          type:
            - string
            - 'null'
        branch_id:
          type:
            - string
            - 'null'
        transcript:
          type: array
          items:
            $ref: >-
              #/components/schemas/ConversationHistoryTranscriptCommonModel-Output
        metadata:
          $ref: '#/components/schemas/ConversationHistoryMetadataCommonModel'
        analysis:
          oneOf:
            - $ref: '#/components/schemas/ConversationHistoryAnalysisCommonModel'
            - type: 'null'
        conversation_initiation_client_data:
          $ref: '#/components/schemas/ConversationInitiationClientDataRequest-Output'
        has_audio:
          type: boolean
        has_user_audio:
          type: boolean
        has_response_audio:
          type: boolean
      required:
        - agent_id
        - conversation_id
        - status
        - transcript
        - metadata
        - has_audio
        - has_user_audio
        - has_response_audio

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.conversations.get("123");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.conversations.get(
    conversation_id="123"
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/123"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/123")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/123")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/123', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/123");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/123")! as URL,
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


# Delete conversation

DELETE https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}

Delete a particular conversation

Reference: https://elevenlabs.io/docs/api-reference/conversations/delete


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete Conversation
  version: endpoint_conversationalAi/conversations.delete
paths:
  /v1/convai/conversations/{conversation_id}:
    delete:
      operationId: delete
      summary: Delete Conversation
      description: Delete a particular conversation
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/conversations
      parameters:
        - name: conversation_id
          in: path
          description: The id of the conversation you're taking the action on.
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
    await client.conversationalAi.conversations.delete("conversation_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.conversations.delete(
    conversation_id="conversation_id"
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/conversation_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/conversation_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/convai/conversations/conversation_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/convai/conversations/conversation_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/conversation_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/conversation_id")! as URL,
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


# Get conversation audio

GET https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/audio

Get the audio recording of a particular conversation

Reference: https://elevenlabs.io/docs/api-reference/conversations/get-audio


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Conversation Audio
  version: endpoint_conversationalAi/conversations/audio.get
paths:
  /v1/convai/conversations/{conversation_id}/audio:
    get:
      operationId: get
      summary: Get Conversation Audio
      description: Get the audio recording of a particular conversation
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/conversations
          - subpackage_conversationalAi/conversations/audio
      parameters:
        - name: conversation_id
          in: path
          description: The id of the conversation you're taking the action on.
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
          description: Successful response
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
    await client.conversationalAi.conversations.audio.get("conversation_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.conversations.audio.get(
    conversation_id="conversation_id"
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio")! as URL,
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


# Get signed URL

GET https://api.elevenlabs.io/v1/convai/conversation/get-signed-url

Get a signed url to start a conversation with an agent with an agent that requires authorization

Reference: https://elevenlabs.io/docs/api-reference/conversations/get-signed-url


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Signed Url
  version: endpoint_conversationalAi/conversations.get_signed_url
paths:
  /v1/convai/conversation/get-signed-url:
    get:
      operationId: get-signed-url
      summary: Get Signed Url
      description: >-
        Get a signed url to start a conversation with an agent with an agent
        that requires authorization
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/conversations
      parameters:
        - name: agent_id
          in: query
          description: The id of the agent you're taking the action on.
          required: true
          schema:
            type: string
        - name: include_conversation_id
          in: query
          description: >-
            Whether to include a conversation_id with the response. If included,
            the conversation_signature cannot be used again.
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
                $ref: '#/components/schemas/ConversationSignedUrlResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    ConversationSignedUrlResponseModel:
      type: object
      properties:
        signed_url:
          type: string
      required:
        - signed_url

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.conversations.getSignedUrl({
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

client.conversational_ai.conversations.get_signed_url(
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

	url := "https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=agent_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=agent_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=agent_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=agent_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=agent_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=agent_id")! as URL,
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


# Get conversation token

GET https://api.elevenlabs.io/v1/convai/conversation/token

Get a WebRTC session token for real-time communication.

Reference: https://elevenlabs.io/docs/api-reference/conversations/get-webrtc-token


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: >-
    Get a webrtc token to start a conversation with an agent that requires
    authorization
  version: endpoint_conversationalAi/conversations.get_webrtc_token
paths:
  /v1/convai/conversation/token:
    get:
      operationId: get-webrtc-token
      summary: >-
        Get a webrtc token to start a conversation with an agent that requires
        authorization
      description: Get a WebRTC session token for real-time communication.
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/conversations
      parameters:
        - name: agent_id
          in: query
          description: The id of the agent you're taking the action on.
          required: true
          schema:
            type: string
        - name: participant_name
          in: query
          description: >-
            Optional custom participant name. If not provided, user ID will be
            used
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
                $ref: '#/components/schemas/TokenResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    TokenResponseModel:
      type: object
      properties:
        token:
          type: string
      required:
        - token

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.conversations.getWebrtcToken({
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

client.conversational_ai.conversations.get_webrtc_token(
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

	url := "https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_id")! as URL,
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


# Send conversation feedback

POST https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/feedback
Content-Type: application/json

Send the feedback for the given conversation

Reference: https://elevenlabs.io/docs/api-reference/conversations/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Send Conversation Feedback
  version: endpoint_conversationalAi/conversations/feedback.create
paths:
  /v1/convai/conversations/{conversation_id}/feedback:
    post:
      operationId: create
      summary: Send Conversation Feedback
      description: Send the feedback for the given conversation
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/conversations
          - subpackage_conversationalAi/conversations/feedback
      parameters:
        - name: conversation_id
          in: path
          description: The id of the conversation you're taking the action on.
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
              $ref: '#/components/schemas/ConversationFeedbackRequestModel'
components:
  schemas:
    UserFeedbackScore:
      type: string
      enum:
        - value: like
        - value: dislike
    ConversationFeedbackRequestModel:
      type: object
      properties:
        feedback:
          oneOf:
            - $ref: '#/components/schemas/UserFeedbackScore'
            - type: 'null'

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.conversations.feedback.create("conversation_id", {
        feedback: "like",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.conversations.feedback.create(
    conversation_id="conversation_id",
    feedback="like"
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/feedback"

	payload := strings.NewReader("{\n  \"feedback\": \"like\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/feedback")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"feedback\": \"like\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/feedback")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"feedback\": \"like\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/conversations/conversation_id/feedback', [
  'body' => '{
  "feedback": "like"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/feedback");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"feedback\": \"like\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["feedback": "like"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/feedback")! as URL,
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


# List tools

GET https://api.elevenlabs.io/v1/convai/tools

Get all available tools in the workspace.

Reference: https://elevenlabs.io/docs/api-reference/tools/list


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Tools
  version: endpoint_conversationalAi/tools.list
paths:
  /v1/convai/tools:
    get:
      operationId: list
      summary: Get Tools
      description: Get all available tools in the workspace.
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/tools
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
                $ref: '#/components/schemas/ToolsResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    DynamicVariableAssignment:
      type: object
      properties:
        source:
          type: string
          enum:
            - type: stringLiteral
              value: response
        dynamic_variable:
          type: string
        value_path:
          type: string
      required:
        - dynamic_variable
        - value_path
    ToolCallSoundType:
      type: string
      enum:
        - value: typing
        - value: elevator1
        - value: elevator2
        - value: elevator3
        - value: elevator4
    ToolCallSoundBehavior:
      type: string
      enum:
        - value: auto
        - value: always
    DynamicVariablesConfigDynamicVariablePlaceholders:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: integer
        - type: boolean
    DynamicVariablesConfig:
      type: object
      properties:
        dynamic_variable_placeholders:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/DynamicVariablesConfigDynamicVariablePlaceholders
    ToolExecutionMode:
      type: string
      enum:
        - value: immediate
        - value: post_tool_speech
        - value: async
    WebhookToolApiSchemaConfigOutputMethod:
      type: string
      enum:
        - value: GET
        - value: POST
        - value: PUT
        - value: PATCH
        - value: DELETE
    LiteralJsonSchemaPropertyType:
      type: string
      enum:
        - value: boolean
        - value: string
        - value: integer
        - value: number
    LiteralJsonSchemaPropertyConstantValue:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
    LiteralJsonSchemaProperty:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/LiteralJsonSchemaPropertyType'
        description:
          type: string
        enum:
          type:
            - array
            - 'null'
          items:
            type: string
        is_system_provided:
          type: boolean
        dynamic_variable:
          type: string
        constant_value:
          $ref: '#/components/schemas/LiteralJsonSchemaPropertyConstantValue'
      required:
        - type
    QueryParamsJsonSchema:
      type: object
      properties:
        properties:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        required:
          type: array
          items:
            type: string
      required:
        - properties
    ArrayJsonSchemaPropertyOutputItems:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
        - $ref: '#/components/schemas/ArrayJsonSchemaProperty-Output'
    ArrayJsonSchemaProperty-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: array
        description:
          type: string
        items:
          $ref: '#/components/schemas/ArrayJsonSchemaPropertyOutputItems'
      required:
        - items
    ObjectJsonSchemaPropertyOutput:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
        - $ref: '#/components/schemas/ArrayJsonSchemaProperty-Output'
    ObjectJsonSchemaProperty-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: object
        required:
          type: array
          items:
            type: string
        description:
          type: string
        properties:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ObjectJsonSchemaPropertyOutput'
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
    ConvAIDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
    WebhookToolApiSchemaConfigOutputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    AuthConnectionLocator:
      type: object
      properties:
        auth_connection_id:
          type: string
      required:
        - auth_connection_id
    WebhookToolApiSchemaConfig-Output:
      type: object
      properties:
        url:
          type: string
        method:
          $ref: '#/components/schemas/WebhookToolApiSchemaConfigOutputMethod'
        path_params_schema:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        query_params_schema:
          oneOf:
            - $ref: '#/components/schemas/QueryParamsJsonSchema'
            - type: 'null'
        request_body_schema:
          oneOf:
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/WebhookToolApiSchemaConfigOutputRequestHeaders
        auth_connection:
          oneOf:
            - $ref: '#/components/schemas/AuthConnectionLocator'
            - type: 'null'
      required:
        - url
    WebhookToolConfig-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: webhook
        name:
          type: string
        description:
          type: string
        response_timeout_secs:
          type: integer
        disable_interruptions:
          type: boolean
        force_pre_tool_speech:
          type: boolean
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        dynamic_variables:
          $ref: '#/components/schemas/DynamicVariablesConfig'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        api_schema:
          $ref: '#/components/schemas/WebhookToolApiSchemaConfig-Output'
      required:
        - name
        - description
        - api_schema
    ClientToolConfig-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: client
        name:
          type: string
        description:
          type: string
        response_timeout_secs:
          type: integer
        disable_interruptions:
          type: boolean
        force_pre_tool_speech:
          type: boolean
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        parameters:
          oneOf:
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
            - type: 'null'
        expects_response:
          type: boolean
        dynamic_variables:
          $ref: '#/components/schemas/DynamicVariablesConfig'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
      required:
        - name
        - description
    EndCallToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: end_call
    LanguageDetectionToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: language_detection
    AgentTransfer:
      type: object
      properties:
        agent_id:
          type: string
        condition:
          type: string
        delay_ms:
          type: integer
        transfer_message:
          type:
            - string
            - 'null'
        enable_transferred_agent_first_message:
          type: boolean
      required:
        - agent_id
        - condition
    TransferToAgentToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: transfer_to_agent
        transfers:
          type: array
          items:
            $ref: '#/components/schemas/AgentTransfer'
      required:
        - transfers
    PhoneNumberTransferDestination:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: phone
        phone_number:
          type: string
      required:
        - phone_number
    SIPUriTransferDestination:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: sip_uri
        sip_uri:
          type: string
      required:
        - sip_uri
    PhoneNumberDynamicVariableTransferDestination:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: phone_dynamic_variable
        phone_number:
          type: string
      required:
        - phone_number
    SIPUriDynamicVariableTransferDestination:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: sip_uri_dynamic_variable
        sip_uri:
          type: string
      required:
        - sip_uri
    PhoneNumberTransferTransferDestination:
      oneOf:
        - $ref: '#/components/schemas/PhoneNumberTransferDestination'
        - $ref: '#/components/schemas/SIPUriTransferDestination'
        - $ref: '#/components/schemas/PhoneNumberDynamicVariableTransferDestination'
        - $ref: '#/components/schemas/SIPUriDynamicVariableTransferDestination'
    TransferTypeEnum:
      type: string
      enum:
        - value: conference
        - value: sip_refer
    PhoneNumberTransfer:
      type: object
      properties:
        transfer_destination:
          oneOf:
            - $ref: '#/components/schemas/PhoneNumberTransferTransferDestination'
            - type: 'null'
        phone_number:
          type:
            - string
            - 'null'
        condition:
          type: string
        transfer_type:
          $ref: '#/components/schemas/TransferTypeEnum'
      required:
        - condition
    TransferToNumberToolConfig-Output:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: transfer_to_number
        transfers:
          type: array
          items:
            $ref: '#/components/schemas/PhoneNumberTransfer'
        enable_client_message:
          type: boolean
      required:
        - transfers
    SkipTurnToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: skip_turn
    PlayDTMFToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: play_keypad_touch_tone
    VoicemailDetectionToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: voicemail_detection
        voicemail_message:
          type:
            - string
            - 'null'
    SystemToolConfigOutputParams:
      oneOf:
        - $ref: '#/components/schemas/EndCallToolConfig'
        - $ref: '#/components/schemas/LanguageDetectionToolConfig'
        - $ref: '#/components/schemas/TransferToAgentToolConfig'
        - $ref: '#/components/schemas/TransferToNumberToolConfig-Output'
        - $ref: '#/components/schemas/SkipTurnToolConfig'
        - $ref: '#/components/schemas/PlayDTMFToolConfig'
        - $ref: '#/components/schemas/VoicemailDetectionToolConfig'
    SystemToolConfig-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: system
        name:
          type: string
        description:
          type: string
        response_timeout_secs:
          type: integer
        disable_interruptions:
          type: boolean
        force_pre_tool_speech:
          type: boolean
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        params:
          $ref: '#/components/schemas/SystemToolConfigOutputParams'
      required:
        - name
        - params
    LiteralOverrideConstantValue:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
    LiteralOverride:
      type: object
      properties:
        description:
          type:
            - string
            - 'null'
        dynamic_variable:
          type:
            - string
            - 'null'
        constant_value:
          oneOf:
            - $ref: '#/components/schemas/LiteralOverrideConstantValue'
            - type: 'null'
    QueryOverride:
      type: object
      properties:
        properties:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/LiteralOverride'
        required:
          type:
            - array
            - 'null'
          items:
            type: string
    ObjectOverrideOutput:
      oneOf:
        - $ref: '#/components/schemas/LiteralOverride'
        - $ref: '#/components/schemas/ObjectOverride-Output'
    ObjectOverride-Output:
      type: object
      properties:
        description:
          type:
            - string
            - 'null'
        properties:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/ObjectOverrideOutput'
        required:
          type:
            - array
            - 'null'
          items:
            type: string
    ApiIntegrationWebhookOverridesOutputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    ApiIntegrationWebhookOverrides-Output:
      type: object
      properties:
        path_params_schema:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/LiteralOverride'
        query_params_schema:
          oneOf:
            - $ref: '#/components/schemas/QueryOverride'
            - type: 'null'
        request_body_schema:
          oneOf:
            - $ref: '#/components/schemas/ObjectOverride-Output'
            - type: 'null'
        request_headers:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: >-
              #/components/schemas/ApiIntegrationWebhookOverridesOutputRequestHeaders
    ApiIntegrationWebhookToolConfigExternal-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: api_integration_webhook
        name:
          type: string
        description:
          type: string
        response_timeout_secs:
          type: integer
        disable_interruptions:
          type: boolean
        force_pre_tool_speech:
          type: boolean
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        dynamic_variables:
          $ref: '#/components/schemas/DynamicVariablesConfig'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        tool_version:
          type: string
        api_integration_id:
          type: string
        api_integration_connection_id:
          type: string
        api_schema_overrides:
          oneOf:
            - $ref: '#/components/schemas/ApiIntegrationWebhookOverrides-Output'
            - type: 'null'
        base_api_schema:
          $ref: '#/components/schemas/WebhookToolApiSchemaConfig-Output'
      required:
        - type
        - name
        - description
        - response_timeout_secs
        - disable_interruptions
        - force_pre_tool_speech
        - assignments
        - tool_call_sound
        - tool_call_sound_behavior
        - dynamic_variables
        - execution_mode
        - tool_version
        - api_integration_id
        - api_integration_connection_id
        - api_schema_overrides
        - base_api_schema
    ToolResponseModelToolConfig:
      oneOf:
        - $ref: '#/components/schemas/WebhookToolConfig-Output'
        - $ref: '#/components/schemas/ClientToolConfig-Output'
        - $ref: '#/components/schemas/SystemToolConfig-Output'
        - $ref: '#/components/schemas/ApiIntegrationWebhookToolConfigExternal-Output'
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
    ToolUsageStatsResponseModel:
      type: object
      properties:
        total_calls:
          type: integer
        avg_latency_secs:
          type: number
          format: double
      required:
        - avg_latency_secs
    ToolResponseModel:
      type: object
      properties:
        id:
          type: string
        tool_config:
          $ref: '#/components/schemas/ToolResponseModelToolConfig'
        access_info:
          $ref: '#/components/schemas/ResourceAccessInfo'
        usage_stats:
          $ref: '#/components/schemas/ToolUsageStatsResponseModel'
      required:
        - id
        - tool_config
        - access_info
        - usage_stats
    ToolsResponseModel:
      type: object
      properties:
        tools:
          type: array
          items:
            $ref: '#/components/schemas/ToolResponseModel'
      required:
        - tools

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.tools.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.tools.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/tools"

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

url = URI("https://api.elevenlabs.io/v1/convai/tools")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/tools")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/tools', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/tools");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/tools")! as URL,
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
**Navigation:** [← Previous](./45-delete-agent.md) | [Index](./index.md) | [Next →](./47-get-tool.md)
