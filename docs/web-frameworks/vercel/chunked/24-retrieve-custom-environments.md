**Navigation:** [← Previous](./23-update-an-existing-drain.md) | [Index](./index.md) | [Next →](./25-list-products-for-integration-configuration.md)

---

# Retrieve custom environments

> Retrieve custom environments for the project. Must not be named 'Production' or 'Preview'.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v9/projects/{idOrName}/custom-environments
paths:
  path: /v9/projects/{idOrName}/custom-environments
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
      query:
        gitBranch:
          schema:
            - type: string
              required: false
              description: Fetch custom environments for a specific git branch
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
      - label: get_/v9/projects/{idOrName}/custom-environments
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.getV9ProjectsIdOrNameCustomEnvironments({
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
              accountLimit:
                allOf:
                  - properties:
                      total:
                        type: number
                    required:
                      - total
                    type: object
                    description: >-
                      The maximum number of custom environments allowed either
                      by the team's plan type or a custom override.
              environments:
                allOf:
                  - items:
                      properties:
                        id:
                          type: string
                          description: >-
                            Unique identifier for the custom environment
                            (format: env_*)
                        slug:
                          type: string
                          description: URL-friendly name of the environment
                        type:
                          type: string
                          enum:
                            - preview
                            - production
                            - development
                          description: >-
                            The type of environment (production, preview, or
                            development)
                        description:
                          type: string
                          description: Optional description of the environment's purpose
                        branchMatcher:
                          properties:
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
                          items:
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
                                  `true` if the domain is verified for use with
                                  the project. If `false` it will not be used as
                                  an alias on this project until the challenge
                                  in `verification` is completed.
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
                                    A list of verification challenges, one of
                                    which must be completed to verify the domain
                                    for use on the project. After the challenge
                                    is complete `POST
                                    /projects/:idOrName/domains/:domain/verify`
                                    to verify the domain. Possible challenges: -
                                    If `verification.type = TXT` the
                                    `verification.domain` will be checked for a
                                    TXT record matching `verification.value`.
                                type: array
                                description: >-
                                  A list of verification challenges, one of
                                  which must be completed to verify the domain
                                  for use on the project. After the challenge is
                                  complete `POST
                                  /projects/:idOrName/domains/:domain/verify` to
                                  verify the domain. Possible challenges: - If
                                  `verification.type = TXT` the
                                  `verification.domain` will be checked for a
                                  TXT record matching `verification.value`.
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
                          items:
                            type: string
                          type: array
                          description: List of aliases for the current deployment
                        createdAt:
                          type: number
                          description: Timestamp when the environment was created
                        updatedAt:
                          type: number
                          description: Timestamp when the environment was last updated
                      required:
                        - id
                        - slug
                        - type
                        - createdAt
                        - updatedAt
                      type: object
                    type: array
            requiredProperties:
              - accountLimit
              - environments
        examples:
          example:
            value:
              accountLimit:
                total: 123
              environments:
                - id: <string>
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
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Retrieve the decrypted value of a Shared Environment Variable by id."

last_updated: "2025-11-07T00:37:12.323Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id"
--------------------------------------------------------------------------------

# Retrieve the decrypted value of a Shared Environment Variable by id.

> Retrieve the decrypted value of a Shared Environment Variable by id.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/env/{id}
paths:
  path: /v1/env/{id}
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
              description: >-
                The unique ID for the Shared Environment Variable to get the
                decrypted value.
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
      - label: getSharedEnvVar
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.getSharedEnvVar({
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
              created:
                allOf:
                  - type: string
                    format: date-time
                    description: The date when the Shared Env Var was created.
                    example: '2021-02-10T13:11:49.180Z'
              key:
                allOf:
                  - type: string
                    description: The name of the Shared Env Var.
                    example: my-api-key
              ownerId:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      The unique identifier of the owner (team) the Shared Env
                      Var was created for.
                    example: team_LLHUOMOoDlqOp8wPE4kFo9pE
              id:
                allOf:
                  - type: string
                    description: The unique identifier of the Shared Env Var.
                    example: env_XCG7t7AIHuO2SBA8667zNUiM
              createdBy:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      The unique identifier of the user who created the Shared
                      Env Var.
                    example: 2qDDuGFTWXBLDNnqZfWPDp1A
              deletedBy:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      The unique identifier of the user who deleted the Shared
                      Env Var.
                    example: 2qDDuGFTWXBLDNnqZfWPDp1A
              updatedBy:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      The unique identifier of the user who last updated the
                      Shared Env Var.
                    example: 2qDDuGFTWXBLDNnqZfWPDp1A
              createdAt:
                allOf:
                  - type: number
                    description: Timestamp for when the Shared Env Var was created.
                    example: 1609492210000
              deletedAt:
                allOf:
                  - type: number
                    description: Timestamp for when the Shared Env Var was (soft) deleted.
                    example: 1609492210000
              updatedAt:
                allOf:
                  - type: number
                    description: Timestamp for when the Shared Env Var was last updated.
                    example: 1609492210000
              value:
                allOf:
                  - type: string
                    description: The value of the Shared Env Var.
              projectId:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      The unique identifiers of the projects which the Shared
                      Env Var is linked to.
                    example:
                      - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                      - prj_2WjyKQmM8ZnGcJsPWMrasEFg
              type:
                allOf:
                  - type: string
                    enum:
                      - encrypted
                      - sensitive
                      - system
                      - plain
                    description: >-
                      The type of this cosmos doc instance, if blank, assume
                      secret.
                    example: encrypted
              target:
                allOf:
                  - items:
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
                allOf:
                  - type: boolean
                    description: >-
                      whether or not this env varible applies to custom
                      environments
              decrypted:
                allOf:
                  - type: boolean
                    description: whether or not this env variable is decrypted
              comment:
                allOf:
                  - type: string
                    description: >-
                      A user provided comment that describes what this Shared
                      Env Var is for.
              lastEditedByDisplayName:
                allOf:
                  - type: string
                    description: The last editor full name or username.
        examples:
          example:
            value:
              created: '2021-02-10T13:11:49.180Z'
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
title: "Update a custom environment"

last_updated: "2025-11-07T00:37:12.312Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/environment/update-a-custom-environment"
--------------------------------------------------------------------------------

# Update a custom environment

> Update a custom environment for the project. Must not be named 'Production' or 'Preview'.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v9/projects/{idOrName}/custom-environments/{environmentSlugOrId}
paths:
  path: /v9/projects/{idOrName}/custom-environments/{environmentSlugOrId}
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
              slug:
                allOf:
                  - description: The slug of the custom environment.
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
                    nullable: true
        examples:
          example:
            value:
              slug: <string>
              description: <string>
              branchMatcher:
                type: equals
                pattern: <string>
    codeSamples:
      - label: updateCustomEnvironment
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.updateCustomEnvironment({
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
title: "Updates one or more shared environment variables"

last_updated: "2025-11-07T00:37:12.422Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/environment/updates-one-or-more-shared-environment-variables"
--------------------------------------------------------------------------------

# Updates one or more shared environment variables

> Updates a given Shared Environment Variable for a Team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/env
paths:
  path: /v1/env
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
              updates:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      additionalProperties: false
                      properties:
                        key:
                          description: The name of the Shared Environment Variable
                          type: string
                          example: API_URL
                        value:
                          description: The value of the Shared Environment Variable
                          type: string
                          example: https://api.vercel.com
                        target:
                          description: >-
                            The target environment of the Shared Environment
                            Variable
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
                          description: Associate a Shared Environment Variable to projects.
                          type: array
                          items:
                            type: string
                          example:
                            - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                            - prj_2WjyKQmM8ZnGcJsPWMrHRCRV
                        projectIdUpdates:
                          description: >-
                            Incrementally update project associations without
                            specifying the full list
                          type: object
                          additionalProperties: false
                          properties:
                            link:
                              description: Project IDs to add to this environment variable
                              type: array
                              items:
                                type: string
                              example:
                                - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                            unlink:
                              description: >-
                                Project IDs to remove from this environment
                                variable
                              type: array
                              items:
                                type: string
                              example:
                                - prj_2WjyKQmM8ZnGcJsPWMrHRCRV
                        type:
                          description: The new type of the Shared Environment Variable
                          type: string
                          enum:
                            - encrypted
                            - sensitive
                          example: encrypted
                        comment:
                          type: string
                          description: >-
                            A comment to add context on what this Shared
                            Environment Variable is for
                          example: database connection string for production
                          maxLength: 500
            requiredProperties:
              - updates
            additionalProperties: false
        examples:
          example:
            value:
              updates: {}
    codeSamples:
      - label: updateSharedEnvVariable
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.updateSharedEnvVariable({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                updates: {

                },
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
              updated:
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
              - updated
              - failed
        examples:
          example:
            value:
              updated:
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
title: "Connect integration resource to project"

last_updated: "2025-11-07T00:37:12.153Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/integrations/connect-integration-resource-to-project"
--------------------------------------------------------------------------------

# Connect integration resource to project

> Connects an integration resource to a Vercel project. This endpoint establishes a connection between a provisioned integration resource (from storage APIs like `POST /v1/storage/stores/integration/direct`) and a specific Vercel project.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/integrations/installations/{integrationConfigurationId}/resources/{resourceId}/connections
paths:
  path: >-
    /v1/integrations/installations/{integrationConfigurationId}/resources/{resourceId}/connections
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
              projectId:
                allOf:
                  - type: string
            requiredProperties:
              - projectId
        examples:
          example:
            value:
              projectId: <string>
    codeSamples:
      - label: connectIntegrationResourceToProject
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.integrations.connectIntegrationResourceToProject({
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
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
title: "Create integration store (free and paid plans)"

last_updated: "2025-11-07T00:37:12.461Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/integrations/create-integration-store-free-and-paid-plans"
--------------------------------------------------------------------------------

# Create integration store (free and paid plans)

> Creates an integration store for both FREE and PAID billing plans. This simplified endpoint automatically provisions real integration storage resources while handling billing complexity behind the scenes. It supports both free and paid billing plans with automatic authorization creation for paid resources. ## How it works 1. Validates the integration configuration and product 2. For free resources: Auto-discovers available free billing plans 3. For paid resources: Creates billing authorization inline using provided billingPlanId 4. Provisions real resources through the Vercel Marketplace 5. Returns the created store with connection details ## Workflow Before using this endpoint, discover available products and billing plans: 1. List your configurations: `GET /v1/integrations/configurations` 2. Get products for a configuration: `GET /v1/integrations/configuration/{id}/products` 3. Get billing plans for a product: `GET /integrations/integration/{integrationId}/products/{productId}/plans` 4. Review the `metadataSchema` for each product to understand required metadata 5. Create storage with discovered product: `POST /v1/storage/stores/integration/direct` ## Usage Patterns - **Free resources**: Omit `billingPlanId` - endpoint will auto-discover free plans - **Paid resources**: Provide `billingPlanId` from billing plans discovery - **Prepayment plans**: Also provide `prepaymentAmountCents` for variable amount plans ## Limitations - **Admin access required**: Only integration configuration admins can create stores - **Storage limits apply**: Subject to your team's storage quotas - **Payment method required**: For paid plans, ensure valid payment method is configured ## Error Responses - `400 Bad Request`: Invalid input, no plans available, or billing issues - `403 Forbidden`: Insufficient permissions (non-admin users) - `404 Not Found`: Integration configuration or product not found - `429 Too Many Requests`: Rate limit exceeded

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/storage/stores/integration/direct
paths:
  path: /v1/storage/stores/integration/direct
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
                  - type: string
                    maxLength: 128
                    description: Human-readable name for the storage resource
                    example: my-dev-database
              integrationConfigurationId:
                allOf:
                  - type: string
                    description: >-
                      ID of your integration configuration. Get this from GET
                      /v1/integrations/configurations
                    example: icfg_cuwj0AdCdH3BwWT4LPijCC7t
                    pattern: ^icfg_[a-zA-Z0-9]+$
              integrationProductIdOrSlug:
                allOf:
                  - type: string
                    description: >-
                      ID or slug of the integration product. Get available
                      products from GET
                      /v1/integrations/configuration/{id}/products
                    example: iap_postgres_db
                    oneOf:
                      - pattern: ^iap_[a-zA-Z0-9_]+$
                        description: Product ID format
                      - pattern: ^[a-z0-9-]+$
                        description: Product slug format
              metadata:
                allOf:
                  - type: object
                    description: Optional key-value pairs for resource metadata
                    additionalProperties:
                      oneOf:
                        - type: string
                        - type: number
                        - type: boolean
                        - type: array
                          items:
                            type: string
                        - type: array
                          items:
                            type: number
                    example:
                      environment: development
                      project: my-app
                      tags:
                        - database
                        - postgres
              externalId:
                allOf:
                  - type: string
                    description: Optional external identifier for tracking purposes
                    example: dev-db-001
              protocolSettings:
                allOf:
                  - type: object
                    description: Protocol-specific configuration settings
                    additionalProperties: true
                    example:
                      experimentation:
                        edgeConfigSyncingEnabled: true
              source:
                allOf:
                  - type: string
                    description: Source of the store creation request
                    example: api
                    default: marketplace
              billingPlanId:
                allOf:
                  - type: string
                    description: >-
                      ID of the billing plan for paid resources. Get available
                      plans from GET
                      /integrations/integration/{id}/products/{productId}/plans.
                      If not provided, automatically discovers free billing
                      plans.
                    example: bp_abc123def456
              paymentMethodId:
                allOf:
                  - type: string
                    description: >-
                      Payment method ID for paid resources. Optional - uses
                      default payment method if not provided.
                    example: pm_1AbcDefGhiJklMno
              prepaymentAmountCents:
                allOf:
                  - type: number
                    minimum: 50
                    description: >-
                      Amount in cents for prepayment billing plans. Required
                      only for prepayment plans with variable amounts.
                    example: 5000
            requiredProperties:
              - name
              - integrationConfigurationId
              - integrationProductIdOrSlug
        examples:
          example:
            value:
              name: my-dev-database
              integrationConfigurationId: icfg_cuwj0AdCdH3BwWT4LPijCC7t
              integrationProductIdOrSlug: iap_postgres_db
              metadata:
                environment: development
                project: my-app
                tags:
                  - database
                  - postgres
              externalId: dev-db-001
              protocolSettings:
                experimentation:
                  edgeConfigSyncingEnabled: true
              source: api
              billingPlanId: bp_abc123def456
              paymentMethodId: pm_1AbcDefGhiJklMno
              prepaymentAmountCents: 5000
    codeSamples:
      - label: createIntegrationStoreDirect
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.integrations.createIntegrationStoreDirect({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "my-dev-database",
                integrationConfigurationId: "icfg_cuwj0AdCdH3BwWT4LPijCC7t",
                integrationProductIdOrSlug: "iap_postgres_db",
                metadata: {
                  "environment": "development",
                  "project": "my-app",
                  "tags": [
                    "database",
                    "postgres",
                  ],
                },
                externalId: "dev-db-001",
                protocolSettings: {
                  "experimentation": {
                    "edgeConfigSyncingEnabled": true,
                  },
                },
                source: "api",
                billingPlanId: "bp_abc123def456",
                paymentMethodId: "pm_1AbcDefGhiJklMno",
                prepaymentAmountCents: 5000,
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
              store:
                allOf:
                  - nullable: true
                    type: object
                    properties:
                      projectsMetadata:
                        items:
                          properties:
                            id:
                              type: string
                            projectId:
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
                            environments:
                              items:
                                type: string
                                enum:
                                  - production
                                  - preview
                                  - development
                              type: array
                            envVarPrefix:
                              nullable: true
                              type: string
                            environmentVariables:
                              items:
                                type: string
                              type: array
                            deployments:
                              properties:
                                required:
                                  type: boolean
                                actions:
                                  items:
                                    properties:
                                      slug:
                                        type: string
                                      environments:
                                        items:
                                          type: string
                                          enum:
                                            - production
                                            - preview
                                            - development
                                        type: array
                                    required:
                                      - slug
                                      - environments
                                    type: object
                                  type: array
                              required:
                                - required
                                - actions
                              type: object
                          required:
                            - id
                            - projectId
                            - name
                            - environments
                            - envVarPrefix
                            - environmentVariables
                          type: object
                        type: array
                      projectFilter:
                        properties:
                          git:
                            properties:
                              providers:
                                oneOf:
                                  - items:
                                      type: string
                                      enum:
                                        - github
                                        - gitlab
                                        - bitbucket
                                    type: array
                                  - type: string
                                    enum:
                                      - '*'
                              owners:
                                items:
                                  type: string
                                type: array
                              repos:
                                items:
                                  type: string
                                type: array
                            required:
                              - providers
                            type: object
                        type: object
                      totalConnectedProjects:
                        type: number
                      usageQuotaExceeded:
                        type: boolean
                      status:
                        nullable: true
                        type: string
                        enum:
                          - available
                          - error
                          - suspended
                          - limits-exceeded-suspended
                          - limits-exceeded-suspended-store-count
                          - initializing
                          - onboarding
                          - uninstalled
                      ownership:
                        type: string
                        enum:
                          - owned
                          - linked
                          - sandbox
                      capabilities:
                        properties:
                          mcp:
                            type: boolean
                          sso:
                            type: boolean
                          billable:
                            type: boolean
                          transferable:
                            type: boolean
                          secretsSync:
                            type: boolean
                          projects:
                            type: boolean
                        type: object
                      metadata:
                        additionalProperties:
                          oneOf:
                            - type: string
                            - type: number
                            - type: boolean
                            - items:
                                type: string
                              type: array
                            - items:
                                type: number
                              type: array
                        type: object
                      externalResourceId:
                        type: string
                      externalResourceStatus:
                        nullable: true
                        type: string
                        enum:
                          - error
                          - suspended
                          - onboarding
                          - uninstalled
                          - ready
                          - pending
                          - resumed
                      product:
                        properties:
                          id:
                            type: string
                          name:
                            type: string
                          slug:
                            type: string
                          iconUrl:
                            type: string
                          capabilities:
                            properties:
                              mcp:
                                type: boolean
                              sso:
                                type: boolean
                              billable:
                                type: boolean
                              transferable:
                                type: boolean
                              secretsSync:
                                type: boolean
                              sandbox:
                                type: boolean
                              linking:
                                type: boolean
                              projects:
                                type: boolean
                            type: object
                          shortDescription:
                            type: string
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
                                        enum:
                                          items:
                                            type: string
                                          type: array
                                        maxLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        minLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        pattern:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        description:
                                          type: string
                                        default:
                                          type: string
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
                                        maximum:
                                          type: number
                                        exclusiveMaximum:
                                          type: number
                                        minimum:
                                          type: number
                                        exclusiveMinimum:
                                          type: number
                                        description:
                                          type: string
                                        default:
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
                                        ui:control:
                                          type: string
                                          enum:
                                            - slider
                                        ui:steps:
                                          items:
                                            type: number
                                          type: array
                                        maxItems:
                                          type: number
                                        minItems:
                                          type: number
                                        description:
                                          type: string
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
                                        - items
                                        - ui:control
                                        - ui:steps
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
                                        enum:
                                          items:
                                            type: string
                                          type: array
                                        maxLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        minLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        pattern:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        description:
                                          type: string
                                        default:
                                          type: string
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
                                                __@BRAND@8675:
                                                  type: object
                                              required:
                                                - __@BRAND@8675
                                            maxLength:
                                              type: object
                                              properties:
                                                __@BRAND@8675:
                                                  type: object
                                              required:
                                                - __@BRAND@8675
                                            pattern:
                                              type: object
                                              properties:
                                                __@BRAND@8675:
                                                  type: object
                                              required:
                                                - __@BRAND@8675
                                            default:
                                              type: string
                                            enum:
                                              items:
                                                type: string
                                              type: array
                                          required:
                                            - type
                                          type: object
                                        ui:control:
                                          type: string
                                          enum:
                                            - multi-select
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
                                        maxItems:
                                          type: number
                                        minItems:
                                          type: number
                                        description:
                                          type: string
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
                                        - items
                                        - ui:control
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
                                                  __@BRAND@8675:
                                                    type: object
                                                required:
                                                  - __@BRAND@8675
                                              - properties:
                                                  value:
                                                    type: object
                                                    properties:
                                                      __@BRAND@8675:
                                                        type: object
                                                    required:
                                                      - __@BRAND@8675
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
                                        enum:
                                          items:
                                            type: string
                                          type: array
                                        maxLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        minLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        pattern:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        description:
                                          type: string
                                        default:
                                          type: string
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
                                            - string
                                        ui:control:
                                          type: string
                                          enum:
                                            - domain
                                        enum:
                                          items:
                                            type: string
                                          type: array
                                        maxLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        minLength:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        pattern:
                                          type: object
                                          properties:
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
                                        description:
                                          type: string
                                        default:
                                          type: string
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
                                            __@BRAND@8675:
                                              type: object
                                          required:
                                            - __@BRAND@8675
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
                          resourceLinks:
                            items:
                              properties:
                                href:
                                  type: string
                                title:
                                  type: string
                              required:
                                - href
                                - title
                              type: object
                            type: array
                          tags:
                            items:
                              type: string
                              enum:
                                - edge-config
                                - redis
                                - postgres
                                - blob
                                - experimentation
                                - checks
                                - storage
                                - ai
                                - observability
                                - video
                                - authentication
                                - workflow
                                - logDrain
                                - traceDrain
                                - messaging
                                - other
                                - mysql
                                - vector
                                - tag_agents
                                - tag_ai
                                - tag_analytics
                                - tag_authentication
                                - tag_cms
                                - tag_code_repository
                                - tag_code_review
                                - tag_code_security
                                - tag_code_testing
                                - tag_commerce
                                - tag_databases
                                - tag_dev_tools
                                - tag_experimentation
                                - tag_flags
                                - tag_logging
                                - tag_messaging
                                - tag_monitoring
                                - tag_observability
                                - tag_payments
                                - tag_performance
                                - tag_productivity
                                - tag_searching
                                - tag_security
                                - tag_support_agent
                                - tag_testing
                                - tag_video
                                - tag_web_automation
                                - tag_workflow
                                - tag_checks
                                - tag_storage
                                - tag_logDrain
                                - tag_traceDrain
                                - tag_other
                            type: array
                          projectConnectionScopes:
                            items:
                              type: string
                              enum:
                                - read:deployment
                                - read:domain
                                - read:project
                                - read-write:deployment
                                - read-write:deployment-check
                                - read-write:domain
                                - read-write:global-project-env-vars
                                - read-write:integration-deployment-action
                                - read-write:log-drain
                                - read-write:drains
                                - read-write:project-env-vars
                                - read-write:project-protection-bypass
                            type: array
                          showSSOLinkOnProjectConnection:
                            type: boolean
                          disableResourceRenaming:
                            type: boolean
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
                          guides:
                            items:
                              properties:
                                framework:
                                  type: string
                                title:
                                  type: string
                                steps:
                                  items:
                                    properties:
                                      title:
                                        type: string
                                      content:
                                        type: string
                                      actions:
                                        items:
                                          properties:
                                            type:
                                              type: string
                                              enum:
                                                - connect_to_project
                                                - configure_project_connections
                                                - add_drain
                                          required:
                                            - type
                                          type: object
                                        type: array
                                    required:
                                      - title
                                      - content
                                    type: object
                                  type: array
                              required:
                                - framework
                                - title
                                - steps
                              type: object
                            type: array
                          value:
                            type: object
                            properties:
                              __@BRAND@8675:
                                type: object
                            required:
                              - __@BRAND@8675
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
                      notification:
                        properties:
                          title:
                            type: string
                          level:
                            type: string
                            enum:
                              - error
                              - info
                              - warn
                          message:
                            type: string
                          href:
                            type: string
                        required:
                          - title
                          - level
                        type: object
                      secrets:
                        items:
                          properties:
                            name:
                              type: string
                            length:
                              type: number
                          required:
                            - name
                            - length
                          type: object
                        type: array
                      billingPlan:
                        properties:
                          type:
                            type: string
                            enum:
                              - prepayment
                              - subscription
                          description:
                            type: string
                          id:
                            type: string
                          name:
                            type: string
                          scope:
                            type: string
                            enum:
                              - installation
                              - resource
                          paymentMethodRequired:
                            type: boolean
                          preauthorizationAmount:
                            type: number
                          initialCharge:
                            type: string
                          minimumAmount:
                            type: string
                          maximumAmount:
                            type: string
                          maximumAmountAutoPurchasePerPeriod:
                            type: string
                          cost:
                            type: string
                          details:
                            items:
                              properties:
                                label:
                                  type: string
                                value:
                                  type: string
                              required:
                                - label
                              type: object
                            type: array
                          highlightedDetails:
                            items:
                              properties:
                                label:
                                  type: string
                                value:
                                  type: string
                              required:
                                - label
                              type: object
                            type: array
                          quote:
                            items:
                              properties:
                                line:
                                  type: string
                                amount:
                                  type: string
                              required:
                                - line
                                - amount
                              type: object
                            type: array
                          effectiveDate:
                            type: string
                          disabled:
                            type: boolean
                        required:
                          - type
                          - description
                          - id
                          - name
                          - scope
                          - paymentMethodRequired
                        type: object
                    required:
                      - projectsMetadata
                      - usageQuotaExceeded
                      - status
                      - externalResourceId
                      - product
                      - secrets
            requiredProperties:
              - store
        examples:
          example:
            value:
              store:
                projectsMetadata:
                  - id: <string>
                    projectId: <string>
                    name: <string>
                    framework: blitzjs
                    latestDeployment: <string>
                    environments:
                      - production
                    envVarPrefix: <string>
                    environmentVariables:
                      - <string>
                    deployments:
                      required: true
                      actions:
                        - slug: <string>
                          environments:
                            - production
                projectFilter:
                  git:
                    providers:
                      - github
                    owners:
                      - <string>
                    repos:
                      - <string>
                totalConnectedProjects: 123
                usageQuotaExceeded: true
                status: available
                ownership: owned
                capabilities:
                  mcp: true
                  sso: true
                  billable: true
                  transferable: true
                  secretsSync: true
                  projects: true
                metadata: {}
                externalResourceId: <string>
                externalResourceStatus: error
                product:
                  id: <string>
                  name: <string>
                  slug: <string>
                  iconUrl: <string>
                  capabilities:
                    mcp: true
                    sso: true
                    billable: true
                    transferable: true
                    secretsSync: true
                    sandbox: true
                    linking: true
                    projects: true
                  shortDescription: <string>
                  metadataSchema:
                    type: object
                    properties: {}
                    required:
                      - <string>
                  resourceLinks:
                    - href: <string>
                      title: <string>
                  tags:
                    - edge-config
                  projectConnectionScopes:
                    - read:deployment
                  showSSOLinkOnProjectConnection: true
                  disableResourceRenaming: true
                  repl:
                    enabled: true
                    supportsReadOnlyMode: true
                    welcomeMessage: <string>
                  guides:
                    - framework: <string>
                      title: <string>
                      steps:
                        - title: <string>
                          content: <string>
                          actions:
                            - type: connect_to_project
                  value:
                    __@BRAND@8675: {}
                  disabled: true
                  hidden: true
                protocolSettings:
                  experimentation:
                    edgeConfigSyncingEnabled: true
                    edgeConfigId: <string>
                    edgeConfigTokenId: <string>
                notification:
                  title: <string>
                  level: error
                  message: <string>
                  href: <string>
                secrets:
                  - name: <string>
                    length: 123
                billingPlan:
                  type: prepayment
                  description: <string>
                  id: <string>
                  name: <string>
                  scope: installation
                  paymentMethodRequired: true
                  preauthorizationAmount: 123
                  initialCharge: <string>
                  minimumAmount: <string>
                  maximumAmount: <string>
                  maximumAmountAutoPurchasePerPeriod: <string>
                  cost: <string>
                  details:
                    - label: <string>
                      value: <string>
                  highlightedDetails:
                    - label: <string>
                      value: <string>
                  quote:
                    - line: <string>
                      amount: <string>
                  effectiveDate: <string>
                  disabled: true
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
    '404': {}
    '409': {}
    '429': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Delete an integration configuration"

last_updated: "2025-11-07T00:37:12.168Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/integrations/delete-an-integration-configuration"
--------------------------------------------------------------------------------

# Delete an integration configuration

> Allows to remove the configuration with the `id` provided in the parameters. The configuration and all of its resources will be removed. This includes Webhooks, LogDrains and Project Env variables.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/integrations/configuration/{id}
paths:
  path: /v1/integrations/configuration/{id}
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
      - label: deleteConfiguration
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Integrations.DeleteConfiguration(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: deleteConfiguration
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.integrations.deleteConfiguration({
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
            description: The configuration was successfully removed
        examples: {}
        description: The configuration was successfully removed
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
title: "Get configurations for the authenticated user or team"

last_updated: "2025-11-07T00:37:12.235Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/integrations/get-configurations-for-the-authenticated-user-or-team"
--------------------------------------------------------------------------------

# Get configurations for the authenticated user or team

> Allows to retrieve all configurations for an authenticated integration. When the `project` view is used, configurations generated for the authorization flow will be filtered out of the results.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/configurations
paths:
  path: /v1/integrations/configurations
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
        view:
          schema:
            - type: enum<string>
              enum:
                - account
                - project
              required: true
        installationType:
          schema:
            - type: enum<string>
              enum:
                - marketplace
                - external
              required: false
        integrationIdOrSlug:
          schema:
            - type: string
              required: false
              description: ID of the integration
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
      - label: getConfigurations
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Integrations.GetConfigurations(ctx, operations.GetConfigurationsRequest{\n        View: operations.ViewAccount,\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: getConfigurations
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.integrations.getConfigurations({
              view: "account",
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
                    completedAt:
                      type: number
                      description: >-
                        A timestamp that tells you when the configuration was
                        installed successfully
                      example: 1558531915505
                    createdAt:
                      type: number
                      description: >-
                        A timestamp that tells you when the configuration was
                        created
                      example: 1558531915505
                    id:
                      type: string
                      description: The unique identifier of the configuration
                      example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                    integrationId:
                      type: string
                      description: >-
                        The unique identifier of the app the configuration was
                        created for
                      example: oac_xzpVzcUOgcB1nrVlirtKhbWV
                    ownerId:
                      type: string
                      description: The user or team ID that owns the configuration
                      example: kr1PsOIzqEL5Xg6M4VZcZosf
                    projects:
                      items:
                        type: string
                      type: array
                      description: >-
                        When a configuration is limited to access certain
                        projects, this will contain each of the project ID it is
                        allowed to access. If it is not defined, the
                        configuration has full access.
                      example:
                        - prj_xQxbutw1HpL6HLYPAzt5h75m8NjO
                    source:
                      type: string
                      enum:
                        - marketplace
                        - deploy-button
                        - external
                        - v0
                        - resource-claims
                      description: >-
                        Source defines where the configuration was installed
                        from. It is used to analyze user engagement for
                        integration installations in product metrics.
                      example: marketplace
                    slug:
                      type: string
                      description: >-
                        The slug of the integration the configuration is created
                        for.
                      example: slack
                    teamId:
                      nullable: true
                      type: string
                      description: >-
                        When the configuration was created for a team, this will
                        show the ID of the team.
                      example: team_nLlpyC6RE1qxydlFKbrxDlud
                    type:
                      type: string
                      enum:
                        - integration-configuration
                    updatedAt:
                      type: number
                      description: >-
                        A timestamp that tells you when the configuration was
                        updated.
                      example: 1558531915505
                    userId:
                      type: string
                      description: The ID of the user that created the configuration.
                      example: kr1PsOIzqEL5Xg6M4VZcZosf
                    scopes:
                      items:
                        type: string
                      type: array
                      description: >-
                        The resources that are allowed to be accessed by the
                        configuration.
                      example:
                        - read:project
                        - read-write:log-drain
                    disabledAt:
                      type: number
                      description: >-
                        A timestamp that tells you when the configuration was
                        disabled. Note: Configurations can be disabled when the
                        associated user loses access to a team. They do not
                        function during this time until the configuration is
                        'transferred', meaning the associated user is changed to
                        one with access to the team.
                      example: 1558531915505
                    deletedAt:
                      nullable: true
                      type: number
                      description: >-
                        A timestamp that tells you when the configuration was
                        deleted.
                      example: 1558531915505
                    deleteRequestedAt:
                      nullable: true
                      type: number
                      description: >-
                        A timestamp that tells you when the configuration
                        deletion has been started for cases when the deletion
                        needs to be settled/approved by partners, such as when
                        marketplace invoices have been paid.
                      example: 1558531915505
                    disabledReason:
                      type: string
                      enum:
                        - disabled-by-owner
                        - feature-not-available
                        - disabled-by-admin
                        - original-owner-left-the-team
                        - account-plan-downgrade
                        - original-owner-role-downgraded
                    installationType:
                      type: string
                      enum:
                        - marketplace
                        - external
                      description: >-
                        Defines the installation type. - 'external' integrations
                        are installed via the existing integrations flow -
                        'marketplace' integrations are natively installed: -
                        when accepting the TOS of a partner during the store
                        creation process - if undefined, assume 'external'
                  type: object
                  description: The list of configurations for the authenticated user
            description: The list of configurations for the authenticated user
          - type: array
            items:
              allOf:
                - properties:
                    integration:
                      properties:
                        name:
                          type: string
                        icon:
                          type: string
                        isLegacy:
                          type: boolean
                        flags:
                          items:
                            type: string
                          type: array
                        assignedBetaLabelAt:
                          type: number
                        tagIds:
                          items:
                            type: string
                            enum:
                              - tag_agents
                              - tag_ai
                              - tag_analytics
                              - tag_authentication
                              - tag_cms
                              - tag_code_repository
                              - tag_code_review
                              - tag_code_security
                              - tag_code_testing
                              - tag_commerce
                              - tag_databases
                              - tag_dev_tools
                              - tag_experimentation
                              - tag_flags
                              - tag_logging
                              - tag_messaging
                              - tag_monitoring
                              - tag_observability
                              - tag_payments
                              - tag_performance
                              - tag_productivity
                              - tag_searching
                              - tag_security
                              - tag_support_agent
                              - tag_testing
                              - tag_video
                              - tag_web_automation
                              - tag_workflow
                          type: array
                      required:
                        - name
                        - icon
                        - isLegacy
                      type: object
                    completedAt:
                      type: number
                      description: >-
                        A timestamp that tells you when the configuration was
                        installed successfully
                      example: 1558531915505
                    createdAt:
                      type: number
                      description: >-
                        A timestamp that tells you when the configuration was
                        created
                      example: 1558531915505
                    id:
                      type: string
                      description: The unique identifier of the configuration
                      example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                    integrationId:
                      type: string
                      description: >-
                        The unique identifier of the app the configuration was
                        created for
                      example: oac_xzpVzcUOgcB1nrVlirtKhbWV
                    ownerId:
                      type: string
                      description: The user or team ID that owns the configuration
                      example: kr1PsOIzqEL5Xg6M4VZcZosf
                    projects:
                      items:
                        type: string
                      type: array
                      description: >-
                        When a configuration is limited to access certain
                        projects, this will contain each of the project ID it is
                        allowed to access. If it is not defined, the
                        configuration has full access.
                      example:
                        - prj_xQxbutw1HpL6HLYPAzt5h75m8NjO
                    source:
                      type: string
                      enum:
                        - marketplace
                        - deploy-button
                        - external
                        - v0
                        - resource-claims
                      description: >-
                        Source defines where the configuration was installed
                        from. It is used to analyze user engagement for
                        integration installations in product metrics.
                      example: marketplace
                    slug:
                      type: string
                      description: >-
                        The slug of the integration the configuration is created
                        for.
                      example: slack
                    teamId:
                      nullable: true
                      type: string
                      description: >-
                        When the configuration was created for a team, this will
                        show the ID of the team.
                      example: team_nLlpyC6RE1qxydlFKbrxDlud
                    type:
                      type: string
                      enum:
                        - integration-configuration
                    updatedAt:
                      type: number
                      description: >-
                        A timestamp that tells you when the configuration was
                        updated.
                      example: 1558531915505
                    userId:
                      type: string
                      description: The ID of the user that created the configuration.
                      example: kr1PsOIzqEL5Xg6M4VZcZosf
                    scopes:
                      items:
                        type: string
                      type: array
                      description: >-
                        The resources that are allowed to be accessed by the
                        configuration.
                      example:
                        - read:project
                        - read-write:log-drain
                    disabledAt:
                      type: number
                      description: >-
                        A timestamp that tells you when the configuration was
                        disabled. Note: Configurations can be disabled when the
                        associated user loses access to a team. They do not
                        function during this time until the configuration is
                        'transferred', meaning the associated user is changed to
                        one with access to the team.
                      example: 1558531915505
                    deletedAt:
                      nullable: true
                      type: number
                      description: >-
                        A timestamp that tells you when the configuration was
                        deleted.
                      example: 1558531915505
                    deleteRequestedAt:
                      nullable: true
                      type: number
                      description: >-
                        A timestamp that tells you when the configuration
                        deletion has been started for cases when the deletion
                        needs to be settled/approved by partners, such as when
                        marketplace invoices have been paid.
                      example: 1558531915505
                    disabledReason:
                      type: string
                      enum:
                        - disabled-by-owner
                        - feature-not-available
                        - disabled-by-admin
                        - original-owner-left-the-team
                        - account-plan-downgrade
                        - original-owner-role-downgraded
                    installationType:
                      type: string
                      enum:
                        - marketplace
                        - external
                      description: >-
                        Defines the installation type. - 'external' integrations
                        are installed via the existing integrations flow -
                        'marketplace' integrations are natively installed: -
                        when accepting the TOS of a partner during the store
                        creation process - if undefined, assume 'external'
                  required:
                    - integration
                    - createdAt
                    - id
                    - integrationId
                    - ownerId
                    - slug
                    - type
                    - updatedAt
                    - userId
                    - scopes
                  type: object
        examples:
          example:
            value:
              - completedAt: 1558531915505
                createdAt: 1558531915505
                id: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                integrationId: oac_xzpVzcUOgcB1nrVlirtKhbWV
                ownerId: kr1PsOIzqEL5Xg6M4VZcZosf
                projects:
                  - prj_xQxbutw1HpL6HLYPAzt5h75m8NjO
                source: marketplace
                slug: slack
                teamId: team_nLlpyC6RE1qxydlFKbrxDlud
                type: integration-configuration
                updatedAt: 1558531915505
                userId: kr1PsOIzqEL5Xg6M4VZcZosf
                scopes:
                  - read:project
                  - read-write:log-drain
                disabledAt: 1558531915505
                deletedAt: 1558531915505
                deleteRequestedAt: 1558531915505
                disabledReason: disabled-by-owner
                installationType: marketplace
        description: The list of configurations for the authenticated user
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
title: "List integration billing plans"

last_updated: "2025-11-07T00:37:12.215Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/integrations/list-integration-billing-plans"
--------------------------------------------------------------------------------

# List integration billing plans

> Get a list of billing plans for an integration and product.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/integration/{integrationIdOrSlug}/products/{productIdOrSlug}/plans
paths:
  path: >-
    /v1/integrations/integration/{integrationIdOrSlug}/products/{productIdOrSlug}/plans
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
        integrationIdOrSlug:
          schema:
            - type: string
              required: true
        productIdOrSlug:
          schema:
            - type: string
              required: true
      query:
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
      - label: getBillingPlans
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.integrations.getBillingPlans({
              integrationIdOrSlug: "<value>",
              productIdOrSlug: "<value>",
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
              plans:
                allOf:
                  - items:
                      properties:
                        type:
                          type: string
                          enum:
                            - prepayment
                            - subscription
                        description:
                          type: string
                        id:
                          type: string
                        name:
                          type: string
                        scope:
                          type: string
                          enum:
                            - installation
                            - resource
                        paymentMethodRequired:
                          type: boolean
                        preauthorizationAmount:
                          type: number
                        initialCharge:
                          type: string
                        minimumAmount:
                          type: string
                        maximumAmount:
                          type: string
                        maximumAmountAutoPurchasePerPeriod:
                          type: string
                        cost:
                          type: string
                        details:
                          items:
                            properties:
                              label:
                                type: string
                              value:
                                type: string
                            required:
                              - label
                            type: object
                          type: array
                        highlightedDetails:
                          items:
                            properties:
                              label:
                                type: string
                              value:
                                type: string
                            required:
                              - label
                            type: object
                          type: array
                        quote:
                          items:
                            properties:
                              line:
                                type: string
                              amount:
                                type: string
                            required:
                              - line
                              - amount
                            type: object
                          type: array
                        effectiveDate:
                          type: string
                        disabled:
                          type: boolean
                      required:
                        - type
                        - description
                        - id
                        - name
                        - scope
                        - paymentMethodRequired
                      type: object
                    type: array
            requiredProperties:
              - plans
        examples:
          example:
            value:
              plans:
                - type: prepayment
                  description: <string>
                  id: <string>
                  name: <string>
                  scope: installation
                  paymentMethodRequired: true
                  preauthorizationAmount: 123
                  initialCharge: <string>
                  minimumAmount: <string>
                  maximumAmount: <string>
                  maximumAmountAutoPurchasePerPeriod: <string>
                  cost: <string>
                  details:
                    - label: <string>
                      value: <string>
                  highlightedDetails:
                    - label: <string>
                      value: <string>
                  quote:
                    - line: <string>
                      amount: <string>
                  effectiveDate: <string>
                  disabled: true
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
title: "List products for integration configuration"

last_updated: "2025-11-07T00:37:12.375Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/integrations/list-products-for-integration-configuration"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./23-update-an-existing-drain.md) | [Index](./index.md) | [Next →](./25-list-products-for-integration-configuration.md)
