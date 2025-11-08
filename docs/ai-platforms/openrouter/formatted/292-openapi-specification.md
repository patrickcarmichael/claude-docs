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
  title: Exchange authorization code for API key
  version: endpoint_oAuth.exchangeAuthCodeForAPIKey
paths:
  /auth/keys:
    post:
      operationId: exchange-auth-code-for-api-key
      summary: Exchange authorization code for API key
      description: >-
        Exchange an authorization code from the PKCE flow for a user-controlled
        API key
      tags:
        - - subpackage_oAuth
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successfully exchanged code for an API key
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/OAuth_exchangeAuthCodeForAPIKey_Response_200
        '400':
          description: Bad Request - Invalid request parameters or malformed input
          content: {}
        '403':
          description: Forbidden - Authentication successful but insufficient permissions
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                code:
                  type: string
                code_verifier:
                  type: string
                code_challenge_method:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/AuthKeysPostRequestBodyContentApplicationJsonSchemaCodeChallengeMethod
                    - type: 'null'
              required:
                - code
components:
  schemas:
    AuthKeysPostRequestBodyContentApplicationJsonSchemaCodeChallengeMethod:
      type: string
      enum:
        - value: S256
        - value: plain
    OAuth_exchangeAuthCodeForAPIKey_Response_200:
      type: object
      properties:
        key:
          type: string
        user_id:
          type:
            - string
            - 'null'
      required:
        - key
        - user_id
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
