**Navigation:** [← Previous](./30-remove-an-environment-variable.md) | [Index](./index.md) | [Next →](./32-retrieve-the-decrypted-value-of-an-environment-var.md)

---

# Retrieve a list of projects

> Allows to retrieve the list of projects of the authenticated user or team. The list will be paginated and the provided query parameters allow filtering the returned projects.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v10/projects
paths:
  path: /v10/projects
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
        from:
          schema:
            - type: string
              description: >-
                Query only projects updated after the given timestamp or
                continuation token.
        gitForkProtection:
          schema:
            - type: enum<string>
              enum:
                - '1'
                - '0'
              description: >-
                Specifies whether PRs from Git forks should require a team
                member's authorization before it can be deployed
              example: '1'
        limit:
          schema:
            - type: string
              description: Limit the number of projects returned
        search:
          schema:
            - type: string
              description: Search projects by the name field
              maxLength: 100
        repo:
          schema:
            - type: string
              description: Filter results by repo. Also used for project count
        repoId:
          schema:
            - type: string
              description: Filter results by Repository ID.
        repoUrl:
          schema:
            - type: string
              description: Filter results by Repository URL.
              example: https://github.com/vercel/next.js
        excludeRepos:
          schema:
            - type: string
              description: Filter results by excluding those projects that belong to a repo
        edgeConfigId:
          schema:
            - type: string
              description: Filter results by connected Edge Config ID
        edgeConfigTokenId:
          schema:
            - type: string
              description: Filter results by connected Edge Config Token ID
        deprecated:
          schema:
            - type: boolean
        elasticConcurrencyEnabled:
          schema:
            - type: enum<string>
              enum:
                - '1'
                - '0'
              description: Filter results by projects with elastic concurrency enabled
              example: '1'
        staticIpsEnabled:
          schema:
            - type: enum<string>
              enum:
                - '0'
                - '1'
              description: Filter results by projects with Static IPs enabled
              example: '1'
        buildMachineTypes:
          schema:
            - type: string
              description: >-
                Filter results by build machine types. Accepts comma-separated
                values. Use \"default\" for projects without a build machine
                type set.
              example: default,enhanced
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
      - label: getProjects
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.getProjects({
              gitForkProtection: "1",
              repoUrl: "https://github.com/vercel/next.js",
              elasticConcurrencyEnabled: "1",
              staticIpsEnabled: "1",
              buildMachineTypes: "default,enhanced",
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
              projects:
                allOf:
                  - items:
                      properties:
                        accountId:
                          type: string
                        analytics:
                          properties:
                            id:
                              type: string
                            canceledAt:
                              nullable: true
                              type: number
                            disabledAt:
                              type: number
                            enabledAt:
                              type: number
                            paidAt:
                              type: number
                            sampleRatePercent:
                              nullable: true
                              type: number
                            spendLimitInDollars:
                              nullable: true
                              type: number
                          required:
                            - id
                            - disabledAt
                            - enabledAt
                          type: object
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
                        autoExposeSystemEnvs:
                          type: boolean
                        autoAssignCustomDomains:
                          type: boolean
                        autoAssignCustomDomainsUpdatedBy:
                          type: string
                        buildCommand:
                          nullable: true
                          type: string
                        commandForIgnoringBuildStep:
                          nullable: true
                          type: string
                        connectConfigurations:
                          nullable: true
                          items:
                            properties:
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
                          type: array
                        connectConfigurationId:
                          nullable: true
                          type: string
                        connectBuildsEnabled:
                          type: boolean
                        passiveConnectConfigurationId:
                          nullable: true
                          type: string
                        createdAt:
                          type: number
                        customerSupportCodeVisibility:
                          type: boolean
                        crons:
                          properties:
                            enabledAt:
                              type: number
                              description: >-
                                The time the feature was enabled for this
                                project. Note: It enables automatically with the
                                first Deployment that outputs cronjobs.
                            disabledAt:
                              nullable: true
                              type: number
                              description: >-
                                The time the feature was disabled for this
                                project.
                            updatedAt:
                              type: number
                            deploymentId:
                              nullable: true
                              type: string
                              description: >-
                                The ID of the Deployment from which the
                                definitions originated.
                            definitions:
                              items:
                                properties:
                                  host:
                                    type: string
                                    description: The hostname that should be used.
                                    example: vercel.com
                                  path:
                                    type: string
                                    description: >-
                                      The path that should be called for the
                                      cronjob.
                                    example: /api/crons/sync-something?hello=world
                                  schedule:
                                    type: string
                                    description: The cron expression.
                                    example: 0 0 * * *
                                required:
                                  - host
                                  - path
                                  - schedule
                                type: object
                              type: array
                          required:
                            - enabledAt
                            - disabledAt
                            - updatedAt
                            - deploymentId
                            - definitions
                          type: object
                        dataCache:
                          properties:
                            userDisabled:
                              type: boolean
                            storageSizeBytes:
                              nullable: true
                              type: number
                            unlimited:
                              type: boolean
                          required:
                            - userDisabled
                          type: object
                        deploymentExpiration:
                          nullable: true
                          properties:
                            expirationDays:
                              type: number
                              description: >-
                                Number of days to keep non-production
                                deployments (mostly preview deployments) before
                                soft deletion.
                            expirationDaysProduction:
                              type: number
                              description: >-
                                Number of days to keep production deployments
                                before soft deletion.
                            expirationDaysCanceled:
                              type: number
                              description: >-
                                Number of days to keep canceled deployments
                                before soft deletion.
                            expirationDaysErrored:
                              type: number
                              description: >-
                                Number of days to keep errored deployments
                                before soft deletion.
                            deploymentsToKeep:
                              type: number
                              description: >-
                                Minimum number of production deployments to keep
                                for this project, even if they are over the
                                production expiration limit.
                          type: object
                          description: >-
                            Retention policies for deployments. These are
                            enforced at the project level, but we also maintain
                            an instance of this at the team level as a default
                            policy that gets applied to new projects.
                        devCommand:
                          nullable: true
                          type: string
                        directoryListing:
                          type: boolean
                        installCommand:
                          nullable: true
                          type: string
                        env:
                          items:
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
                                  This is used to identiy variables that have
                                  been migrated from type secret to sensitive.
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
                            required:
                              - type
                              - value
                              - key
                            type: object
                          type: array
                        customEnvironments:
                          items:
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
                                  The type of environment (production, preview,
                                  or development)
                              description:
                                type: string
                                description: >-
                                  Optional description of the environment's
                                  purpose
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
                                  Configuration for matching git branches to
                                  this environment
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
                                        with the project. If `false` it will not
                                        be used as an alias on this project
                                        until the challenge in `verification` is
                                        completed.
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
                                          A list of verification challenges, one
                                          of which must be completed to verify the
                                          domain for use on the project. After the
                                          challenge is complete `POST
                                          /projects/:idOrName/domains/:domain/verify`
                                          to verify the domain. Possible
                                          challenges: - If `verification.type =
                                          TXT` the `verification.domain` will be
                                          checked for a TXT record matching
                                          `verification.value`.
                                      type: array
                                      description: >-
                                        A list of verification challenges, one
                                        of which must be completed to verify the
                                        domain for use on the project. After the
                                        challenge is complete `POST
                                        /projects/:idOrName/domains/:domain/verify`
                                        to verify the domain. Possible
                                        challenges: - If `verification.type =
                                        TXT` the `verification.domain` will be
                                        checked for a TXT record matching
                                        `verification.value`.
                                  required:
                                    - name
                                    - apexName
                                    - projectId
                                    - verified
                                  type: object
                                  description: >-
                                    List of domains associated with this
                                    environment
                                type: array
                                description: >-
                                  List of domains associated with this
                                  environment
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
                                description: >-
                                  Timestamp when the environment was last
                                  updated
                            required:
                              - id
                              - slug
                              - type
                              - createdAt
                              - updatedAt
                            type: object
                            description: >-
                              Internal representation of a custom environment
                              with all required properties
                          type: array
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
                        gitLFS:
                          type: boolean
                        id:
                          type: string
                        ipBuckets:
                          items:
                            properties:
                              bucket:
                                type: string
                              supportUntil:
                                type: number
                            required:
                              - bucket
                            type: object
                          type: array
                        latestDeployments:
                          items:
                            properties:
                              id:
                                type: string
                              alias:
                                items:
                                  type: string
                                type: array
                              aliasAssigned:
                                nullable: true
                                oneOf:
                                  - type: number
                                  - type: boolean
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
                              aliasFinal:
                                nullable: true
                                type: string
                              automaticAliases:
                                items:
                                  type: string
                                type: array
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
                              buildingAt:
                                type: number
                              builds:
                                items:
                                  properties:
                                    use:
                                      type: string
                                    src:
                                      type: string
                                    dest:
                                      type: string
                                  required:
                                    - use
                                  type: object
                                type: array
                              checksConclusion:
                                type: string
                                enum:
                                  - succeeded
                                  - failed
                                  - skipped
                                  - canceled
                              checksState:
                                type: string
                                enum:
                                  - registered
                                  - running
                                  - completed
                              connectBuildsEnabled:
                                type: boolean
                              connectConfigurationId:
                                type: string
                              createdAt:
                                type: number
                              createdIn:
                                type: string
                              creator:
                                nullable: true
                                properties:
                                  email:
                                    type: string
                                  githubLogin:
                                    type: string
                                  gitlabLogin:
                                    type: string
                                  uid:
                                    type: string
                                  username:
                                    type: string
                                required:
                                  - email
                                  - uid
                                  - username
                                type: object
                              deletedAt:
                                type: number
                              deploymentHostname:
                                type: string
                              forced:
                                type: boolean
                              name:
                                type: string
                              meta:
                                additionalProperties:
                                  type: string
                                type: object
                              monorepoManager:
                                nullable: true
                                type: string
                              oidcTokenClaims:
                                properties:
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
                              plan:
                                type: string
                                enum:
                                  - pro
                                  - enterprise
                                  - hobby
                              previewCommentsEnabled:
                                type: boolean
                                description: >-
                                  Whether or not preview comments are enabled
                                  for the deployment
                                example: false
                              private:
                                type: boolean
                              readyAt:
                                type: number
                              readyState:
                                type: string
                                enum:
                                  - BUILDING
                                  - ERROR
                                  - INITIALIZING
                                  - QUEUED
                                  - READY
                                  - CANCELED
                              readySubstate:
                                type: string
                                enum:
                                  - STAGED
                                  - ROLLING
                                  - PROMOTED
                              requestedAt:
                                type: number
                              target:
                                nullable: true
                                type: string
                              teamId:
                                nullable: true
                                type: string
                              type:
                                type: string
                                enum:
                                  - LAMBDAS
                              url:
                                type: string
                              userId:
                                type: string
                              withCache:
                                type: boolean
                            required:
                              - id
                              - createdAt
                              - createdIn
                              - creator
                              - deploymentHostname
                              - name
                              - plan
                              - private
                              - readyState
                              - type
                              - url
                              - userId
                            type: object
                          type: array
                        link:
                          oneOf:
                            - properties:
                                org:
                                  type: string
                                repoOwnerId:
                                  type: number
                                  description: >-
                                    A new field, should be included in all new
                                    project links, is being added just in time
                                    when a deployment is created. This is needed
                                    for Protected Git scopes.
                                repo:
                                  type: string
                                repoId:
                                  type: number
                                type:
                                  type: string
                                  enum:
                                    - github
                                createdAt:
                                  type: number
                                deployHooks:
                                  items:
                                    properties:
                                      createdAt:
                                        type: number
                                      id:
                                        type: string
                                      name:
                                        type: string
                                      ref:
                                        type: string
                                      url:
                                        type: string
                                    required:
                                      - id
                                      - name
                                      - ref
                                      - url
                                    type: object
                                  type: array
                                gitCredentialId:
                                  type: string
                                updatedAt:
                                  type: number
                                sourceless:
                                  type: boolean
                                productionBranch:
                                  type: string
                              required:
                                - org
                                - type
                                - gitCredentialId
                                - productionBranch
                                - deployHooks
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - github-limited
                                repo:
                                  type: string
                                repoId:
                                  type: number
                                createdAt:
                                  type: number
                                updatedAt:
                                  type: number
                                org:
                                  type: string
                                repoOwnerId:
                                  type: number
                                  description: >-
                                    A new field, should be included in all new
                                    project links, is being added just in time
                                    when a deployment is created. This is needed
                                    for Protected Git scopes.
                                deployHooks:
                                  items:
                                    properties:
                                      createdAt:
                                        type: number
                                      id:
                                        type: string
                                      name:
                                        type: string
                                      ref:
                                        type: string
                                      url:
                                        type: string
                                    required:
                                      - id
                                      - name
                                      - ref
                                      - url
                                    type: object
                                  type: array
                                gitCredentialId:
                                  type: string
                                sourceless:
                                  type: boolean
                                productionBranch:
                                  type: string
                              required:
                                - type
                                - org
                                - gitCredentialId
                                - productionBranch
                                - deployHooks
                              type: object
                            - properties:
                                org:
                                  type: string
                                repoOwnerId:
                                  type: number
                                  description: >-
                                    A new field, should be included in all new
                                    project links, is being added just in time
                                    when a deployment is created. This is needed
                                    for Protected Git scopes.
                                repo:
                                  type: string
                                repoId:
                                  type: number
                                type:
                                  type: string
                                  enum:
                                    - github-custom-host
                                host:
                                  type: string
                                createdAt:
                                  type: number
                                deployHooks:
                                  items:
                                    properties:
                                      createdAt:
                                        type: number
                                      id:
                                        type: string
                                      name:
                                        type: string
                                      ref:
                                        type: string
                                      url:
                                        type: string
                                    required:
                                      - id
                                      - name
                                      - ref
                                      - url
                                    type: object
                                  type: array
                                gitCredentialId:
                                  type: string
                                updatedAt:
                                  type: number
                                sourceless:
                                  type: boolean
                                productionBranch:
                                  type: string
                              required:
                                - org
                                - type
                                - host
                                - gitCredentialId
                                - productionBranch
                                - deployHooks
                              type: object
                            - properties:
                                projectId:
                                  type: string
                                projectName:
                                  type: string
                                projectNameWithNamespace:
                                  type: string
                                projectNamespace:
                                  type: string
                                projectOwnerId:
                                  type: number
                                  description: >-
                                    A new field, should be included in all new
                                    project links, is being added just in time
                                    when a deployment is created. This is needed
                                    for Protected Git scopes. This is the id of
                                    the top level group that a namespace belongs
                                    to. Gitlab supports group nesting (up to 20
                                    levels).
                                projectUrl:
                                  type: string
                                type:
                                  type: string
                                  enum:
                                    - gitlab
                                createdAt:
                                  type: number
                                deployHooks:
                                  items:
                                    properties:
                                      createdAt:
                                        type: number
                                      id:
                                        type: string
                                      name:
                                        type: string
                                      ref:
                                        type: string
                                      url:
                                        type: string
                                    required:
                                      - id
                                      - name
                                      - ref
                                      - url
                                    type: object
                                  type: array
                                gitCredentialId:
                                  type: string
                                updatedAt:
                                  type: number
                                sourceless:
                                  type: boolean
                                productionBranch:
                                  type: string
                              required:
                                - projectId
                                - projectName
                                - projectNameWithNamespace
                                - projectNamespace
                                - projectUrl
                                - type
                                - gitCredentialId
                                - productionBranch
                                - deployHooks
                              type: object
                            - properties:
                                name:
                                  type: string
                                slug:
                                  type: string
                                owner:
                                  type: string
                                type:
                                  type: string
                                  enum:
                                    - bitbucket
                                uuid:
                                  type: string
                                workspaceUuid:
                                  type: string
                                createdAt:
                                  type: number
                                deployHooks:
                                  items:
                                    properties:
                                      createdAt:
                                        type: number
                                      id:
                                        type: string
                                      name:
                                        type: string
                                      ref:
                                        type: string
                                      url:
                                        type: string
                                    required:
                                      - id
                                      - name
                                      - ref
                                      - url
                                    type: object
                                  type: array
                                gitCredentialId:
                                  type: string
                                updatedAt:
                                  type: number
                                sourceless:
                                  type: boolean
                                productionBranch:
                                  type: string
                              required:
                                - name
                                - slug
                                - owner
                                - type
                                - uuid
                                - workspaceUuid
                                - gitCredentialId
                                - productionBranch
                                - deployHooks
                              type: object
                        microfrontends:
                          oneOf:
                            - properties:
                                isDefaultApp:
                                  type: boolean
                                updatedAt:
                                  type: number
                                  description: >-
                                    Timestamp when the microfrontends settings
                                    were last updated.
                                groupIds:
                                  items:
                                    oneOf:
                                      - type: string
                                      - type: string
                                  maxItems: 2
                                  minItems: 2
                                  type: array
                                  description: >-
                                    The group IDs of microfrontends that this
                                    project belongs to. Each microfrontend
                                    project must belong to a microfrontends
                                    group that is the set of microfrontends that
                                    are used together.
                                enabled:
                                  type: boolean
                                  description: >-
                                    Whether microfrontends are enabled for this
                                    project.
                                defaultRoute:
                                  type: string
                                  description: >-
                                    A path that is used to take screenshots and
                                    as the default path in preview links when a
                                    domain for this microfrontend is shown in
                                    the UI. Includes the leading slash, e.g.
                                    `/docs`
                              required:
                                - isDefaultApp
                                - updatedAt
                                - groupIds
                                - enabled
                              type: object
                            - properties:
                                isDefaultApp:
                                  type: boolean
                                routeObservabilityToThisProject:
                                  type: boolean
                                  description: >-
                                    Whether observability data should be routed
                                    to this microfrontend project or a root
                                    project.
                                doNotRouteWithMicrofrontendsRouting:
                                  type: boolean
                                  description: >-
                                    Whether to add microfrontends routing to
                                    aliases. This means domains in this project
                                    will route as a microfrontend.
                                updatedAt:
                                  type: number
                                  description: >-
                                    Timestamp when the microfrontends settings
                                    were last updated.
                                groupIds:
                                  items:
                                    oneOf:
                                      - type: string
                                      - type: string
                                  maxItems: 2
                                  minItems: 2
                                  type: array
                                  description: >-
                                    The group IDs of microfrontends that this
                                    project belongs to. Each microfrontend
                                    project must belong to a microfrontends
                                    group that is the set of microfrontends that
                                    are used together.
                                enabled:
                                  type: boolean
                                  description: >-
                                    Whether microfrontends are enabled for this
                                    project.
                                defaultRoute:
                                  type: string
                                  description: >-
                                    A path that is used to take screenshots and
                                    as the default path in preview links when a
                                    domain for this microfrontend is shown in
                                    the UI. Includes the leading slash, e.g.
                                    `/docs`
                              required:
                                - updatedAt
                                - groupIds
                                - enabled
                              type: object
                            - properties:
                                updatedAt:
                                  type: number
                                groupIds:
                                  items:
                                    oneOf: []
                                  maxItems: 0
                                  minItems: 0
                                  type: array
                                enabled:
                                  type: boolean
                              required:
                                - updatedAt
                                - groupIds
                                - enabled
                              type: object
                        name:
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
                        optionsAllowlist:
                          nullable: true
                          properties:
                            paths:
                              items:
                                properties:
                                  value:
                                    type: string
                                required:
                                  - value
                                type: object
                              type: array
                          required:
                            - paths
                          type: object
                        outputDirectory:
                          nullable: true
                          type: string
                        passwordProtection:
                          nullable: true
                          type: object
                        productionDeploymentsFastLane:
                          type: boolean
                        publicSource:
                          nullable: true
                          type: boolean
                        resourceConfig:
                          properties:
                            elasticConcurrencyEnabled:
                              type: boolean
                            fluid:
                              type: boolean
                            functionDefaultRegions:
                              items:
                                type: string
                              type: array
                            functionDefaultTimeout:
                              type: number
                            functionDefaultMemoryType:
                              type: string
                              enum:
                                - standard_legacy
                                - standard
                                - performance
                            functionZeroConfigFailover:
                              type: boolean
                            buildMachineType:
                              type: string
                              enum:
                                - enhanced
                                - turbo
                            isNSNBDisabled:
                              type: boolean
                          type: object
                          required:
                            - functionDefaultRegions
                        rollbackDescription:
                          properties:
                            userId:
                              type: string
                              description: The user who rolled back the project.
                            username:
                              type: string
                              description: >-
                                The username of the user who rolled back the
                                project.
                            description:
                              type: string
                              description: >-
                                User-supplied explanation of why they rolled
                                back the project. Limited to 250 characters.
                            createdAt:
                              type: number
                              description: Timestamp of when the rollback was requested.
                          required:
                            - userId
                            - username
                            - description
                            - createdAt
                          type: object
                          description: >-
                            Description of why a project was rolled back, and by
                            whom. Note that lastAliasRequest contains the
                            from/to details of the rollback.
                        rollingRelease:
                          nullable: true
                          properties:
                            target:
                              type: string
                              description: >-
                                The environment that the release targets,
                                currently only supports production. Adding in
                                case we want to configure with alias groups or
                                custom environments.
                              example: production
                            stages:
                              nullable: true
                              items:
                                properties:
                                  targetPercentage:
                                    type: number
                                    description: >-
                                      The percentage of traffic to serve to the
                                      canary deployment (0-100)
                                    example: 25
                                  requireApproval:
                                    type: boolean
                                    description: >-
                                      Whether or not this stage requires manual
                                      approval to proceed
                                    example: false
                                  duration:
                                    type: number
                                    description: >-
                                      Duration in minutes for automatic
                                      advancement to the next stage
                                    example: 600
                                  linearShift:
                                    type: boolean
                                    description: >-
                                      Whether to linearly shift traffic over the
                                      duration of this stage
                                    example: false
                                required:
                                  - targetPercentage
                                type: object
                                description: >-
                                  An array of all the stages required during a
                                  deployment release. Each stage defines a
                                  target percentage and advancement rules. The
                                  final stage must always have targetPercentage:
                                  100.
                              type: array
                              description: >-
                                An array of all the stages required during a
                                deployment release. Each stage defines a target
                                percentage and advancement rules. The final
                                stage must always have targetPercentage: 100.
                            canaryResponseHeader:
                              type: boolean
                              description: >-
                                Whether the request served by a canary
                                deployment should return a header indicating a
                                canary was served. Defaults to `false` when
                                omitted.
                              example: false
                          required:
                            - target
                          type: object
                          description: >-
                            Project-level rolling release configuration that
                            defines how deployments should be gradually rolled
                            out
                        defaultResourceConfig:
                          properties:
                            elasticConcurrencyEnabled:
                              type: boolean
                            fluid:
                              type: boolean
                            functionDefaultRegions:
                              items:
                                type: string
                              type: array
                            functionDefaultTimeout:
                              type: number
                            functionDefaultMemoryType:
                              type: string
                              enum:
                                - standard_legacy
                                - standard
                                - performance
                            functionZeroConfigFailover:
                              type: boolean
                            buildMachineType:
                              type: string
                              enum:
                                - enhanced
                                - turbo
                            isNSNBDisabled:
                              type: boolean
                          type: object
                          required:
                            - functionDefaultRegions
                        rootDirectory:
                          nullable: true
                          type: string
                        serverlessFunctionZeroConfigFailover:
                          type: boolean
                        skewProtectionBoundaryAt:
                          type: number
                        skewProtectionMaxAge:
                          type: number
                        skipGitConnectDuringLink:
                          type: boolean
                        sourceFilesOutsideRootDirectory:
                          type: boolean
                        enableAffectedProjectsDeployments:
                          type: boolean
                        ssoProtection:
                          nullable: true
                          properties:
                            deploymentType:
                              type: string
                              enum:
                                - preview
                                - all
                                - prod_deployment_urls_and_all_previews
                                - all_except_custom_domains
                          required:
                            - deploymentType
                          type: object
                        targets:
                          additionalProperties:
                            nullable: true
                            properties:
                              id:
                                type: string
                              alias:
                                items:
                                  type: string
                                type: array
                              aliasAssigned:
                                nullable: true
                                oneOf:
                                  - type: number
                                  - type: boolean
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
                              aliasFinal:
                                nullable: true
                                type: string
                              automaticAliases:
                                items:
                                  type: string
                                type: array
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
                              buildingAt:
                                type: number
                              builds:
                                items:
                                  properties:
                                    use:
                                      type: string
                                    src:
                                      type: string
                                    dest:
                                      type: string
                                  required:
                                    - use
                                  type: object
                                type: array
                              checksConclusion:
                                type: string
                                enum:
                                  - succeeded
                                  - failed
                                  - skipped
                                  - canceled
                              checksState:
                                type: string
                                enum:
                                  - registered
                                  - running
                                  - completed
                              connectBuildsEnabled:
                                type: boolean
                              connectConfigurationId:
                                type: string
                              createdAt:
                                type: number
                              createdIn:
                                type: string
                              creator:
                                nullable: true
                                properties:
                                  email:
                                    type: string
                                  githubLogin:
                                    type: string
                                  gitlabLogin:
                                    type: string
                                  uid:
                                    type: string
                                  username:
                                    type: string
                                required:
                                  - email
                                  - uid
                                  - username
                                type: object
                              deletedAt:
                                type: number
                              deploymentHostname:
                                type: string
                              forced:
                                type: boolean
                              name:
                                type: string
                              meta:
                                additionalProperties:
                                  type: string
                                type: object
                              monorepoManager:
                                nullable: true
                                type: string
                              oidcTokenClaims:
                                properties:
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
                              plan:
                                type: string
                                enum:
                                  - pro
                                  - enterprise
                                  - hobby
                              previewCommentsEnabled:
                                type: boolean
                                description: >-
                                  Whether or not preview comments are enabled
                                  for the deployment
                                example: false
                              private:
                                type: boolean
                              readyAt:
                                type: number
                              readyState:
                                type: string
                                enum:
                                  - BUILDING
                                  - ERROR
                                  - INITIALIZING
                                  - QUEUED
                                  - READY
                                  - CANCELED
                              readySubstate:
                                type: string
                                enum:
                                  - STAGED
                                  - ROLLING
                                  - PROMOTED
                              requestedAt:
                                type: number
                              target:
                                nullable: true
                                type: string
                              teamId:
                                nullable: true
                                type: string
                              type:
                                type: string
                                enum:
                                  - LAMBDAS
                              url:
                                type: string
                              userId:
                                type: string
                              withCache:
                                type: boolean
                            required:
                              - id
                              - createdAt
                              - createdIn
                              - creator
                              - deploymentHostname
                              - name
                              - plan
                              - private
                              - readyState
                              - type
                              - url
                              - userId
                            type: object
                          type: object
                        transferCompletedAt:
                          type: number
                        transferStartedAt:
                          type: number
                        transferToAccountId:
                          type: string
                        transferredFromAccountId:
                          type: string
                        updatedAt:
                          type: number
                        live:
                          type: boolean
                        enablePreviewFeedback:
                          nullable: true
                          type: boolean
                        enableProductionFeedback:
                          nullable: true
                          type: boolean
                        permissions:
                          properties:
                            oauth2Connection:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            user:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            userConnection:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            userSudo:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            webAuthn:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            accessGroup:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            agent:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            alerts:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            aliasGlobal:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            analyticsSampling:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            analyticsUsage:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            apiKey:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            apiKeyAiGateway:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            apiKeyOwnedBySelf:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            oauth2Application:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            vercelAppInstallation:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            vercelAppInstallationRequest:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            auditLog:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            billingAddress:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            billingInformation:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            billingInvoice:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            billingInvoiceEmailRecipient:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            billingInvoiceLanguage:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            billingPlan:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            billingPurchaseOrder:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            billingRefund:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            billingTaxId:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            blob:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            blobStoreTokenSet:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            budget:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            cacheArtifact:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            cacheArtifactUsageEvent:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            codeChecks:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            concurrentBuilds:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            connect:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            connectConfiguration:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            dataCacheBillingSettings:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            defaultDeploymentProtection:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            domain:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            domainAcceptDelegation:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            domainAuthCodes:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            domainCertificate:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            domainCheckConfig:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            domainMove:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            domainPurchase:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            domainRecord:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            domainTransferIn:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            drain:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            edgeConfig:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            edgeConfigItem:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            edgeConfigSchema:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            edgeConfigToken:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            endpointVerification:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            event:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            fileUpload:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            flagsExplorerSubscription:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            gitRepository:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            imageOptimizationNewPrice:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integration:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationAccount:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationConfiguration:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationConfigurationProjects:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationConfigurationRole:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationConfigurationTransfer:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationDeploymentAction:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationEvent:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationLog:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationResource:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationResourceReplCommand:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationResourceSecrets:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationSSOSession:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationStoreTokenSet:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationVercelConfigurationOverride:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            integrationPullRequest:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            ipBlocking:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            jobGlobal:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            logDrain:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            marketplaceBillingData:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            marketplaceExperimentationEdgeConfigData:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            marketplaceExperimentationItem:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            marketplaceInstallationMember:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            marketplaceInvoice:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            marketplaceSettings:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            Monitoring:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            monitoringAlert:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            monitoringChart:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            monitoringQuery:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            monitoringSettings:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            notificationCustomerBudget:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            notificationDeploymentFailed:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            notificationDomainConfiguration:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            notificationDomainExpire:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            notificationDomainMoved:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            notificationDomainPurchase:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            notificationDomainRenewal:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            notificationDomainTransfer:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            notificationDomainUnverified:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            NotificationMonitoringAlert:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            notificationPaymentFailed:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            notificationPreferences:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            notificationStatementOfReasons:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            notificationUsageAlert:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            observabilityConfiguration:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            observabilityFunnel:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            observabilityNotebook:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            openTelemetryEndpoint:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            ownEvent:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            passwordProtectionInvoiceItem:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            paymentMethod:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            permissions:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            postgres:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            postgresStoreTokenSet:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            previewDeploymentSuffix:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectTransferIn:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            proTrialOnboarding:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            rateLimit:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            redis:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            redisStoreTokenSet:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            remoteCaching:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            repository:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            samlConfig:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            secret:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            sensitiveEnvironmentVariablePolicy:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            sharedEnvVars:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            sharedEnvVarsProduction:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            space:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            spaceRun:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            storeTransfer:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            supportCase:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            supportCaseComment:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            team:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            teamAccessRequest:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            teamFellowMembership:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            teamGitExclusivity:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            teamInvite:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            teamInviteCode:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            teamJoin:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            teamMemberMfaStatus:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            teamMicrofrontends:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            teamOwnMembership:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            teamOwnMembershipDisconnectSAML:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            token:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            usage:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            usageCycle:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            vercelRun:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            vercelRunExec:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            vpcPeeringConnection:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            webAnalyticsPlan:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            webhook:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            webhook-event:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            aliasProject:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            aliasProtectionBypass:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            buildMachine:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            connectConfigurationLink:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            dataCacheNamespace:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            deployment:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            deploymentBuildLogs:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            deploymentCheck:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            deploymentCheckPreview:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            deploymentCheckReRunFromProductionBranch:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            deploymentProductionGit:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            deploymentV0:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            deploymentPreview:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            deploymentPrivate:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            deploymentPromote:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            deploymentRollback:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            edgeCacheNamespace:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            environments:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            job:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            logs:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            logsPreset:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            observabilityData:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            onDemandBuild:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            onDemandConcurrency:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            optionsAllowlist:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            passwordProtection:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            productionAliasProtectionBypass:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            project:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectAccessGroup:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectAnalyticsSampling:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectAnalyticsUsage:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectCheck:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectCheckRun:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectDeploymentExpiration:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectDeploymentHook:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectDomain:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectDomainCheckConfig:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectDomainMove:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectEnvVars:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectEnvVarsProduction:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectEnvVarsUnownedByIntegration:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectFlags:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectFromV0:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectId:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectIntegrationConfiguration:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectLink:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectMember:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectMonitoring:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectOIDCToken:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectPermissions:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectProductionBranch:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectProtectionBypass:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectRollingRelease:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectSupportCase:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectSupportCaseComment:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectTier:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectTransfer:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectTransferOut:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            projectUsage:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            seawallConfig:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            sharedEnvVarConnection:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            skewProtection:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            analytics:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            trustedIps:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            v0Chat:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                            webAnalytics:
                              items:
                                $ref: '#/components/schemas/ACLAction'
                              type: array
                          type: object
                        lastRollbackTarget:
                          nullable: true
                          type: object
                        lastAliasRequest:
                          nullable: true
                          properties:
                            fromDeploymentId:
                              type: string
                            toDeploymentId:
                              type: string
                            fromRollingReleaseId:
                              type: string
                              description: >-
                                If rolling back from a rolling release,
                                fromDeploymentId captures the "base" of that
                                rolling release, and fromRollingReleaseId
                                captures the "target" of that rolling release.
                            jobStatus:
                              type: string
                              enum:
                                - succeeded
                                - failed
                                - skipped
                                - pending
                                - in-progress
                            requestedAt:
                              type: number
                            type:
                              type: string
                              enum:
                                - promote
                                - rollback
                          required:
                            - fromDeploymentId
                            - toDeploymentId
                            - jobStatus
                            - requestedAt
                            - type
                          type: object
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
                                      - integration-automation-bypass
                                  integrationId:
                                    type: string
                                  configurationId:
                                    type: string
                                required:
                                  - createdAt
                                  - createdBy
                                  - scope
                                  - integrationId
                                  - configurationId
                                type: object
                              - properties:
                                  createdAt:
                                    type: number
                                  createdBy:
                                    type: string
                                  scope:
                                    type: string
                                    enum:
                                      - automation-bypass
                                required:
                                  - createdAt
                                  - createdBy
                                  - scope
                                type: object
                          type: object
                        hasActiveBranches:
                          type: boolean
                        trustedIps:
                          nullable: true
                          oneOf:
                            - properties:
                                deploymentType:
                                  type: string
                                  enum:
                                    - preview
                                    - production
                                    - all
                                    - prod_deployment_urls_and_all_previews
                                    - all_except_custom_domains
                                addresses:
                                  items:
                                    properties:
                                      value:
                                        type: string
                                      note:
                                        type: string
                                    required:
                                      - value
                                    type: object
                                  type: array
                                protectionMode:
                                  type: string
                                  enum:
                                    - additional
                                    - exclusive
                              required:
                                - deploymentType
                                - addresses
                                - protectionMode
                              type: object
                            - properties:
                                deploymentType:
                                  type: string
                                  enum:
                                    - preview
                                    - production
                                    - all
                                    - prod_deployment_urls_and_all_previews
                                    - all_except_custom_domains
                              required:
                                - deploymentType
                              type: object
                        gitComments:
                          properties:
                            onPullRequest:
                              type: boolean
                              description: Whether the Vercel bot should comment on PRs
                            onCommit:
                              type: boolean
                              description: Whether the Vercel bot should comment on commits
                          required:
                            - onPullRequest
                            - onCommit
                          type: object
                        gitProviderOptions:
                          properties:
                            createDeployments:
                              type: string
                              enum:
                                - enabled
                                - disabled
                              description: >-
                                Whether the Vercel bot should automatically
                                create GitHub deployments
                                https://docs.github.com/en/rest/deployments/deployments#about-deployments
                                NOTE: repository-dispatch events should be used
                                instead
                            disableRepositoryDispatchEvents:
                              type: boolean
                              description: >-
                                Whether the Vercel bot should not automatically
                                create GitHub repository-dispatch events on
                                deployment events.
                                https://vercel.com/docs/git/vercel-for-github#repository-dispatch-events
                            requireVerifiedCommits:
                              type: boolean
                              description: >-
                                Whether the project requires commits to be
                                signed before deployments will be created.
                          required:
                            - createDeployments
                          type: object
                        paused:
                          type: boolean
                        concurrencyBucketName:
                          type: string
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
                        security:
                          properties:
                            attackModeEnabled:
                              type: boolean
                            attackModeUpdatedAt:
                              type: number
                            firewallEnabled:
                              type: boolean
                            firewallUpdatedAt:
                              type: number
                            attackModeActiveUntil:
                              nullable: true
                              type: number
                            firewallConfigVersion:
                              type: number
                            firewallSeawallEnabled:
                              type: boolean
                            ja3Enabled:
                              type: boolean
                            ja4Enabled:
                              type: boolean
                            firewallBypassIps:
                              items:
                                type: string
                              type: array
                            managedRules:
                              nullable: true
                              properties:
                                bot_filter:
                                  properties:
                                    active:
                                      type: boolean
                                    action:
                                      type: string
                                      enum:
                                        - log
                                        - challenge
                                        - deny
                                  required:
                                    - active
                                  type: object
                                ai_bots:
                                  properties:
                                    active:
                                      type: boolean
                                    action:
                                      type: string
                                      enum:
                                        - log
                                        - challenge
                                        - deny
                                  required:
                                    - active
                                  type: object
                                owasp:
                                  properties:
                                    active:
                                      type: boolean
                                    action:
                                      type: string
                                      enum:
                                        - log
                                        - challenge
                                        - deny
                                  required:
                                    - active
                                  type: object
                              required:
                                - bot_filter
                                - ai_bots
                                - owasp
                              type: object
                            botIdEnabled:
                              type: boolean
                          type: object
                        oidcTokenConfig:
                          properties:
                            enabled:
                              type: boolean
                              description: >-
                                Whether or not to generate OpenID Connect JSON
                                Web Tokens.
                            issuerMode:
                              type: string
                              enum:
                                - team
                                - global
                              description: >-
                                - team: `https://oidc.vercel.com/[team_slug]` -
                                global: `https://oidc.vercel.com`
                          type: object
                        tier:
                          type: string
                          enum:
                            - standard
                            - advanced
                            - critical
                        features:
                          properties:
                            webAnalytics:
                              type: boolean
                          type: object
                        v0:
                          type: boolean
                        abuse:
                          properties:
                            scanner:
                              type: string
                            history:
                              items:
                                properties:
                                  scanner:
                                    type: string
                                  reason:
                                    type: string
                                  by:
                                    type: string
                                  byId:
                                    type: string
                                  at:
                                    type: number
                                required:
                                  - scanner
                                  - reason
                                  - by
                                  - byId
                                  - at
                                type: object
                              type: array
                            updatedAt:
                              type: number
                            block:
                              properties:
                                action:
                                  type: string
                                  enum:
                                    - blocked
                                reason:
                                  type: string
                                statusCode:
                                  type: number
                                createdAt:
                                  type: number
                                caseId:
                                  type: string
                                actor:
                                  type: string
                                comment:
                                  type: string
                                isCascading:
                                  type: boolean
                              required:
                                - action
                                - reason
                                - statusCode
                                - createdAt
                              type: object
                            blockHistory:
                              items:
                                oneOf:
                                  - properties:
                                      action:
                                        type: string
                                        enum:
                                          - blocked
                                      reason:
                                        type: string
                                      statusCode:
                                        type: number
                                      createdAt:
                                        type: number
                                      caseId:
                                        type: string
                                      actor:
                                        type: string
                                      comment:
                                        type: string
                                      isCascading:
                                        type: boolean
                                    required:
                                      - action
                                      - reason
                                      - statusCode
                                      - createdAt
                                    type: object
                                  - properties:
                                      action:
                                        type: string
                                        enum:
                                          - unblocked
                                      createdAt:
                                        type: number
                                      caseId:
                                        type: string
                                      actor:
                                        type: string
                                      comment:
                                        type: string
                                      isCascading:
                                        type: boolean
                                    required:
                                      - action
                                      - createdAt
                                    type: object
                                  - properties:
                                      action:
                                        type: string
                                        enum:
                                          - route-blocked
                                      route:
                                        oneOf:
                                          - properties:
                                              src:
                                                type: string
                                              status:
                                                type: number
                                            required:
                                              - src
                                              - status
                                            type: object
                                          - properties:
                                              has:
                                                items:
                                                  oneOf:
                                                    - properties:
                                                        type:
                                                          type: string
                                                          enum:
                                                            - header
                                                        key:
                                                          type: string
                                                          enum:
                                                            - x-vercel-ip-country
                                                        value:
                                                          properties:
                                                            eq:
                                                              type: string
                                                          required:
                                                            - eq
                                                          type: object
                                                      required:
                                                        - type
                                                        - key
                                                        - value
                                                      type: object
                                                    - properties:
                                                        type:
                                                          type: string
                                                          enum:
                                                            - host
                                                        value:
                                                          properties:
                                                            eq:
                                                              type: string
                                                          required:
                                                            - eq
                                                          type: object
                                                      required:
                                                        - type
                                                        - value
                                                      type: object
                                                type: array
                                              mitigate:
                                                properties:
                                                  action:
                                                    type: string
                                                    enum:
                                                      - block_legal_cwc
                                                required:
                                                  - action
                                                type: object
                                              src:
                                                type: string
                                            required:
                                              - has
                                              - mitigate
                                            type: object
                                      reason:
                                        type: string
                                      createdAt:
                                        type: number
                                      caseId:
                                        type: string
                                      actor:
                                        type: string
                                      comment:
                                        type: string
                                      isCascading:
                                        type: boolean
                                    required:
                                      - action
                                      - route
                                      - reason
                                      - createdAt
                                    type: object
                                  - properties:
                                      action:
                                        type: string
                                        enum:
                                          - route-unblocked
                                      route:
                                        oneOf:
                                          - properties:
                                              src:
                                                type: string
                                              status:
                                                type: number
                                            required:
                                              - src
                                              - status
                                            type: object
                                          - properties:
                                              has:
                                                items:
                                                  oneOf:
                                                    - properties:
                                                        type:
                                                          type: string
                                                          enum:
                                                            - header
                                                        key:
                                                          type: string
                                                          enum:
                                                            - x-vercel-ip-country
                                                        value:
                                                          properties:
                                                            eq:
                                                              type: string
                                                          required:
                                                            - eq
                                                          type: object
                                                      required:
                                                        - type
                                                        - key
                                                        - value
                                                      type: object
                                                    - properties:
                                                        type:
                                                          type: string
                                                          enum:
                                                            - host
                                                        value:
                                                          properties:
                                                            eq:
                                                              type: string
                                                          required:
                                                            - eq
                                                          type: object
                                                      required:
                                                        - type
                                                        - value
                                                      type: object
                                                type: array
                                              mitigate:
                                                properties:
                                                  action:
                                                    type: string
                                                    enum:
                                                      - block_legal_cwc
                                                required:
                                                  - action
                                                type: object
                                              src:
                                                type: string
                                            required:
                                              - has
                                              - mitigate
                                            type: object
                                      statusCode:
                                        type: number
                                      createdAt:
                                        type: number
                                      caseId:
                                        type: string
                                      actor:
                                        type: string
                                      comment:
                                        type: string
                                      isCascading:
                                        type: boolean
                                    required:
                                      - action
                                      - route
                                      - createdAt
                                    type: object
                              type: array
                            interstitial:
                              type: boolean
                            interstitialHistory:
                              items:
                                properties:
                                  action:
                                    type: string
                                    enum:
                                      - add-interstitial
                                      - remove-interstitial
                                  createdAt:
                                    type: number
                                  caseId:
                                    type: string
                                  reason:
                                    type: string
                                  actor:
                                    type: string
                                  comment:
                                    type: string
                                required:
                                  - action
                                  - createdAt
                                type: object
                              type: array
                          required:
                            - history
                            - updatedAt
                          type: object
                        internalRoutes:
                          items:
                            oneOf:
                              - properties:
                                  src:
                                    type: string
                                  status:
                                    type: number
                                required:
                                  - src
                                  - status
                                type: object
                              - properties:
                                  has:
                                    items:
                                      oneOf:
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - header
                                            key:
                                              type: string
                                              enum:
                                                - x-vercel-ip-country
                                            value:
                                              properties:
                                                eq:
                                                  type: string
                                              required:
                                                - eq
                                              type: object
                                          required:
                                            - type
                                            - key
                                            - value
                                          type: object
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - host
                                            value:
                                              properties:
                                                eq:
                                                  type: string
                                              required:
                                                - eq
                                              type: object
                                          required:
                                            - type
                                            - value
                                          type: object
                                    type: array
                                  mitigate:
                                    properties:
                                      action:
                                        type: string
                                        enum:
                                          - block_legal_cwc
                                    required:
                                      - action
                                    type: object
                                  src:
                                    type: string
                                required:
                                  - has
                                  - mitigate
                                type: object
                          type: array
                      required:
                        - accountId
                        - directoryListing
                        - id
                        - name
                        - nodeVersion
                        - resourceConfig
                        - defaultResourceConfig
                      type: object
                    type: array
              pagination:
                allOf:
                  - oneOf:
                      - properties:
                          count:
                            type: number
                            description: Amount of items in the current page.
                            example: 20
                          next:
                            nullable: true
                            type: string
                            description: >-
                              Continuation token that must be used to request
                              the next page. Base32 encoded for safe URL
                              transmission.
                            example: JBSWY3DPEHPK3PXP
                        required:
                          - count
                          - next
                        type: object
                        description: >-
                          This object contains information related to the
                          pagination of the current request using continuation
                          tokens. Since CosmosDB doesn't support going to
                          previous pages, only count and next are provided.
                      - $ref: '#/components/schemas/Pagination'
            description: The paginated list of projects
            requiredProperties:
              - projects
              - pagination
        examples:
          example:
            value:
              projects:
                - accountId: <string>
                  analytics:
                    id: <string>
                    canceledAt: 123
                    disabledAt: 123
                    enabledAt: 123
                    paidAt: 123
                    sampleRatePercent: 123
                    spendLimitInDollars: 123
                  speedInsights:
                    id: <string>
                    enabledAt: 123
                    disabledAt: 123
                    canceledAt: 123
                    hasData: true
                    paidAt: 123
                  autoExposeSystemEnvs: true
                  autoAssignCustomDomains: true
                  autoAssignCustomDomainsUpdatedBy: <string>
                  buildCommand: <string>
                  commandForIgnoringBuildStep: <string>
                  connectConfigurations:
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
                  connectConfigurationId: <string>
                  connectBuildsEnabled: true
                  passiveConnectConfigurationId: <string>
                  createdAt: 123
                  customerSupportCodeVisibility: true
                  crons:
                    enabledAt: 123
                    disabledAt: 123
                    updatedAt: 123
                    deploymentId: <string>
                    definitions:
                      - host: vercel.com
                        path: /api/crons/sync-something?hello=world
                        schedule: 0 0 * * *
                  dataCache:
                    userDisabled: true
                    storageSizeBytes: 123
                    unlimited: true
                  deploymentExpiration:
                    expirationDays: 123
                    expirationDaysProduction: 123
                    expirationDaysCanceled: 123
                    expirationDaysErrored: 123
                    deploymentsToKeep: 123
                  devCommand: <string>
                  directoryListing: true
                  installCommand: <string>
                  env:
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
                  customEnvironments:
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
                  framework: blitzjs
                  gitForkProtection: true
                  gitLFS: true
                  id: <string>
                  ipBuckets:
                    - bucket: <string>
                      supportUntil: 123
                  latestDeployments:
                    - id: <string>
                      alias:
                        - <string>
                      aliasAssigned: 123
                      aliasError:
                        code: <string>
                        message: <string>
                      aliasFinal: <string>
                      automaticAliases:
                        - <string>
                      branchMatcher:
                        type: endsWith
                        pattern: <string>
                      buildingAt: 123
                      builds:
                        - use: <string>
                          src: <string>
                          dest: <string>
                      checksConclusion: succeeded
                      checksState: registered
                      connectBuildsEnabled: true
                      connectConfigurationId: <string>
                      createdAt: 123
                      createdIn: <string>
                      creator:
                        email: <string>
                        githubLogin: <string>
                        gitlabLogin: <string>
                        uid: <string>
                        username: <string>
                      deletedAt: 123
                      deploymentHostname: <string>
                      forced: true
                      name: <string>
                      meta: {}
                      monorepoManager: <string>
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
                      plan: pro
                      previewCommentsEnabled: false
                      private: true
                      readyAt: 123
                      readyState: BUILDING
                      readySubstate: STAGED
                      requestedAt: 123
                      target: <string>
                      teamId: <string>
                      type: LAMBDAS
                      url: <string>
                      userId: <string>
                      withCache: true
                  link:
                    org: <string>
                    repoOwnerId: 123
                    repo: <string>
                    repoId: 123
                    type: github
                    createdAt: 123
                    deployHooks:
                      - createdAt: 123
                        id: <string>
                        name: <string>
                        ref: <string>
                        url: <string>
                    gitCredentialId: <string>
                    updatedAt: 123
                    sourceless: true
                    productionBranch: <string>
                  microfrontends:
                    isDefaultApp: true
                    updatedAt: 123
                    groupIds:
                      - <string>
                    enabled: true
                    defaultRoute: <string>
                  name: <string>
                  nodeVersion: 22.x
                  optionsAllowlist:
                    paths:
                      - value: <string>
                  outputDirectory: <string>
                  passwordProtection: {}
                  productionDeploymentsFastLane: true
                  publicSource: true
                  resourceConfig:
                    elasticConcurrencyEnabled: true
                    fluid: true
                    functionDefaultRegions:
                      - <string>
                    functionDefaultTimeout: 123
                    functionDefaultMemoryType: standard_legacy
                    functionZeroConfigFailover: true
                    buildMachineType: enhanced
                    isNSNBDisabled: true
                  rollbackDescription:
                    userId: <string>
                    username: <string>
                    description: <string>
                    createdAt: 123
                  rollingRelease:
                    target: production
                    stages:
                      - targetPercentage: 25
                        requireApproval: false
                        duration: 600
                        linearShift: false
                    canaryResponseHeader: false
                  defaultResourceConfig:
                    elasticConcurrencyEnabled: true
                    fluid: true
                    functionDefaultRegions:
                      - <string>
                    functionDefaultTimeout: 123
                    functionDefaultMemoryType: standard_legacy
                    functionZeroConfigFailover: true
                    buildMachineType: enhanced
                    isNSNBDisabled: true
                  rootDirectory: <string>
                  serverlessFunctionZeroConfigFailover: true
                  skewProtectionBoundaryAt: 123
                  skewProtectionMaxAge: 123
                  skipGitConnectDuringLink: true
                  sourceFilesOutsideRootDirectory: true
                  enableAffectedProjectsDeployments: true
                  ssoProtection:
                    deploymentType: preview
                  targets: {}
                  transferCompletedAt: 123
                  transferStartedAt: 123
                  transferToAccountId: <string>
                  transferredFromAccountId: <string>
                  updatedAt: 123
                  live: true
                  enablePreviewFeedback: true
                  enableProductionFeedback: true
                  permissions:
                    oauth2Connection:
                      - create
                    user:
                      - create
                    userConnection:
                      - create
                    userSudo:
                      - create
                    webAuthn:
                      - create
                    accessGroup:
                      - create
                    agent:
                      - create
                    alerts:
                      - create
                    aliasGlobal:
                      - create
                    analyticsSampling:
                      - create
                    analyticsUsage:
                      - create
                    apiKey:
                      - create
                    apiKeyAiGateway:
                      - create
                    apiKeyOwnedBySelf:
                      - create
                    oauth2Application:
                      - create
                    vercelAppInstallation:
                      - create
                    vercelAppInstallationRequest:
                      - create
                    auditLog:
                      - create
                    billingAddress:
                      - create
                    billingInformation:
                      - create
                    billingInvoice:
                      - create
                    billingInvoiceEmailRecipient:
                      - create
                    billingInvoiceLanguage:
                      - create
                    billingPlan:
                      - create
                    billingPurchaseOrder:
                      - create
                    billingRefund:
                      - create
                    billingTaxId:
                      - create
                    blob:
                      - create
                    blobStoreTokenSet:
                      - create
                    budget:
                      - create
                    cacheArtifact:
                      - create
                    cacheArtifactUsageEvent:
                      - create
                    codeChecks:
                      - create
                    concurrentBuilds:
                      - create
                    connect:
                      - create
                    connectConfiguration:
                      - create
                    dataCacheBillingSettings:
                      - create
                    defaultDeploymentProtection:
                      - create
                    domain:
                      - create
                    domainAcceptDelegation:
                      - create
                    domainAuthCodes:
                      - create
                    domainCertificate:
                      - create
                    domainCheckConfig:
                      - create
                    domainMove:
                      - create
                    domainPurchase:
                      - create
                    domainRecord:
                      - create
                    domainTransferIn:
                      - create
                    drain:
                      - create
                    edgeConfig:
                      - create
                    edgeConfigItem:
                      - create
                    edgeConfigSchema:
                      - create
                    edgeConfigToken:
                      - create
                    endpointVerification:
                      - create
                    event:
                      - create
                    fileUpload:
                      - create
                    flagsExplorerSubscription:
                      - create
                    gitRepository:
                      - create
                    imageOptimizationNewPrice:
                      - create
                    integration:
                      - create
                    integrationAccount:
                      - create
                    integrationConfiguration:
                      - create
                    integrationConfigurationProjects:
                      - create
                    integrationConfigurationRole:
                      - create
                    integrationConfigurationTransfer:
                      - create
                    integrationDeploymentAction:
                      - create
                    integrationEvent:
                      - create
                    integrationLog:
                      - create
                    integrationResource:
                      - create
                    integrationResourceReplCommand:
                      - create
                    integrationResourceSecrets:
                      - create
                    integrationSSOSession:
                      - create
                    integrationStoreTokenSet:
                      - create
                    integrationVercelConfigurationOverride:
                      - create
                    integrationPullRequest:
                      - create
                    ipBlocking:
                      - create
                    jobGlobal:
                      - create
                    logDrain:
                      - create
                    marketplaceBillingData:
                      - create
                    marketplaceExperimentationEdgeConfigData:
                      - create
                    marketplaceExperimentationItem:
                      - create
                    marketplaceInstallationMember:
                      - create
                    marketplaceInvoice:
                      - create
                    marketplaceSettings:
                      - create
                    Monitoring:
                      - create
                    monitoringAlert:
                      - create
                    monitoringChart:
                      - create
                    monitoringQuery:
                      - create
                    monitoringSettings:
                      - create
                    notificationCustomerBudget:
                      - create
                    notificationDeploymentFailed:
                      - create
                    notificationDomainConfiguration:
                      - create
                    notificationDomainExpire:
                      - create
                    notificationDomainMoved:
                      - create
                    notificationDomainPurchase:
                      - create
                    notificationDomainRenewal:
                      - create
                    notificationDomainTransfer:
                      - create
                    notificationDomainUnverified:
                      - create
                    NotificationMonitoringAlert:
                      - create
                    notificationPaymentFailed:
                      - create
                    notificationPreferences:
                      - create
                    notificationStatementOfReasons:
                      - create
                    notificationUsageAlert:
                      - create
                    observabilityConfiguration:
                      - create
                    observabilityFunnel:
                      - create
                    observabilityNotebook:
                      - create
                    openTelemetryEndpoint:
                      - create
                    ownEvent:
                      - create
                    passwordProtectionInvoiceItem:
                      - create
                    paymentMethod:
                      - create
                    permissions:
                      - create
                    postgres:
                      - create
                    postgresStoreTokenSet:
                      - create
                    previewDeploymentSuffix:
                      - create
                    projectTransferIn:
                      - create
                    proTrialOnboarding:
                      - create
                    rateLimit:
                      - create
                    redis:
                      - create
                    redisStoreTokenSet:
                      - create
                    remoteCaching:
                      - create
                    repository:
                      - create
                    samlConfig:
                      - create
                    secret:
                      - create
                    sensitiveEnvironmentVariablePolicy:
                      - create
                    sharedEnvVars:
                      - create
                    sharedEnvVarsProduction:
                      - create
                    space:
                      - create
                    spaceRun:
                      - create
                    storeTransfer:
                      - create
                    supportCase:
                      - create
                    supportCaseComment:
                      - create
                    team:
                      - create
                    teamAccessRequest:
                      - create
                    teamFellowMembership:
                      - create
                    teamGitExclusivity:
                      - create
                    teamInvite:
                      - create
                    teamInviteCode:
                      - create
                    teamJoin:
                      - create
                    teamMemberMfaStatus:
                      - create
                    teamMicrofrontends:
                      - create
                    teamOwnMembership:
                      - create
                    teamOwnMembershipDisconnectSAML:
                      - create
                    token:
                      - create
                    usage:
                      - create
                    usageCycle:
                      - create
                    vercelRun:
                      - create
                    vercelRunExec:
                      - create
                    vpcPeeringConnection:
                      - create
                    webAnalyticsPlan:
                      - create
                    webhook:
                      - create
                    webhook-event:
                      - create
                    aliasProject:
                      - create
                    aliasProtectionBypass:
                      - create
                    buildMachine:
                      - create
                    connectConfigurationLink:
                      - create
                    dataCacheNamespace:
                      - create
                    deployment:
                      - create
                    deploymentBuildLogs:
                      - create
                    deploymentCheck:
                      - create
                    deploymentCheckPreview:
                      - create
                    deploymentCheckReRunFromProductionBranch:
                      - create
                    deploymentProductionGit:
                      - create
                    deploymentV0:
                      - create
                    deploymentPreview:
                      - create
                    deploymentPrivate:
                      - create
                    deploymentPromote:
                      - create
                    deploymentRollback:
                      - create
                    edgeCacheNamespace:
                      - create
                    environments:
                      - create
                    job:
                      - create
                    logs:
                      - create
                    logsPreset:
                      - create
                    observabilityData:
                      - create
                    onDemandBuild:
                      - create
                    onDemandConcurrency:
                      - create
                    optionsAllowlist:
                      - create
                    passwordProtection:
                      - create
                    productionAliasProtectionBypass:
                      - create
                    project:
                      - create
                    projectAccessGroup:
                      - create
                    projectAnalyticsSampling:
                      - create
                    projectAnalyticsUsage:
                      - create
                    projectCheck:
                      - create
                    projectCheckRun:
                      - create
                    projectDeploymentExpiration:
                      - create
                    projectDeploymentHook:
                      - create
                    projectDomain:
                      - create
                    projectDomainCheckConfig:
                      - create
                    projectDomainMove:
                      - create
                    projectEnvVars:
                      - create
                    projectEnvVarsProduction:
                      - create
                    projectEnvVarsUnownedByIntegration:
                      - create
                    projectFlags:
                      - create
                    projectFromV0:
                      - create
                    projectId:
                      - create
                    projectIntegrationConfiguration:
                      - create
                    projectLink:
                      - create
                    projectMember:
                      - create
                    projectMonitoring:
                      - create
                    projectOIDCToken:
                      - create
                    projectPermissions:
                      - create
                    projectProductionBranch:
                      - create
                    projectProtectionBypass:
                      - create
                    projectRollingRelease:
                      - create
                    projectSupportCase:
                      - create
                    projectSupportCaseComment:
                      - create
                    projectTier:
                      - create
                    projectTransfer:
                      - create
                    projectTransferOut:
                      - create
                    projectUsage:
                      - create
                    seawallConfig:
                      - create
                    sharedEnvVarConnection:
                      - create
                    skewProtection:
                      - create
                    analytics:
                      - create
                    trustedIps:
                      - create
                    v0Chat:
                      - create
                    webAnalytics:
                      - create
                  lastRollbackTarget: {}
                  lastAliasRequest:
                    fromDeploymentId: <string>
                    toDeploymentId: <string>
                    fromRollingReleaseId: <string>
                    jobStatus: succeeded
                    requestedAt: 123
                    type: promote
                  protectionBypass: {}
                  hasActiveBranches: true
                  trustedIps:
                    deploymentType: preview
                    addresses:
                      - value: <string>
                        note: <string>
                    protectionMode: additional
                  gitComments:
                    onPullRequest: true
                    onCommit: true
                  gitProviderOptions:
                    createDeployments: enabled
                    disableRepositoryDispatchEvents: true
                    requireVerifiedCommits: true
                  paused: true
                  concurrencyBucketName: <string>
                  webAnalytics:
                    id: <string>
                    disabledAt: 123
                    canceledAt: 123
                    enabledAt: 123
                    hasData: true
                  security:
                    attackModeEnabled: true
                    attackModeUpdatedAt: 123
                    firewallEnabled: true
                    firewallUpdatedAt: 123
                    attackModeActiveUntil: 123
                    firewallConfigVersion: 123
                    firewallSeawallEnabled: true
                    ja3Enabled: true
                    ja4Enabled: true
                    firewallBypassIps:
                      - <string>
                    managedRules:
                      bot_filter:
                        active: true
                        action: log
                      ai_bots:
                        active: true
                        action: log
                      owasp:
                        active: true
                        action: log
                    botIdEnabled: true
                  oidcTokenConfig:
                    enabled: true
                    issuerMode: team
                  tier: standard
                  features:
                    webAnalytics: true
                  v0: true
                  abuse:
                    scanner: <string>
                    history:
                      - scanner: <string>
                        reason: <string>
                        by: <string>
                        byId: <string>
                        at: 123
                    updatedAt: 123
                    block:
                      action: blocked
                      reason: <string>
                      statusCode: 123
                      createdAt: 123
                      caseId: <string>
                      actor: <string>
                      comment: <string>
                      isCascading: true
                    blockHistory:
                      - action: blocked
                        reason: <string>
                        statusCode: 123
                        createdAt: 123
                        caseId: <string>
                        actor: <string>
                        comment: <string>
                        isCascading: true
                    interstitial: true
                    interstitialHistory:
                      - action: add-interstitial
                        createdAt: 123
                        caseId: <string>
                        reason: <string>
                        actor: <string>
                        comment: <string>
                  internalRoutes:
                    - src: <string>
                      status: 123
              pagination:
                count: 20
                next: JBSWY3DPEHPK3PXP
        description: The paginated list of projects
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
    ACLAction:
      type: string
      enum:
        - create
        - delete
        - read
        - update
        - list
      description: >-
        Enum containing the actions that can be performed against a resource.
        Group operations are included.
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
title: "Retrieve project domains by project by id or name"

last_updated: "2025-11-07T00:37:14.540Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/retrieve-project-domains-by-project-by-id-or-name"
--------------------------------------------------------------------------------

# Retrieve project domains by project by id or name

> Retrieve the domains associated with a given project by passing either the project `id` or `name` in the URL.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v9/projects/{idOrName}/domains
paths:
  path: /v9/projects/{idOrName}/domains
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
        production:
          schema:
            - type: enum<string>
              enum:
                - 'true'
                - 'false'
              required: false
              description: Filters only production domains when set to `true`.
              default: 'false'
        target:
          schema:
            - type: enum<string>
              enum:
                - production
                - preview
              required: false
              description: >-
                Filters on the target of the domain. Can be either
                \"production\", \"preview\"
        customEnvironmentId:
          schema:
            - type: string
              required: false
              description: The unique custom environment identifier within the project
              example: env_123abc4567
        gitBranch:
          schema:
            - type: string
              required: false
              description: Filters domains based on specific branch.
        redirects:
          schema:
            - type: enum<string>
              enum:
                - 'true'
                - 'false'
              required: false
              description: >-
                Excludes redirect project domains when \"false\". Includes
                redirect project domains when \"true\" (default).
              default: 'true'
        redirect:
          schema:
            - type: string
              required: false
              description: Filters domains based on their redirect target.
              example: example.com
        verified:
          schema:
            - type: enum<string>
              enum:
                - 'true'
                - 'false'
              required: false
              description: Filters domains based on their verification status.
        limit:
          schema:
            - type: number
              required: false
              description: Maximum number of domains to list from a request (max 100).
              example: 20
        since:
          schema:
            - type: number
              required: false
              description: Get domains created after this JavaScript timestamp.
              example: 1609499532000
        until:
          schema:
            - type: number
              required: false
              description: Get domains created before this JavaScript timestamp.
              example: 1612264332000
        order:
          schema:
            - type: enum<string>
              enum:
                - ASC
                - DESC
              required: false
              description: Domains sort order by createdAt
              default: DESC
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
      - label: getProjectDomains
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.getProjectDomains({
              idOrName: "<value>",
              customEnvironmentId: "env_123abc4567",
              redirect: "example.com",
              limit: 20,
              since: 1609499532000,
              until: 1612264332000,
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
                    type: array
              pagination:
                allOf:
                  - properties:
                      count:
                        type: number
                      next:
                        nullable: true
                        type: number
                      prev:
                        nullable: true
                        type: number
                    required:
                      - count
                      - next
                      - prev
                    type: object
            requiredProperties:
              - domains
              - pagination
          - type: object
            properties:
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
                    type: array
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            requiredProperties:
              - domains
              - pagination
        examples:
          example:
            value:
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
              pagination:
                count: 123
                next: 123
                prev: 123
        description: Successful response retrieving a list of domains
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
title: "Retrieve the decrypted value of an environment variable of a project by id"

last_updated: "2025-11-07T00:37:14.605Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/retrieve-the-decrypted-value-of-an-environment-variable-of-a-project-by-id"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./30-remove-an-environment-variable.md) | [Index](./index.md) | [Next →](./32-retrieve-the-decrypted-value-of-an-environment-var.md)
