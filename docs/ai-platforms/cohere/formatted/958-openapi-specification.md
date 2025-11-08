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
  title: Create a Dataset
  version: endpoint_datasets.create
paths:
  /v1/datasets:
    post:
      operationId: create
      summary: Create a Dataset
      description: >-
        Create a dataset by uploading a file. See ['Dataset
        Creation'](https://docs.cohere.com/docs/datasets#dataset-creation) for
        more information.
      tags:
        - - subpackage_datasets
      parameters:
        - name: name
          in: query
          description: The name of the uploaded dataset.
          required: true
          schema:
            type: string
        - name: type
          in: query
          description: >-
            The dataset type, which is used to validate the data. The only valid
            type is `embed-input` used in conjunction with the Embed Jobs API.
          required: true
          schema:
            $ref: '#/components/schemas/DatasetType'
        - name: keep_original_file
          in: query
          description: Indicates if the original file should be stored.
          required: false
          schema:
            type: boolean
        - name: skip_malformed_input
          in: query
          description: >-
            Indicates whether rows with malformed input should be dropped
            (instead of failing the validation check). Dropped rows will be
            returned in the warnings field.
          required: false
          schema:
            type: boolean
        - name: keep_fields
          in: query
          description: >-
            List of names of fields that will be persisted in the Dataset. By
            default the Dataset will retain only the required fields indicated
            in the [schema for the corresponding Dataset
            type](https://docs.cohere.com/docs/datasets#dataset-types). For
            example, datasets of type `embed-input` will drop all fields other
            than the required `text` field. If any of the fields in
            `keep_fields` are missing from the uploaded file, Dataset validation
            will fail.
          required: false
          schema:
            type: array
            items:
              type: string
        - name: optional_fields
          in: query
          description: >-
            List of names of fields that will be persisted in the Dataset. By
            default the Dataset will retain only the required fields indicated
            in the [schema for the corresponding Dataset
            type](https://docs.cohere.com/docs/datasets#dataset-types). For
            example, Datasets of type `embed-input` will drop all fields other
            than the required `text` field. If any of the fields in
            `optional_fields` are missing from the uploaded file, Dataset
            validation will pass.
          required: false
          schema:
            type: array
            items:
              type: string
        - name: text_separator
          in: query
          description: >-
            Raw .txt uploads will be split into entries using the text_separator
            value.
          required: false
          schema:
            type: string
        - name: csv_delimiter
          in: query
          description: The delimiter used for .csv uploads.
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
                $ref: '#/components/schemas/datasets_create_Response_200'
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
          multipart/form-data:
            schema:
              type: object
              properties: {}
components:
  schemas:
    DatasetType:
      type: string
      enum:
        - value: embed-input
        - value: embed-result
        - value: cluster-result
        - value: cluster-outliers
        - value: reranker-finetune-input
        - value: single-label-classification-finetune-input
        - value: chat-finetune-input
        - value: multi-label-classification-finetune-input
        - value: batch-chat-input
        - value: batch-openai-chat-input
        - value: batch-embed-v2-input
        - value: batch-chat-v2-input
    datasets_create_Response_200:
      type: object
      properties:
        id:
          type: string
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
