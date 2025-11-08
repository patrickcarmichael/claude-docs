**Navigation:** [← Previous](./24-retrieve-custom-environments.md) | [Index](./index.md) | [Next →](./26-get-integration-resources.md)

---

# List products for integration configuration

> Lists all products available for an integration configuration. Use this endpoint to discover what integration products are available for your integration configuration. The returned product IDs or slugs can then be used with storage provisioning endpoints like `POST /v1/storage/stores/integration/direct`. ## Workflow 1. Get your integration configurations: `GET /v1/integrations/configurations` 2. **Use this endpoint**: Get products for a configuration: `GET /v1/integrations/configuration/{id}/products` 3. Create storage resource: `POST /v1/storage/stores/integration/direct` ## Response Returns an array of products with their IDs, slugs, names, supported protocols, and metadata requirements. Each product represents a different type of resource you can provision. The `metadataSchema` field contains a JSON Schema that defines: - **Required metadata**: Fields that must be provided during storage creation - **Optional metadata**: Fields that can be provided but are not mandatory - **Field validation**: Data types, allowed values, and constraints Use this schema to validate metadata before calling the storage creation endpoint.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/configuration/{id}/products
paths:
  path: /v1/integrations/configuration/{id}/products
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: ID of the integration configuration
              example: icfg_cuwj0AdCdH3BwWT4LPijCC7t
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getConfigurationProducts
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.integrations.getConfigurationProducts({
              id: "icfg_cuwj0AdCdH3BwWT4LPijCC7t",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              products:
                allOf:
                  - items:
                      properties:
                        id:
                          type: string
                        slug:
                          type: string
                        name:
                          type: string
                        protocols:
                          properties:
                            storage:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                                repl:
                                  properties:
                                    enabled:
                                      type: boolean
                                    supportsReadOnlyMode:
                                      type: boolean
                                    welcomeMessage:
                                      type: string
                                  required:
                                    - enabled
                                    - supportsReadOnlyMode
                                  type: object
                              required:
                                - status
                              type: object
                            experimentation:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                                edgeConfigSyncingSupport:
                                  type: boolean
                              required:
                                - status
                              type: object
                            ai:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            authentication:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            observability:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            video:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            workflow:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            checks:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            logDrain:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                                endpoint:
                                  type: string
                                headers:
                                  additionalProperties:
                                    type: string
                                  type: object
                                format:
                                  type: string
                                  enum:
                                    - json
                                    - ndjson
                              required:
                                - status
                                - endpoint
                                - format
                              type: object
                            traceDrain:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                                endpoint:
                                  type: string
                                headers:
                                  additionalProperties:
                                    type: string
                                  type: object
                                format:
                                  type: string
                                  enum:
                                    - json
                                    - proto
                              required:
                                - status
                                - endpoint
                                - format
                              type: object
                            messaging:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                            other:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - disabled
                                    - enabled
                              required:
                                - status
                              type: object
                          type: object
                        primaryProtocol:
                          type: string
                          enum:
                            - storage
                            - experimentation
                            - ai
                            - observability
                            - video
                            - authentication
                            - workflow
                            - checks
                            - logDrain
                            - traceDrain
                            - messaging
                            - other
                        metadataSchema:
                          properties:
                            type:
                              type: string
                              enum:
                                - object
                            properties:
                              additionalProperties:
                                oneOf:
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - string
                                      ui:control:
                                        type: string
                                        enum:
                                          - input
                                      description:
                                        type: string
                                      minLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      maxLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      pattern:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      default:
                                        type: string
                                      enum:
                                        items:
                                          type: string
                                        type: array
                                      ui:label:
                                        type: string
                                      ui:read-only:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:hidden:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:disabled:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:description:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                      ui:formatted-value:
                                        properties:
                                          expr:
                                            type: string
                                        required:
                                          - expr
                                        type: object
                                      ui:placeholder:
                                        type: string
                                    required:
                                      - type
                                      - ui:control
                                    type: object
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - number
                                      ui:control:
                                        type: string
                                        enum:
                                          - input
                                      minimum:
                                        type: number
                                      maximum:
                                        type: number
                                      description:
                                        type: string
                                      default:
                                        type: number
                                      exclusiveMinimum:
                                        type: number
                                      exclusiveMaximum:
                                        type: number
                                      ui:label:
                                        type: string
                                      ui:read-only:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:hidden:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:disabled:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:description:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                      ui:formatted-value:
                                        properties:
                                          expr:
                                            type: string
                                        required:
                                          - expr
                                        type: object
                                      ui:placeholder:
                                        type: string
                                    required:
                                      - type
                                      - ui:control
                                    type: object
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - boolean
                                      ui:control:
                                        type: string
                                        enum:
                                          - toggle
                                      description:
                                        type: string
                                      default:
                                        type: boolean
                                      ui:label:
                                        type: string
                                      ui:read-only:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:hidden:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:disabled:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:description:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                      ui:formatted-value:
                                        properties:
                                          expr:
                                            type: string
                                        required:
                                          - expr
                                        type: object
                                    required:
                                      - type
                                      - ui:control
                                    type: object
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - array
                                      ui:control:
                                        type: string
                                        enum:
                                          - slider
                                      ui:steps:
                                        items:
                                          type: number
                                        type: array
                                      items:
                                        properties:
                                          type:
                                            type: string
                                            enum:
                                              - number
                                          description:
                                            type: string
                                          minimum:
                                            type: number
                                          exclusiveMinimum:
                                            type: number
                                          maximum:
                                            type: number
                                          exclusiveMaximum:
                                            type: number
                                          default:
                                            type: number
                                        required:
                                          - type
                                        type: object
                                      description:
                                        type: string
                                      minItems:
                                        type: number
                                      maxItems:
                                        type: number
                                      ui:label:
                                        type: string
                                      ui:read-only:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:hidden:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:disabled:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:description:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                      ui:formatted-value:
                                        properties:
                                          expr:
                                            type: string
                                        required:
                                          - expr
                                        type: object
                                      default:
                                        items:
                                          type: number
                                        type: array
                                    required:
                                      - type
                                      - ui:control
                                      - ui:steps
                                      - items
                                    type: object
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - string
                                      ui:control:
                                        type: string
                                        enum:
                                          - select
                                      ui:options:
                                        items:
                                          properties:
                                            value:
                                              type: string
                                            label:
                                              type: string
                                            disabled:
                                              oneOf:
                                                - type: boolean
                                                - properties:
                                                    expr:
                                                      type: string
                                                  required:
                                                    - expr
                                                  type: object
                                                - type: string
                                                  enum:
                                                    - update
                                                    - create
                                            hidden:
                                              oneOf:
                                                - type: boolean
                                                - properties:
                                                    expr:
                                                      type: string
                                                  required:
                                                    - expr
                                                  type: object
                                                - type: string
                                                  enum:
                                                    - update
                                                    - create
                                          required:
                                            - value
                                            - label
                                          type: object
                                        type: array
                                      description:
                                        type: string
                                      minLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      maxLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      pattern:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      default:
                                        type: string
                                      enum:
                                        items:
                                          type: string
                                        type: array
                                      ui:label:
                                        type: string
                                      ui:read-only:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:hidden:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:disabled:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:description:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                      ui:formatted-value:
                                        properties:
                                          expr:
                                            type: string
                                        required:
                                          - expr
                                        type: object
                                      ui:placeholder:
                                        type: string
                                    required:
                                      - type
                                      - ui:control
                                      - ui:options
                                    type: object
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - array
                                      ui:control:
                                        type: string
                                        enum:
                                          - multi-select
                                      items:
                                        properties:
                                          type:
                                            type: string
                                            enum:
                                              - string
                                          description:
                                            type: string
                                          minLength:
                                            type: object
                                            properties:
                                              __@BRAND@647815:
                                                type: object
                                            required:
                                              - __@BRAND@647815
                                          maxLength:
                                            type: object
                                            properties:
                                              __@BRAND@647815:
                                                type: object
                                            required:
                                              - __@BRAND@647815
                                          pattern:
                                            type: object
                                            properties:
                                              __@BRAND@647815:
                                                type: object
                                            required:
                                              - __@BRAND@647815
                                          default:
                                            type: string
                                          enum:
                                            items:
                                              type: string
                                            type: array
                                        required:
                                          - type
                                        type: object
                                      ui:options:
                                        items:
                                          properties:
                                            value:
                                              type: string
                                            label:
                                              type: string
                                            disabled:
                                              oneOf:
                                                - type: boolean
                                                - properties:
                                                    expr:
                                                      type: string
                                                  required:
                                                    - expr
                                                  type: object
                                                - type: string
                                                  enum:
                                                    - update
                                                    - create
                                            hidden:
                                              oneOf:
                                                - type: boolean
                                                - properties:
                                                    expr:
                                                      type: string
                                                  required:
                                                    - expr
                                                  type: object
                                                - type: string
                                                  enum:
                                                    - update
                                                    - create
                                          required:
                                            - value
                                            - label
                                          type: object
                                        type: array
                                      description:
                                        type: string
                                      minItems:
                                        type: number
                                      maxItems:
                                        type: number
                                      ui:label:
                                        type: string
                                      ui:read-only:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:hidden:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:disabled:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:description:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                      ui:formatted-value:
                                        properties:
                                          expr:
                                            type: string
                                        required:
                                          - expr
                                        type: object
                                      ui:placeholder:
                                        type: string
                                      default:
                                        items:
                                          type: string
                                        type: array
                                      example:
                                        items:
                                          type: string
                                        type: array
                                    required:
                                      - type
                                      - ui:control
                                      - items
                                      - ui:options
                                    type: object
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - string
                                      ui:control:
                                        type: string
                                        enum:
                                          - vercel-region
                                      ui:options:
                                        items:
                                          oneOf:
                                            - properties:
                                                value:
                                                  type: string
                                                label:
                                                  type: string
                                                disabled:
                                                  oneOf:
                                                    - type: boolean
                                                    - properties:
                                                        expr:
                                                          type: string
                                                      required:
                                                        - expr
                                                      type: object
                                                    - type: string
                                                      enum:
                                                        - update
                                                        - create
                                                hidden:
                                                  oneOf:
                                                    - type: boolean
                                                    - properties:
                                                        expr:
                                                          type: string
                                                      required:
                                                        - expr
                                                      type: object
                                                    - type: string
                                                      enum:
                                                        - update
                                                        - create
                                              required:
                                                - value
                                                - label
                                              type: object
                                            - type: object
                                              properties:
                                                __@BRAND@647815:
                                                  type: object
                                              required:
                                                - __@BRAND@647815
                                            - properties:
                                                value:
                                                  type: object
                                                  properties:
                                                    __@BRAND@647815:
                                                      type: object
                                                  required:
                                                    - __@BRAND@647815
                                                disabled:
                                                  oneOf:
                                                    - type: boolean
                                                    - properties:
                                                        expr:
                                                          type: string
                                                      required:
                                                        - expr
                                                      type: object
                                                    - type: string
                                                      enum:
                                                        - update
                                                        - create
                                                hidden:
                                                  oneOf:
                                                    - type: boolean
                                                    - properties:
                                                        expr:
                                                          type: string
                                                      required:
                                                        - expr
                                                      type: object
                                                    - type: string
                                                      enum:
                                                        - update
                                                        - create
                                              required:
                                                - value
                                              type: object
                                        type: array
                                      description:
                                        type: string
                                      minLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      maxLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      pattern:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      default:
                                        type: string
                                      enum:
                                        items:
                                          type: string
                                        type: array
                                      ui:label:
                                        type: string
                                      ui:read-only:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:hidden:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:disabled:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:description:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                      ui:formatted-value:
                                        properties:
                                          expr:
                                            type: string
                                        required:
                                          - expr
                                        type: object
                                      ui:placeholder:
                                        type: string
                                    required:
                                      - type
                                      - ui:control
                                      - ui:options
                                    type: object
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - array
                                      ui:control:
                                        type: string
                                        enum:
                                          - multi-vercel-region
                                      items:
                                        properties:
                                          type:
                                            type: string
                                            enum:
                                              - string
                                          description:
                                            type: string
                                          minLength:
                                            type: object
                                            properties:
                                              __@BRAND@647815:
                                                type: object
                                            required:
                                              - __@BRAND@647815
                                          maxLength:
                                            type: object
                                            properties:
                                              __@BRAND@647815:
                                                type: object
                                            required:
                                              - __@BRAND@647815
                                          pattern:
                                            type: object
                                            properties:
                                              __@BRAND@647815:
                                                type: object
                                            required:
                                              - __@BRAND@647815
                                          default:
                                            type: string
                                          enum:
                                            items:
                                              type: string
                                            type: array
                                        required:
                                          - type
                                        type: object
                                      ui:options:
                                        items:
                                          oneOf:
                                            - properties:
                                                value:
                                                  type: string
                                                label:
                                                  type: string
                                                disabled:
                                                  oneOf:
                                                    - type: boolean
                                                    - properties:
                                                        expr:
                                                          type: string
                                                      required:
                                                        - expr
                                                      type: object
                                                    - type: string
                                                      enum:
                                                        - update
                                                        - create
                                                hidden:
                                                  oneOf:
                                                    - type: boolean
                                                    - properties:
                                                        expr:
                                                          type: string
                                                      required:
                                                        - expr
                                                      type: object
                                                    - type: string
                                                      enum:
                                                        - update
                                                        - create
                                              required:
                                                - value
                                                - label
                                              type: object
                                            - type: object
                                              properties:
                                                __@BRAND@647815:
                                                  type: object
                                              required:
                                                - __@BRAND@647815
                                            - properties:
                                                value:
                                                  type: object
                                                  properties:
                                                    __@BRAND@647815:
                                                      type: object
                                                  required:
                                                    - __@BRAND@647815
                                                disabled:
                                                  oneOf:
                                                    - type: boolean
                                                    - properties:
                                                        expr:
                                                          type: string
                                                      required:
                                                        - expr
                                                      type: object
                                                    - type: string
                                                      enum:
                                                        - update
                                                        - create
                                                hidden:
                                                  oneOf:
                                                    - type: boolean
                                                    - properties:
                                                        expr:
                                                          type: string
                                                      required:
                                                        - expr
                                                      type: object
                                                    - type: string
                                                      enum:
                                                        - update
                                                        - create
                                              required:
                                                - value
                                              type: object
                                        type: array
                                      description:
                                        type: string
                                      minItems:
                                        type: number
                                      maxItems:
                                        type: number
                                      ui:label:
                                        type: string
                                      ui:read-only:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:hidden:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:disabled:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:description:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                      ui:formatted-value:
                                        properties:
                                          expr:
                                            type: string
                                        required:
                                          - expr
                                        type: object
                                      ui:placeholder:
                                        type: string
                                      default:
                                        items:
                                          type: object
                                          properties:
                                            __@BRAND@647815:
                                              type: object
                                          required:
                                            - __@BRAND@647815
                                        type: array
                                      example:
                                        items:
                                          type: object
                                          properties:
                                            __@BRAND@647815:
                                              type: object
                                          required:
                                            - __@BRAND@647815
                                        type: array
                                    required:
                                      - type
                                      - ui:control
                                      - items
                                      - ui:options
                                    type: object
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - string
                                      ui:control:
                                        type: string
                                        enum:
                                          - domain
                                      description:
                                        type: string
                                      minLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      maxLength:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      pattern:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      default:
                                        type: string
                                      enum:
                                        items:
                                          type: string
                                        type: array
                                      ui:label:
                                        type: string
                                      ui:read-only:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:hidden:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:disabled:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      ui:description:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                      ui:formatted-value:
                                        properties:
                                          expr:
                                            type: string
                                        required:
                                          - expr
                                        type: object
                                      ui:placeholder:
                                        type: string
                                    required:
                                      - type
                                      - ui:control
                                    type: object
                                  - properties:
                                      value:
                                        type: object
                                        properties:
                                          __@BRAND@647815:
                                            type: object
                                        required:
                                          - __@BRAND@647815
                                      disabled:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                      hidden:
                                        oneOf:
                                          - type: boolean
                                          - properties:
                                              expr:
                                                type: string
                                            required:
                                              - expr
                                            type: object
                                          - type: string
                                            enum:
                                              - update
                                              - create
                                    required:
                                      - value
                                    type: object
                              type: object
                            required:
                              items:
                                type: string
                              type: array
                          required:
                            - type
                            - properties
                          type: object
                      required:
                        - id
                        - slug
                        - name
                        - protocols
                        - metadataSchema
                      type: object
                    type: array
              integration:
                allOf:
                  - properties:
                      id:
                        type: string
                      slug:
                        type: string
                      name:
                        type: string
                    required:
                      - id
                      - slug
                      - name
                    type: object
              configuration:
                allOf:
                  - properties:
                      id:
                        type: string
                    required:
                      - id
                    type: object
            requiredProperties:
              - products
              - integration
              - configuration
        examples:
          example:
            value:
              products:
                - id: <string>
                  slug: <string>
                  name: <string>
                  protocols:
                    storage:
                      status: disabled
                      repl:
                        enabled: true
                        supportsReadOnlyMode: true
                        welcomeMessage: <string>
                    experimentation:
                      status: disabled
                      edgeConfigSyncingSupport: true
                    ai:
                      status: disabled
                    authentication:
                      status: disabled
                    observability:
                      status: disabled
                    video:
                      status: disabled
                    workflow:
                      status: disabled
                    checks:
                      status: disabled
                    logDrain:
                      status: disabled
                      endpoint: <string>
                      headers: {}
                      format: json
                    traceDrain:
                      status: disabled
                      endpoint: <string>
                      headers: {}
                      format: json
                    messaging:
                      status: disabled
                    other:
                      status: disabled
                  primaryProtocol: storage
                  metadataSchema:
                    type: object
                    properties: {}
                    required:
                      - <string>
              integration:
                id: <string>
                slug: <string>
                name: <string>
              configuration:
                id: <string>
        description: List of products available for this integration configuration
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Retrieve an integration configuration"

last_updated: "2025-11-07T00:37:12.209Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/integrations/retrieve-an-integration-configuration"
--------------------------------------------------------------------------------

# Retrieve an integration configuration

> Allows to retrieve a the configuration with the provided id in case it exists. The authenticated user or team must be the owner of the config in order to access it.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/configuration/{id}
paths:
  path: /v1/integrations/configuration/{id}
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: ID of the configuration to check
              example: icfg_cuwj0AdCdH3BwWT4LPijCC7t
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getConfiguration
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Integrations.GetConfiguration(ctx, \"icfg_cuwj0AdCdH3BwWT4LPijCC7t\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: getConfiguration
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.integrations.getConfiguration({
              id: "icfg_cuwj0AdCdH3BwWT4LPijCC7t",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              projectSelection:
                allOf:
                  - type: string
                    enum:
                      - selected
                      - all
                    description: >-
                      A string representing the permission for projects.
                      Possible values are `all` or `selected`.
                    example: all
              notification:
                allOf:
                  - properties:
                      level:
                        type: string
                        enum:
                          - info
                          - warn
                          - error
                      title:
                        type: string
                      message:
                        type: string
                      href:
                        type: string
                    required:
                      - level
                      - title
                    type: object
              transferRequest:
                allOf:
                  - oneOf:
                      - properties:
                          kind:
                            type: string
                            enum:
                              - transfer-to-marketplace
                          metadata:
                            additionalProperties: true
                            type: object
                          billingPlan:
                            properties:
                              id:
                                type: string
                              type:
                                type: string
                                enum:
                                  - subscription
                                  - prepayment
                              scope:
                                type: string
                                enum:
                                  - installation
                                  - resource
                              name:
                                type: string
                              description:
                                type: string
                              paymentMethodRequired:
                                type: boolean
                              preauthorizationAmount:
                                type: number
                            required:
                              - id
                              - type
                              - name
                              - description
                            type: object
                          requestId:
                            type: string
                          transferId:
                            type: string
                          requester:
                            properties:
                              name:
                                type: string
                              email:
                                type: string
                            required:
                              - name
                            type: object
                          createdAt:
                            type: number
                          expiresAt:
                            type: number
                          discardedAt:
                            type: number
                          discardedBy:
                            type: string
                          approvedAt:
                            type: number
                          approvedBy:
                            type: string
                          authorizationId:
                            type: string
                        required:
                          - kind
                          - requestId
                          - transferId
                          - requester
                          - createdAt
                          - expiresAt
                        type: object
                      - properties:
                          kind:
                            type: string
                            enum:
                              - transfer-from-marketplace
                          requestId:
                            type: string
                          transferId:
                            type: string
                          requester:
                            properties:
                              name:
                                type: string
                              email:
                                type: string
                            required:
                              - name
                            type: object
                          createdAt:
                            type: number
                          expiresAt:
                            type: number
                          discardedAt:
                            type: number
                          discardedBy:
                            type: string
                          approvedAt:
                            type: number
                          approvedBy:
                            type: string
                          authorizationId:
                            type: string
                        required:
                          - kind
                          - requestId
                          - transferId
                          - requester
                          - createdAt
                          - expiresAt
                        type: object
              projects:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      When a configuration is limited to access certain
                      projects, this will contain each of the project ID it is
                      allowed to access. If it is not defined, the configuration
                      has full access.
                    example:
                      - prj_xQxbutw1HpL6HLYPAzt5h75m8NjO
              createdAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      created
                    example: 1558531915505
              completedAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      installed successfully
                    example: 1558531915505
              id:
                allOf:
                  - type: string
                    description: The unique identifier of the configuration
                    example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
              integrationId:
                allOf:
                  - type: string
                    description: >-
                      The unique identifier of the app the configuration was
                      created for
                    example: oac_xzpVzcUOgcB1nrVlirtKhbWV
              ownerId:
                allOf:
                  - type: string
                    description: The user or team ID that owns the configuration
                    example: kr1PsOIzqEL5Xg6M4VZcZosf
              slug:
                allOf:
                  - type: string
                    description: >-
                      The slug of the integration the configuration is created
                      for.
                    example: slack
              teamId:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      When the configuration was created for a team, this will
                      show the ID of the team.
                    example: team_nLlpyC6RE1qxydlFKbrxDlud
              updatedAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      updated.
                    example: 1558531915505
              userId:
                allOf:
                  - type: string
                    description: The ID of the user that created the configuration.
                    example: kr1PsOIzqEL5Xg6M4VZcZosf
              scopes:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      The resources that are allowed to be accessed by the
                      configuration.
                    example:
                      - read:project
                      - read-write:log-drain
              disabledAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      disabled. Note: Configurations can be disabled when the
                      associated user loses access to a team. They do not
                      function during this time until the configuration is
                      'transferred', meaning the associated user is changed to
                      one with access to the team.
                    example: 1558531915505
              disabledReason:
                allOf:
                  - type: string
                    enum:
                      - disabled-by-owner
                      - feature-not-available
                      - disabled-by-admin
                      - original-owner-left-the-team
                      - account-plan-downgrade
                      - original-owner-role-downgraded
              source:
                allOf:
                  - type: string
                    enum:
                      - marketplace
                      - deploy-button
                      - external
                      - v0
                      - resource-claims
                    description: >-
                      Source defines where the configuration was installed from.
                      It is used to analyze user engagement for integration
                      installations in product metrics.
                    example: marketplace
              canConfigureOpenTelemetry:
                allOf:
                  - type: boolean
              installationType:
                allOf:
                  - type: string
                    enum:
                      - marketplace
                      - external
                    description: >-
                      Defines the installation type. - 'external' integrations
                      are installed via the existing integrations flow -
                      'marketplace' integrations are natively installed: - when
                      accepting the TOS of a partner during the store creation
                      process - if undefined, assume 'external'
              deleteRequestedAt:
                allOf:
                  - nullable: true
                    type: number
                    description: >-
                      A timestamp that tells you when the configuration deletion
                      has been started for cases when the deletion needs to be
                      settled/approved by partners, such as when marketplace
                      invoices have been paid.
                    example: 1558531915505
              type:
                allOf:
                  - type: string
                    enum:
                      - integration-configuration
              deletedAt:
                allOf:
                  - nullable: true
                    type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      deleted.
                    example: 1558531915505
            requiredProperties:
              - projectSelection
              - notification
              - transferRequest
              - createdAt
              - id
              - integrationId
              - ownerId
              - slug
              - updatedAt
              - userId
              - scopes
              - type
          - type: object
            properties:
              completedAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      installed successfully
                    example: 1558531915505
              createdAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      created
                    example: 1558531915505
              id:
                allOf:
                  - type: string
                    description: The unique identifier of the configuration
                    example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
              integrationId:
                allOf:
                  - type: string
                    description: >-
                      The unique identifier of the app the configuration was
                      created for
                    example: oac_xzpVzcUOgcB1nrVlirtKhbWV
              ownerId:
                allOf:
                  - type: string
                    description: The user or team ID that owns the configuration
                    example: kr1PsOIzqEL5Xg6M4VZcZosf
              projects:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      When a configuration is limited to access certain
                      projects, this will contain each of the project ID it is
                      allowed to access. If it is not defined, the configuration
                      has full access.
                    example:
                      - prj_xQxbutw1HpL6HLYPAzt5h75m8NjO
              source:
                allOf:
                  - type: string
                    enum:
                      - marketplace
                      - deploy-button
                      - external
                      - v0
                      - resource-claims
                    description: >-
                      Source defines where the configuration was installed from.
                      It is used to analyze user engagement for integration
                      installations in product metrics.
                    example: marketplace
              slug:
                allOf:
                  - type: string
                    description: >-
                      The slug of the integration the configuration is created
                      for.
                    example: slack
              teamId:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      When the configuration was created for a team, this will
                      show the ID of the team.
                    example: team_nLlpyC6RE1qxydlFKbrxDlud
              type:
                allOf:
                  - type: string
                    enum:
                      - integration-configuration
              updatedAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      updated.
                    example: 1558531915505
              userId:
                allOf:
                  - type: string
                    description: The ID of the user that created the configuration.
                    example: kr1PsOIzqEL5Xg6M4VZcZosf
              scopes:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      The resources that are allowed to be accessed by the
                      configuration.
                    example:
                      - read:project
                      - read-write:log-drain
              disabledAt:
                allOf:
                  - type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      disabled. Note: Configurations can be disabled when the
                      associated user loses access to a team. They do not
                      function during this time until the configuration is
                      'transferred', meaning the associated user is changed to
                      one with access to the team.
                    example: 1558531915505
              deletedAt:
                allOf:
                  - nullable: true
                    type: number
                    description: >-
                      A timestamp that tells you when the configuration was
                      deleted.
                    example: 1558531915505
              deleteRequestedAt:
                allOf:
                  - nullable: true
                    type: number
                    description: >-
                      A timestamp that tells you when the configuration deletion
                      has been started for cases when the deletion needs to be
                      settled/approved by partners, such as when marketplace
                      invoices have been paid.
                    example: 1558531915505
              disabledReason:
                allOf:
                  - type: string
                    enum:
                      - disabled-by-owner
                      - feature-not-available
                      - disabled-by-admin
                      - original-owner-left-the-team
                      - account-plan-downgrade
                      - original-owner-role-downgraded
              installationType:
                allOf:
                  - type: string
                    enum:
                      - marketplace
                      - external
                    description: >-
                      Defines the installation type. - 'external' integrations
                      are installed via the existing integrations flow -
                      'marketplace' integrations are natively installed: - when
                      accepting the TOS of a partner during the store creation
                      process - if undefined, assume 'external'
            description: The configuration with the provided id
            requiredProperties:
              - createdAt
              - id
              - integrationId
              - ownerId
              - slug
              - type
              - updatedAt
              - userId
              - scopes
        examples:
          example:
            value:
              projectSelection: all
              notification:
                level: info
                title: <string>
                message: <string>
                href: <string>
              transferRequest:
                kind: transfer-to-marketplace
                metadata: {}
                billingPlan:
                  id: <string>
                  type: subscription
                  scope: installation
                  name: <string>
                  description: <string>
                  paymentMethodRequired: true
                  preauthorizationAmount: 123
                requestId: <string>
                transferId: <string>
                requester:
                  name: <string>
                  email: <string>
                createdAt: 123
                expiresAt: 123
                discardedAt: 123
                discardedBy: <string>
                approvedAt: 123
                approvedBy: <string>
                authorizationId: <string>
              projects:
                - prj_xQxbutw1HpL6HLYPAzt5h75m8NjO
              createdAt: 1558531915505
              completedAt: 1558531915505
              id: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
              integrationId: oac_xzpVzcUOgcB1nrVlirtKhbWV
              ownerId: kr1PsOIzqEL5Xg6M4VZcZosf
              slug: slack
              teamId: team_nLlpyC6RE1qxydlFKbrxDlud
              updatedAt: 1558531915505
              userId: kr1PsOIzqEL5Xg6M4VZcZosf
              scopes:
                - read:project
                - read-write:log-drain
              disabledAt: 1558531915505
              disabledReason: disabled-by-owner
              source: marketplace
              canConfigureOpenTelemetry: true
              installationType: marketplace
              deleteRequestedAt: 1558531915505
              type: integration-configuration
              deletedAt: 1558531915505
        description: The configuration with the provided id
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The configuration was not found
        examples: {}
        description: The configuration was not found
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Creates a Configurable Log Drain (deprecated)"

last_updated: "2025-11-07T00:37:12.754Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/logdrains/creates-a-configurable-log-drain-deprecated"
--------------------------------------------------------------------------------

# Creates a Configurable Log Drain (deprecated)

> Creates a configurable log drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed)

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/log-drains
paths:
  path: /v1/log-drains
  method: post
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path: {}
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              deliveryFormat:
                allOf:
                  - description: The delivery log format
                    example: json
                    enum:
                      - json
                      - ndjson
              url:
                allOf:
                  - description: The log drain url
                    format: uri
                    pattern: ^(http|https)?://
                    type: string
              headers:
                allOf:
                  - description: Headers to be sent together with the request
                    type: object
                    additionalProperties:
                      type: string
              projectIds:
                allOf:
                  - minItems: 1
                    maxItems: 50
                    type: array
                    items:
                      pattern: ^[a-zA-z0-9_]+$
                      type: string
              sources:
                allOf:
                  - type: array
                    uniqueItems: true
                    items:
                      type: string
                      enum:
                        - static
                        - lambda
                        - build
                        - edge
                        - external
                        - firewall
                    minItems: 1
              environments:
                allOf:
                  - type: array
                    uniqueItems: true
                    items:
                      type: string
                      enum:
                        - preview
                        - production
                    minItems: 1
              secret:
                allOf:
                  - description: Custom secret of log drain
                    type: string
              samplingRate:
                allOf:
                  - type: number
                    description: >-
                      The sampling rate for this log drain. It should be a
                      percentage rate between 0 and 100. With max 2 decimal
                      points
                    minimum: 0.01
                    maximum: 1
                    multipleOf: 0.01
              name:
                allOf:
                  - type: string
                    description: The custom name of this log drain.
            required: true
            requiredProperties:
              - deliveryFormat
              - url
              - sources
            additionalProperties: false
        examples:
          example:
            value:
              deliveryFormat: json
              url: <string>
              headers: {}
              projectIds:
                - <string>
              sources:
                - static
              environments:
                - preview
              secret: <string>
              samplingRate: 0.505
              name: <string>
    codeSamples:
      - label: createConfigurableLogDrain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.LogDrains.CreateConfigurableLogDrain(ctx, nil, nil, &operations.CreateConfigurableLogDrainRequestBody{\n        DeliveryFormat: operations.CreateConfigurableLogDrainDeliveryFormatJSON,\n        URL: \"https://sugary-technician.name\",\n        Sources: []operations.CreateConfigurableLogDrainSources{\n            operations.CreateConfigurableLogDrainSourcesExternal,\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createConfigurableLogDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.logDrains.createConfigurableLogDrain({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                deliveryFormat: "json",
                url: "https://wavy-meander.net",
                sources: [],
              },
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
        examples:
          example:
            value: {}
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Creates a new Integration Log Drain (deprecated)"

last_updated: "2025-11-07T00:37:12.737Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/logdrains/creates-a-new-integration-log-drain-deprecated"
--------------------------------------------------------------------------------

# Creates a new Integration Log Drain (deprecated)

> Creates an Integration log drain. This endpoint must be called with an OAuth2 client (integration), since log drains are tied to integrations. If it is called with a different token type it will produce a 400 error.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/integrations/log-drains
paths:
  path: /v2/integrations/log-drains
  method: post
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path: {}
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - description: The name of the log drain
                    example: My first log drain
                    maxLength: 100
                    pattern: ^[A-z0-9_ -]+$
                    type: string
              projectIds:
                allOf:
                  - minItems: 1
                    maxItems: 50
                    type: array
                    items:
                      pattern: ^[a-zA-z0-9_]+$
                      type: string
              secret:
                allOf:
                  - description: >-
                      A secret to sign log drain notification headers so a
                      consumer can verify their authenticity
                    example: a1Xsfd325fXcs
                    maxLength: 100
                    pattern: ^[A-z0-9_ -]+$
                    type: string
              deliveryFormat:
                allOf:
                  - description: The delivery log format
                    example: json
                    enum:
                      - json
                      - ndjson
              url:
                allOf:
                  - description: >-
                      The url where you will receive logs. The protocol must be
                      `https://` or `http://` when type is `json` and `ndjson`.
                    example: https://example.com/log-drain
                    format: uri
                    pattern: ^https?://
                    type: string
              sources:
                allOf:
                  - type: array
                    uniqueItems: true
                    items:
                      type: string
                      enum:
                        - static
                        - lambda
                        - build
                        - edge
                        - external
                        - firewall
                    minItems: 1
              headers:
                allOf:
                  - description: Headers to be sent together with the request
                    type: object
                    additionalProperties:
                      type: string
              environments:
                allOf:
                  - type: array
                    uniqueItems: true
                    items:
                      type: string
                      enum:
                        - preview
                        - production
                    minItems: 1
            required: true
            requiredProperties:
              - name
              - url
        examples:
          example:
            value:
              name: My first log drain
              projectIds:
                - <string>
              secret: a1Xsfd325fXcs
              deliveryFormat: json
              url: https://example.com/log-drain
              sources:
                - static
              headers: {}
              environments:
                - preview
    codeSamples:
      - label: createLogDrain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.LogDrains.CreateLogDrain(ctx, nil, nil, &operations.CreateLogDrainRequestBody{\n        Name: \"My first log drain\",\n        Secret: vercel.String(\"a1Xsfd325fXcs\"),\n        DeliveryFormat: operations.DeliveryFormatJSON.ToPointer(),\n        URL: \"https://example.com/log-drain\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createLogDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.logDrains.createLogDrain({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "My first log drain",
                secret: "a1Xsfd325fXcs",
                deliveryFormat: "json",
                url: "https://example.com/log-drain",
              },
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              clientId:
                allOf:
                  - type: string
                    description: >-
                      The oauth2 client application id that created this log
                      drain
                    example: oac_xRhY4LAB7yLhUADD69EvV7ct
              configurationId:
                allOf:
                  - type: string
                    description: The client configuration this log drain was created with
                    example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
              createdAt:
                allOf:
                  - type: number
                    description: A timestamp that tells you when the log drain was created
                    example: 1558531915505
              id:
                allOf:
                  - type: string
                    description: >-
                      The unique identifier of the log drain. Always prefixed
                      with `ld_`
                    example: ld_nBuA7zCID8g4QZ8g
              deliveryFormat:
                allOf:
                  - type: string
                    enum:
                      - json
                      - ndjson
                      - syslog
                      - protobuf
                    description: The delivery log format
                    example: json
              name:
                allOf:
                  - type: string
                    description: The name of the log drain
                    example: My first log drain
              ownerId:
                allOf:
                  - type: string
                    description: >-
                      The identifier of the team or user whose events will
                      trigger the log drain
                    example: kr1PsOIzqEL5Xg6M4VZcZosf
              projectId:
                allOf:
                  - nullable: true
                    type: string
                    example: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
              projectIds:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      The identifier of the projects this log drain is
                      associated with
                    example: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
              url:
                allOf:
                  - type: string
                    description: The URL to call when logs are generated
                    example: https://example.com/log-drain
              sources:
                allOf:
                  - items:
                      type: string
                      enum:
                        - build
                        - edge
                        - lambda
                        - static
                        - external
                        - firewall
                        - redirect
                      description: >-
                        The sources from which logs are currently being
                        delivered to this log drain.
                      example:
                        - build
                        - edge
                    type: array
                    description: >-
                      The sources from which logs are currently being delivered
                      to this log drain.
                    example:
                      - build
                      - edge
              createdFrom:
                allOf:
                  - type: string
                    enum:
                      - integration
                      - self-served
                    description: >-
                      Whether the log drain was created by an integration or by
                      a user
                    example: integration
              headers:
                allOf:
                  - additionalProperties:
                      type: string
                    type: object
                    description: The headers to send with the request
                    example: '{"Authorization": "Bearer 123"}'
              environments:
                allOf:
                  - items:
                      type: string
                      enum:
                        - production
                        - preview
                      description: The environment of log drain
                      example:
                        - production
                    type: array
                    description: The environment of log drain
                    example:
                      - production
              branch:
                allOf:
                  - type: string
                    description: The branch regexp of log drain
                    example: feature/*
              samplingRate:
                allOf:
                  - type: number
                    description: The sampling rate of log drain
                    example: 0.5
              source:
                allOf:
                  - oneOf:
                      - properties:
                          kind:
                            type: string
                            enum:
                              - self-served
                        required:
                          - kind
                        type: object
                      - properties:
                          kind:
                            type: string
                            enum:
                              - integration
                          resourceId:
                            type: string
                          externalResourceId:
                            type: string
                          integrationId:
                            type: string
                          integrationConfigurationId:
                            type: string
                        required:
                          - kind
                          - integrationId
                          - integrationConfigurationId
                        type: object
            requiredProperties:
              - createdAt
              - id
              - name
              - ownerId
              - url
              - source
        examples:
          example:
            value:
              clientId: oac_xRhY4LAB7yLhUADD69EvV7ct
              configurationId: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
              createdAt: 1558531915505
              id: ld_nBuA7zCID8g4QZ8g
              deliveryFormat: json
              name: My first log drain
              ownerId: kr1PsOIzqEL5Xg6M4VZcZosf
              projectId: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
              projectIds: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
              url: https://example.com/log-drain
              sources:
                - build
                - edge
              createdFrom: integration
              headers: '{"Authorization": "Bearer 123"}'
              environments:
                - production
              branch: feature/*
              samplingRate: 0.5
              source:
                kind: self-served
        description: The log drain was successfully created
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              The provided token is not from an OAuth2 Client
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          The provided token is not from an OAuth2 Client
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Deletes a Configurable Log Drain (deprecated)"

last_updated: "2025-11-07T00:37:12.739Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/logdrains/deletes-a-configurable-log-drain-deprecated"
--------------------------------------------------------------------------------

# Deletes a Configurable Log Drain (deprecated)

> Deletes a Configurable Log Drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated team can be deleted.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/log-drains/{id}
paths:
  path: /v1/log-drains/{id}
  method: delete
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: deleteConfigurableLogDrain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.LogDrains.DeleteConfigurableLogDrain(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: deleteConfigurableLogDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.logDrains.deleteConfigurableLogDrain({
              id: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });


          }

          run();
  response:
    '204': {}
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Deletes the Integration log drain with the provided `id` (deprecated)"

last_updated: "2025-11-07T00:37:12.795Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/logdrains/deletes-the-integration-log-drain-with-the-provided-%60id%60-deprecated"
--------------------------------------------------------------------------------

# Deletes the Integration log drain with the provided `id` (deprecated)

> Deletes the Integration log drain with the provided `id`. When using an OAuth2 Token, the log drain can be deleted only if the integration owns it.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/integrations/log-drains/{id}
paths:
  path: /v1/integrations/log-drains/{id}
  method: delete
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: ID of the log drain to be deleted
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: deleteIntegrationLogDrain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.LogDrains.DeleteIntegrationLogDrain(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: deleteIntegrationLogDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.logDrains.deleteIntegrationLogDrain({
              id: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });


          }

          run();
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The log drain was successfully deleted
        examples: {}
        description: The log drain was successfully deleted
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Retrieves a Configurable Log Drain (deprecated)"

last_updated: "2025-11-07T00:37:12.792Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/logdrains/retrieves-a-configurable-log-drain-deprecated"
--------------------------------------------------------------------------------

# Retrieves a Configurable Log Drain (deprecated)

> Retrieves a Configurable Log Drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated team can be accessed.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/log-drains/{id}
paths:
  path: /v1/log-drains/{id}
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getConfigurableLogDrain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.LogDrains.GetConfigurableLogDrain(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getConfigurableLogDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.logDrains.getConfigurableLogDrain({
              id: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              projectsMetadata:
                allOf:
                  - nullable: true
                    items:
                      properties:
                        id:
                          type: string
                        name:
                          type: string
                        framework:
                          nullable: true
                          type: string
                          enum:
                            - blitzjs
                            - nextjs
                            - gatsby
                            - remix
                            - react-router
                            - astro
                            - hexo
                            - eleventy
                            - docusaurus-2
                            - docusaurus
                            - preact
                            - solidstart-1
                            - solidstart
                            - dojo
                            - ember
                            - vue
                            - scully
                            - ionic-angular
                            - angular
                            - polymer
                            - svelte
                            - sveltekit
                            - sveltekit-1
                            - ionic-react
                            - create-react-app
                            - gridsome
                            - umijs
                            - sapper
                            - saber
                            - stencil
                            - nuxtjs
                            - redwoodjs
                            - hugo
                            - jekyll
                            - brunch
                            - middleman
                            - zola
                            - hydrogen
                            - vite
                            - vitepress
                            - vuepress
                            - parcel
                            - fastapi
                            - flask
                            - fasthtml
                            - sanity-v3
                            - sanity
                            - storybook
                            - nitro
                            - hono
                            - express
                            - h3
                            - nestjs
                            - fastify
                            - xmcp
                        latestDeployment:
                          type: string
                      required:
                        - id
                        - name
                      type: object
                    type: array
              integrationIcon:
                allOf:
                  - type: string
              integrationConfigurationUri:
                allOf:
                  - type: string
              integrationWebsite:
                allOf:
                  - type: string
        examples:
          example:
            value:
              projectsMetadata:
                - id: <string>
                  name: <string>
                  framework: blitzjs
                  latestDeployment: <string>
              integrationIcon: <string>
              integrationConfigurationUri: <string>
              integrationWebsite: <string>
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Retrieves a list of all the Log Drains (deprecated)"

last_updated: "2025-11-07T00:37:12.784Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/logdrains/retrieves-a-list-of-all-the-log-drains-deprecated"
--------------------------------------------------------------------------------

# Retrieves a list of all the Log Drains (deprecated)

> Retrieves a list of all the Log Drains owned by the account. This endpoint must be called with an account AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated account can be accessed.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/log-drains
paths:
  path: /v1/log-drains
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path: {}
      query:
        projectId:
          schema:
            - type: string
        includeMetadata:
          schema:
            - type: boolean
              default: false
        projectIdOrName:
          schema:
            - type: string
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getAllLogDrains
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.LogDrains.GetAllLogDrains(ctx, nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.ResponseBodies != nil {\n        // handle response\n    }\n}"
      - label: getAllLogDrains
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.logDrains.getAllLogDrains({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              drains:
                allOf:
                  - oneOf:
                      - items:
                          properties:
                            id:
                              type: string
                            ownerId:
                              type: string
                            name:
                              type: string
                            createdAt:
                              type: number
                            createdFrom:
                              type: string
                              enum:
                                - self-served
                                - integration
                            updatedAt:
                              type: number
                            projectIds:
                              items:
                                type: string
                              type: array
                            schemas:
                              properties:
                                log:
                                  type: object
                                trace:
                                  type: object
                                analytics:
                                  type: object
                                speed_insights:
                                  type: object
                              type: object
                            delivery:
                              oneOf:
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - http
                                    endpoint:
                                      type: string
                                    encoding:
                                      type: string
                                      enum:
                                        - json
                                        - ndjson
                                    compression:
                                      type: string
                                      enum:
                                        - gzip
                                        - none
                                    headers:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - encoding
                                    - headers
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - otlphttp
                                    endpoint:
                                      properties:
                                        traces:
                                          type: string
                                      required:
                                        - traces
                                      type: object
                                    encoding:
                                      type: string
                                      enum:
                                        - json
                                        - proto
                                    headers:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - encoding
                                    - headers
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - syslog
                                    endpoint:
                                      type: string
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - secret
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - clickhouse
                                    endpoint:
                                      type: string
                                    table:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - table
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - internal
                                    target:
                                      type: string
                                      enum:
                                        - vercel-otel-traces-db
                                  required:
                                    - type
                                    - target
                                  type: object
                            sampling:
                              items:
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - head_sampling
                                  rate:
                                    type: number
                                  env:
                                    type: string
                                    enum:
                                      - production
                                      - preview
                                  requestPath:
                                    type: string
                                required:
                                  - type
                                  - rate
                                type: object
                              type: array
                            teamId:
                              nullable: true
                              type: string
                            status:
                              type: string
                              enum:
                                - enabled
                                - disabled
                                - errored
                            disabledAt:
                              type: number
                            disabledReason:
                              type: string
                              enum:
                                - disabled-by-owner
                                - feature-not-available
                                - account-plan-downgrade
                                - disabled-by-admin
                            disabledBy:
                              type: string
                            firstErrorTimestamp:
                              type: number
                            configurationId:
                              type: string
                            clientId:
                              type: string
                            source:
                              oneOf:
                                - properties:
                                    kind:
                                      type: string
                                      enum:
                                        - self-served
                                  required:
                                    - kind
                                  type: object
                                - properties:
                                    kind:
                                      type: string
                                      enum:
                                        - integration
                                    resourceId:
                                      type: string
                                    externalResourceId:
                                      type: string
                                    integrationId:
                                      type: string
                                    integrationConfigurationId:
                                      type: string
                                  required:
                                    - kind
                                    - integrationId
                                    - integrationConfigurationId
                                  type: object
                            filter:
                              type: string
                            filterV2:
                              oneOf:
                                - properties:
                                    version:
                                      type: string
                                      enum:
                                        - v1
                                  required:
                                    - version
                                  type: object
                                - properties:
                                    version:
                                      type: string
                                      enum:
                                        - v2
                                    filter:
                                      oneOf:
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - basic
                                            project:
                                              properties:
                                                ids:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            log:
                                              properties:
                                                sources:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            deployment:
                                              properties:
                                                environments:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                          required:
                                            - type
                                          type: object
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - odata
                                            text:
                                              type: string
                                          required:
                                            - type
                                            - text
                                          type: object
                                  required:
                                    - version
                                    - filter
                                  type: object
                          required:
                            - id
                            - ownerId
                            - name
                            - createdAt
                            - updatedAt
                            - source
                          type: object
                        type: array
                      - items:
                          properties:
                            id:
                              type: string
                            ownerId:
                              type: string
                            name:
                              type: string
                            createdAt:
                              type: number
                            createdFrom:
                              type: string
                              enum:
                                - self-served
                                - integration
                            updatedAt:
                              type: number
                            projectIds:
                              items:
                                type: string
                              type: array
                            schemas:
                              properties:
                                log:
                                  type: object
                                trace:
                                  type: object
                                analytics:
                                  type: object
                                speed_insights:
                                  type: object
                              type: object
                            delivery:
                              oneOf:
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - http
                                    endpoint:
                                      type: string
                                    encoding:
                                      type: string
                                      enum:
                                        - json
                                        - ndjson
                                    compression:
                                      type: string
                                      enum:
                                        - gzip
                                        - none
                                    headers:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - encoding
                                    - headers
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - otlphttp
                                    endpoint:
                                      properties:
                                        traces:
                                          type: string
                                      required:
                                        - traces
                                      type: object
                                    encoding:
                                      type: string
                                      enum:
                                        - json
                                        - proto
                                    headers:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - encoding
                                    - headers
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - syslog
                                    endpoint:
                                      type: string
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - secret
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - clickhouse
                                    endpoint:
                                      type: string
                                    table:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - table
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - internal
                                    target:
                                      type: string
                                      enum:
                                        - vercel-otel-traces-db
                                  required:
                                    - type
                                    - target
                                  type: object
                            sampling:
                              items:
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - head_sampling
                                  rate:
                                    type: number
                                  env:
                                    type: string
                                    enum:
                                      - production
                                      - preview
                                  requestPath:
                                    type: string
                                required:
                                  - type
                                  - rate
                                type: object
                              type: array
                            teamId:
                              nullable: true
                              type: string
                            status:
                              type: string
                              enum:
                                - enabled
                                - disabled
                                - errored
                            disabledAt:
                              type: number
                            disabledReason:
                              type: string
                              enum:
                                - disabled-by-owner
                                - feature-not-available
                                - account-plan-downgrade
                                - disabled-by-admin
                            disabledBy:
                              type: string
                            firstErrorTimestamp:
                              type: number
                            configurationId:
                              type: string
                            clientId:
                              type: string
                            source:
                              oneOf:
                                - properties:
                                    kind:
                                      type: string
                                      enum:
                                        - self-served
                                  required:
                                    - kind
                                  type: object
                                - properties:
                                    kind:
                                      type: string
                                      enum:
                                        - integration
                                    resourceId:
                                      type: string
                                    externalResourceId:
                                      type: string
                                    integrationId:
                                      type: string
                                    integrationConfigurationId:
                                      type: string
                                  required:
                                    - kind
                                    - integrationId
                                    - integrationConfigurationId
                                  type: object
                            filter:
                              type: string
                            filterV2:
                              oneOf:
                                - properties:
                                    version:
                                      type: string
                                      enum:
                                        - v1
                                  required:
                                    - version
                                  type: object
                                - properties:
                                    version:
                                      type: string
                                      enum:
                                        - v2
                                    filter:
                                      oneOf:
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - basic
                                            project:
                                              properties:
                                                ids:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            log:
                                              properties:
                                                sources:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            deployment:
                                              properties:
                                                environments:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                          required:
                                            - type
                                          type: object
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - odata
                                            text:
                                              type: string
                                          required:
                                            - type
                                            - text
                                          type: object
                                  required:
                                    - version
                                    - filter
                                  type: object
                            integrationIcon:
                              type: string
                            integrationConfigurationUri:
                              type: string
                            integrationWebsite:
                              type: string
                            projectsMetadata:
                              items:
                                properties:
                                  id:
                                    type: string
                                  name:
                                    type: string
                                  framework:
                                    nullable: true
                                    type: string
                                    enum:
                                      - blitzjs
                                      - nextjs
                                      - gatsby
                                      - remix
                                      - react-router
                                      - astro
                                      - hexo
                                      - eleventy
                                      - docusaurus-2
                                      - docusaurus
                                      - preact
                                      - solidstart-1
                                      - solidstart
                                      - dojo
                                      - ember
                                      - vue
                                      - scully
                                      - ionic-angular
                                      - angular
                                      - polymer
                                      - svelte
                                      - sveltekit
                                      - sveltekit-1
                                      - ionic-react
                                      - create-react-app
                                      - gridsome
                                      - umijs
                                      - sapper
                                      - saber
                                      - stencil
                                      - nuxtjs
                                      - redwoodjs
                                      - hugo
                                      - jekyll
                                      - brunch
                                      - middleman
                                      - zola
                                      - hydrogen
                                      - vite
                                      - vitepress
                                      - vuepress
                                      - parcel
                                      - fastapi
                                      - flask
                                      - fasthtml
                                      - sanity-v3
                                      - sanity
                                      - storybook
                                      - nitro
                                      - hono
                                      - express
                                      - h3
                                      - nestjs
                                      - fastify
                                      - xmcp
                                  latestDeployment:
                                    type: string
                                required:
                                  - id
                                  - name
                                type: object
                              type: array
                          required:
                            - id
                            - ownerId
                            - name
                            - createdAt
                            - updatedAt
                            - source
                          type: object
                        type: array
            requiredProperties:
              - drains
          - type: array
            items:
              allOf:
                - type: object
                  properties:
                    projectsMetadata:
                      nullable: true
                      items:
                        properties:
                          id:
                            type: string
                          name:
                            type: string
                          framework:
                            nullable: true
                            type: string
                            enum:
                              - blitzjs
                              - nextjs
                              - gatsby
                              - remix
                              - react-router
                              - astro
                              - hexo
                              - eleventy
                              - docusaurus-2
                              - docusaurus
                              - preact
                              - solidstart-1
                              - solidstart
                              - dojo
                              - ember
                              - vue
                              - scully
                              - ionic-angular
                              - angular
                              - polymer
                              - svelte
                              - sveltekit
                              - sveltekit-1
                              - ionic-react
                              - create-react-app
                              - gridsome
                              - umijs
                              - sapper
                              - saber
                              - stencil
                              - nuxtjs
                              - redwoodjs
                              - hugo
                              - jekyll
                              - brunch
                              - middleman
                              - zola
                              - hydrogen
                              - vite
                              - vitepress
                              - vuepress
                              - parcel
                              - fastapi
                              - flask
                              - fasthtml
                              - sanity-v3
                              - sanity
                              - storybook
                              - nitro
                              - hono
                              - express
                              - h3
                              - nestjs
                              - fastify
                              - xmcp
                          latestDeployment:
                            type: string
                        required:
                          - id
                          - name
                        type: object
                      type: array
                    integrationIcon:
                      type: string
                    integrationConfigurationUri:
                      type: string
                    integrationWebsite:
                      type: string
        examples:
          example:
            value:
              drains:
                - id: <string>
                  ownerId: <string>
                  name: <string>
                  createdAt: 123
                  createdFrom: self-served
                  updatedAt: 123
                  projectIds:
                    - <string>
                  schemas:
                    log: {}
                    trace: {}
                    analytics: {}
                    speed_insights: {}
                  delivery:
                    type: http
                    endpoint: <string>
                    encoding: json
                    compression: gzip
                    headers: {}
                    secret: <string>
                  sampling:
                    - type: head_sampling
                      rate: 123
                      env: production
                      requestPath: <string>
                  teamId: <string>
                  status: enabled
                  disabledAt: 123
                  disabledReason: disabled-by-owner
                  disabledBy: <string>
                  firstErrorTimestamp: 123
                  configurationId: <string>
                  clientId: <string>
                  source:
                    kind: self-served
                  filter: <string>
                  filterV2:
                    version: v1
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Retrieves a list of Integration log drains (deprecated)"

last_updated: "2025-11-07T00:37:12.948Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/logdrains/retrieves-a-list-of-integration-log-drains-deprecated"
--------------------------------------------------------------------------------

# Retrieves a list of Integration log drains (deprecated)

> Retrieves a list of all Integration log drains that are defined for the authenticated user or team. When using an OAuth2 token, the list is limited to log drains created by the authenticated integration.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/integrations/log-drains
paths:
  path: /v2/integrations/log-drains
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path: {}
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getIntegrationLogDrains
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.LogDrains.GetIntegrationLogDrains(ctx, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.ResponseBodies != nil {\n        // handle response\n    }\n}"
      - label: getIntegrationLogDrains
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.logDrains.getIntegrationLogDrains({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - properties:
                    clientId:
                      type: string
                      description: >-
                        The oauth2 client application id that created this log
                        drain
                      example: oac_xRhY4LAB7yLhUADD69EvV7ct
                    configurationId:
                      type: string
                      description: The client configuration this log drain was created with
                      example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                    createdAt:
                      type: number
                      description: >-
                        A timestamp that tells you when the log drain was
                        created
                      example: 1558531915505
                    id:
                      type: string
                      description: >-
                        The unique identifier of the log drain. Always prefixed
                        with `ld_`
                      example: ld_nBuA7zCID8g4QZ8g
                    deliveryFormat:
                      type: string
                      enum:
                        - json
                        - ndjson
                        - syslog
                        - protobuf
                      description: The delivery log format
                      example: json
                    name:
                      type: string
                      description: The name of the log drain
                      example: My first log drain
                    ownerId:
                      type: string
                      description: >-
                        The identifier of the team or user whose events will
                        trigger the log drain
                      example: kr1PsOIzqEL5Xg6M4VZcZosf
                    projectId:
                      nullable: true
                      type: string
                      example: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
                    projectIds:
                      items:
                        type: string
                      type: array
                      description: >-
                        The identifier of the projects this log drain is
                        associated with
                      example: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
                    url:
                      type: string
                      description: The URL to call when logs are generated
                      example: https://example.com/log-drain
                    sources:
                      items:
                        type: string
                        enum:
                          - build
                          - edge
                          - lambda
                          - static
                          - external
                          - firewall
                          - redirect
                        description: >-
                          The sources from which logs are currently being
                          delivered to this log drain.
                        example:
                          - build
                          - edge
                      type: array
                      description: >-
                        The sources from which logs are currently being
                        delivered to this log drain.
                      example:
                        - build
                        - edge
                    createdFrom:
                      type: string
                      enum:
                        - integration
                        - self-served
                      description: >-
                        Whether the log drain was created by an integration or
                        by a user
                      example: integration
                    headers:
                      additionalProperties:
                        type: string
                      type: object
                      description: The headers to send with the request
                      example: '{"Authorization": "Bearer 123"}'
                    environments:
                      items:
                        type: string
                        enum:
                          - production
                          - preview
                        description: The environment of log drain
                        example:
                          - production
                      type: array
                      description: The environment of log drain
                      example:
                        - production
                    branch:
                      type: string
                      description: The branch regexp of log drain
                      example: feature/*
                    samplingRate:
                      type: number
                      description: The sampling rate of log drain
                      example: 0.5
                    source:
                      oneOf:
                        - properties:
                            kind:
                              type: string
                              enum:
                                - self-served
                          required:
                            - kind
                          type: object
                        - properties:
                            kind:
                              type: string
                              enum:
                                - integration
                            resourceId:
                              type: string
                            externalResourceId:
                              type: string
                            integrationId:
                              type: string
                            integrationConfigurationId:
                              type: string
                          required:
                            - kind
                            - integrationId
                            - integrationConfigurationId
                          type: object
                  required:
                    - createdAt
                    - id
                    - name
                    - ownerId
                    - url
                    - source
                  type: object
        examples:
          example:
            value:
              - clientId: oac_xRhY4LAB7yLhUADD69EvV7ct
                configurationId: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                createdAt: 1558531915505
                id: ld_nBuA7zCID8g4QZ8g
                deliveryFormat: json
                name: My first log drain
                ownerId: kr1PsOIzqEL5Xg6M4VZcZosf
                projectId: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
                projectIds: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
                url: https://example.com/log-drain
                sources:
                  - build
                  - edge
                createdFrom: integration
                headers: '{"Authorization": "Bearer 123"}'
                environments:
                  - production
                branch: feature/*
                samplingRate: 0.5
                source:
                  kind: self-served
        description: A list of log drains
    '400': {}
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get logs for a deployment"

last_updated: "2025-11-07T00:37:12.859Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/logs/get-logs-for-a-deployment"
--------------------------------------------------------------------------------

# Get logs for a deployment

> Returns a stream of logs for a given deployment.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{projectId}/deployments/{deploymentId}/runtime-logs
paths:
  path: /v1/projects/{projectId}/deployments/{deploymentId}/runtime-logs
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        projectId:
          schema:
            - type: string
              required: true
        deploymentId:
          schema:
            - type: string
              required: true
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getRuntimeLogs
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.logs.getRuntimeLogs({
              projectId: "<id>",
              deploymentId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/stream+json:
        schemaArray:
          - type: object
            properties:
              level:
                allOf:
                  - type: string
                    enum:
                      - error
                      - warning
                      - info
              message:
                allOf:
                  - type: string
              rowId:
                allOf:
                  - type: string
              source:
                allOf:
                  - type: string
                    enum:
                      - delimiter
                      - edge-function
                      - edge-middleware
                      - serverless
                      - request
              timestampInMs:
                allOf:
                  - type: number
              domain:
                allOf:
                  - type: string
              messageTruncated:
                allOf:
                  - type: boolean
              requestMethod:
                allOf:
                  - type: string
              requestPath:
                allOf:
                  - type: string
              responseStatusCode:
                allOf:
                  - type: number
            requiredProperties:
              - level
              - message
              - rowId
              - source
              - timestampInMs
              - domain
              - messageTruncated
              - requestMethod
              - requestPath
              - responseStatusCode
        examples:
          example:
            value:
              level: error
              message: <string>
              rowId: <string>
              source: delimiter
              timestampInMs: 123
              domain: <string>
              messageTruncated: true
              requestMethod: <string>
              requestPath: <string>
              responseStatusCode: 123
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Create Event"

last_updated: "2025-11-07T00:37:12.827Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/create-event"
--------------------------------------------------------------------------------

# Create Event

> Partner notifies Vercel of any changes made to an Installation or a Resource. Vercel is expected to use `list-resources` and other read APIs to get the new state.<br/> <br/> `resource.updated` event should be dispatched when any state of a resource linked to Vercel is modified by the partner.<br/> `installation.updated` event should be dispatched when an installation's billing plan is changed via the provider instead of Vercel.<br/> <br/> Resource update use cases: <br/> <br/> - The user renames a database in the partner’s application. The partner should dispatch a `resource.updated` event to notify Vercel to update the resource in Vercel’s datastores.<br/> - A resource has been suspended due to a lack of use. The partner should dispatch a `resource.updated` event to notify Vercel to update the resource's status in Vercel's datastores.<br/>

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/events
paths:
  path: /v1/installations/{integrationConfigurationId}/events
  method: post
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        integrationConfigurationId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              event:
                allOf:
                  - oneOf:
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - installation.updated
                          billingPlanId:
                            type: string
                            description: The installation-level billing plan ID
                        required:
                          - type
                        additionalProperties: false
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - resource.updated
                          productId:
                            type: string
                            description: Partner-provided product slug or id
                          resourceId:
                            type: string
                            description: Partner provided resource ID
                        required:
                          - type
                          - resourceId
                        additionalProperties: false
            required: true
            requiredProperties:
              - event
            additionalProperties: false
        examples:
          example:
            value:
              event:
                type: installation.updated
                billingPlanId: <string>
    codeSamples:
      - label: create-event
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.createEvent({
              integrationConfigurationId: "<id>",
              requestBody: {
                event: {
                  type: "installation.updated",
                },
              },
            });


          }

          run();
  response:
    '201': {}
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Create one or multiple experimentation items"

last_updated: "2025-11-07T00:37:12.961Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/create-one-or-multiple-experimentation-items"
--------------------------------------------------------------------------------

# Create one or multiple experimentation items

> Create one or multiple experimentation items

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items
  method: post
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        integrationConfigurationId:
          schema:
            - type: string
              required: true
        resourceId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              items:
                allOf:
                  - type: array
                    maxItems: 50
                    items:
                      type: object
                      additionalProperties: false
                      required:
                        - id
                        - slug
                        - origin
                      properties:
                        id:
                          type: string
                          maxLength: 1024
                        slug:
                          type: string
                          maxLength: 1024
                        origin:
                          type: string
                          maxLength: 2048
                        category:
                          type: string
                          enum:
                            - experiment
                            - flag
                        name:
                          type: string
                          maxLength: 1024
                        description:
                          type: string
                          maxLength: 1024
                        isArchived:
                          type: boolean
                        createdAt:
                          type: number
                        updatedAt:
                          type: number
            requiredProperties:
              - items
            additionalProperties: false
        examples:
          example:
            value:
              items:
                - id: <string>
                  slug: <string>
                  origin: <string>
                  category: experiment
                  name: <string>
                  description: <string>
                  isArchived: true
                  createdAt: 123
                  updatedAt: 123
    codeSamples:
      - label: >-
          post_/v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.createInstallationIntegrationConfiguration({
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
            });


          }

          run();
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The items were created
        examples: {}
        description: The items were created
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Delete an existing experimentation item"

last_updated: "2025-11-07T00:37:12.844Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/delete-an-existing-experimentation-item"
--------------------------------------------------------------------------------

# Delete an existing experimentation item

> Delete an existing experimentation item

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
  method: delete
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        integrationConfigurationId:
          schema:
            - type: string
              required: true
        resourceId:
          schema:
            - type: string
              required: true
        itemId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: >-
          delete_/v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.deleteInstallationIntegrationConfiguration({
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
              itemId: "<id>",
            });


          }

          run();
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The item was deleted
        examples: {}
        description: The item was deleted
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Delete Integration Resource"

last_updated: "2025-11-07T00:37:12.832Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/delete-integration-resource"
--------------------------------------------------------------------------------

# Delete Integration Resource

> Delete a resource owned by the selected installation ID.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/installations/{integrationConfigurationId}/resources/{resourceId}
paths:
  path: /v1/installations/{integrationConfigurationId}/resources/{resourceId}
  method: delete
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        integrationConfigurationId:
          schema:
            - type: string
              required: true
        resourceId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: delete-integration-resource
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.deleteIntegrationResource({
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
            });


          }

          run();
  response:
    '204': {}
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get Account Information"

last_updated: "2025-11-07T00:37:12.829Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/get-account-information"
--------------------------------------------------------------------------------

# Get Account Information

> Fetches the best account or user’s contact info

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/account
paths:
  path: /v1/installations/{integrationConfigurationId}/account
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        integrationConfigurationId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: get-account-info
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.getAccountInfo({
              integrationConfigurationId: "<id>",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: The name of the team the installation is tied to.
              url:
                allOf:
                  - type: string
                    description: A URL linking to the installation in the Vercel Dashboard.
              contact:
                allOf:
                  - nullable: true
                    properties:
                      email:
                        type: string
                      name:
                        type: string
                    required:
                      - email
                    type: object
                    description: >-
                      The best contact for the integration, which can change as
                      team members and their roles change.
            requiredProperties:
              - url
              - contact
        examples:
          example:
            value:
              name: <string>
              url: <string>
              contact:
                email: <string>
                name: <string>
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get Integration Resource"

last_updated: "2025-11-07T00:37:12.906Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/get-integration-resource"
--------------------------------------------------------------------------------

# Get Integration Resource

> Get a resource by its partner ID.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/resources/{resourceId}
paths:
  path: /v1/installations/{integrationConfigurationId}/resources/{resourceId}
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        integrationConfigurationId:
          schema:
            - type: string
              required: true
              description: >-
                The ID of the integration configuration (installation) the
                resource belongs to
        resourceId:
          schema:
            - type: string
              required: true
              description: The ID provided by the 3rd party provider for the given resource
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: get-integration-resource
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.getIntegrationResource({
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: >-
                      The ID provided by the 3rd party provider for the given
                      resource
              internalId:
                allOf:
                  - type: string
                    description: The ID assigned by Vercel for the given resource
              name:
                allOf:
                  - type: string
                    description: The name of the resource as it is recorded in Vercel
              status:
                allOf:
                  - type: string
                    enum:
                      - ready
                      - pending
                      - onboarding
                      - suspended
                      - resumed
                      - uninstalled
                      - error
                    description: The current status of the resource
              productId:
                allOf:
                  - type: string
                    description: The ID of the product the resource is derived from
              protocolSettings:
                allOf:
                  - properties:
                      experimentation:
                        properties:
                          edgeConfigSyncingEnabled:
                            type: boolean
                          edgeConfigId:
                            type: string
                          edgeConfigTokenId:
                            type: string
                        type: object
                    type: object
                    description: >-
                      Any settings provided for the resource to support its
                      product's protocols
              notification:
                allOf:
                  - properties:
                      level:
                        type: string
                        enum:
                          - error
                          - info
                          - warn
                      title:
                        type: string
                      message:
                        type: string
                      href:
                        type: string
                    required:
                      - level
                      - title
                    type: object
                    description: >-
                      The notification, if set, displayed to the user when
                      viewing the resource in Vercel
              billingPlanId:
                allOf:
                  - type: string
                    description: >-
                      The ID of the billing plan the resource is subscribed to,
                      if applicable
              metadata:
                allOf:
                  - additionalProperties:
                      oneOf:
                        - type: string
                        - type: number
                        - type: boolean
                        - items:
                            type: string
                          type: array
                          description: >-
                            The configured metadata for the resource as defined
                            by its product's Metadata Schema
                        - items:
                            type: number
                          type: array
                          description: >-
                            The configured metadata for the resource as defined
                            by its product's Metadata Schema
                    type: object
                    description: >-
                      The configured metadata for the resource as defined by its
                      product's Metadata Schema
            requiredProperties:
              - id
              - internalId
              - name
              - productId
        examples:
          example:
            value:
              id: <string>
              internalId: <string>
              name: <string>
              status: ready
              productId: <string>
              protocolSettings:
                experimentation:
                  edgeConfigSyncingEnabled: true
                  edgeConfigId: <string>
                  edgeConfigTokenId: <string>
              notification:
                level: error
                title: <string>
                message: <string>
                href: <string>
              billingPlanId: <string>
              metadata: {}
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get Integration Resources"

last_updated: "2025-11-07T00:37:12.973Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/get-integration-resources"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./24-retrieve-custom-environments.md) | [Index](./index.md) | [Next →](./26-get-integration-resources.md)
