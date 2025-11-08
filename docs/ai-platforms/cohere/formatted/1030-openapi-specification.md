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
  title: Retrieve training metrics for fine-tuned models.
  version: endpoint_finetuning.ListTrainingStepMetrics
paths:
  /v1/finetuning/finetuned-models/{finetuned_model_id}/training-step-metrics:
    get:
      operationId: list-training-step-metrics
      summary: Retrieve training metrics for fine-tuned models.
      description: >-
        Returns a list of metrics measured during the training of a fine-tuned
        model.

        The metrics are ordered by step number, with the most recent step first.

        The list can be paginated using `page_size` and `page_token` parameters.
      tags:
        - - subpackage_finetuning
      parameters:
        - name: finetuned_model_id
          in: path
          description: The parent fine-tuned model ID.
          required: true
          schema:
            type: string
        - name: page_size
          in: query
          description: >-
            Maximum number of results to be returned by the server. If 0,
            defaults to

            50.
          required: false
          schema:
            type: integer
        - name: page_token
          in: query
          description: Request a specific page of the list results.
          required: false
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
                $ref: '#/components/schemas/ListTrainingStepMetricsResponse'
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
    TrainingStepMetrics:
      type: object
      properties:
        created_at:
          type: string
          format: date-time
        step_number:
          type: integer
        metrics:
          type: object
          additionalProperties:
            type: number
            format: double
    ListTrainingStepMetricsResponse:
      type: object
      properties:
        step_metrics:
          type: array
          items:
            $ref: '#/components/schemas/TrainingStepMetrics'
        next_page_token:
          type: string
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
