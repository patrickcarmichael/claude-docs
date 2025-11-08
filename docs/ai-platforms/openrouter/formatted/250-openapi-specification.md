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
  title: Get total count of available models
  version: endpoint_models.listModelsCount
paths:
  /models/count:
    get:
      operationId: list-models-count
      summary: Get total count of available models
      tags:
        - - subpackage_models
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns the total count of available models
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelsCountResponse'
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    ModelsCountResponseData:
      type: object
      properties:
        count:
          type: number
          format: double
      required:
        - count
    ModelsCountResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/ModelsCountResponseData'
      required:
        - data
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
