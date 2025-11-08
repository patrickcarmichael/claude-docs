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
  title: List Models
  version: endpoint_models.list
paths:
  /v1/models:
    get:
      operationId: list
      summary: List Models
      description: Returns a list of models available for use.
      tags:
        - - subpackage_models
      parameters:
        - name: page_size
          in: query
          description: |-
            Maximum number of models to include in a page
            Defaults to `20`, min value of `1`, max value of `1000`.
          required: false
          schema:
            type: number
            format: double
        - name: page_token
          in: query
          description: >-
            Page token provided in the `next_page_token` field of a previous
            response.
          required: false
          schema:
            type: string
        - name: endpoint
          in: query
          description: >-
            When provided, filters the list of models to only those that are
            compatible with the specified endpoint.
          required: false
          schema:
            $ref: '#/components/schemas/CompatibleEndpoint'
        - name: default_only
          in: query
          description: >-
            When provided, filters the list of models to only the default model
            to the endpoint. This parameter is only valid when `endpoint` is
            provided.
          required: false
          schema:
            type: boolean
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListModelsResponse'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
components:
  schemas:
    CompatibleEndpoint:
      type: string
      enum:
        - value: chat
        - value: embed
        - value: classify
        - value: summarize
        - value: rerank
        - value: rate
        - value: generate
    GetModelResponse:
      type: object
      properties:
        name:
          type: string
        is_deprecated:
          type: boolean
        endpoints:
          type: array
          items:
            $ref: '#/components/schemas/CompatibleEndpoint'
        finetuned:
          type: boolean
        context_length:
          type: number
          format: double
        tokenizer_url:
          type: string
        default_endpoints:
          type: array
          items:
            $ref: '#/components/schemas/CompatibleEndpoint'
        features:
          type: array
          items:
            type: string
    ListModelsResponse:
      type: object
      properties:
        models:
          type: array
          items:
            $ref: '#/components/schemas/GetModelResponse'
        next_page_token:
          type: string
      required:
        - models
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
