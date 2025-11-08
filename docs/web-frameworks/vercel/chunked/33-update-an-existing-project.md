**Navigation:** [← Previous](./32-retrieve-the-decrypted-value-of-an-environment-var.md) | [Index](./index.md) | [Next →](./34-update-the-data-cache-feature.md)

---

# Update an existing project

> Update the fields of a project using either its `name` or `id`.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v9/projects/{idOrName}
paths:
  path: /v9/projects/{idOrName}
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              autoExposeSystemEnvs:
                allOf:
                  - type: boolean
              autoAssignCustomDomains:
                allOf:
                  - type: boolean
              autoAssignCustomDomainsUpdatedBy:
                allOf:
                  - type: string
              buildCommand:
                allOf:
                  - description: >-
                      The build command for this project. When `null` is used
                      this value will be automatically detected
                    maxLength: 256
                    type: string
                    nullable: true
              commandForIgnoringBuildStep:
                allOf:
                  - maxLength: 256
                    type: string
                    nullable: true
              customerSupportCodeVisibility:
                allOf:
                  - description: >-
                      Specifies whether customer support can see git source for
                      a deployment
                    type: boolean
              devCommand:
                allOf:
                  - description: >-
                      The dev command for this project. When `null` is used this
                      value will be automatically detected
                    maxLength: 256
                    type: string
                    nullable: true
              directoryListing:
                allOf:
                  - type: boolean
              framework:
                allOf:
                  - description: >-
                      The framework that is being used for this project. When
                      `null` is used no framework is selected
                    enum:
                      - null
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
                    type: string
                    nullable: true
              gitForkProtection:
                allOf:
                  - description: >-
                      Specifies whether PRs from Git forks should require a team
                      member's authorization before it can be deployed
                    type: boolean
              gitLFS:
                allOf:
                  - description: Specifies whether Git LFS is enabled for this project.
                    type: boolean
              installCommand:
                allOf:
                  - description: >-
                      The install command for this project. When `null` is used
                      this value will be automatically detected
                    maxLength: 256
                    type: string
                    nullable: true
              name:
                allOf:
                  - description: The desired name for the project
                    example: a-project-name
                    type: string
                    maxLength: 100
              nodeVersion:
                allOf:
                  - enum:
                      - 22.x
                      - 20.x
                      - 18.x
                      - 16.x
                      - 14.x
                      - 12.x
                      - 10.x
                    type: string
              outputDirectory:
                allOf:
                  - description: >-
                      The output directory of the project. When `null` is used
                      this value will be automatically detected
                    maxLength: 256
                    type: string
                    nullable: true
              previewDeploymentsDisabled:
                allOf:
                  - description: >-
                      Specifies whether preview deployments are disabled for
                      this project.
                    type: boolean
                    nullable: true
              publicSource:
                allOf:
                  - description: >-
                      Specifies whether the source code and logs of the
                      deployments for this project should be public or not
                    type: boolean
                    nullable: true
              resourceConfig:
                allOf:
                  - properties:
                      buildMachineType:
                        enum:
                          - null
                          - enhanced
                          - turbo
                      fluid:
                        type: boolean
                      functionDefaultRegions:
                        description: >-
                          The regions to deploy Vercel Functions to for this
                          project
                        type: array
                        minItems: 1
                        uniqueItems: true
                        items:
                          type: string
                          maxLength: 4
                      functionDefaultTimeout:
                        type: number
                        maximum: 900
                        minimum: 1
                      functionDefaultMemoryType:
                        enum:
                          - standard_legacy
                          - standard
                          - performance
                      functionZeroConfigFailover:
                        description: >-
                          Specifies whether Zero Config Failover is enabled for
                          this project.
                        oneOf:
                          - type: boolean
                      elasticConcurrencyEnabled:
                        type: boolean
                      isNSNBDisabled:
                        type: boolean
                    type: object
                    description: Specifies resource override configuration for the project
                    additionalProperties: false
              rootDirectory:
                allOf:
                  - description: >-
                      The name of a directory or relative path to the source
                      code of your project. When `null` is used it will default
                      to the project root
                    maxLength: 256
                    type: string
                    nullable: true
              serverlessFunctionRegion:
                allOf:
                  - description: The region to deploy Serverless Functions in this project
                    maxLength: 4
                    type: string
                    nullable: true
              serverlessFunctionZeroConfigFailover:
                allOf:
                  - description: >-
                      Specifies whether Zero Config Failover is enabled for this
                      project.
                    oneOf:
                      - type: boolean
              skewProtectionBoundaryAt:
                allOf:
                  - description: >-
                      Deployments created before this absolute datetime have
                      Skew Protection disabled. Value is in milliseconds since
                      epoch to match \"createdAt\" fields.
                    minimum: 0
                    type: integer
              skewProtectionMaxAge:
                allOf:
                  - description: >-
                      Deployments created before this rolling window have Skew
                      Protection disabled. Value is in seconds to match
                      \"revalidate\" fields.
                    minimum: 0
                    type: integer
              skipGitConnectDuringLink:
                allOf:
                  - description: >-
                      Opts-out of the message prompting a CLI user to connect a
                      Git repository in `vercel link`.
                    type: boolean
                    deprecated: true
              sourceFilesOutsideRootDirectory:
                allOf:
                  - description: >-
                      Indicates if there are source files outside of the root
                      directory
                    type: boolean
              enablePreviewFeedback:
                allOf:
                  - description: Opt-in to preview toolbar on the project level
                    type: boolean
                    nullable: true
              enableProductionFeedback:
                allOf:
                  - description: Opt-in to production toolbar on the project level
                    type: boolean
                    nullable: true
              enableAffectedProjectsDeployments:
                allOf:
                  - description: >-
                      Opt-in to skip deployments when there are no changes to
                      the root directory and its dependencies
                    type: boolean
              staticIps:
                allOf:
                  - additionalProperties: false
                    description: Manage Static IPs for this project
                    properties:
                      enabled:
                        description: Opt-in to Static IPs for this project
                        type: boolean
                    required:
                      - enabled
                    type: object
              oidcTokenConfig:
                allOf:
                  - description: OpenID Connect JSON Web Token generation configuration.
                    type: object
                    additionalProperties: false
                    properties:
                      enabled:
                        description: >-
                          Whether or not to generate OpenID Connect JSON Web
                          Tokens.
                        deprecated: true
                        type: boolean
                        default: true
                      issuerMode:
                        description: >-
                          team: `https://oidc.vercel.com/[team_slug]` global:
                          `https://oidc.vercel.com`
                        type: string
                        enum:
                          - team
                          - global
                        default: team
              passwordProtection:
                allOf:
                  - additionalProperties: false
                    description: Allows to protect project deployments with a password
                    properties:
                      deploymentType:
                        description: >-
                          Specify if the password will apply to every Deployment
                          Target or just Preview
                        enum:
                          - all
                          - preview
                          - prod_deployment_urls_and_all_previews
                          - all_except_custom_domains
                        type: string
                      password:
                        description: >-
                          The password that will be used to protect Project
                          Deployments
                        maxLength: 72
                        type: string
                        nullable: true
                    required:
                      - deploymentType
                    type: object
                    nullable: true
              ssoProtection:
                allOf:
                  - additionalProperties: false
                    description: >-
                      Ensures visitors to your Preview Deployments are logged
                      into Vercel and have a minimum of Viewer access on your
                      team
                    properties:
                      deploymentType:
                        default: preview
                        description: >-
                          Specify if the Vercel Authentication (SSO Protection)
                          will apply to every Deployment Target or just Preview
                        enum:
                          - all
                          - preview
                          - prod_deployment_urls_and_all_previews
                          - all_except_custom_domains
                        type: string
                    required:
                      - deploymentType
                    type: object
                    nullable: true
              trustedIps:
                allOf:
                  - additionalProperties: false
                    description: >-
                      Restricts access to deployments based on the incoming
                      request IP address
                    properties:
                      deploymentType:
                        description: >-
                          Specify if the Trusted IPs will apply to every
                          Deployment Target or just Preview
                        enum:
                          - all
                          - preview
                          - production
                          - prod_deployment_urls_and_all_previews
                          - all_except_custom_domains
                        type: string
                      addresses:
                        type: array
                        items:
                          type: object
                          properties:
                            value:
                              type: string
                              description: >-
                                The IP addresses that are allowlisted. Supports
                                IPv4 addresses and CIDR notations. IPv6 is not
                                supported
                            note:
                              type: string
                              description: >-
                                An optional note explaining what the IP address
                                or subnet is used for
                              maxLength: 20
                          required:
                            - value
                          additionalProperties: false
                        minItems: 1
                      protectionMode:
                        description: >-
                          exclusive: ip match is enough to bypass deployment
                          protection (regardless of other settings). additional:
                          ip must match + any other protection should be also
                          provided (password, vercel auth, shareable link,
                          automation bypass header, automation bypass query
                          param)
                        enum:
                          - exclusive
                          - additional
                        type: string
                    required:
                      - deploymentType
                      - addresses
                      - protectionMode
                    type: object
                    nullable: true
              optionsAllowlist:
                allOf:
                  - additionalProperties: false
                    description: >-
                      Specify a list of paths that should not be protected by
                      Deployment Protection to enable Cors preflight requests
                    properties:
                      paths:
                        type: array
                        items:
                          type: object
                          properties:
                            value:
                              type: string
                              description: >-
                                The regex path that should not be protected by
                                Deployment Protection
                              pattern: ^/.*
                          required:
                            - value
                          additionalProperties: false
                        minItems: 1
                        maxItems: 5
                    required:
                      - paths
                    type: object
                    nullable: true
              connectConfigurations:
                allOf:
                  - type: array
                    description: >-
                      The list of connections from project environment to Secure
                      Compute network
                    items:
                      additionalProperties: false
                      properties:
                        envId:
                          type: string
                          description: The ID of the environment
                        connectConfigurationId:
                          type: string
                          description: The ID of the Secure Compute network
                        passive:
                          type: boolean
                          description: >-
                            Whether the configuration should be passive, meaning
                            builds will not run there and only passive
                            Serverless Functions will be deployed
                        buildsEnabled:
                          type: boolean
                          description: >-
                            Flag saying if project builds should use Secure
                            Compute
                      required:
                        - envId
                        - connectConfigurationId
                        - passive
                        - buildsEnabled
                      oneOf:
                        - type: object
                    minItems: 1
                    nullable: true
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              autoExposeSystemEnvs: true
              autoAssignCustomDomains: true
              autoAssignCustomDomainsUpdatedBy: <string>
              buildCommand: <string>
              commandForIgnoringBuildStep: <string>
              customerSupportCodeVisibility: true
              devCommand: <string>
              directoryListing: true
              framework: blitzjs
              gitForkProtection: true
              gitLFS: true
              installCommand: <string>
              name: a-project-name
              nodeVersion: 22.x
              outputDirectory: <string>
              previewDeploymentsDisabled: true
              publicSource: true
              resourceConfig:
                buildMachineType: <any>
                fluid: true
                functionDefaultRegions:
                  - <string>
                functionDefaultTimeout: 450.5
                functionDefaultMemoryType: standard_legacy
                functionZeroConfigFailover: true
                elasticConcurrencyEnabled: true
                isNSNBDisabled: true
              rootDirectory: <string>
              serverlessFunctionRegion: <string>
              serverlessFunctionZeroConfigFailover: true
              skewProtectionBoundaryAt: 1
              skewProtectionMaxAge: 1
              skipGitConnectDuringLink: true
              sourceFilesOutsideRootDirectory: true
              enablePreviewFeedback: true
              enableProductionFeedback: true
              enableAffectedProjectsDeployments: true
              staticIps:
                enabled: true
              oidcTokenConfig:
                enabled: true
                issuerMode: team
              passwordProtection:
                deploymentType: all
                password: <string>
              ssoProtection:
                deploymentType: preview
              trustedIps:
                deploymentType: all
                addresses:
                  - value: <string>
                    note: <string>
                protectionMode: exclusive
              optionsAllowlist:
                paths:
                  - value: <string>
              connectConfigurations:
                - envId: <string>
                  connectConfigurationId: <string>
                  passive: true
                  buildsEnabled: true
    codeSamples:
      - label: updateProject
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.UpdateProject(ctx, \"prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB\", nil, nil, &operations.UpdateProjectRequestBody{\n        Name: vercel.String(\"a-project-name\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateProject
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.updateProject({
              idOrName: "prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "a-project-name",
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
              accountId:
                allOf:
                  - type: string
              analytics:
                allOf:
                  - properties:
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
                allOf:
                  - properties:
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
                allOf:
                  - type: boolean
              autoAssignCustomDomains:
                allOf:
                  - type: boolean
              autoAssignCustomDomainsUpdatedBy:
                allOf:
                  - type: string
              buildCommand:
                allOf:
                  - nullable: true
                    type: string
              commandForIgnoringBuildStep:
                allOf:
                  - nullable: true
                    type: string
              connectConfigurations:
                allOf:
                  - nullable: true
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
                allOf:
                  - nullable: true
                    type: string
              connectBuildsEnabled:
                allOf:
                  - type: boolean
              passiveConnectConfigurationId:
                allOf:
                  - nullable: true
                    type: string
              createdAt:
                allOf:
                  - type: number
              customerSupportCodeVisibility:
                allOf:
                  - type: boolean
              crons:
                allOf:
                  - properties:
                      enabledAt:
                        type: number
                        description: >-
                          The time the feature was enabled for this project.
                          Note: It enables automatically with the first
                          Deployment that outputs cronjobs.
                      disabledAt:
                        nullable: true
                        type: number
                        description: The time the feature was disabled for this project.
                      updatedAt:
                        type: number
                      deploymentId:
                        nullable: true
                        type: string
                        description: >-
                          The ID of the Deployment from which the definitions
                          originated.
                      definitions:
                        items:
                          properties:
                            host:
                              type: string
                              description: The hostname that should be used.
                              example: vercel.com
                            path:
                              type: string
                              description: The path that should be called for the cronjob.
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
                allOf:
                  - properties:
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
                allOf:
                  - nullable: true
                    properties:
                      expirationDays:
                        type: number
                        description: >-
                          Number of days to keep non-production deployments
                          (mostly preview deployments) before soft deletion.
                      expirationDaysProduction:
                        type: number
                        description: >-
                          Number of days to keep production deployments before
                          soft deletion.
                      expirationDaysCanceled:
                        type: number
                        description: >-
                          Number of days to keep canceled deployments before
                          soft deletion.
                      expirationDaysErrored:
                        type: number
                        description: >-
                          Number of days to keep errored deployments before soft
                          deletion.
                      deploymentsToKeep:
                        type: number
                        description: >-
                          Minimum number of production deployments to keep for
                          this project, even if they are over the production
                          expiration limit.
                    type: object
                    description: >-
                      Retention policies for deployments. These are enforced at
                      the project level, but we also maintain an instance of
                      this at the team level as a default policy that gets
                      applied to new projects.
              devCommand:
                allOf:
                  - nullable: true
                    type: string
              directoryListing:
                allOf:
                  - type: boolean
              installCommand:
                allOf:
                  - nullable: true
                    type: string
              env:
                allOf:
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
                      required:
                        - type
                        - value
                        - key
                      type: object
                    type: array
              customEnvironments:
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
                      description: >-
                        Internal representation of a custom environment with all
                        required properties
                    type: array
              framework:
                allOf:
                  - nullable: true
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
                allOf:
                  - type: boolean
              gitLFS:
                allOf:
                  - type: boolean
              id:
                allOf:
                  - type: string
              ipBuckets:
                allOf:
                  - items:
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
                allOf:
                  - items:
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
                            Whether or not preview comments are enabled for the
                            deployment
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
                allOf:
                  - oneOf:
                      - properties:
                          org:
                            type: string
                          repoOwnerId:
                            type: number
                            description: >-
                              A new field, should be included in all new project
                              links, is being added just in time when a
                              deployment is created. This is needed for
                              Protected Git scopes.
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
                              A new field, should be included in all new project
                              links, is being added just in time when a
                              deployment is created. This is needed for
                              Protected Git scopes.
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
                              A new field, should be included in all new project
                              links, is being added just in time when a
                              deployment is created. This is needed for
                              Protected Git scopes.
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
                              A new field, should be included in all new project
                              links, is being added just in time when a
                              deployment is created. This is needed for
                              Protected Git scopes. This is the id of the top
                              level group that a namespace belongs to. Gitlab
                              supports group nesting (up to 20 levels).
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
                allOf:
                  - oneOf:
                      - properties:
                          isDefaultApp:
                            type: boolean
                          updatedAt:
                            type: number
                            description: >-
                              Timestamp when the microfrontends settings were
                              last updated.
                          groupIds:
                            items:
                              oneOf:
                                - type: string
                                - type: string
                            maxItems: 2
                            minItems: 2
                            type: array
                            description: >-
                              The group IDs of microfrontends that this project
                              belongs to. Each microfrontend project must belong
                              to a microfrontends group that is the set of
                              microfrontends that are used together.
                          enabled:
                            type: boolean
                            description: >-
                              Whether microfrontends are enabled for this
                              project.
                          defaultRoute:
                            type: string
                            description: >-
                              A path that is used to take screenshots and as the
                              default path in preview links when a domain for
                              this microfrontend is shown in the UI. Includes
                              the leading slash, e.g. `/docs`
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
                              Whether observability data should be routed to
                              this microfrontend project or a root project.
                          doNotRouteWithMicrofrontendsRouting:
                            type: boolean
                            description: >-
                              Whether to add microfrontends routing to aliases.
                              This means domains in this project will route as a
                              microfrontend.
                          updatedAt:
                            type: number
                            description: >-
                              Timestamp when the microfrontends settings were
                              last updated.
                          groupIds:
                            items:
                              oneOf:
                                - type: string
                                - type: string
                            maxItems: 2
                            minItems: 2
                            type: array
                            description: >-
                              The group IDs of microfrontends that this project
                              belongs to. Each microfrontend project must belong
                              to a microfrontends group that is the set of
                              microfrontends that are used together.
                          enabled:
                            type: boolean
                            description: >-
                              Whether microfrontends are enabled for this
                              project.
                          defaultRoute:
                            type: string
                            description: >-
                              A path that is used to take screenshots and as the
                              default path in preview links when a domain for
                              this microfrontend is shown in the UI. Includes
                              the leading slash, e.g. `/docs`
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
              optionsAllowlist:
                allOf:
                  - nullable: true
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
                allOf:
                  - nullable: true
                    type: string
              passwordProtection:
                allOf:
                  - nullable: true
                    type: object
              productionDeploymentsFastLane:
                allOf:
                  - type: boolean
              publicSource:
                allOf:
                  - nullable: true
                    type: boolean
              resourceConfig:
                allOf:
                  - properties:
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
                allOf:
                  - properties:
                      userId:
                        type: string
                        description: The user who rolled back the project.
                      username:
                        type: string
                        description: The username of the user who rolled back the project.
                      description:
                        type: string
                        description: >-
                          User-supplied explanation of why they rolled back the
                          project. Limited to 250 characters.
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
                      Description of why a project was rolled back, and by whom.
                      Note that lastAliasRequest contains the from/to details of
                      the rollback.
              rollingRelease:
                allOf:
                  - nullable: true
                    properties:
                      target:
                        type: string
                        description: >-
                          The environment that the release targets, currently
                          only supports production. Adding in case we want to
                          configure with alias groups or custom environments.
                        example: production
                      stages:
                        nullable: true
                        items:
                          properties:
                            targetPercentage:
                              type: number
                              description: >-
                                The percentage of traffic to serve to the canary
                                deployment (0-100)
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
                                Duration in minutes for automatic advancement to
                                the next stage
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
                            deployment release. Each stage defines a target
                            percentage and advancement rules. The final stage
                            must always have targetPercentage: 100.
                        type: array
                        description: >-
                          An array of all the stages required during a
                          deployment release. Each stage defines a target
                          percentage and advancement rules. The final stage must
                          always have targetPercentage: 100.
                      canaryResponseHeader:
                        type: boolean
                        description: >-
                          Whether the request served by a canary deployment
                          should return a header indicating a canary was served.
                          Defaults to `false` when omitted.
                        example: false
                    required:
                      - target
                    type: object
                    description: >-
                      Project-level rolling release configuration that defines
                      how deployments should be gradually rolled out
              defaultResourceConfig:
                allOf:
                  - properties:
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
                allOf:
                  - nullable: true
                    type: string
              serverlessFunctionZeroConfigFailover:
                allOf:
                  - type: boolean
              skewProtectionBoundaryAt:
                allOf:
                  - type: number
              skewProtectionMaxAge:
                allOf:
                  - type: number
              skipGitConnectDuringLink:
                allOf:
                  - type: boolean
              sourceFilesOutsideRootDirectory:
                allOf:
                  - type: boolean
              enableAffectedProjectsDeployments:
                allOf:
                  - type: boolean
              ssoProtection:
                allOf:
                  - nullable: true
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
                allOf:
                  - additionalProperties:
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
                            Whether or not preview comments are enabled for the
                            deployment
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
                allOf:
                  - type: number
              transferStartedAt:
                allOf:
                  - type: number
              transferToAccountId:
                allOf:
                  - type: string
              transferredFromAccountId:
                allOf:
                  - type: string
              updatedAt:
                allOf:
                  - type: number
              live:
                allOf:
                  - type: boolean
              enablePreviewFeedback:
                allOf:
                  - nullable: true
                    type: boolean
              enableProductionFeedback:
                allOf:
                  - nullable: true
                    type: boolean
              permissions:
                allOf:
                  - properties:
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
                allOf:
                  - nullable: true
                    type: object
              lastAliasRequest:
                allOf:
                  - nullable: true
                    properties:
                      fromDeploymentId:
                        type: string
                      toDeploymentId:
                        type: string
                      fromRollingReleaseId:
                        type: string
                        description: >-
                          If rolling back from a rolling release,
                          fromDeploymentId captures the "base" of that rolling
                          release, and fromRollingReleaseId captures the
                          "target" of that rolling release.
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
                allOf:
                  - additionalProperties:
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
                allOf:
                  - type: boolean
              trustedIps:
                allOf:
                  - nullable: true
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
                allOf:
                  - properties:
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
                allOf:
                  - properties:
                      createDeployments:
                        type: string
                        enum:
                          - enabled
                          - disabled
                        description: >-
                          Whether the Vercel bot should automatically create
                          GitHub deployments
                          https://docs.github.com/en/rest/deployments/deployments#about-deployments
                          NOTE: repository-dispatch events should be used
                          instead
                      disableRepositoryDispatchEvents:
                        type: boolean
                        description: >-
                          Whether the Vercel bot should not automatically create
                          GitHub repository-dispatch events on deployment
                          events.
                          https://vercel.com/docs/git/vercel-for-github#repository-dispatch-events
                      requireVerifiedCommits:
                        type: boolean
                        description: >-
                          Whether the project requires commits to be signed
                          before deployments will be created.
                    required:
                      - createDeployments
                    type: object
              paused:
                allOf:
                  - type: boolean
              concurrencyBucketName:
                allOf:
                  - type: string
              webAnalytics:
                allOf:
                  - properties:
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
                allOf:
                  - properties:
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
                allOf:
                  - properties:
                      enabled:
                        type: boolean
                        description: >-
                          Whether or not to generate OpenID Connect JSON Web
                          Tokens.
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
                allOf:
                  - type: string
                    enum:
                      - standard
                      - advanced
                      - critical
              features:
                allOf:
                  - properties:
                      webAnalytics:
                        type: boolean
                    type: object
              v0:
                allOf:
                  - type: boolean
              abuse:
                allOf:
                  - properties:
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
                allOf:
                  - items:
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
            requiredProperties:
              - accountId
              - directoryListing
              - id
              - name
              - nodeVersion
              - resourceConfig
              - defaultResourceConfig
        examples:
          example:
            value:
              accountId: <string>
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
                    - <string>
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
        description: The project was successfully updated
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
              Trusted IPs is only accessible for enterprise customers
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
          Trusted IPs is only accessible for enterprise customers
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
            description: >-
              The account was soft-blocked for an unhandled reason.

              The account is missing a payment so payment method must be updated

              Pro customers are allowed to deploy Serverless Functions to up to
              `proMaxRegions` regions, or if the project was created before the
              limit was introduced.

              Deploying to Serverless Functions to multiple regions requires a
              plan update
        examples: {}
        description: >-
          The account was soft-blocked for an unhandled reason.

          The account is missing a payment so payment method must be updated

          Pro customers are allowed to deploy Serverless Functions to up to
          `proMaxRegions` regions, or if the project was created before the
          limit was introduced.

          Deploying to Serverless Functions to multiple regions requires a plan
          update
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
            description: |-
              The provided name for the project is already being used
              The project is currently being transferred.
        examples: {}
        description: |-
          The provided name for the project is already being used
          The project is currently being transferred.
    '428':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              Owner does not have protection add-on
              Advanced Deployment Protection is not available for the user plan
        examples: {}
        description: |-
          Owner does not have protection add-on
          Advanced Deployment Protection is not available for the user plan
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

````

--------------------------------------------------------------------------------
title: "Update Protection Bypass for Automation"

last_updated: "2025-11-07T00:37:14.544Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/update-protection-bypass-for-automation"
--------------------------------------------------------------------------------

# Update Protection Bypass for Automation

> Update the deployment protection automation bypass for a project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/projects/{idOrName}/protection-bypass
paths:
  path: /v1/projects/{idOrName}/protection-bypass
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
              revoke:
                allOf:
                  - description: >-
                      Optional instructions for revoking and regenerating a
                      automation bypass
                    type: object
                    properties:
                      secret:
                        description: Automation bypass to revoked
                        type: string
                      regenerate:
                        description: >-
                          Whether or not a new automation bypass should be
                          created after the provided secret is revoked
                        type: boolean
                    required:
                      - secret
                      - regenerate
              generate:
                allOf:
                  - description: >-
                      Generate a new secret. If neither generate or revoke are
                      provided, a new random secret will be generated.
                    type: object
                    properties:
                      secret:
                        description: >-
                          Optional value of the secret to generate, don't send
                          it for oauth2 tokens
                        type: string
                        pattern: ^[a-zA-Z0-9]{32}$
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              revoke:
                secret: <string>
                regenerate: true
              generate:
                secret: <string>
    codeSamples:
      - label: updateProjectProtectionBypass
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.UpdateProjectProtectionBypass(ctx, \"<value>\", nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateProjectProtectionBypass
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.updateProjectProtectionBypass({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {},
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
              protectionBypass:
                allOf:
                  - additionalProperties:
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
        examples:
          example:
            value:
              protectionBypass: {}
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
title: "Update the data cache feature"

last_updated: "2025-11-07T00:37:14.830Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/projects/update-the-data-cache-feature"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./32-retrieve-the-decrypted-value-of-an-environment-var.md) | [Index](./index.md) | [Next →](./34-update-the-data-cache-feature.md)
