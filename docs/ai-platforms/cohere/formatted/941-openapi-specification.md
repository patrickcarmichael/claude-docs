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
  title: Create an Embed Job
  version: endpoint_embedJobs.create
paths:
  /v1/embed-jobs:
    post:
      operationId: create
      summary: Create an Embed Job
      description: >-
        This API launches an async Embed job for a
        [Dataset](https://docs.cohere.com/docs/datasets) of type `embed-input`.
        The result of a completed embed job is new Dataset of type
        `embed-output`, which contains the original text entries and the
        corresponding embeddings.
      tags:
        - - subpackage_embedJobs
      parameters:
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
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateEmbedJobResponse'
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
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateEmbedJobRequest'
components:
  schemas:
    EmbedInputType:
      type: string
      enum:
        - value: search_document
        - value: search_query
        - value: classification
        - value: clustering
        - value: image
    EmbeddingType:
      type: string
      enum:
        - value: float
        - value: int8
        - value: uint8
        - value: binary
        - value: ubinary
        - value: base64
    CreateEmbedJobRequestTruncate:
      type: string
      enum:
        - value: START
        - value: END
    CreateEmbedJobRequest:
      type: object
      properties:
        model:
          type: string
          format: string
        dataset_id:
          type: string
        input_type:
          $ref: '#/components/schemas/EmbedInputType'
        name:
          type: string
        embedding_types:
          type: array
          items:
            $ref: '#/components/schemas/EmbeddingType'
        truncate:
          $ref: '#/components/schemas/CreateEmbedJobRequestTruncate'
      required:
        - model
        - dataset_id
        - input_type
    ApiMetaApiVersion:
      type: object
      properties:
        version:
          type: string
        is_deprecated:
          type: boolean
        is_experimental:
          type: boolean
      required:
        - version
    ApiMetaBilledUnits:
      type: object
      properties:
        images:
          type: number
          format: double
        input_tokens:
          type: number
          format: double
        output_tokens:
          type: number
          format: double
        search_units:
          type: number
          format: double
        classifications:
          type: number
          format: double
    ApiMetaTokens:
      type: object
      properties:
        input_tokens:
          type: number
          format: double
        output_tokens:
          type: number
          format: double
    ApiMeta:
      type: object
      properties:
        api_version:
          $ref: '#/components/schemas/ApiMetaApiVersion'
        billed_units:
          $ref: '#/components/schemas/ApiMetaBilledUnits'
        tokens:
          $ref: '#/components/schemas/ApiMetaTokens'
        cached_tokens:
          type: number
          format: double
        warnings:
          type: array
          items:
            type: string
    CreateEmbedJobResponse:
      type: object
      properties:
        job_id:
          type: string
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - job_id
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
