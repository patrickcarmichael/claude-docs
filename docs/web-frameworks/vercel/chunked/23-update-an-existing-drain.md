**Navigation:** [← Previous](./22-update-auto-renew-for-a-domain.md) | [Index](./index.md) | [Next →](./24-retrieve-custom-environments.md)

---

# Update an existing Drain

> Update the configuration of an existing drain.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/drains/{id}
paths:
  path: /v1/drains/{id}
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
              projects:
                allOf:
                  - type: string
                    enum:
                      - some
                      - all
              projectIds:
                allOf:
                  - type: array
                    items:
                      type: string
                    nullable: true
              filter:
                allOf:
                  - oneOf:
                      - type: string
                        nullable: true
                      - type: object
                        additionalProperties: false
                        required:
                          - version
                          - filter
                        properties:
                          version:
                            type: string
                          filter:
                            oneOf:
                              - type: object
                                additionalProperties: false
                                required:
                                  - type
                                properties:
                                  type:
                                    type: string
                                  project:
                                    type: object
                                    additionalProperties: false
                                    properties:
                                      ids:
                                        type: array
                                        items:
                                          type: string
                                  log:
                                    type: object
                                    additionalProperties: false
                                    properties:
                                      sources:
                                        type: array
                                        items:
                                          type: string
                                  deployment:
                                    type: object
                                    additionalProperties: false
                                    properties:
                                      environments:
                                        type: array
                                        items:
                                          type: string
                              - type: object
                                additionalProperties: false
                                required:
                                  - type
                                  - text
                                properties:
                                  type:
                                    type: string
                                  text:
                                    type: string
              schemas:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      required:
                        - version
                      properties:
                        version:
                          type: string
              delivery:
                allOf:
                  - type: object
                    oneOf:
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        properties:
                          type:
                            type: string
                          endpoint:
                            type: string
                          compression:
                            type: string
                            enum:
                              - gzip
                              - none
                          encoding:
                            type: string
                            enum:
                              - json
                              - ndjson
                          headers:
                            type: object
                            additionalProperties:
                              type: string
                          secret:
                            type: string
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        properties:
                          type:
                            type: string
                          endpoint:
                            oneOf:
                              - type: object
                                additionalProperties: false
                                required:
                                  - traces
                                properties:
                                  traces:
                                    type: string
                          encoding:
                            type: string
                            enum:
                              - proto
                              - json
                          headers:
                            type: object
                            additionalProperties:
                              type: string
                          secret:
                            type: string
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - secret
                        properties:
                          type:
                            type: string
                          endpoint:
                            type: string
                          secret:
                            type: string
              sampling:
                allOf:
                  - type: array
                    items:
                      type: object
                      additionalProperties: false
                      required:
                        - type
                        - rate
                      properties:
                        type:
                          type: string
                        rate:
                          type: number
                          minimum: 0
                          maximum: 1
                          description: Sampling rate from 0 to 1 (e.g., 0.1 for 10%)
                        env:
                          type: string
                          enum:
                            - production
                            - preview
                          description: Environment to apply sampling to
                        requestPath:
                          type: string
                          description: Request path prefix to apply the sampling rule to
                    nullable: true
              transforms:
                allOf:
                  - type: array
                    items:
                      type: object
                      required:
                        - id
                      properties:
                        id:
                          type: string
                    nullable: true
              status:
                allOf:
                  - type: string
                    enum:
                      - enabled
                      - disabled
              source:
                allOf:
                  - type: object
                    oneOf:
                      - oneOf:
                          - properties:
                              kind:
                                type: string
                                default: integration
                              externalResourceId:
                                type: string
                            additionalProperties: false
                            required:
                              - externalResourceId
                          - properties:
                              kind:
                                type: string
                                default: integration
                              resourceId:
                                type: string
                            additionalProperties: false
                            required:
                              - resourceId
                          - properties:
                              kind:
                                type: string
                                default: integration
                            additionalProperties: false
                            required:
                              - kind
                      - properties:
                          kind:
                            type: string
                            default: self-served
                        additionalProperties: false
                        required:
                          - kind
            additionalProperties: false
        examples:
          example:
            value:
              name: <string>
              projects: some
              projectIds:
                - <string>
              filter: <string>
              schemas: {}
              delivery:
                type: <string>
                endpoint: <string>
                compression: gzip
                encoding: json
                headers: {}
                secret: <string>
              sampling:
                - type: <string>
                  rate: 0.5
                  env: production
                  requestPath: <string>
              transforms:
                - id: <string>
              status: enabled
              source:
                kind: integration
                externalResourceId: <string>
    codeSamples:
      - label: updateDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.drains.updateDrain({
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
              id:
                allOf:
                  - type: string
              ownerId:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              createdFrom:
                allOf:
                  - type: string
                    enum:
                      - self-served
                      - integration
              updatedAt:
                allOf:
                  - type: number
              projectIds:
                allOf:
                  - items:
                      type: string
                    type: array
              schemas:
                allOf:
                  - properties:
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
                allOf:
                  - oneOf:
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
                allOf:
                  - items:
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
                allOf:
                  - nullable: true
                    type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - enabled
                      - disabled
                      - errored
              disabledAt:
                allOf:
                  - type: number
              disabledReason:
                allOf:
                  - type: string
                    enum:
                      - disabled-by-owner
                      - feature-not-available
                      - account-plan-downgrade
                      - disabled-by-admin
              disabledBy:
                allOf:
                  - type: string
              firstErrorTimestamp:
                allOf:
                  - type: number
              configurationId:
                allOf:
                  - type: string
              clientId:
                allOf:
                  - type: string
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
              filter:
                allOf:
                  - type: string
              filterV2:
                allOf:
                  - oneOf:
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
            requiredProperties:
              - id
              - ownerId
              - name
              - createdAt
              - updatedAt
              - source
          - type: object
            properties:
              id:
                allOf:
                  - type: string
              ownerId:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              createdFrom:
                allOf:
                  - type: string
                    enum:
                      - self-served
                      - integration
              updatedAt:
                allOf:
                  - type: number
              projectIds:
                allOf:
                  - items:
                      type: string
                    type: array
              schemas:
                allOf:
                  - properties:
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
                allOf:
                  - oneOf:
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
                allOf:
                  - items:
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
                allOf:
                  - nullable: true
                    type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - enabled
                      - disabled
                      - errored
              disabledAt:
                allOf:
                  - type: number
              disabledReason:
                allOf:
                  - type: string
                    enum:
                      - disabled-by-owner
                      - feature-not-available
                      - account-plan-downgrade
                      - disabled-by-admin
              disabledBy:
                allOf:
                  - type: string
              firstErrorTimestamp:
                allOf:
                  - type: number
              configurationId:
                allOf:
                  - type: string
              clientId:
                allOf:
                  - type: string
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
              filter:
                allOf:
                  - type: string
              filterV2:
                allOf:
                  - oneOf:
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
                allOf:
                  - type: string
              integrationConfigurationUri:
                allOf:
                  - type: string
              integrationWebsite:
                allOf:
                  - type: string
              projectsMetadata:
                allOf:
                  - items:
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
            requiredProperties:
              - id
              - ownerId
              - name
              - createdAt
              - updatedAt
              - source
        examples:
          example:
            value:
              id: <string>
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
title: "Validate Drain delivery configuration"

last_updated: "2025-11-07T00:37:10.974Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/drains/validate-drain-delivery-configuration"
--------------------------------------------------------------------------------

# Validate Drain delivery configuration

> Validate the delivery configuration of a Drain using sample events.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/drains/test
paths:
  path: /v1/drains/test
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
              schemas:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      required:
                        - version
                      properties:
                        version:
                          type: string
              delivery:
                allOf:
                  - type: object
                    oneOf:
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        properties:
                          type:
                            type: string
                          endpoint:
                            type: string
                          compression:
                            type: string
                            enum:
                              - gzip
                              - none
                          encoding:
                            type: string
                            enum:
                              - json
                              - ndjson
                          headers:
                            type: object
                            additionalProperties:
                              type: string
                          secret:
                            type: string
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        properties:
                          type:
                            type: string
                          endpoint:
                            oneOf:
                              - type: object
                                additionalProperties: false
                                required:
                                  - traces
                                properties:
                                  traces:
                                    type: string
                          encoding:
                            type: string
                            enum:
                              - proto
                              - json
                          headers:
                            type: object
                            additionalProperties:
                              type: string
                          secret:
                            type: string
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - secret
                        properties:
                          type:
                            type: string
                          endpoint:
                            type: string
                          secret:
                            type: string
            requiredProperties:
              - schemas
              - delivery
            additionalProperties: false
        examples:
          example:
            value:
              schemas: {}
              delivery:
                type: <string>
                endpoint: <string>
                compression: gzip
                encoding: json
                headers: {}
                secret: <string>
    codeSamples:
      - label: testDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.drains.testDrain({
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
              status:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
              endpoint:
                allOf:
                  - type: string
            requiredProperties:
              - status
              - error
              - endpoint
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
title: "Dangerously delete by tag"

last_updated: "2025-11-07T00:37:10.579Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-cache/dangerously-delete-by-tag"
--------------------------------------------------------------------------------

# Dangerously delete by tag

> Marks a cache tag as deleted, causing cache entries associated with that tag to be revalidated in the foreground on the next request. Use this method with caution because one tag can be associated with many paths and deleting the cache can cause many concurrent requests to the origin leading to cache stampede problem. A good use case for deleting the cache is when the origin has also been deleted, for example it returns a 404 or 410 status code.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/edge-cache/dangerously-delete-by-tags
paths:
  path: /v1/edge-cache/dangerously-delete-by-tags
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
        projectIdOrName:
          schema:
            - type: string
              required: true
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
              revalidationDeadlineSeconds:
                allOf:
                  - minimum: 0
                    type: number
              tags:
                allOf:
                  - oneOf:
                      - items:
                          maxLength: 256
                          type: string
                        maxItems: 16
                        minItems: 1
                        type: array
                      - maxLength: 8196
                        type: string
              target:
                allOf:
                  - enum:
                      - production
                      - preview
                    type: string
            requiredProperties:
              - tags
            additionalProperties: false
        examples:
          example:
            value:
              revalidationDeadlineSeconds: 1
              tags:
                - <string>
              target: production
    codeSamples:
      - label: dangerouslyDeleteByTags
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.edgeCache.dangerouslyDeleteByTags({
              projectIdOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });


          }

          run();
  response:
    '200': {}
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
title: "Invalidate by tag"

last_updated: "2025-11-07T00:37:10.693Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-cache/invalidate-by-tag"
--------------------------------------------------------------------------------

# Invalidate by tag

> Marks a cache tag as stale, causing cache entries associated with that tag to be revalidated in the background on the next request.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/edge-cache/invalidate-by-tags
paths:
  path: /v1/edge-cache/invalidate-by-tags
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
        projectIdOrName:
          schema:
            - type: string
              required: true
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
              tags:
                allOf:
                  - oneOf:
                      - items:
                          maxLength: 256
                          type: string
                        maxItems: 16
                        minItems: 1
                        type: array
                      - maxLength: 8196
                        type: string
              target:
                allOf:
                  - enum:
                      - production
                      - preview
                    type: string
            requiredProperties:
              - tags
            additionalProperties: false
        examples:
          example:
            value:
              tags:
                - <string>
              target: production
    codeSamples:
      - label: invalidateByTags
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.edgeCache.invalidateByTags({
              projectIdOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });


          }

          run();
  response:
    '200': {}
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
title: "Create an Edge Config"

last_updated: "2025-11-07T00:37:10.892Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/create-an-edge-config"
--------------------------------------------------------------------------------

# Create an Edge Config

> Creates an Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/edge-config
paths:
  path: /v1/edge-config
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
              slug:
                allOf:
                  - maxLength: 64
                    pattern: ^[\\w-]+$
                    type: string
              items:
                allOf:
                  - type: object
                    additionalProperties: {}
            required: true
            requiredProperties:
              - slug
        examples:
          example:
            value:
              slug: <string>
              items: {}
    codeSamples:
      - label: createEdgeConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.CreateEdgeConfig(ctx, nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createEdgeConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.createEdgeConfig({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                slug: "<value>",
              },
            });

            console.log(result);
          }

          run();
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
              deletedAt:
                allOf:
                  - nullable: true
                    type: number
              id:
                allOf:
                  - type: string
              slug:
                allOf:
                  - type: string
                    description: >-
                      Name for the Edge Config Names are not unique. Must start
                      with an alphabetic character and can contain only
                      alphanumeric characters and underscores).
              ownerId:
                allOf:
                  - type: string
              digest:
                allOf:
                  - type: string
              transfer:
                allOf:
                  - properties:
                      fromAccountId:
                        type: string
                      startedAt:
                        type: number
                      doneAt:
                        nullable: true
                        type: number
                    required:
                      - fromAccountId
                      - startedAt
                      - doneAt
                    type: object
                    description: >-
                      Keeps track of the current state of the Edge Config while
                      it gets transferred.
              schema:
                allOf:
                  - type: object
              purpose:
                allOf:
                  - oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - flags
                          projectId:
                            type: string
                        required:
                          - type
                          - projectId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - experimentation
                          resourceId:
                            type: string
                        required:
                          - type
                          - resourceId
                        type: object
              syncedToDynamoAt:
                allOf:
                  - type: number
                    description: >-
                      Timestamp of when the Edge Config was synced to DynamoDB
                      initially. It is only set when syncing the entire Edge
                      Config, not when updating.
              sizeInBytes:
                allOf:
                  - type: number
              itemCount:
                allOf:
                  - type: number
            description: An Edge Config
            requiredProperties:
              - createdAt
              - updatedAt
              - id
              - slug
              - ownerId
              - digest
              - sizeInBytes
              - itemCount
        examples:
          example:
            value:
              createdAt: 123
              updatedAt: 123
              deletedAt: 123
              id: <string>
              slug: <string>
              ownerId: <string>
              digest: <string>
              transfer:
                fromAccountId: <string>
                startedAt: 123
                doneAt: 123
              schema: {}
              purpose:
                type: flags
                projectId: <string>
              syncedToDynamoAt: 123
              sizeInBytes: 123
              itemCount: 123
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
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Create an Edge Config token"

last_updated: "2025-11-07T00:37:10.566Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/create-an-edge-config-token"
--------------------------------------------------------------------------------

# Create an Edge Config token

> Adds a token to an existing Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/edge-config/{edgeConfigId}/token
paths:
  path: /v1/edge-config/{edgeConfigId}/token
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
        edgeConfigId:
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              label:
                allOf:
                  - maxLength: 52
                    type: string
            required: true
            requiredProperties:
              - label
            additionalProperties: false
        examples:
          example:
            value:
              label: <string>
    codeSamples:
      - label: createEdgeConfigToken
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.CreateEdgeConfigToken(ctx, \"<id>\", nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createEdgeConfigToken
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.createEdgeConfigToken({
              edgeConfigId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                label: "<value>",
              },
            });

            console.log(result);
          }

          run();
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              token:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
            requiredProperties:
              - token
              - id
        examples:
          example:
            value:
              token: <string>
              id: <string>
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
title: "Delete an Edge Config"

last_updated: "2025-11-07T00:37:10.618Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/delete-an-edge-config"
--------------------------------------------------------------------------------

# Delete an Edge Config

> Delete an Edge Config by id.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/edge-config/{edgeConfigId}
paths:
  path: /v1/edge-config/{edgeConfigId}
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
        edgeConfigId:
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
      - label: deleteEdgeConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.DeleteEdgeConfig(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: deleteEdgeConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.edgeConfig.deleteEdgeConfig({
              edgeConfigId: "<id>",
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
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Delete an Edge Config's schema"

last_updated: "2025-11-07T00:37:10.847Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/delete-an-edge-configs-schema"
--------------------------------------------------------------------------------

# Delete an Edge Config's schema

> Deletes the schema of existing Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/edge-config/{edgeConfigId}/schema
paths:
  path: /v1/edge-config/{edgeConfigId}/schema
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
        edgeConfigId:
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
      - label: deleteEdgeConfigSchema
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.DeleteEdgeConfigSchema(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: deleteEdgeConfigSchema
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.edgeConfig.deleteEdgeConfigSchema({
              edgeConfigId: "<id>",
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
title: "Delete one or more Edge Config tokens"

last_updated: "2025-11-07T00:37:11.147Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/delete-one-or-more-edge-config-tokens"
--------------------------------------------------------------------------------

# Delete one or more Edge Config tokens

> Deletes one or more tokens of an existing Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/edge-config/{edgeConfigId}/tokens
paths:
  path: /v1/edge-config/{edgeConfigId}/tokens
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
        edgeConfigId:
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              tokens:
                allOf:
                  - type: array
                    items:
                      type: string
            required: true
            requiredProperties:
              - tokens
            additionalProperties: false
        examples:
          example:
            value:
              tokens:
                - <string>
    codeSamples:
      - label: deleteEdgeConfigTokens
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.DeleteEdgeConfigTokens(ctx, \"<id>\", nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: deleteEdgeConfigTokens
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.edgeConfig.deleteEdgeConfigTokens({
              edgeConfigId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                tokens: [
                  "<value 1>",
                  "<value 2>",
                  "<value 3>",
                ],
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
title: "Get all tokens of an Edge Config"

last_updated: "2025-11-07T00:37:11.604Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/get-all-tokens-of-an-edge-config"
--------------------------------------------------------------------------------

# Get all tokens of an Edge Config

> Returns all tokens of an Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/tokens
paths:
  path: /v1/edge-config/{edgeConfigId}/tokens
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
        edgeConfigId:
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
      - label: getEdgeConfigTokens
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfigTokens(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.EdgeConfigToken != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfigTokens
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfigTokens({
              edgeConfigId: "<id>",
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
              token:
                allOf:
                  - type: string
              label:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
                    description: >-
                      This is not the token itself, but rather an id to identify
                      the token by
              edgeConfigId:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
            description: The EdgeConfig.
            refIdentifier: '#/components/schemas/EdgeConfigToken'
            requiredProperties:
              - token
              - label
              - id
              - edgeConfigId
              - createdAt
        examples:
          example:
            value:
              token: <string>
              label: <string>
              id: <string>
              edgeConfigId: <string>
              createdAt: 123
        description: The EdgeConfig.
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
title: "Get an Edge Config"

last_updated: "2025-11-07T00:37:11.430Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/get-an-edge-config"
--------------------------------------------------------------------------------

# Get an Edge Config

> Returns an Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}
paths:
  path: /v1/edge-config/{edgeConfigId}
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
        edgeConfigId:
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
      - label: getEdgeConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfig(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfig({
              edgeConfigId: "<id>",
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
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
              deletedAt:
                allOf:
                  - nullable: true
                    type: number
              id:
                allOf:
                  - type: string
              slug:
                allOf:
                  - type: string
                    description: >-
                      Name for the Edge Config Names are not unique. Must start
                      with an alphabetic character and can contain only
                      alphanumeric characters and underscores).
              ownerId:
                allOf:
                  - type: string
              digest:
                allOf:
                  - type: string
              transfer:
                allOf:
                  - properties:
                      fromAccountId:
                        type: string
                      startedAt:
                        type: number
                      doneAt:
                        nullable: true
                        type: number
                    required:
                      - fromAccountId
                      - startedAt
                      - doneAt
                    type: object
                    description: >-
                      Keeps track of the current state of the Edge Config while
                      it gets transferred.
              schema:
                allOf:
                  - type: object
              purpose:
                allOf:
                  - oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - flags
                          projectId:
                            type: string
                        required:
                          - type
                          - projectId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - experimentation
                          resourceId:
                            type: string
                        required:
                          - type
                          - resourceId
                        type: object
              syncedToDynamoAt:
                allOf:
                  - type: number
                    description: >-
                      Timestamp of when the Edge Config was synced to DynamoDB
                      initially. It is only set when syncing the entire Edge
                      Config, not when updating.
              sizeInBytes:
                allOf:
                  - type: number
              itemCount:
                allOf:
                  - type: number
            description: The EdgeConfig.
            requiredProperties:
              - createdAt
              - updatedAt
              - id
              - slug
              - ownerId
              - digest
              - sizeInBytes
              - itemCount
        examples:
          example:
            value:
              createdAt: 123
              updatedAt: 123
              deletedAt: 123
              id: <string>
              slug: <string>
              ownerId: <string>
              digest: <string>
              transfer:
                fromAccountId: <string>
                startedAt: 123
                doneAt: 123
              schema: {}
              purpose:
                type: flags
                projectId: <string>
              syncedToDynamoAt: 123
              sizeInBytes: 123
              itemCount: 123
        description: The EdgeConfig.
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
title: "Get an Edge Config item"

last_updated: "2025-11-07T00:37:11.471Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/get-an-edge-config-item"
--------------------------------------------------------------------------------

# Get an Edge Config item

> Returns a specific Edge Config Item.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/item/{edgeConfigItemKey}
paths:
  path: /v1/edge-config/{edgeConfigId}/item/{edgeConfigItemKey}
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
        edgeConfigId:
          schema:
            - type: string
              required: true
        edgeConfigItemKey:
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
      - label: getEdgeConfigItem
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfigItem(ctx, \"<id>\", \"<value>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.EdgeConfigItem != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfigItem
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfigItem({
              edgeConfigId: "<id>",
              edgeConfigItemKey: "<value>",
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
              key:
                allOf:
                  - type: string
              value:
                allOf:
                  - $ref: '#/components/schemas/EdgeConfigItemValue'
              description:
                allOf:
                  - type: string
              edgeConfigId:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
            description: The EdgeConfig.
            refIdentifier: '#/components/schemas/EdgeConfigItem'
            requiredProperties:
              - key
              - value
              - edgeConfigId
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              key: <string>
              value: <string>
              description: <string>
              edgeConfigId: <string>
              createdAt: 123
              updatedAt: 123
        description: The EdgeConfig.
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
title: "Get Edge Config backup"

last_updated: "2025-11-07T00:37:11.463Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-backup"
--------------------------------------------------------------------------------

# Get Edge Config backup

> Retrieves a specific version of an Edge Config from backup storage.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/backups/{edgeConfigBackupVersionId}
paths:
  path: /v1/edge-config/{edgeConfigId}/backups/{edgeConfigBackupVersionId}
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
        edgeConfigId:
          schema:
            - type: string
              required: true
        edgeConfigBackupVersionId:
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
      - label: getEdgeConfigBackup
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfigBackup(ctx, \"<id>\", \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfigBackup
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfigBackup({
              edgeConfigId: "<id>",
              edgeConfigBackupVersionId: "<id>",
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
              lastModified:
                allOf:
                  - type: number
              backup:
                allOf:
                  - properties:
                      digest:
                        type: string
                      items:
                        additionalProperties:
                          properties:
                            updatedAt:
                              type: number
                            value:
                              $ref: '#/components/schemas/EdgeConfigItemValue'
                            description:
                              type: string
                            createdAt:
                              type: number
                          required:
                            - updatedAt
                            - value
                            - createdAt
                          type: object
                        type: object
                      slug:
                        type: string
                        description: >-
                          Name for the Edge Config Names are not unique. Must
                          start with an alphabetic character and can contain
                          only alphanumeric characters and underscores).
                      updatedAt:
                        type: number
                    required:
                      - digest
                      - items
                      - slug
                      - updatedAt
                    type: object
              metadata:
                allOf:
                  - properties:
                      updatedAt:
                        type: string
                      updatedBy:
                        type: string
                      itemsCount:
                        type: number
                      itemsBytes:
                        type: number
                    type: object
              user:
                allOf:
                  - properties:
                      id:
                        type: string
                      username:
                        type: string
                      email:
                        type: string
                      name:
                        type: string
                      avatar:
                        type: string
                    required:
                      - id
                      - username
                      - email
                    type: object
            description: >-
              The object the API responds with when requesting an Edge Config
              backup
            requiredProperties:
              - id
              - lastModified
              - backup
              - metadata
          - type: object
            properties:
              user:
                allOf:
                  - properties:
                      id:
                        type: string
                      username:
                        type: string
                      email:
                        type: string
                      name:
                        type: string
                      avatar:
                        type: string
                    required:
                      - id
                      - username
                      - email
                    type: object
              id:
                allOf:
                  - type: string
              lastModified:
                allOf:
                  - type: number
              backup:
                allOf:
                  - properties:
                      digest:
                        type: string
                      items:
                        additionalProperties:
                          properties:
                            updatedAt:
                              type: number
                            value:
                              $ref: '#/components/schemas/EdgeConfigItemValue'
                            description:
                              type: string
                            createdAt:
                              type: number
                          required:
                            - updatedAt
                            - value
                            - createdAt
                          type: object
                        type: object
                      slug:
                        type: string
                        description: >-
                          Name for the Edge Config Names are not unique. Must
                          start with an alphabetic character and can contain
                          only alphanumeric characters and underscores).
                      updatedAt:
                        type: number
                    required:
                      - digest
                      - items
                      - slug
                      - updatedAt
                    type: object
              metadata:
                allOf:
                  - properties:
                      updatedAt:
                        type: string
                      updatedBy:
                        type: string
                      itemsCount:
                        type: number
                      itemsBytes:
                        type: number
                    type: object
            requiredProperties:
              - user
              - id
              - lastModified
              - backup
              - metadata
        examples:
          example:
            value:
              id: <string>
              lastModified: 123
              backup:
                digest: <string>
                items: {}
                slug: <string>
                updatedAt: 123
              metadata:
                updatedAt: <string>
                updatedBy: <string>
                itemsCount: 123
                itemsBytes: 123
              user:
                id: <string>
                username: <string>
                email: <string>
                name: <string>
                avatar: <string>
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
title: "Get Edge Config backups"

last_updated: "2025-11-07T00:37:11.870Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-backups"
--------------------------------------------------------------------------------

# Get Edge Config backups

> Returns backups of an Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/backups
paths:
  path: /v1/edge-config/{edgeConfigId}/backups
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
        edgeConfigId:
          schema:
            - type: string
              required: true
      query:
        next:
          schema:
            - type: string
              required: false
        limit:
          schema:
            - type: number
              required: false
              maximum: 50
              minimum: 0
        metadata:
          schema:
            - type: string
              required: false
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
      - label: getEdgeConfigBackups
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfigBackups(ctx, operations.GetEdgeConfigBackupsRequest{\n        EdgeConfigID: \"<id>\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfigBackups
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfigBackups({
              edgeConfigId: "<id>",
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
              backups:
                allOf:
                  - items:
                      properties:
                        metadata:
                          properties:
                            updatedAt:
                              type: string
                            updatedBy:
                              type: string
                            itemsCount:
                              type: number
                            itemsBytes:
                              type: number
                          type: object
                        id:
                          type: string
                        lastModified:
                          type: number
                      required:
                        - id
                        - lastModified
                      type: object
                    type: array
              pagination:
                allOf:
                  - properties:
                      hasNext:
                        type: boolean
                      next:
                        type: string
                    required:
                      - hasNext
                    type: object
            requiredProperties:
              - backups
              - pagination
        examples:
          example:
            value:
              backups:
                - metadata:
                    updatedAt: <string>
                    updatedBy: <string>
                    itemsCount: 123
                    itemsBytes: 123
                  id: <string>
                  lastModified: 123
              pagination:
                hasNext: true
                next: <string>
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
title: "Get Edge Config items"

last_updated: "2025-11-07T00:37:11.617Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-items"
--------------------------------------------------------------------------------

# Get Edge Config items

> Returns all items of an Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/items
paths:
  path: /v1/edge-config/{edgeConfigId}/items
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
        edgeConfigId:
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
      - label: getEdgeConfigItems
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfigItems(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.EdgeConfigItem != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfigItems
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfigItems({
              edgeConfigId: "<id>",
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
                - $ref: '#/components/schemas/EdgeConfigItem'
        examples:
          example:
            value:
              - key: <string>
                value: <string>
                description: <string>
                edgeConfigId: <string>
                createdAt: 123
                updatedAt: 123
        description: List of all Edge Config items.
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
    EdgeConfigItem:
      properties:
        key:
          type: string
        value:
          $ref: '#/components/schemas/EdgeConfigItemValue'
        description:
          type: string
        edgeConfigId:
          type: string
        createdAt:
          type: number
        updatedAt:
          type: number
      required:
        - key
        - value
        - edgeConfigId
        - createdAt
        - updatedAt
      type: object
      description: The EdgeConfig.

````

--------------------------------------------------------------------------------
title: "Get Edge Config schema"

last_updated: "2025-11-07T00:37:11.662Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-schema"
--------------------------------------------------------------------------------

# Get Edge Config schema

> Returns the schema of an Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/schema
paths:
  path: /v1/edge-config/{edgeConfigId}/schema
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
        edgeConfigId:
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
      - label: getEdgeConfigSchema
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfigSchema(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfigSchema
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfigSchema({
              edgeConfigId: "<id>",
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
            description: The EdgeConfig.
          - type: 'null'
            description: The EdgeConfig.
        examples:
          example:
            value: {}
        description: The EdgeConfig.
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
title: "Get Edge Config token meta data"

last_updated: "2025-11-07T00:37:11.433Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-token-meta-data"
--------------------------------------------------------------------------------

# Get Edge Config token meta data

> Return meta data about an Edge Config token.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/token/{token}
paths:
  path: /v1/edge-config/{edgeConfigId}/token/{token}
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
        edgeConfigId:
          schema:
            - type: string
              required: true
        token:
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
      - label: getEdgeConfigToken
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfigToken(ctx, \"<id>\", \"<value>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.EdgeConfigToken != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfigToken
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfigToken({
              edgeConfigId: "<id>",
              token: "<value>",
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
              token:
                allOf:
                  - type: string
              label:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
                    description: >-
                      This is not the token itself, but rather an id to identify
                      the token by
              edgeConfigId:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
            description: The EdgeConfig.
            refIdentifier: '#/components/schemas/EdgeConfigToken'
            requiredProperties:
              - token
              - label
              - id
              - edgeConfigId
              - createdAt
        examples:
          example:
            value:
              token: <string>
              label: <string>
              id: <string>
              edgeConfigId: <string>
              createdAt: 123
        description: The EdgeConfig.
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
title: "Get Edge Configs"

last_updated: "2025-11-07T00:37:11.522Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/get-edge-configs"
--------------------------------------------------------------------------------

# Get Edge Configs

> Returns all Edge Configs.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config
paths:
  path: /v1/edge-config
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
      - label: getEdgeConfigs
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.GetEdgeConfigs(ctx, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.ResponseBodies != nil {\n        // handle response\n    }\n}"
      - label: getEdgeConfigs
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.getEdgeConfigs({
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
                    id:
                      type: string
                    createdAt:
                      type: number
                    ownerId:
                      type: string
                    slug:
                      type: string
                      description: >-
                        Name for the Edge Config Names are not unique. Must
                        start with an alphabetic character and can contain only
                        alphanumeric characters and underscores).
                    updatedAt:
                      type: number
                    digest:
                      type: string
                    transfer:
                      properties:
                        fromAccountId:
                          type: string
                        startedAt:
                          type: number
                        doneAt:
                          nullable: true
                          type: number
                      required:
                        - fromAccountId
                        - startedAt
                        - doneAt
                      type: object
                      description: >-
                        Keeps track of the current state of the Edge Config
                        while it gets transferred.
                    schema:
                      type: object
                    purpose:
                      properties:
                        type:
                          type: string
                          enum:
                            - flags
                        projectId:
                          type: string
                      required:
                        - type
                        - projectId
                      type: object
                    sizeInBytes:
                      type: number
                    itemCount:
                      type: number
                  required:
                    - sizeInBytes
                    - itemCount
            description: List of all edge configs.
        examples:
          example:
            value:
              - id: <string>
                createdAt: 123
                ownerId: <string>
                slug: <string>
                updatedAt: 123
                digest: <string>
                transfer:
                  fromAccountId: <string>
                  startedAt: 123
                  doneAt: 123
                schema: {}
                purpose:
                  type: flags
                  projectId: <string>
                sizeInBytes: 123
                itemCount: 123
        description: List of all edge configs.
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
title: "Update an Edge Config"

last_updated: "2025-11-07T00:37:11.525Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/update-an-edge-config"
--------------------------------------------------------------------------------

# Update an Edge Config

> Updates an Edge Config.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/edge-config/{edgeConfigId}
paths:
  path: /v1/edge-config/{edgeConfigId}
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
        edgeConfigId:
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              slug:
                allOf:
                  - maxLength: 64
                    pattern: ^[\\w-]+$
                    type: string
            required: true
            requiredProperties:
              - slug
        examples:
          example:
            value:
              slug: <string>
    codeSamples:
      - label: updateEdgeConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.UpdateEdgeConfig(ctx, \"<id>\", nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateEdgeConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.updateEdgeConfig({
              edgeConfigId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                slug: "<value>",
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
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
              deletedAt:
                allOf:
                  - nullable: true
                    type: number
              id:
                allOf:
                  - type: string
              slug:
                allOf:
                  - type: string
                    description: >-
                      Name for the Edge Config Names are not unique. Must start
                      with an alphabetic character and can contain only
                      alphanumeric characters and underscores).
              ownerId:
                allOf:
                  - type: string
              digest:
                allOf:
                  - type: string
              transfer:
                allOf:
                  - properties:
                      fromAccountId:
                        type: string
                      startedAt:
                        type: number
                      doneAt:
                        nullable: true
                        type: number
                    required:
                      - fromAccountId
                      - startedAt
                      - doneAt
                    type: object
                    description: >-
                      Keeps track of the current state of the Edge Config while
                      it gets transferred.
              schema:
                allOf:
                  - type: object
              purpose:
                allOf:
                  - oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - flags
                          projectId:
                            type: string
                        required:
                          - type
                          - projectId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - experimentation
                          resourceId:
                            type: string
                        required:
                          - type
                          - resourceId
                        type: object
              syncedToDynamoAt:
                allOf:
                  - type: number
                    description: >-
                      Timestamp of when the Edge Config was synced to DynamoDB
                      initially. It is only set when syncing the entire Edge
                      Config, not when updating.
              sizeInBytes:
                allOf:
                  - type: number
              itemCount:
                allOf:
                  - type: number
            description: An Edge Config
            requiredProperties:
              - createdAt
              - updatedAt
              - id
              - slug
              - ownerId
              - digest
              - sizeInBytes
              - itemCount
        examples:
          example:
            value:
              createdAt: 123
              updatedAt: 123
              deletedAt: 123
              id: <string>
              slug: <string>
              ownerId: <string>
              digest: <string>
              transfer:
                fromAccountId: <string>
                startedAt: 123
                doneAt: 123
              schema: {}
              purpose:
                type: flags
                projectId: <string>
              syncedToDynamoAt: 123
              sizeInBytes: 123
              itemCount: 123
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
title: "Update Edge Config items in batch"

last_updated: "2025-11-07T00:37:11.465Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/update-edge-config-items-in-batch"
--------------------------------------------------------------------------------

# Update Edge Config items in batch

> Update multiple Edge Config Items in batch.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/edge-config/{edgeConfigId}/items
paths:
  path: /v1/edge-config/{edgeConfigId}/items
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
        edgeConfigId:
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              items:
                allOf:
                  - type: array
                    items:
                      oneOf:
                        - type: object
                          properties:
                            operation:
                              enum:
                                - create
                                - update
                                - upsert
                                - delete
                            key:
                              maxLength: 256
                              pattern: ^[\\w-]+$
                              type: string
                            value:
                              nullable: true
                            description:
                              oneOf:
                                - type: string
                                  maxLength: 512
                                - {}
                              nullable: true
                          anyOf:
                            - properties:
                                operation:
                                  type: string
                                  enum:
                                    - create
                              required:
                                - operation
                                - key
                                - value
                            - properties:
                                operation:
                                  enum:
                                    - update
                                    - upsert
                              required:
                                - operation
                                - key
                                - value
                            - properties:
                                operation:
                                  enum:
                                    - update
                                    - upsert
                              required:
                                - operation
                                - key
                                - description
            requiredProperties:
              - items
            additionalProperties: false
        examples:
          example:
            value:
              items:
                - operation: create
                  key: <string>
                  value: <any>
                  description: <string>
    codeSamples:
      - label: patchEdgeConfigItems
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.patchEdgeConfigItems({
              edgeConfigId: "<id>",
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
              status:
                allOf:
                  - type: string
            requiredProperties:
              - status
        examples:
          example:
            value:
              status: <string>
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
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
    '409': {}
    '412': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update Edge Config schema"

last_updated: "2025-11-07T00:37:11.446Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/edge-config/update-edge-config-schema"
--------------------------------------------------------------------------------

# Update Edge Config schema

> Update an Edge Config's schema.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/edge-config/{edgeConfigId}/schema
paths:
  path: /v1/edge-config/{edgeConfigId}/schema
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
        edgeConfigId:
          schema:
            - type: string
              required: true
      query:
        dryRun:
          schema:
            - type: string
              required: false
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
              definition:
                allOf:
                  - {}
            required: true
            requiredProperties:
              - definition
            additionalProperties: false
        examples:
          example:
            value:
              definition: <any>
    codeSamples:
      - label: patchEdgeConfigSchema
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.EdgeConfig.PatchEdgeConfigSchema(ctx, operations.PatchEdgeConfigSchemaRequest{\n        EdgeConfigID: \"<id>\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: patchEdgeConfigSchema
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.edgeConfig.patchEdgeConfigSchema({
              edgeConfigId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                definition: "<value>",
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
            description: The JSON schema uploaded by the user
          - type: 'null'
            description: The JSON schema uploaded by the user
        examples:
          example:
            value: {}
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
title: "Create a custom environment for the current project."

last_updated: "2025-11-07T00:37:11.723Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/environment/create-a-custom-environment-for-the-current-project"
--------------------------------------------------------------------------------

# Create a custom environment for the current project.

> Creates a custom environment for the current project. Cannot be named 'Production' or 'Preview'.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v9/projects/{idOrName}/custom-environments
paths:
  path: /v9/projects/{idOrName}/custom-environments
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
              slug:
                allOf:
                  - description: The slug of the custom environment to create.
                    type: string
                    maxLength: 32
              description:
                allOf:
                  - description: Description of the custom environment. This is optional.
                    type: string
                    maxLength: 256
              branchMatcher:
                allOf:
                  - required:
                      - type
                      - pattern
                    description: >-
                      How we want to determine a matching branch. This is
                      optional.
                    type: object
                    properties:
                      type:
                        description: >-
                          Type of matcher. One of \"equals\", \"startsWith\", or
                          \"endsWith\".
                        enum:
                          - equals
                          - startsWith
                          - endsWith
                      pattern:
                        description: Git branch name or portion thereof.
                        type: string
                        maxLength: 100
              copyEnvVarsFrom:
                allOf:
                  - description: >-
                      Where to copy environment variables from. This is
                      optional.
                    type: string
        examples:
          example:
            value:
              slug: <string>
              description: <string>
              branchMatcher:
                type: equals
                pattern: <string>
              copyEnvVarsFrom: <string>
    codeSamples:
      - label: createCustomEnvironment
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.createCustomEnvironment({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: >-
                      Unique identifier for the custom environment (format:
                      env_*)
              slug:
                allOf:
                  - type: string
                    description: URL-friendly name of the environment
              type:
                allOf:
                  - type: string
                    enum:
                      - preview
                      - production
                      - development
                    description: >-
                      The type of environment (production, preview, or
                      development)
              description:
                allOf:
                  - type: string
                    description: Optional description of the environment's purpose
              branchMatcher:
                allOf:
                  - properties:
                      type:
                        type: string
                        enum:
                          - endsWith
                          - startsWith
                          - equals
                        description: The type of matching to perform
                      pattern:
                        type: string
                        description: The pattern to match against branch names
                    required:
                      - type
                      - pattern
                    type: object
                    description: >-
                      Configuration for matching git branches to this
                      environment
              domains:
                allOf:
                  - items:
                      properties:
                        name:
                          type: string
                        apexName:
                          type: string
                        projectId:
                          type: string
                        redirect:
                          nullable: true
                          type: string
                        redirectStatusCode:
                          nullable: true
                          type: number
                          enum:
                            - 307
                            - 301
                            - 302
                            - 308
                        gitBranch:
                          nullable: true
                          type: string
                        customEnvironmentId:
                          nullable: true
                          type: string
                        updatedAt:
                          type: number
                        createdAt:
                          type: number
                        verified:
                          type: boolean
                          description: >-
                            `true` if the domain is verified for use with the
                            project. If `false` it will not be used as an alias
                            on this project until the challenge in
                            `verification` is completed.
                        verification:
                          items:
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
                              A list of verification challenges, one of which
                              must be completed to verify the domain for use on
                              the project. After the challenge is complete `POST
                              /projects/:idOrName/domains/:domain/verify` to
                              verify the domain. Possible challenges: - If
                              `verification.type = TXT` the
                              `verification.domain` will be checked for a TXT
                              record matching `verification.value`.
                          type: array
                          description: >-
                            A list of verification challenges, one of which must
                            be completed to verify the domain for use on the
                            project. After the challenge is complete `POST
                            /projects/:idOrName/domains/:domain/verify` to
                            verify the domain. Possible challenges: - If
                            `verification.type = TXT` the `verification.domain`
                            will be checked for a TXT record matching
                            `verification.value`.
                      required:
                        - name
                        - apexName
                        - projectId
                        - verified
                      type: object
                      description: List of domains associated with this environment
                    type: array
                    description: List of domains associated with this environment
              currentDeploymentAliases:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: List of aliases for the current deployment
              createdAt:
                allOf:
                  - type: number
                    description: Timestamp when the environment was created
              updatedAt:
                allOf:
                  - type: number
                    description: Timestamp when the environment was last updated
            description: >-
              Internal representation of a custom environment with all required
              properties
            requiredProperties:
              - id
              - slug
              - type
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: <string>
              slug: <string>
              type: preview
              description: <string>
              branchMatcher:
                type: endsWith
                pattern: <string>
              domains:
                - name: <string>
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
              currentDeploymentAliases:
                - <string>
              createdAt: 123
              updatedAt: 123
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
title: "Create one or more shared environment variables"

last_updated: "2025-11-07T00:37:11.645Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/environment/create-one-or-more-shared-environment-variables"
--------------------------------------------------------------------------------

# Create one or more shared environment variables

> Creates shared environment variable(s) for a team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/env
paths:
  path: /v1/env
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
              evs:
                allOf:
                  - &ref_0
                    type: array
                    maximum: 50
                    minimum: 1
                    items:
                      type: object
                      required:
                        - key
                        - value
                      properties:
                        key:
                          description: The name of the Shared Environment Variable
                          type: string
                          example: API_URL
                        value:
                          description: The value of the Shared Environment Variable
                          type: string
                          example: https://api.vercel.com
                        comment:
                          type: string
                          description: >-
                            A comment to add context on what this Shared
                            Environment Variable is for
                          example: database connection string for production
                          maxLength: 500
              type:
                allOf:
                  - &ref_1
                    description: The type of environment variable
                    type: string
                    enum:
                      - encrypted
                      - sensitive
                    example: encrypted
              target:
                allOf:
                  - &ref_2
                    description: The target environment of the Shared Environment Variable
                    type: array
                    items:
                      enum:
                        - production
                        - preview
                        - development
                    example:
                      - production
                      - preview
              projectId:
                allOf:
                  - &ref_3
                    description: Associate a Shared Environment Variable to projects.
                    type: array
                    items:
                      type: string
                    example:
                      - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                      - prj_2WjyKQmM8ZnGcJsPWMrHRCRV
                    deprecated: true
            requiredProperties:
              - evs
              - target
          - type: object
            properties:
              evs:
                allOf:
                  - *ref_0
              type:
                allOf:
                  - *ref_1
              target:
                allOf:
                  - *ref_2
              projectId:
                allOf:
                  - *ref_3
            requiredProperties:
              - evs
              - applyToAllCustomEnvironments
        examples:
          example:
            value:
              evs:
                - key: API_URL
                  value: https://api.vercel.com
                  comment: database connection string for production
              type: encrypted
              target:
                - production
                - preview
              projectId:
                - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                - prj_2WjyKQmM8ZnGcJsPWMrHRCRV
    codeSamples:
      - label: createSharedEnvVariable
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.createSharedEnvVariable({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                evs: [],
                type: "encrypted",
                target: [
                  "production",
                  "preview",
                ],
              },
            });

            console.log(result);
          }

          run();
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              created:
                allOf:
                  - items:
                      properties:
                        created:
                          type: string
                          format: date-time
                          description: The date when the Shared Env Var was created.
                          example: '2021-02-10T13:11:49.180Z'
                        key:
                          type: string
                          description: The name of the Shared Env Var.
                          example: my-api-key
                        ownerId:
                          nullable: true
                          type: string
                          description: >-
                            The unique identifier of the owner (team) the Shared
                            Env Var was created for.
                          example: team_LLHUOMOoDlqOp8wPE4kFo9pE
                        id:
                          type: string
                          description: The unique identifier of the Shared Env Var.
                          example: env_XCG7t7AIHuO2SBA8667zNUiM
                        createdBy:
                          nullable: true
                          type: string
                          description: >-
                            The unique identifier of the user who created the
                            Shared Env Var.
                          example: 2qDDuGFTWXBLDNnqZfWPDp1A
                        deletedBy:
                          nullable: true
                          type: string
                          description: >-
                            The unique identifier of the user who deleted the
                            Shared Env Var.
                          example: 2qDDuGFTWXBLDNnqZfWPDp1A
                        updatedBy:
                          nullable: true
                          type: string
                          description: >-
                            The unique identifier of the user who last updated
                            the Shared Env Var.
                          example: 2qDDuGFTWXBLDNnqZfWPDp1A
                        createdAt:
                          type: number
                          description: Timestamp for when the Shared Env Var was created.
                          example: 1609492210000
                        deletedAt:
                          type: number
                          description: >-
                            Timestamp for when the Shared Env Var was (soft)
                            deleted.
                          example: 1609492210000
                        updatedAt:
                          type: number
                          description: >-
                            Timestamp for when the Shared Env Var was last
                            updated.
                          example: 1609492210000
                        value:
                          type: string
                          description: The value of the Shared Env Var.
                        projectId:
                          items:
                            type: string
                          type: array
                          description: >-
                            The unique identifiers of the projects which the
                            Shared Env Var is linked to.
                          example:
                            - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                            - prj_2WjyKQmM8ZnGcJsPWMrasEFg
                        type:
                          type: string
                          enum:
                            - encrypted
                            - sensitive
                            - system
                            - plain
                          description: >-
                            The type of this cosmos doc instance, if blank,
                            assume secret.
                          example: encrypted
                        target:
                          items:
                            type: string
                            enum:
                              - production
                              - preview
                              - development
                            description: environments this env variable targets
                            example: production
                          type: array
                          description: environments this env variable targets
                          example: production
                        applyToAllCustomEnvironments:
                          type: boolean
                          description: >-
                            whether or not this env varible applies to custom
                            environments
                        decrypted:
                          type: boolean
                          description: whether or not this env variable is decrypted
                        comment:
                          type: string
                          description: >-
                            A user provided comment that describes what this
                            Shared Env Var is for.
                        lastEditedByDisplayName:
                          type: string
                          description: The last editor full name or username.
                      type: object
                    type: array
              failed:
                allOf:
                  - items:
                      properties:
                        error:
                          properties:
                            code:
                              type: string
                            message:
                              type: string
                            key:
                              type: string
                            envVarId:
                              type: string
                            envVarKey:
                              type: string
                            action:
                              type: string
                            link:
                              type: string
                            value:
                              oneOf:
                                - type: string
                                - items:
                                    type: string
                                    enum:
                                      - production
                                      - preview
                                      - development
                                      - preview
                                      - development
                                  type: array
                            gitBranch:
                              type: string
                            target:
                              oneOf:
                                - items:
                                    type: string
                                    enum:
                                      - production
                                      - preview
                                      - development
                                      - preview
                                      - development
                                  type: array
                                - type: string
                                  enum:
                                    - production
                                    - preview
                                    - development
                                    - preview
                                    - development
                            project:
                              type: string
                          required:
                            - code
                            - message
                          type: object
                      required:
                        - error
                      type: object
                    type: array
            requiredProperties:
              - created
              - failed
        examples:
          example:
            value:
              created:
                - created: '2021-02-10T13:11:49.180Z'
                  key: my-api-key
                  ownerId: team_LLHUOMOoDlqOp8wPE4kFo9pE
                  id: env_XCG7t7AIHuO2SBA8667zNUiM
                  createdBy: 2qDDuGFTWXBLDNnqZfWPDp1A
                  deletedBy: 2qDDuGFTWXBLDNnqZfWPDp1A
                  updatedBy: 2qDDuGFTWXBLDNnqZfWPDp1A
                  createdAt: 1609492210000
                  deletedAt: 1609492210000
                  updatedAt: 1609492210000
                  value: <string>
                  projectId:
                    - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                    - prj_2WjyKQmM8ZnGcJsPWMrasEFg
                  type: encrypted
                  target: production
                  applyToAllCustomEnvironments: true
                  decrypted: true
                  comment: <string>
                  lastEditedByDisplayName: <string>
              failed:
                - error:
                    code: <string>
                    message: <string>
                    key: <string>
                    envVarId: <string>
                    envVarKey: <string>
                    action: <string>
                    link: <string>
                    value: <string>
                    gitBranch: <string>
                    target:
                      - production
                    project: <string>
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
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Delete one or more Env Var"

last_updated: "2025-11-07T00:37:11.471Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/environment/delete-one-or-more-env-var"
--------------------------------------------------------------------------------

# Delete one or more Env Var

> Deletes one or many Shared Environment Variables for a given team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/env
paths:
  path: /v1/env
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
              ids:
                allOf:
                  - description: IDs of the Shared Environment Variables to delete
                    minimum: 1
                    maximum: 50
                    type: array
                    items:
                      type: string
                    example:
                      - env_abc123
                      - env_abc124
            requiredProperties:
              - ids
        examples:
          example:
            value:
              ids:
                - env_abc123
                - env_abc124
    codeSamples:
      - label: deleteSharedEnvVariable
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.deleteSharedEnvVariable({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                ids: [
                  "env_abc123",
                  "env_abc124",
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
              deleted:
                allOf:
                  - items:
                      type: string
                    type: array
              failed:
                allOf:
                  - items:
                      properties:
                        error:
                          properties:
                            code:
                              type: string
                            message:
                              type: string
                            key:
                              type: string
                            envVarId:
                              type: string
                            envVarKey:
                              type: string
                            action:
                              type: string
                            link:
                              type: string
                            value:
                              oneOf:
                                - type: string
                                - items:
                                    type: string
                                    enum:
                                      - production
                                      - preview
                                      - development
                                      - preview
                                      - development
                                  type: array
                            gitBranch:
                              type: string
                            target:
                              oneOf:
                                - items:
                                    type: string
                                    enum:
                                      - production
                                      - preview
                                      - development
                                      - preview
                                      - development
                                  type: array
                                - type: string
                                  enum:
                                    - production
                                    - preview
                                    - development
                                    - preview
                                    - development
                            project:
                              type: string
                          required:
                            - code
                            - message
                          type: object
                      required:
                        - error
                      type: object
                    type: array
            requiredProperties:
              - deleted
              - failed
        examples:
          example:
            value:
              deleted:
                - <string>
              failed:
                - error:
                    code: <string>
                    message: <string>
                    key: <string>
                    envVarId: <string>
                    envVarKey: <string>
                    action: <string>
                    link: <string>
                    value: <string>
                    gitBranch: <string>
                    target:
                      - production
                    project: <string>
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
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Disconnects a shared environment variable for a given project"

last_updated: "2025-11-07T00:37:12.265Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/environment/disconnects-a-shared-environment-variable-for-a-given-project"
--------------------------------------------------------------------------------

# Disconnects a shared environment variable for a given project

> Disconnects a shared environment variable for a given project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/env/{id}/unlink/{projectId}
paths:
  path: /v1/env/{id}/unlink/{projectId}
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
        id:
          schema:
            - type: string
              required: true
              description: >-
                The unique ID for the Shared Environment Variable to unlink from
                the project.
        projectId:
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
      - label: unlinkSharedEnvVariable
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.unlinkSharedEnvVariable({
              id: "<id>",
              projectId: "<id>",
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
title: "Lists all Shared Environment Variables for a team"

last_updated: "2025-11-07T00:37:12.160Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/environment/lists-all-shared-environment-variables-for-a-team"
--------------------------------------------------------------------------------

# Lists all Shared Environment Variables for a team

> Lists all Shared Environment Variables for a team, taking into account optional filters.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/env
paths:
  path: /v1/env
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
        search:
          schema:
            - type: string
        projectId:
          schema:
            - type: string
              description: Filter SharedEnvVariables that belong to a project
              example: prj_2WjyKQmM8ZnGcJsPWMrHRHrE
        ids:
          schema:
            - type: string
              description: Filter SharedEnvVariables based on comma separated ids
              example: env_2WjyKQmM8ZnGcJsPWMrHRHrE,env_2WjyKQmM8ZnGcJsPWMrHRCRV
        exclude_ids:
          schema:
            - type: string
              description: Filter SharedEnvVariables based on comma separated ids
              example: env_2WjyKQmM8ZnGcJsPWMrHRHrE,env_2WjyKQmM8ZnGcJsPWMrHRCRV
        exclude-ids:
          schema:
            - type: string
              description: Filter SharedEnvVariables based on comma separated ids
              example: env_2WjyKQmM8ZnGcJsPWMrHRHrE,env_2WjyKQmM8ZnGcJsPWMrHRCRV
        exclude_projectId:
          schema:
            - type: string
              description: Filter SharedEnvVariables that belong to a project
              example: prj_2WjyKQmM8ZnGcJsPWMrHRHrE
        exclude-projectId:
          schema:
            - type: string
              description: Filter SharedEnvVariables that belong to a project
              example: prj_2WjyKQmM8ZnGcJsPWMrHRHrE
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
      - label: listSharedEnvVariable
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.listSharedEnvVariable({
              projectId: "prj_2WjyKQmM8ZnGcJsPWMrHRHrE",
              ids: "env_2WjyKQmM8ZnGcJsPWMrHRHrE,env_2WjyKQmM8ZnGcJsPWMrHRCRV",
              excludeIdsQueryParameter: "env_2WjyKQmM8ZnGcJsPWMrHRHrE,env_2WjyKQmM8ZnGcJsPWMrHRCRV",
              excludeIdsQueryParameter1: "env_2WjyKQmM8ZnGcJsPWMrHRHrE,env_2WjyKQmM8ZnGcJsPWMrHRCRV",
              excludeProjectIdQueryParameter: "prj_2WjyKQmM8ZnGcJsPWMrHRHrE",
              excludeProjectIdQueryParameter1: "prj_2WjyKQmM8ZnGcJsPWMrHRHrE",
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
              data:
                allOf:
                  - items:
                      properties:
                        created:
                          type: string
                          format: date-time
                          description: The date when the Shared Env Var was created.
                          example: '2021-02-10T13:11:49.180Z'
                        key:
                          type: string
                          description: The name of the Shared Env Var.
                          example: my-api-key
                        ownerId:
                          nullable: true
                          type: string
                          description: >-
                            The unique identifier of the owner (team) the Shared
                            Env Var was created for.
                          example: team_LLHUOMOoDlqOp8wPE4kFo9pE
                        id:
                          type: string
                          description: The unique identifier of the Shared Env Var.
                          example: env_XCG7t7AIHuO2SBA8667zNUiM
                        createdBy:
                          nullable: true
                          type: string
                          description: >-
                            The unique identifier of the user who created the
                            Shared Env Var.
                          example: 2qDDuGFTWXBLDNnqZfWPDp1A
                        deletedBy:
                          nullable: true
                          type: string
                          description: >-
                            The unique identifier of the user who deleted the
                            Shared Env Var.
                          example: 2qDDuGFTWXBLDNnqZfWPDp1A
                        updatedBy:
                          nullable: true
                          type: string
                          description: >-
                            The unique identifier of the user who last updated
                            the Shared Env Var.
                          example: 2qDDuGFTWXBLDNnqZfWPDp1A
                        createdAt:
                          type: number
                          description: Timestamp for when the Shared Env Var was created.
                          example: 1609492210000
                        deletedAt:
                          type: number
                          description: >-
                            Timestamp for when the Shared Env Var was (soft)
                            deleted.
                          example: 1609492210000
                        updatedAt:
                          type: number
                          description: >-
                            Timestamp for when the Shared Env Var was last
                            updated.
                          example: 1609492210000
                        value:
                          type: string
                          description: The value of the Shared Env Var.
                        projectId:
                          items:
                            type: string
                          type: array
                          description: >-
                            The unique identifiers of the projects which the
                            Shared Env Var is linked to.
                          example:
                            - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                            - prj_2WjyKQmM8ZnGcJsPWMrasEFg
                        type:
                          type: string
                          enum:
                            - encrypted
                            - sensitive
                            - system
                            - plain
                          description: >-
                            The type of this cosmos doc instance, if blank,
                            assume secret.
                          example: encrypted
                        target:
                          items:
                            type: string
                            enum:
                              - production
                              - preview
                              - development
                            description: environments this env variable targets
                            example: production
                          type: array
                          description: environments this env variable targets
                          example: production
                        applyToAllCustomEnvironments:
                          type: boolean
                          description: >-
                            whether or not this env varible applies to custom
                            environments
                        decrypted:
                          type: boolean
                          description: whether or not this env variable is decrypted
                        comment:
                          type: string
                          description: >-
                            A user provided comment that describes what this
                            Shared Env Var is for.
                        lastEditedByDisplayName:
                          type: string
                          description: The last editor full name or username.
                      type: object
                    type: array
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            requiredProperties:
              - data
              - pagination
        examples:
          example:
            value:
              data:
                - created: '2021-02-10T13:11:49.180Z'
                  key: my-api-key
                  ownerId: team_LLHUOMOoDlqOp8wPE4kFo9pE
                  id: env_XCG7t7AIHuO2SBA8667zNUiM
                  createdBy: 2qDDuGFTWXBLDNnqZfWPDp1A
                  deletedBy: 2qDDuGFTWXBLDNnqZfWPDp1A
                  updatedBy: 2qDDuGFTWXBLDNnqZfWPDp1A
                  createdAt: 1609492210000
                  deletedAt: 1609492210000
                  updatedAt: 1609492210000
                  value: <string>
                  projectId:
                    - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                    - prj_2WjyKQmM8ZnGcJsPWMrasEFg
                  type: encrypted
                  target: production
                  applyToAllCustomEnvironments: true
                  decrypted: true
                  comment: <string>
                  lastEditedByDisplayName: <string>
              pagination:
                count: 20
                next: 1540095775951
                prev: 1540095775951
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
  schemas:
    Pagination:
      properties:
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
          description: Timestamp that must be used to request the previous page.
          example: 1540095775951
      required:
        - count
        - next
        - prev
      type: object
      description: >-
        This object contains information related to the pagination of the
        current request, including the necessary parameters to get the next or
        previous page of data.

````

--------------------------------------------------------------------------------
title: "Remove a custom environment"

last_updated: "2025-11-07T00:37:12.263Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/environment/remove-a-custom-environment"
--------------------------------------------------------------------------------

# Remove a custom environment

> Remove a custom environment for the project. Must not be named 'Production' or 'Preview'.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v9/projects/{idOrName}/custom-environments/{environmentSlugOrId}
paths:
  path: /v9/projects/{idOrName}/custom-environments/{environmentSlugOrId}
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
        environmentSlugOrId:
          schema:
            - type: string
              required: true
              description: The unique custom environment identifier within the project
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
              deleteUnassignedEnvironmentVariables:
                allOf:
                  - description: >-
                      Delete Environment Variables that are not assigned to any
                      environments.
                    type: boolean
        examples:
          example:
            value:
              deleteUnassignedEnvironmentVariables: true
    codeSamples:
      - label: removeCustomEnvironment
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.removeCustomEnvironment({
              idOrName: "<value>",
              environmentSlugOrId: "<id>",
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
                    description: >-
                      Unique identifier for the custom environment (format:
                      env_*)
              slug:
                allOf:
                  - type: string
                    description: URL-friendly name of the environment
              type:
                allOf:
                  - type: string
                    enum:
                      - preview
                      - production
                      - development
                    description: >-
                      The type of environment (production, preview, or
                      development)
              description:
                allOf:
                  - type: string
                    description: Optional description of the environment's purpose
              branchMatcher:
                allOf:
                  - properties:
                      type:
                        type: string
                        enum:
                          - endsWith
                          - startsWith
                          - equals
                        description: The type of matching to perform
                      pattern:
                        type: string
                        description: The pattern to match against branch names
                    required:
                      - type
                      - pattern
                    type: object
                    description: >-
                      Configuration for matching git branches to this
                      environment
              domains:
                allOf:
                  - items:
                      properties:
                        name:
                          type: string
                        apexName:
                          type: string
                        projectId:
                          type: string
                        redirect:
                          nullable: true
                          type: string
                        redirectStatusCode:
                          nullable: true
                          type: number
                          enum:
                            - 307
                            - 301
                            - 302
                            - 308
                        gitBranch:
                          nullable: true
                          type: string
                        customEnvironmentId:
                          nullable: true
                          type: string
                        updatedAt:
                          type: number
                        createdAt:
                          type: number
                        verified:
                          type: boolean
                          description: >-
                            `true` if the domain is verified for use with the
                            project. If `false` it will not be used as an alias
                            on this project until the challenge in
                            `verification` is completed.
                        verification:
                          items:
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
                              A list of verification challenges, one of which
                              must be completed to verify the domain for use on
                              the project. After the challenge is complete `POST
                              /projects/:idOrName/domains/:domain/verify` to
                              verify the domain. Possible challenges: - If
                              `verification.type = TXT` the
                              `verification.domain` will be checked for a TXT
                              record matching `verification.value`.
                          type: array
                          description: >-
                            A list of verification challenges, one of which must
                            be completed to verify the domain for use on the
                            project. After the challenge is complete `POST
                            /projects/:idOrName/domains/:domain/verify` to
                            verify the domain. Possible challenges: - If
                            `verification.type = TXT` the `verification.domain`
                            will be checked for a TXT record matching
                            `verification.value`.
                      required:
                        - name
                        - apexName
                        - projectId
                        - verified
                      type: object
                      description: List of domains associated with this environment
                    type: array
                    description: List of domains associated with this environment
              currentDeploymentAliases:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: List of aliases for the current deployment
              createdAt:
                allOf:
                  - type: number
                    description: Timestamp when the environment was created
              updatedAt:
                allOf:
                  - type: number
                    description: Timestamp when the environment was last updated
            description: >-
              Internal representation of a custom environment with all required
              properties
            requiredProperties:
              - id
              - slug
              - type
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: <string>
              slug: <string>
              type: preview
              description: <string>
              branchMatcher:
                type: endsWith
                pattern: <string>
              domains:
                - name: <string>
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
              currentDeploymentAliases:
                - <string>
              createdAt: 123
              updatedAt: 123
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
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Retrieve a custom environment"

last_updated: "2025-11-07T00:37:12.167Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/environment/retrieve-a-custom-environment"
--------------------------------------------------------------------------------

# Retrieve a custom environment

> Retrieve a custom environment for the project. Must not be named 'Production' or 'Preview'.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v9/projects/{idOrName}/custom-environments/{environmentSlugOrId}
paths:
  path: /v9/projects/{idOrName}/custom-environments/{environmentSlugOrId}
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
              description: The unique project identifier or the project name
        environmentSlugOrId:
          schema:
            - type: string
              required: true
              description: The unique custom environment identifier within the project
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
      - label: getCustomEnvironment
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.getCustomEnvironment({
              idOrName: "<value>",
              environmentSlugOrId: "<id>",
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
                    description: >-
                      Unique identifier for the custom environment (format:
                      env_*)
              slug:
                allOf:
                  - type: string
                    description: URL-friendly name of the environment
              type:
                allOf:
                  - type: string
                    enum:
                      - preview
                      - production
                      - development
                    description: >-
                      The type of environment (production, preview, or
                      development)
              description:
                allOf:
                  - type: string
                    description: Optional description of the environment's purpose
              branchMatcher:
                allOf:
                  - properties:
                      type:
                        type: string
                        enum:
                          - endsWith
                          - startsWith
                          - equals
                        description: The type of matching to perform
                      pattern:
                        type: string
                        description: The pattern to match against branch names
                    required:
                      - type
                      - pattern
                    type: object
                    description: >-
                      Configuration for matching git branches to this
                      environment
              domains:
                allOf:
                  - items:
                      properties:
                        name:
                          type: string
                        apexName:
                          type: string
                        projectId:
                          type: string
                        redirect:
                          nullable: true
                          type: string
                        redirectStatusCode:
                          nullable: true
                          type: number
                          enum:
                            - 307
                            - 301
                            - 302
                            - 308
                        gitBranch:
                          nullable: true
                          type: string
                        customEnvironmentId:
                          nullable: true
                          type: string
                        updatedAt:
                          type: number
                        createdAt:
                          type: number
                        verified:
                          type: boolean
                          description: >-
                            `true` if the domain is verified for use with the
                            project. If `false` it will not be used as an alias
                            on this project until the challenge in
                            `verification` is completed.
                        verification:
                          items:
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
                              A list of verification challenges, one of which
                              must be completed to verify the domain for use on
                              the project. After the challenge is complete `POST
                              /projects/:idOrName/domains/:domain/verify` to
                              verify the domain. Possible challenges: - If
                              `verification.type = TXT` the
                              `verification.domain` will be checked for a TXT
                              record matching `verification.value`.
                          type: array
                          description: >-
                            A list of verification challenges, one of which must
                            be completed to verify the domain for use on the
                            project. After the challenge is complete `POST
                            /projects/:idOrName/domains/:domain/verify` to
                            verify the domain. Possible challenges: - If
                            `verification.type = TXT` the `verification.domain`
                            will be checked for a TXT record matching
                            `verification.value`.
                      required:
                        - name
                        - apexName
                        - projectId
                        - verified
                      type: object
                      description: List of domains associated with this environment
                    type: array
                    description: List of domains associated with this environment
              currentDeploymentAliases:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: List of aliases for the current deployment
              createdAt:
                allOf:
                  - type: number
                    description: Timestamp when the environment was created
              updatedAt:
                allOf:
                  - type: number
                    description: Timestamp when the environment was last updated
            description: >-
              Internal representation of a custom environment with all required
              properties
            requiredProperties:
              - id
              - slug
              - type
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: <string>
              slug: <string>
              type: preview
              description: <string>
              branchMatcher:
                type: endsWith
                pattern: <string>
              domains:
                - name: <string>
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
              currentDeploymentAliases:
                - <string>
              createdAt: 123
              updatedAt: 123
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
title: "Retrieve custom environments"

last_updated: "2025-11-07T00:37:12.191Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/environment/retrieve-custom-environments"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./22-update-auto-renew-for-a-domain.md) | [Index](./index.md) | [Next →](./24-retrieve-custom-environments.md)
