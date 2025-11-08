**Navigation:** [← Previous](./31-retrieve-a-list-of-projects.md) | [Index](./index.md) | [Next →](./33-update-an-existing-project.md)

---

# Retrieve the decrypted value of an environment variable of a project by id

> Retrieve the environment variable for a given project.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/env/{id}
paths:
  path: /v1/projects/{idOrName}/env/{id}
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
              example: prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA
        id:
          schema:
            - type: string
              required: true
              description: >-
                The unique ID for the environment variable to get the decrypted
                value.
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
      - label: getProjectEnv
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.GetProjectEnv(ctx, \"prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA\", \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: getProjectEnv
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.getProjectEnv({
              idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",
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
              decrypted:
                allOf:
                  - type: boolean
              target:
                allOf:
                  - oneOf:
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
              type:
                allOf:
                  - type: string
                    enum:
                      - system
                      - encrypted
                      - plain
                      - sensitive
                      - secret
              sunsetSecretId:
                allOf:
                  - type: string
                    description: >-
                      This is used to identiy variables that have been migrated
                      from type secret to sensitive.
              id:
                allOf:
                  - type: string
              key:
                allOf:
                  - type: string
              configurationId:
                allOf:
                  - nullable: true
                    type: string
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
              createdBy:
                allOf:
                  - nullable: true
                    type: string
              updatedBy:
                allOf:
                  - nullable: true
                    type: string
              gitBranch:
                allOf:
                  - type: string
              edgeConfigId:
                allOf:
                  - nullable: true
                    type: string
              edgeConfigTokenId:
                allOf:
                  - nullable: true
                    type: string
              contentHint:
                allOf:
                  - nullable: true
                    oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-read-only-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - blob-read-write-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url-non-pooling
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-prisma-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-user
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-host
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-password
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-database
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url-no-ssl
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - integration-store-secret
                          storeId:
                            type: string
                          integrationId:
                            type: string
                          integrationProductId:
                            type: string
                          integrationConfigurationId:
                            type: string
                        required:
                          - type
                          - storeId
                          - integrationId
                          - integrationProductId
                          - integrationConfigurationId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - flags-connection-string
                          projectId:
                            type: string
                        required:
                          - type
                          - projectId
                        type: object
              internalContentHint:
                allOf:
                  - nullable: true
                    properties:
                      type:
                        type: string
                        enum:
                          - flags-secret
                      encryptedValue:
                        type: string
                        description: >-
                          Contains the `value` of the env variable, encrypted
                          with a special key to make decryption possible in the
                          subscriber Lambda.
                    required:
                      - type
                      - encryptedValue
                    type: object
                    description: >-
                      Similar to `contentHints`, but should not be exposed to
                      the user.
              comment:
                allOf:
                  - type: string
              customEnvironmentIds:
                allOf:
                  - items:
                      type: string
                    type: array
            requiredProperties:
              - decrypted
              - type
              - key
          - type: object
            properties:
              target:
                allOf:
                  - oneOf:
                      - items:
                          type: string
                          enum:
                            - production
                            - preview
                            - development
                        type: array
                      - type: string
                        enum:
                          - production
                          - preview
                          - development
              type:
                allOf:
                  - type: string
                    enum:
                      - system
                      - encrypted
                      - plain
                      - sensitive
                      - secret
              sunsetSecretId:
                allOf:
                  - type: string
                    description: >-
                      This is used to identiy variables that have been migrated
                      from type secret to sensitive.
              decrypted:
                allOf:
                  - type: boolean
              value:
                allOf:
                  - type: string
              vsmValue:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
              key:
                allOf:
                  - type: string
              configurationId:
                allOf:
                  - nullable: true
                    type: string
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
              createdBy:
                allOf:
                  - nullable: true
                    type: string
              updatedBy:
                allOf:
                  - nullable: true
                    type: string
              gitBranch:
                allOf:
                  - type: string
              edgeConfigId:
                allOf:
                  - nullable: true
                    type: string
              edgeConfigTokenId:
                allOf:
                  - nullable: true
                    type: string
              contentHint:
                allOf:
                  - nullable: true
                    oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-read-only-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - blob-read-write-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url-non-pooling
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-prisma-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-user
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-host
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-password
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-database
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url-no-ssl
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - integration-store-secret
                          storeId:
                            type: string
                          integrationId:
                            type: string
                          integrationProductId:
                            type: string
                          integrationConfigurationId:
                            type: string
                        required:
                          - type
                          - storeId
                          - integrationId
                          - integrationProductId
                          - integrationConfigurationId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - flags-connection-string
                          projectId:
                            type: string
                        required:
                          - type
                          - projectId
                        type: object
              internalContentHint:
                allOf:
                  - nullable: true
                    properties:
                      type:
                        type: string
                        enum:
                          - flags-secret
                      encryptedValue:
                        type: string
                        description: >-
                          Contains the `value` of the env variable, encrypted
                          with a special key to make decryption possible in the
                          subscriber Lambda.
                    required:
                      - type
                      - encryptedValue
                    type: object
                    description: >-
                      Similar to `contentHints`, but should not be exposed to
                      the user.
              comment:
                allOf:
                  - type: string
              customEnvironmentIds:
                allOf:
                  - items:
                      type: string
                    type: array
            requiredProperties:
              - type
              - value
              - key
          - type: object
            properties:
              target:
                allOf:
                  - oneOf:
                      - items:
                          type: string
                        type: array
                      - type: string
                        enum:
                          - production
                          - preview
                          - development
              type:
                allOf:
                  - type: string
                    enum:
                      - system
                      - encrypted
                      - plain
                      - sensitive
                      - secret
              sunsetSecretId:
                allOf:
                  - type: string
                    description: >-
                      This is used to identiy variables that have been migrated
                      from type secret to sensitive.
              decrypted:
                allOf:
                  - type: boolean
              value:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
              key:
                allOf:
                  - type: string
              configurationId:
                allOf:
                  - nullable: true
                    type: string
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
              createdBy:
                allOf:
                  - nullable: true
                    type: string
              updatedBy:
                allOf:
                  - nullable: true
                    type: string
              gitBranch:
                allOf:
                  - type: string
              edgeConfigId:
                allOf:
                  - nullable: true
                    type: string
              edgeConfigTokenId:
                allOf:
                  - nullable: true
                    type: string
              contentHint:
                allOf:
                  - nullable: true
                    oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-read-only-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - blob-read-write-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url-non-pooling
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-prisma-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-user
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-host
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-password
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-database
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url-no-ssl
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - integration-store-secret
                          storeId:
                            type: string
                          integrationId:
                            type: string
                          integrationProductId:
                            type: string
                          integrationConfigurationId:
                            type: string
                        required:
                          - type
                          - storeId
                          - integrationId
                          - integrationProductId
                          - integrationConfigurationId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - flags-connection-string
                          projectId:
                            type: string
                        required:
                          - type
                          - projectId
                        type: object
              internalContentHint:
                allOf:
                  - nullable: true
                    properties:
                      type:
                        type: string
                        enum:
                          - flags-secret
                      encryptedValue:
                        type: string
                        description: >-
                          Contains the `value` of the env variable, encrypted
                          with a special key to make decryption possible in the
                          subscriber Lambda.
                    required:
                      - type
                      - encryptedValue
                    type: object
                    description: >-
                      Similar to `contentHints`, but should not be exposed to
                      the user.
              comment:
                allOf:
                  - type: string
              customEnvironmentIds:
                allOf:
                  - items:
                      type: string
                    type: array
            requiredProperties:
              - type
              - value
              - key
        examples:
          example:
            value:
              decrypted: true
              target:
                - production
              type: system
              sunsetSecretId: <string>
              id: <string>
              key: <string>
              configurationId: <string>
              createdAt: 123
              updatedAt: 123
              createdBy: <string>
              updatedBy: <string>
              gitBranch: <string>
              edgeConfigId: <string>
              edgeConfigTokenId: <string>
              contentHint:
                type: redis-url
                storeId: <string>
              internalContentHint:
                type: flags-secret
                encryptedValue: <string>
              comment: <string>
              customEnvironmentIds:
                - <string>
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
title: "Retrieve the environment variables of a project by id or name"

last_updated: "2025-11-07T00:37:14.506Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name"
--------------------------------------------------------------------------------

# Retrieve the environment variables of a project by id or name

> Retrieve the environment variables for a given project by passing either the project `id` or `name` in the URL.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v10/projects/{idOrName}/env
paths:
  path: /v10/projects/{idOrName}/env
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
              example: prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA
      query:
        gitBranch:
          schema:
            - type: string
              required: false
              description: >-
                If defined, the git branch of the environment variable to filter
                the results (must have target=preview)
              maxLength: 250
              example: feature-1
        decrypt:
          schema:
            - type: enum<string>
              enum:
                - 'true'
                - 'false'
              required: false
              description: If true, the environment variable value will be decrypted
              deprecated: true
              example: 'true'
        source:
          schema:
            - type: string
              required: false
              description: The source that is calling the endpoint.
              example: vercel-cli:pull
        customEnvironmentId:
          schema:
            - type: string
              required: false
              description: The unique custom environment identifier within the project
              example: env_123abc4567
        customEnvironmentSlug:
          schema:
            - type: string
              required: false
              description: The custom environment slug (name) within the project
              example: my-custom-env
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
      - label: filterProjectEnvs
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.filterProjectEnvs({
              idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",
              gitBranch: "feature-1",
              decrypt: "true",
              source: "vercel-cli:pull",
              customEnvironmentId: "env_123abc4567",
              customEnvironmentSlug: "my-custom-env",
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
              target:
                allOf:
                  - oneOf:
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
              type:
                allOf:
                  - type: string
                    enum:
                      - system
                      - encrypted
                      - plain
                      - sensitive
                      - secret
              sunsetSecretId:
                allOf:
                  - type: string
                    description: >-
                      This is used to identiy variables that have been migrated
                      from type secret to sensitive.
              decrypted:
                allOf:
                  - type: boolean
              value:
                allOf:
                  - type: string
              vsmValue:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
              key:
                allOf:
                  - type: string
              configurationId:
                allOf:
                  - nullable: true
                    type: string
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
              createdBy:
                allOf:
                  - nullable: true
                    type: string
              updatedBy:
                allOf:
                  - nullable: true
                    type: string
              gitBranch:
                allOf:
                  - type: string
              edgeConfigId:
                allOf:
                  - nullable: true
                    type: string
              edgeConfigTokenId:
                allOf:
                  - nullable: true
                    type: string
              contentHint:
                allOf:
                  - nullable: true
                    oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-read-only-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - blob-read-write-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url-non-pooling
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-prisma-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-user
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-host
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-password
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-database
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url-no-ssl
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - integration-store-secret
                          storeId:
                            type: string
                          integrationId:
                            type: string
                          integrationProductId:
                            type: string
                          integrationConfigurationId:
                            type: string
                        required:
                          - type
                          - storeId
                          - integrationId
                          - integrationProductId
                          - integrationConfigurationId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - flags-connection-string
                          projectId:
                            type: string
                        required:
                          - type
                          - projectId
                        type: object
              internalContentHint:
                allOf:
                  - nullable: true
                    properties:
                      type:
                        type: string
                        enum:
                          - flags-secret
                      encryptedValue:
                        type: string
                        description: >-
                          Contains the `value` of the env variable, encrypted
                          with a special key to make decryption possible in the
                          subscriber Lambda.
                    required:
                      - type
                      - encryptedValue
                    type: object
                    description: >-
                      Similar to `contentHints`, but should not be exposed to
                      the user.
              comment:
                allOf:
                  - type: string
              customEnvironmentIds:
                allOf:
                  - items:
                      type: string
                    type: array
              system:
                allOf:
                  - type: boolean
            requiredProperties:
              - type
              - value
              - key
          - type: object
            properties:
              envs:
                allOf:
                  - items:
                      properties:
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
                        type:
                          type: string
                          enum:
                            - system
                            - encrypted
                            - plain
                            - sensitive
                            - secret
                        sunsetSecretId:
                          type: string
                          description: >-
                            This is used to identiy variables that have been
                            migrated from type secret to sensitive.
                        decrypted:
                          type: boolean
                        value:
                          type: string
                        vsmValue:
                          type: string
                        id:
                          type: string
                        key:
                          type: string
                        configurationId:
                          nullable: true
                          type: string
                        createdAt:
                          type: number
                        updatedAt:
                          type: number
                        createdBy:
                          nullable: true
                          type: string
                        updatedBy:
                          nullable: true
                          type: string
                        gitBranch:
                          type: string
                        edgeConfigId:
                          nullable: true
                          type: string
                        edgeConfigTokenId:
                          nullable: true
                          type: string
                        contentHint:
                          nullable: true
                          oneOf:
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-token
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-read-only-token
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - blob-read-write-token
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url-non-pooling
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-prisma-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-user
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-host
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-password
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-database
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url-no-ssl
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - integration-store-secret
                                storeId:
                                  type: string
                                integrationId:
                                  type: string
                                integrationProductId:
                                  type: string
                                integrationConfigurationId:
                                  type: string
                              required:
                                - type
                                - storeId
                                - integrationId
                                - integrationProductId
                                - integrationConfigurationId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - flags-connection-string
                                projectId:
                                  type: string
                              required:
                                - type
                                - projectId
                              type: object
                        internalContentHint:
                          nullable: true
                          properties:
                            type:
                              type: string
                              enum:
                                - flags-secret
                            encryptedValue:
                              type: string
                              description: >-
                                Contains the `value` of the env variable,
                                encrypted with a special key to make decryption
                                possible in the subscriber Lambda.
                          required:
                            - type
                            - encryptedValue
                          type: object
                          description: >-
                            Similar to `contentHints`, but should not be exposed
                            to the user.
                        comment:
                          type: string
                        customEnvironmentIds:
                          items:
                            type: string
                          type: array
                        system:
                          type: boolean
                      required:
                        - type
                        - value
                        - key
                      type: object
                    type: array
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            requiredProperties:
              - envs
              - pagination
          - type: object
            properties:
              envs:
                allOf:
                  - items:
                      properties:
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
                        type:
                          type: string
                          enum:
                            - system
                            - encrypted
                            - plain
                            - sensitive
                            - secret
                        sunsetSecretId:
                          type: string
                          description: >-
                            This is used to identiy variables that have been
                            migrated from type secret to sensitive.
                        decrypted:
                          type: boolean
                        value:
                          type: string
                        vsmValue:
                          type: string
                        id:
                          type: string
                        key:
                          type: string
                        configurationId:
                          nullable: true
                          type: string
                        createdAt:
                          type: number
                        updatedAt:
                          type: number
                        createdBy:
                          nullable: true
                          type: string
                        updatedBy:
                          nullable: true
                          type: string
                        gitBranch:
                          type: string
                        edgeConfigId:
                          nullable: true
                          type: string
                        edgeConfigTokenId:
                          nullable: true
                          type: string
                        contentHint:
                          nullable: true
                          oneOf:
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-token
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-read-only-token
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - blob-read-write-token
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url-non-pooling
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-prisma-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-user
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-host
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-password
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-database
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url-no-ssl
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - integration-store-secret
                                storeId:
                                  type: string
                                integrationId:
                                  type: string
                                integrationProductId:
                                  type: string
                                integrationConfigurationId:
                                  type: string
                              required:
                                - type
                                - storeId
                                - integrationId
                                - integrationProductId
                                - integrationConfigurationId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - flags-connection-string
                                projectId:
                                  type: string
                              required:
                                - type
                                - projectId
                              type: object
                        internalContentHint:
                          nullable: true
                          properties:
                            type:
                              type: string
                              enum:
                                - flags-secret
                            encryptedValue:
                              type: string
                              description: >-
                                Contains the `value` of the env variable,
                                encrypted with a special key to make decryption
                                possible in the subscriber Lambda.
                          required:
                            - type
                            - encryptedValue
                          type: object
                          description: >-
                            Similar to `contentHints`, but should not be exposed
                            to the user.
                        comment:
                          type: string
                        customEnvironmentIds:
                          items:
                            type: string
                          type: array
                        system:
                          type: boolean
                      required:
                        - type
                        - value
                        - key
                      type: object
                    type: array
            description: The list of environment variables for the given project
            requiredProperties:
              - envs
        examples:
          example:
            value:
              target:
                - production
              type: system
              sunsetSecretId: <string>
              decrypted: true
              value: <string>
              vsmValue: <string>
              id: <string>
              key: <string>
              configurationId: <string>
              createdAt: 123
              updatedAt: 123
              createdBy: <string>
              updatedBy: <string>
              gitBranch: <string>
              edgeConfigId: <string>
              edgeConfigTokenId: <string>
              contentHint:
                type: redis-url
                storeId: <string>
              internalContentHint:
                type: flags-secret
                encryptedValue: <string>
              comment: <string>
              customEnvironmentIds:
                - <string>
              system: true
        description: The list of environment variables for the given project
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
title: "Unpause a project"

last_updated: "2025-11-07T00:37:14.550Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/unpause-a-project"
--------------------------------------------------------------------------------

# Unpause a project

> Unpause a project by passing its project `id` in the URL. If the project does not exist given the id then the request will fail with 400 status code. If the project enables auto assigning custom production domains and unblocks the active Production Deployment then the request will return with 200 status code.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{projectId}/unpause
paths:
  path: /v1/projects/{projectId}/unpause
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
        projectId:
          schema:
            - type: string
              required: true
              description: The unique project identifier
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
      - label: unpauseProject
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.UnpauseProject(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: unpauseProject
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.projects.unpauseProject({
              projectId: "<id>",
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update a project domain"

last_updated: "2025-11-07T00:37:14.490Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/update-a-project-domain"
--------------------------------------------------------------------------------

# Update a project domain

> Update a project domain's configuration, including the name, git branch and redirect of the domain.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v9/projects/{idOrName}/domains/{domain}
paths:
  path: /v9/projects/{idOrName}/domains/{domain}
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
        idOrName:
          schema:
            - type: string
              required: true
              description: The unique project identifier or the project name
        domain:
          schema:
            - type: string
              required: true
              description: The project domain name
              example: www.example.com
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
              gitBranch:
                allOf:
                  - description: Git branch to link the project domain
                    example: null
                    type: string
                    maxLength: 250
                    nullable: true
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
        examples:
          example:
            value:
              gitBranch: null
              redirect: foobar.com
              redirectStatusCode: 307
    codeSamples:
      - label: updateProjectDomain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.UpdateProjectDomain(ctx, operations.UpdateProjectDomainRequest{\n        IDOrName: \"<value>\",\n        Domain: \"www.example.com\",\n        RequestBody: &operations.UpdateProjectDomainRequestBody{\n            GitBranch: nil,\n            Redirect: vercel.String(\"foobar.com\"),\n            RedirectStatusCode: operations.RedirectStatusCodeThreeHundredAndSeven.ToPointer(),\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateProjectDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.updateProjectDomain({
              idOrName: "<value>",
              domain: "www.example.com",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
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
        description: The domain was updated successfuly
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
              The domain redirect is not valid
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
          The domain redirect is not valid
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
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The project is currently being transferred
        examples: {}
        description: The project is currently being transferred
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update an existing project"

last_updated: "2025-11-07T00:37:14.793Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/update-an-existing-project"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./31-retrieve-a-list-of-projects.md) | [Index](./index.md) | [Next →](./33-update-an-existing-project.md)
