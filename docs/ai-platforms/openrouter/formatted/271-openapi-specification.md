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
  title: List all providers
  version: endpoint_providers.listProviders
paths:
  /providers:
    get:
      operationId: list-providers
      summary: List all providers
      tags:
        - - subpackage_providers
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns a list of providers
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Providers_listProviders_Response_200'
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    ProvidersGetResponsesContentApplicationJsonSchemaDataItems:
      type: object
      properties:
        name:
          type: string
        slug:
          type: string
        privacy_policy_url:
          type:
            - string
            - 'null'
        terms_of_service_url:
          type:
            - string
            - 'null'
        status_page_url:
          type:
            - string
            - 'null'
      required:
        - name
        - slug
        - privacy_policy_url
    Providers_listProviders_Response_200:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: >-
              #/components/schemas/ProvidersGetResponsesContentApplicationJsonSchemaDataItems
      required:
        - data
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
