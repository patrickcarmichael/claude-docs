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
  title: Get a Dataset
  version: endpoint_datasets.get
paths:
  /v1/datasets/{id}:
    get:
      operationId: get
      summary: Get a Dataset
      description: >-
        Retrieve a dataset by ID. See
        ['Datasets'](https://docs.cohere.com/docs/datasets) for more
        information.
      tags:
        - - subpackage_datasets
      parameters:
        - name: id
          in: path
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
                $ref: '#/components/schemas/datasets_get_Response_200'
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
    DatasetValidationStatus:
      type: string
      enum:
        - value: unknown
        - value: queued
        - value: processing
        - value: failed
        - value: validated
        - value: skipped
    DatasetPart:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        url:
          type: string
        index:
          type: integer
        size_bytes:
          type: integer
        num_rows:
          type: integer
        original_url:
          type: string
        samples:
          type: array
          items:
            type: string
      required:
        - id
        - name
    ParseInfo:
      type: object
      properties:
        separator:
          type: string
        delimiter:
          type: string
    RerankerDataMetrics:
      type: object
      properties:
        num_train_queries:
          type: integer
          format: int64
        num_train_relevant_passages:
          type: integer
          format: int64
        num_train_hard_negatives:
          type: integer
          format: int64
        num_eval_queries:
          type: integer
          format: int64
        num_eval_relevant_passages:
          type: integer
          format: int64
        num_eval_hard_negatives:
          type: integer
          format: int64
    ChatDataMetrics:
      type: object
      properties:
        num_train_turns:
          type: integer
          format: int64
        num_eval_turns:
          type: integer
          format: int64
        preamble:
          type: string
    LabelMetric:
      type: object
      properties:
        total_examples:
          type: integer
          format: int64
        label:
          type: string
        samples:
          type: array
          items:
            type: string
    ClassifyDataMetrics:
      type: object
      properties:
        label_metrics:
          type: array
          items:
            $ref: '#/components/schemas/LabelMetric'
    FinetuneDatasetMetrics:
      type: object
      properties:
        trainable_token_count:
          type: integer
          format: int64
        total_examples:
          type: integer
          format: int64
        train_examples:
          type: integer
          format: int64
        train_size_bytes:
          type: integer
          format: int64
        eval_examples:
          type: integer
          format: int64
        eval_size_bytes:
          type: integer
          format: int64
        reranker_data_metrics:
          $ref: '#/components/schemas/RerankerDataMetrics'
        chat_data_metrics:
          $ref: '#/components/schemas/ChatDataMetrics'
        classify_data_metrics:
          $ref: '#/components/schemas/ClassifyDataMetrics'
    Metrics:
      type: object
      properties:
        finetune_dataset_metrics:
          $ref: '#/components/schemas/FinetuneDatasetMetrics'
    Dataset:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        dataset_type:
          $ref: '#/components/schemas/DatasetType'
        validation_status:
          $ref: '#/components/schemas/DatasetValidationStatus'
        validation_error:
          type: string
        schema:
          type: string
        required_fields:
          type: array
          items:
            type: string
        preserve_fields:
          type: array
          items:
            type: string
        dataset_parts:
          type: array
          items:
            $ref: '#/components/schemas/DatasetPart'
        validation_warnings:
          type: array
          items:
            type: string
        parse_info:
          $ref: '#/components/schemas/ParseInfo'
        metrics:
          $ref: '#/components/schemas/Metrics'
      required:
        - id
        - name
        - created_at
        - updated_at
        - dataset_type
        - validation_status
    datasets_get_Response_200:
      type: object
      properties:
        dataset:
          $ref: '#/components/schemas/Dataset'
      required:
        - dataset
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
