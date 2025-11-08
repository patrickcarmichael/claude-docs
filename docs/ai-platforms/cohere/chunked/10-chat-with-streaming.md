**Navigation:** [← Previous](./09-chat.md) | [Index](./index.md) | [Next →](./11-embed-api-v2.md)

---

# Chat with Streaming

POST https://api.cohere.com/v2/chat
Content-Type: application/json

Generates a text response to a user message. To learn how to use the Chat API and RAG follow our [Text Generation guides](https://docs.cohere.com/v2/docs/chat-api).

Follow the [Migration Guide](https://docs.cohere.com/v2/docs/migrating-v1-to-v2) for instructions on moving from API v1 to API v2.


Reference: https://docs.cohere.com/reference/chat-stream

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Chat API (v2)
  version: endpoint_v2.chat_stream
paths:
  /v2/chat:
    post:
      operationId: chat-stream
      summary: Chat API (v2)
      description: >
        Generates a text response to a user message. To learn how to use the
        Chat API and RAG follow our [Text Generation
        guides](https://docs.cohere.com/v2/docs/chat-api).


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
          description: >
            Generates a text response to a user message. To learn how to use the
            Chat API and RAG follow our [Text Generation
            guides](https://docs.cohere.com/v2/docs/chat-api).


            Follow the [Migration
            Guide](https://docs.cohere.com/v2/docs/migrating-v1-to-v2) for
            instructions on moving from API v1 to API v2.
          content:
            text/event-stream:
              schema:
                $ref: '#/components/schemas/v2_chat_Response_stream_streaming'
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
                      value: true
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
    ChatStreamEventTypeType:
      type: string
      enum:
        - value: message-start
        - value: content-start
        - value: content-delta
        - value: content-end
        - value: tool-call-start
        - value: tool-call-delta
        - value: tool-call-end
        - value: tool-plan-delta
        - value: citation-start
        - value: citation-end
        - value: message-end
    ChatMessageStartEventDeltaMessageRole:
      type: string
      enum:
        - value: assistant
    ChatMessageStartEventDeltaMessage:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/ChatMessageStartEventDeltaMessageRole'
    ChatMessageStartEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/ChatMessageStartEventDeltaMessage'
    ChatContentStartEventDeltaMessageContentType:
      type: string
      enum:
        - value: text
        - value: thinking
    ChatContentStartEventDeltaMessageContent:
      type: object
      properties:
        thinking:
          type: string
        text:
          type: string
        type:
          $ref: '#/components/schemas/ChatContentStartEventDeltaMessageContentType'
    ChatContentStartEventDeltaMessage:
      type: object
      properties:
        content:
          $ref: '#/components/schemas/ChatContentStartEventDeltaMessageContent'
    ChatContentStartEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/ChatContentStartEventDeltaMessage'
    ChatContentDeltaEventDeltaMessageContent:
      type: object
      properties:
        thinking:
          type: string
        text:
          type: string
    ChatContentDeltaEventDeltaMessage:
      type: object
      properties:
        content:
          $ref: '#/components/schemas/ChatContentDeltaEventDeltaMessageContent'
    ChatContentDeltaEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/ChatContentDeltaEventDeltaMessage'
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
    ChatToolPlanDeltaEventDeltaMessage:
      type: object
      properties:
        tool_plan:
          type: string
    ChatToolPlanDeltaEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/ChatToolPlanDeltaEventDeltaMessage'
    ChatToolCallStartEventDeltaMessage:
      type: object
      properties:
        tool_calls:
          $ref: '#/components/schemas/ToolCallV2'
    ChatToolCallStartEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/ChatToolCallStartEventDeltaMessage'
    ChatToolCallDeltaEventDeltaMessageToolCallsFunction:
      type: object
      properties:
        arguments:
          type: string
    ChatToolCallDeltaEventDeltaMessageToolCalls:
      type: object
      properties:
        function:
          $ref: >-
            #/components/schemas/ChatToolCallDeltaEventDeltaMessageToolCallsFunction
    ChatToolCallDeltaEventDeltaMessage:
      type: object
      properties:
        tool_calls:
          $ref: '#/components/schemas/ChatToolCallDeltaEventDeltaMessageToolCalls'
    ChatToolCallDeltaEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/ChatToolCallDeltaEventDeltaMessage'
    CitationStartEventDeltaMessage:
      type: object
      properties:
        citations:
          $ref: '#/components/schemas/Citation'
    CitationStartEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/CitationStartEventDeltaMessage'
    ChatFinishReason:
      type: string
      enum:
        - value: COMPLETE
        - value: STOP_SEQUENCE
        - value: MAX_TOKENS
        - value: TOOL_CALL
        - value: ERROR
        - value: TIMEOUT
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
    ChatMessageEndEventDelta:
      type: object
      properties:
        error:
          type: string
        finish_reason:
          $ref: '#/components/schemas/ChatFinishReason'
        usage:
          $ref: '#/components/schemas/Usage'
    ChatStreamEventEventType:
      type: string
      enum:
        - value: stream-start
        - value: search-queries-generation
        - value: search-results
        - value: text-generation
        - value: citation-generation
        - value: stream-end
        - value: debug
    v2_chat_Response_stream_streaming:
      oneOf:
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            id:
              type: string
            delta:
              $ref: '#/components/schemas/ChatMessageStartEventDelta'
          required:
            - type
          description: message-start variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
            delta:
              $ref: '#/components/schemas/ChatContentStartEventDelta'
          required:
            - type
          description: content-start variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
            delta:
              $ref: '#/components/schemas/ChatContentDeltaEventDelta'
            logprobs:
              $ref: '#/components/schemas/LogprobItem'
          required:
            - type
          description: content-delta variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
          required:
            - type
          description: content-end variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            delta:
              $ref: '#/components/schemas/ChatToolPlanDeltaEventDelta'
          required:
            - type
          description: tool-plan-delta variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
            delta:
              $ref: '#/components/schemas/ChatToolCallStartEventDelta'
          required:
            - type
          description: tool-call-start variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
            delta:
              $ref: '#/components/schemas/ChatToolCallDeltaEventDelta'
          required:
            - type
          description: tool-call-delta variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
          required:
            - type
          description: tool-call-end variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
            delta:
              $ref: '#/components/schemas/CitationStartEventDelta'
          required:
            - type
          description: citation-start variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
          required:
            - type
          description: citation-end variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            id:
              type: string
            delta:
              $ref: '#/components/schemas/ChatMessageEndEventDelta'
          required:
            - type
          description: message-end variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - debug
              description: 'Discriminator value: debug'
            event_type:
              $ref: '#/components/schemas/ChatStreamEventEventType'
            prompt:
              type: string
          required:
            - type
            - event_type
          description: debug variant
      discriminator:
        propertyName: type

```

## SDK Code Examples

```typescript Default
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({});

(async () => {
  const stream = await cohere.chatStream({
    model: 'command-a-03-2025',
    messages: [
      {
        role: 'user',
        content: 'Tell me about LLMs',
      },
    ],
  });

  for await (const chatEvent of stream) {
    if (chatEvent.type === 'content-delta') {
      console.log(chatEvent.delta?.message);
    }
  }
})();

```

```python Default
import cohere

co = cohere.ClientV2()

response = co.chat_stream(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": "Tell me about LLMs"}],
)

for event in response:
    if event.type == "content-delta":
        print(event.delta.message.content.text, end="")

```

```java Default
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatStreamRequest;
import com.cohere.api.types.*;
import java.util.List;

public class Stream {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    Iterable<StreamedChatResponseV2> response =
        cohere
            .v2()
            .chatStream(
                V2ChatStreamRequest.builder()
                    .model("command-a-03-2025")
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(UserMessageContent.of("Tell me about LLMs"))
                                    .build())))
                    .build());

    for (StreamedChatResponseV2 chatResponse : response) {
      if (chatResponse.isContentDelta()) {
        System.out.println(
            chatResponse
                .getContentDelta()
                .flatMap(ChatContentDeltaEvent::getDelta)
                .flatMap(ChatContentDeltaEventDelta::getMessage)
                .flatMap(ChatContentDeltaEventDeltaMessage::getContent)
                .flatMap(ChatContentDeltaEventDeltaMessageContent::getText)
                .orElse(""));
      }
    }

    System.out.println(response);
  }
}

```

```go Default
package main

import (
	"context"
	"errors"
	"io"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.ChatStream(
		context.TODO(),
		&cohere.V2ChatStreamRequest{
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

	// Make sure to close the stream when you're done reading.
	// This is easily handled with defer.
	defer resp.Close()

	for {
		message, err := resp.Recv()

		if errors.Is(err, io.EOF) {
			// An io.EOF error means the server is done sending messages
			// and should be treated as a success.
			break
		}

		if message.ContentDelta != nil {
			log.Printf("%+v", message)
		}
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
request.body = "{\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Tell me about LLMs\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Default
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": true,
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
request.AddParameter("application/json", "{\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Tell me about LLMs\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Default
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": true,
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
  const stream = await cohere.chatStream({
    model: 'command-a-03-2025',
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
    messages: [
      {
        role: 'user',
        content: 'Who is more popular: Nsync or Backstreet Boys?',
      },
    ],
  });

  for await (const chatEvent of stream) {
    console.log(chatEvent);
  }
})();

```

```python Documents
import cohere

co = cohere.ClientV2()

response = co.chat_stream(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": "Who is more popular: Nsync or Backstreet Boys?"}],
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
                "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven't study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn't a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
            }
        },
        {
            "data":  {
                "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
                "snippet": " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women's – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
            }
        },
        {
            "data":  {
                "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
                "snippet": " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I'll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC's albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
            }
        }
    ],
)

for event in response:
    if event.type == "message-start":
        print("\nMessage started.")
    elif event.type == "message-end":
        print("\nMessage ended.")
    elif event.type == "content-delta":
        print(event.delta.message.content.text, end="")


```

```java Documents
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatStreamRequest;
import com.cohere.api.resources.v2.types.V2ChatStreamRequestDocumentsItem;
import com.cohere.api.types.*;
import java.util.List;

public class StreamDocuments {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    Iterable<StreamedChatResponseV2> response =
        cohere
            .v2()
            .chatStream(
                V2ChatStreamRequest.builder()
                    .model("command-a-03-2025")
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(UserMessageContent.of("Who is the most popular?"))
                                    .build())))
                    .documents(
                        List.of(
                            V2ChatStreamRequestDocumentsItem.of(
                                "↓ Skip to Main Content\n\n"
                                    + "Music industry – One step closer to being accurate\n\n"
                                    + "CSPC: Backstreet Boys Popularity Analysis\n\n"
                                    + "At one point, Backstreet Boys defined success: massive album"
                                    + " sales..."),
                            V2ChatStreamRequestDocumentsItem.of(
                                "↓ Skip to Main Content\n\n"
                                    + "CSPC: NSYNC Popularity Analysis\n\n"
                                    + "At the turn of the millennium, three teen acts were huge:"
                                    + " Backstreet Boys, Britney Spears, and NSYNC..."),
                            V2ChatStreamRequestDocumentsItem.of(
                                "Yet the way many music consumers embraced Backstreet Boys deserves"
                                    + " its own chapter..."),
                            V2ChatStreamRequestDocumentsItem.of(
                                "Was NSYNC only successful in the US, or were they a global"
                                    + " phenomenon?...")))
                    .build());

    for (StreamedChatResponseV2 chatResponse : response) {
      if (chatResponse.isContentDelta()) {
        String text =
            chatResponse
                .getContentDelta()
                .flatMap(ChatContentDeltaEvent::getDelta)
                .flatMap(ChatContentDeltaEventDelta::getMessage)
                .flatMap(ChatContentDeltaEventDeltaMessage::getContent)
                .flatMap(ChatContentDeltaEventDeltaMessageContent::getText)
                .orElse("");
        System.out.println(text);
      }
    }
  }
}

```

```go Documents
package main

import (
	"context"
	"errors"
	"io"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.ChatStream(
		context.TODO(),
		&cohere.V2ChatStreamRequest{
			Model: "command-a-03-2025",
			Documents: []*cohere.V2ChatStreamRequestDocumentsItem{
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
		},
	)

	if err != nil {
		log.Fatal(err)
	}
	defer resp.Close()

	for {
		message, err := resp.Recv()

		if errors.Is(err, io.EOF) {
			// An io.EOF error means the server is done sending messages
			// and should be treated as a success.
			break
		}

		// Log the received message
		if message.ContentDelta != nil {
			log.Printf("%+v", message)
		}
	}
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
request.body = "{\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Who is more popular: Nsync or Backstreet Boys?\"\n    }\n  ],\n  \"documents\": [\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.\"\n      }\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Documents
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": true,
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
request.AddParameter("application/json", "{\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Who is more popular: Nsync or Backstreet Boys?\"\n    }\n  ],\n  \"documents\": [\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.\"\n      }\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Documents
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": true,
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
  const stream = await cohere.chatStream({
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

  for await (const chatEvent of stream) {
    if (chatEvent.type === 'tool-call-delta') {
      console.log(chatEvent.delta?.message);
    }
  }
})();

```

```python Tools
import cohere

co = cohere.ClientV2()

response = co.chat_stream(
    model="command-a-03-2025",
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

for event in response:
    if event.type in ["tool-call-start", "tool-call-delta"]:
        for tool_call in event.delta.message.tool_calls:
            print(tool_call)

```

```java Tools
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatStreamRequest;
import com.cohere.api.types.*;
import java.util.List;
import java.util.Map;

public class StreamTools {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    Iterable<StreamedChatResponseV2> response =
        cohere
            .v2()
            .chatStream(
                V2ChatStreamRequest.builder()
                    .model("command-a-03-2025")
                    .tools(
                        List.of(
                            ToolV2.builder()
                                .function(
                                    ToolV2Function.builder()
                                        .name("query_daily_sales_report")
                                        .description(
                                            "Connects to a database to retrieve overall sales"
                                                + " volumes and sales information for a given day.")
                                        .parameters(
                                            Map.of(
                                                "day",
                                                ToolParameterDefinitionsValue.builder()
                                                    .type("str")
                                                    .description(
                                                        "Retrieves sales data for this day,"
                                                            + " formatted as YYYY-MM-DD.")
                                                    .required(true)
                                                    .build()))
                                        .build())
                                .build(),
                            ToolV2.builder()
                                .function(
                                    ToolV2Function.builder()
                                        .name("query_product_catalog")
                                        .description(
                                            "Connects to a product catalog with information about"
                                                + " all the products being sold, including"
                                                + " categories, prices, and stock levels.")
                                        .parameters(
                                            Map.of(
                                                "category",
                                                ToolParameterDefinitionsValue.builder()
                                                    .type("str")
                                                    .description(
                                                        "Retrieves product information data for all"
                                                            + " products in this category.")
                                                    .required(true)
                                                    .build()))
                                        .build())
                                .build()))
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(
                                        UserMessageContent.of(
                                            "Can you provide a sales summary for 29th September"
                                                + " 2023, and also give me some details about the"
                                                + " products in the 'Electronics' category?"))
                                    .build())))
                    .build());

    for (StreamedChatResponseV2 chatResponse : response) {
      if (chatResponse.isContentDelta()) {
        String text =
            chatResponse
                .getContentDelta()
                .flatMap(ChatContentDeltaEvent::getDelta)
                .flatMap(ChatContentDeltaEventDelta::getMessage)
                .flatMap(ChatContentDeltaEventDeltaMessage::getContent)
                .flatMap(ChatContentDeltaEventDeltaMessageContent::getText)
                .orElse("");
        System.out.println(text);
      }
    }
  }
}

```

```go Tools
package main

import (
	"context"
	"errors"
	"io"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.ChatStream(
		context.TODO(),
		&cohere.V2ChatStreamRequest{
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

	// Make sure to close the stream when you're done reading.
	// This is easily handled with defer.
	defer resp.Close()

	for {
		message, err := resp.Recv()

		if errors.Is(err, io.EOF) {
			// An io.EOF error means the server is done sending messages
			// and should be treated as a success.
			break
		}

		// Log the received message
		if message.ToolCallDelta != nil {
			log.Printf("%+v", message)
		}
	}
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
request.body = "{\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_daily_sales_report\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"day\": {\n              \"description\": \"Retrieves sales data for this day, formatted as YYYY-MM-DD.\",\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"description\": \"Connects to a database to retrieve overall sales volumes and sales information for a given day.\"\n      }\n    },\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_product_catalog\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"category\": {\n              \"description\": \"Retrieves product information data for all products in this category.\",\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"description\": \"Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels.\"\n      }\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Tools
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": true,
  "model": "command-a-03-2025",
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
              "type": "string"
            }
          }
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
              "type": "string"
            }
          }
        },
        "description": "Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels."
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
request.AddParameter("application/json", "{\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_daily_sales_report\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"day\": {\n              \"description\": \"Retrieves sales data for this day, formatted as YYYY-MM-DD.\",\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"description\": \"Connects to a database to retrieve overall sales volumes and sales information for a given day.\"\n      }\n    },\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_product_catalog\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"category\": {\n              \"description\": \"Retrieves product information data for all products in this category.\",\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"description\": \"Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels.\"\n      }\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Tools
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": true,
  "model": "command-a-03-2025",
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
              "type": "string"
            ]]
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
              "type": "string"
            ]]
        ],
        "description": "Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels."
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
  const stream = await cohere.chatStream({
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

  for await (const chatEvent of stream) {
    if (chatEvent.type === 'content-delta') {
      console.log(chatEvent.delta?.message);
    }
  }
})();

```

```python Images
import cohere

co = cohere.ClientV2()

response = co.chat_stream(
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

for event in response:
    if event.type == "content-delta":
        print(event.delta.message.content.text, end="")
```

```java Images
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatStreamRequest;
import com.cohere.api.types.*;
import java.util.List;

public class Stream {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    Iterable<StreamedChatResponseV2> response =
        cohere
            .v2()
            .chatStream(
                V2ChatStreamRequest.builder()
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

    for (StreamedChatResponseV2 chatResponse : response) {
      if (chatResponse.isContentDelta()) {
        System.out.println(
            chatResponse
                .getContentDelta()
                .flatMap(ChatContentDeltaEvent::getDelta)
                .flatMap(ChatContentDeltaEventDelta::getMessage)
                .flatMap(ChatContentDeltaEventDeltaMessage::getContent)
                .flatMap(ChatContentDeltaEventDeltaMessageContent::getText)
                .orElse(""));
      }
    }

    System.out.println(response);
  }
}

```

```go Images
package main

import (
	"context"
	"errors"
	"io"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.ChatStream(
		context.TODO(),
		&cohere.V2ChatStreamRequest{
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

	// Make sure to close the stream when you're done reading.
	// This is easily handled with defer.
	defer resp.Close()

	for {
		message, err := resp.Recv()

		if errors.Is(err, io.EOF) {
			// An io.EOF error means the server is done sending messages
			// and should be treated as a success.
			break
		}

		if message.ContentDelta != nil {
			log.Printf("%+v", message)
		}
	}
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
request.body = "{\n  \"stream\": true,\n  \"model\": \"command-a-vision-07-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": [\n        {\n          \"type\": \"text\",\n          \"text\": \"Describe this image\"\n        },\n        {\n          \"type\": \"image_url\",\n          \"image_url\": {\n            \"url\": \"https://cohere.com/favicon-32x32.png\",\n            \"detail\": \"auto\"\n          }\n        }\n      ]\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Images
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": true,
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
request.AddParameter("application/json", "{\n  \"stream\": true,\n  \"model\": \"command-a-vision-07-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": [\n        {\n          \"type\": \"text\",\n          \"text\": \"Describe this image\"\n        },\n        {\n          \"type\": \"image_url\",\n          \"image_url\": {\n            \"url\": \"https://cohere.com/favicon-32x32.png\",\n            \"detail\": \"auto\"\n          }\n        }\n      ]\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Images
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": true,
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

# Rerank API (v2)

POST https://api.cohere.com/v2/rerank
Content-Type: application/json

This endpoint takes in a query and a list of texts and produces an ordered array with each text assigned a relevance score.

Reference: https://docs.cohere.com/reference/rerank

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Rerank API (v2)
  version: endpoint_v2.rerank
paths:
  /v2/rerank:
    post:
      operationId: rerank
      summary: Rerank API (v2)
      description: >-
        This endpoint takes in a query and a list of texts and produces an
        ordered array with each text assigned a relevance score.
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
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/v2_rerank_Response_200'
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
        description: ''
        content:
          application/json:
            schema:
              type: object
              properties:
                model:
                  type: string
                query:
                  type: string
                documents:
                  type: array
                  items:
                    type: string
                top_n:
                  type: integer
                max_tokens_per_doc:
                  type: integer
                priority:
                  type: integer
              required:
                - model
                - query
                - documents
components:
  schemas:
    V2RerankPostResponsesContentApplicationJsonSchemaResultsItems:
      type: object
      properties:
        index:
          type: integer
        relevance_score:
          type: number
          format: double
      required:
        - index
        - relevance_score
    ApiMetaApiVersion:
      type: object
      properties:
        version:
          type: string
        is_deprecated:
          type: boolean
        is_experimental:
          type: boolean
      required:
        - version
    ApiMetaBilledUnits:
      type: object
      properties:
        images:
          type: number
          format: double
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
    ApiMetaTokens:
      type: object
      properties:
        input_tokens:
          type: number
          format: double
        output_tokens:
          type: number
          format: double
    ApiMeta:
      type: object
      properties:
        api_version:
          $ref: '#/components/schemas/ApiMetaApiVersion'
        billed_units:
          $ref: '#/components/schemas/ApiMetaBilledUnits'
        tokens:
          $ref: '#/components/schemas/ApiMetaTokens'
        cached_tokens:
          type: number
          format: double
        warnings:
          type: array
          items:
            type: string
    v2_rerank_Response_200:
      type: object
      properties:
        id:
          type: string
        results:
          type: array
          items:
            $ref: >-
              #/components/schemas/V2RerankPostResponsesContentApplicationJsonSchemaResultsItems
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - results

```

## SDK Code Examples

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const rerank = await cohere.v2.rerank({
    documents: [
      'Carson City is the capital city of the American state of Nevada.',
      'The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.',
      'Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.',
      'Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.',
      'Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.',
    ],
    query: 'What is the capital of the United States?',
    topN: 3,
    model: 'rerank-v3.5',
  });

  console.log(rerank);
})();

```

```python Sync
import cohere

co = cohere.ClientV2()

docs = [
    "Carson City is the capital city of the American state of Nevada.",
    "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
    "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
    "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
    "Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
]

response = co.rerank(
    model="rerank-v3.5",
    query="What is the capital of the United States?",
    documents=docs,
    top_n=3,
)
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClientV2()

async def main():
    response = await co.rerank(
        model="rerank-v3.5",
        query="What is the capital of the United States?",
        documents=[
            "Carson City is the capital city of the American state of Nevada.",
            "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
            "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
            "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
            "Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
        ],
        top_n=3
    )
    print(response)


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2RerankRequest;
import com.cohere.api.resources.v2.types.V2RerankResponse;
import java.util.List;

public class RerankV2Post {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    V2RerankResponse response =
        cohere
            .v2()
            .rerank(
                V2RerankRequest.builder()
                    .model("rerank-v3.5")
                    .query("What is the capital of the United States?")
                    .documents(
                        List.of(
                            "Carson City is the capital city of the American state of Nevada.",
                            "The Commonwealth of the Northern Mariana Islands is a group of islands"
                                + " in the Pacific Ocean. Its capital is Saipan.",
                            "Capitalization or capitalisation in English grammar is the use of a"
                                + " capital letter at the start of a word. English usage varies"
                                + " from capitalization in other languages.",
                            "Washington, D.C. (also known as simply Washington or D.C., and"
                                + " officially as the District of Columbia) is the capital of the"
                                + " United States. It is a federal district.",
                            "Capital punishment has existed in the United States since before the"
                                + " United States was a country. As of 2017, capital punishment is"
                                + " legal in 30 of the 50 states."))
                    .topN(3)
                    .build());

    System.out.println(response);
  }
}

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

	url := "https://api.cohere.com/v2/rerank"

	payload := strings.NewReader("{\n  \"model\": \"rerank-v3.5\",\n  \"query\": \"What is the capital of the United States?\",\n  \"documents\": [\n    \"Carson City is the capital city of the American state of Nevada.\",\n    \"The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.\",\n    \"Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.\",\n    \"Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.\",\n    \"Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.\"\n  ],\n  \"top_n\": 3\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
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

url = URI("https://api.cohere.com/v2/rerank")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model\": \"rerank-v3.5\",\n  \"query\": \"What is the capital of the United States?\",\n  \"documents\": [\n    \"Carson City is the capital city of the American state of Nevada.\",\n    \"The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.\",\n    \"Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.\",\n    \"Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.\",\n    \"Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.\"\n  ],\n  \"top_n\": 3\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/rerank', [
  'body' => '{
  "model": "rerank-v3.5",
  "query": "What is the capital of the United States?",
  "documents": [
    "Carson City is the capital city of the American state of Nevada.",
    "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
    "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
    "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
    "Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states."
  ],
  "top_n": 3
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v2/rerank");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model\": \"rerank-v3.5\",\n  \"query\": \"What is the capital of the United States?\",\n  \"documents\": [\n    \"Carson City is the capital city of the American state of Nevada.\",\n    \"The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.\",\n    \"Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.\",\n    \"Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.\",\n    \"Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.\"\n  ],\n  \"top_n\": 3\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "model": "rerank-v3.5",
  "query": "What is the capital of the United States?",
  "documents": ["Carson City is the capital city of the American state of Nevada.", "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.", "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.", "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.", "Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states."],
  "top_n": 3
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/rerank")! as URL,
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

**Navigation:** [← Previous](./09-chat.md) | [Index](./index.md) | [Next →](./11-embed-api-v2.md)
