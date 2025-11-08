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
  title: Create authorization code
  version: endpoint_oAuth.createAuthKeysCode
paths:
  /auth/keys/code:
    post:
      operationId: create-auth-keys-code
      summary: Create authorization code
      description: >-
        Create an authorization code for the PKCE flow to generate a
        user-controlled API key
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
          description: Successfully created authorization code
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OAuth_createAuthKeysCode_Response_200'
        '400':
          description: Bad Request - Invalid request parameters or malformed input
          content: {}
        '401':
          description: Unauthorized - Authentication required or invalid credentials
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
                callback_url:
                  type: string
                  format: uri
                code_challenge:
                  type: string
                code_challenge_method:
                  $ref: >-
                    #/components/schemas/AuthKeysCodePostRequestBodyContentApplicationJsonSchemaCodeChallengeMethod
                limit:
                  type: number
                  format: double
              required:
                - callback_url
components:
  schemas:
    AuthKeysCodePostRequestBodyContentApplicationJsonSchemaCodeChallengeMethod:
      type: string
      enum:
        - value: S256
        - value: plain
    AuthKeysCodePostResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
        app_id:
          type: number
          format: double
        created_at:
          type: string
      required:
        - id
        - app_id
        - created_at
    OAuth_createAuthKeysCode_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/AuthKeysCodePostResponsesContentApplicationJsonSchemaData
      required:
        - data
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
