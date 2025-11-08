---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create a completion
  version: endpoint_completions.createCompletions
paths:
  /completions:
    post:
      operationId: create-completions
      summary: Create a completion
      description: >-
        Creates a completion for the provided prompt and parameters. Supports
        both streaming and non-streaming modes.
      tags:
        - - subpackage_completions
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful completion response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CompletionResponse'
        '400':
          description: Bad request - invalid parameters
          content: {}
        '401':
          description: Unauthorized - invalid API key
          content: {}
        '429':
          description: Too many requests - rate limit exceeded
          content: {}
        '500':
          description: Internal server error
          content: {}
      requestBody:
        description: Completion request parameters
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CompletionCreateParams'
components:
  schemas:
    ModelName:
      type: string
    CompletionCreateParamsPrompt:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
        - type: array
          items:
            type: number
            format: double
        - type: array
          items:
            type: array
            items:
              type: number
              format: double
    CompletionCreateParamsStop:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
    CompletionCreateParamsStreamOptions:
      type: object
      properties:
        include_usage:
          type:
            - boolean
            - 'null'
    CompletionCreateParamsResponseFormat0:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: text
      required:
        - type
    CompletionCreateParamsResponseFormat1:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: json_object
      required:
        - type
    JSONSchemaConfig:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        schema:
          type: object
          additionalProperties:
            description: Any type
        strict:
          type:
            - boolean
            - 'null'
      required:
        - name
    ResponseFormatJSONSchema:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: json_schema
        json_schema:
          $ref: '#/components/schemas/JSONSchemaConfig'
      required:
        - type
        - json_schema
    ResponseFormatTextGrammar:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: grammar
        grammar:
          type: string
      required:
        - type
        - grammar
    CompletionCreateParamsResponseFormat4:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: python
      required:
        - type
    CompletionCreateParamsResponseFormat:
      oneOf:
        - $ref: '#/components/schemas/CompletionCreateParamsResponseFormat0'
        - $ref: '#/components/schemas/CompletionCreateParamsResponseFormat1'
        - $ref: '#/components/schemas/ResponseFormatJSONSchema'
        - $ref: '#/components/schemas/ResponseFormatTextGrammar'
        - $ref: '#/components/schemas/CompletionCreateParamsResponseFormat4'
    CompletionCreateParams:
      type: object
      properties:
        model:
          $ref: '#/components/schemas/ModelName'
        models:
          type: array
          items:
            $ref: '#/components/schemas/ModelName'
        prompt:
          $ref: '#/components/schemas/CompletionCreateParamsPrompt'
        best_of:
          type:
            - integer
            - 'null'
        echo:
          type:
            - boolean
            - 'null'
        frequency_penalty:
          type:
            - number
            - 'null'
          format: double
        logit_bias:
          type:
            - object
            - 'null'
          additionalProperties:
            type: number
            format: double
        logprobs:
          type:
            - integer
            - 'null'
        max_tokens:
          type:
            - integer
            - 'null'
        'n':
          type:
            - integer
            - 'null'
        presence_penalty:
          type:
            - number
            - 'null'
          format: double
        seed:
          type:
            - integer
            - 'null'
        stop:
          oneOf:
            - $ref: '#/components/schemas/CompletionCreateParamsStop'
            - type: 'null'
        stream:
          type: boolean
        stream_options:
          oneOf:
            - $ref: '#/components/schemas/CompletionCreateParamsStreamOptions'
            - type: 'null'
        suffix:
          type:
            - string
            - 'null'
        temperature:
          type:
            - number
            - 'null'
          format: double
        top_p:
          type:
            - number
            - 'null'
          format: double
        user:
          type: string
        metadata:
          type:
            - object
            - 'null'
          additionalProperties:
            type: string
        response_format:
          oneOf:
            - $ref: '#/components/schemas/CompletionCreateParamsResponseFormat'
            - type: 'null'
      required:
        - prompt
    CompletionLogprobs:
      type: object
      properties:
        tokens:
          type: array
          items:
            type: string
        token_logprobs:
          type: array
          items:
            type: number
            format: double
        top_logprobs:
          type:
            - array
            - 'null'
          items:
            type: object
            additionalProperties:
              type: number
              format: double
        text_offset:
          type: array
          items:
            type: number
            format: double
      required:
        - tokens
        - token_logprobs
        - top_logprobs
        - text_offset
    CompletionFinishReason:
      type: string
      enum:
        - value: stop
        - value: length
        - value: content_filter
    CompletionChoice:
      type: object
      properties:
        text:
          type: string
        index:
          type: number
          format: double
        logprobs:
          oneOf:
            - $ref: '#/components/schemas/CompletionLogprobs'
            - type: 'null'
        finish_reason:
          $ref: '#/components/schemas/CompletionFinishReason'
      required:
        - text
        - index
        - logprobs
        - finish_reason
    CompletionUsage:
      type: object
      properties:
        prompt_tokens:
          type: number
          format: double
        completion_tokens:
          type: number
          format: double
        total_tokens:
          type: number
          format: double
      required:
        - prompt_tokens
        - completion_tokens
        - total_tokens
    CompletionResponse:
      type: object
      properties:
        id:
          type: string
        object:
          type: string
          enum:
            - type: stringLiteral
              value: text_completion
        created:
          type: number
          format: double
        model:
          type: string
        system_fingerprint:
          type: string
        choices:
          type: array
          items:
            $ref: '#/components/schemas/CompletionChoice'
        usage:
          $ref: '#/components/schemas/CompletionUsage'
      required:
        - id
        - object
        - created
        - model
        - choices
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
