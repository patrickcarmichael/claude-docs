**Navigation:** [← Previous](./08-teams-and-roles-on-the-cohere-platform.md) | [Index](./index.md) | [Next →](./10-chat-with-streaming.md)

---

# Chat

POST https://api.cohere.com/v2/chat
Content-Type: application/json

Generates a text response to a user message and streams it down, token by token. To learn how to use the Chat API with streaming follow our [Text Generation guides](https://docs.cohere.com/v2/docs/chat-api).

Follow the [Migration Guide](https://docs.cohere.com/v2/docs/migrating-v1-to-v2) for instructions on moving from API v1 to API v2.


Reference: https://docs.cohere.com/reference/chat

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Chat API (v2)
  version: endpoint_v2.chat
paths:
  /v2/chat:
    post:
      operationId: chat
      summary: Chat API (v2)
      description: >
        Generates a text response to a user message and streams it down, token
        by token. To learn how to use the Chat API with streaming follow our
        [Text Generation guides](https://docs.cohere.com/v2/docs/chat-api).


        Follow the [Migration
        Guide](https://docs.cohere.com/v2/docs/migrating-v1-to-v2) for
        instructions on moving from API v1 to API v2.
      tags:
        - - subpackage_v2
      parameters:
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Response with status 200
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/v2_chat_Response_stream'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                stream:
                  type: string
                  enum:
                    - type: booleanLiteral
                      value: false
                model:
                  type: string
                messages:
                  $ref: '#/components/schemas/ChatMessages'
                tools:
                  type: array
                  items:
                    $ref: '#/components/schemas/ToolV2'
                strict_tools:
                  type: boolean
                documents:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/V2ChatPostRequestBodyContentApplicationJsonSchemaDocumentsItems
                citation_options:
                  $ref: '#/components/schemas/CitationOptions'
                response_format:
                  $ref: '#/components/schemas/ResponseFormatV2'
                safety_mode:
                  $ref: >-
                    #/components/schemas/V2ChatPostRequestBodyContentApplicationJsonSchemaSafetyMode
                max_tokens:
                  type: integer
                stop_sequences:
                  type: array
                  items:
                    type: string
                temperature:
                  type: number
                  format: double
                seed:
                  type: integer
                frequency_penalty:
                  type: number
                  format: double
                presence_penalty:
                  type: number
                  format: double
                k:
                  type: integer
                p:
                  type: number
                  format: double
                logprobs:
                  type: boolean
                tool_choice:
                  $ref: >-
                    #/components/schemas/V2ChatPostRequestBodyContentApplicationJsonSchemaToolChoice
                thinking:
                  $ref: '#/components/schemas/Thinking'
                priority:
                  type: integer
              required:
                - stream
                - model
                - messages
components:
  schemas:
    UserMessageV2Role:
      type: string
      enum:
        - value: user
    ChatTextContentType:
      type: string
      enum:
        - value: text
    ChatTextContent:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ChatTextContentType'
        text:
          type: string
      required:
        - type
        - text
    ContentType:
      type: string
      enum:
        - value: text
        - value: image_url
    ImageUrlDetail:
      type: string
      enum:
        - value: auto
        - value: low
        - value: high
    ImageUrl:
      type: object
      properties:
        url:
          type: string
        detail:
          $ref: '#/components/schemas/ImageUrlDetail'
      required:
        - url
    ImageContent:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ContentType'
        image_url:
          $ref: '#/components/schemas/ImageUrl'
      required:
        - type
        - image_url
    Content:
      oneOf:
        - $ref: '#/components/schemas/ChatTextContent'
        - $ref: '#/components/schemas/ImageContent'
    UserMessageV2Content1:
      type: array
      items:
        $ref: '#/components/schemas/Content'
    UserMessageV2Content:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/UserMessageV2Content1'
    UserMessageV2:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/UserMessageV2Role'
        content:
          $ref: '#/components/schemas/UserMessageV2Content'
      required:
        - role
        - content
    AssistantMessageV2Role:
      type: string
      enum:
        - value: assistant
    ToolCallV2Type:
      type: string
      enum:
        - value: function
    ToolCallV2Function:
      type: object
      properties:
        name:
          type: string
        arguments:
          type: string
    ToolCallV2:
      type: object
      properties:
        id:
          type: string
        type:
          $ref: '#/components/schemas/ToolCallV2Type'
        function:
          $ref: '#/components/schemas/ToolCallV2Function'
      required:
        - id
        - type
    ChatThinkingContentType:
      type: string
      enum:
        - value: thinking
    ChatThinkingContent:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ChatThinkingContentType'
        thinking:
          type: string
      required:
        - type
        - thinking
    AssistantMessageV2ContentOneOf1Items:
      oneOf:
        - $ref: '#/components/schemas/ChatTextContent'
        - $ref: '#/components/schemas/ChatThinkingContent'
    AssistantMessageV2Content1:
      type: array
      items:
        $ref: '#/components/schemas/AssistantMessageV2ContentOneOf1Items'
    AssistantMessageV2Content:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/AssistantMessageV2Content1'
    Source:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - tool
              description: 'Discriminator value: tool'
            id:
              type: string
            tool_output:
              type: object
              additionalProperties:
                description: Any type
          required:
            - type
          description: tool variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - document
              description: 'Discriminator value: document'
            id:
              type: string
            document:
              type: object
              additionalProperties:
                description: Any type
          required:
            - type
          description: document variant
      discriminator:
        propertyName: type
    CitationType:
      type: string
      enum:
        - value: TEXT_CONTENT
        - value: THINKING_CONTENT
        - value: PLAN
    Citation:
      type: object
      properties:
        start:
          type: integer
        end:
          type: integer
        text:
          type: string
        sources:
          type: array
          items:
            $ref: '#/components/schemas/Source'
        content_index:
          type: integer
        type:
          $ref: '#/components/schemas/CitationType'
    AssistantMessageV2:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/AssistantMessageV2Role'
        tool_calls:
          type: array
          items:
            $ref: '#/components/schemas/ToolCallV2'
        tool_plan:
          type: string
        content:
          $ref: '#/components/schemas/AssistantMessageV2Content'
        citations:
          type: array
          items:
            $ref: '#/components/schemas/Citation'
      required:
        - role
    SystemMessageV2Role:
      type: string
      enum:
        - value: system
    SystemMessageV2ContentOneOf1Items:
      oneOf:
        - $ref: '#/components/schemas/ChatTextContent'
    SystemMessageV2Content1:
      type: array
      items:
        $ref: '#/components/schemas/SystemMessageV2ContentOneOf1Items'
    SystemMessageV2Content:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/SystemMessageV2Content1'
    SystemMessageV2:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/SystemMessageV2Role'
        content:
          $ref: '#/components/schemas/SystemMessageV2Content'
      required:
        - role
        - content
    ToolMessageV2Role:
      type: string
      enum:
        - value: tool
    DocumentContentType:
      type: string
      enum:
        - value: document
    Document-qmvpd9:
      type: object
      properties: {}
    Document:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/Document-qmvpd9'
        id:
          type: string
      required:
        - data
    DocumentContent:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/DocumentContentType'
        document:
          $ref: '#/components/schemas/Document'
      required:
        - type
        - document
    ToolContent:
      oneOf:
        - $ref: '#/components/schemas/ChatTextContent'
        - $ref: '#/components/schemas/DocumentContent'
    ToolMessageV2Content1:
      type: array
      items:
        $ref: '#/components/schemas/ToolContent'
    ToolMessageV2Content:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ToolMessageV2Content1'
    ToolMessageV2:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/ToolMessageV2Role'
        tool_call_id:
          type: string
        content:
          $ref: '#/components/schemas/ToolMessageV2Content'
      required:
        - role
        - tool_call_id
        - content
    ChatMessageV2:
      oneOf:
        - $ref: '#/components/schemas/UserMessageV2'
        - $ref: '#/components/schemas/AssistantMessageV2'
        - $ref: '#/components/schemas/SystemMessageV2'
        - $ref: '#/components/schemas/ToolMessageV2'
    ChatMessages:
      type: array
      items:
        $ref: '#/components/schemas/ChatMessageV2'
    ToolV2Type:
      type: string
      enum:
        - value: function
    ToolV2-6eoehf:
      type: object
      properties: {}
    ToolV2Function:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        parameters:
          $ref: '#/components/schemas/ToolV2-6eoehf'
      required:
        - name
        - parameters
    ToolV2:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ToolV2Type'
        function:
          $ref: '#/components/schemas/ToolV2Function'
      required:
        - type
    V2ChatPostRequestBodyContentApplicationJsonSchemaDocumentsItems:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/Document'
    CitationOptionsMode:
      type: string
      enum:
        - value: ENABLED
        - value: DISABLED
        - value: FAST
        - value: ACCURATE
        - value: 'OFF'
    CitationOptions:
      type: object
      properties:
        mode:
          $ref: '#/components/schemas/CitationOptionsMode'
    ResponseFormatTypeV2:
      type: string
      enum:
        - value: text
        - value: json_object
    ChatTextResponseFormatV2:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ResponseFormatTypeV2'
      required:
        - type
    JsonResponseFormatV2-uu9wid:
      type: object
      properties: {}
    JsonResponseFormatV2:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ResponseFormatTypeV2'
        json_schema:
          $ref: '#/components/schemas/JsonResponseFormatV2-uu9wid'
      required:
        - type
    ResponseFormatV2:
      oneOf:
        - $ref: '#/components/schemas/ChatTextResponseFormatV2'
        - $ref: '#/components/schemas/JsonResponseFormatV2'
    V2ChatPostRequestBodyContentApplicationJsonSchemaSafetyMode:
      type: string
      enum:
        - value: CONTEXTUAL
        - value: STRICT
        - value: 'OFF'
    V2ChatPostRequestBodyContentApplicationJsonSchemaToolChoice:
      type: string
      enum:
        - value: REQUIRED
        - value: NONE
    ThinkingType:
      type: string
      enum:
        - value: enabled
        - value: disabled
    Thinking:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ThinkingType'
        token_budget:
          type: integer
      required:
        - type
    ChatFinishReason:
      type: string
      enum:
        - value: COMPLETE
        - value: STOP_SEQUENCE
        - value: MAX_TOKENS
        - value: TOOL_CALL
        - value: ERROR
        - value: TIMEOUT
    AssistantMessageResponseRole:
      type: string
      enum:
        - value: assistant
    AssistantMessageResponseContentItems:
      oneOf:
        - $ref: '#/components/schemas/ChatTextContent'
        - $ref: '#/components/schemas/ChatThinkingContent'
    AssistantMessageResponse:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/AssistantMessageResponseRole'
        tool_calls:
          type: array
          items:
            $ref: '#/components/schemas/ToolCallV2'
        tool_plan:
          type: string
        content:
          type: array
          items:
            $ref: '#/components/schemas/AssistantMessageResponseContentItems'
        citations:
          type: array
          items:
            $ref: '#/components/schemas/Citation'
      required:
        - role
    UsageBilledUnits:
      type: object
      properties:
        input_tokens:
          type: number
          format: double
        output_tokens:
          type: number
          format: double
        search_units:
          type: number
          format: double
        classifications:
          type: number
          format: double
    UsageTokens:
      type: object
      properties:
        input_tokens:
          type: number
          format: double
        output_tokens:
          type: number
          format: double
    Usage:
      type: object
      properties:
        billed_units:
          $ref: '#/components/schemas/UsageBilledUnits'
        tokens:
          $ref: '#/components/schemas/UsageTokens'
        cached_tokens:
          type: number
          format: double
    LogprobItem:
      type: object
      properties:
        text:
          type: string
        token_ids:
          type: array
          items:
            type: integer
        logprobs:
          type: array
          items:
            type: number
            format: double
      required:
        - token_ids
    v2_chat_Response_stream:
      type: object
      properties:
        id:
          type: string
        finish_reason:
          $ref: '#/components/schemas/ChatFinishReason'
        message:
          $ref: '#/components/schemas/AssistantMessageResponse'
        usage:
          $ref: '#/components/schemas/Usage'
        logprobs:
          type: array
          items:
            $ref: '#/components/schemas/LogprobItem'
      required:
        - id
        - finish_reason
        - message

```

## SDK Code Examples

```typescript Default
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({});

(async () => {
  const response = await cohere.chat({
    model: 'command-a-03-2025',
    messages: [
      {
        role: 'user',
        content: 'Tell me about LLMs',
      },
    ],
  });

  console.log(response);
})();

```

```python Default
import cohere

co = cohere.ClientV2()

response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": "Tell me about LLMs"}],
)

print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClientV2()

async def main():
    response = await co.chat(
        model="command-a-03-2025",
        messages=[{"role": "user", "content": "Tell me about LLMs"}],
    )
    print(response)

asyncio.run(main())

```

```go Default
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.Chat(
		context.TODO(),
		&cohere.V2ChatRequest{
			Model: "command-a-03-2025",
			Messages: cohere.ChatMessages{
				{
					Role: "user",
					User: &cohere.UserMessageV2{
						Content: &cohere.UserMessageV2Content{
							String: "Tell me about LLMs",
						},
					},
				},
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```java Default
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatRequest;
import com.cohere.api.types.*;
import java.util.List;

public class Default {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ChatResponse response =
        cohere
            .v2()
            .chat(
                V2ChatRequest.builder()
                    .model("command-a-03-2025")
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(UserMessageContent.of("Tell me about LLMs"))
                                    .build())))
                    .build());

    System.out.println(response);
  }
}

```

```ruby Default
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Tell me about LLMs\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Default
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": false,
  "model": "command-a-03-2025",
  "messages": [
    {
      "role": "user",
      "content": "Tell me about LLMs"
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Default
var client = new RestClient("https://api.cohere.com/v2/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Tell me about LLMs\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Default
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": false,
  "model": "command-a-03-2025",
  "messages": [
    [
      "role": "user",
      "content": "Tell me about LLMs"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/chat")! as URL,
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

```typescript Documents
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({});

(async () => {
  const response = await cohere.chat({
    model: 'command-a-03-2025',
    messages: [
      {
        role: 'user',
        content: 'Who is more popular: Nsync or Backstreet Boys?',
      },
    ],
    documents: [
      {
        data: {
          title: 'CSPC: Backstreet Boys Popularity Analysis - ChartMasters',
          snippet:
            '↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.',
        },
      },
      {
        data: {
          title: 'CSPC: NSYNC Popularity Analysis - ChartMasters',
          snippet:
            "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven't study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn't a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
        },
      },
      {
        data: {
          title: 'CSPC: Backstreet Boys Popularity Analysis - ChartMasters',
          snippet:
            " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women's – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
        },
      },
      {
        data: {
          title: 'CSPC: NSYNC Popularity Analysis - ChartMasters',
          snippet:
            " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I'll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC's albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
        },
      },
    ],
  });

  console.log(response);
})();

```

```python Documents
import cohere

co = cohere.ClientV2()

response = co.chat(
    model="command-a-03-2025",
    messages=[{
        "role": "user", 
        "content": "Who is more popular: Nsync or Backstreet Boys?"
    }],
    documents=[
        {
            "data":  {
                "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
                "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.",
            }
        },
        {
            "data":  {
                "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
                "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
            }
        },
        {
            "data":  {
                "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
                "snippet": " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
            }
        },
        {
            "data":  {
                "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
                "snippet": " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
            }
        }
    ],
)

print(response)

```

```java Documents
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatRequest;
import com.cohere.api.resources.v2.types.V2ChatRequestDocumentsItem;
import com.cohere.api.types.*;
import java.util.List;
import java.util.Map;

public class Documents {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ChatResponse response =
        cohere
            .v2()
            .chat(
                V2ChatRequest.builder()
                    .model("command-a-03-2025")
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(
                                        UserMessageContent.of(
                                            "Who is more popular: Nsync or Backstreet Boys?"))
                                    .build())))
                    .documents(
                        List.of(
                            V2ChatRequestDocumentsItem.of(
                                Document.builder()
                                    .data(
                                        Map.of(
                                            "title",
                                            "CSPC: Backstreet Boys Popularity Analysis -"
                                                + " ChartMasters",
                                            "snippet",
                                            "↓ Skip to Main Content\n\n"
                                                + "Music industry – One step closer to being"
                                                + " accurate\n\n"
                                                + "CSPC: Backstreet Boys Popularity Analysis\n\n"
                                                + "Hernán Lopez Posted on February 9, 2017 Posted"
                                                + " in CSPC 72 Comments Tagged with Backstreet"
                                                + " Boys, Boy band\n\n"
                                                + "At one point, Backstreet Boys defined success:"
                                                + " massive albums sales across the globe, great"
                                                + " singles sales, plenty of chart topping"
                                                + " releases, hugely hyped tours and tremendous"
                                                + " media coverage.\n\n"
                                                + "It is true that they benefited from"
                                                + " extraordinarily good market conditions in all"
                                                + " markets. After all, the all-time record year"
                                                + " for the music business, as far as revenues in"
                                                + " billion dollars are concerned, was actually"
                                                + " 1999. That is, back when this five men group"
                                                + " was at its peak."))
                                    .build()),
                            V2ChatRequestDocumentsItem.of(
                                Document.builder()
                                    .data(
                                        Map.of(
                                            "title",
                                            "CSPC: NSYNC Popularity Analysis - ChartMasters",
                                            "snippet",
                                            "↓ Skip to Main Content\n\n"
                                                + "Music industry – One step closer to being"
                                                + " accurate\n\n"
                                                + "CSPC: NSYNC Popularity Analysis\n\n"
                                                + "MJD Posted on February 9, 2018 Posted in CSPC"
                                                + " 27 Comments Tagged with Boy band, N'Sync\n\n"
                                                + "At the turn of the millennium three teen acts"
                                                + " were huge in the US, the Backstreet Boys,"
                                                + " Britney Spears and NSYNC. The latter is the"
                                                + " only one we haven't study so far. It took 15"
                                                + " years and Adele to break their record of 2,4"
                                                + " million units sold of No Strings Attached in"
                                                + " its first week alone.\n\n"
                                                + "It wasn't a fluke, as the second fastest"
                                                + " selling album of the Soundscan era prior 2015,"
                                                + " was also theirs since Celebrity debuted with"
                                                + " 1,88 million units sold."))
                                    .build()),
                            V2ChatRequestDocumentsItem.of(
                                Document.builder()
                                    .data(
                                        Map.of(
                                            "title",
                                            "CSPC: Backstreet Boys Popularity Analysis -"
                                                + " ChartMasters",
                                            "snippet",
                                            " 1997, 1998, 2000 and 2001 also rank amongst some"
                                                + " of the very best years.\n\n"
                                                + "Yet the way many music consumers – especially"
                                                + " teenagers and young women's – embraced their"
                                                + " output deserves its own chapter. If Jonas"
                                                + " Brothers and more recently One Direction"
                                                + " reached a great level of popularity during the"
                                                + " past decade, the type of success achieved by"
                                                + " Backstreet Boys is in a completely different"
                                                + " level as they really dominated the business"
                                                + " for a few years all over the world, including"
                                                + " in some countries that were traditionally hard"
                                                + " to penetrate for Western artists.\n\n"
                                                + "We will try to analyze the extent of that"
                                                + " hegemony with this new article with final"
                                                + " results which will more than surprise many"
                                                + " readers."))
                                    .build()),
                            V2ChatRequestDocumentsItem.of(
                                Document.builder()
                                    .data(
                                        Map.of(
                                            "title",
                                            "CSPC: NSYNC Popularity Analysis - ChartMasters",
                                            "snippet",
                                            " Was the teen group led by Justin Timberlake"
                                                + " really that big? Was it only in the US where"
                                                + " they found success? Or were they a global"
                                                + " phenomenon?\n\n"
                                                + "As usual, I'll be using the Commensurate Sales"
                                                + " to Popularity Concept in order to relevantly"
                                                + " gauge their results. This concept will not"
                                                + " only bring you sales information for all"
                                                + " NSYNC's albums, physical and download singles,"
                                                + " as well as audio and video streaming, but it"
                                                + " will also determine their true popularity. If"
                                                + " you are not yet familiar with the CSPC method,"
                                                + " the next page explains it with a short video."
                                                + " I fully recommend watching the video before"
                                                + " getting into the sales figures."))
                                    .build())))
                    .build());
    System.out.println(response);
  }
}

```

```go Documents
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.Chat(
		context.TODO(),
		&cohere.V2ChatRequest{
			Model: "command-a-03-2025",
			Messages: cohere.ChatMessages{
				{
					Role: "user",
					User: &cohere.UserMessageV2{
						Content: &cohere.UserMessageV2Content{
							String: "Who is more popular: Nsync or Backstreet Boys?",
						},
					},
				},
			},
			Documents: []*cohere.V2ChatRequestDocumentsItem{
				{
					Document: &cohere.Document{
						Data: map[string]interface{}{
							"title":   "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
							"snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.",
						},
					},
				},
				{
					Document: &cohere.Document{
						Data: map[string]interface{}{
							"title":   "CSPC: NSYNC Popularity Analysis - ChartMasters",
							"snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven't study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn't a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
						},
					},
				},
				{
					Document: &cohere.Document{
						Data: map[string]interface{}{
							"title":   "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
							"snippet": " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women's – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
						},
					},
				},
				{
					Document: &cohere.Document{
						Data: map[string]interface{}{
							"title":   "CSPC: NSYNC Popularity Analysis - ChartMasters",
							"snippet": " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I'll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC's albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
						},
					},
				},
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```ruby Documents
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Who is more popular: Nsync or Backstreet Boys?\"\n    }\n  ],\n  \"documents\": [\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.\"\n      }\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Documents
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": false,
  "model": "command-a-03-2025",
  "messages": [
    {
      "role": "user",
      "content": "Who is more popular: Nsync or Backstreet Boys?"
    }
  ],
  "documents": [
    {
      "data": {
        "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
        "snippet": "↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak."
      }
    },
    {
      "data": {
        "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
        "snippet": "↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N\'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold."
      }
    },
    {
      "data": {
        "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
        "snippet": "1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers."
      }
    },
    {
      "data": {
        "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
        "snippet": "Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures."
      }
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Documents
var client = new RestClient("https://api.cohere.com/v2/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Who is more popular: Nsync or Backstreet Boys?\"\n    }\n  ],\n  \"documents\": [\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.\"\n      }\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Documents
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": false,
  "model": "command-a-03-2025",
  "messages": [
    [
      "role": "user",
      "content": "Who is more popular: Nsync or Backstreet Boys?"
    ]
  ],
  "documents": [["data": [
        "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
        "snippet": "↓ Skip to Main Content

Music industry – One step closer to being accurate

CSPC: Backstreet Boys Popularity Analysis

Hernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band

At one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.

It is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak."
      ]], ["data": [
        "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
        "snippet": "↓ Skip to Main Content

Music industry – One step closer to being accurate

CSPC: NSYNC Popularity Analysis

MJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync

At the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.

It wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold."
      ]], ["data": [
        "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
        "snippet": "1997, 1998, 2000 and 2001 also rank amongst some of the very best years.
Yet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.

We will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers."
      ]], ["data": [
        "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
        "snippet": "Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?
As usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures."
      ]]]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/chat")! as URL,
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

```typescript Tools
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({});

(async () => {
  const response = await cohere.chat({
    model: 'command-a-03-2025',
    messages: [
      {
        role: 'user',
        content:
          "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
      },
    ],
    tools: [
      {
        type: 'function',
        function: {
          name: 'query_daily_sales_report',
          description:
            'Connects to a database to retrieve overall sales volumes and sales information for a given day.',
          parameters: {
            type: 'object',
            properties: {
              day: {
                description: 'Retrieves sales data for this day, formatted as YYYY-MM-DD.',
                type: 'string',
              },
            },
            required: ['day'],
          },
        },
      },
      {
        type: 'function',
        function: {
          name: 'query_product_catalog',
          description:
            'Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels.',
          parameters: {
            type: 'object',
            properties: {
              category: {
                description:
                  'Retrieves product information data for all products in this category.',
                type: 'string',
              },
            },
            required: ['category'],
          },
        },
      },
    ],
  });

  console.log(response);
})();

```

```python Tools
import cohere

co = cohere.ClientV2()

response = co.chat(
    model="command-a-reasoning-08-2025",
    messages=[
        {
            "role": "user",
            "content": "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
        }
    ],
    tools=[
        cohere.ToolV2(
            type="function",
            function={
                "name": "query_daily_sales_report",
                "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "day": {
                            "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
                            "type": "string",
                        }
                    },
                    "required": ["day"],
                },
            },
        ),
        cohere.ToolV2(
            type="function",
            function={
                "name": "query_product_catalog",
                "description": "Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "description": "Retrieves product information data for all products in this category.",
                            "type": "string",
                        }
                    },
                    "required": ["category"],
                },
            },
        ),
    ],
)

print(response)

```

```java Tools
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatRequest;
import com.cohere.api.types.*;
import java.util.List;
import java.util.Map;

public class Tools {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ChatResponse response =
        cohere
            .v2()
            .chat(
                V2ChatRequest.builder()
                    .model("command-a-reasoning-08-2025")
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(
                                        UserMessageContent.of(
                                            "Can you provide a sales summary for 29th September"
                                                + " 2023, and also give me some details about the"
                                                + " products in the 'Electronics' category, for"
                                                + " example their prices and stock levels?"))
                                    .build())))
                    .tools(
                        List.of(
                            ToolV2.builder()
                                .type("function")
                                .function(
                                    ToolV2Function.builder()
                                        .name("query_daily_sales_report")
                                        .description(
                                            "Connects to a database to retrieve overall sales"
                                                + " volumes and sales information for a given"
                                                + " day.")
                                        .parameters(
                                            Map.of(
                                                "type",
                                                "object",
                                                "properties",
                                                Map.of(
                                                    "day",
                                                    Map.of(
                                                        "description",
                                                        "Retrieves sales data for this day,"
                                                            + " formatted as YYYY-MM-DD.",
                                                        "type",
                                                        "string")),
                                                "required",
                                                List.of("day")))
                                        .build())
                                .build(),
                            ToolV2.builder()
                                .type("function")
                                .function(
                                    ToolV2Function.builder()
                                        .name("query_product_catalog")
                                        .description(
                                            "Connects to a product catalog with information"
                                                + " about all the products being sold, including"
                                                + " categories, prices, and stock levels.")
                                        .parameters(
                                            Map.of(
                                                "type",
                                                "object",
                                                "properties",
                                                Map.of(
                                                    "category",
                                                    Map.of(
                                                        "description",
                                                        "Retrieves product information data for all"
                                                            + " products in this category.",
                                                        "type",
                                                        "string")),
                                                "required",
                                                List.of("category")))
                                        .build())
                                .build()))
                    .build());

    System.out.println(response);
  }
}

```

```go Tools
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.Chat(
		context.TODO(),
		&cohere.V2ChatRequest{
			Model: "command-a-03-2025",
			Messages: cohere.ChatMessages{
				{
					Role: "user",
					User: &cohere.UserMessageV2{
						Content: &cohere.UserMessageV2Content{
							String: "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
						},
					},
				},
			},
			Tools: []*cohere.ToolV2{
				{
					Type: cohere.String("function"),
					Function: &cohere.ToolV2Function{
						Name:        "query_daily_sales_report",
						Description: cohere.String("Connects to a database to retrieve overall sales volumes and sales information for a given day."),
						Parameters: map[string]interface{}{
							"type": "object",
							"properties": map[string]interface{}{
								"day": map[string]interface{}{
									"type":        "string",
									"description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
								},
							},
							"required": []string{"day"},
						},
					},
				},
				{
					Type: cohere.String("function"),
					Function: &cohere.ToolV2Function{
						Name:        "query_product_catalog",
						Description: cohere.String("Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels."),
						Parameters: map[string]interface{}{
							"type": "object",
							"properties": map[string]interface{}{
								"category": map[string]interface{}{
									"type":        "string",
									"description": "Retrieves product information data for all products in this category.",
								},
							},
							"required": []string{"category"},
						},
					},
				},
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```ruby Tools
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stream\": false,\n  \"model\": \"command-r\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_daily_sales_report\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"day\": {\n              \"description\": \"Retrieves sales data for this day, formatted as YYYY-MM-DD.\",\n              \"type\": \"str\"\n            }\n          },\n          \"required\": [\n            \"day\"\n          ],\n          \"x-fern-type-name\": \"tools-by6k68\"\n        },\n        \"description\": \"Connects to a database to retrieve overall sales volumes and sales information for a given day.\"\n      }\n    },\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_product_catalog\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"category\": {\n              \"description\": \"Retrieves product information data for all products in this category.\",\n              \"type\": \"str\"\n            }\n          },\n          \"required\": [\n            \"category\"\n          ],\n          \"x-fern-type-name\": \"tools-o09qd6\"\n        },\n        \"description\": \"Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.\"\n      }\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Tools
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": false,
  "model": "command-r",
  "messages": [
    {
      "role": "user",
      "content": "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the \'Electronics\' category, for example their prices and stock levels?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "query_daily_sales_report",
        "parameters": {
          "type": "object",
          "properties": {
            "day": {
              "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
              "type": "str"
            }
          },
          "required": [
            "day"
          ],
          "x-fern-type-name": "tools-by6k68"
        },
        "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day."
      }
    },
    {
      "type": "function",
      "function": {
        "name": "query_product_catalog",
        "parameters": {
          "type": "object",
          "properties": {
            "category": {
              "description": "Retrieves product information data for all products in this category.",
              "type": "str"
            }
          },
          "required": [
            "category"
          ],
          "x-fern-type-name": "tools-o09qd6"
        },
        "description": "Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels."
      }
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Tools
var client = new RestClient("https://api.cohere.com/v2/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stream\": false,\n  \"model\": \"command-r\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_daily_sales_report\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"day\": {\n              \"description\": \"Retrieves sales data for this day, formatted as YYYY-MM-DD.\",\n              \"type\": \"str\"\n            }\n          },\n          \"required\": [\n            \"day\"\n          ],\n          \"x-fern-type-name\": \"tools-by6k68\"\n        },\n        \"description\": \"Connects to a database to retrieve overall sales volumes and sales information for a given day.\"\n      }\n    },\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_product_catalog\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"category\": {\n              \"description\": \"Retrieves product information data for all products in this category.\",\n              \"type\": \"str\"\n            }\n          },\n          \"required\": [\n            \"category\"\n          ],\n          \"x-fern-type-name\": \"tools-o09qd6\"\n        },\n        \"description\": \"Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.\"\n      }\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Tools
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": false,
  "model": "command-r",
  "messages": [
    [
      "role": "user",
      "content": "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?"
    ]
  ],
  "tools": [
    [
      "type": "function",
      "function": [
        "name": "query_daily_sales_report",
        "parameters": [
          "type": "object",
          "properties": ["day": [
              "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
              "type": "str"
            ]],
          "required": ["day"],
          "x-fern-type-name": "tools-by6k68"
        ],
        "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day."
      ]
    ],
    [
      "type": "function",
      "function": [
        "name": "query_product_catalog",
        "parameters": [
          "type": "object",
          "properties": ["category": [
              "description": "Retrieves product information data for all products in this category.",
              "type": "str"
            ]],
          "required": ["category"],
          "x-fern-type-name": "tools-o09qd6"
        ],
        "description": "Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels."
      ]
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/chat")! as URL,
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

```typescript Images
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({});

(async () => {
  const response = await cohere.chat({
    model: 'command-a-vision-07-2025',
    messages: [
      {
        role: 'user',
        content: [
          { type: 'text', text: 'Describe this image' },
          {
            type: 'image_url',
            imageUrl: {
              // Can be either a base64 data URI or a web URL.
              url: 'https://cohere.com/favicon-32x32.png',
              detail: 'auto',
            },
          },
        ],
      },
    ],
  });
  console.log(response.message.content[0].text);
})();

```

```python Images
import cohere

co = cohere.ClientV2()

response = co.chat(
    model="command-a-vision-07-2025",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this image"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        # Can be either a base64 data URI or a web URL.
                        "url": "https://cohere.com/favicon-32x32.png",
                        "detail": "auto"
                    }
                }
            ]
        }
    ]
)

print(response)
```

```java Images
/* (C)2024 */
package chatv2post;

import java.util.List;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatRequest;
import com.cohere.api.types.ChatMessageV2;
import com.cohere.api.types.ChatResponse;
import com.cohere.api.types.Content;
import com.cohere.api.types.ImageContent;
import com.cohere.api.types.ImageUrl;
import com.cohere.api.types.TextContent;
import com.cohere.api.types.UserMessage;
import com.cohere.api.types.UserMessageContent;

public class Image {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ChatResponse response =
        cohere
            .v2()
            .chat(
                V2ChatRequest.builder()
                    .model("command-a-vision-07-2025")
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(
                                        UserMessageContent.of(
                                            List.of(
                                                Content.text(
                                                    TextContent.builder()
                                                        .text("Describe this image")
                                                        .build()),
                                                Content.imageUrl(
                                                    ImageContent.builder()
                                                        .imageUrl(
                                                            ImageUrl.builder()
                                                                // Can be either a base64 data URI or a web URL.
                                                                .url(
                                                                    "https://cohere.com/favicon-32x32.png")
                                                                .build())
                                                        .build()))))
                                    .build())))
                    .build());

    System.out.println(response);
  }
}

```

```go Images
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.Chat(
		context.TODO(),
		&cohere.V2ChatRequest{
			Model: "command-a-vision-07-2025",
			Messages: cohere.ChatMessages{
				{
					Role: "user",
					User: &cohere.UserMessageV2{
						Content: &cohere.UserMessageV2Content{
							ContentList: []*cohere.Content{
								{Type: "text", Text: &cohere.ChatTextContent{Text: "Describe this image"}},
								{Type: "image_url", ImageUrl: &cohere.ImageContent{
									ImageUrl: &cohere.ImageUrl{
										// Can be either a base64 data URI or a web URL.
										Url:    "https://cohere.com/favicon-32x32.png",
										Detail: cohere.ImageUrlDetailAuto.Ptr(),
									},
								}},
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```ruby Images
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stream\": false,\n  \"model\": \"command-a-vision-07-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": [\n        {\n          \"type\": \"text\",\n          \"text\": \"Describe this image\"\n        },\n        {\n          \"type\": \"image_url\",\n          \"image_url\": {\n            \"url\": \"https://cohere.com/favicon-32x32.png\",\n            \"detail\": \"auto\"\n          }\n        }\n      ]\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Images
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": false,
  "model": "command-a-vision-07-2025",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Describe this image"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://cohere.com/favicon-32x32.png",
            "detail": "auto"
          }
        }
      ]
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Images
var client = new RestClient("https://api.cohere.com/v2/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stream\": false,\n  \"model\": \"command-a-vision-07-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": [\n        {\n          \"type\": \"text\",\n          \"text\": \"Describe this image\"\n        },\n        {\n          \"type\": \"image_url\",\n          \"image_url\": {\n            \"url\": \"https://cohere.com/favicon-32x32.png\",\n            \"detail\": \"auto\"\n          }\n        }\n      ]\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Images
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": false,
  "model": "command-a-vision-07-2025",
  "messages": [
    [
      "role": "user",
      "content": [
        [
          "type": "text",
          "text": "Describe this image"
        ],
        [
          "type": "image_url",
          "image_url": [
            "url": "https://cohere.com/favicon-32x32.png",
            "detail": "auto"
          ]
        ]
      ]
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/chat")! as URL,
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

**Navigation:** [← Previous](./08-teams-and-roles-on-the-cohere-platform.md) | [Index](./index.md) | [Next →](./10-chat-with-streaming.md)
