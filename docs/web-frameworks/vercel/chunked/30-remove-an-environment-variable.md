**Navigation:** [← Previous](./29-find-a-project-by-id-or-name.md) | [Index](./index.md) | [Next →](./31-retrieve-a-list-of-projects.md)

---

# Remove an environment variable

> Delete a specific environment variable for a given project by passing the environment variable identifier and either passing the project `id` or `name` in the URL.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v9/projects/{idOrName}/env/{id}
paths:
  path: /v9/projects/{idOrName}/env/{id}
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
        id:
          schema:
            - type: string
              required: true
              description: The unique environment variable identifier
              example: XMbOEya1gUUO1ir4
      query:
        customEnvironmentId:
          schema:
            - type: string
              required: false
              description: The unique custom environment identifier within the project
              example: env_123abc4567
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
      - label: removeProjectEnv
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.RemoveProjectEnv(ctx, \"prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA\", \"XMbOEya1gUUO1ir4\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: removeProjectEnv
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.removeProjectEnv({
              idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",
              id: "XMbOEya1gUUO1ir4",
              customEnvironmentId: "env_123abc4567",
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
                            Contains the `value` of the env variable, encrypted
                            with a special key to make decryption possible in
                            the subscriber Lambda.
                      required:
                        - type
                        - encryptedValue
                      type: object
                      description: >-
                        Similar to `contentHints`, but should not be exposed to
                        the user.
                    comment:
                      type: string
                    customEnvironmentIds:
                      items:
                        type: string
                      type: array
                  required:
                    - type
                    - value
                    - key
                  type: object
          - type: object
            properties:
              system:
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
        examples:
          example:
            value:
              - target:
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
        description: The environment variable was successfully removed
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
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              The project is being transfered and removing an environment
              variable is not possible
        examples: {}
        description: >-
          The project is being transfered and removing an environment variable
          is not possible
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Retrieve a list of projects"

last_updated: "2025-11-07T00:37:15.002Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/retrieve-a-list-of-projects"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./29-find-a-project-by-id-or-name.md) | [Index](./index.md) | [Next →](./31-retrieve-a-list-of-projects.md)
