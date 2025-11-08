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
  title: Get remaining credits
  version: endpoint_credits.getCredits
paths:
  /credits:
    get:
      operationId: get-credits
      summary: Get remaining credits
      description: Get total credits purchased and used for the authenticated user
      tags:
        - - subpackage_credits
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns the total credits purchased and used
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Credits_getCredits_Response_200'
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '403':
          description: Forbidden - Only provisioning keys can fetch credits
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    Credits_getCredits_Response_200:
      type: object
      properties: {}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
