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
  title: List Connectors
  version: endpoint_connectors.list
paths:
  /v1/connectors:
    get:
      operationId: list
      summary: List Connectors
      description: >-
        Returns a list of connectors ordered by descending creation date (newer
        first). See ['Managing your
        Connector'](https://docs.cohere.com/docs/managing-your-connector) for
        more information.
      tags:
        - - subpackage_connectors
      parameters:
        - name: limit
          in: query
          description: Maximum number of connectors to return [0, 100].
          required: false
          schema:
            type: number
            format: double
        - name: offset
          in: query
          description: Number of connectors to skip before returning results [0, inf].
          required: false
          schema:
            type: number
            format: double
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
                $ref: '#/components/schemas/ListConnectorsResponse'
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
    ListConnectorsResponse:
      type: object
      properties:
        connectors:
          type: array
          items:
            $ref: '#/components/schemas/Connector'
        total_count:
          type: number
          format: double
      required:
        - connectors
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
