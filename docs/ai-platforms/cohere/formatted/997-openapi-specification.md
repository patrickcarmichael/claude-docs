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
  title: Create a Connector
  version: endpoint_connectors.create
paths:
  /v1/connectors:
    post:
      operationId: create
      summary: Create a Connector
      description: >-
        Creates a new connector. The connector is tested during registration and
        will cancel registration when the test is unsuccessful. See ['Creating
        and Deploying a
        Connector'](https://docs.cohere.com/v1/docs/creating-and-deploying-a-connector)
        for more information.
      tags:
        - - subpackage_connectors
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
                $ref: '#/components/schemas/CreateConnectorResponse'
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
              $ref: '#/components/schemas/CreateConnectorRequest'
components:
  schemas:
    CreateConnectorOAuth:
      type: object
      properties:
        client_id:
          type: string
        client_secret:
          type: string
        authorize_url:
          type: string
        token_url:
          type: string
        scope:
          type: string
    AuthTokenType:
      type: string
      enum:
        - value: bearer
        - value: basic
        - value: noscheme
    CreateConnectorServiceAuth:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/AuthTokenType'
        token:
          type: string
      required:
        - type
        - token
    CreateConnectorRequest:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        url:
          type: string
        excludes:
          type: array
          items:
            type: string
        oauth:
          $ref: '#/components/schemas/CreateConnectorOAuth'
        active:
          type: boolean
        continue_on_failure:
          type: boolean
        service_auth:
          $ref: '#/components/schemas/CreateConnectorServiceAuth'
      required:
        - name
        - url
    ConnectorOAuth:
      type: object
      properties:
        client_id:
          type: string
        client_secret:
          type: string
        authorize_url:
          type: string
        token_url:
          type: string
        scope:
          type: string
      required:
        - authorize_url
        - token_url
    ConnectorAuthStatus:
      type: string
      enum:
        - value: valid
        - value: expired
    Connector:
      type: object
      properties:
        id:
          type: string
        organization_id:
          type: string
        name:
          type: string
        description:
          type: string
        url:
          type: string
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        excludes:
          type: array
          items:
            type: string
        auth_type:
          type: string
          format: enum
        oauth:
          $ref: '#/components/schemas/ConnectorOAuth'
        auth_status:
          $ref: '#/components/schemas/ConnectorAuthStatus'
        active:
          type: boolean
        continue_on_failure:
          type: boolean
      required:
        - id
        - name
        - created_at
        - updated_at
    CreateConnectorResponse:
      type: object
      properties:
        connector:
          $ref: '#/components/schemas/Connector'
      required:
        - connector
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
