**Navigation:** [← Previous](./17-monitoring-quickstart.md) | [Index](./index.md) | [Next →](./19-cancel-a-deployment.md)

---

# List aliases

> Retrieves a list of aliases for the authenticated User or Team. When `domain` is provided, only aliases for that domain will be returned. When `projectId` is provided, it will only return the given project aliases.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/aliases
paths:
  path: /v4/aliases
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
        domain:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
              description: Get only aliases of the given domain name
              maxItems: 20
              example: my-test-domain.com
            - type: string
              description: Get only aliases of the given domain name
              example: my-test-domain.com
        from:
          schema:
            - type: number
              description: Get only aliases created after the provided timestamp
              deprecated: true
              example: 1540095775951
        limit:
          schema:
            - type: number
              description: Maximum number of aliases to list from a request
              example: 10
        projectId:
          schema:
            - type: string
              description: Filter aliases from the given `projectId`
              example: prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
        since:
          schema:
            - type: number
              description: Get aliases created after this JavaScript timestamp
              example: 1540095775941
        until:
          schema:
            - type: number
              description: Get aliases created before this JavaScript timestamp
              example: 1540095775951
        rollbackDeploymentId:
          schema:
            - type: string
              description: Get aliases that would be rolled back for the given deployment
              example: dpl_XXX
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
      - label: listAliases
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Aliases.ListAliases(ctx, operations.ListAliasesRequest{\n        Domain: vercel.Pointer(operations.CreateDomainStr(\n            \"my-test-domain.com\",\n        )),\n        From: vercel.Float64(1540095775951),\n        Limit: vercel.Float64(10),\n        ProjectID: vercel.String(\"prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB\"),\n        Since: vercel.Float64(1540095775941),\n        Until: vercel.Float64(1540095775951),\n        RollbackDeploymentID: vercel.String(\"dpl_XXX\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: listAliases
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.aliases.listAliases({
              domain: "my-test-domain.com",
              from: 1540095775951,
              limit: 10,
              projectId: "prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
              since: 1540095775941,
              until: 1540095775951,
              rollbackDeploymentId: "dpl_XXX",
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
              aliases:
                allOf:
                  - items:
                      properties:
                        alias:
                          type: string
                          description: >-
                            The alias name, it could be a `.vercel.app`
                            subdomain or a custom domain
                          example: my-alias.vercel.app
                        created:
                          type: string
                          format: date-time
                          description: The date when the alias was created
                          example: '2017-04-26T23:00:34.232Z'
                        createdAt:
                          type: number
                          description: >-
                            The date when the alias was created in milliseconds
                            since the UNIX epoch
                          example: 1540095775941
                        creator:
                          properties:
                            uid:
                              type: string
                              description: ID of the user who created the alias
                              example: 96SnxkFiMyVKsK3pnoHfx3Hz
                            email:
                              type: string
                              description: Email of the user who created the alias
                              example: john-doe@gmail.com
                            username:
                              type: string
                              description: Username of the user who created the alias
                              example: john-doe
                          required:
                            - uid
                            - email
                            - username
                          type: object
                          description: Information of the user who created the alias
                        deletedAt:
                          type: number
                          description: >-
                            The date when the alias was deleted in milliseconds
                            since the UNIX epoch
                          example: 1540095775941
                          nullable: true
                        deployment:
                          properties:
                            id:
                              type: string
                              description: The deployment unique identifier
                              example: dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx
                            url:
                              type: string
                              description: The deployment unique URL
                              example: my-instant-deployment-3ij3cxz9qr.now.sh
                            meta:
                              type: string
                              description: The deployment metadata
                              example: {}
                          required:
                            - id
                            - url
                          type: object
                          description: A map with the deployment ID, URL and metadata
                        deploymentId:
                          nullable: true
                          type: string
                          description: The deployment ID
                          example: dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx
                        projectId:
                          nullable: true
                          type: string
                          description: The unique identifier of the project
                          example: prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                        redirect:
                          nullable: true
                          type: string
                          description: >-
                            Target destination domain for redirect when the
                            alias is a redirect
                        redirectStatusCode:
                          nullable: true
                          type: number
                          enum:
                            - 301
                            - 302
                            - 307
                            - 308
                          description: Status code to be used on redirect
                        uid:
                          type: string
                          description: The unique identifier of the alias
                        updatedAt:
                          type: number
                          description: >-
                            The date when the alias was updated in milliseconds
                            since the UNIX epoch
                          example: 1540095775941
                        protectionBypass:
                          additionalProperties:
                            oneOf:
                              - properties:
                                  createdAt:
                                    type: number
                                  createdBy:
                                    type: string
                                  scope:
                                    type: string
                                    enum:
                                      - shareable-link
                                  expires:
                                    type: number
                                required:
                                  - createdAt
                                  - createdBy
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                              - properties:
                                  createdAt:
                                    type: number
                                  lastUpdatedAt:
                                    type: number
                                  lastUpdatedBy:
                                    type: string
                                  access:
                                    type: string
                                    enum:
                                      - requested
                                      - granted
                                  scope:
                                    type: string
                                    enum:
                                      - user
                                required:
                                  - createdAt
                                  - lastUpdatedAt
                                  - lastUpdatedBy
                                  - access
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                              - properties:
                                  createdAt:
                                    type: number
                                  createdBy:
                                    type: string
                                  scope:
                                    type: string
                                    enum:
                                      - alias-protection-override
                                required:
                                  - createdAt
                                  - createdBy
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                              - properties:
                                  createdAt:
                                    type: number
                                  lastUpdatedAt:
                                    type: number
                                  lastUpdatedBy:
                                    type: string
                                  scope:
                                    type: string
                                    enum:
                                      - email_invite
                                required:
                                  - createdAt
                                  - lastUpdatedAt
                                  - lastUpdatedBy
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                          type: object
                          description: The protection bypass for the alias
                        microfrontends:
                          properties:
                            defaultApp:
                              properties:
                                projectId:
                                  type: string
                              required:
                                - projectId
                              type: object
                            applications:
                              oneOf:
                                - items:
                                    properties:
                                      fallbackHost:
                                        type: string
                                        description: >-
                                          This is always set. In production it is
                                          used as a pointer to each apps
                                          production deployment. For
                                          pre-production, it's used as the
                                          fallback if there is no deployment for
                                          the branch.
                                      projectId:
                                        type: string
                                        description: >-
                                          The project ID of the microfrontends
                                          application.
                                    required:
                                      - fallbackHost
                                      - projectId
                                    type: object
                                    description: >-
                                      A list of the deployment routing
                                      information for each project.
                                  type: array
                                  description: >-
                                    A list of the deployment routing information
                                    for each project.
                                - items:
                                    properties:
                                      fallbackHost:
                                        type: string
                                        description: >-
                                          This is always set. For branch aliases,
                                          it's used as the fallback if there is no
                                          deployment for the branch.
                                      branchAlias:
                                        type: string
                                        description: >-
                                          Could point to a branch without a
                                          deployment if the project was never
                                          deployed. The proxy will fallback to the
                                          fallbackHost if there is no deployment.
                                      projectId:
                                        type: string
                                        description: >-
                                          The project ID of the microfrontends
                                          application.
                                    required:
                                      - fallbackHost
                                      - branchAlias
                                      - projectId
                                    type: object
                                    description: >-
                                      A list of the deployment routing
                                      information for each project.
                                  type: array
                                  description: >-
                                    A list of the deployment routing information
                                    for each project.
                                - items:
                                    properties:
                                      deploymentId:
                                        type: string
                                        description: >-
                                          This is the deployment for the same
                                          commit, it could be a cancelled
                                          deployment. The proxy will fallback to
                                          the branchDeploymentId and then the
                                          fallbackDeploymentId.
                                      branchDeploymentId:
                                        type: string
                                        description: >-
                                          This is the latest non-cancelled
                                          deployment of the branch alias at the
                                          time the commit alias was created. It is
                                          possible there is no deployment for the
                                          branch, or this was set before the
                                          deployment was canceled, in which case
                                          this will point to a cancelled
                                          deployment, in either case the proxy
                                          will fallback to the
                                          fallbackDeploymentId.
                                      fallbackDeploymentId:
                                        type: string
                                        description: >-
                                          This is the deployment of the fallback
                                          host at the time the commit alias was
                                          created. It is possible for this to be a
                                          deleted deployment, in which case the
                                          proxy will show that the deployment is
                                          deleted. It will not use the
                                          fallbackHost, as a future deployment on
                                          the fallback host could be invalid for
                                          this deployment, and it could lead to
                                          confusion / incorrect behavior for the
                                          commit alias.
                                      fallbackHost:
                                        type: string
                                        description: >-
                                          Temporary for backwards compatibility.
                                          Can remove when metadata change is
                                          released
                                      branchAlias:
                                        type: string
                                      projectId:
                                        type: string
                                        description: >-
                                          The project ID of the microfrontends
                                          application.
                                    required:
                                      - projectId
                                    type: object
                                    description: >-
                                      A list of the deployment routing
                                      information for each project.
                                  type: array
                                  description: >-
                                    A list of the deployment routing information
                                    for each project.
                          required:
                            - defaultApp
                            - applications
                          type: object
                          description: >-
                            The microfrontends for the alias including the
                            routing configuration
                      required:
                        - alias
                        - created
                        - deploymentId
                        - projectId
                        - uid
                      type: object
                    type: array
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            requiredProperties:
              - aliases
              - pagination
        examples:
          example:
            value:
              aliases:
                - alias: my-alias.vercel.app
                  created: '2017-04-26T23:00:34.232Z'
                  createdAt: 1540095775941
                  creator:
                    uid: 96SnxkFiMyVKsK3pnoHfx3Hz
                    email: john-doe@gmail.com
                    username: john-doe
                  deletedAt: 1540095775941
                  deployment:
                    id: dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx
                    url: my-instant-deployment-3ij3cxz9qr.now.sh
                    meta: {}
                  deploymentId: dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx
                  projectId: prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                  redirect: <string>
                  redirectStatusCode: 301
                  uid: <string>
                  updatedAt: 1540095775941
                  protectionBypass: {}
                  microfrontends:
                    defaultApp:
                      projectId: <string>
                    applications:
                      - fallbackHost: <string>
                        projectId: <string>
              pagination:
                count: 20
                next: 1540095775951
                prev: 1540095775951
        description: The paginated list of aliases
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
title: "List Deployment Aliases"

last_updated: "2025-11-07T00:37:07.784Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/aliases/list-deployment-aliases"
--------------------------------------------------------------------------------

# List Deployment Aliases

> Retrieves all Aliases for the Deployment with the given ID. The authenticated user or team must own the deployment.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/deployments/{id}/aliases
paths:
  path: /v2/deployments/{id}/aliases
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
              description: The ID of the deployment the aliases should be listed for
              example: dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa
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
      - label: listDeploymentAliases
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Aliases.ListDeploymentAliases(ctx, \"dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: listDeploymentAliases
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.aliases.listDeploymentAliases({
              id: "dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa",
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
              aliases:
                allOf:
                  - items:
                      properties:
                        uid:
                          type: string
                          description: The unique identifier of the alias
                          example: 2WjyKQmM8ZnGcJsPWMrHRHrE
                        alias:
                          type: string
                          description: >-
                            The alias name, it could be a `.vercel.app`
                            subdomain or a custom domain
                          example: my-alias.vercel.app
                        created:
                          type: string
                          format: date-time
                          description: The date when the alias was created
                          example: '2017-04-26T23:00:34.232Z'
                        redirect:
                          nullable: true
                          type: string
                          description: >-
                            Target destination domain for redirect when the
                            alias is a redirect
                        protectionBypass:
                          additionalProperties:
                            oneOf:
                              - properties:
                                  createdAt:
                                    type: number
                                  createdBy:
                                    type: string
                                  scope:
                                    type: string
                                    enum:
                                      - shareable-link
                                  expires:
                                    type: number
                                required:
                                  - createdAt
                                  - createdBy
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                              - properties:
                                  createdAt:
                                    type: number
                                  lastUpdatedAt:
                                    type: number
                                  lastUpdatedBy:
                                    type: string
                                  access:
                                    type: string
                                    enum:
                                      - requested
                                      - granted
                                  scope:
                                    type: string
                                    enum:
                                      - user
                                required:
                                  - createdAt
                                  - lastUpdatedAt
                                  - lastUpdatedBy
                                  - access
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                              - properties:
                                  createdAt:
                                    type: number
                                  createdBy:
                                    type: string
                                  scope:
                                    type: string
                                    enum:
                                      - alias-protection-override
                                required:
                                  - createdAt
                                  - createdBy
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                              - properties:
                                  createdAt:
                                    type: number
                                  lastUpdatedAt:
                                    type: number
                                  lastUpdatedBy:
                                    type: string
                                  scope:
                                    type: string
                                    enum:
                                      - email_invite
                                required:
                                  - createdAt
                                  - lastUpdatedAt
                                  - lastUpdatedBy
                                  - scope
                                type: object
                                description: The protection bypass for the alias
                          type: object
                          description: The protection bypass for the alias
                      required:
                        - uid
                        - alias
                        - created
                      type: object
                      description: A list of the aliases assigned to the deployment
                    type: array
                    description: A list of the aliases assigned to the deployment
            requiredProperties:
              - aliases
        examples:
          example:
            value:
              aliases:
                - uid: 2WjyKQmM8ZnGcJsPWMrHRHrE
                  alias: my-alias.vercel.app
                  created: '2017-04-26T23:00:34.232Z'
                  redirect: <string>
                  protectionBypass: {}
        description: The list of aliases assigned to the deployment
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
            description: The deployment was not found
        examples: {}
        description: The deployment was not found
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update the protection bypass for a URL"

last_updated: "2025-11-07T00:37:07.964Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/aliases/update-the-protection-bypass-for-a-url"
--------------------------------------------------------------------------------

# Update the protection bypass for a URL

> Update the protection bypass for the alias or deployment URL (used for user access & comment access for deployments). Used as shareable links and user scoped access for Vercel Authentication and also to allow external (logged in) people to comment on previews for Preview Comments (next-live-mode).

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /aliases/{id}/protection-bypass
paths:
  path: /aliases/{id}/protection-bypass
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
              description: The alias or deployment ID
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
              ttl:
                allOf:
                  - description: >-
                      Optional time the shareable link is valid for in seconds.
                      If not provided, the shareable link will never expire.
                    type: number
                    maximum: 63072000
              revoke:
                allOf:
                  - description: >-
                      Optional instructions for revoking and regenerating a
                      shareable link
                    type: object
                    properties:
                      secret:
                        description: Sharebale link to revoked
                        type: string
                      regenerate:
                        description: >-
                          Whether or not a new shareable link should be created
                          after the provided secret is revoked
                        type: boolean
                    required:
                      - secret
                      - regenerate
            additionalProperties: false
          - type: object
            properties:
              scope:
                allOf:
                  - description: Instructions for creating a user scoped protection bypass
                    type: object
                    properties:
                      userId:
                        type: string
                        description: Specified user id for the scoped bypass.
                      email:
                        type: string
                        format: email
                        description: Specified email for the scoped bypass.
                      access:
                        enum:
                          - denied
                          - granted
                        description: Invitation status for the user scoped bypass.
                    allOf:
                      - anyOf:
                          - required:
                              - userId
                          - required:
                              - email
                      - required:
                          - access
            requiredProperties:
              - scope
            additionalProperties: false
          - type: object
            properties:
              override:
                allOf:
                  - type: object
                    properties:
                      scope:
                        enum:
                          - alias-protection-override
                      action:
                        enum:
                          - create
                          - revoke
                    required:
                      - scope
                      - action
            requiredProperties:
              - override
            additionalProperties: false
        examples:
          example:
            value:
              ttl: 123
              revoke:
                secret: <string>
                regenerate: true
    codeSamples:
      - label: patchUrlProtectionBypass
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.aliases.patchUrlProtectionBypass({
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
            properties: {}
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
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
    '409': {}
    '428': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Check if a cache artifact exists"

last_updated: "2025-11-07T00:37:08.108Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/artifacts/check-if-a-cache-artifact-exists"
--------------------------------------------------------------------------------

# Check if a cache artifact exists

> Check that a cache artifact with the given `hash` exists. This request returns response headers only and is equivalent to a `GET` request to this endpoint where the response contains no body.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples head /v8/artifacts/{hash}
paths:
  path: /v8/artifacts/{hash}
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
        hash:
          schema:
            - type: string
              required: true
              description: The artifact hash
              example: 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
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
      - label: artifactExists
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Artifacts.ArtifactExists(ctx, \"12HKQaOmR5t5Uy6vdcQsNIiZgHGB\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: artifactExists
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.artifacts.artifactExists({
              hash: "12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });


          }

          run();
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The artifact was found and headers are returned
        examples: {}
        description: The artifact was found and headers are returned
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
            description: >-
              The customer has reached their spend cap limit and has been
              paused. An owner can disable the cap or raise the limit in
              settings.

              The Remote Caching usage limit has been reached for this account
              for this billing cycle.

              Remote Caching has been disabled for this team or user. An owner
              can enable it in the billing settings.

              You do not have permission to access this resource.
        examples: {}
        description: >-
          The customer has reached their spend cap limit and has been paused. An
          owner can disable the cap or raise the limit in settings.

          The Remote Caching usage limit has been reached for this account for
          this billing cycle.

          Remote Caching has been disabled for this team or user. An owner can
          enable it in the billing settings.

          You do not have permission to access this resource.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The artifact was not found
        examples: {}
        description: The artifact was not found
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Download a cache artifact"

last_updated: "2025-11-07T00:37:07.927Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/artifacts/download-a-cache-artifact"
--------------------------------------------------------------------------------

# Download a cache artifact

> Downloads a cache artifact indentified by its `hash` specified on the request path. The artifact is downloaded as an octet-stream. The client should verify the content-length header and response body.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v8/artifacts/{hash}
paths:
  path: /v8/artifacts/{hash}
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
        hash:
          schema:
            - type: string
              required: true
              description: The artifact hash
              example: 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
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
      header:
        x-artifact-client-ci:
          schema:
            - type: string
              description: >-
                The continuous integration or delivery environment where this
                artifact is downloaded.
              maxLength: 50
              example: VERCEL
        x-artifact-client-interactive:
          schema:
            - type: integer
              description: 1 if the client is an interactive shell. Otherwise 0
              maximum: 1
              minimum: 0
              example: 0
      cookie: {}
    body: {}
    codeSamples:
      - label: downloadArtifact
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Artifacts.DownloadArtifact(ctx, operations.DownloadArtifactRequest{\n        XArtifactClientCi: vercel.String(\"VERCEL\"),\n        XArtifactClientInteractive: vercel.Int64(0),\n        Hash: \"12HKQaOmR5t5Uy6vdcQsNIiZgHGB\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.ResponseStream != nil {\n        // handle response\n    }\n}"
      - label: downloadArtifact
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.artifacts.downloadArtifact({
              xArtifactClientCi: "VERCEL",
              xArtifactClientInteractive: 0,
              hash: "12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
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
          - type: file
            contentEncoding: binary
            description: >-
              An octet stream response that will be piped to the response
              stream.
        examples:
          example: {}
        description: >-
          The artifact was found and is downloaded as a stream. Content-Length
          should be verified.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request query is invalid.
              One of the provided values in the headers is invalid
        examples: {}
        description: |-
          One of the provided values in the request query is invalid.
          One of the provided values in the headers is invalid
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
              The customer has reached their spend cap limit and has been
              paused. An owner can disable the cap or raise the limit in
              settings.

              The Remote Caching usage limit has been reached for this account
              for this billing cycle.

              Remote Caching has been disabled for this team or user. An owner
              can enable it in the billing settings.

              You do not have permission to access this resource.
        examples: {}
        description: >-
          The customer has reached their spend cap limit and has been paused. An
          owner can disable the cap or raise the limit in settings.

          The Remote Caching usage limit has been reached for this account for
          this billing cycle.

          Remote Caching has been disabled for this team or user. An owner can
          enable it in the billing settings.

          You do not have permission to access this resource.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The artifact was not found
        examples: {}
        description: The artifact was not found
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get status of Remote Caching for this principal"

last_updated: "2025-11-07T00:37:08.142Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/artifacts/get-status-of-remote-caching-for-this-principal"
--------------------------------------------------------------------------------

# Get status of Remote Caching for this principal

> Check the status of Remote Caching for this principal. Returns a JSON-encoded status indicating if Remote Caching is enabled, disabled, or disabled due to usage limits.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v8/artifacts/status
paths:
  path: /v8/artifacts/status
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
      - label: status
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Artifacts.Status(ctx, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: status
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.artifacts.status({
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
                    enum:
                      - disabled
                      - enabled
                      - over_limit
                      - paused
            requiredProperties:
              - status
        examples:
          example:
            value:
              status: disabled
        description: ''
    '400': {}
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
title: "Query information about an artifact"

last_updated: "2025-11-07T00:37:08.080Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/artifacts/query-information-about-an-artifact"
--------------------------------------------------------------------------------

# Query information about an artifact

> Query information about an array of artifacts.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v8/artifacts
paths:
  path: /v8/artifacts
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
              hashes:
                allOf:
                  - items:
                      type: string
                    description: artifact hashes
                    type: array
                    example:
                      - 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                      - 34HKQaOmR5t5Uy6vasdasdasdasd
            required: true
            requiredProperties:
              - hashes
        examples:
          example:
            value:
              hashes:
                - 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                - 34HKQaOmR5t5Uy6vasdasdasdasd
    codeSamples:
      - label: artifactQuery
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Artifacts.ArtifactQuery(ctx, nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: artifactQuery
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.artifacts.artifactQuery({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                hashes: [
                  "12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
                  "34HKQaOmR5t5Uy6vasdasdasdasd",
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
            properties: {}
            additionalProperties:
              allOf:
                - nullable: true
                  oneOf:
                    - properties:
                        size:
                          type: number
                        taskDurationMs:
                          type: number
                        tag:
                          type: string
                      required:
                        - size
                        - taskDurationMs
                      type: object
                    - properties:
                        error:
                          properties:
                            message:
                              type: string
                          required:
                            - message
                          type: object
                      required:
                        - error
                      type: object
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
              The customer has reached their spend cap limit and has been
              paused. An owner can disable the cap or raise the limit in
              settings.

              The Remote Caching usage limit has been reached for this account
              for this billing cycle.

              Remote Caching has been disabled for this team or user. An owner
              can enable it in the billing settings.

              You do not have permission to access this resource.
        examples: {}
        description: >-
          The customer has reached their spend cap limit and has been paused. An
          owner can disable the cap or raise the limit in settings.

          The Remote Caching usage limit has been reached for this account for
          this billing cycle.

          Remote Caching has been disabled for this team or user. An owner can
          enable it in the billing settings.

          You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Record an artifacts cache usage event"

last_updated: "2025-11-07T00:37:07.948Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/artifacts/record-an-artifacts-cache-usage-event"
--------------------------------------------------------------------------------

# Record an artifacts cache usage event

> Records an artifacts cache usage event. The body of this request is an array of cache usage events. The supported event types are `HIT` and `MISS`. The source is either `LOCAL` the cache event was on the users filesystem cache or `REMOTE` if the cache event is for a remote cache. When the event is a `HIT` the request also accepts a number `duration` which is the time taken to generate the artifact in the cache.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v8/artifacts/events
paths:
  path: /v8/artifacts/events
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
      header:
        x-artifact-client-ci:
          schema:
            - type: string
              description: >-
                The continuous integration or delivery environment where this
                artifact is downloaded.
              maxLength: 50
              example: VERCEL
        x-artifact-client-interactive:
          schema:
            - type: integer
              description: 1 if the client is an interactive shell. Otherwise 0
              maximum: 1
              minimum: 0
              example: 0
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - type: object
                  additionalProperties: false
                  required:
                    - sessionId
                    - source
                    - hash
                    - event
                  properties:
                    sessionId:
                      type: string
                      description: >-
                        A UUID (universally unique identifer) for the session
                        that generated this event.
                    source:
                      type: string
                      enum:
                        - LOCAL
                        - REMOTE
                      description: >-
                        One of `LOCAL` or `REMOTE`. `LOCAL` specifies that the
                        cache event was from the user's filesystem cache.
                        `REMOTE` specifies that the cache event is from a remote
                        cache.
                    event:
                      type: string
                      enum:
                        - HIT
                        - MISS
                      description: >-
                        One of `HIT` or `MISS`. `HIT` specifies that a cached
                        artifact for `hash` was found in the cache. `MISS`
                        specifies that a cached artifact with `hash` was not
                        found.
                    hash:
                      type: string
                      example: 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                      description: The artifact hash
                    duration:
                      type: number
                      description: >-
                        The time taken to generate the artifact. This should be
                        sent as a body parameter on `HIT` events.
                      example: 400
            required: true
        examples:
          example:
            value:
              - sessionId: <string>
                source: LOCAL
                event: HIT
                hash: 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                duration: 400
    codeSamples:
      - label: recordEvents
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Artifacts.RecordEvents(ctx, operations.RecordEventsRequest{\n        XArtifactClientCi: vercel.String(\"VERCEL\"),\n        XArtifactClientInteractive: vercel.Int64(0),\n        RequestBody: []operations.RequestBody{\n            operations.RequestBody{\n                SessionID: \"<id>\",\n                Source: operations.SourceLocal,\n                Event: operations.EventHit,\n                Hash: \"12HKQaOmR5t5Uy6vdcQsNIiZgHGB\",\n                Duration: vercel.Float64(400),\n            },\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: recordEvents
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.artifacts.recordEvents({
              xArtifactClientCi: "VERCEL",
              xArtifactClientInteractive: 0,
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: [],
            });


          }

          run();
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Success. Event recorded.
        examples: {}
        description: Success. Event recorded.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the headers is invalid
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the headers is invalid
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
              The customer has reached their spend cap limit and has been
              paused. An owner can disable the cap or raise the limit in
              settings.

              The Remote Caching usage limit has been reached for this account
              for this billing cycle.

              Remote Caching has been disabled for this team or user. An owner
              can enable it in the billing settings.

              You do not have permission to access this resource.
        examples: {}
        description: >-
          The customer has reached their spend cap limit and has been paused. An
          owner can disable the cap or raise the limit in settings.

          The Remote Caching usage limit has been reached for this account for
          this billing cycle.

          Remote Caching has been disabled for this team or user. An owner can
          enable it in the billing settings.

          You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Upload a cache artifact"

last_updated: "2025-11-07T00:37:08.115Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/artifacts/upload-a-cache-artifact"
--------------------------------------------------------------------------------

# Upload a cache artifact

> Uploads a cache artifact identified by the `hash` specified on the path. The cache artifact can then be downloaded with the provided `hash`.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v8/artifacts/{hash}
paths:
  path: /v8/artifacts/{hash}
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
        hash:
          schema:
            - type: string
              required: true
              description: The artifact hash
              example: 12HKQaOmR5t5Uy6vdcQsNIiZgHGB
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
      header:
        Content-Length:
          schema:
            - type: number
              required: true
              description: The artifact size in bytes
        x-artifact-duration:
          schema:
            - type: number
              required: false
              description: >-
                The time taken to generate the uploaded artifact in
                milliseconds.
              example: 400
        x-artifact-client-ci:
          schema:
            - type: string
              required: false
              description: >-
                The continuous integration or delivery environment where this
                artifact was generated.
              maxLength: 50
              example: VERCEL
        x-artifact-client-interactive:
          schema:
            - type: integer
              required: false
              description: 1 if the client is an interactive shell. Otherwise 0
              maximum: 1
              minimum: 0
              example: 0
        x-artifact-tag:
          schema:
            - type: string
              required: false
              description: >-
                The base64 encoded tag for this artifact. The value is sent back
                to clients when the artifact is downloaded as the header
                `x-artifact-tag`
              maxLength: 600
              example: Tc0BmHvJYMIYJ62/zx87YqO0Flxk+5Ovip25NY825CQ=
      cookie: {}
    body:
      application/octet-stream:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
    codeSamples:
      - label: uploadArtifact
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Artifacts.UploadArtifact(ctx, operations.UploadArtifactRequest{\n        ContentLength: 4504.13,\n        XArtifactDuration: vercel.Float64(400),\n        XArtifactClientCi: vercel.String(\"VERCEL\"),\n        XArtifactClientInteractive: vercel.Int64(0),\n        XArtifactTag: vercel.String(\"Tc0BmHvJYMIYJ62/zx87YqO0Flxk+5Ovip25NY825CQ=\"),\n        Hash: \"12HKQaOmR5t5Uy6vdcQsNIiZgHGB\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: uploadArtifact
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";
          import { openAsBlob } from "node:fs";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.artifacts.uploadArtifact({
              contentLength: 3848.22,
              xArtifactDuration: 400,
              xArtifactClientCi: "VERCEL",
              xArtifactClientInteractive: 0,
              xArtifactTag: "Tc0BmHvJYMIYJ62/zx87YqO0Flxk+5Ovip25NY825CQ=",
              hash: "12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: await openAsBlob("example.file"),
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
              urls:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: Array of URLs where the artifact was updated
                    example:
                      - >-
                        https://api.vercel.com/v2/now/artifact/12HKQaOmR5t5Uy6vdcQsNIiZgHGB
            requiredProperties:
              - urls
        examples:
          example:
            value:
              urls:
                - >-
                  https://api.vercel.com/v2/now/artifact/12HKQaOmR5t5Uy6vdcQsNIiZgHGB
        description: File successfully uploaded
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request query is invalid.
              One of the provided values in the headers is invalid
              File size is not valid
        examples: {}
        description: |-
          One of the provided values in the request query is invalid.
          One of the provided values in the headers is invalid
          File size is not valid
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
              The customer has reached their spend cap limit and has been
              paused. An owner can disable the cap or raise the limit in
              settings.

              The Remote Caching usage limit has been reached for this account
              for this billing cycle.

              Remote Caching has been disabled for this team or user. An owner
              can enable it in the billing settings.

              You do not have permission to access this resource.
        examples: {}
        description: >-
          The customer has reached their spend cap limit and has been paused. An
          owner can disable the cap or raise the limit in settings.

          The Remote Caching usage limit has been reached for this account for
          this billing cycle.

          Remote Caching has been disabled for this team or user. An owner can
          enable it in the billing settings.

          You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Create an Auth Token"

last_updated: "2025-11-07T00:37:08.012Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/authentication/create-an-auth-token"
--------------------------------------------------------------------------------

# Create an Auth Token

> Creates and returns a new authentication token for the currently authenticated User. The `bearerToken` property is only provided once, in the response body, so be sure to save it on the client for use with API requests.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v3/user/tokens
paths:
  path: /v3/user/tokens
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
              expiresAt:
                allOf:
                  - type: number
            required: true
            requiredProperties:
              - name
            additionalProperties: false
        examples:
          example:
            value:
              name: <string>
              expiresAt: 123
    codeSamples:
      - label: createAuthToken
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Authentication.CreateAuthToken(ctx, nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createAuthToken
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.authentication.createAuthToken({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "<value>",
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
              token:
                allOf:
                  - $ref: '#/components/schemas/AuthToken'
              bearerToken:
                allOf:
                  - type: string
                    description: >-
                      The authentication token's actual value. This token is
                      only provided in this response, and can never be retrieved
                      again in the future. Be sure to save it somewhere safe!
                    example: uRKJSTt0L4RaSkiMj41QTkxM
            description: Successful response.
            requiredProperties:
              - token
              - bearerToken
        examples:
          example:
            value:
              token:
                id: >-
                  5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
                name: <string>
                type: oauth2-token
                origin: github
                scopes:
                  - type: user
                    sudo:
                      origin: totp
                      expiresAt: 123
                    origin: saml
                    createdAt: 123
                    expiresAt: 123
                expiresAt: 1632816536002
                activeAt: 1632816536002
                createdAt: 1632816536002
              bearerToken: uRKJSTt0L4RaSkiMj41QTkxM
        description: Successful response.
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
  schemas:
    AuthToken:
      properties:
        id:
          type: string
          description: The unique identifier of the token.
          example: 5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
        name:
          type: string
          description: The human-readable name of the token.
        type:
          type: string
          description: The type of the token.
          example: oauth2-token
        origin:
          type: string
          description: The origin of how the token was created.
          example: github
        scopes:
          items:
            oneOf:
              - properties:
                  type:
                    type: string
                    enum:
                      - user
                  sudo:
                    properties:
                      origin:
                        type: string
                        enum:
                          - totp
                          - webauthn
                          - recovery-code
                        description: Possible multi-factor origins
                      expiresAt:
                        type: number
                    required:
                      - origin
                      - expiresAt
                    type: object
                  origin:
                    type: string
                    enum:
                      - saml
                      - github
                      - gitlab
                      - bitbucket
                      - email
                      - manual
                      - passkey
                      - otp
                      - sms
                      - invite
                      - google
                      - apple
                      - app
                  createdAt:
                    type: number
                  expiresAt:
                    type: number
                required:
                  - type
                  - createdAt
                type: object
                description: The access scopes granted to the token.
              - properties:
                  type:
                    type: string
                    enum:
                      - team
                  teamId:
                    type: string
                  origin:
                    type: string
                    enum:
                      - saml
                      - github
                      - gitlab
                      - bitbucket
                      - email
                      - manual
                      - passkey
                      - otp
                      - sms
                      - invite
                      - google
                      - apple
                      - app
                  createdAt:
                    type: number
                  expiresAt:
                    type: number
                required:
                  - type
                  - teamId
                  - createdAt
                type: object
                description: The access scopes granted to the token.
          type: array
          description: The access scopes granted to the token.
        expiresAt:
          type: number
          description: Timestamp (in milliseconds) of when the token expires.
          example: 1632816536002
        activeAt:
          type: number
          description: >-
            Timestamp (in milliseconds) of when the token was most recently
            used.
          example: 1632816536002
        createdAt:
          type: number
          description: Timestamp (in milliseconds) of when the token was created.
          example: 1632816536002
      required:
        - id
        - name
        - type
        - activeAt
        - createdAt
      type: object
      description: Authentication token metadata.

````

--------------------------------------------------------------------------------
title: "Delete an authentication token"

last_updated: "2025-11-07T00:37:08.246Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/authentication/delete-an-authentication-token"
--------------------------------------------------------------------------------

# Delete an authentication token

> Invalidate an authentication token, such that it will no longer be valid for future HTTP requests.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v3/user/tokens/{tokenId}
paths:
  path: /v3/user/tokens/{tokenId}
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
        tokenId:
          schema:
            - type: string
              required: true
              description: >-
                The identifier of the token to invalidate. The special value
                \"current\" may be supplied, which invalidates the token that
                the HTTP request was authenticated with.
              example: 5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: deleteAuthToken
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Authentication.DeleteAuthToken(ctx, \"5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: deleteAuthToken
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.authentication.deleteAuthToken({
              tokenId: "5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391",
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
              tokenId:
                allOf:
                  - type: string
                    description: The unique identifier of the token that was deleted.
                    example: >-
                      5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
            description: Authentication token successfully deleted.
            requiredProperties:
              - tokenId
        examples:
          example:
            value:
              tokenId: 5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
        description: Authentication token successfully deleted.
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
            description: Token not found with the requested `tokenId`.
        examples: {}
        description: Token not found with the requested `tokenId`.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get Auth Token Metadata"

last_updated: "2025-11-07T00:37:08.036Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/authentication/get-auth-token-metadata"
--------------------------------------------------------------------------------

# Get Auth Token Metadata

> Retrieve metadata about an authentication token belonging to the currently authenticated User.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v5/user/tokens/{tokenId}
paths:
  path: /v5/user/tokens/{tokenId}
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
        tokenId:
          schema:
            - type: string
              required: true
              description: >-
                The identifier of the token to retrieve. The special value
                \"current\" may be supplied, which returns the metadata for the
                token that the current HTTP request is authenticated with.
              example: 5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getAuthToken
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Authentication.GetAuthToken(ctx, \"5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getAuthToken
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.authentication.getAuthToken({
              tokenId: "5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391",
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
                  - $ref: '#/components/schemas/AuthToken'
            description: Successful response.
            requiredProperties:
              - token
        examples:
          example:
            value:
              token:
                id: >-
                  5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
                name: <string>
                type: oauth2-token
                origin: github
                scopes:
                  - type: user
                    sudo:
                      origin: totp
                      expiresAt: 123
                    origin: saml
                    createdAt: 123
                    expiresAt: 123
                expiresAt: 1632816536002
                activeAt: 1632816536002
                createdAt: 1632816536002
        description: Successful response.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401': {}
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
            description: Token not found with the requested `tokenId`.
        examples: {}
        description: Token not found with the requested `tokenId`.
  deprecated: false
  type: path
components:
  schemas:
    AuthToken:
      properties:
        id:
          type: string
          description: The unique identifier of the token.
          example: 5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
        name:
          type: string
          description: The human-readable name of the token.
        type:
          type: string
          description: The type of the token.
          example: oauth2-token
        origin:
          type: string
          description: The origin of how the token was created.
          example: github
        scopes:
          items:
            oneOf:
              - properties:
                  type:
                    type: string
                    enum:
                      - user
                  sudo:
                    properties:
                      origin:
                        type: string
                        enum:
                          - totp
                          - webauthn
                          - recovery-code
                        description: Possible multi-factor origins
                      expiresAt:
                        type: number
                    required:
                      - origin
                      - expiresAt
                    type: object
                  origin:
                    type: string
                    enum:
                      - saml
                      - github
                      - gitlab
                      - bitbucket
                      - email
                      - manual
                      - passkey
                      - otp
                      - sms
                      - invite
                      - google
                      - apple
                      - app
                  createdAt:
                    type: number
                  expiresAt:
                    type: number
                required:
                  - type
                  - createdAt
                type: object
                description: The access scopes granted to the token.
              - properties:
                  type:
                    type: string
                    enum:
                      - team
                  teamId:
                    type: string
                  origin:
                    type: string
                    enum:
                      - saml
                      - github
                      - gitlab
                      - bitbucket
                      - email
                      - manual
                      - passkey
                      - otp
                      - sms
                      - invite
                      - google
                      - apple
                      - app
                  createdAt:
                    type: number
                  expiresAt:
                    type: number
                required:
                  - type
                  - teamId
                  - createdAt
                type: object
                description: The access scopes granted to the token.
          type: array
          description: The access scopes granted to the token.
        expiresAt:
          type: number
          description: Timestamp (in milliseconds) of when the token expires.
          example: 1632816536002
        activeAt:
          type: number
          description: >-
            Timestamp (in milliseconds) of when the token was most recently
            used.
          example: 1632816536002
        createdAt:
          type: number
          description: Timestamp (in milliseconds) of when the token was created.
          example: 1632816536002
      required:
        - id
        - name
        - type
        - activeAt
        - createdAt
      type: object
      description: Authentication token metadata.

````

--------------------------------------------------------------------------------
title: "List Auth Tokens"

last_updated: "2025-11-07T00:37:08.165Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/authentication/list-auth-tokens"
--------------------------------------------------------------------------------

# List Auth Tokens

> Retrieve a list of the current User's authentication tokens.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v5/user/tokens
paths:
  path: /v5/user/tokens
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
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: listAuthTokens
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Authentication.ListAuthTokens(ctx)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: listAuthTokens
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.authentication.listAuthTokens();

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              tokens:
                allOf:
                  - items:
                      $ref: '#/components/schemas/AuthToken'
                    type: array
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            requiredProperties:
              - tokens
              - pagination
        examples:
          example:
            value:
              tokens:
                - id: >-
                    5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
                  name: <string>
                  type: oauth2-token
                  origin: github
                  scopes:
                    - type: user
                      sudo:
                        origin: totp
                        expiresAt: 123
                      origin: saml
                      createdAt: 123
                      expiresAt: 123
                  expiresAt: 1632816536002
                  activeAt: 1632816536002
                  createdAt: 1632816536002
              pagination:
                count: 20
                next: 1540095775951
                prev: 1540095775951
        description: ''
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
    AuthToken:
      properties:
        id:
          type: string
          description: The unique identifier of the token.
          example: 5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391
        name:
          type: string
          description: The human-readable name of the token.
        type:
          type: string
          description: The type of the token.
          example: oauth2-token
        origin:
          type: string
          description: The origin of how the token was created.
          example: github
        scopes:
          items:
            oneOf:
              - properties:
                  type:
                    type: string
                    enum:
                      - user
                  sudo:
                    properties:
                      origin:
                        type: string
                        enum:
                          - totp
                          - webauthn
                          - recovery-code
                        description: Possible multi-factor origins
                      expiresAt:
                        type: number
                    required:
                      - origin
                      - expiresAt
                    type: object
                  origin:
                    type: string
                    enum:
                      - saml
                      - github
                      - gitlab
                      - bitbucket
                      - email
                      - manual
                      - passkey
                      - otp
                      - sms
                      - invite
                      - google
                      - apple
                      - app
                  createdAt:
                    type: number
                  expiresAt:
                    type: number
                required:
                  - type
                  - createdAt
                type: object
                description: The access scopes granted to the token.
              - properties:
                  type:
                    type: string
                    enum:
                      - team
                  teamId:
                    type: string
                  origin:
                    type: string
                    enum:
                      - saml
                      - github
                      - gitlab
                      - bitbucket
                      - email
                      - manual
                      - passkey
                      - otp
                      - sms
                      - invite
                      - google
                      - apple
                      - app
                  createdAt:
                    type: number
                  expiresAt:
                    type: number
                required:
                  - type
                  - teamId
                  - createdAt
                type: object
                description: The access scopes granted to the token.
          type: array
          description: The access scopes granted to the token.
        expiresAt:
          type: number
          description: Timestamp (in milliseconds) of when the token expires.
          example: 1632816536002
        activeAt:
          type: number
          description: >-
            Timestamp (in milliseconds) of when the token was most recently
            used.
          example: 1632816536002
        createdAt:
          type: number
          description: Timestamp (in milliseconds) of when the token was created.
          example: 1632816536002
      required:
        - id
        - name
        - type
        - activeAt
        - createdAt
      type: object
      description: Authentication token metadata.

````

--------------------------------------------------------------------------------
title: "SSO Token Exchange"

last_updated: "2025-11-07T00:37:07.958Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/authentication/sso-token-exchange"
--------------------------------------------------------------------------------

# SSO Token Exchange

> During the autorization process, Vercel sends the user to the provider [redirectLoginUrl](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-login-url), that includes the OAuth authorization `code` parameter. The provider then calls the SSO Token Exchange endpoint with the sent code and receives the OIDC token. They log the user in based on this token and redirects the user back to the Vercel account using deep-link parameters included the redirectLoginUrl. Providers should not persist the returned `id_token` in a database since the token will expire. See [**Authentication with SSO**](https://vercel.com/docs/integrations/create-integration/marketplace-api#authentication-with-sso) for more details.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/integrations/sso/token
paths:
  path: /v1/integrations/sso/token
  method: post
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security: []
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              code:
                allOf:
                  - type: string
                    description: The sensitive code received from Vercel
              state:
                allOf:
                  - type: string
                    description: The state received from the initialization request
              client_id:
                allOf:
                  - type: string
                    description: The integration client id
              client_secret:
                allOf:
                  - type: string
                    description: The integration client secret
              redirect_uri:
                allOf:
                  - type: string
                    description: The integration redirect URI
              grant_type:
                allOf:
                  - type: string
                    description: >-
                      The grant type, when using x-www-form-urlencoded content
                      type
                    enum:
                      - authorization_code
            required: true
            requiredProperties:
              - code
              - client_id
              - client_secret
        examples:
          example:
            value:
              code: <string>
              state: <string>
              client_id: <string>
              client_secret: <string>
              redirect_uri: <string>
              grant_type: authorization_code
    codeSamples:
      - label: exchange-sso-token
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel();

          async function run() {
            const result = await vercel.authentication.exchangeSsoToken({
              code: "<value>",
              clientId: "<id>",
              clientSecret: "<value>",
            });

            console.log(result);
          }

          run();
      - label: exchange-sso-token
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel();

          async function run() {
            const result = await vercel.marketplace.exchangeSsoToken({
              code: "<value>",
              clientId: "<id>",
              clientSecret: "<value>",
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
              id_token:
                allOf:
                  - type: string
              access_token:
                allOf:
                  - nullable: true
                    type: string
              token_type:
                allOf:
                  - nullable: true
                    type: string
              expires_in:
                allOf:
                  - type: number
            requiredProperties:
              - id_token
              - access_token
              - token_type
        examples:
          example:
            value:
              id_token: <string>
              access_token: <string>
              token_type: <string>
              expires_in: 123
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
    '403': {}
    '404': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get cert by id"

last_updated: "2025-11-07T00:37:07.944Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/certs/get-cert-by-id"
--------------------------------------------------------------------------------

# Get cert by id

> Get cert by id

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v8/certs/{id}
paths:
  path: /v8/certs/{id}
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
              description: The cert id
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
      - label: getCertById
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.certs.getCertById({
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
              createdAt:
                allOf:
                  - type: number
              expiresAt:
                allOf:
                  - type: number
              autoRenew:
                allOf:
                  - type: boolean
              cns:
                allOf:
                  - items:
                      type: string
                    type: array
            requiredProperties:
              - id
              - createdAt
              - expiresAt
              - autoRenew
              - cns
        examples:
          example:
            value:
              id: <string>
              createdAt: 123
              expiresAt: 123
              autoRenew: true
              cns:
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
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Issue a new cert"

last_updated: "2025-11-07T00:37:08.177Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/certs/issue-a-new-cert"
--------------------------------------------------------------------------------

# Issue a new cert

> Issue a new cert

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v8/certs
paths:
  path: /v8/certs
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
              cns:
                allOf:
                  - description: The common names the cert should be issued for
                    type: array
                    items:
                      type: string
        examples:
          example:
            value:
              cns:
                - <string>
    codeSamples:
      - label: issueCert
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.certs.issueCert({
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
              createdAt:
                allOf:
                  - type: number
              expiresAt:
                allOf:
                  - type: number
              autoRenew:
                allOf:
                  - type: boolean
              cns:
                allOf:
                  - items:
                      type: string
                    type: array
            requiredProperties:
              - id
              - createdAt
              - expiresAt
              - autoRenew
              - cns
        examples:
          example:
            value:
              id: <string>
              createdAt: 123
              expiresAt: 123
              autoRenew: true
              cns:
                - <string>
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
    '449': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Remove cert"

last_updated: "2025-11-07T00:37:08.586Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/certs/remove-cert"
--------------------------------------------------------------------------------

# Remove cert

> Remove cert

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v8/certs/{id}
paths:
  path: /v8/certs/{id}
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
              description: The cert id to remove
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
      - label: removeCert
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.certs.removeCert({
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
            properties: {}
        examples:
          example:
            value: {}
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
title: "Upload a cert"

last_updated: "2025-11-07T00:37:08.929Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/certs/upload-a-cert"
--------------------------------------------------------------------------------

# Upload a cert

> Upload a cert

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v8/certs
paths:
  path: /v8/certs
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
              ca:
                allOf:
                  - type: string
                    description: The certificate authority
              key:
                allOf:
                  - type: string
                    description: The certificate key
              cert:
                allOf:
                  - type: string
                    description: The certificate
              skipValidation:
                allOf:
                  - type: boolean
                    description: Skip validation of the certificate
            requiredProperties:
              - ca
              - key
              - cert
            additionalProperties: false
        examples:
          example:
            value:
              ca: <string>
              key: <string>
              cert: <string>
              skipValidation: true
    codeSamples:
      - label: uploadCert
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.certs.uploadCert({
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
              createdAt:
                allOf:
                  - type: number
              expiresAt:
                allOf:
                  - type: number
              autoRenew:
                allOf:
                  - type: boolean
              cns:
                allOf:
                  - items:
                      type: string
                    type: array
            requiredProperties:
              - id
              - createdAt
              - expiresAt
              - autoRenew
              - cns
        examples:
          example:
            value:
              id: <string>
              createdAt: 123
              expiresAt: 123
              autoRenew: true
              cns:
                - <string>
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
            description: This feature is only available for Enterprise customers.
        examples: {}
        description: This feature is only available for Enterprise customers.
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
title: "Creates a new Check"

last_updated: "2025-11-07T00:37:08.549Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/checks/creates-a-new-check"
--------------------------------------------------------------------------------

# Creates a new Check

> Creates a new check. This endpoint must be called with an OAuth2 or it will produce a 400 error.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/deployments/{deploymentId}/checks
paths:
  path: /v1/deployments/{deploymentId}/checks
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
        deploymentId:
          schema:
            - type: string
              required: true
              description: The deployment to create the check for.
              example: dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6
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
                  - description: The name of the check being created
                    maxLength: 100
                    example: Performance Check
                    type: string
              path:
                allOf:
                  - description: Path of the page that is being checked
                    type: string
                    maxLength: 255
                    example: /
              blocking:
                allOf:
                  - description: >-
                      Whether the check should block a deployment from
                      succeeding
                    type: boolean
                    example: true
              detailsUrl:
                allOf:
                  - description: URL to display for further details
                    type: string
                    example: http://example.com
              externalId:
                allOf:
                  - description: An identifier that can be used as an external reference
                    type: string
                    example: 1234abc
              rerequestable:
                allOf:
                  - description: >-
                      Whether a user should be able to request for the check to
                      be rerun if it fails
                    type: boolean
                    example: true
            required: true
            requiredProperties:
              - name
              - blocking
        examples:
          example:
            value:
              name: Performance Check
              path: /
              blocking: true
              detailsUrl: http://example.com
              externalId: 1234abc
              rerequestable: true
    codeSamples:
      - label: createCheck
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Checks.CreateCheck(ctx, \"dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6\", nil, nil, &operations.CreateCheckRequestBody{\n        Name: \"Performance Check\",\n        Path: vercel.String(\"/\"),\n        Blocking: true,\n        DetailsURL: vercel.String(\"http://example.com\"),\n        ExternalID: vercel.String(\"1234abc\"),\n        Rerequestable: vercel.Bool(true),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createCheck
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.checks.createCheck({
              deploymentId: "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "Performance Check",
                path: "/",
                blocking: true,
                detailsUrl: "http://example.com",
                externalId: "1234abc",
                rerequestable: true,
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
                    example: chk_1a2b3c4d5e6f7g8h9i0j
              name:
                allOf:
                  - type: string
                    example: Performance Check
              path:
                allOf:
                  - type: string
                    example: /api/users
              status:
                allOf:
                  - type: string
                    enum:
                      - registered
                      - running
                      - completed
                    example: completed
              conclusion:
                allOf:
                  - type: string
                    enum:
                      - canceled
                      - failed
                      - neutral
                      - succeeded
                      - skipped
                      - stale
                    example: succeeded
              blocking:
                allOf:
                  - type: boolean
              output:
                allOf:
                  - properties:
                      metrics:
                        properties:
                          FCP:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          LCP:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          CLS:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          TBT:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          virtualExperienceScore:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                        required:
                          - FCP
                          - LCP
                          - CLS
                          - TBT
                        type: object
                    type: object
              detailsUrl:
                allOf:
                  - type: string
              integrationId:
                allOf:
                  - type: string
              deploymentId:
                allOf:
                  - type: string
              externalId:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
              startedAt:
                allOf:
                  - type: number
              completedAt:
                allOf:
                  - type: number
              rerequestable:
                allOf:
                  - type: boolean
            requiredProperties:
              - id
              - name
              - status
              - blocking
              - integrationId
              - deploymentId
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: chk_1a2b3c4d5e6f7g8h9i0j
              name: Performance Check
              path: /api/users
              status: completed
              conclusion: succeeded
              blocking: true
              output:
                metrics:
                  FCP:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  LCP:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  CLS:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  TBT:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  virtualExperienceScore:
                    value: 123
                    previousValue: 123
                    source: web-vitals
              detailsUrl: <string>
              integrationId: <string>
              deploymentId: <string>
              externalId: <string>
              createdAt: 123
              updatedAt: 123
              startedAt: 123
              completedAt: 123
              rerequestable: true
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
              Cannot create check for finished deployment
              The provided token is not from an OAuth2 Client
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
          Cannot create check for finished deployment
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
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The deployment was not found
        examples: {}
        description: The deployment was not found
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get a single check"

last_updated: "2025-11-07T00:37:08.567Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/checks/get-a-single-check"
--------------------------------------------------------------------------------

# Get a single check

> Return a detailed response for a single check.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/deployments/{deploymentId}/checks/{checkId}
paths:
  path: /v1/deployments/{deploymentId}/checks/{checkId}
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
        deploymentId:
          schema:
            - type: string
              required: true
              description: The deployment to get the check for.
              example: dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6
        checkId:
          schema:
            - type: string
              required: true
              description: The check to fetch
              example: check_2qn7PZrx89yxY34vEZPD31Y9XVj6
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
      - label: getCheck
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Checks.GetCheck(ctx, \"dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6\", \"check_2qn7PZrx89yxY34vEZPD31Y9XVj6\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getCheck
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.checks.getCheck({
              deploymentId: "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6",
              checkId: "check_2qn7PZrx89yxY34vEZPD31Y9XVj6",
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
              name:
                allOf:
                  - type: string
              path:
                allOf:
                  - type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - registered
                      - running
                      - completed
              conclusion:
                allOf:
                  - type: string
                    enum:
                      - canceled
                      - failed
                      - neutral
                      - succeeded
                      - skipped
                      - stale
              blocking:
                allOf:
                  - type: boolean
              output:
                allOf:
                  - properties:
                      metrics:
                        properties:
                          FCP:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          LCP:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          CLS:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          TBT:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          virtualExperienceScore:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                        required:
                          - FCP
                          - LCP
                          - CLS
                          - TBT
                        type: object
                    type: object
              detailsUrl:
                allOf:
                  - type: string
              integrationId:
                allOf:
                  - type: string
              deploymentId:
                allOf:
                  - type: string
              externalId:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
              startedAt:
                allOf:
                  - type: number
              completedAt:
                allOf:
                  - type: number
              rerequestable:
                allOf:
                  - type: boolean
            requiredProperties:
              - id
              - name
              - status
              - blocking
              - integrationId
              - deploymentId
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: <string>
              name: <string>
              path: <string>
              status: registered
              conclusion: canceled
              blocking: true
              output:
                metrics:
                  FCP:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  LCP:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  CLS:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  TBT:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  virtualExperienceScore:
                    value: 123
                    previousValue: 123
                    source: web-vitals
              detailsUrl: <string>
              integrationId: <string>
              deploymentId: <string>
              externalId: <string>
              createdAt: 123
              updatedAt: 123
              startedAt: 123
              completedAt: 123
              rerequestable: true
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
            description: >-
              You do not have permission to access this resource.

              The provided token is not from an OAuth2 Client that created the
              Check
        examples: {}
        description: |-
          You do not have permission to access this resource.
          The provided token is not from an OAuth2 Client that created the Check
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              Check was not found
              The deployment was not found
        examples: {}
        description: |-
          Check was not found
          The deployment was not found
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Rerequest a check"

last_updated: "2025-11-07T00:37:08.555Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/checks/rerequest-a-check"
--------------------------------------------------------------------------------

# Rerequest a check

> Rerequest a selected check that has failed.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/deployments/{deploymentId}/checks/{checkId}/rerequest
paths:
  path: /v1/deployments/{deploymentId}/checks/{checkId}/rerequest
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
        deploymentId:
          schema:
            - type: string
              required: true
              description: The deployment to rerun the check for.
              example: dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6
        checkId:
          schema:
            - type: string
              required: true
              description: The check to rerun
              example: check_2qn7PZrx89yxY34vEZPD31Y9XVj6
      query:
        autoUpdate:
          schema:
            - type: boolean
              required: false
              description: Mark the check as running
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
      - label: rerequestCheck
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Checks.RerequestCheck(ctx, \"dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6\", \"check_2qn7PZrx89yxY34vEZPD31Y9XVj6\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: rerequestCheck
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.checks.rerequestCheck({
              deploymentId: "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6",
              checkId: "check_2qn7PZrx89yxY34vEZPD31Y9XVj6",
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
        examples:
          example:
            value: {}
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
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              The deployment was not found
              Check was not found
        examples: {}
        description: |-
          The deployment was not found
          Check was not found
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Retrieve a list of all checks"

last_updated: "2025-11-07T00:37:08.583Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/checks/retrieve-a-list-of-all-checks"
--------------------------------------------------------------------------------

# Retrieve a list of all checks

> List all of the checks created for a deployment.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/deployments/{deploymentId}/checks
paths:
  path: /v1/deployments/{deploymentId}/checks
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
        deploymentId:
          schema:
            - type: string
              required: true
              description: The deployment to get all checks for
              example: dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6
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
      - label: getAllChecks
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Checks.GetAllChecks(ctx, \"dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getAllChecks
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.checks.getAllChecks({
              deploymentId: "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6",
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
              checks:
                allOf:
                  - items:
                      properties:
                        completedAt:
                          type: number
                        conclusion:
                          type: string
                          enum:
                            - canceled
                            - failed
                            - neutral
                            - succeeded
                            - skipped
                            - stale
                        createdAt:
                          type: number
                        detailsUrl:
                          type: string
                        id:
                          type: string
                        integrationId:
                          type: string
                        name:
                          type: string
                        output:
                          properties:
                            metrics:
                              properties:
                                FCP:
                                  properties:
                                    value:
                                      nullable: true
                                      type: number
                                    previousValue:
                                      type: number
                                    source:
                                      type: string
                                      enum:
                                        - web-vitals
                                  required:
                                    - value
                                    - source
                                  type: object
                                LCP:
                                  properties:
                                    value:
                                      nullable: true
                                      type: number
                                    previousValue:
                                      type: number
                                    source:
                                      type: string
                                      enum:
                                        - web-vitals
                                  required:
                                    - value
                                    - source
                                  type: object
                                CLS:
                                  properties:
                                    value:
                                      nullable: true
                                      type: number
                                    previousValue:
                                      type: number
                                    source:
                                      type: string
                                      enum:
                                        - web-vitals
                                  required:
                                    - value
                                    - source
                                  type: object
                                TBT:
                                  properties:
                                    value:
                                      nullable: true
                                      type: number
                                    previousValue:
                                      type: number
                                    source:
                                      type: string
                                      enum:
                                        - web-vitals
                                  required:
                                    - value
                                    - source
                                  type: object
                                virtualExperienceScore:
                                  properties:
                                    value:
                                      nullable: true
                                      type: number
                                    previousValue:
                                      type: number
                                    source:
                                      type: string
                                      enum:
                                        - web-vitals
                                  required:
                                    - value
                                    - source
                                  type: object
                              required:
                                - FCP
                                - LCP
                                - CLS
                                - TBT
                              type: object
                          type: object
                        path:
                          type: string
                        rerequestable:
                          type: boolean
                        blocking:
                          type: boolean
                        startedAt:
                          type: number
                        status:
                          type: string
                          enum:
                            - registered
                            - running
                            - completed
                        updatedAt:
                          type: number
                      required:
                        - createdAt
                        - id
                        - integrationId
                        - name
                        - rerequestable
                        - blocking
                        - status
                        - updatedAt
                      type: object
                    type: array
            requiredProperties:
              - checks
        examples:
          example:
            value:
              checks:
                - completedAt: 123
                  conclusion: canceled
                  createdAt: 123
                  detailsUrl: <string>
                  id: <string>
                  integrationId: <string>
                  name: <string>
                  output:
                    metrics:
                      FCP:
                        value: 123
                        previousValue: 123
                        source: web-vitals
                      LCP:
                        value: 123
                        previousValue: 123
                        source: web-vitals
                      CLS:
                        value: 123
                        previousValue: 123
                        source: web-vitals
                      TBT:
                        value: 123
                        previousValue: 123
                        source: web-vitals
                      virtualExperienceScore:
                        value: 123
                        previousValue: 123
                        source: web-vitals
                  path: <string>
                  rerequestable: true
                  blocking: true
                  startedAt: 123
                  status: registered
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
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The deployment was not found
        examples: {}
        description: The deployment was not found
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update a check"

last_updated: "2025-11-07T00:37:08.795Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/checks/update-a-check"
--------------------------------------------------------------------------------

# Update a check

> Update an existing check. This endpoint must be called with an OAuth2 or it will produce a 400 error.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/deployments/{deploymentId}/checks/{checkId}
paths:
  path: /v1/deployments/{deploymentId}/checks/{checkId}
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
        deploymentId:
          schema:
            - type: string
              required: true
              description: The deployment to update the check for.
              example: dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6
        checkId:
          schema:
            - type: string
              required: true
              description: The check being updated
              example: check_2qn7PZrx89yxY34vEZPD31Y9XVj6
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
                  - description: The name of the check being created
                    maxLength: 100
                    example: Performance Check
                    type: string
              path:
                allOf:
                  - description: Path of the page that is being checked
                    type: string
                    maxLength: 255
                    example: /
              status:
                allOf:
                  - description: The current status of the check
                    enum:
                      - running
                      - completed
              conclusion:
                allOf:
                  - description: The result of the check being run
                    enum:
                      - canceled
                      - failed
                      - neutral
                      - succeeded
                      - skipped
              detailsUrl:
                allOf:
                  - description: >-
                      A URL a user may visit to see more information about the
                      check
                    type: string
                    example: https://example.com/check/run/1234abc
              output:
                allOf:
                  - description: The results of the check Run
                    type: object
                    properties:
                      metrics:
                        type: object
                        description: Metrics about the page
                        required:
                          - FCP
                          - LCP
                          - CLS
                          - TBT
                        additionalProperties: false
                        properties:
                          FCP:
                            type: object
                            required:
                              - value
                              - source
                            properties:
                              value:
                                type: number
                                example: 1200
                                description: First Contentful Paint value
                                nullable: true
                              previousValue:
                                type: number
                                example: 900
                                description: >-
                                  Previous First Contentful Paint value to
                                  display a delta
                              source:
                                type: string
                                enum:
                                  - web-vitals
                          LCP:
                            type: object
                            required:
                              - value
                              - source
                            properties:
                              value:
                                type: number
                                example: 1200
                                description: Largest Contentful Paint value
                                nullable: true
                              previousValue:
                                type: number
                                example: 1000
                                description: >-
                                  Previous Largest Contentful Paint value to
                                  display a delta
                              source:
                                type: string
                                enum:
                                  - web-vitals
                          CLS:
                            type: object
                            required:
                              - value
                              - source
                            properties:
                              value:
                                type: number
                                example: 4
                                description: Cumulative Layout Shift value
                                nullable: true
                              previousValue:
                                type: number
                                example: 2
                                description: >-
                                  Previous Cumulative Layout Shift value to
                                  display a delta
                              source:
                                type: string
                                enum:
                                  - web-vitals
                          TBT:
                            type: object
                            required:
                              - value
                              - source
                            properties:
                              value:
                                type: number
                                example: 3000
                                description: Total Blocking Time value
                                nullable: true
                              previousValue:
                                type: number
                                example: 3500
                                description: >-
                                  Previous Total Blocking Time value to display
                                  a delta
                              source:
                                enum:
                                  - web-vitals
                          virtualExperienceScore:
                            type: object
                            required:
                              - value
                              - source
                            properties:
                              value:
                                type: integer
                                maximum: 100
                                minimum: 0
                                example: 30
                                description: >-
                                  The calculated Virtual Experience Score value,
                                  between 0 and 100
                                nullable: true
                              previousValue:
                                type: integer
                                maximum: 100
                                minimum: 0
                                example: 35
                                description: >-
                                  A previous Virtual Experience Score value to
                                  display a delta, between 0 and 100
                              source:
                                enum:
                                  - web-vitals
              externalId:
                allOf:
                  - description: An identifier that can be used as an external reference
                    type: string
                    example: 1234abc
            required: true
        examples:
          example:
            value:
              name: Performance Check
              path: /
              status: running
              conclusion: canceled
              detailsUrl: https://example.com/check/run/1234abc
              output:
                metrics:
                  FCP:
                    value: 1200
                    previousValue: 900
                    source: web-vitals
                  LCP:
                    value: 1200
                    previousValue: 1000
                    source: web-vitals
                  CLS:
                    value: 4
                    previousValue: 2
                    source: web-vitals
                  TBT:
                    value: 3000
                    previousValue: 3500
                    source: web-vitals
                  virtualExperienceScore:
                    value: 30
                    previousValue: 35
                    source: web-vitals
              externalId: 1234abc
    codeSamples:
      - label: updateCheck
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Checks.UpdateCheck(ctx, operations.UpdateCheckRequest{\n        DeploymentID: \"dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6\",\n        CheckID: \"check_2qn7PZrx89yxY34vEZPD31Y9XVj6\",\n        RequestBody: &operations.UpdateCheckRequestBody{\n            Name: vercel.String(\"Performance Check\"),\n            Path: vercel.String(\"/\"),\n            DetailsURL: vercel.String(\"https://example.com/check/run/1234abc\"),\n            Output: &operations.Output{\n                Metrics: &operations.Metrics{\n                    Fcp: operations.Fcp{\n                        Value: vercel.Float64(1200),\n                        PreviousValue: vercel.Float64(900),\n                        Source: operations.UpdateCheckSourceWebVitals,\n                    },\n                    Lcp: operations.Lcp{\n                        Value: vercel.Float64(1200),\n                        PreviousValue: vercel.Float64(1000),\n                        Source: operations.UpdateCheckChecksSourceWebVitals,\n                    },\n                    Cls: operations.Cls{\n                        Value: vercel.Float64(4),\n                        PreviousValue: vercel.Float64(2),\n                        Source: operations.UpdateCheckChecksRequestSourceWebVitals,\n                    },\n                    Tbt: operations.Tbt{\n                        Value: vercel.Float64(3000),\n                        PreviousValue: vercel.Float64(3500),\n                        Source: operations.UpdateCheckChecksRequestRequestBodySourceWebVitals,\n                    },\n                    VirtualExperienceScore: &operations.VirtualExperienceScore{\n                        Value: vercel.Int64(30),\n                        PreviousValue: vercel.Int64(35),\n                        Source: operations.UpdateCheckChecksRequestRequestBodyOutputSourceWebVitals,\n                    },\n                },\n            },\n            ExternalID: vercel.String(\"1234abc\"),\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateCheck
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.checks.updateCheck({
              deploymentId: "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6",
              checkId: "check_2qn7PZrx89yxY34vEZPD31Y9XVj6",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "Performance Check",
                path: "/",
                detailsUrl: "https://example.com/check/run/1234abc",
                output: {
                  metrics: {
                    fcp: {
                      value: 1200,
                      previousValue: 900,
                      source: "web-vitals",
                    },
                    lcp: {
                      value: 1200,
                      previousValue: 1000,
                      source: "web-vitals",
                    },
                    cls: {
                      value: 4,
                      previousValue: 2,
                      source: "web-vitals",
                    },
                    tbt: {
                      value: 3000,
                      previousValue: 3500,
                      source: "web-vitals",
                    },
                    virtualExperienceScore: {
                      value: 30,
                      previousValue: 35,
                      source: "web-vitals",
                    },
                  },
                },
                externalId: "1234abc",
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
              name:
                allOf:
                  - type: string
              path:
                allOf:
                  - type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - registered
                      - running
                      - completed
              conclusion:
                allOf:
                  - type: string
                    enum:
                      - canceled
                      - failed
                      - neutral
                      - succeeded
                      - skipped
                      - stale
              blocking:
                allOf:
                  - type: boolean
              output:
                allOf:
                  - properties:
                      metrics:
                        properties:
                          FCP:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          LCP:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          CLS:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          TBT:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                          virtualExperienceScore:
                            properties:
                              value:
                                nullable: true
                                type: number
                              previousValue:
                                type: number
                              source:
                                type: string
                                enum:
                                  - web-vitals
                            required:
                              - value
                              - source
                            type: object
                        required:
                          - FCP
                          - LCP
                          - CLS
                          - TBT
                        type: object
                    type: object
              detailsUrl:
                allOf:
                  - type: string
              integrationId:
                allOf:
                  - type: string
              deploymentId:
                allOf:
                  - type: string
              externalId:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
              startedAt:
                allOf:
                  - type: number
              completedAt:
                allOf:
                  - type: number
              rerequestable:
                allOf:
                  - type: boolean
            requiredProperties:
              - id
              - name
              - status
              - blocking
              - integrationId
              - deploymentId
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: <string>
              name: <string>
              path: <string>
              status: registered
              conclusion: canceled
              blocking: true
              output:
                metrics:
                  FCP:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  LCP:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  CLS:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  TBT:
                    value: 123
                    previousValue: 123
                    source: web-vitals
                  virtualExperienceScore:
                    value: 123
                    previousValue: 123
                    source: web-vitals
              detailsUrl: <string>
              integrationId: <string>
              deploymentId: <string>
              externalId: <string>
              createdAt: 123
              updatedAt: 123
              startedAt: 123
              completedAt: 123
              rerequestable: true
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
              The provided token is not from an OAuth2 Client
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
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
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              Check was not found
              The deployment was not found
        examples: {}
        description: |-
          Check was not found
          The deployment was not found
    '413':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The output provided is too large
        examples: {}
        description: The output provided is too large
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Configures Static IPs for a project"

last_updated: "2025-11-07T00:37:08.591Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/connect/configures-static-ips-for-a-project"
--------------------------------------------------------------------------------

# Configures Static IPs for a project

> Allows configuring Static IPs for a project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/projects/{idOrName}/shared-connect-links
paths:
  path: /v1/projects/{idOrName}/shared-connect-links
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
              builds:
                allOf:
                  - &ref_0
                    type: boolean
                    description: Whether to use Static IPs for builds.
              regions:
                allOf:
                  - &ref_1
                    type: array
                    items:
                      type: string
                      maxLength: 4
                      description: The region in which to enable Static IPs.
                      example: iad1
                    minItems: 0
                    maxItems: 3
                    uniqueItems: true
            requiredProperties:
              - builds
          - type: object
            properties:
              builds:
                allOf:
                  - *ref_0
              regions:
                allOf:
                  - *ref_1
            requiredProperties:
              - regions
        examples:
          example:
            value:
              builds: true
              regions:
                - iad1
    codeSamples:
      - label: updateStaticIps
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.connect.updateStaticIps({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                regions: [
                  "iad1",
                ],
              },
            });

            console.log(result);
          }

          run();
      - label: updateStaticIps
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.staticIps.updateStaticIps({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                regions: [
                  "iad1",
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
          - type: array
            items:
              allOf:
                - properties:
                    envId:
                      oneOf:
                        - type: string
                        - type: string
                          enum:
                            - preview
                            - production
                    connectConfigurationId:
                      type: string
                    dc:
                      type: string
                    passive:
                      type: boolean
                    buildsEnabled:
                      type: boolean
                    aws:
                      properties:
                        subnetIds:
                          items:
                            type: string
                          type: array
                        securityGroupId:
                          type: string
                      required:
                        - subnetIds
                        - securityGroupId
                      type: object
                    createdAt:
                      type: number
                    updatedAt:
                      type: number
                  required:
                    - envId
                    - connectConfigurationId
                    - passive
                    - buildsEnabled
                    - createdAt
                    - updatedAt
                  type: object
        examples:
          example:
            value:
              - envId: <string>
                connectConfigurationId: <string>
                dc: <string>
                passive: true
                buildsEnabled: true
                aws:
                  subnetIds:
                    - <string>
                  securityGroupId: <string>
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
    '402': {}
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
title: "Cancel a deployment"

last_updated: "2025-11-07T00:37:08.749Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/deployments/cancel-a-deployment"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./17-monitoring-quickstart.md) | [Index](./index.md) | [Next →](./19-cancel-a-deployment.md)
