**Navigation:** [← Previous](./25-list-products-for-integration-configuration.md) | [Index](./index.md) | [Next →](./27-create-a-new-project.md)

---

# Get Integration Resources

> Get all resources for a given installation ID.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/resources
paths:
  path: /v1/installations/{integrationConfigurationId}/resources
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
      - label: get-integration-resources
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.getIntegrationResources({
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
              resources:
                allOf:
                  - items:
                      properties:
                        partnerId:
                          type: string
                          description: >-
                            The ID provided by the partner for the given
                            resource
                        internalId:
                          type: string
                          description: The ID assigned by Vercel for the given resource
                        name:
                          type: string
                          description: The name of the resource as it is recorded in Vercel
                        status:
                          type: string
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
                          type: string
                          description: The ID of the product the resource is derived from
                        protocolSettings:
                          properties:
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
                            Any settings provided for the resource to support
                            its product's protocols
                        notification:
                          properties:
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
                          type: string
                          description: >-
                            The ID of the billing plan the resource is
                            subscribed to, if applicable
                        metadata:
                          additionalProperties:
                            oneOf:
                              - type: string
                              - type: number
                              - type: boolean
                              - items:
                                  type: string
                                type: array
                                description: >-
                                  The configured metadata for the resource as
                                  defined by its product's Metadata Schema
                              - items:
                                  type: number
                                type: array
                                description: >-
                                  The configured metadata for the resource as
                                  defined by its product's Metadata Schema
                          type: object
                          description: >-
                            The configured metadata for the resource as defined
                            by its product's Metadata Schema
                      required:
                        - partnerId
                        - internalId
                        - name
                        - productId
                      type: object
                    type: array
            requiredProperties:
              - resources
        examples:
          example:
            value:
              resources:
                - partnerId: <string>
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
title: "Get Invoice"

last_updated: "2025-11-07T00:37:13.432Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/get-invoice"
--------------------------------------------------------------------------------

# Get Invoice

> Get Invoice details and status for a given invoice ID.<br/> <br/> See Billing Events with Webhooks documentation on how to receive invoice events. This endpoint is used to retrieve the invoice details.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}
paths:
  path: /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}
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
        invoiceId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: get-invoice
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.getInvoice({
              integrationConfigurationId: "<id>",
              invoiceId: "<id>",
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
              test:
                allOf:
                  - type: boolean
                    description: >-
                      Whether the invoice is in the testmode (no real
                      transaction created).
              invoiceId:
                allOf:
                  - type: string
                    description: Vercel Marketplace Invoice ID.
              externalId:
                allOf:
                  - type: string
                    description: Partner-supplied Invoice ID, if applicable.
              state:
                allOf:
                  - type: string
                    enum:
                      - draft
                      - pending
                      - scheduled
                      - invoiced
                      - paid
                      - notpaid
                      - refund_requested
                      - refunded
                    description: Invoice state.
              invoiceNumber:
                allOf:
                  - type: string
                    description: User-readable invoice number.
              invoiceDate:
                allOf:
                  - type: string
                    description: Invoice date. ISO 8601 timestamp.
              period:
                allOf:
                  - properties:
                      start:
                        type: string
                      end:
                        type: string
                    required:
                      - start
                      - end
                    type: object
                    description: >-
                      Subscription period for this billing cycle. ISO 8601
                      timestamps.
              memo:
                allOf:
                  - type: string
                    description: Additional memo for the invoice.
              items:
                allOf:
                  - items:
                      properties:
                        billingPlanId:
                          type: string
                          description: Partner's billing plan ID.
                        resourceId:
                          type: string
                          description: >-
                            Partner's resource ID. If not specified, indicates
                            installation-wide item.
                        start:
                          type: string
                          description: >-
                            Start and end are only needed if different from the
                            period's start/end. ISO 8601 timestamp.
                        end:
                          type: string
                          description: >-
                            Start and end are only needed if different from the
                            period's start/end. ISO 8601 timestamp.
                        name:
                          type: string
                          description: Invoice item name.
                        details:
                          type: string
                          description: Additional item details.
                        price:
                          type: string
                          description: Item price. A dollar-based decimal string.
                        quantity:
                          type: number
                          description: Item quantity.
                        units:
                          type: string
                          description: Units for item's quantity.
                        total:
                          type: string
                          description: Item total. A dollar-based decimal string.
                      required:
                        - billingPlanId
                        - name
                        - price
                        - quantity
                        - units
                        - total
                      type: object
                      description: Invoice items.
                    type: array
                    description: Invoice items.
              discounts:
                allOf:
                  - items:
                      properties:
                        billingPlanId:
                          type: string
                          description: Partner's billing plan ID.
                        resourceId:
                          type: string
                          description: >-
                            Partner's resource ID. If not specified, indicates
                            installation-wide discount.
                        start:
                          type: string
                          description: >-
                            Start and end are only needed if different from the
                            period's start/end. ISO 8601 timestamp.
                        end:
                          type: string
                          description: >-
                            Start and end are only needed if different from the
                            period's start/end. ISO 8601 timestamp.
                        name:
                          type: string
                          description: Discount name.
                        details:
                          type: string
                          description: Additional discount details.
                        amount:
                          type: string
                          description: Discount amount. A dollar-based decimal string.
                      required:
                        - billingPlanId
                        - name
                        - amount
                      type: object
                      description: Invoice discounts.
                    type: array
                    description: Invoice discounts.
              total:
                allOf:
                  - type: string
                    description: Invoice total amount. A dollar-based decimal string.
              refundReason:
                allOf:
                  - type: string
                    description: >-
                      The reason for refund. Only applicable for states
                      "refunded" or "refund_request".
              refundTotal:
                allOf:
                  - type: string
                    description: >-
                      Refund amount. Only applicable for states "refunded" or
                      "refund_request". A dollar-based decimal string.
              created:
                allOf:
                  - type: string
                    description: System creation date. ISO 8601 timestamp.
              updated:
                allOf:
                  - type: string
                    description: System update date. ISO 8601 timestamp.
            requiredProperties:
              - invoiceId
              - state
              - invoiceDate
              - period
              - items
              - total
              - created
              - updated
        examples:
          example:
            value:
              test: true
              invoiceId: <string>
              externalId: <string>
              state: draft
              invoiceNumber: <string>
              invoiceDate: <string>
              period:
                start: <string>
                end: <string>
              memo: <string>
              items:
                - billingPlanId: <string>
                  resourceId: <string>
                  start: <string>
                  end: <string>
                  name: <string>
                  details: <string>
                  price: <string>
                  quantity: 123
                  units: <string>
                  total: <string>
              discounts:
                - billingPlanId: <string>
                  resourceId: <string>
                  start: <string>
                  end: <string>
                  name: <string>
                  details: <string>
                  amount: <string>
              total: <string>
              refundReason: <string>
              refundTotal: <string>
              created: <string>
              updated: <string>
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
title: "Get Member Information"

last_updated: "2025-11-07T00:37:13.541Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/get-member-information"
--------------------------------------------------------------------------------

# Get Member Information

> Returns the member role and other information for a given member ID ("user_id" claim in the SSO OIDC token).

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/member/{memberId}
paths:
  path: /v1/installations/{integrationConfigurationId}/member/{memberId}
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
        memberId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: get-member
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.getMember({
              integrationConfigurationId: "<id>",
              memberId: "<id>",
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
              role:
                allOf:
                  - type: string
                    enum:
                      - ADMIN
                      - USER
                    description: >-
                      "The `ADMIN` role, by default, is provided to users
                      capable of installing integrations, while the `USER` role
                      can be granted to Vercel users with the Vercel `Billing`
                      or Vercel `Viewer` role, which are considered to be
                      Read-Only roles."
            requiredProperties:
              - id
              - role
        examples:
          example:
            value:
              id: <string>
              role: ADMIN
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
title: "Get the data of a user-provided Edge Config"

last_updated: "2025-11-07T00:37:13.522Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/get-the-data-of-a-user-provided-edge-config"
--------------------------------------------------------------------------------

# Get the data of a user-provided Edge Config

> When the user enabled Edge Config syncing, then this endpoint can be used by the partner to fetch the contents of the Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples head /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config
  method: head
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
      - label: >-
          head_/v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.createInstallationIntegrationEdgeConfig({
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
              items:
                allOf:
                  - additionalProperties:
                      $ref: '#/components/schemas/EdgeConfigItemValue'
                    type: object
              updatedAt:
                allOf:
                  - type: number
              digest:
                allOf:
                  - type: string
            requiredProperties:
              - items
              - updatedAt
              - digest
        examples:
          example:
            value:
              items: {}
              updatedAt: 123
              digest: <string>
        description: The Edge Config data
    '304': {}
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
  schemas:
    EdgeConfigItemValue:
      nullable: true
      oneOf:
        - type: string
        - type: number
        - type: boolean
        - additionalProperties:
            $ref: '#/components/schemas/EdgeConfigItemValue'
          type: object
        - items:
            $ref: '#/components/schemas/EdgeConfigItemValue'
          type: array

````

--------------------------------------------------------------------------------
title: "Import Resource"

last_updated: "2025-11-07T00:37:13.281Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/import-resource"
--------------------------------------------------------------------------------

# Import Resource

> This endpoint imports (upserts) a resource to Vercel's installation. This may be needed if resources can be independently created on the partner's side and need to be synchronized to Vercel.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/installations/{integrationConfigurationId}/resources/{resourceId}
paths:
  path: /v1/installations/{integrationConfigurationId}/resources/{resourceId}
  method: put
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
              ownership:
                allOf:
                  - type: string
                    enum:
                      - owned
                      - linked
                      - sandbox
              productId:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
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
              metadata:
                allOf:
                  - type: object
                    additionalProperties: true
              billingPlan:
                allOf:
                  - type: object
                    required:
                      - id
                      - type
                      - name
                    properties:
                      id:
                        type: string
                      type:
                        type: string
                        enum:
                          - prepayment
                          - subscription
                      name:
                        type: string
                      description:
                        type: string
                      paymentMethodRequired:
                        type: boolean
                      cost:
                        type: string
                      details:
                        type: array
                        items:
                          type: object
                          properties:
                            label:
                              type: string
                            value:
                              type: string
                          required:
                            - label
                          additionalProperties: false
                      highlightedDetails:
                        type: array
                        items:
                          type: object
                          properties:
                            label:
                              type: string
                            value:
                              type: string
                          required:
                            - label
                          additionalProperties: false
                      effectiveDate:
                        type: string
                    additionalProperties: true
              notification:
                allOf:
                  - type: object
                    required:
                      - level
                      - title
                    properties:
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
                        format: uri
              extras:
                allOf:
                  - type: object
                    additionalProperties: true
              secrets:
                allOf:
                  - type: array
                    items:
                      type: object
                      required:
                        - name
                        - value
                      properties:
                        name:
                          type: string
                        value:
                          type: string
                        prefix:
                          type: string
                        environmentOverrides:
                          type: object
                          description: >-
                            A map of environments to override values for the
                            secret, used for setting different values across
                            deployments in production, preview, and development
                            environments. Note: the same value will be used for
                            all deployments in the given environment.
                          properties:
                            development:
                              type: string
                              description: Value used for development environment.
                            preview:
                              type: string
                              description: Value used for preview environment.
                            production:
                              type: string
                              description: Value used for production environment.
                      additionalProperties: false
            requiredProperties:
              - productId
              - name
              - status
            additionalProperties: false
        examples:
          example:
            value:
              ownership: owned
              productId: <string>
              name: <string>
              status: ready
              metadata: {}
              billingPlan:
                id: <string>
                type: prepayment
                name: <string>
                description: <string>
                paymentMethodRequired: true
                cost: <string>
                details:
                  - label: <string>
                    value: <string>
                highlightedDetails:
                  - label: <string>
                    value: <string>
                effectiveDate: <string>
              notification:
                level: info
                title: <string>
                message: <string>
                href: <string>
              extras: {}
              secrets:
                - name: <string>
                  value: <string>
                  prefix: <string>
                  environmentOverrides:
                    development: <string>
                    preview: <string>
                    production: <string>
    codeSamples:
      - label: import-resource
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.importResource({
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
              name:
                allOf:
                  - type: string
            requiredProperties:
              - name
        examples:
          example:
            value:
              name: <string>
        description: ''
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
    '409': {}
    '422': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Invoice Actions"

last_updated: "2025-11-07T00:37:13.416Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/invoice-actions"
--------------------------------------------------------------------------------

# Invoice Actions

> This endpoint allows the partner to request a refund for an invoice to Vercel. The invoice is created using the [Submit Invoice API](#submit-invoice-api).

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}/actions
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}/actions
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
        invoiceId:
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
              action:
                allOf:
                  - type: string
                    enum:
                      - refund
              reason:
                allOf:
                  - type: string
                    description: Refund reason.
              total:
                allOf:
                  - description: >-
                      The total amount to be refunded. Must be less than or
                      equal to the total amount of the invoice.
                    type: string
                    pattern: ^[0-9]+(\\.[0-9]+)?$
            required: true
            requiredProperties:
              - action
              - reason
              - total
            additionalProperties: false
        examples:
          example:
            value:
              action: refund
              reason: <string>
              total: <string>
    codeSamples:
      - label: update-invoice
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.updateInvoice({
              integrationConfigurationId: "<id>",
              invoiceId: "<id>",
              requestBody: {
                action: "refund",
                reason: "<value>",
                total: "<value>",
              },
            });


          }

          run();
  response:
    '204': {}
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
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Patch an existing experimentation item"

last_updated: "2025-11-07T00:37:13.236Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/patch-an-existing-experimentation-item"
--------------------------------------------------------------------------------

# Patch an existing experimentation item

> Patch an existing experimentation item

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
  method: patch
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              slug:
                allOf:
                  - type: string
                    maxLength: 1024
              origin:
                allOf:
                  - type: string
                    maxLength: 2048
              name:
                allOf:
                  - type: string
                    maxLength: 1024
              category:
                allOf:
                  - type: string
                    enum:
                      - experiment
                      - flag
              description:
                allOf:
                  - type: string
                    maxLength: 1024
              isArchived:
                allOf:
                  - type: boolean
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
            requiredProperties:
              - slug
              - origin
            additionalProperties: false
        examples:
          example:
            value:
              slug: <string>
              origin: <string>
              name: <string>
              category: experiment
              description: <string>
              isArchived: true
              createdAt: 123
              updatedAt: 123
    codeSamples:
      - label: >-
          patch_/v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.updateInstallationIntegrationConfiguration({
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
            description: The item was updated
        examples: {}
        description: The item was updated
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
title: "Push data into a user-provided Edge Config"

last_updated: "2025-11-07T00:37:13.290Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/push-data-into-a-user-provided-edge-config"
--------------------------------------------------------------------------------

# Push data into a user-provided Edge Config

> When the user enabled Edge Config syncing, then this endpoint can be used by the partner to push their configuration data into the relevant Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config
  method: put
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
              data:
                allOf:
                  - type: object
                    additionalProperties: {}
            requiredProperties:
              - data
            additionalProperties: false
        examples:
          example:
            value:
              data: {}
    codeSamples:
      - label: >-
          put_/v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.updateInstallationIntegrationEdgeConfig({
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
              items:
                allOf:
                  - additionalProperties:
                      $ref: '#/components/schemas/EdgeConfigItemValue'
                    type: object
              updatedAt:
                allOf:
                  - type: number
              digest:
                allOf:
                  - type: string
            requiredProperties:
              - items
              - updatedAt
              - digest
        examples:
          example:
            value:
              items: {}
              updatedAt: 123
              digest: <string>
        description: The Edge Config was updated
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
    '409': {}
    '412': {}
  deprecated: false
  type: path
components:
  schemas:
    EdgeConfigItemValue:
      nullable: true
      oneOf:
        - type: string
        - type: number
        - type: boolean
        - additionalProperties:
            $ref: '#/components/schemas/EdgeConfigItemValue'
          type: object
        - items:
            $ref: '#/components/schemas/EdgeConfigItemValue'
          type: array

````

--------------------------------------------------------------------------------
title: "Submit Billing Data"

last_updated: "2025-11-07T00:37:13.237Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/submit-billing-data"
--------------------------------------------------------------------------------

# Submit Billing Data

> Sends the billing and usage data. The partner should do this at least once a day and ideally once per hour. <br/> Use the `credentials.access_token` we provided in the [Upsert Installation](#upsert-installation) body to authorize this request.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing
paths:
  path: /v1/installations/{integrationConfigurationId}/billing
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
              timestamp:
                allOf:
                  - description: >-
                      Server time of your integration, used to determine the
                      most recent data for race conditions & updates. Only the
                      latest usage data for a given day, week, and month will be
                      kept.
                    type: string
                    format: date-time
              eod:
                allOf:
                  - description: >-
                      End of Day, the UTC datetime for when the end of the
                      billing/usage day is in UTC time. This tells us which day
                      the usage data is for, and also allows for your \"end of
                      day\" to be different from UTC 00:00:00. eod must be
                      within the period dates, and cannot be older than 24h
                      earlier from our server's current time.
                    type: string
                    format: date-time
              period:
                allOf:
                  - type: object
                    description: >-
                      Period for the billing cycle. The period end date cannot
                      be older than 24 hours earlier than our current server's
                      time.
                    properties:
                      start:
                        type: string
                        format: date-time
                      end:
                        type: string
                        format: date-time
                    required:
                      - start
                      - end
                    additionalProperties: false
              billing:
                allOf:
                  - description: Billing data (interim invoicing data).
                    oneOf:
                      - type: array
                        items:
                          type: object
                          properties:
                            billingPlanId:
                              type: string
                              description: Partner's billing plan ID.
                            resourceId:
                              type: string
                              description: Partner's resource ID.
                            start:
                              description: >-
                                Start and end are only needed if different from
                                the period's start/end.
                              type: string
                              format: date-time
                            end:
                              description: >-
                                Start and end are only needed if different from
                                the period's start/end.
                              type: string
                              format: date-time
                            name:
                              type: string
                              description: Line item name.
                            details:
                              type: string
                              description: Line item details.
                            price:
                              description: Price per unit.
                              type: string
                              pattern: ^[0-9]+(\\.[0-9]+)?$
                            quantity:
                              type: number
                              description: Quantity of units.
                            units:
                              type: string
                              description: Units of the quantity.
                            total:
                              description: Total amount.
                              type: string
                              pattern: ^[0-9]+(\\.[0-9]+)?$
                          required:
                            - billingPlanId
                            - name
                            - price
                            - quantity
                            - units
                            - total
                          additionalProperties: false
                      - type: object
                        properties:
                          items:
                            type: array
                            items:
                              type: object
                              properties:
                                billingPlanId:
                                  type: string
                                  description: Partner's billing plan ID.
                                resourceId:
                                  type: string
                                  description: Partner's resource ID.
                                start:
                                  description: >-
                                    Start and end are only needed if different
                                    from the period's start/end.
                                  type: string
                                  format: date-time
                                end:
                                  description: >-
                                    Start and end are only needed if different
                                    from the period's start/end.
                                  type: string
                                  format: date-time
                                name:
                                  type: string
                                  description: Line item name.
                                details:
                                  type: string
                                  description: Line item details.
                                price:
                                  description: Price per unit.
                                  type: string
                                  pattern: ^[0-9]+(\\.[0-9]+)?$
                                quantity:
                                  type: number
                                  description: Quantity of units.
                                units:
                                  type: string
                                  description: Units of the quantity.
                                total:
                                  description: Total amount.
                                  type: string
                                  pattern: ^[0-9]+(\\.[0-9]+)?$
                              required:
                                - billingPlanId
                                - name
                                - price
                                - quantity
                                - units
                                - total
                              additionalProperties: false
                          discounts:
                            type: array
                            items:
                              type: object
                              properties:
                                billingPlanId:
                                  type: string
                                  description: Partner's billing plan ID.
                                resourceId:
                                  type: string
                                  description: Partner's resource ID.
                                start:
                                  description: >-
                                    Start and end are only needed if different
                                    from the period's start/end.
                                  type: string
                                  format: date-time
                                end:
                                  description: >-
                                    Start and end are only needed if different
                                    from the period's start/end.
                                  type: string
                                  format: date-time
                                name:
                                  type: string
                                  description: Discount name.
                                details:
                                  type: string
                                  description: Discount details.
                                amount:
                                  description: Discount amount.
                                  type: string
                                  pattern: ^[0-9]+(\\.[0-9]+)?$
                              required:
                                - billingPlanId
                                - name
                                - amount
                              additionalProperties: false
                        required:
                          - items
              usage:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        resourceId:
                          type: string
                          description: Partner's resource ID.
                        name:
                          type: string
                          description: Metric name.
                        type:
                          type: string
                          description: >-
                            \n              Type of the metric.\n              -
                            total: measured total value, such as Database
                            size\n              - interval: usage during the
                            period, such as i/o or number of
                            queries.\n              - rate: rate of usage, such
                            as queries per second.\n            
                          enum:
                            - total
                            - interval
                            - rate
                        units:
                          type: string
                          description: 'Metric units. Example: \"GB\"'
                        dayValue:
                          type: number
                          description: >-
                            Metric value for the day. Could be a final or an
                            interim value for the day.
                        periodValue:
                          type: number
                          description: >-
                            Metric value for the billing period. Could be a
                            final or an interim value for the period.
                        planValue:
                          type: number
                          description: >-
                            The limit value of the metric for a billing period,
                            if a limit is defined by the plan.
                      required:
                        - name
                        - type
                        - units
                        - dayValue
                        - periodValue
                      additionalProperties: false
            required: true
            requiredProperties:
              - timestamp
              - eod
              - period
              - billing
              - usage
            additionalProperties: false
        examples:
          example:
            value:
              timestamp: '2023-11-07T05:31:56Z'
              eod: '2023-11-07T05:31:56Z'
              period:
                start: '2023-11-07T05:31:56Z'
                end: '2023-11-07T05:31:56Z'
              billing:
                - billingPlanId: <string>
                  resourceId: <string>
                  start: '2023-11-07T05:31:56Z'
                  end: '2023-11-07T05:31:56Z'
                  name: <string>
                  details: <string>
                  price: <string>
                  quantity: 123
                  units: <string>
                  total: <string>
              usage:
                - resourceId: <string>
                  name: <string>
                  type: total
                  units: <string>
                  dayValue: 123
                  periodValue: 123
                  planValue: 123
    codeSamples:
      - label: submit-billing-data
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.submitBillingData({
              integrationConfigurationId: "<id>",
              requestBody: {
                timestamp: new Date("2023-11-26T05:03:03.977Z"),
                eod: new Date("2023-04-14T04:58:49.647Z"),
                period: {
                  start: new Date("2023-03-12T13:32:00.895Z"),
                  end: new Date("2023-12-15T15:17:13.187Z"),
                },
                billing: [
                  {
                    billingPlanId: "<id>",
                    name: "<value>",
                    price: "694.00",
                    quantity: 228.64,
                    units: "<value>",
                    total: "<value>",
                  },
                ],
                usage: [
                  {
                    name: "<value>",
                    type: "interval",
                    units: "<value>",
                    dayValue: 5212.43,
                    periodValue: 4147.35,
                  },
                ],
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
title: "Submit Invoice"

last_updated: "2025-11-07T00:37:13.339Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/submit-invoice"
--------------------------------------------------------------------------------

# Submit Invoice

> This endpoint allows the partner to submit an invoice to Vercel. The invoice is created in Vercel's billing system and sent to the customer. Depending on the type of billing plan, the invoice can be sent at a time of signup, at the start of the billing period, or at the end of the billing period.<br/> <br/> Use the `credentials.access_token` we provided in the [Upsert Installation](#upsert-installation) body to authorize this request. <br/> There are several limitations to the invoice submission:<br/> <br/> 1. A resource can only be billed once per the billing period and the billing plan.<br/> 2. The billing plan used to bill the resource must have been active for this resource during the billing period.<br/> 3. The billing plan used must be a subscription plan.<br/> 4. The interim usage data must be sent hourly for all types of subscriptions. See [Send subscription billing and usage data](#send-subscription-billing-and-usage-data) API on how to send interim billing and usage data.<br/>

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing/invoices
paths:
  path: /v1/installations/{integrationConfigurationId}/billing/invoices
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
              externalId:
                allOf:
                  - type: string
              invoiceDate:
                allOf:
                  - description: Invoice date. Must be within the period's start and end.
                    type: string
                    format: date-time
              memo:
                allOf:
                  - type: string
                    description: Additional memo for the invoice.
              period:
                allOf:
                  - type: object
                    description: Subscription period for this billing cycle.
                    properties:
                      start:
                        type: string
                        format: date-time
                      end:
                        type: string
                        format: date-time
                    required:
                      - start
                      - end
                    additionalProperties: false
              items:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        resourceId:
                          type: string
                          description: Partner's resource ID.
                        billingPlanId:
                          type: string
                          description: Partner's billing plan ID.
                        start:
                          description: >-
                            Start and end are only needed if different from the
                            period's start/end.
                          type: string
                          format: date-time
                        end:
                          description: >-
                            Start and end are only needed if different from the
                            period's start/end.
                          type: string
                          format: date-time
                        name:
                          type: string
                        details:
                          type: string
                        price:
                          type: string
                          pattern: ^[0-9]+(\\.[0-9]+)?$
                          description: Currency amount as a decimal string.
                        quantity:
                          type: number
                        units:
                          type: string
                        total:
                          type: string
                          pattern: ^[0-9]+(\\.[0-9]+)?$
                          description: Currency amount as a decimal string.
                      required:
                        - billingPlanId
                        - name
                        - price
                        - quantity
                        - units
                        - total
                      additionalProperties: false
              discounts:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        resourceId:
                          type: string
                          description: Partner's resource ID.
                        billingPlanId:
                          type: string
                          description: Partner's billing plan ID.
                        start:
                          description: >-
                            Start and end are only needed if different from the
                            period's start/end.
                          type: string
                          format: date-time
                        end:
                          description: >-
                            Start and end are only needed if different from the
                            period's start/end.
                          type: string
                          format: date-time
                        name:
                          type: string
                        details:
                          type: string
                        amount:
                          type: string
                          pattern: ^[0-9]+(\\.[0-9]+)?$
                          description: Currency amount as a decimal string.
                      required:
                        - billingPlanId
                        - name
                        - amount
                      additionalProperties: false
              test:
                allOf:
                  - type: object
                    description: Test mode
                    properties:
                      validate:
                        type: boolean
                      result:
                        type: string
                        enum:
                          - paid
                          - notpaid
                    additionalProperties: false
            required: true
            requiredProperties:
              - invoiceDate
              - period
              - items
            additionalProperties: false
        examples:
          example:
            value:
              externalId: <string>
              invoiceDate: '2023-11-07T05:31:56Z'
              memo: <string>
              period:
                start: '2023-11-07T05:31:56Z'
                end: '2023-11-07T05:31:56Z'
              items:
                - resourceId: <string>
                  billingPlanId: <string>
                  start: '2023-11-07T05:31:56Z'
                  end: '2023-11-07T05:31:56Z'
                  name: <string>
                  details: <string>
                  price: <string>
                  quantity: 123
                  units: <string>
                  total: <string>
              discounts:
                - resourceId: <string>
                  billingPlanId: <string>
                  start: '2023-11-07T05:31:56Z'
                  end: '2023-11-07T05:31:56Z'
                  name: <string>
                  details: <string>
                  amount: <string>
              test:
                validate: true
                result: paid
    codeSamples:
      - label: submit-invoice
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.submitInvoice({
              integrationConfigurationId: "<id>",
              requestBody: {
                invoiceDate: new Date("2023-12-12T13:24:35.882Z"),
                period: {
                  start: new Date("2024-10-20T02:46:19.279Z"),
                  end: new Date("2025-06-06T21:30:28.107Z"),
                },
                items: [
                  {
                    billingPlanId: "<id>",
                    name: "<value>",
                    price: "469.29",
                    quantity: 3808.42,
                    units: "<value>",
                    total: "<value>",
                  },
                ],
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
              invoiceId:
                allOf:
                  - type: string
              test:
                allOf:
                  - type: boolean
              validationErrors:
                allOf:
                  - items:
                      type: string
                    type: array
        examples:
          example:
            value:
              invoiceId: <string>
              test: true
              validationErrors:
                - <string>
        description: ''
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
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Submit Prepayment Balances"

last_updated: "2025-11-07T00:37:13.376Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/submit-prepayment-balances"
--------------------------------------------------------------------------------

# Submit Prepayment Balances

> Sends the prepayment balances. The partner should do this at least once a day and ideally once per hour. <br/> Use the `credentials.access_token` we provided in the [Upsert Installation](#upsert-installation) body to authorize this request.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing/balance
paths:
  path: /v1/installations/{integrationConfigurationId}/billing/balance
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
              timestamp:
                allOf:
                  - description: >-
                      Server time of your integration, used to determine the
                      most recent data for race conditions & updates. Only the
                      latest usage data for a given day, week, and month will be
                      kept.
                    type: string
                    format: date-time
              balances:
                allOf:
                  - type: array
                    items:
                      type: object
                      description: A credit balance for a particular token type
                      properties:
                        resourceId:
                          type: string
                          description: >-
                            Partner's resource ID, exclude if credits are tied
                            to the installation and not an individual resource.
                        credit:
                          type: string
                          description: >-
                            A human-readable description of the credits the user
                            currently has, e.g. \"2,000 Tokens\"
                        nameLabel:
                          type: string
                          description: >-
                            The name of the credits, for display purposes, e.g.
                            \"Tokens\"
                        currencyValueInCents:
                          type: number
                          description: >-
                            The dollar value of the credit balance, in USD and
                            provided in cents, which is used to trigger
                            automatic purchase thresholds.
                      required:
                        - currencyValueInCents
                      additionalProperties: false
            requiredProperties:
              - timestamp
              - balances
            additionalProperties: false
        examples:
          example:
            value:
              timestamp: '2023-11-07T05:31:56Z'
              balances:
                - resourceId: <string>
                  credit: <string>
                  nameLabel: <string>
                  currencyValueInCents: 123
    codeSamples:
      - label: submit-prepayment-balances
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.submitPrepaymentBalances({
              integrationConfigurationId: "<id>",
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
title: "Update Installation"

last_updated: "2025-11-07T00:37:13.439Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/update-installation"
--------------------------------------------------------------------------------

# Update Installation

> This endpoint updates an integration installation.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/installations/{integrationConfigurationId}
paths:
  path: /v1/installations/{integrationConfigurationId}
  method: patch
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
              billingPlan:
                allOf:
                  - type: object
                    required:
                      - id
                      - type
                      - name
                    properties:
                      id:
                        type: string
                      type:
                        type: string
                        enum:
                          - prepayment
                          - subscription
                      name:
                        type: string
                      description:
                        type: string
                      paymentMethodRequired:
                        type: boolean
                      cost:
                        type: string
                      details:
                        type: array
                        items:
                          type: object
                          properties:
                            label:
                              type: string
                            value:
                              type: string
                          required:
                            - label
                          additionalProperties: false
                      highlightedDetails:
                        type: array
                        items:
                          type: object
                          properties:
                            label:
                              type: string
                            value:
                              type: string
                          required:
                            - label
                          additionalProperties: false
                      effectiveDate:
                        type: string
                    additionalProperties: true
              notification:
                allOf:
                  - oneOf:
                      - type: object
                        required:
                          - level
                          - title
                        properties:
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
                            format: uri
                      - type: string
                    description: >-
                      A notification to display to your customer. Send `null` to
                      clear the current notification.
            additionalProperties: false
        examples:
          example:
            value:
              billingPlan:
                id: <string>
                type: prepayment
                name: <string>
                description: <string>
                paymentMethodRequired: true
                cost: <string>
                details:
                  - label: <string>
                    value: <string>
                highlightedDetails:
                  - label: <string>
                    value: <string>
                effectiveDate: <string>
              notification:
                level: info
                title: <string>
                message: <string>
                href: <string>
    codeSamples:
      - label: update-installation
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.updateInstallation({
              integrationConfigurationId: "<id>",
            });


          }

          run();
  response:
    '204': {}
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
title: "Update Resource"

last_updated: "2025-11-07T00:37:13.330Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/update-resource"
--------------------------------------------------------------------------------

# Update Resource

> This endpoint updates an existing resource in the installation. All parameters are optional, allowing partial updates.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/installations/{integrationConfigurationId}/resources/{resourceId}
paths:
  path: /v1/installations/{integrationConfigurationId}/resources/{resourceId}
  method: patch
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
              ownership:
                allOf:
                  - type: string
                    enum:
                      - owned
                      - linked
                      - sandbox
              name:
                allOf:
                  - type: string
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
              metadata:
                allOf:
                  - type: object
                    additionalProperties: true
              billingPlan:
                allOf:
                  - type: object
                    required:
                      - id
                      - type
                      - name
                    properties:
                      id:
                        type: string
                      type:
                        type: string
                        enum:
                          - prepayment
                          - subscription
                      name:
                        type: string
                      description:
                        type: string
                      paymentMethodRequired:
                        type: boolean
                      cost:
                        type: string
                      details:
                        type: array
                        items:
                          type: object
                          properties:
                            label:
                              type: string
                            value:
                              type: string
                          required:
                            - label
                          additionalProperties: false
                      highlightedDetails:
                        type: array
                        items:
                          type: object
                          properties:
                            label:
                              type: string
                            value:
                              type: string
                          required:
                            - label
                          additionalProperties: false
                      effectiveDate:
                        type: string
                    additionalProperties: true
              notification:
                allOf:
                  - type: object
                    required:
                      - level
                      - title
                    properties:
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
                        format: uri
              extras:
                allOf:
                  - type: object
                    additionalProperties: true
              secrets:
                allOf:
                  - type: array
                    items:
                      type: object
                      required:
                        - name
                        - value
                      properties:
                        name:
                          type: string
                        value:
                          type: string
                        prefix:
                          type: string
                        environmentOverrides:
                          type: object
                          description: >-
                            A map of environments to override values for the
                            secret, used for setting different values across
                            deployments in production, preview, and development
                            environments. Note: the same value will be used for
                            all deployments in the given environment.
                          properties:
                            development:
                              type: string
                              description: Value used for development environment.
                            preview:
                              type: string
                              description: Value used for preview environment.
                            production:
                              type: string
                              description: Value used for production environment.
                      additionalProperties: false
            additionalProperties: false
        examples:
          example:
            value:
              ownership: owned
              name: <string>
              status: ready
              metadata: {}
              billingPlan:
                id: <string>
                type: prepayment
                name: <string>
                description: <string>
                paymentMethodRequired: true
                cost: <string>
                details:
                  - label: <string>
                    value: <string>
                highlightedDetails:
                  - label: <string>
                    value: <string>
                effectiveDate: <string>
              notification:
                level: info
                title: <string>
                message: <string>
                href: <string>
              extras: {}
              secrets:
                - name: <string>
                  value: <string>
                  prefix: <string>
                  environmentOverrides:
                    development: <string>
                    preview: <string>
                    production: <string>
    codeSamples:
      - label: update-resource
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.marketplace.updateResource({
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
              name:
                allOf:
                  - type: string
            requiredProperties:
              - name
        examples:
          example:
            value:
              name: <string>
        description: ''
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
    '409': {}
    '422': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update Resource Secrets"

last_updated: "2025-11-07T00:37:13.296Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/update-resource-secrets"
--------------------------------------------------------------------------------

# Update Resource Secrets

> This endpoint updates the secrets of a resource. If a resource has projects connected, the connected secrets are updated with the new secrets. The old secrets may still be used by existing connected projects because they are not automatically redeployed. Redeployment is a manual action and must be completed by the user. All new project connections will use the new secrets.<br/> <br/> Use cases for this endpoint:<br/> <br/> - Resetting the credentials of a database in the partner. If the user requests the credentials to be updated in the partner’s application, the partner post the new set of secrets to Vercel, the user should redeploy their application and the expire the old credentials.<br/>

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/installations/{integrationConfigurationId}/resources/{resourceId}/secrets
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/resources/{resourceId}/secrets
  method: put
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
              secrets:
                allOf:
                  - type: array
                    items:
                      type: object
                      required:
                        - name
                        - value
                      properties:
                        name:
                          type: string
                        value:
                          type: string
                        prefix:
                          type: string
                        environmentOverrides:
                          type: object
                          description: >-
                            A map of environments to override values for the
                            secret, used for setting different values across
                            deployments in production, preview, and development
                            environments. Note: the same value will be used for
                            all deployments in the given environment.
                          properties:
                            development:
                              type: string
                              description: Value used for development environment.
                            preview:
                              type: string
                              description: Value used for preview environment.
                            production:
                              type: string
                              description: Value used for production environment.
                      additionalProperties: false
              partial:
                allOf:
                  - type: boolean
                    description: >-
                      If true, will only overwrite the provided secrets instead
                      of replacing all secrets.
            requiredProperties:
              - secrets
            additionalProperties: false
        examples:
          example:
            value:
              secrets:
                - name: <string>
                  value: <string>
                  prefix: <string>
                  environmentOverrides:
                    development: <string>
                    preview: <string>
                    production: <string>
              partial: true
    codeSamples:
      - label: update-resource-secrets-by-id
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.updateResourceSecretsById({
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
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
    '409': {}
    '422': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update Resource Secrets (Deprecated)"

last_updated: "2025-11-07T00:37:13.330Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/marketplace/update-resource-secrets-deprecated"
--------------------------------------------------------------------------------

# Update Resource Secrets (Deprecated)

> This endpoint is deprecated and replaced with the endpoint [Update Resource Secrets](#update-resource-secrets). <br/> This endpoint updates the secrets of a resource. If a resource has projects connected, the connected secrets are updated with the new secrets. The old secrets may still be used by existing connected projects because they are not automatically redeployed. Redeployment is a manual action and must be completed by the user. All new project connections will use the new secrets.<br/> <br/> Use cases for this endpoint:<br/> <br/> - Resetting the credentials of a database in the partner. If the user requests the credentials to be updated in the partner’s application, the partner post the new set of secrets to Vercel, the user should redeploy their application and the expire the old credentials.<br/>

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/installations/{integrationConfigurationId}/products/{integrationProductIdOrSlug}/resources/{resourceId}/secrets
paths:
  path: >-
    /v1/installations/{integrationConfigurationId}/products/{integrationProductIdOrSlug}/resources/{resourceId}/secrets
  method: put
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
        integrationProductIdOrSlug:
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
              secrets:
                allOf:
                  - type: array
                    items:
                      type: object
                      required:
                        - name
                        - value
                      properties:
                        name:
                          type: string
                        value:
                          type: string
                        prefix:
                          type: string
                        environmentOverrides:
                          type: object
                          description: >-
                            A map of environments to override values for the
                            secret, used for setting different values across
                            deployments in production, preview, and development
                            environments. Note: the same value will be used for
                            all deployments in the given environment.
                          properties:
                            development:
                              type: string
                              description: Value used for development environment.
                            preview:
                              type: string
                              description: Value used for preview environment.
                            production:
                              type: string
                              description: Value used for production environment.
                      additionalProperties: false
              partial:
                allOf:
                  - type: boolean
                    description: If true, will only update the provided secrets
            required: true
            requiredProperties:
              - secrets
            additionalProperties: false
        examples:
          example:
            value:
              secrets:
                - name: <string>
                  value: <string>
                  prefix: <string>
                  environmentOverrides:
                    development: <string>
                    preview: <string>
                    production: <string>
              partial: true
    codeSamples:
      - label: update-resource-secrets
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.marketplace.updateResourceSecrets({
              integrationConfigurationId: "<id>",
              integrationProductIdOrSlug: "<value>",
              resourceId: "<id>",
              requestBody: {
                secrets: [],
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
    '409': {}
    '422': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Adds a new member to a project."

last_updated: "2025-11-07T00:37:13.370Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projectmembers/adds-a-new-member-to-a-project"
--------------------------------------------------------------------------------

# Adds a new member to a project.

> Adds a new member to the project.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{idOrName}/members
paths:
  path: /v1/projects/{idOrName}/members
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
        idOrName:
          schema:
            - type: string
              required: true
              description: The ID or name of the Project.
              example: prj_pavWOn1iLObbXLRiwVvzmPrTWyTf
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
              uid:
                allOf:
                  - &ref_0
                    type: string
                    maxLength: 256
                    example: ndlgr43fadlPyCtREAqxxdyFK
                    description: >-
                      The ID of the team member that should be added to this
                      project.
              username:
                allOf:
                  - &ref_1
                    type: string
                    maxLength: 256
                    example: example
                    description: >-
                      The username of the team member that should be added to
                      this project.
              email:
                allOf:
                  - &ref_2
                    type: string
                    format: email
                    example: entity@example.com
                    description: >-
                      The email of the team member that should be added to this
                      project.
              role:
                allOf:
                  - &ref_3
                    type: string
                    enum:
                      - ADMIN
                      - PROJECT_DEVELOPER
                      - PROJECT_VIEWER
                    example: ADMIN
                    description: The project role of the member that will be added.
            required: true
            requiredProperties:
              - role
              - uid
            additionalProperties: false
          - type: object
            properties:
              uid:
                allOf:
                  - *ref_0
              username:
                allOf:
                  - *ref_1
              email:
                allOf:
                  - *ref_2
              role:
                allOf:
                  - *ref_3
            required: true
            requiredProperties:
              - role
              - username
            additionalProperties: false
          - type: object
            properties:
              uid:
                allOf:
                  - *ref_0
              username:
                allOf:
                  - *ref_1
              email:
                allOf:
                  - *ref_2
              role:
                allOf:
                  - *ref_3
            required: true
            requiredProperties:
              - role
              - email
            additionalProperties: false
        examples:
          example:
            value:
              uid: ndlgr43fadlPyCtREAqxxdyFK
              username: example
              email: entity@example.com
              role: ADMIN
    codeSamples:
      - label: addProjectMember
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.ProjectMembers.AddProjectMember(ctx, \"prj_pavWOn1iLObbXLRiwVvzmPrTWyTf\", nil, nil, vercel.Pointer(operations.CreateAddProjectMemberRequestBodyAddProjectMemberRequestBody1(\n        operations.AddProjectMemberRequestBody1{\n            UID: \"ndlgr43fadlPyCtREAqxxdyFK\",\n            Username: vercel.String(\"example\"),\n            Email: vercel.String(\"entity@example.com\"),\n            Role: operations.RequestBodyRoleAdmin,\n        },\n    )))\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: addProjectMember
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projectMembers.addProjectMember({
              idOrName: "prj_pavWOn1iLObbXLRiwVvzmPrTWyTf",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                uid: "ndlgr43fadlPyCtREAqxxdyFK",
                username: "example",
                email: "entity@example.com",
                role: "ADMIN",
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
              id:
                allOf:
                  - type: string
            description: Responds with the project ID on success.
            requiredProperties:
              - id
        examples:
          example:
            value:
              id: <string>
        description: Responds with the project ID on success.
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "List project members"

last_updated: "2025-11-07T00:37:13.874Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projectmembers/list-project-members"
--------------------------------------------------------------------------------

# List project members

> Lists all members of a project.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/members
paths:
  path: /v1/projects/{idOrName}/members
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
        idOrName:
          schema:
            - type: string
              required: true
              description: The ID or name of the Project.
              example: prj_pavWOn1iLObbXLRiwVvzmPrTWyTf
      query:
        limit:
          schema:
            - type: integer
              required: false
              description: Limit how many project members should be returned
              maximum: 100
              minimum: 1
              example: 20
        since:
          schema:
            - type: integer
              required: false
              description: >-
                Timestamp in milliseconds to only include members added since
                then.
              example: 1540095775951
        until:
          schema:
            - type: integer
              required: false
              description: >-
                Timestamp in milliseconds to only include members added until
                then.
              example: 1540095775951
        search:
          schema:
            - type: string
              required: false
              description: Search project members by their name, username, and email.
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
      - label: getProjectMembers
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.ProjectMembers.GetProjectMembers(ctx, operations.GetProjectMembersRequest{\n        IDOrName: \"prj_pavWOn1iLObbXLRiwVvzmPrTWyTf\",\n        Limit: vercel.Int64(20),\n        Since: vercel.Int64(1540095775951),\n        Until: vercel.Int64(1540095775951),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: getProjectMembers
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projectMembers.getProjectMembers({
              idOrName: "prj_pavWOn1iLObbXLRiwVvzmPrTWyTf",
              limit: 20,
              since: 1540095775951,
              until: 1540095775951,
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
            properties: {}
          - type: object
            properties:
              members:
                allOf:
                  - items:
                      properties:
                        avatar:
                          type: string
                          description: ID of the file for the Avatar of this member.
                          example: 123a6c5209bc3778245d011443644c8d27dc2c50
                        email:
                          type: string
                          description: The email of this member.
                          example: jane.doe@example.com
                        role:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_DEVELOPER
                            - PROJECT_VIEWER
                          description: Role of this user in the project.
                          example: ADMIN
                        computedProjectRole:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_DEVELOPER
                            - PROJECT_VIEWER
                          description: Role of this user in the project.
                          example: ADMIN
                        uid:
                          type: string
                          description: The ID of this user.
                          example: zTuNVUXEAvvnNN3IaqinkyMw
                        username:
                          type: string
                          description: The unique username of this user.
                          example: jane-doe
                        name:
                          type: string
                          description: The name of this user.
                          example: Jane Doe
                        createdAt:
                          type: number
                          description: >-
                            Timestamp in milliseconds when this member was
                            added.
                          example: 1588720733602
                        teamRole:
                          type: string
                          enum:
                            - OWNER
                            - MEMBER
                            - DEVELOPER
                            - SECURITY
                            - BILLING
                            - VIEWER
                            - VIEWER_FOR_PLUS
                            - CONTRIBUTOR
                          description: The role of this user in the team.
                          example: CONTRIBUTOR
                      required:
                        - email
                        - role
                        - computedProjectRole
                        - uid
                        - username
                        - createdAt
                        - teamRole
                      type: object
                    type: array
              pagination:
                allOf:
                  - properties:
                      hasNext:
                        type: boolean
                      count:
                        type: number
                        description: Amount of items in the current page.
                        example: 20
                      next:
                        nullable: true
                        type: number
                        description: Timestamp that must be used to request the next page.
                        example: 1540095775951
                      prev:
                        nullable: true
                        type: number
                        description: >-
                          Timestamp that must be used to request the previous
                          page.
                        example: 1540095775951
                    required:
                      - hasNext
                      - count
                      - next
                      - prev
                    type: object
            description: Paginated list of members for the project.
            requiredProperties:
              - members
              - pagination
        examples:
          example:
            value: {}
        description: Paginated list of members for the project.
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
title: "Remove a Project Member"

last_updated: "2025-11-07T00:37:13.814Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projectmembers/remove-a-project-member"
--------------------------------------------------------------------------------

# Remove a Project Member

> Remove a member from a specific project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/projects/{idOrName}/members/{uid}
paths:
  path: /v1/projects/{idOrName}/members/{uid}
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
        idOrName:
          schema:
            - type: string
              required: true
              description: The ID or name of the Project.
              example: prj_pavWOn1iLObbXLRiwVvzmPrTWyTf
        uid:
          schema:
            - type: string
              required: true
              description: The user ID of the member.
              example: ndlgr43fadlPyCtREAqxxdyFK
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
      - label: removeProjectMember
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.ProjectMembers.RemoveProjectMember(ctx, \"prj_pavWOn1iLObbXLRiwVvzmPrTWyTf\", \"ndlgr43fadlPyCtREAqxxdyFK\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: removeProjectMember
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projectMembers.removeProjectMember({
              idOrName: "prj_pavWOn1iLObbXLRiwVvzmPrTWyTf",
              uid: "ndlgr43fadlPyCtREAqxxdyFK",
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
              id:
                allOf:
                  - type: string
            requiredProperties:
              - id
        examples:
          example:
            value:
              id: <string>
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
title: "Accept project transfer request"

last_updated: "2025-11-07T00:37:13.910Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/accept-project-transfer-request"
--------------------------------------------------------------------------------

# Accept project transfer request

> Accept a project transfer request initated by another team. <br/> The `code` is generated using the `POST /projects/:idOrName/transfer-request` endpoint.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /projects/transfer-request/{code}
paths:
  path: /projects/transfer-request/{code}
  method: put
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
        code:
          schema:
            - type: string
              required: true
              description: The code of the project transfer request.
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
              newProjectName:
                allOf:
                  - description: The desired name for the project
                    example: a-project-name
                    type: string
                    maxLength: 100
              paidFeatures:
                allOf:
                  - type: object
                    additionalProperties: false
                    properties:
                      concurrentBuilds:
                        type: integer
                        nullable: true
                      passwordProtection:
                        type: boolean
                        nullable: true
                      previewDeploymentSuffix:
                        type: boolean
                        nullable: true
              acceptedPolicies:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      additionalProperties:
                        type: string
                        format: date-time
                      required:
                        - eula
                        - privacy
                      properties:
                        eula:
                          type: string
                          format: date-time
                        privacy:
                          type: string
                          format: date-time
            additionalProperties: false
        examples:
          example:
            value:
              newProjectName: a-project-name
              paidFeatures:
                concurrentBuilds: 123
                passwordProtection: true
                previewDeploymentSuffix: true
              acceptedPolicies: {}
    codeSamples:
      - label: acceptProjectTransferRequest
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.acceptProjectTransferRequest({
              code: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                newProjectName: "a-project-name",
              },
            });

            console.log(result);
          }

          run();
  response:
    '202':
      application/json:
        schemaArray:
          - type: object
            properties:
              partnerCalls:
                allOf:
                  - items:
                      properties:
                        installationId:
                          type: string
                        resourceIds:
                          items:
                            type: string
                          type: array
                        result:
                          properties:
                            status:
                              type: string
                              enum:
                                - fulfilled
                                - errored
                            error:
                              type: object
                            code:
                              type: string
                          required:
                            - status
                          type: object
                      required:
                        - installationId
                        - resourceIds
                        - result
                      type: object
                    type: array
              resourceTransferErrors:
                allOf:
                  - items:
                      type: object
                    type: array
            requiredProperties:
              - partnerCalls
              - resourceTransferErrors
          - type: object
            properties: {}
        examples:
          example:
            value:
              partnerCalls:
                - installationId: <string>
                  resourceIds:
                    - <string>
                  result:
                    status: fulfilled
                    error: {}
                    code: <string>
              resourceTransferErrors:
                - {}
        description: The project has been transferred successfully.
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
    '422': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Add a domain to a project"

last_updated: "2025-11-07T00:37:14.224Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/add-a-domain-to-a-project"
--------------------------------------------------------------------------------

# Add a domain to a project

> Add a domain to the project by passing its domain name and by specifying the project by either passing the project `id` or `name` in the URL. If the domain is not yet verified to be used on this project, the request will return `verified = false`, and the domain will need to be verified according to the `verification` challenge via `POST /projects/:idOrName/domains/:domain/verify`. If the domain already exists on the project, the request will fail with a `400` status code.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v10/projects/{idOrName}/domains
paths:
  path: /v10/projects/{idOrName}/domains
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
        idOrName:
          schema:
            - type: string
              required: true
              description: The unique project identifier or the project name
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
                  - description: The project domain name
                    example: www.example.com
                    type: string
              gitBranch:
                allOf:
                  - description: Git branch to link the project domain
                    example: null
                    maxLength: 250
                    type: string
                    nullable: true
              customEnvironmentId:
                allOf:
                  - description: >-
                      The unique custom environment identifier within the
                      project
                    type: string
              redirect:
                allOf:
                  - description: Target destination domain for redirect
                    example: foobar.com
                    type: string
                    nullable: true
              redirectStatusCode:
                allOf:
                  - description: Status code for domain redirect
                    example: 307
                    type: integer
                    enum:
                      - null
                      - 301
                      - 302
                      - 307
                      - 308
                    nullable: true
            required: true
            requiredProperties:
              - name
        examples:
          example:
            value:
              name: www.example.com
              gitBranch: null
              customEnvironmentId: <string>
              redirect: foobar.com
              redirectStatusCode: 307
    codeSamples:
      - label: addProjectDomain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.AddProjectDomain(ctx, \"<value>\", nil, nil, &operations.AddProjectDomainRequestBody{\n        Name: \"www.example.com\",\n        GitBranch: nil,\n        Redirect: vercel.String(\"foobar.com\"),\n        RedirectStatusCode: operations.AddProjectDomainRedirectStatusCodeThreeHundredAndSeven.ToPointer(),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: addProjectDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.addProjectDomain({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "www.example.com",
                gitBranch: null,
                redirect: "foobar.com",
                redirectStatusCode: 307,
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
              name:
                allOf:
                  - type: string
              apexName:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - type: string
              redirect:
                allOf:
                  - nullable: true
                    type: string
              redirectStatusCode:
                allOf:
                  - nullable: true
                    type: number
                    enum:
                      - 307
                      - 301
                      - 302
                      - 308
              gitBranch:
                allOf:
                  - nullable: true
                    type: string
              customEnvironmentId:
                allOf:
                  - nullable: true
                    type: string
              updatedAt:
                allOf:
                  - type: number
              createdAt:
                allOf:
                  - type: number
              verified:
                allOf:
                  - type: boolean
                    description: >-
                      `true` if the domain is verified for use with the project.
                      If `false` it will not be used as an alias on this project
                      until the challenge in `verification` is completed.
              verification:
                allOf:
                  - items:
                      properties:
                        type:
                          type: string
                        domain:
                          type: string
                        value:
                          type: string
                        reason:
                          type: string
                      required:
                        - type
                        - domain
                        - value
                        - reason
                      type: object
                      description: >-
                        A list of verification challenges, one of which must be
                        completed to verify the domain for use on the project.
                        After the challenge is complete `POST
                        /projects/:idOrName/domains/:domain/verify` to verify
                        the domain. Possible challenges: - If `verification.type
                        = TXT` the `verification.domain` will be checked for a
                        TXT record matching `verification.value`.
                    type: array
                    description: >-
                      A list of verification challenges, one of which must be
                      completed to verify the domain for use on the project.
                      After the challenge is complete `POST
                      /projects/:idOrName/domains/:domain/verify` to verify the
                      domain. Possible challenges: - If `verification.type =
                      TXT` the `verification.domain` will be checked for a TXT
                      record matching `verification.value`.
            requiredProperties:
              - name
              - apexName
              - projectId
              - verified
        examples:
          example:
            value:
              name: <string>
              apexName: <string>
              projectId: <string>
              redirect: <string>
              redirectStatusCode: 307
              gitBranch: <string>
              customEnvironmentId: <string>
              updatedAt: 123
              createdAt: 123
              verified: true
              verification:
                - type: <string>
                  domain: <string>
                  value: <string>
                  reason: <string>
        description: The domain was successfully added to the project
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              One of the provided values in the request body is invalid.

              One of the provided values in the request query is invalid.

              The domain is not valid

              You can't set both a git branch and a redirect for the domain

              The domain can not be added because the latest production
              deployment for the project was not successful

              The domain redirect is not valid

              A domain cannot redirect to itself

              You can not set the production branch as a branch for your domain
        examples: {}
        description: >-
          One of the provided values in the request body is invalid.

          One of the provided values in the request query is invalid.

          The domain is not valid

          You can't set both a git branch and a redirect for the domain

          The domain can not be added because the latest production deployment
          for the project was not successful

          The domain redirect is not valid

          A domain cannot redirect to itself

          You can not set the production branch as a branch for your domain
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '402':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              The account was soft-blocked for an unhandled reason.
              The account is missing a payment so payment method must be updated
        examples: {}
        description: |-
          The account was soft-blocked for an unhandled reason.
          The account is missing a payment so payment method must be updated
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              You do not have permission to access this resource.
              You don't have access to the domain you are adding
        examples: {}
        description: |-
          You do not have permission to access this resource.
          You don't have access to the domain you are adding
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              The domain is already assigned to another Vercel project

              Cannot create project domain since owner already has `domain` on
              their account, but it's not verified yet.

              Cannot create project domain since owner already has `domain` on
              their account, and it's verified.

              The domain is not allowed to be used

              The project is currently being transferred
        examples: {}
        description: >-
          The domain is already assigned to another Vercel project

          Cannot create project domain since owner already has `domain` on their
          account, but it's not verified yet.

          Cannot create project domain since owner already has `domain` on their
          account, and it's verified.

          The domain is not allowed to be used

          The project is currently being transferred
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Batch remove environment variables"

last_updated: "2025-11-07T00:37:14.050Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/batch-remove-environment-variables"
--------------------------------------------------------------------------------

# Batch remove environment variables

> Delete multiple environment variables for a given project in a single batch operation.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/projects/{idOrName}/env
paths:
  path: /v1/projects/{idOrName}/env
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
        idOrName:
          schema:
            - type: string
              required: true
              description: The unique project identifier or the project name
              example: prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA
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
              ids:
                allOf:
                  - description: Array of environment variable IDs to delete
                    type: array
                    items:
                      type: string
                    minItems: 1
                    maxItems: 1000
            requiredProperties:
              - ids
            additionalProperties: false
        examples:
          example:
            value:
              ids:
                - <string>
    codeSamples:
      - label: batchRemoveProjectEnv
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.batchRemoveProjectEnv({
              idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",
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
              deleted:
                allOf:
                  - type: number
              ids:
                allOf:
                  - items:
                      type: string
                    type: array
            requiredProperties:
              - deleted
              - ids
        examples:
          example:
            value:
              deleted: 123
              ids:
                - <string>
        description: ''
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
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Create a new project"

last_updated: "2025-11-07T00:37:13.939Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/create-a-new-project"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./25-list-products-for-integration-configuration.md) | [Index](./index.md) | [Next →](./27-create-a-new-project.md)
