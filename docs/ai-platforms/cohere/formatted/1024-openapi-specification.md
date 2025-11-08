---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Deletes a fine-tuned model.
  version: endpoint_finetuning.DeleteFinetunedModel
paths:
  /v1/finetuning/finetuned-models/{id}:
    delete:
      operationId: delete-finetuned-model
      summary: Deletes a fine-tuned model.
      description: >-
        Deletes a fine-tuned model. The model will be removed from the system
        and will no longer be available for use.

        This operation is irreversible.
      tags:
        - - subpackage_finetuning
      parameters:
        - name: id
          in: path
          description: The fine-tuned model ID.
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteFinetunedModelResponse'
        '400':
          description: Bad Request
          content: {}
        '401':
          description: Unauthorized
          content: {}
        '403':
          description: Forbidden
          content: {}
        '404':
          description: Not Found
          content: {}
        '500':
          description: Internal Server Error
          content: {}
        '503':
          description: Status Service Unavailable
          content: {}
components:
  schemas:
    DeleteFinetunedModelResponse:
      type: object
      properties: {}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
