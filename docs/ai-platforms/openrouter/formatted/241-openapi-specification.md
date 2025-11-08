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
  title: Create a Coinbase charge for crypto payment
  version: endpoint_credits.createCoinbaseCharge
paths:
  /credits/coinbase:
    post:
      operationId: create-coinbase-charge
      summary: Create a Coinbase charge for crypto payment
      description: Create a Coinbase charge for crypto payment
      tags:
        - - subpackage_credits
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns the calldata to fulfill the transaction
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Credits_createCoinbaseCharge_Response_200'
        '400':
          description: Bad Request - Invalid credit amount or request body
          content: {}
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateChargeRequest'
components:
  schemas:
    CreateChargeRequestChainId:
      type: string
      enum:
        - value: '1'
        - value: '137'
        - value: '8453'
    CreateChargeRequest:
      type: object
      properties:
        amount:
          type: number
          format: double
        sender:
          type: string
        chain_id:
          $ref: '#/components/schemas/CreateChargeRequestChainId'
      required:
        - amount
        - sender
        - chain_id
    CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3DataTransferIntentCallData:
      type: object
      properties:
        deadline:
          type: string
        fee_amount:
          type: string
        id:
          type: string
        operator:
          type: string
        prefix:
          type: string
        recipient:
          type: string
        recipient_amount:
          type: string
        recipient_currency:
          type: string
        refund_destination:
          type: string
        signature:
          type: string
      required:
        - deadline
        - fee_amount
        - id
        - operator
        - prefix
        - recipient
        - recipient_amount
        - recipient_currency
        - refund_destination
        - signature
    CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3DataTransferIntentMetadata:
      type: object
      properties:
        chain_id:
          type: number
          format: double
        contract_address:
          type: string
        sender:
          type: string
      required:
        - chain_id
        - contract_address
        - sender
    CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3DataTransferIntent:
      type: object
      properties:
        call_data:
          $ref: >-
            #/components/schemas/CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3DataTransferIntentCallData
        metadata:
          $ref: >-
            #/components/schemas/CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3DataTransferIntentMetadata
      required:
        - call_data
        - metadata
    CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3Data:
      type: object
      properties:
        transfer_intent:
          $ref: >-
            #/components/schemas/CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3DataTransferIntent
      required:
        - transfer_intent
    CreditsCoinbasePostResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
        created_at:
          type: string
        expires_at:
          type: string
        web3_data:
          $ref: >-
            #/components/schemas/CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3Data
      required:
        - id
        - created_at
        - expires_at
        - web3_data
    Credits_createCoinbaseCharge_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/CreditsCoinbasePostResponsesContentApplicationJsonSchemaData
      required:
        - data
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
