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
  title: Fetch history of statuses for a fine-tuned model.
  version: endpoint_finetuning.ListEvents
paths:
  /v1/finetuning/finetuned-models/{finetuned_model_id}/events:
    get:
      operationId: list-events
      summary: Fetch history of statuses for a fine-tuned model.
      description: >-
        Returns a list of events that occurred during the life-cycle of the
        fine-tuned model.

        The events are ordered by creation time, with the most recent event
        first.

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
        - name: order_by
          in: query
          description: >-
            Comma separated list of fields. For example: "created_at,name". The
            default

            sorting order is ascending. To specify descending order for a field,
            append

            " desc" to the field name. For example: "created_at desc,name".


            Supported sorting fields:
              - created_at (default)
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
                $ref: '#/components/schemas/ListEventsResponse'
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
    Status:
      type: string
      enum:
        - value: STATUS_UNSPECIFIED
        - value: STATUS_FINETUNING
        - value: STATUS_DEPLOYING_API
        - value: STATUS_READY
        - value: STATUS_FAILED
        - value: STATUS_DELETED
        - value: STATUS_TEMPORARILY_OFFLINE
        - value: STATUS_PAUSED
        - value: STATUS_QUEUED
    Event:
      type: object
      properties:
        user_id:
          type: string
        status:
          $ref: '#/components/schemas/Status'
        created_at:
          type: string
          format: date-time
    ListEventsResponse:
      type: object
      properties:
        events:
          type: array
          items:
            $ref: '#/components/schemas/Event'
        next_page_token:
          type: string
        total_size:
          type: integer
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
