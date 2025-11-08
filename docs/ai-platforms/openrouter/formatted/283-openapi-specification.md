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
  title: Delete an API key
  version: endpoint_apiKeys.deleteKeys
paths:
  /keys/{hash}:
    delete:
      operationId: delete-keys
      summary: Delete an API key
      tags:
        - - subpackage_apiKeys
      parameters:
        - name: hash
          in: path
          description: The hash identifier of the API key to delete
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
          description: API key deleted successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/API Keys_deleteKeys_Response_200'
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '404':
          description: Not Found - API key does not exist
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    API Keys_deleteKeys_Response_200:
      type: object
      properties:
        deleted:
          type: string
          enum:
            - type: booleanLiteral
              value: true
      required:
        - deleted
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
