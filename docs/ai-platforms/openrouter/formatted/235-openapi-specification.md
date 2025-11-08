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
  title: Get user activity grouped by endpoint
  version: endpoint_analytics.getUserActivity
paths:
  /activity:
    get:
      operationId: get-user-activity
      summary: Get user activity grouped by endpoint
      description: >-
        Returns user activity data grouped by endpoint for the last 30
        (completed) UTC days
      tags:
        - - subpackage_analytics
      parameters:
        - name: date
          in: query
          description: Filter by a single UTC date in the last 30 days (YYYY-MM-DD format).
          required: false
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
          description: Returns user activity data grouped by endpoint
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Analytics_getUserActivity_Response_200'
        '400':
          description: Bad Request - Invalid date format or date range
          content: {}
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '403':
          description: Forbidden - Only provisioning keys can fetch activity
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    ActivityItem:
      type: object
      properties:
        date:
          type: string
        model:
          type: string
        model_permaslug:
          type: string
        endpoint_id:
          type: string
        provider_name:
          type: string
        usage:
          type: number
          format: double
        byok_usage_inference:
          type: number
          format: double
        requests:
          type: number
          format: double
        prompt_tokens:
          type: number
          format: double
        completion_tokens:
          type: number
          format: double
        reasoning_tokens:
          type: number
          format: double
      required:
        - date
        - model
        - model_permaslug
        - endpoint_id
        - provider_name
        - usage
        - byok_usage_inference
        - requests
        - prompt_tokens
        - completion_tokens
        - reasoning_tokens
    Analytics_getUserActivity_Response_200:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/ActivityItem'
      required:
        - data
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
