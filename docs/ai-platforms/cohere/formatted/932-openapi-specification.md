---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
