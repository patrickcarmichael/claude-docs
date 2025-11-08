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
  title: Lists fine-tuned models.
  version: endpoint_finetuning.ListFinetunedModels
paths:
  /v1/finetuning/finetuned-models:
    get:
      operationId: list-finetuned-models
      summary: Lists fine-tuned models.
      description: Returns a list of fine-tuned models that the user has access to.
      tags:
        - - subpackage_finetuning
      parameters:
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
                $ref: '#/components/schemas/ListFinetunedModelsResponse'
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
    BaseType:
      type: string
      enum:
        - value: BASE_TYPE_UNSPECIFIED
        - value: BASE_TYPE_GENERATIVE
        - value: BASE_TYPE_CLASSIFICATION
        - value: BASE_TYPE_RERANK
        - value: BASE_TYPE_CHAT
    Strategy:
      type: string
      enum:
        - value: STRATEGY_UNSPECIFIED
        - value: STRATEGY_VANILLA
        - value: STRATEGY_TFEW
    BaseModel:
      type: object
      properties:
        name:
          type: string
        version:
          type: string
        base_type:
          $ref: '#/components/schemas/BaseType'
        strategy:
          $ref: '#/components/schemas/Strategy'
      required:
        - base_type
    LoraTargetModules:
      type: string
      enum:
        - value: LORA_TARGET_MODULES_UNSPECIFIED
        - value: LORA_TARGET_MODULES_QV
        - value: LORA_TARGET_MODULES_QKVO
        - value: LORA_TARGET_MODULES_QKVO_FFN
    Hyperparameters:
      type: object
      properties:
        early_stopping_patience:
          type: integer
        early_stopping_threshold:
          type: number
          format: double
        train_batch_size:
          type: integer
        train_epochs:
          type: integer
        learning_rate:
          type: number
          format: double
        lora_alpha:
          type: integer
        lora_rank:
          type: integer
        lora_target_modules:
          $ref: '#/components/schemas/LoraTargetModules'
    WandbConfig:
      type: object
      properties:
        project:
          type: string
        api_key:
          type: string
        entity:
          type: string
      required:
        - project
        - api_key
    Settings:
      type: object
      properties:
        base_model:
          $ref: '#/components/schemas/BaseModel'
        dataset_id:
          type: string
        hyperparameters:
          $ref: '#/components/schemas/Hyperparameters'
        multi_label:
          type: boolean
        wandb:
          $ref: '#/components/schemas/WandbConfig'
      required:
        - base_model
        - dataset_id
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
    FinetunedModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        creator_id:
          type: string
        organization_id:
          type: string
        settings:
          $ref: '#/components/schemas/Settings'
        status:
          $ref: '#/components/schemas/Status'
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        completed_at:
          type: string
          format: date-time
        last_used:
          type: string
          format: date-time
      required:
        - name
        - settings
    ListFinetunedModelsResponse:
      type: object
      properties:
        finetuned_models:
          type: array
          items:
            $ref: '#/components/schemas/FinetunedModel'
        next_page_token:
          type: string
        total_size:
          type: integer
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
