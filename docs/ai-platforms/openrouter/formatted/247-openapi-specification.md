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
  title: Get request & usage metadata for a generation
  version: endpoint_generations.getGeneration
paths:
  /generation:
    get:
      operationId: get-generation
      summary: Get request & usage metadata for a generation
      tags:
        - - subpackage_generations
      parameters:
        - name: id
          in: query
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns the request metadata for this generation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Generations_getGeneration_Response_200'
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '402':
          description: Payment Required - Insufficient credits or quota to complete request
          content: {}
        '404':
          description: Not Found - Generation not found
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
        '502':
          description: Bad Gateway - Provider/upstream API failure
          content: {}
components:
  schemas:
    GenerationGetResponsesContentApplicationJsonSchemaDataApiType:
      type: string
      enum:
        - value: completions
        - value: embeddings
    GenerationGetResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
        upstream_id:
          type:
            - string
            - 'null'
        total_cost:
          type: number
          format: double
        cache_discount:
          type:
            - number
            - 'null'
          format: double
        upstream_inference_cost:
          type:
            - number
            - 'null'
          format: double
        created_at:
          type: string
        model:
          type: string
        app_id:
          type:
            - number
            - 'null'
          format: double
        streamed:
          type:
            - boolean
            - 'null'
        cancelled:
          type:
            - boolean
            - 'null'
        provider_name:
          type:
            - string
            - 'null'
        latency:
          type:
            - number
            - 'null'
          format: double
        moderation_latency:
          type:
            - number
            - 'null'
          format: double
        generation_time:
          type:
            - number
            - 'null'
          format: double
        finish_reason:
          type:
            - string
            - 'null'
        tokens_prompt:
          type:
            - number
            - 'null'
          format: double
        tokens_completion:
          type:
            - number
            - 'null'
          format: double
        native_tokens_prompt:
          type:
            - number
            - 'null'
          format: double
        native_tokens_completion:
          type:
            - number
            - 'null'
          format: double
        native_tokens_completion_images:
          type:
            - number
            - 'null'
          format: double
        native_tokens_reasoning:
          type:
            - number
            - 'null'
          format: double
        native_tokens_cached:
          type:
            - number
            - 'null'
          format: double
        num_media_prompt:
          type:
            - number
            - 'null'
          format: double
        num_input_audio_prompt:
          type:
            - number
            - 'null'
          format: double
        num_media_completion:
          type:
            - number
            - 'null'
          format: double
        num_search_results:
          type:
            - number
            - 'null'
          format: double
        origin:
          type: string
        usage:
          type: number
          format: double
        is_byok:
          type: boolean
        native_finish_reason:
          type:
            - string
            - 'null'
        external_user:
          type:
            - string
            - 'null'
        api_type:
          oneOf:
            - $ref: >-
                #/components/schemas/GenerationGetResponsesContentApplicationJsonSchemaDataApiType
            - type: 'null'
      required:
        - id
        - upstream_id
        - total_cost
        - cache_discount
        - upstream_inference_cost
        - created_at
        - model
        - app_id
        - streamed
        - cancelled
        - provider_name
        - latency
        - moderation_latency
        - generation_time
        - finish_reason
        - tokens_prompt
        - tokens_completion
        - native_tokens_prompt
        - native_tokens_completion
        - native_tokens_completion_images
        - native_tokens_reasoning
        - native_tokens_cached
        - num_media_prompt
        - num_input_audio_prompt
        - num_media_completion
        - num_search_results
        - origin
        - usage
        - is_byok
        - native_finish_reason
        - external_user
        - api_type
    Generations_getGeneration_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/GenerationGetResponsesContentApplicationJsonSchemaData
      required:
        - data
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
