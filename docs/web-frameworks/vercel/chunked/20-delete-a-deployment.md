**Navigation:** [← Previous](./19-cancel-a-deployment.md) | [Index](./index.md) | [Next →](./21-create-a-dns-record.md)

---

# Delete a Deployment

> This API allows you to delete a deployment, either by supplying its `id` in the URL or the `url` of the deployment as a query parameter. You can obtain the ID, for example, by listing all deployments.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v13/deployments/{id}
paths:
  path: /v13/deployments/{id}
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
              description: The ID of the deployment to be deleted
              example: dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd
      query:
        url:
          schema:
            - type: string
              required: false
              description: >-
                A Deployment or Alias URL. In case it is passed, the ID will be
                ignored
              example: https://files-orcin-xi.vercel.app/
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
      - label: deleteDeployment
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Deployments.DeleteDeployment(ctx, \"dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd\", vercel.String(\"https://files-orcin-xi.vercel.app/\"), nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: deleteDeployment
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.deployments.deleteDeployment({
              id: "dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd",
              url: "https://files-orcin-xi.vercel.app/",
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
              uid:
                allOf:
                  - type: string
                    description: The removed deployment ID.
                    example: dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd
              state:
                allOf:
                  - type: string
                    enum:
                      - DELETED
                    description: A constant with the final state of the deployment.
            requiredProperties:
              - uid
              - state
        examples:
          example:
            value:
              uid: dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd
              state: DELETED
        description: The deployment was successfully deleted
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
title: "Get a deployment by ID or URL"

last_updated: "2025-11-07T00:37:08.634Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/deployments/get-a-deployment-by-id-or-url"
--------------------------------------------------------------------------------

# Get a deployment by ID or URL

> Retrieves information for a deployment either by supplying its ID (`id` property) or Hostname (`url` property). Additional details will be included when the authenticated user or team is an owner of the deployment.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v13/deployments/{idOrUrl}
paths:
  path: /v13/deployments/{idOrUrl}
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
        idOrUrl:
          schema:
            - type: string
              required: true
              description: The unique identifier or hostname of the deployment.
              example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
      query:
        withGitRepoInfo:
          schema:
            - type: string
              required: false
              description: Whether to add in gitRepo information.
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
    body: {}
    codeSamples:
      - label: getDeployment
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Deployments.GetDeployment(ctx, \"dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ\", vercel.String(\"true\"), nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: getDeployment
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.deployments.getDeployment({
              idOrUrl: "dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ",
              withGitRepoInfo: "true",
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
              aliasAssignedAt:
                allOf:
                  - nullable: true
                    oneOf:
                      - type: number
                      - type: boolean
              alwaysRefuseToBuild:
                allOf:
                  - type: boolean
              build:
                allOf:
                  - properties:
                      env:
                        items:
                          type: string
                        type: array
                    required:
                      - env
                    type: object
              buildArtifactUrls:
                allOf:
                  - items:
                      type: string
                    type: array
              builds:
                allOf:
                  - items:
                      properties:
                        use:
                          type: string
                        src:
                          type: string
                        config:
                          additionalProperties: true
                          type: object
                      required:
                        - use
                      type: object
                    type: array
              env:
                allOf:
                  - items:
                      type: string
                    type: array
              inspectorUrl:
                allOf:
                  - nullable: true
                    type: string
              isInConcurrentBuildsQueue:
                allOf:
                  - type: boolean
              isInSystemBuildsQueue:
                allOf:
                  - type: boolean
              projectSettings:
                allOf:
                  - properties:
                      buildCommand:
                        nullable: true
                        type: string
                      devCommand:
                        nullable: true
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
                      commandForIgnoringBuildStep:
                        nullable: true
                        type: string
                      installCommand:
                        nullable: true
                        type: string
                      outputDirectory:
                        nullable: true
                        type: string
                      speedInsights:
                        properties:
                          id:
                            type: string
                          enabledAt:
                            type: number
                          disabledAt:
                            type: number
                          canceledAt:
                            type: number
                          hasData:
                            type: boolean
                          paidAt:
                            type: number
                        required:
                          - id
                        type: object
                      webAnalytics:
                        properties:
                          id:
                            type: string
                          disabledAt:
                            type: number
                          canceledAt:
                            type: number
                          enabledAt:
                            type: number
                          hasData:
                            type: boolean
                        required:
                          - id
                        type: object
                    type: object
              readyStateReason:
                allOf:
                  - type: string
              integrations:
                allOf:
                  - properties:
                      status:
                        type: string
                        enum:
                          - skipped
                          - pending
                          - ready
                          - error
                          - timeout
                      startedAt:
                        type: number
                      completedAt:
                        type: number
                      skippedAt:
                        type: number
                      skippedBy:
                        type: string
                    required:
                      - status
                      - startedAt
                    type: object
              images:
                allOf:
                  - properties:
                      sizes:
                        items:
                          type: number
                        type: array
                      qualities:
                        items:
                          type: number
                        type: array
                      domains:
                        items:
                          type: string
                        type: array
                      remotePatterns:
                        items:
                          properties:
                            protocol:
                              type: string
                              enum:
                                - http
                                - https
                              description: Must be `http` or `https`.
                            hostname:
                              type: string
                              description: >-
                                Can be literal or wildcard. Single `*` matches a
                                single subdomain. Double `**` matches any number
                                of subdomains.
                            port:
                              type: string
                              description: >-
                                Can be literal port such as `8080` or empty
                                string meaning no port.
                            pathname:
                              type: string
                              description: >-
                                Can be literal or wildcard. Single `*` matches a
                                single path segment. Double `**` matches any
                                number of path segments.
                            search:
                              type: string
                              description: >-
                                Can be literal query string such as `?v=1` or
                                empty string meaning no query string.
                          required:
                            - hostname
                          type: object
                        type: array
                      localPatterns:
                        items:
                          properties:
                            pathname:
                              type: string
                              description: >-
                                Can be literal or wildcard. Single `*` matches a
                                single path segment. Double `**` matches any
                                number of path segments.
                            search:
                              type: string
                              description: >-
                                Can be literal query string such as `?v=1` or
                                empty string meaning no query string.
                          type: object
                        type: array
                      minimumCacheTTL:
                        type: number
                      formats:
                        items:
                          type: string
                          enum:
                            - image/avif
                            - image/webp
                        type: array
                      dangerouslyAllowSVG:
                        type: boolean
                      contentSecurityPolicy:
                        type: string
                      contentDispositionType:
                        type: string
                        enum:
                          - inline
                          - attachment
                    type: object
              alias:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      A list of all the aliases (default aliases, staging
                      aliases and production aliases) that were assigned upon
                      deployment creation
                    example: []
              aliasAssigned:
                allOf:
                  - type: boolean
                    description: >-
                      A boolean that will be true when the aliases from the
                      alias property were assigned successfully
                    example: true
              bootedAt:
                allOf:
                  - type: number
              buildingAt:
                allOf:
                  - type: number
              buildContainerFinishedAt:
                allOf:
                  - type: number
                    description: >-
                      Since April 2025 it necessary for On-Demand Concurrency
                      Minutes calculation
              buildSkipped:
                allOf:
                  - type: boolean
              creator:
                allOf:
                  - properties:
                      uid:
                        type: string
                        description: The ID of the user that created the deployment
                        example: 96SnxkFiMyVKsK3pnoHfx3Hz
                      username:
                        type: string
                        description: The username of the user that created the deployment
                        example: john-doe
                      avatar:
                        type: string
                        description: The avatar of the user that created the deployment
                    required:
                      - uid
                    type: object
                    description: Information about the deployment creator
              initReadyAt:
                allOf:
                  - type: number
              isFirstBranchDeployment:
                allOf:
                  - type: boolean
              lambdas:
                allOf:
                  - items:
                      properties:
                        id:
                          type: string
                        createdAt:
                          type: number
                        readyState:
                          type: string
                          enum:
                            - BUILDING
                            - ERROR
                            - INITIALIZING
                            - READY
                        entrypoint:
                          nullable: true
                          type: string
                        readyStateAt:
                          type: number
                        output:
                          items:
                            properties:
                              path:
                                type: string
                              functionName:
                                type: string
                            required:
                              - path
                              - functionName
                            type: object
                          type: array
                      required:
                        - id
                        - output
                      type: object
                      description: >-
                        A partial representation of a Build used by the
                        deployment endpoint.
                    type: array
              public:
                allOf:
                  - type: boolean
                    description: >-
                      A boolean representing if the deployment is public or not.
                      By default this is `false`
                    example: false
              ready:
                allOf:
                  - type: number
              status:
                allOf:
                  - type: string
                    enum:
                      - QUEUED
                      - BUILDING
                      - ERROR
                      - INITIALIZING
                      - READY
                      - CANCELED
              team:
                allOf:
                  - properties:
                      id:
                        type: string
                      name:
                        type: string
                      slug:
                        type: string
                      avatar:
                        type: string
                    required:
                      - id
                      - name
                      - slug
                    type: object
                    description: The team that owns the deployment if any
              userAliases:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      An array of domains that were provided by the user when
                      creating the Deployment.
                    example:
                      - sub1.example.com
                      - sub2.example.com
              previewCommentsEnabled:
                allOf:
                  - type: boolean
                    description: >-
                      Whether or not preview comments are enabled for the
                      deployment
                    example: false
              ttyBuildLogs:
                allOf:
                  - type: boolean
              customEnvironment:
                allOf:
                  - oneOf:
                      - properties:
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
                              - production
                              - preview
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
                                    `true` if the domain is verified for use
                                    with the project. If `false` it will not be
                                    used as an alias on this project until the
                                    challenge in `verification` is completed.
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
                                      which must be completed to verify the
                                      domain for use on the project. After the
                                      challenge is complete `POST
                                      /projects/:idOrName/domains/:domain/verify`
                                      to verify the domain. Possible challenges:
                                      - If `verification.type = TXT` the
                                      `verification.domain` will be checked for
                                      a TXT record matching
                                      `verification.value`.
                                  type: array
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
                        description: >-
                          If the deployment was created using a Custom
                          Environment, then this property contains information
                          regarding the environment used.
                      - properties:
                          id:
                            type: string
                        required:
                          - id
                        type: object
                        description: >-
                          If the deployment was created using a Custom
                          Environment, then this property contains information
                          regarding the environment used.
              oomReport:
                allOf:
                  - type: string
                    enum:
                      - out-of-memory
              aliasWarning:
                allOf:
                  - nullable: true
                    properties:
                      code:
                        type: string
                      message:
                        type: string
                      link:
                        type: string
                      action:
                        type: string
                    required:
                      - code
                      - message
                    type: object
              id:
                allOf:
                  - type: string
                    description: A string holding the unique ID of the deployment
                    example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
              createdAt:
                allOf:
                  - type: number
                    description: >-
                      A number containing the date when the deployment was
                      created in milliseconds
                    example: 1540257589405
              readyState:
                allOf:
                  - type: string
                    enum:
                      - QUEUED
                      - BUILDING
                      - ERROR
                      - INITIALIZING
                      - READY
                      - CANCELED
                    description: >-
                      The state of the deployment depending on the process of
                      deploying, or if it is ready or in an error state
                    example: READY
              name:
                allOf:
                  - type: string
                    description: >-
                      The name of the project associated with the deployment at
                      the time that the deployment was created
                    example: my-project
              type:
                allOf:
                  - type: string
                    enum:
                      - LAMBDAS
              aliasError:
                allOf:
                  - nullable: true
                    properties:
                      code:
                        type: string
                      message:
                        type: string
                    required:
                      - code
                      - message
                    type: object
                    description: >-
                      An object that will contain a `code` and a `message` when
                      the aliasing fails, otherwise the value will be `null`
                    example: null
              aliasFinal:
                allOf:
                  - nullable: true
                    type: string
              autoAssignCustomDomains:
                allOf:
                  - type: boolean
                    description: applies to custom domains only, defaults to `true`
              automaticAliases:
                allOf:
                  - items:
                      type: string
                    type: array
              buildErrorAt:
                allOf:
                  - type: number
              checksState:
                allOf:
                  - type: string
                    enum:
                      - registered
                      - running
                      - completed
              checksConclusion:
                allOf:
                  - type: string
                    enum:
                      - succeeded
                      - failed
                      - skipped
                      - canceled
              deletedAt:
                allOf:
                  - nullable: true
                    type: number
                    description: >-
                      A number containing the date when the deployment was
                      deleted at milliseconds
                    example: 1540257589405
              defaultRoute:
                allOf:
                  - type: string
                    description: >-
                      Computed field that is only available for deployments with
                      a microfrontend configuration.
              canceledAt:
                allOf:
                  - type: number
              errorCode:
                allOf:
                  - type: string
              errorLink:
                allOf:
                  - type: string
              errorMessage:
                allOf:
                  - nullable: true
                    type: string
              errorStep:
                allOf:
                  - type: string
              passiveRegions:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      Since November 2023 this field defines a set of regions
                      that we will deploy the lambda to passively Lambdas will
                      be deployed to these regions but only invoked if all of
                      the primary `regions` are marked as out of service
              gitSource:
                allOf:
                  - oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - github
                          repoId:
                            oneOf:
                              - type: string
                              - type: number
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - repoId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github
                          org:
                            type: string
                          repo:
                            type: string
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - org
                          - repo
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github-custom-host
                          host:
                            type: string
                          repoId:
                            oneOf:
                              - type: string
                              - type: number
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - host
                          - repoId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github-custom-host
                          host:
                            type: string
                          org:
                            type: string
                          repo:
                            type: string
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - host
                          - org
                          - repo
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github-limited
                          repoId:
                            oneOf:
                              - type: string
                              - type: number
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - repoId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github-limited
                          org:
                            type: string
                          repo:
                            type: string
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - org
                          - repo
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - gitlab
                          projectId:
                            oneOf:
                              - type: string
                              - type: number
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - projectId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - bitbucket
                          workspaceUuid:
                            type: string
                          repoUuid:
                            type: string
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - repoUuid
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - bitbucket
                          owner:
                            type: string
                          slug:
                            type: string
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - owner
                          - slug
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - custom
                          ref:
                            type: string
                          sha:
                            type: string
                          gitUrl:
                            type: string
                        required:
                          - type
                          - ref
                          - sha
                          - gitUrl
                        type: object
                        description: >-
                          Allows custom git sources (local folder mounted to the
                          container) in test mode
                      - properties:
                          type:
                            type: string
                            enum:
                              - github
                          ref:
                            type: string
                          sha:
                            type: string
                          repoId:
                            type: number
                          org:
                            type: string
                          repo:
                            type: string
                        required:
                          - type
                          - ref
                          - sha
                          - repoId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github-custom-host
                          host:
                            type: string
                          ref:
                            type: string
                          sha:
                            type: string
                          repoId:
                            type: number
                          org:
                            type: string
                          repo:
                            type: string
                        required:
                          - type
                          - host
                          - ref
                          - sha
                          - repoId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github-limited
                          ref:
                            type: string
                          sha:
                            type: string
                          repoId:
                            type: number
                          org:
                            type: string
                          repo:
                            type: string
                        required:
                          - type
                          - ref
                          - sha
                          - repoId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - gitlab
                          ref:
                            type: string
                          sha:
                            type: string
                          projectId:
                            type: number
                        required:
                          - type
                          - ref
                          - sha
                          - projectId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - bitbucket
                          ref:
                            type: string
                          sha:
                            type: string
                          owner:
                            type: string
                          slug:
                            type: string
                          workspaceUuid:
                            type: string
                          repoUuid:
                            type: string
                        required:
                          - type
                          - ref
                          - sha
                          - workspaceUuid
                          - repoUuid
                        type: object
              meta:
                allOf:
                  - additionalProperties:
                      type: string
                    type: object
              originCacheRegion:
                allOf:
                  - type: string
              nodeVersion:
                allOf:
                  - type: string
                    enum:
                      - 22.x
                      - 20.x
                      - 18.x
                      - 16.x
                      - 14.x
                      - 12.x
                      - 10.x
                      - 8.10.x
                    description: >-
                      If set it overrides the `projectSettings.nodeVersion` for
                      this deployment.
              project:
                allOf:
                  - properties:
                      id:
                        type: string
                      name:
                        type: string
                      framework:
                        nullable: true
                        type: string
                    required:
                      - id
                      - name
                    type: object
                    description: >-
                      The public project information associated with the
                      deployment.
              readySubstate:
                allOf:
                  - type: string
                    enum:
                      - STAGED
                      - ROLLING
                      - PROMOTED
                    description: >-
                      Substate of deployment when readyState is 'READY' Tracks
                      whether or not deployment has seen production traffic: -
                      STAGED: never seen production traffic - ROLLING: in the
                      process of having production traffic gradually
                      transitioned. - PROMOTED: has seen production traffic
              regions:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: The regions the deployment exists in
                    example:
                      - sfo1
              softDeletedByRetention:
                allOf:
                  - type: boolean
                    description: >-
                      flag to indicate if the deployment was deleted by
                      retention policy
                    example: 'true'
              source:
                allOf:
                  - type: string
                    enum:
                      - api-trigger-git-deploy
                      - cli
                      - clone/repo
                      - git
                      - import
                      - import/repo
                      - redeploy
                      - v0-web
                    description: Where was the deployment created from
                    example: cli
              target:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - staging
                      - production
                    description: >-
                      If defined, either `staging` if a staging alias in the
                      format `<project>.<team>.now.sh` was assigned upon
                      creation, or `production` if the aliases from `alias` were
                      assigned. `null` value indicates the "preview" deployment.
                    example: null
              undeletedAt:
                allOf:
                  - type: number
                    description: >-
                      A number containing the date when the deployment was
                      undeleted at milliseconds
                    example: 1540257589405
              url:
                allOf:
                  - type: string
                    description: A string with the unique URL of the deployment
                    example: my-instant-deployment-3ij3cxz9qr.now.sh
              version:
                allOf:
                  - type: number
                    enum:
                      - 2
                    description: >-
                      The platform version that was used to create the
                      deployment.
                    example: 2
              oidcTokenClaims:
                allOf:
                  - properties:
                      iss:
                        type: string
                      sub:
                        type: string
                      scope:
                        type: string
                      aud:
                        type: string
                      owner:
                        type: string
                      owner_id:
                        type: string
                      project:
                        type: string
                      project_id:
                        type: string
                      environment:
                        type: string
                    required:
                      - iss
                      - sub
                      - scope
                      - aud
                      - owner
                      - owner_id
                      - project
                      - project_id
                      - environment
                    type: object
              projectId:
                allOf:
                  - type: string
              plan:
                allOf:
                  - type: string
                    enum:
                      - pro
                      - enterprise
                      - hobby
              connectBuildsEnabled:
                allOf:
                  - type: boolean
              connectConfigurationId:
                allOf:
                  - type: string
              createdIn:
                allOf:
                  - type: string
              crons:
                allOf:
                  - items:
                      properties:
                        schedule:
                          type: string
                        path:
                          type: string
                      required:
                        - schedule
                        - path
                      type: object
                    type: array
              functions:
                allOf:
                  - nullable: true
                    additionalProperties:
                      properties:
                        architecture:
                          type: string
                          enum:
                            - x86_64
                            - arm64
                        memory:
                          type: number
                        maxDuration:
                          type: number
                        runtime:
                          type: string
                        includeFiles:
                          type: string
                        excludeFiles:
                          type: string
                        experimentalTriggers:
                          items:
                            properties:
                              type:
                                type: string
                                enum:
                                  - queue/v1beta
                                description: Event type - must be "queue/v1beta" (REQUIRED)
                              topic:
                                type: string
                                description: >-
                                  Name of the queue topic to consume from
                                  (REQUIRED)
                              consumer:
                                type: string
                                description: >-
                                  Name of the consumer group for this trigger
                                  (REQUIRED)
                              maxDeliveries:
                                type: number
                                description: >-
                                  Maximum number of delivery attempts for
                                  message processing (OPTIONAL) This represents
                                  the total number of times a message can be
                                  delivered, not the number of retries. Must be
                                  at least 1 if specified. Behavior when not
                                  specified depends on the server's default
                                  configuration.
                              retryAfterSeconds:
                                type: number
                                description: >-
                                  Delay in seconds before retrying failed
                                  executions (OPTIONAL) Behavior when not
                                  specified depends on the server's default
                                  configuration.
                              initialDelaySeconds:
                                type: number
                                description: >-
                                  Initial delay in seconds before first
                                  execution attempt (OPTIONAL) Must be 0 or
                                  greater. Use 0 for no initial delay. Behavior
                                  when not specified depends on the server's
                                  default configuration.
                            required:
                              - type
                              - topic
                              - consumer
                            type: object
                            description: >-
                              Queue trigger event for Vercel's queue system.
                              Handles "queue/v1beta" events with queue-specific
                              configuration.
                          type: array
                        supportsCancellation:
                          type: boolean
                      type: object
                    type: object
              monorepoManager:
                allOf:
                  - nullable: true
                    type: string
              ownerId:
                allOf:
                  - type: string
              passiveConnectConfigurationId:
                allOf:
                  - type: string
                    description: >-
                      Since November 2023 this field defines a Secure Compute
                      network that will only be used to deploy passive lambdas
                      to (as in passiveRegions)
              routes:
                allOf:
                  - nullable: true
                    items:
                      oneOf:
                        - properties:
                            src:
                              type: string
                            dest:
                              type: string
                            headers:
                              additionalProperties:
                                type: string
                              type: object
                            methods:
                              items:
                                type: string
                              type: array
                            continue:
                              type: boolean
                            override:
                              type: boolean
                            caseSensitive:
                              type: boolean
                            check:
                              type: boolean
                            important:
                              type: boolean
                            status:
                              type: number
                            has:
                              items:
                                oneOf:
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - host
                                      value:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              eq:
                                                oneOf:
                                                  - type: string
                                                  - type: number
                                              neq:
                                                type: string
                                              inc:
                                                items:
                                                  type: string
                                                type: array
                                              ninc:
                                                items:
                                                  type: string
                                                type: array
                                              pre:
                                                type: string
                                              suf:
                                                type: string
                                              re:
                                                type: string
                                              gt:
                                                type: number
                                              gte:
                                                type: number
                                              lt:
                                                type: number
                                              lte:
                                                type: number
                                            type: object
                                    required:
                                      - type
                                      - value
                                    type: object
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - header
                                          - cookie
                                          - query
                                      key:
                                        type: string
                                      value:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              eq:
                                                oneOf:
                                                  - type: string
                                                  - type: number
                                              neq:
                                                type: string
                                              inc:
                                                items:
                                                  type: string
                                                type: array
                                              ninc:
                                                items:
                                                  type: string
                                                type: array
                                              pre:
                                                type: string
                                              suf:
                                                type: string
                                              re:
                                                type: string
                                              gt:
                                                type: number
                                              gte:
                                                type: number
                                              lt:
                                                type: number
                                              lte:
                                                type: number
                                            type: object
                                    required:
                                      - type
                                      - key
                                    type: object
                              type: array
                            missing:
                              items:
                                oneOf:
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - host
                                      value:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              eq:
                                                oneOf:
                                                  - type: string
                                                  - type: number
                                              neq:
                                                type: string
                                              inc:
                                                items:
                                                  type: string
                                                type: array
                                              ninc:
                                                items:
                                                  type: string
                                                type: array
                                              pre:
                                                type: string
                                              suf:
                                                type: string
                                              re:
                                                type: string
                                              gt:
                                                type: number
                                              gte:
                                                type: number
                                              lt:
                                                type: number
                                              lte:
                                                type: number
                                            type: object
                                    required:
                                      - type
                                      - value
                                    type: object
                                  - properties:
                                      type:
                                        type: string
                                        enum:
                                          - header
                                          - cookie
                                          - query
                                      key:
                                        type: string
                                      value:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              eq:
                                                oneOf:
                                                  - type: string
                                                  - type: number
                                              neq:
                                                type: string
                                              inc:
                                                items:
                                                  type: string
                                                type: array
                                              ninc:
                                                items:
                                                  type: string
                                                type: array
                                              pre:
                                                type: string
                                              suf:
                                                type: string
                                              re:
                                                type: string
                                              gt:
                                                type: number
                                              gte:
                                                type: number
                                              lt:
                                                type: number
                                              lte:
                                                type: number
                                            type: object
                                    required:
                                      - type
                                      - key
                                    type: object
                              type: array
                            mitigate:
                              properties:
                                action:
                                  type: string
                                  enum:
                                    - challenge
                                    - deny
                              required:
                                - action
                              type: object
                            transforms:
                              items:
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - request.headers
                                      - request.query
                                      - response.headers
                                  op:
                                    type: string
                                    enum:
                                      - append
                                      - set
                                      - delete
                                  target:
                                    properties:
                                      key:
                                        oneOf:
                                          - type: string
                                          - properties:
                                              eq:
                                                oneOf:
                                                  - type: string
                                                  - type: number
                                              neq:
                                                type: string
                                              inc:
                                                items:
                                                  type: string
                                                type: array
                                              ninc:
                                                items:
                                                  type: string
                                                type: array
                                              pre:
                                                type: string
                                              suf:
                                                type: string
                                              gt:
                                                type: number
                                              gte:
                                                type: number
                                              lt:
                                                type: number
                                              lte:
                                                type: number
                                            type: object
                                    required:
                                      - key
                                    type: object
                                  args:
                                    oneOf:
                                      - type: string
                                      - items:
                                          type: string
                                        type: array
                                required:
                                  - type
                                  - op
                                  - target
                                type: object
                              type: array
                            locale:
                              properties:
                                redirect:
                                  additionalProperties:
                                    type: string
                                  type: object
                                cookie:
                                  type: string
                              type: object
                            middlewarePath:
                              type: string
                              description: >-
                                A middleware key within the `output` key under
                                the build result. Overrides a `middleware`
                                definition.
                            middlewareRawSrc:
                              items:
                                type: string
                              type: array
                              description: The original middleware matchers.
                            middleware:
                              type: number
                              description: >-
                                A middleware index in the `middleware` key under
                                the build result
                          required:
                            - src
                          type: object
                        - properties:
                            handle:
                              type: string
                              enum:
                                - error
                                - filesystem
                                - hit
                                - miss
                                - rewrite
                                - resource
                            src:
                              type: string
                            dest:
                              type: string
                            status:
                              type: number
                          required:
                            - handle
                          type: object
                        - properties:
                            src:
                              type: string
                            continue:
                              type: boolean
                            middleware:
                              type: number
                              enum:
                                - 0
                          required:
                            - src
                            - continue
                            - middleware
                          type: object
                    type: array
              gitRepo:
                allOf:
                  - nullable: true
                    oneOf:
                      - properties:
                          namespace:
                            type: string
                          projectId:
                            type: number
                          type:
                            type: string
                            enum:
                              - gitlab
                          url:
                            type: string
                          path:
                            type: string
                          defaultBranch:
                            type: string
                          name:
                            type: string
                          private:
                            type: boolean
                          ownerType:
                            type: string
                            enum:
                              - team
                              - user
                        required:
                          - namespace
                          - projectId
                          - type
                          - url
                          - path
                          - defaultBranch
                          - name
                          - private
                          - ownerType
                        type: object
                      - properties:
                          org:
                            type: string
                          repo:
                            type: string
                          repoId:
                            type: number
                          type:
                            type: string
                            enum:
                              - github
                          repoOwnerId:
                            type: number
                          path:
                            type: string
                          defaultBranch:
                            type: string
                          name:
                            type: string
                          private:
                            type: boolean
                          ownerType:
                            type: string
                            enum:
                              - team
                              - user
                        required:
                          - org
                          - repo
                          - repoId
                          - type
                          - repoOwnerId
                          - path
                          - defaultBranch
                          - name
                          - private
                          - ownerType
                        type: object
                      - properties:
                          owner:
                            type: string
                          repoUuid:
                            type: string
                          slug:
                            type: string
                          type:
                            type: string
                            enum:
                              - bitbucket
                          workspaceUuid:
                            type: string
                          path:
                            type: string
                          defaultBranch:
                            type: string
                          name:
                            type: string
                          private:
                            type: boolean
                          ownerType:
                            type: string
                            enum:
                              - team
                              - user
                        required:
                          - owner
                          - repoUuid
                          - slug
                          - type
                          - workspaceUuid
                          - path
                          - defaultBranch
                          - name
                          - private
                          - ownerType
                        type: object
              flags:
                allOf:
                  - oneOf:
                      - properties:
                          definitions:
                            additionalProperties:
                              properties:
                                options:
                                  items:
                                    properties:
                                      value:
                                        $ref: '#/components/schemas/FlagJSONValue'
                                      label:
                                        type: string
                                    required:
                                      - value
                                    type: object
                                  type: array
                                url:
                                  type: string
                                description:
                                  type: string
                              type: object
                            type: object
                        required:
                          - definitions
                        type: object
                        description: >-
                          Flags defined in the Build Output API, used by this
                          deployment. Primarily used by the Toolbar to know
                          about the used flags.
                      - items:
                          type: object
                          description: >-
                            Flags defined in the Build Output API, used by this
                            deployment. Primarily used by the Toolbar to know
                            about the used flags.
                        type: array
                        description: >-
                          Flags defined in the Build Output API, used by this
                          deployment. Primarily used by the Toolbar to know
                          about the used flags.
              microfrontends:
                allOf:
                  - oneOf:
                      - properties:
                          isDefaultApp:
                            type: boolean
                          defaultAppProjectName:
                            type: string
                            description: >-
                              The project name of the default app of this
                              deployment's microfrontends group.
                          defaultRoute:
                            type: string
                            description: >-
                              A path that is used to take screenshots and as the
                              default path in preview links when a domain for
                              this microfrontend is shown in the UI.
                          groupIds:
                            items:
                              oneOf:
                                - type: string
                                - type: string
                            maxItems: 2
                            minItems: 2
                            type: array
                            description: >-
                              The group of microfrontends that this project
                              belongs to. Each microfrontend project must belong
                              to a microfrontends group that is the set of
                              microfrontends that are used together.
                          microfrontendsAlias2Enabled:
                            type: boolean
                            description: >-
                              Whether the MicrofrontendsAlias2 team flag should
                              be considered enabled for this deployment or not.
                        required:
                          - defaultAppProjectName
                          - groupIds
                        type: object
                      - properties:
                          isDefaultApp:
                            type: boolean
                          applications:
                            additionalProperties:
                              properties:
                                isDefaultApp:
                                  type: boolean
                                productionHost:
                                  type: string
                                  description: >-
                                    This is the production alias, it will always
                                    show the most up to date of each
                                    application.
                                deploymentAlias:
                                  type: string
                                  description: >-
                                    Use the fixed deploymentAlias and
                                    deploymentHost so that the microfrontend
                                    preview stays in sync with the deployment.
                                    These are only present for mono-repos when a
                                    single commit creates multiple deployments.
                                    If they are not present, productionHost will
                                    be used.
                                deploymentHost:
                                  type: string
                              required:
                                - productionHost
                              type: object
                              description: >-
                                A map of the other applications that are part of
                                this group. Only defined on the default
                                application. The field is set after deployments
                                have been created, so can be undefined, but
                                should be there for a successful deployment.
                                Note: this field will be removed when MFE alias
                                routing is fully rolled out.
                            type: object
                            description: >-
                              A map of the other applications that are part of
                              this group. Only defined on the default
                              application. The field is set after deployments
                              have been created, so can be undefined, but should
                              be there for a successful deployment. Note: this
                              field will be removed when MFE alias routing is
                              fully rolled out.
                          mfeConfigUploadState:
                            type: string
                            enum:
                              - success
                              - waiting_on_build
                              - no_config
                            description: >-
                              The result of the microfrontends config upload
                              during deployment creation / build. Only set for
                              default app deployments. The config upload is
                              attempted during deployment create, and then again
                              during the build. If the config is not in the root
                              directory, or the deployment is prebuilt, the
                              config cannot be uploaded during deployment
                              create. The upload during deployment build finds
                              the config even if it's not in the root directory,
                              as it has access to all files. Uploading the
                              config during create is ideal, as then all child
                              deployments are guaranteed to have access to the
                              default app deployment config even if the default
                              app has not yet started building. If the config is
                              not uploaded, the child app will show as building
                              until the config has been uploaded during the
                              default app build. - `success` - The config was
                              uploaded successfully, either when the deployment
                              was created or during the build. -
                              `waiting_on_build` - The config could not be
                              uploaded during deployment create, will be
                              attempted again during the build. - `no_config` -
                              No config was found. Only set once the build has
                              not found the config in any of the deployment's
                              files. - `undefined` - Legacy deployments, or
                              there was an error uploading the config during
                              deployment create.
                          defaultAppProjectName:
                            type: string
                            description: >-
                              The project name of the default app of this
                              deployment's microfrontends group.
                          defaultRoute:
                            type: string
                            description: >-
                              A path that is used to take screenshots and as the
                              default path in preview links when a domain for
                              this microfrontend is shown in the UI.
                          groupIds:
                            items:
                              oneOf:
                                - type: string
                                - type: string
                            maxItems: 2
                            minItems: 2
                            type: array
                            description: >-
                              The group of microfrontends that this project
                              belongs to. Each microfrontend project must belong
                              to a microfrontends group that is the set of
                              microfrontends that are used together.
                          microfrontendsAlias2Enabled:
                            type: boolean
                            description: >-
                              Whether the MicrofrontendsAlias2 team flag should
                              be considered enabled for this deployment or not.
                        required:
                          - isDefaultApp
                          - defaultAppProjectName
                          - groupIds
                        type: object
              config:
                allOf:
                  - properties:
                      version:
                        type: number
                      functionType:
                        type: string
                        enum:
                          - fluid
                          - standard
                      functionMemoryType:
                        type: string
                        enum:
                          - standard
                          - standard_legacy
                          - performance
                      functionTimeout:
                        nullable: true
                        type: number
                      secureComputePrimaryRegion:
                        nullable: true
                        type: string
                      secureComputeFallbackRegion:
                        nullable: true
                        type: string
                      isUsingActiveCPU:
                        type: boolean
                    required:
                      - functionType
                      - functionMemoryType
                      - functionTimeout
                      - secureComputePrimaryRegion
                      - secureComputeFallbackRegion
                    type: object
                    description: >-
                      Since February 2025 the configuration must include
                      snapshot data at the time of deployment creation to
                      capture properties for the /deployments/:id/config
                      endpoint utilized for displaying Deployment Configuration
                      on the frontend This is optional because older deployments
                      may not have this data captured
              checks:
                allOf:
                  - properties:
                      deployment-alias:
                        properties:
                          state:
                            type: string
                            enum:
                              - succeeded
                              - failed
                              - pending
                          startedAt:
                            type: number
                          completedAt:
                            type: number
                        required:
                          - state
                          - startedAt
                        type: object
                        description: >-
                          Condensed check data. Retrieve individual check and
                          check run data using api-checks v2 routes.
                    required:
                      - deployment-alias
                    type: object
            description: The deployment including both public and private information
            requiredProperties:
              - build
              - env
              - inspectorUrl
              - isInConcurrentBuildsQueue
              - isInSystemBuildsQueue
              - projectSettings
              - aliasAssigned
              - bootedAt
              - buildingAt
              - buildSkipped
              - creator
              - public
              - status
              - id
              - createdAt
              - readyState
              - name
              - type
              - meta
              - regions
              - url
              - version
              - projectId
              - plan
              - createdIn
              - ownerId
              - routes
          - type: object
            properties:
              alias:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      A list of all the aliases (default aliases, staging
                      aliases and production aliases) that were assigned upon
                      deployment creation
                    example: []
              aliasAssigned:
                allOf:
                  - type: boolean
                    description: >-
                      A boolean that will be true when the aliases from the
                      alias property were assigned successfully
                    example: true
              bootedAt:
                allOf:
                  - type: number
              buildingAt:
                allOf:
                  - type: number
              buildContainerFinishedAt:
                allOf:
                  - type: number
                    description: >-
                      Since April 2025 it necessary for On-Demand Concurrency
                      Minutes calculation
              buildSkipped:
                allOf:
                  - type: boolean
              creator:
                allOf:
                  - properties:
                      uid:
                        type: string
                        description: The ID of the user that created the deployment
                        example: 96SnxkFiMyVKsK3pnoHfx3Hz
                      username:
                        type: string
                        description: The username of the user that created the deployment
                        example: john-doe
                      avatar:
                        type: string
                        description: The avatar of the user that created the deployment
                    required:
                      - uid
                    type: object
                    description: Information about the deployment creator
              initReadyAt:
                allOf:
                  - type: number
              isFirstBranchDeployment:
                allOf:
                  - type: boolean
              lambdas:
                allOf:
                  - items:
                      properties:
                        id:
                          type: string
                        createdAt:
                          type: number
                        readyState:
                          type: string
                          enum:
                            - BUILDING
                            - ERROR
                            - INITIALIZING
                            - READY
                        entrypoint:
                          nullable: true
                          type: string
                        readyStateAt:
                          type: number
                        output:
                          items:
                            properties:
                              path:
                                type: string
                              functionName:
                                type: string
                            required:
                              - path
                              - functionName
                            type: object
                          type: array
                      required:
                        - id
                        - output
                      type: object
                      description: >-
                        A partial representation of a Build used by the
                        deployment endpoint.
                    type: array
              public:
                allOf:
                  - type: boolean
                    description: >-
                      A boolean representing if the deployment is public or not.
                      By default this is `false`
                    example: false
              ready:
                allOf:
                  - type: number
              status:
                allOf:
                  - type: string
                    enum:
                      - QUEUED
                      - BUILDING
                      - ERROR
                      - INITIALIZING
                      - READY
                      - CANCELED
              team:
                allOf:
                  - properties:
                      id:
                        type: string
                      name:
                        type: string
                      slug:
                        type: string
                      avatar:
                        type: string
                    required:
                      - id
                      - name
                      - slug
                    type: object
                    description: The team that owns the deployment if any
              userAliases:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      An array of domains that were provided by the user when
                      creating the Deployment.
                    example:
                      - sub1.example.com
                      - sub2.example.com
              previewCommentsEnabled:
                allOf:
                  - type: boolean
                    description: >-
                      Whether or not preview comments are enabled for the
                      deployment
                    example: false
              ttyBuildLogs:
                allOf:
                  - type: boolean
              customEnvironment:
                allOf:
                  - oneOf:
                      - properties:
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
                              - production
                              - preview
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
                                    `true` if the domain is verified for use
                                    with the project. If `false` it will not be
                                    used as an alias on this project until the
                                    challenge in `verification` is completed.
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
                                      which must be completed to verify the
                                      domain for use on the project. After the
                                      challenge is complete `POST
                                      /projects/:idOrName/domains/:domain/verify`
                                      to verify the domain. Possible challenges:
                                      - If `verification.type = TXT` the
                                      `verification.domain` will be checked for
                                      a TXT record matching
                                      `verification.value`.
                                  type: array
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
                        description: >-
                          If the deployment was created using a Custom
                          Environment, then this property contains information
                          regarding the environment used.
                      - properties:
                          id:
                            type: string
                        required:
                          - id
                        type: object
                        description: >-
                          If the deployment was created using a Custom
                          Environment, then this property contains information
                          regarding the environment used.
              oomReport:
                allOf:
                  - type: string
                    enum:
                      - out-of-memory
              aliasWarning:
                allOf:
                  - nullable: true
                    properties:
                      code:
                        type: string
                      message:
                        type: string
                      link:
                        type: string
                      action:
                        type: string
                    required:
                      - code
                      - message
                    type: object
              id:
                allOf:
                  - type: string
                    description: A string holding the unique ID of the deployment
                    example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
              createdAt:
                allOf:
                  - type: number
                    description: >-
                      A number containing the date when the deployment was
                      created in milliseconds
                    example: 1540257589405
              readyState:
                allOf:
                  - type: string
                    enum:
                      - QUEUED
                      - BUILDING
                      - ERROR
                      - INITIALIZING
                      - READY
                      - CANCELED
                    description: >-
                      The state of the deployment depending on the process of
                      deploying, or if it is ready or in an error state
                    example: READY
              name:
                allOf:
                  - type: string
                    description: >-
                      The name of the project associated with the deployment at
                      the time that the deployment was created
                    example: my-project
              type:
                allOf:
                  - type: string
                    enum:
                      - LAMBDAS
              aliasError:
                allOf:
                  - nullable: true
                    properties:
                      code:
                        type: string
                      message:
                        type: string
                    required:
                      - code
                      - message
                    type: object
                    description: >-
                      An object that will contain a `code` and a `message` when
                      the aliasing fails, otherwise the value will be `null`
                    example: null
              aliasFinal:
                allOf:
                  - nullable: true
                    type: string
              autoAssignCustomDomains:
                allOf:
                  - type: boolean
                    description: applies to custom domains only, defaults to `true`
              automaticAliases:
                allOf:
                  - items:
                      type: string
                    type: array
              buildErrorAt:
                allOf:
                  - type: number
              checksState:
                allOf:
                  - type: string
                    enum:
                      - registered
                      - running
                      - completed
              checksConclusion:
                allOf:
                  - type: string
                    enum:
                      - succeeded
                      - failed
                      - skipped
                      - canceled
              deletedAt:
                allOf:
                  - nullable: true
                    type: number
                    description: >-
                      A number containing the date when the deployment was
                      deleted at milliseconds
                    example: 1540257589405
              defaultRoute:
                allOf:
                  - type: string
                    description: >-
                      Computed field that is only available for deployments with
                      a microfrontend configuration.
              canceledAt:
                allOf:
                  - type: number
              errorCode:
                allOf:
                  - type: string
              errorLink:
                allOf:
                  - type: string
              errorMessage:
                allOf:
                  - nullable: true
                    type: string
              errorStep:
                allOf:
                  - type: string
              passiveRegions:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      Since November 2023 this field defines a set of regions
                      that we will deploy the lambda to passively Lambdas will
                      be deployed to these regions but only invoked if all of
                      the primary `regions` are marked as out of service
              gitSource:
                allOf:
                  - oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - github
                          repoId:
                            oneOf:
                              - type: string
                              - type: number
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - repoId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github
                          org:
                            type: string
                          repo:
                            type: string
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - org
                          - repo
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github-custom-host
                          host:
                            type: string
                          repoId:
                            oneOf:
                              - type: string
                              - type: number
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - host
                          - repoId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github-custom-host
                          host:
                            type: string
                          org:
                            type: string
                          repo:
                            type: string
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - host
                          - org
                          - repo
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github-limited
                          repoId:
                            oneOf:
                              - type: string
                              - type: number
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - repoId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github-limited
                          org:
                            type: string
                          repo:
                            type: string
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - org
                          - repo
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - gitlab
                          projectId:
                            oneOf:
                              - type: string
                              - type: number
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - projectId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - bitbucket
                          workspaceUuid:
                            type: string
                          repoUuid:
                            type: string
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - repoUuid
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - bitbucket
                          owner:
                            type: string
                          slug:
                            type: string
                          ref:
                            nullable: true
                            type: string
                          sha:
                            type: string
                          prId:
                            nullable: true
                            type: number
                        required:
                          - type
                          - owner
                          - slug
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - custom
                          ref:
                            type: string
                          sha:
                            type: string
                          gitUrl:
                            type: string
                        required:
                          - type
                          - ref
                          - sha
                          - gitUrl
                        type: object
                        description: >-
                          Allows custom git sources (local folder mounted to the
                          container) in test mode
                      - properties:
                          type:
                            type: string
                            enum:
                              - github
                          ref:
                            type: string
                          sha:
                            type: string
                          repoId:
                            type: number
                          org:
                            type: string
                          repo:
                            type: string
                        required:
                          - type
                          - ref
                          - sha
                          - repoId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github-custom-host
                          host:
                            type: string
                          ref:
                            type: string
                          sha:
                            type: string
                          repoId:
                            type: number
                          org:
                            type: string
                          repo:
                            type: string
                        required:
                          - type
                          - host
                          - ref
                          - sha
                          - repoId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - github-limited
                          ref:
                            type: string
                          sha:
                            type: string
                          repoId:
                            type: number
                          org:
                            type: string
                          repo:
                            type: string
                        required:
                          - type
                          - ref
                          - sha
                          - repoId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - gitlab
                          ref:
                            type: string
                          sha:
                            type: string
                          projectId:
                            type: number
                        required:
                          - type
                          - ref
                          - sha
                          - projectId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - bitbucket
                          ref:
                            type: string
                          sha:
                            type: string
                          owner:
                            type: string
                          slug:
                            type: string
                          workspaceUuid:
                            type: string
                          repoUuid:
                            type: string
                        required:
                          - type
                          - ref
                          - sha
                          - workspaceUuid
                          - repoUuid
                        type: object
              meta:
                allOf:
                  - additionalProperties:
                      type: string
                    type: object
              originCacheRegion:
                allOf:
                  - type: string
              nodeVersion:
                allOf:
                  - type: string
                    enum:
                      - 22.x
                      - 20.x
                      - 18.x
                      - 16.x
                      - 14.x
                      - 12.x
                      - 10.x
                      - 8.10.x
                    description: >-
                      If set it overrides the `projectSettings.nodeVersion` for
                      this deployment.
              project:
                allOf:
                  - properties:
                      id:
                        type: string
                      name:
                        type: string
                      framework:
                        nullable: true
                        type: string
                    required:
                      - id
                      - name
                    type: object
                    description: >-
                      The public project information associated with the
                      deployment.
              readySubstate:
                allOf:
                  - type: string
                    enum:
                      - STAGED
                      - ROLLING
                      - PROMOTED
                    description: >-
                      Substate of deployment when readyState is 'READY' Tracks
                      whether or not deployment has seen production traffic: -
                      STAGED: never seen production traffic - ROLLING: in the
                      process of having production traffic gradually
                      transitioned. - PROMOTED: has seen production traffic
              regions:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: The regions the deployment exists in
                    example:
                      - sfo1
              softDeletedByRetention:
                allOf:
                  - type: boolean
                    description: >-
                      flag to indicate if the deployment was deleted by
                      retention policy
                    example: 'true'
              source:
                allOf:
                  - type: string
                    enum:
                      - api-trigger-git-deploy
                      - cli
                      - clone/repo
                      - git
                      - import
                      - import/repo
                      - redeploy
                      - v0-web
                    description: Where was the deployment created from
                    example: cli
              target:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - staging
                      - production
                    description: >-
                      If defined, either `staging` if a staging alias in the
                      format `<project>.<team>.now.sh` was assigned upon
                      creation, or `production` if the aliases from `alias` were
                      assigned. `null` value indicates the "preview" deployment.
                    example: null
              undeletedAt:
                allOf:
                  - type: number
                    description: >-
                      A number containing the date when the deployment was
                      undeleted at milliseconds
                    example: 1540257589405
              url:
                allOf:
                  - type: string
                    description: A string with the unique URL of the deployment
                    example: my-instant-deployment-3ij3cxz9qr.now.sh
              version:
                allOf:
                  - type: number
                    enum:
                      - 2
                    description: >-
                      The platform version that was used to create the
                      deployment.
                    example: 2
              oidcTokenClaims:
                allOf:
                  - properties:
                      iss:
                        type: string
                      sub:
                        type: string
                      scope:
                        type: string
                      aud:
                        type: string
                      owner:
                        type: string
                      owner_id:
                        type: string
                      project:
                        type: string
                      project_id:
                        type: string
                      environment:
                        type: string
                    required:
                      - iss
                      - sub
                      - scope
                      - aud
                      - owner
                      - owner_id
                      - project
                      - project_id
                      - environment
                    type: object
            description: The deployment including only public information
            requiredProperties:
              - aliasAssigned
              - bootedAt
              - buildingAt
              - buildSkipped
              - creator
              - public
              - status
              - id
              - createdAt
              - readyState
              - name
              - type
              - meta
              - regions
              - url
              - version
        examples:
          example:
            value:
              aliasAssignedAt: 123
              alwaysRefuseToBuild: true
              build:
                env:
                  - <string>
              buildArtifactUrls:
                - <string>
              builds:
                - use: <string>
                  src: <string>
                  config: {}
              env:
                - <string>
              inspectorUrl: <string>
              isInConcurrentBuildsQueue: true
              isInSystemBuildsQueue: true
              projectSettings:
                buildCommand: <string>
                devCommand: <string>
                framework: blitzjs
                commandForIgnoringBuildStep: <string>
                installCommand: <string>
                outputDirectory: <string>
                speedInsights:
                  id: <string>
                  enabledAt: 123
                  disabledAt: 123
                  canceledAt: 123
                  hasData: true
                  paidAt: 123
                webAnalytics:
                  id: <string>
                  disabledAt: 123
                  canceledAt: 123
                  enabledAt: 123
                  hasData: true
              readyStateReason: <string>
              integrations:
                status: skipped
                startedAt: 123
                completedAt: 123
                skippedAt: 123
                skippedBy: <string>
              images:
                sizes:
                  - 123
                qualities:
                  - 123
                domains:
                  - <string>
                remotePatterns:
                  - protocol: http
                    hostname: <string>
                    port: <string>
                    pathname: <string>
                    search: <string>
                localPatterns:
                  - pathname: <string>
                    search: <string>
                minimumCacheTTL: 123
                formats:
                  - image/avif
                dangerouslyAllowSVG: true
                contentSecurityPolicy: <string>
                contentDispositionType: inline
              alias: []
              aliasAssigned: true
              bootedAt: 123
              buildingAt: 123
              buildContainerFinishedAt: 123
              buildSkipped: true
              creator:
                uid: 96SnxkFiMyVKsK3pnoHfx3Hz
                username: john-doe
                avatar: <string>
              initReadyAt: 123
              isFirstBranchDeployment: true
              lambdas:
                - id: <string>
                  createdAt: 123
                  readyState: BUILDING
                  entrypoint: <string>
                  readyStateAt: 123
                  output:
                    - path: <string>
                      functionName: <string>
              public: false
              ready: 123
              status: QUEUED
              team:
                id: <string>
                name: <string>
                slug: <string>
                avatar: <string>
              userAliases:
                - sub1.example.com
                - sub2.example.com
              previewCommentsEnabled: false
              ttyBuildLogs: true
              customEnvironment:
                id: <string>
                slug: <string>
                type: production
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
              oomReport: out-of-memory
              aliasWarning:
                code: <string>
                message: <string>
                link: <string>
                action: <string>
              id: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
              createdAt: 1540257589405
              readyState: READY
              name: my-project
              type: LAMBDAS
              aliasError: null
              aliasFinal: <string>
              autoAssignCustomDomains: true
              automaticAliases:
                - <string>
              buildErrorAt: 123
              checksState: registered
              checksConclusion: succeeded
              deletedAt: 1540257589405
              defaultRoute: <string>
              canceledAt: 123
              errorCode: <string>
              errorLink: <string>
              errorMessage: <string>
              errorStep: <string>
              passiveRegions:
                - <string>
              gitSource:
                type: github
                repoId: <string>
                ref: <string>
                sha: <string>
                prId: 123
              meta: {}
              originCacheRegion: <string>
              nodeVersion: 22.x
              project:
                id: <string>
                name: <string>
                framework: <string>
              readySubstate: STAGED
              regions:
                - sfo1
              softDeletedByRetention: 'true'
              source: cli
              target: null
              undeletedAt: 1540257589405
              url: my-instant-deployment-3ij3cxz9qr.now.sh
              version: 2
              oidcTokenClaims:
                iss: <string>
                sub: <string>
                scope: <string>
                aud: <string>
                owner: <string>
                owner_id: <string>
                project: <string>
                project_id: <string>
                environment: <string>
              projectId: <string>
              plan: pro
              connectBuildsEnabled: true
              connectConfigurationId: <string>
              createdIn: <string>
              crons:
                - schedule: <string>
                  path: <string>
              functions: {}
              monorepoManager: <string>
              ownerId: <string>
              passiveConnectConfigurationId: <string>
              routes:
                - src: <string>
                  dest: <string>
                  headers: {}
                  methods:
                    - <string>
                  continue: true
                  override: true
                  caseSensitive: true
                  check: true
                  important: true
                  status: 123
                  has:
                    - type: host
                      value: <string>
                  missing:
                    - type: host
                      value: <string>
                  mitigate:
                    action: challenge
                  transforms:
                    - type: request.headers
                      op: append
                      target:
                        key: <string>
                      args: <string>
                  locale:
                    redirect: {}
                    cookie: <string>
                  middlewarePath: <string>
                  middlewareRawSrc:
                    - <string>
                  middleware: 123
              gitRepo:
                namespace: <string>
                projectId: 123
                type: gitlab
                url: <string>
                path: <string>
                defaultBranch: <string>
                name: <string>
                private: true
                ownerType: team
              flags:
                definitions: {}
              microfrontends:
                isDefaultApp: true
                defaultAppProjectName: <string>
                defaultRoute: <string>
                groupIds:
                  - <string>
                microfrontendsAlias2Enabled: true
              config:
                version: 123
                functionType: fluid
                functionMemoryType: standard
                functionTimeout: 123
                secureComputePrimaryRegion: <string>
                secureComputeFallbackRegion: <string>
                isUsingActiveCPU: true
              checks:
                deployment-alias:
                  state: succeeded
                  startedAt: 123
                  completedAt: 123
        description: |-
          The deployment including only public information
          The deployment including both public and private information
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
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
  schemas:
    FlagJSONValue:
      nullable: true
      oneOf:
        - type: string
        - type: number
        - type: boolean
        - items:
            $ref: '#/components/schemas/FlagJSONValue'
          type: array
          description: >-
            TODO: The following types will eventually be exported by a more
            relevant package.
        - additionalProperties:
            $ref: '#/components/schemas/FlagJSONValue'
          type: object

````

--------------------------------------------------------------------------------
title: "Get deployment events"

last_updated: "2025-11-07T00:37:08.782Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/deployments/get-deployment-events"
--------------------------------------------------------------------------------

# Get deployment events

> Get the build logs of a deployment by deployment ID and build ID. It can work as an infinite stream of logs or as a JSON endpoint depending on the input parameters.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v3/deployments/{idOrUrl}/events
paths:
  path: /v3/deployments/{idOrUrl}/events
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
        idOrUrl:
          schema:
            - type: string
              required: true
              description: The unique identifier or hostname of the deployment.
              example: dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd
      query:
        direction:
          schema:
            - type: enum<string>
              enum:
                - backward
                - forward
              required: false
              description: Order of the returned events based on the timestamp.
              default: forward
              example: backward
        follow:
          schema:
            - type: enum<number>
              enum:
                - 0
                - 1
              required: false
              description: >-
                When enabled, this endpoint will return live events as they
                happen.
              example: 1
        limit:
          schema:
            - type: number
              required: false
              description: >-
                Maximum number of events to return. Provide `-1` to return all
                available logs.
              example: 100
        name:
          schema:
            - type: string
              required: false
              description: Deployment build ID.
              example: bld_cotnkcr76
        since:
          schema:
            - type: number
              required: false
              description: Timestamp for when build logs should be pulled from.
              example: 1540095775941
        until:
          schema:
            - type: number
              required: false
              description: Timestamp for when the build logs should be pulled up until.
              example: 1540106318643
        statusCode:
          schema:
            - type: number
              required: false
              description: HTTP status code range to filter events by.
              example: 5xx
            - type: string
              required: false
              description: HTTP status code range to filter events by.
              example: 5xx
        delimiter:
          schema:
            - type: enum<number>
              enum:
                - 0
                - 1
              required: false
              example: 1
        builds:
          schema:
            - type: enum<number>
              enum:
                - 0
                - 1
              required: false
              example: 1
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
      - label: getDeploymentEvents
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Deployments.GetDeploymentEvents(ctx, operations.GetDeploymentEventsRequest{\n        IDOrURL: \"dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd\",\n        Direction: operations.DirectionBackward.ToPointer(),\n        Follow: vercel.Float64(1),\n        Limit: vercel.Float64(100),\n        Name: vercel.String(\"bld_cotnkcr76\"),\n        Since: vercel.Float64(1540095775941),\n        Until: vercel.Float64(1540106318643),\n        StatusCode: vercel.Pointer(operations.CreateStatusCodeStr(\n            \"5xx\",\n        )),\n        Delimiter: vercel.Float64(1),\n        Builds: vercel.Float64(1),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: getDeploymentEvents
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.deployments.getDeploymentEvents({
              idOrUrl: "dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd",
              direction: "backward",
              follow: 1,
              limit: 100,
              name: "bld_cotnkcr76",
              since: 1540095775941,
              until: 1540106318643,
              statusCode: "5xx",
              delimiter: 1,
              builds: 1,
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
                - oneOf:
                    - properties:
                        type:
                          type: string
                          enum:
                            - delimiter
                            - command
                            - stdout
                            - stderr
                            - exit
                            - deployment-state
                            - middleware
                            - middleware-invocation
                            - edge-function-invocation
                            - metric
                            - report
                            - fatal
                        created:
                          type: number
                        payload:
                          properties:
                            deploymentId:
                              type: string
                            info:
                              properties:
                                type:
                                  type: string
                                name:
                                  type: string
                                entrypoint:
                                  type: string
                                path:
                                  type: string
                                step:
                                  type: string
                                readyState:
                                  type: string
                              required:
                                - type
                                - name
                              type: object
                            text:
                              type: string
                            id:
                              type: string
                            date:
                              type: number
                            serial:
                              type: string
                            created:
                              type: number
                            statusCode:
                              type: number
                            requestId:
                              type: string
                            proxy:
                              properties:
                                timestamp:
                                  type: number
                                method:
                                  type: string
                                host:
                                  type: string
                                path:
                                  type: string
                                statusCode:
                                  type: number
                                userAgent:
                                  items:
                                    type: string
                                  type: array
                                referer:
                                  type: string
                                clientIp:
                                  type: string
                                region:
                                  type: string
                                scheme:
                                  type: string
                                responseByteSize:
                                  type: number
                                cacheId:
                                  type: string
                                pathType:
                                  type: string
                                pathTypeVariant:
                                  type: string
                                vercelId:
                                  type: string
                                vercelCache:
                                  type: string
                                  enum:
                                    - MISS
                                    - HIT
                                    - STALE
                                    - BYPASS
                                    - PRERENDER
                                    - REVALIDATED
                                lambdaRegion:
                                  type: string
                                wafAction:
                                  type: string
                                  enum:
                                    - log
                                    - challenge
                                    - deny
                                    - bypass
                                    - rate_limit
                                wafRuleId:
                                  type: string
                              required:
                                - timestamp
                                - method
                                - host
                                - path
                                - userAgent
                                - referer
                                - region
                              type: object
                          required:
                            - deploymentId
                            - id
                            - date
                            - serial
                          type: object
                      required:
                        - type
                        - created
                        - payload
                      type: object
                    - properties:
                        created:
                          type: number
                        date:
                          type: number
                        deploymentId:
                          type: string
                        id:
                          type: string
                        info:
                          properties:
                            type:
                              type: string
                            name:
                              type: string
                            entrypoint:
                              type: string
                            path:
                              type: string
                            step:
                              type: string
                            readyState:
                              type: string
                          required:
                            - type
                            - name
                          type: object
                        serial:
                          type: string
                        text:
                          type: string
                        type:
                          type: string
                          enum:
                            - delimiter
                            - command
                            - stdout
                            - stderr
                            - exit
                            - deployment-state
                            - middleware
                            - middleware-invocation
                            - edge-function-invocation
                            - metric
                            - report
                            - fatal
                        level:
                          type: string
                          enum:
                            - error
                            - warning
                      required:
                        - created
                        - date
                        - deploymentId
                        - id
                        - info
                        - serial
                        - type
                      type: object
                  nullable: true
          - type: 'null'
        examples:
          example:
            value:
              - type: delimiter
                created: 123
                payload:
                  deploymentId: <string>
                  info:
                    type: <string>
                    name: <string>
                    entrypoint: <string>
                    path: <string>
                    step: <string>
                    readyState: <string>
                  text: <string>
                  id: <string>
                  date: 123
                  serial: <string>
                  created: 123
                  statusCode: 123
                  requestId: <string>
                  proxy:
                    timestamp: 123
                    method: <string>
                    host: <string>
                    path: <string>
                    statusCode: 123
                    userAgent:
                      - <string>
                    referer: <string>
                    clientIp: <string>
                    region: <string>
                    scheme: <string>
                    responseByteSize: 123
                    cacheId: <string>
                    pathType: <string>
                    pathTypeVariant: <string>
                    vercelId: <string>
                    vercelCache: MISS
                    lambdaRegion: <string>
                    wafAction: log
                    wafRuleId: <string>
        description: ''
      application/stream+json:
        schemaArray:
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - delimiter
                      - command
                      - stdout
                      - stderr
                      - exit
                      - deployment-state
                      - middleware
                      - middleware-invocation
                      - edge-function-invocation
                      - metric
                      - report
                      - fatal
              created:
                allOf:
                  - type: number
              payload:
                allOf:
                  - properties:
                      deploymentId:
                        type: string
                      info:
                        properties:
                          type:
                            type: string
                          name:
                            type: string
                          entrypoint:
                            type: string
                          path:
                            type: string
                          step:
                            type: string
                          readyState:
                            type: string
                        required:
                          - type
                          - name
                        type: object
                      text:
                        type: string
                      id:
                        type: string
                      date:
                        type: number
                      serial:
                        type: string
                      created:
                        type: number
                      statusCode:
                        type: number
                      requestId:
                        type: string
                      proxy:
                        properties:
                          timestamp:
                            type: number
                          method:
                            type: string
                          host:
                            type: string
                          path:
                            type: string
                          statusCode:
                            type: number
                          userAgent:
                            items:
                              type: string
                            type: array
                          referer:
                            type: string
                          clientIp:
                            type: string
                          region:
                            type: string
                          scheme:
                            type: string
                          responseByteSize:
                            type: number
                          cacheId:
                            type: string
                          pathType:
                            type: string
                          pathTypeVariant:
                            type: string
                          vercelId:
                            type: string
                          vercelCache:
                            type: string
                            enum:
                              - MISS
                              - HIT
                              - STALE
                              - BYPASS
                              - PRERENDER
                              - REVALIDATED
                          lambdaRegion:
                            type: string
                          wafAction:
                            type: string
                            enum:
                              - log
                              - challenge
                              - deny
                              - bypass
                              - rate_limit
                          wafRuleId:
                            type: string
                        required:
                          - timestamp
                          - method
                          - host
                          - path
                          - userAgent
                          - referer
                          - region
                        type: object
                    required:
                      - deploymentId
                      - id
                      - date
                      - serial
                    type: object
            requiredProperties:
              - type
              - created
              - payload
          - type: object
            properties:
              created:
                allOf:
                  - type: number
              date:
                allOf:
                  - type: number
              deploymentId:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
              info:
                allOf:
                  - properties:
                      type:
                        type: string
                      name:
                        type: string
                      entrypoint:
                        type: string
                      path:
                        type: string
                      step:
                        type: string
                      readyState:
                        type: string
                    required:
                      - type
                      - name
                    type: object
              serial:
                allOf:
                  - type: string
              text:
                allOf:
                  - type: string
              type:
                allOf:
                  - type: string
                    enum:
                      - delimiter
                      - command
                      - stdout
                      - stderr
                      - exit
                      - deployment-state
                      - middleware
                      - middleware-invocation
                      - edge-function-invocation
                      - metric
                      - report
                      - fatal
              level:
                allOf:
                  - type: string
                    enum:
                      - error
                      - warning
            requiredProperties:
              - created
              - date
              - deploymentId
              - id
              - info
              - serial
              - type
        examples:
          example:
            value:
              type: delimiter
              created: 123
              payload:
                deploymentId: <string>
                info:
                  type: <string>
                  name: <string>
                  entrypoint: <string>
                  path: <string>
                  step: <string>
                  readyState: <string>
                text: <string>
                id: <string>
                date: 123
                serial: <string>
                created: 123
                statusCode: 123
                requestId: <string>
                proxy:
                  timestamp: 123
                  method: <string>
                  host: <string>
                  path: <string>
                  statusCode: 123
                  userAgent:
                    - <string>
                  referer: <string>
                  clientIp: <string>
                  region: <string>
                  scheme: <string>
                  responseByteSize: 123
                  cacheId: <string>
                  pathType: <string>
                  pathTypeVariant: <string>
                  vercelId: <string>
                  vercelCache: MISS
                  lambdaRegion: <string>
                  wafAction: log
                  wafRuleId: <string>
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get Deployment File Contents"

last_updated: "2025-11-07T00:37:08.628Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/deployments/get-deployment-file-contents"
--------------------------------------------------------------------------------

# Get Deployment File Contents

> Allows to retrieve the content of a file by supplying the file identifier and the deployment unique identifier. The response body will contain a JSON response containing the contents of the file encoded as base64.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v8/deployments/{id}/files/{fileId}
paths:
  path: /v8/deployments/{id}/files/{fileId}
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
              description: The unique deployment identifier
        fileId:
          schema:
            - type: string
              required: true
              description: The unique file identifier
      query:
        path:
          schema:
            - type: string
              required: false
              description: Path to the file to fetch (only for Git deployments)
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
      - label: getDeploymentFileContents
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.deployments.getDeploymentFileContents({
              id: "<id>",
              fileId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });


          }

          run();
  response:
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
              File not found
              Deployment not found
        examples: {}
        description: |-
          File not found
          Deployment not found
    '410':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Invalid API version.
        examples: {}
        description: Invalid API version.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "List Deployment Files"

last_updated: "2025-11-07T00:37:08.552Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/deployments/list-deployment-files"
--------------------------------------------------------------------------------

# List Deployment Files

> Allows to retrieve the file structure of the source code of a deployment by supplying the deployment unique identifier. If the deployment was created with the Vercel CLI or the API directly with the `files` key, it will have a file tree that can be retrievable.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v6/deployments/{id}/files
paths:
  path: /v6/deployments/{id}/files
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
              description: The unique deployment identifier
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
      - label: listDeploymentFiles
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Deployments.ListDeploymentFiles(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.FileTrees != nil {\n        // handle response\n    }\n}"
      - label: listDeploymentFiles
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.deployments.listDeploymentFiles({
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
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/FileTree'
        examples:
          example:
            value:
              - name: my-file.json
                type: file
                uid: 2d4aad419917f15b1146e9e03ddc9bb31747e4d0
                children:
                  - {}
                contentType: application/json
                mode: 123
        description: Retrieved the file tree successfully
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
              File tree not found
              Deployment not found
        examples: {}
        description: |-
          File tree not found
          Deployment not found
  deprecated: false
  type: path
components:
  schemas:
    FileTree:
      properties:
        name:
          type: string
          description: The name of the file tree entry
          example: my-file.json
        type:
          type: string
          enum:
            - directory
            - file
            - symlink
            - lambda
            - middleware
            - invalid
          description: String indicating the type of file tree entry.
          example: file
        uid:
          type: string
          description: The unique identifier of the file (only valid for the `file` type)
          example: 2d4aad419917f15b1146e9e03ddc9bb31747e4d0
        children:
          items:
            $ref: '#/components/schemas/FileTree'
          type: array
          description: >-
            The list of children files of the directory (only valid for the
            `directory` type)
        contentType:
          type: string
          description: The content-type of the file (only valid for the `file` type)
          example: application/json
        mode:
          type: number
          description: The file "mode" indicating file type and permissions.
      required:
        - name
        - type
        - mode
      type: object
      description: A deployment file tree entry

````

--------------------------------------------------------------------------------
title: "List deployments"

last_updated: "2025-11-07T00:37:09.411Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/deployments/list-deployments"
--------------------------------------------------------------------------------

# List deployments

> List deployments under the authenticated user or team. If a deployment hasn't finished uploading (is incomplete), the `url` property will have a value of `null`.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v6/deployments
paths:
  path: /v6/deployments
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
        app:
          schema:
            - type: string
              description: Name of the deployment.
              example: docs
        from:
          schema:
            - type: number
              description: >-
                Gets the deployment created after this Date timestamp. (default:
                current time)
              deprecated: true
              example: 1612948664566
        limit:
          schema:
            - type: number
              description: Maximum number of deployments to list from a request.
              example: 10
        projectId:
          schema:
            - type: string
              description: Filter deployments from the given ID or name.
              example: QmXGTs7mvAMMC7WW5ebrM33qKG32QK3h4vmQMjmY
        projectIds:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
              description: >-
                Filter deployments from the given project IDs. Cannot be used
                when projectId is specified.
              maxItems: 20
              minItems: 1
              example:
                - prj_123
                - prj_456
        target:
          schema:
            - type: string
              description: Filter deployments based on the environment.
              example: production
        to:
          schema:
            - type: number
              description: >-
                Gets the deployment created before this Date timestamp.
                (default: current time)
              deprecated: true
              example: 1612948664566
        users:
          schema:
            - type: string
              description: >-
                Filter out deployments based on users who have created the
                deployment.
              example: kr1PsOIzqEL5Xg6M4VZcZosf,K4amb7K9dAt5R2vBJWF32bmY
        since:
          schema:
            - type: number
              description: Get Deployments created after this JavaScript timestamp.
              example: 1540095775941
        until:
          schema:
            - type: number
              description: Get Deployments created before this JavaScript timestamp.
              example: 1540095775951
        state:
          schema:
            - type: string
              description: >-
                Filter deployments based on their state (`BUILDING`, `ERROR`,
                `INITIALIZING`, `QUEUED`, `READY`, `CANCELED`)
              example: BUILDING,READY
        rollbackCandidate:
          schema:
            - type: boolean
              description: Filter deployments based on their rollback candidacy
        branch:
          schema:
            - type: string
              description: Filter deployments based on the branch name
        sha:
          schema:
            - type: string
              description: Filter deployments based on the SHA
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
      - label: getDeployments
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Deployments.GetDeployments(ctx, operations.GetDeploymentsRequest{\n        App: vercel.String(\"docs\"),\n        From: vercel.Float64(1612948664566),\n        Limit: vercel.Float64(10),\n        ProjectID: vercel.String(\"QmXGTs7mvAMMC7WW5ebrM33qKG32QK3h4vmQMjmY\"),\n        Target: vercel.String(\"production\"),\n        To: vercel.Float64(1612948664566),\n        Users: vercel.String(\"kr1PsOIzqEL5Xg6M4VZcZosf,K4amb7K9dAt5R2vBJWF32bmY\"),\n        Since: vercel.Float64(1540095775941),\n        Until: vercel.Float64(1540095775951),\n        State: vercel.String(\"BUILDING,READY\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getDeployments
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.deployments.getDeployments({
              app: "docs",
              from: 1612948664566,
              limit: 10,
              projectId: "QmXGTs7mvAMMC7WW5ebrM33qKG32QK3h4vmQMjmY",
              projectIds: [
                "prj_123",
                "prj_456",
              ],
              target: "production",
              to: 1612948664566,
              users: "kr1PsOIzqEL5Xg6M4VZcZosf,K4amb7K9dAt5R2vBJWF32bmY",
              since: 1540095775941,
              until: 1540095775951,
              state: "BUILDING,READY",
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
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
              deployments:
                allOf:
                  - items:
                      properties:
                        uid:
                          type: string
                          description: The unique identifier of the deployment.
                          example: dpl_2euZBFqxYdDMDG1jTrHFnNZ2eUVa
                        name:
                          type: string
                          description: The name of the deployment.
                          example: docs
                        projectId:
                          type: string
                          description: The project ID of the deployment
                        url:
                          type: string
                          description: The URL of the deployment.
                          example: docs-9jaeg38me.vercel.app
                        created:
                          type: number
                          description: Timestamp of when the deployment got created.
                          example: 1609492210000
                        defaultRoute:
                          type: string
                          description: >-
                            The default route that should be used for
                            screenshots and links if configured with
                            microfrontends.
                          example: /docs
                        deleted:
                          type: number
                          description: Timestamp of when the deployment got deleted.
                          example: 1609492210000
                        undeleted:
                          type: number
                          description: Timestamp of when the deployment was undeleted.
                          example: 1609492210000
                        softDeletedByRetention:
                          type: boolean
                          description: >-
                            Optional flag to indicate if the deployment was soft
                            deleted by retention policy.
                          example: true
                        source:
                          type: string
                          enum:
                            - api-trigger-git-deploy
                            - cli
                            - clone/repo
                            - git
                            - import
                            - import/repo
                            - redeploy
                            - v0-web
                          description: The source of the deployment.
                          example: cli
                        state:
                          type: string
                          enum:
                            - BUILDING
                            - ERROR
                            - INITIALIZING
                            - QUEUED
                            - READY
                            - CANCELED
                            - DELETED
                          description: In which state is the deployment.
                          example: READY
                        readyState:
                          type: string
                          enum:
                            - BUILDING
                            - ERROR
                            - INITIALIZING
                            - QUEUED
                            - READY
                            - CANCELED
                            - DELETED
                          description: In which state is the deployment.
                          example: READY
                        type:
                          type: string
                          enum:
                            - LAMBDAS
                          description: The type of the deployment.
                          example: LAMBDAS
                        creator:
                          properties:
                            uid:
                              type: string
                              description: The unique identifier of the user.
                              example: eLrCnEgbKhsHyfbiNR7E8496
                            email:
                              type: string
                              description: The email address of the user.
                              example: example@example.com
                            username:
                              type: string
                              description: The username of the user.
                              example: johndoe
                            githubLogin:
                              type: string
                              description: The GitHub login of the user.
                              example: johndoe
                            gitlabLogin:
                              type: string
                              description: The GitLab login of the user.
                              example: johndoe
                          required:
                            - uid
                          type: object
                          description: >-
                            Metadata information of the user who created the
                            deployment.
                        meta:
                          additionalProperties:
                            type: string
                            description: Metadata information from the Git provider.
                          type: object
                          description: Metadata information from the Git provider.
                        target:
                          nullable: true
                          type: string
                          enum:
                            - production
                            - staging
                          description: >-
                            On which environment has the deployment been
                            deployed to.
                          example: production
                        aliasError:
                          nullable: true
                          properties:
                            code:
                              type: string
                            message:
                              type: string
                          required:
                            - code
                            - message
                          type: object
                          description: >-
                            An error object in case aliasing of the deployment
                            failed.
                        aliasAssigned:
                          nullable: true
                          oneOf:
                            - type: number
                            - type: boolean
                        createdAt:
                          type: number
                          description: Timestamp of when the deployment got created.
                          example: 1609492210000
                        buildingAt:
                          type: number
                          description: >-
                            Timestamp of when the deployment started building
                            at.
                          example: 1609492210000
                        ready:
                          type: number
                          description: Timestamp of when the deployment got ready.
                          example: 1609492210000
                        readySubstate:
                          type: string
                          enum:
                            - STAGED
                            - ROLLING
                            - PROMOTED
                          description: >-
                            Substate of deployment when readyState is 'READY'
                            Tracks whether or not deployment has seen production
                            traffic: - STAGED: never seen production traffic -
                            ROLLING: in the process of gradually transitioning
                            production traffic - PROMOTED: has seen production
                            traffic
                        checksState:
                          type: string
                          enum:
                            - registered
                            - running
                            - completed
                          description: State of all registered checks
                        checksConclusion:
                          type: string
                          enum:
                            - succeeded
                            - failed
                            - skipped
                            - canceled
                          description: Conclusion for checks
                        checks:
                          properties:
                            deployment-alias:
                              properties:
                                state:
                                  type: string
                                  enum:
                                    - succeeded
                                    - failed
                                    - pending
                                startedAt:
                                  type: number
                                completedAt:
                                  type: number
                              required:
                                - state
                                - startedAt
                              type: object
                              description: >-
                                Detailed information about v2 deployment checks.
                                Includes information about blocked workflows in
                                the deployment lifecycle.
                          required:
                            - deployment-alias
                          type: object
                          description: >-
                            Detailed information about v2 deployment checks.
                            Includes information about blocked workflows in the
                            deployment lifecycle.
                        inspectorUrl:
                          nullable: true
                          type: string
                          description: Vercel URL to inspect the deployment.
                          example: >-
                            https://vercel.com/acme/nextjs/J1hXN00qjUeoYfpEEf7dnDtpSiVq
                        errorCode:
                          type: string
                          description: Error code when the deployment is in an error state.
                          example: BUILD_FAILED
                        errorMessage:
                          nullable: true
                          type: string
                          description: >-
                            Error message when the deployment is in an canceled
                            or error state.
                          example: >-
                            The Deployment has been canceled because this
                            project was not affected
                        oomReport:
                          type: string
                          enum:
                            - out-of-memory
                          description: >-
                            Indicates if the deployment encountered an
                            out-of-memory error.
                          example: out-of-memory
                        isRollbackCandidate:
                          nullable: true
                          type: boolean
                          description: Deployment can be used for instant rollback
                        projectSettings:
                          properties:
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
                            gitForkProtection:
                              type: boolean
                            customerSupportCodeVisibility:
                              type: boolean
                            gitLFS:
                              type: boolean
                            devCommand:
                              nullable: true
                              type: string
                            installCommand:
                              nullable: true
                              type: string
                            buildCommand:
                              nullable: true
                              type: string
                            nodeVersion:
                              type: string
                              enum:
                                - 22.x
                                - 20.x
                                - 18.x
                                - 16.x
                                - 14.x
                                - 12.x
                                - 10.x
                                - 8.10.x
                            outputDirectory:
                              nullable: true
                              type: string
                            publicSource:
                              nullable: true
                              type: boolean
                            rootDirectory:
                              nullable: true
                              type: string
                            sourceFilesOutsideRootDirectory:
                              type: boolean
                            commandForIgnoringBuildStep:
                              nullable: true
                              type: string
                            createdAt:
                              type: number
                            speedInsights:
                              properties:
                                id:
                                  type: string
                                enabledAt:
                                  type: number
                                disabledAt:
                                  type: number
                                canceledAt:
                                  type: number
                                hasData:
                                  type: boolean
                                paidAt:
                                  type: number
                              required:
                                - id
                              type: object
                            webAnalytics:
                              properties:
                                id:
                                  type: string
                                disabledAt:
                                  type: number
                                canceledAt:
                                  type: number
                                enabledAt:
                                  type: number
                                hasData:
                                  type: boolean
                              required:
                                - id
                              type: object
                            skipGitConnectDuringLink:
                              type: boolean
                            gitComments:
                              properties:
                                onPullRequest:
                                  type: boolean
                                  description: Whether the Vercel bot should comment on PRs
                                onCommit:
                                  type: boolean
                                  description: >-
                                    Whether the Vercel bot should comment on
                                    commits
                              required:
                                - onPullRequest
                                - onCommit
                              type: object
                              description: Since June '23
                          type: object
                          description: >-
                            The project settings which was used for this
                            deployment
                        connectBuildsEnabled:
                          type: boolean
                          description: >-
                            The flag saying if Secure Compute network is used
                            for builds
                        connectConfigurationId:
                          type: string
                          description: >-
                            The ID of Secure Compute network used for this
                            deployment
                        passiveConnectConfigurationId:
                          type: string
                          description: >-
                            The ID of Secure Compute network used for this
                            deployment's passive functions
                        expiration:
                          type: number
                          description: >-
                            The expiration configured by the project retention
                            policy
                        proposedExpiration:
                          type: number
                          description: >-
                            The expiration proposed to replace the existing
                            expiration
                        customEnvironment:
                          properties:
                            id:
                              type: string
                            slug:
                              type: string
                          required:
                            - id
                          type: object
                          description: >-
                            The custom environment used for this deployment, if
                            any
                      required:
                        - uid
                        - name
                        - projectId
                        - url
                        - created
                        - type
                        - creator
                        - inspectorUrl
                      type: object
                    type: array
            requiredProperties:
              - pagination
              - deployments
        examples:
          example:
            value:
              pagination:
                count: 20
                next: 1540095775951
                prev: 1540095775951
              deployments:
                - uid: dpl_2euZBFqxYdDMDG1jTrHFnNZ2eUVa
                  name: docs
                  projectId: <string>
                  url: docs-9jaeg38me.vercel.app
                  created: 1609492210000
                  defaultRoute: /docs
                  deleted: 1609492210000
                  undeleted: 1609492210000
                  softDeletedByRetention: true
                  source: cli
                  state: READY
                  readyState: READY
                  type: LAMBDAS
                  creator:
                    uid: eLrCnEgbKhsHyfbiNR7E8496
                    email: example@example.com
                    username: johndoe
                    githubLogin: johndoe
                    gitlabLogin: johndoe
                  meta: {}
                  target: production
                  aliasError:
                    code: <string>
                    message: <string>
                  aliasAssigned: 123
                  createdAt: 1609492210000
                  buildingAt: 1609492210000
                  ready: 1609492210000
                  readySubstate: STAGED
                  checksState: registered
                  checksConclusion: succeeded
                  checks:
                    deployment-alias:
                      state: succeeded
                      startedAt: 123
                      completedAt: 123
                  inspectorUrl: https://vercel.com/acme/nextjs/J1hXN00qjUeoYfpEEf7dnDtpSiVq
                  errorCode: BUILD_FAILED
                  errorMessage: >-
                    The Deployment has been canceled because this project was
                    not affected
                  oomReport: out-of-memory
                  isRollbackCandidate: true
                  projectSettings:
                    framework: blitzjs
                    gitForkProtection: true
                    customerSupportCodeVisibility: true
                    gitLFS: true
                    devCommand: <string>
                    installCommand: <string>
                    buildCommand: <string>
                    nodeVersion: 22.x
                    outputDirectory: <string>
                    publicSource: true
                    rootDirectory: <string>
                    sourceFilesOutsideRootDirectory: true
                    commandForIgnoringBuildStep: <string>
                    createdAt: 123
                    speedInsights:
                      id: <string>
                      enabledAt: 123
                      disabledAt: 123
                      canceledAt: 123
                      hasData: true
                      paidAt: 123
                    webAnalytics:
                      id: <string>
                      disabledAt: 123
                      canceledAt: 123
                      enabledAt: 123
                      hasData: true
                    skipGitConnectDuringLink: true
                    gitComments:
                      onPullRequest: true
                      onCommit: true
                  connectBuildsEnabled: true
                  connectConfigurationId: <string>
                  passiveConnectConfigurationId: <string>
                  expiration: 123
                  proposedExpiration: 123
                  customEnvironment:
                    id: <string>
                    slug: <string>
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
    '422': {}
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
title: "Update deployment integration action"

last_updated: "2025-11-07T00:37:09.549Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/deployments/update-deployment-integration-action"
--------------------------------------------------------------------------------

# Update deployment integration action

> Updates the deployment integration action for the specified integration installation

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/deployments/{deploymentId}/integrations/{integrationConfigurationId}/resources/{resourceId}/actions/{action}
paths:
  path: >-
    /v1/deployments/{deploymentId}/integrations/{integrationConfigurationId}/resources/{resourceId}/actions/{action}
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
        integrationConfigurationId:
          schema:
            - type: string
              required: true
        resourceId:
          schema:
            - type: string
              required: true
        action:
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
              status:
                allOf:
                  - type: string
                    enum:
                      - running
                      - succeeded
                      - failed
              statusText:
                allOf:
                  - type: string
              statusUrl:
                allOf:
                  - type: string
                    format: uri
                    pattern: '^https?://|^sso:'
              outcomes:
                allOf:
                  - type: array
                    items:
                      oneOf:
                        - type: object
                          properties:
                            kind:
                              type: string
                            secrets:
                              type: array
                              items:
                                type: object
                                properties:
                                  name:
                                    type: string
                                  value:
                                    type: string
                                required:
                                  - name
                                  - value
                                additionalProperties: false
                          required:
                            - kind
                            - secrets
                          additionalProperties: false
            additionalProperties: false
        examples:
          example:
            value:
              status: running
              statusText: <string>
              statusUrl: <string>
              outcomes:
                - kind: <string>
                  secrets:
                    - name: <string>
                      value: <string>
    codeSamples:
      - label: update-integration-deployment-action
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.deployments.updateIntegrationDeploymentAction({
              deploymentId: "<id>",
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
              action: "<value>",
            });


          }

          run();
      - label: update-integration-deployment-action
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.integrations.updateIntegrationDeploymentAction({
              deploymentId: "<id>",
              integrationConfigurationId: "<id>",
              resourceId: "<id>",
              action: "<value>",
            });


          }

          run();
  response:
    '202': {}
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
title: "Upload Deployment Files"

last_updated: "2025-11-07T00:37:09.445Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/deployments/upload-deployment-files"
--------------------------------------------------------------------------------

# Upload Deployment Files

> Before you create a deployment you need to upload the required files for that deployment. To do it, you need to first upload each file to this endpoint. Once that's completed, you can create a new deployment with the uploaded files. The file content must be placed inside the body of the request. In the case of a successful response you'll receive a status code 200 with an empty body.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/files
paths:
  path: /v2/files
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
        Content-Length:
          schema:
            - type: number
              description: The file size in bytes
        x-vercel-digest:
          schema:
            - type: string
              description: The file SHA1 used to check the integrity
              maxLength: 40
        x-now-digest:
          schema:
            - type: string
              description: The file SHA1 used to check the integrity
              deprecated: true
              maxLength: 40
        x-now-size:
          schema:
            - type: number
              description: The file size as an alternative to `Content-Length`
              deprecated: true
      cookie: {}
    body:
      application/octet-stream:
        schemaArray:
          - type: file
            contentEncoding: binary
        examples:
          example: {}
    codeSamples:
      - label: uploadFile
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Deployments.UploadFile(ctx, operations.UploadFileRequest{})\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: uploadFile
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.deployments.uploadFile({
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
              urls:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: Array of URLs where the file was updated
                    example:
                      - example-upload.aws.com
            requiredProperties:
              - urls
          - type: object
            properties: {}
        examples:
          example:
            value:
              urls:
                - example-upload.aws.com
        description: |-
          File already uploaded
          File successfully uploaded
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the headers is invalid
              Digest is not valid
              File size is not valid
        examples: {}
        description: |-
          One of the provided values in the headers is invalid
          Digest is not valid
          File size is not valid
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
title: "Create a DNS record"

last_updated: "2025-11-07T00:37:09.417Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/dns/create-a-dns-record"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./19-cancel-a-deployment.md) | [Index](./index.md) | [Next →](./21-create-a-dns-record.md)
