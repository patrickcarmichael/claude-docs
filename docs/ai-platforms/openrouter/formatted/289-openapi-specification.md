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
  title: Get current API key
  version: endpoint_apiKeys.getCurrentKey
paths:
  /key:
    get:
      operationId: get-current-key
      summary: Get current API key
      description: >-
        Get information on the API key associated with the current
        authentication session
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
        '200':
          description: API key details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/API Keys_getCurrentKey_Response_200'
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    KeyGetResponsesContentApplicationJsonSchemaDataRateLimit:
      type: object
      properties:
        requests:
          type: number
          format: double
        interval:
          type: string
        note:
          type: string
      required:
        - requests
        - interval
        - note
    KeyGetResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        label:
          type: string
        limit:
          type:
            - number
            - 'null'
          format: double
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
        is_free_tier:
          type: boolean
        is_provisioning_key:
          type: boolean
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
        rate_limit:
          $ref: >-
            #/components/schemas/KeyGetResponsesContentApplicationJsonSchemaDataRateLimit
      required:
        - label
        - limit
        - usage
        - usage_daily
        - usage_weekly
        - usage_monthly
        - byok_usage
        - byok_usage_daily
        - byok_usage_weekly
        - byok_usage_monthly
        - is_free_tier
        - is_provisioning_key
        - limit_remaining
        - limit_reset
        - include_byok_in_limit
        - rate_limit
    API Keys_getCurrentKey_Response_200:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/KeyGetResponsesContentApplicationJsonSchemaData'
      required:
        - data
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
