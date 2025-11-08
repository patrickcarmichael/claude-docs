**Navigation:** [← Previous](./27-create-a-new-project.md) | [Index](./index.md) | [Next →](./29-find-a-project-by-id-or-name.md)

---

# Create one or more environment variables

> Create one or more environment variables for a project by passing its `key`, `value`, `type` and `target` and by specifying the project by either passing the project `id` or `name` in the URL. If you include `upsert=true` as a query parameter, a new environment variable will not be created if it already exists but, the existing variable's value will be updated.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v10/projects/{idOrName}/env
paths:
  path: /v10/projects/{idOrName}/env
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
              example: prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA
      query:
        upsert:
          schema:
            - type: string
              required: false
              description: Allow override of environment variable if it already exists
              example: 'true'
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
              key:
                allOf:
                  - &ref_0
                    description: The name of the environment variable
                    type: string
                    example: API_URL
              value:
                allOf:
                  - &ref_1
                    description: The value of the environment variable
                    type: string
                    example: https://api.vercel.com
              type:
                allOf:
                  - &ref_2
                    description: The type of environment variable
                    type: string
                    enum:
                      - system
                      - secret
                      - encrypted
                      - plain
                      - sensitive
                    example: plain
              target:
                allOf:
                  - &ref_3
                    description: The target environment of the environment variable
                    type: array
                    items:
                      enum:
                        - production
                        - preview
                        - development
                    example:
                      - preview
              gitBranch:
                allOf:
                  - &ref_4
                    description: >-
                      If defined, the git branch of the environment variable
                      (must have target=preview)
                    type: string
                    maxLength: 250
                    example: feature-1
                    nullable: true
              comment:
                allOf:
                  - &ref_5
                    type: string
                    description: >-
                      A comment to add context on what this environment variable
                      is for
                    example: database connection string for production
                    maxLength: 500
              customEnvironmentIds:
                allOf:
                  - &ref_6
                    type: array
                    description: >-
                      The custom environment IDs associated with the environment
                      variable
                    items:
                      type: string
                      example: env_1234567890
            required: true
            requiredProperties:
              - key
              - value
              - type
              - target
          - type: object
            properties:
              key:
                allOf:
                  - *ref_0
              value:
                allOf:
                  - *ref_1
              type:
                allOf:
                  - *ref_2
              target:
                allOf:
                  - *ref_3
              gitBranch:
                allOf:
                  - *ref_4
              comment:
                allOf:
                  - *ref_5
              customEnvironmentIds:
                allOf:
                  - *ref_6
            required: true
            requiredProperties:
              - key
              - value
              - type
              - customEnvironmentIds
          - type: array
            items:
              allOf:
                - type: object
                  required:
                    - key
                    - value
                    - type
                  anyOf:
                    - required:
                        - target
                    - required:
                        - customEnvironmentIds
                  properties:
                    key:
                      description: The name of the environment variable
                      type: string
                      example: API_URL
                    value:
                      description: The value of the environment variable
                      type: string
                      example: https://api.vercel.com
                    type:
                      description: The type of environment variable
                      type: string
                      enum:
                        - system
                        - secret
                        - encrypted
                        - plain
                        - sensitive
                      example: plain
                    target:
                      description: The target environment of the environment variable
                      type: array
                      items:
                        enum:
                          - production
                          - preview
                          - development
                      example:
                        - preview
                    gitBranch:
                      description: >-
                        If defined, the git branch of the environment variable
                        (must have target=preview)
                      type: string
                      maxLength: 250
                      example: feature-1
                      nullable: true
                    comment:
                      type: string
                      description: >-
                        A comment to add context on what this environment
                        variable is for
                      example: database connection string for production
                      maxLength: 500
                    customEnvironmentIds:
                      type: array
                      description: >-
                        The custom environment IDs associated with the
                        environment variable
                      items:
                        type: string
                        example: env_1234567890
            required: true
        examples:
          example:
            value:
              key: API_URL
              value: https://api.vercel.com
              type: plain
              target:
                - preview
              gitBranch: feature-1
              comment: database connection string for production
              customEnvironmentIds:
                - env_1234567890
    codeSamples:
      - label: createProjectEnv
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.CreateProjectEnv(ctx, operations.CreateProjectEnvRequest{\n        IDOrName: \"prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA\",\n        Upsert: vercel.String(\"true\"),\n        RequestBody: vercel.Pointer(operations.CreateCreateProjectEnvRequestBodyCreateProjectEnvRequestBody1(\n            operations.CreateCreateProjectEnvRequestBody1CreateProjectEnv12(\n                operations.CreateProjectEnv12{\n                    Key: \"API_URL\",\n                    Value: \"https://api.vercel.com\",\n                    Type: operations.CreateProjectEnv1TypePlain,\n                    Target: []operations.CreateProjectEnv1Target{\n                        operations.CreateProjectEnv1TargetPreview,\n                    },\n                    GitBranch: vercel.String(\"feature-1\"),\n                    Comment: vercel.String(\"database connection string for production\"),\n                },\n            ),\n        )),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createProjectEnv
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.createProjectEnv({
              idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",
              upsert: "true",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                key: "API_URL",
                value: "https://api.vercel.com",
                type: "plain",
                target: [
                  "preview",
                ],
                gitBranch: "feature-1",
                comment: "database connection string for production",
                customEnvironmentIds: [
                  "env_1234567890",
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
                  - oneOf:
                      - properties:
                          target:
                            oneOf:
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
                                  encrypted with a special key to make
                                  decryption possible in the subscriber Lambda.
                            required:
                              - type
                              - encryptedValue
                            type: object
                            description: >-
                              Similar to `contentHints`, but should not be
                              exposed to the user.
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
                      - items:
                          properties:
                            target:
                              oneOf:
                                - items:
                                    type: string
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
                                    Contains the `value` of the env variable,
                                    encrypted with a special key to make
                                    decryption possible in the subscriber
                                    Lambda.
                              required:
                                - type
                                - encryptedValue
                              type: object
                              description: >-
                                Similar to `contentHints`, but should not be
                                exposed to the user.
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
        description: The environment variable was created successfully
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              One of the provided values in the request body is invalid.

              One of the provided values in the request query is invalid.

              The environment variable coudn't be created because an ongoing
              update env update is already happening

              The environment variable coudn't be created because project
              document is too large
        examples: {}
        description: >-
          One of the provided values in the request body is invalid.

          One of the provided values in the request query is invalid.

          The environment variable coudn't be created because an ongoing update
          env update is already happening

          The environment variable coudn't be created because project document
          is too large
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
            description: >-
              You do not have permission to access this resource.

              The environment variable cannot be created because it already
              exists

              Additional permissions are required to create production
              environment variables
        examples: {}
        description: >-
          You do not have permission to access this resource.

          The environment variable cannot be created because it already exists

          Additional permissions are required to create production environment
          variables
    '404': {}
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              The project is being transfered and creating an environment
              variable is not possible
        examples: {}
        description: >-
          The project is being transfered and creating an environment variable
          is not possible
    '429': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Create project transfer request"

last_updated: "2025-11-07T00:37:13.818Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/create-project-transfer-request"
--------------------------------------------------------------------------------

# Create project transfer request

> Initiates a project transfer request from one team to another. <br/> Returns a `code` that remains valid for 24 hours and can be used to accept the transfer request by another team using the `PUT /projects/transfer-request/:code` endpoint. <br/> Users can also accept the project transfer request using the claim URL: `https://vercel.com/claim-deployment?code=<code>&returnUrl=<returnUrl>`. <br/> The `code` parameter specifies the project transfer request code generated using this endpoint. <br/> The `returnUrl` parameter redirects users to a specific page of the application if the claim URL is invalid or expired.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /projects/{idOrName}/transfer-request
paths:
  path: /projects/{idOrName}/transfer-request
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
              description: The ID or name of the project to transfer.
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
              callbackUrl:
                allOf:
                  - type: string
                    description: >-
                      The URL to send a webhook to when the transfer is
                      accepted.
              callbackSecret:
                allOf:
                  - type: string
                    description: >-
                      The secret to use to sign the webhook payload with
                      HMAC-SHA256.
        examples:
          example:
            value:
              callbackUrl: <string>
              callbackSecret: <string>
    codeSamples:
      - label: createProjectTransferRequest
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.createProjectTransferRequest({
              idOrName: "<value>",
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
              code:
                allOf:
                  - type: string
                    description: >-
                      Code that can be used to accept the project transfer
                      request.
                    example: f99cc49a-602e-4786-a748-762dfb205880
            requiredProperties:
              - code
        examples:
          example:
            value:
              code: f99cc49a-602e-4786-a748-762dfb205880
        description: The project transfer request has been initiated successfully.
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
title: "Delete a Project"

last_updated: "2025-11-07T00:37:13.856Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/delete-a-project"
--------------------------------------------------------------------------------

# Delete a Project

> Delete a specific project by passing either the project `id` or `name` in the URL.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v9/projects/{idOrName}
paths:
  path: /v9/projects/{idOrName}
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
              example: prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
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
      - label: deleteProject
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.DeleteProject(ctx, \"prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: deleteProject
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.projects.deleteProject({
              idOrName: "prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
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
            description: The project was successfuly removed
        examples: {}
        description: The project was successfuly removed
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
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Edit an environment variable"

last_updated: "2025-11-07T00:37:13.867Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/edit-an-environment-variable"
--------------------------------------------------------------------------------

# Edit an environment variable

> Edit a specific environment variable for a given project by passing the environment variable identifier and either passing the project `id` or `name` in the URL.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v9/projects/{idOrName}/env/{id}
paths:
  path: /v9/projects/{idOrName}/env/{id}
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
              example: prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA
        id:
          schema:
            - type: string
              required: true
              description: The unique environment variable identifier
              example: XMbOEya1gUUO1ir4
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
              key:
                allOf:
                  - description: The name of the environment variable
                    type: string
                    example: GITHUB_APP_ID
              target:
                allOf:
                  - description: The target environment of the environment variable
                    type: array
                    items:
                      enum:
                        - production
                        - preview
                        - development
                    example:
                      - preview
              gitBranch:
                allOf:
                  - description: >-
                      If defined, the git branch of the environment variable
                      (must have target=preview)
                    type: string
                    maxLength: 250
                    example: feature-1
                    nullable: true
              type:
                allOf:
                  - description: The type of environment variable
                    type: string
                    enum:
                      - system
                      - secret
                      - encrypted
                      - plain
                      - sensitive
                    example: plain
              value:
                allOf:
                  - description: The value of the environment variable
                    type: string
                    example: bkWIjbnxcvo78
              customEnvironmentIds:
                allOf:
                  - type: array
                    description: >-
                      The custom environments that the environment variable
                      should be synced to
                    items:
                      type: string
                      example: env_1234567890
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this env var is for
                    example: database connection string for production
                    maxLength: 500
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              key: GITHUB_APP_ID
              target:
                - preview
              gitBranch: feature-1
              type: plain
              value: bkWIjbnxcvo78
              customEnvironmentIds:
                - env_1234567890
              comment: database connection string for production
    codeSamples:
      - label: editProjectEnv
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.EditProjectEnv(ctx, operations.EditProjectEnvRequest{\n        IDOrName: \"prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA\",\n        ID: \"XMbOEya1gUUO1ir4\",\n        RequestBody: &operations.EditProjectEnvRequestBody{\n            Key: vercel.String(\"GITHUB_APP_ID\"),\n            Target: []operations.EditProjectEnvTarget{\n                operations.EditProjectEnvTargetPreview,\n            },\n            GitBranch: vercel.String(\"feature-1\"),\n            Type: operations.EditProjectEnvTypePlain.ToPointer(),\n            Value: vercel.String(\"bkWIjbnxcvo78\"),\n            CustomEnvironmentIds: []string{\n                \"env_1234567890\",\n            },\n            Comment: vercel.String(\"database connection string for production\"),\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: editProjectEnv
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.editProjectEnv({
              idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",
              id: "XMbOEya1gUUO1ir4",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                key: "GITHUB_APP_ID",
                target: [
                  "preview",
                ],
                gitBranch: "feature-1",
                type: "plain",
                value: "bkWIjbnxcvo78",
                customEnvironmentIds: [
                  "env_1234567890",
                ],
                comment: "database connection string for production",
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
          - type: object
            properties: {}
        examples:
          example:
            value:
              target:
                - <string>
              type: system
              sunsetSecretId: <string>
              decrypted: true
              value: <string>
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
        description: The environment variable was successfully edited
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
              At least one environment variable failed validation
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
          At least one environment variable failed validation
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
    '429': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Find a project by id or name"

last_updated: "2025-11-07T00:37:14.170Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/find-a-project-by-id-or-name"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./27-create-a-new-project.md) | [Index](./index.md) | [Next →](./29-find-a-project-by-id-or-name.md)
