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
  title: Create a new API key
  version: endpoint_apiKeys.createKeys
paths:
  /keys:
    post:
      operationId: create-keys
      summary: Create a new API key
      tags:
        - - subpackage_apiKeys
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '201':
          description: API key created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/API Keys_createKeys_Response_201'
        '400':
          description: Bad Request - Invalid request parameters
          content: {}
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                limit:
                  type:
                    - number
                    - 'null'
                  format: double
                limit_reset:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/KeysPostRequestBodyContentApplicationJsonSchemaLimitReset
                    - type: 'null'
                include_byok_in_limit:
                  type: boolean
              required:
                - name
components:
  schemas:
    KeysPostRequestBodyContentApplicationJsonSchemaLimitReset:
      type: string
      enum:
        - value: daily
        - value: weekly
        - value: monthly
    KeysPostResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        hash:
          type: string
        name:
          type: string
        label:
          type: string
        disabled:
          type: boolean
        limit:
          type:
            - number
            - 'null'
          format: double
        limit_remaining:
          type:
            - number
            - 'null'
          format: double
        limit_reset:
          type:
            - string
            - 'null'
        include_byok_in_limit:
          type: boolean
        usage:
          type: number
          format: double
        usage_daily:
          type: number
          format: double
        usage_weekly:
          type: number
          format: double
        usage_monthly:
          type: number
          format: double
        byok_usage:
          type: number
          format: double
        byok_usage_daily:
          type: number
          format: double
        byok_usage_weekly:
          type: number
          format: double
        byok_usage_monthly:
          type: number
          format: double
        created_at:
          type: string
        updated_at:
          type:
            - string
            - 'null'
      required:
        - hash
        - name
        - label
        - disabled
        - limit
        - limit_remaining
        - limit_reset
        - include_byok_in_limit
        - usage
        - usage_daily
        - usage_weekly
        - usage_monthly
        - byok_usage
        - byok_usage_daily
        - byok_usage_weekly
        - byok_usage_monthly
        - created_at
        - updated_at
    API Keys_createKeys_Response_201:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/KeysPostResponsesContentApplicationJsonSchemaData
        key:
          type: string
      required:
        - data
        - key
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
