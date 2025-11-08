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
  title: Embed API (v2)
  version: endpoint_v2.embed
paths:
  /v2/embed:
    post:
      operationId: embed
      summary: Embed API (v2)
      description: >-
        This endpoint returns text embeddings. An embedding is a list of
        floating point numbers that captures semantic information about the text
        that it represents.


        Embeddings can be used to create text classifiers as well as empower
        semantic search. To learn more about embeddings, see the embedding page.


        If you want to learn more how to use the embedding model, have a look at
        the [Semantic Search
        Guide](https://docs.cohere.com/docs/semantic-search).
      tags:
        - - subpackage_v2
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
                $ref: '#/components/schemas/EmbedByTypeResponse'
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
        description: ''
        content:
          application/json:
            schema:
              type: object
              properties:
                texts:
                  type: array
                  items:
                    type: string
                images:
                  type: array
                  items:
                    type: string
                model:
                  type: string
                input_type:
                  $ref: '#/components/schemas/EmbedInputType'
                inputs:
                  type: array
                  items:
                    $ref: '#/components/schemas/EmbedInput'
                max_tokens:
                  type: integer
                output_dimension:
                  type: integer
                embedding_types:
                  type: array
                  items:
                    $ref: '#/components/schemas/EmbeddingType'
                truncate:
                  $ref: >-
                    #/components/schemas/V2EmbedPostRequestBodyContentApplicationJsonSchemaTruncate
                priority:
                  type: integer
              required:
                - model
                - input_type
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
    EmbedContentType:
      type: string
      enum:
        - value: text
        - value: image_url
    EmbedImageUrl:
      type: object
      properties:
        url:
          type: string
      required:
        - url
    EmbedImage:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/EmbedContentType'
        image_url:
          $ref: '#/components/schemas/EmbedImageUrl'
    EmbedText:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/EmbedContentType'
        text:
          type: string
    EmbedContent:
      oneOf:
        - $ref: '#/components/schemas/EmbedImage'
        - $ref: '#/components/schemas/EmbedText'
    EmbedInput:
      type: object
      properties:
        content:
          type: array
          items:
            $ref: '#/components/schemas/EmbedContent'
      required:
        - content
    EmbeddingType:
      type: string
      enum:
        - value: float
        - value: int8
        - value: uint8
        - value: binary
        - value: ubinary
        - value: base64
    V2EmbedPostRequestBodyContentApplicationJsonSchemaTruncate:
      type: string
      enum:
        - value: NONE
        - value: START
        - value: END
    EmbedByTypeResponseResponseType:
      type: string
      enum:
        - value: embeddings_floats
        - value: embeddings_by_type
    EmbedByTypeResponseEmbeddings:
      type: object
      properties:
        float:
          type: array
          items:
            type: array
            items:
              type: number
              format: double
        int8:
          type: array
          items:
            type: array
            items:
              type: integer
        uint8:
          type: array
          items:
            type: array
            items:
              type: integer
        binary:
          type: array
          items:
            type: array
            items:
              type: integer
        ubinary:
          type: array
          items:
            type: array
            items:
              type: integer
        base64:
          type: array
          items:
            type: string
    Image:
      type: object
      properties:
        width:
          type: integer
          format: int64
        height:
          type: integer
          format: int64
        format:
          type: string
        bit_depth:
          type: integer
          format: int64
      required:
        - width
        - height
        - format
        - bit_depth
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
    EmbedByTypeResponse:
      type: object
      properties:
        response_type:
          $ref: '#/components/schemas/EmbedByTypeResponseResponseType'
        id:
          type: string
        embeddings:
          $ref: '#/components/schemas/EmbedByTypeResponseEmbeddings'
        texts:
          type: array
          items:
            type: string
        images:
          type: array
          items:
            $ref: '#/components/schemas/Image'
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - id
        - embeddings
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
