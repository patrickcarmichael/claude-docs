**Navigation:** [← Previous](./35-get-the-active-rolling-release-information-for-a-p.md) | [Index](./index.md) | [Next →](./37-list-user-events.md)

---

# Get a Team

> Get information for the Team specified by the `teamId` parameter.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/teams/{teamId}
paths:
  path: /v2/teams/{teamId}
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
        teamId:
          schema:
            - type: string
              required: true
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query:
        slug:
          schema:
            - type: string
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getTeam
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.GetTeam(ctx, \"<id>\", nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Team != nil {\n        // handle response\n    }\n}"
      - label: getTeam
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.getTeam({
              slug: "my-team-url-slug",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
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
              connect:
                allOf:
                  - properties:
                      enabled:
                        type: boolean
                    type: object
              creatorId:
                allOf:
                  - type: string
                    description: The ID of the user who created the Team.
                    example: R6efeCJQ2HKXywuasPDc0fOWB
              updatedAt:
                allOf:
                  - type: number
                    description: >-
                      Timestamp (in milliseconds) of when the Team was last
                      updated.
                    example: 1611796915677
              emailDomain:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      Hostname that'll be matched with emails on sign-up to
                      automatically join the Team.
                    example: example.com
              saml:
                allOf:
                  - properties:
                      connection:
                        properties:
                          type:
                            type: string
                            description: The Identity Provider "type", for example Okta.
                            example: OktaSAML
                          status:
                            type: string
                            description: Current status of the connection.
                            example: linked
                          state:
                            type: string
                            description: Current state of the connection.
                            example: active
                          connectedAt:
                            type: number
                            description: >-
                              Timestamp (in milliseconds) of when the
                              configuration was connected.
                            example: 1611796915677
                          lastReceivedWebhookEvent:
                            type: number
                            description: >-
                              Timestamp (in milliseconds) of when the last
                              webhook event was received from WorkOS.
                            example: 1611796915677
                        required:
                          - type
                          - status
                          - state
                          - connectedAt
                        type: object
                        description: Information for the SAML Single Sign-On configuration.
                      directory:
                        properties:
                          type:
                            type: string
                            description: The Identity Provider "type", for example Okta.
                            example: OktaSAML
                          state:
                            type: string
                            description: Current state of the connection.
                            example: active
                          connectedAt:
                            type: number
                            description: >-
                              Timestamp (in milliseconds) of when the
                              configuration was connected.
                            example: 1611796915677
                          lastReceivedWebhookEvent:
                            type: number
                            description: >-
                              Timestamp (in milliseconds) of when the last
                              webhook event was received from WorkOS.
                            example: 1611796915677
                        required:
                          - type
                          - state
                          - connectedAt
                        type: object
                        description: Information for the Directory Sync configuration.
                      enforced:
                        type: boolean
                        description: >-
                          When `true`, interactions with the Team **must** be
                          done with an authentication token that has been
                          authenticated with the Team's SAML Single Sign-On
                          provider.
                      defaultRedirectUri:
                        type: string
                        enum:
                          - vercel.com
                          - v0.dev
                          - v0.app
                        description: >-
                          The default redirect URI to use after successful SAML
                          authentication.
                      roles:
                        additionalProperties:
                          oneOf:
                            - properties:
                                accessGroupId:
                                  type: string
                              required:
                                - accessGroupId
                              type: object
                              description: >-
                                When "Directory Sync" is configured, this object
                                contains a mapping of which Directory Group (by
                                ID) should be assigned to which Vercel Team
                                "role".
                            - type: string
                              enum:
                                - OWNER
                                - MEMBER
                                - DEVELOPER
                                - SECURITY
                                - BILLING
                                - VIEWER
                                - VIEWER_FOR_PLUS
                                - CONTRIBUTOR
                        type: object
                        description: >-
                          When "Directory Sync" is configured, this object
                          contains a mapping of which Directory Group (by ID)
                          should be assigned to which Vercel Team "role".
                    required:
                      - enforced
                    type: object
                    description: >-
                      When "Single Sign-On (SAML)" is configured, this object
                      contains information regarding the configuration of the
                      Identity Provider (IdP).
              inviteCode:
                allOf:
                  - type: string
                    description: >-
                      Code that can be used to join this Team. Only visible to
                      Team owners.
                    example: hasihf9e89
              description:
                allOf:
                  - nullable: true
                    type: string
                    description: A short description of the Team.
                    example: >-
                      Our mission is to make cloud computing accessible to
                      everyone.
              defaultRoles:
                allOf:
                  - properties:
                      teamRoles:
                        items:
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
                        type: array
                      teamPermissions:
                        items:
                          type: string
                          enum:
                            - IntegrationManager
                            - CreateProject
                            - FullProductionDeployment
                            - UsageViewer
                            - EnvVariableManager
                            - EnvironmentManager
                            - V0Builder
                            - V0Chatter
                            - V0Viewer
                        type: array
                    type: object
                    description: Default roles for the team.
              stagingPrefix:
                allOf:
                  - type: string
                    description: The prefix that is prepended to automatic aliases.
              resourceConfig:
                allOf:
                  - properties:
                      concurrentBuilds:
                        type: number
                        description: >-
                          The total amount of concurrent builds that can be
                          used.
                      elasticConcurrencyEnabled:
                        type: boolean
                        description: >-
                          Whether every build for this team / user has elastic
                          concurrency enabled automatically.
                      edgeConfigSize:
                        type: number
                        description: >-
                          The maximum size in kilobytes of an Edge Config. Only
                          specified if a custom limit is set.
                      edgeConfigs:
                        type: number
                        description: >-
                          The maximum number of edge configs an account can
                          create.
                      kvDatabases:
                        type: number
                        description: >-
                          The maximum number of kv databases an account can
                          create.
                      blobStores:
                        type: number
                        description: >-
                          The maximum number of blob stores an account can
                          create.
                      postgresDatabases:
                        type: number
                        description: >-
                          The maximum number of postgres databases an account
                          can create.
                      buildEntitlements:
                        properties:
                          enhancedBuilds:
                            type: boolean
                        type: object
                    type: object
              previewDeploymentSuffix:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      The hostname that is current set as preview deployment
                      suffix.
                    example: example.dev
              platform:
                allOf:
                  - type: boolean
                    description: Whether the team is a platform team.
                    example: true
              disableHardAutoBlocks:
                allOf:
                  - oneOf:
                      - type: number
                      - type: boolean
              remoteCaching:
                allOf:
                  - properties:
                      enabled:
                        type: boolean
                    type: object
                    description: Is remote caching enabled for this team
              defaultDeploymentProtection:
                allOf:
                  - properties:
                      passwordProtection:
                        properties:
                          deploymentType:
                            type: string
                        required:
                          - deploymentType
                        type: object
                      ssoProtection:
                        properties:
                          deploymentType:
                            type: string
                        required:
                          - deploymentType
                        type: object
                    type: object
                    description: Default deployment protection for this team
              defaultExpirationSettings:
                allOf:
                  - properties:
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
                    description: Default deployment expiration settings for this team
              enablePreviewFeedback:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - default
                      - 'on'
                      - 'off'
                      - on-force
                      - off-force
                      - default-force
                    description: Whether toolbar is enabled on preview deployments
              enableProductionFeedback:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - default
                      - 'on'
                      - 'off'
                      - on-force
                      - off-force
                      - default-force
                    description: Whether toolbar is enabled on production deployments
              sensitiveEnvironmentVariablePolicy:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - default
                      - 'on'
                      - 'off'
                    description: Sensitive environment variable policy for this team
              hideIpAddresses:
                allOf:
                  - nullable: true
                    type: boolean
                    description: >-
                      Indicates if IP addresses should be accessible in
                      observability (o11y) tooling
              hideIpAddressesInLogDrains:
                allOf:
                  - nullable: true
                    type: boolean
                    description: >-
                      Indicates if IP addresses should be accessible in log
                      drains
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
              id:
                allOf:
                  - type: string
                    description: The Team's unique identifier.
                    example: team_nllPyCtREAqxxdyFKbbMDlxd
              slug:
                allOf:
                  - type: string
                    description: >-
                      The Team's slug, which is unique across the Vercel
                      platform.
                    example: my-team
              name:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      Name associated with the Team account, or `null` if none
                      has been provided.
                    example: My Team
              avatar:
                allOf:
                  - nullable: true
                    type: string
                    description: The ID of the file used as avatar for this Team.
                    example: 6eb07268bcfadd309905ffb1579354084c24655c
              membership:
                allOf:
                  - properties:
                      uid:
                        type: string
                      entitlements:
                        items:
                          properties:
                            entitlement:
                              type: string
                          required:
                            - entitlement
                          type: object
                        type: array
                      teamId:
                        type: string
                      confirmed:
                        type: boolean
                      accessRequestedAt:
                        type: number
                      role:
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
                      teamRoles:
                        items:
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
                        type: array
                      teamPermissions:
                        items:
                          type: string
                          enum:
                            - IntegrationManager
                            - CreateProject
                            - FullProductionDeployment
                            - UsageViewer
                            - EnvVariableManager
                            - EnvironmentManager
                            - V0Builder
                            - V0Chatter
                            - V0Viewer
                        type: array
                      createdAt:
                        type: number
                      created:
                        type: number
                      joinedFrom:
                        properties:
                          origin:
                            type: string
                            enum:
                              - link
                              - saml
                              - mail
                              - import
                              - teams
                              - github
                              - gitlab
                              - bitbucket
                              - dsync
                              - feedback
                              - organization-teams
                          commitId:
                            type: string
                          repoId:
                            type: string
                          repoPath:
                            type: string
                          gitUserId:
                            oneOf:
                              - type: string
                              - type: number
                          gitUserLogin:
                            type: string
                          ssoUserId:
                            type: string
                          ssoConnectedAt:
                            type: number
                          idpUserId:
                            type: string
                          dsyncUserId:
                            type: string
                          dsyncConnectedAt:
                            type: number
                        required:
                          - origin
                        type: object
                    required:
                      - confirmed
                      - role
                      - createdAt
                      - created
                    type: object
                    description: >-
                      The membership of the authenticated User in relation to
                      the Team.
              createdAt:
                allOf:
                  - type: number
                    description: >-
                      UNIX timestamp (in milliseconds) when the Team was
                      created.
                    example: 1630748523395
            description: Data representing a Team.
            refIdentifier: '#/components/schemas/Team'
            requiredProperties:
              - creatorId
              - updatedAt
              - description
              - stagingPrefix
              - id
              - slug
              - name
              - avatar
              - membership
              - createdAt
        examples:
          example:
            value:
              connect:
                enabled: true
              creatorId: R6efeCJQ2HKXywuasPDc0fOWB
              updatedAt: 1611796915677
              emailDomain: example.com
              saml:
                connection:
                  type: OktaSAML
                  status: linked
                  state: active
                  connectedAt: 1611796915677
                  lastReceivedWebhookEvent: 1611796915677
                directory:
                  type: OktaSAML
                  state: active
                  connectedAt: 1611796915677
                  lastReceivedWebhookEvent: 1611796915677
                enforced: true
                defaultRedirectUri: vercel.com
                roles: {}
              inviteCode: hasihf9e89
              description: Our mission is to make cloud computing accessible to everyone.
              defaultRoles:
                teamRoles:
                  - OWNER
                teamPermissions:
                  - IntegrationManager
              stagingPrefix: <string>
              resourceConfig:
                concurrentBuilds: 123
                elasticConcurrencyEnabled: true
                edgeConfigSize: 123
                edgeConfigs: 123
                kvDatabases: 123
                blobStores: 123
                postgresDatabases: 123
                buildEntitlements:
                  enhancedBuilds: true
              previewDeploymentSuffix: example.dev
              platform: true
              disableHardAutoBlocks: 123
              remoteCaching:
                enabled: true
              defaultDeploymentProtection:
                passwordProtection:
                  deploymentType: <string>
                ssoProtection:
                  deploymentType: <string>
              defaultExpirationSettings:
                expirationDays: 123
                expirationDaysProduction: 123
                expirationDaysCanceled: 123
                expirationDaysErrored: 123
                deploymentsToKeep: 123
              enablePreviewFeedback: default
              enableProductionFeedback: default
              sensitiveEnvironmentVariablePolicy: default
              hideIpAddresses: true
              hideIpAddressesInLogDrains: true
              ipBuckets:
                - bucket: <string>
                  supportUntil: 123
              id: team_nllPyCtREAqxxdyFKbbMDlxd
              slug: my-team
              name: My Team
              avatar: 6eb07268bcfadd309905ffb1579354084c24655c
              membership:
                uid: <string>
                entitlements:
                  - entitlement: <string>
                teamId: <string>
                confirmed: true
                accessRequestedAt: 123
                role: OWNER
                teamRoles:
                  - OWNER
                teamPermissions:
                  - IntegrationManager
                createdAt: 123
                created: 123
                joinedFrom:
                  origin: link
                  commitId: <string>
                  repoId: <string>
                  repoPath: <string>
                  gitUserId: <string>
                  gitUserLogin: <string>
                  ssoUserId: <string>
                  ssoConnectedAt: 123
                  idpUserId: <string>
                  dsyncUserId: <string>
                  dsyncConnectedAt: 123
              createdAt: 1630748523395
        description: The requested team
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
            description: |-
              You do not have permission to access this resource.
              Not authorized to access the team.
        examples: {}
        description: |-
          You do not have permission to access this resource.
          Not authorized to access the team.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Team was not found.
        examples: {}
        description: Team was not found.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get access request status"

last_updated: "2025-11-07T00:37:15.998Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/teams/get-access-request-status"
--------------------------------------------------------------------------------

# Get access request status

> Check the status of a join request. It'll respond with a 404 if the request has been declined. If no `userId` path segment was provided, this endpoint will instead return the status of the authenticated user.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/teams/{teamId}/request/{userId}
paths:
  path: /v1/teams/{teamId}/request/{userId}
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
        userId:
          schema:
            - type: string
              required: true
              description: The unique user identifier
        teamId:
          schema:
            - type: string
              required: true
              description: The unique team identifier
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getTeamAccessRequest
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.GetTeamAccessRequest(ctx, \"<id>\", \"<id>\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getTeamAccessRequest
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.getTeamAccessRequest({
              userId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
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
              teamSlug:
                allOf:
                  - type: string
                    description: The slug of the team.
                    example: my-team
              teamName:
                allOf:
                  - type: string
                    description: The name of the team.
                    example: My Team
              confirmed:
                allOf:
                  - type: boolean
                    description: >-
                      Current status of the membership. Will be `true` if
                      confirmed, if pending it'll be `false`.
                    example: false
              joinedFrom:
                allOf:
                  - properties:
                      origin:
                        type: string
                        enum:
                          - link
                          - mail
                          - import
                          - teams
                          - github
                          - gitlab
                          - bitbucket
                          - saml
                          - dsync
                          - feedback
                          - organization-teams
                      commitId:
                        type: string
                      repoId:
                        type: string
                      repoPath:
                        type: string
                      gitUserId:
                        oneOf:
                          - type: string
                          - type: number
                      gitUserLogin:
                        type: string
                      ssoUserId:
                        type: string
                      ssoConnectedAt:
                        type: number
                      idpUserId:
                        type: string
                      dsyncUserId:
                        type: string
                      dsyncConnectedAt:
                        type: number
                    required:
                      - origin
                    type: object
                    description: >-
                      A map that describes the origin from where the user
                      joined.
              accessRequestedAt:
                allOf:
                  - type: number
                    description: >-
                      Timestamp in milliseconds when the user requested access
                      to the team.
                    example: 1588720733602
              github:
                allOf:
                  - nullable: true
                    properties:
                      login:
                        type: string
                    type: object
                    description: Map of the connected GitHub account.
              gitlab:
                allOf:
                  - nullable: true
                    properties:
                      login:
                        type: string
                    type: object
                    description: Map of the connected GitLab account.
              bitbucket:
                allOf:
                  - nullable: true
                    properties:
                      login:
                        type: string
                    type: object
                    description: Map of the connected Bitbucket account.
            requiredProperties:
              - teamSlug
              - teamName
              - confirmed
              - joinedFrom
              - accessRequestedAt
              - github
              - gitlab
              - bitbucket
        examples:
          example:
            value:
              teamSlug: my-team
              teamName: My Team
              confirmed: false
              joinedFrom:
                origin: link
                commitId: <string>
                repoId: <string>
                repoPath: <string>
                gitUserId: <string>
                gitUserLogin: <string>
                ssoUserId: <string>
                ssoConnectedAt: 123
                idpUserId: <string>
                dsyncUserId: <string>
                dsyncConnectedAt: 123
              accessRequestedAt: 1588720733602
              github:
                login: <string>
              gitlab:
                login: <string>
              bitbucket:
                login: <string>
        description: Successfully
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              One of the provided values in the request query is invalid.

              User is already a confirmed member of the team and did not request
              access. Only visible when the authenticated user does have access
              to the team.
        examples: {}
        description: >-
          One of the provided values in the request query is invalid.

          User is already a confirmed member of the team and did not request
          access. Only visible when the authenticated user does have access to
          the team.
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
            description: |-
              The provided user doesn't have a membership.
              Team was not found.
        examples: {}
        description: |-
          The provided user doesn't have a membership.
          Team was not found.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Invite a user"

last_updated: "2025-11-07T00:37:15.903Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/teams/invite-a-user"
--------------------------------------------------------------------------------

# Invite a user

> Invite a user to join the team specified in the URL. The authenticated user needs to be an `OWNER` in order to successfully invoke this endpoint. The user to be invited must be specified by email.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams/{teamId}/members
paths:
  path: /v1/teams/{teamId}/members
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
        teamId:
          schema:
            - type: string
              required: true
              description: The unique team identifier
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              email:
                allOf:
                  - type: string
                    format: email
                    description: The email address of the user to invite
                    example: john@example.com
              role:
                allOf:
                  - type: string
                    enum:
                      - OWNER
                      - MEMBER
                      - DEVELOPER
                      - SECURITY
                      - BILLING
                      - VIEWER
                      - VIEWER_FOR_PLUS
                      - CONTRIBUTOR
                    description: The role of the user to invite
                    example:
                      - OWNER
                      - MEMBER
                      - DEVELOPER
                      - SECURITY
                      - BILLING
                      - VIEWER
                      - VIEWER_FOR_PLUS
                      - CONTRIBUTOR
                    default: MEMBER
              projects:
                allOf:
                  - type: array
                    items:
                      type: object
                      additionalProperties: false
                      required:
                        - role
                        - projectId
                      properties:
                        projectId:
                          type: string
                          maxLength: 64
                          example: prj_ndlgr43fadlPyCtREAqxxdyFK
                          description: The ID of the project.
                        role:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_VIEWER
                            - PROJECT_DEVELOPER
                          example: ADMIN
                          description: Sets the project roles for the invited user
            required: true
            requiredProperties:
              - email
        examples:
          example:
            value:
              email: john@example.com
              role:
                - OWNER
                - MEMBER
                - DEVELOPER
                - SECURITY
                - BILLING
                - VIEWER
                - VIEWER_FOR_PLUS
                - CONTRIBUTOR
              projects:
                - projectId: prj_ndlgr43fadlPyCtREAqxxdyFK
                  role: ADMIN
    codeSamples:
      - label: inviteUserToTeam
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.InviteUserToTeam(ctx, \"<id>\", &operations.InviteUserToTeamRequestBody{\n        UID: vercel.String(\"kr1PsOIzqEL5Xg6M4VZcZosf\"),\n        Email: vercel.String(\"john@example.com\"),\n        Role: operations.InviteUserToTeamRoleViewer.ToPointer(),\n        Projects: []operations.InviteUserToTeamProjects{\n            operations.InviteUserToTeamProjects{\n                ProjectID: \"prj_ndlgr43fadlPyCtREAqxxdyFK\",\n                Role: operations.InviteUserToTeamTeamsRoleAdmin,\n            },\n            operations.InviteUserToTeamProjects{\n                ProjectID: \"prj_ndlgr43fadlPyCtREAqxxdyFK\",\n                Role: operations.InviteUserToTeamTeamsRoleAdmin,\n            },\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: inviteUserToTeam
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.inviteUserToTeam({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                email: "john@example.com",
                role: "DEVELOPER",
                projects: [
                  {
                    projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",
                    role: "ADMIN",
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
              uid:
                allOf:
                  - type: string
                    description: The ID of the invited user
                    example: kr1PsOIzqEL5Xg6M4VZcZosf
              username:
                allOf:
                  - type: string
                    description: The username of the invited user
                    example: john-doe
              email:
                allOf:
                  - type: string
                    description: The email of the invited user.
                    example: john@user.co
              role:
                allOf:
                  - type: string
                    enum:
                      - OWNER
                      - MEMBER
                      - DEVELOPER
                      - SECURITY
                      - BILLING
                      - VIEWER
                      - VIEWER_FOR_PLUS
                      - CONTRIBUTOR
                    description: The role used for the invitation
                    example: MEMBER
              teamRoles:
                allOf:
                  - items:
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
                      description: The team roles of the user
                      example:
                        - MEMBER
                    type: array
                    description: The team roles of the user
                    example:
                      - MEMBER
              teamPermissions:
                allOf:
                  - items:
                      type: string
                      enum:
                        - IntegrationManager
                        - CreateProject
                        - FullProductionDeployment
                        - UsageViewer
                        - EnvVariableManager
                        - EnvironmentManager
                        - V0Builder
                        - V0Chatter
                        - V0Viewer
                      description: The team permissions of the user
                      example:
                        - CreateProject
                    type: array
                    description: The team permissions of the user
                    example:
                      - CreateProject
            description: The member was successfully added to the team
            requiredProperties:
              - uid
              - username
              - email
              - role
        examples:
          example:
            value:
              uid: kr1PsOIzqEL5Xg6M4VZcZosf
              username: john-doe
              email: john@user.co
              role: MEMBER
              teamRoles:
                - MEMBER
              teamPermissions:
                - CreateProject
        description: The member was successfully added to the team
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
              The user already requested access to the team
              The team reached the maximum allowed amount of members
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
          The user already requested access to the team
          The team reached the maximum allowed amount of members
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
            description: |-
              The authenticated user must be a team owner to perform the action
              You do not have permission to access this resource.
        examples: {}
        description: |-
          The authenticated user must be a team owner to perform the action
          You do not have permission to access this resource.
    '503': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Join a team"

last_updated: "2025-11-07T00:37:15.893Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/teams/join-a-team"
--------------------------------------------------------------------------------

# Join a team

> Join a team with a provided invite code or team ID.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams/{teamId}/members/teams/join
paths:
  path: /v1/teams/{teamId}/members/teams/join
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
        teamId:
          schema:
            - type: string
              required: true
              description: The unique team identifier
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              inviteCode:
                allOf:
                  - type: string
                    description: The invite code to join the team.
                    example: fisdh38aejkeivn34nslfore9vjtn4ls
            required: true
        examples:
          example:
            value:
              inviteCode: fisdh38aejkeivn34nslfore9vjtn4ls
    codeSamples:
      - label: joinTeam
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.JoinTeam(ctx, \"<id>\", &operations.JoinTeamRequestBody{\n        InviteCode: vercel.String(\"fisdh38aejkeivn34nslfore9vjtn4ls\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: joinTeam
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.joinTeam({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                inviteCode: "fisdh38aejkeivn34nslfore9vjtn4ls",
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
              teamId:
                allOf:
                  - type: string
                    description: The ID of the team the user joined.
                    example: team_LLHUOMOoDlqOp8wPE4kFo9pE
              slug:
                allOf:
                  - type: string
                    description: The slug of the team the user joined.
                    example: my-team
              name:
                allOf:
                  - type: string
                    description: The name of the team the user joined.
                    example: My Team
              from:
                allOf:
                  - type: string
                    description: The origin of how the user joined.
                    example: email
            description: Successfully joined a team.
            requiredProperties:
              - teamId
              - slug
              - name
              - from
        examples:
          example:
            value:
              teamId: team_LLHUOMOoDlqOp8wPE4kFo9pE
              slug: my-team
              name: My Team
              from: email
        description: Successfully joined a team.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
    '401': {}
    '402': {}
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
title: "List all teams"

last_updated: "2025-11-07T00:37:15.884Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/teams/list-all-teams"
--------------------------------------------------------------------------------

# List all teams

> Get a paginated list of all the Teams the authenticated User is a member of.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/teams
paths:
  path: /v2/teams
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
        limit:
          schema:
            - type: number
              description: Maximum number of Teams which may be returned.
              example: 20
        since:
          schema:
            - type: number
              description: >-
                Timestamp (in milliseconds) to only include Teams created since
                then.
              example: 1540095775951
        until:
          schema:
            - type: number
              description: >-
                Timestamp (in milliseconds) to only include Teams created until
                then.
              example: 1540095775951
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getTeams
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.GetTeams(ctx, vercel.Float64(20), vercel.Float64(1540095775951), vercel.Float64(1540095775951))\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getTeams
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.getTeams({
              limit: 20,
              since: 1540095775951,
              until: 1540095775951,
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
              teams:
                allOf:
                  - items:
                      oneOf:
                        - $ref: '#/components/schemas/Team'
                        - $ref: '#/components/schemas/TeamLimited'
                    type: array
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            description: A paginated list of teams.
            requiredProperties:
              - teams
              - pagination
        examples:
          example:
            value:
              teams:
                - connect:
                    enabled: true
                  creatorId: R6efeCJQ2HKXywuasPDc0fOWB
                  updatedAt: 1611796915677
                  emailDomain: example.com
                  saml:
                    connection:
                      type: OktaSAML
                      status: linked
                      state: active
                      connectedAt: 1611796915677
                      lastReceivedWebhookEvent: 1611796915677
                    directory:
                      type: OktaSAML
                      state: active
                      connectedAt: 1611796915677
                      lastReceivedWebhookEvent: 1611796915677
                    enforced: true
                    defaultRedirectUri: vercel.com
                    roles: {}
                  inviteCode: hasihf9e89
                  description: >-
                    Our mission is to make cloud computing accessible to
                    everyone.
                  defaultRoles:
                    teamRoles:
                      - OWNER
                    teamPermissions:
                      - IntegrationManager
                  stagingPrefix: <string>
                  resourceConfig:
                    concurrentBuilds: 123
                    elasticConcurrencyEnabled: true
                    edgeConfigSize: 123
                    edgeConfigs: 123
                    kvDatabases: 123
                    blobStores: 123
                    postgresDatabases: 123
                    buildEntitlements:
                      enhancedBuilds: true
                  previewDeploymentSuffix: example.dev
                  platform: true
                  disableHardAutoBlocks: 123
                  remoteCaching:
                    enabled: true
                  defaultDeploymentProtection:
                    passwordProtection:
                      deploymentType: <string>
                    ssoProtection:
                      deploymentType: <string>
                  defaultExpirationSettings:
                    expirationDays: 123
                    expirationDaysProduction: 123
                    expirationDaysCanceled: 123
                    expirationDaysErrored: 123
                    deploymentsToKeep: 123
                  enablePreviewFeedback: default
                  enableProductionFeedback: default
                  sensitiveEnvironmentVariablePolicy: default
                  hideIpAddresses: true
                  hideIpAddressesInLogDrains: true
                  ipBuckets:
                    - bucket: <string>
                      supportUntil: 123
                  id: team_nllPyCtREAqxxdyFKbbMDlxd
                  slug: my-team
                  name: My Team
                  avatar: 6eb07268bcfadd309905ffb1579354084c24655c
                  membership:
                    uid: <string>
                    entitlements:
                      - entitlement: <string>
                    teamId: <string>
                    confirmed: true
                    accessRequestedAt: 123
                    role: OWNER
                    teamRoles:
                      - OWNER
                    teamPermissions:
                      - IntegrationManager
                    createdAt: 123
                    created: 123
                    joinedFrom:
                      origin: link
                      commitId: <string>
                      repoId: <string>
                      repoPath: <string>
                      gitUserId: <string>
                      gitUserLogin: <string>
                      ssoUserId: <string>
                      ssoConnectedAt: 123
                      idpUserId: <string>
                      dsyncUserId: <string>
                      dsyncConnectedAt: 123
                  createdAt: 1630748523395
              pagination:
                count: 20
                next: 1540095775951
                prev: 1540095775951
        description: A paginated list of teams.
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
    Team:
      properties:
        connect:
          properties:
            enabled:
              type: boolean
          type: object
        creatorId:
          type: string
          description: The ID of the user who created the Team.
          example: R6efeCJQ2HKXywuasPDc0fOWB
        updatedAt:
          type: number
          description: Timestamp (in milliseconds) of when the Team was last updated.
          example: 1611796915677
        emailDomain:
          nullable: true
          type: string
          description: >-
            Hostname that'll be matched with emails on sign-up to automatically
            join the Team.
          example: example.com
        saml:
          properties:
            connection:
              properties:
                type:
                  type: string
                  description: The Identity Provider "type", for example Okta.
                  example: OktaSAML
                status:
                  type: string
                  description: Current status of the connection.
                  example: linked
                state:
                  type: string
                  description: Current state of the connection.
                  example: active
                connectedAt:
                  type: number
                  description: >-
                    Timestamp (in milliseconds) of when the configuration was
                    connected.
                  example: 1611796915677
                lastReceivedWebhookEvent:
                  type: number
                  description: >-
                    Timestamp (in milliseconds) of when the last webhook event
                    was received from WorkOS.
                  example: 1611796915677
              required:
                - type
                - status
                - state
                - connectedAt
              type: object
              description: Information for the SAML Single Sign-On configuration.
            directory:
              properties:
                type:
                  type: string
                  description: The Identity Provider "type", for example Okta.
                  example: OktaSAML
                state:
                  type: string
                  description: Current state of the connection.
                  example: active
                connectedAt:
                  type: number
                  description: >-
                    Timestamp (in milliseconds) of when the configuration was
                    connected.
                  example: 1611796915677
                lastReceivedWebhookEvent:
                  type: number
                  description: >-
                    Timestamp (in milliseconds) of when the last webhook event
                    was received from WorkOS.
                  example: 1611796915677
              required:
                - type
                - state
                - connectedAt
              type: object
              description: Information for the Directory Sync configuration.
            enforced:
              type: boolean
              description: >-
                When `true`, interactions with the Team **must** be done with an
                authentication token that has been authenticated with the Team's
                SAML Single Sign-On provider.
            defaultRedirectUri:
              type: string
              enum:
                - vercel.com
                - v0.dev
                - v0.app
              description: >-
                The default redirect URI to use after successful SAML
                authentication.
            roles:
              additionalProperties:
                oneOf:
                  - properties:
                      accessGroupId:
                        type: string
                    required:
                      - accessGroupId
                    type: object
                    description: >-
                      When "Directory Sync" is configured, this object contains
                      a mapping of which Directory Group (by ID) should be
                      assigned to which Vercel Team "role".
                  - type: string
                    enum:
                      - OWNER
                      - MEMBER
                      - DEVELOPER
                      - SECURITY
                      - BILLING
                      - VIEWER
                      - VIEWER_FOR_PLUS
                      - CONTRIBUTOR
              type: object
              description: >-
                When "Directory Sync" is configured, this object contains a
                mapping of which Directory Group (by ID) should be assigned to
                which Vercel Team "role".
          required:
            - enforced
          type: object
          description: >-
            When "Single Sign-On (SAML)" is configured, this object contains
            information regarding the configuration of the Identity Provider
            (IdP).
        inviteCode:
          type: string
          description: >-
            Code that can be used to join this Team. Only visible to Team
            owners.
          example: hasihf9e89
        description:
          nullable: true
          type: string
          description: A short description of the Team.
          example: Our mission is to make cloud computing accessible to everyone.
        defaultRoles:
          properties:
            teamRoles:
              items:
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
              type: array
            teamPermissions:
              items:
                type: string
                enum:
                  - IntegrationManager
                  - CreateProject
                  - FullProductionDeployment
                  - UsageViewer
                  - EnvVariableManager
                  - EnvironmentManager
                  - V0Builder
                  - V0Chatter
                  - V0Viewer
              type: array
          type: object
          description: Default roles for the team.
        stagingPrefix:
          type: string
          description: The prefix that is prepended to automatic aliases.
        resourceConfig:
          properties:
            concurrentBuilds:
              type: number
              description: The total amount of concurrent builds that can be used.
            elasticConcurrencyEnabled:
              type: boolean
              description: >-
                Whether every build for this team / user has elastic concurrency
                enabled automatically.
            edgeConfigSize:
              type: number
              description: >-
                The maximum size in kilobytes of an Edge Config. Only specified
                if a custom limit is set.
            edgeConfigs:
              type: number
              description: The maximum number of edge configs an account can create.
            kvDatabases:
              type: number
              description: The maximum number of kv databases an account can create.
            blobStores:
              type: number
              description: The maximum number of blob stores an account can create.
            postgresDatabases:
              type: number
              description: The maximum number of postgres databases an account can create.
            buildEntitlements:
              properties:
                enhancedBuilds:
                  type: boolean
              type: object
          type: object
        previewDeploymentSuffix:
          nullable: true
          type: string
          description: The hostname that is current set as preview deployment suffix.
          example: example.dev
        platform:
          type: boolean
          description: Whether the team is a platform team.
          example: true
        disableHardAutoBlocks:
          oneOf:
            - type: number
            - type: boolean
        remoteCaching:
          properties:
            enabled:
              type: boolean
          type: object
          description: Is remote caching enabled for this team
        defaultDeploymentProtection:
          properties:
            passwordProtection:
              properties:
                deploymentType:
                  type: string
              required:
                - deploymentType
              type: object
            ssoProtection:
              properties:
                deploymentType:
                  type: string
              required:
                - deploymentType
              type: object
          type: object
          description: Default deployment protection for this team
        defaultExpirationSettings:
          properties:
            expirationDays:
              type: number
              description: >-
                Number of days to keep non-production deployments (mostly
                preview deployments) before soft deletion.
            expirationDaysProduction:
              type: number
              description: >-
                Number of days to keep production deployments before soft
                deletion.
            expirationDaysCanceled:
              type: number
              description: >-
                Number of days to keep canceled deployments before soft
                deletion.
            expirationDaysErrored:
              type: number
              description: Number of days to keep errored deployments before soft deletion.
            deploymentsToKeep:
              type: number
              description: >-
                Minimum number of production deployments to keep for this
                project, even if they are over the production expiration limit.
          type: object
          description: Default deployment expiration settings for this team
        enablePreviewFeedback:
          nullable: true
          type: string
          enum:
            - default
            - 'on'
            - 'off'
            - on-force
            - off-force
            - default-force
          description: Whether toolbar is enabled on preview deployments
        enableProductionFeedback:
          nullable: true
          type: string
          enum:
            - default
            - 'on'
            - 'off'
            - on-force
            - off-force
            - default-force
          description: Whether toolbar is enabled on production deployments
        sensitiveEnvironmentVariablePolicy:
          nullable: true
          type: string
          enum:
            - default
            - 'on'
            - 'off'
          description: Sensitive environment variable policy for this team
        hideIpAddresses:
          nullable: true
          type: boolean
          description: >-
            Indicates if IP addresses should be accessible in observability
            (o11y) tooling
        hideIpAddressesInLogDrains:
          nullable: true
          type: boolean
          description: Indicates if IP addresses should be accessible in log drains
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
        id:
          type: string
          description: The Team's unique identifier.
          example: team_nllPyCtREAqxxdyFKbbMDlxd
        slug:
          type: string
          description: The Team's slug, which is unique across the Vercel platform.
          example: my-team
        name:
          nullable: true
          type: string
          description: >-
            Name associated with the Team account, or `null` if none has been
            provided.
          example: My Team
        avatar:
          nullable: true
          type: string
          description: The ID of the file used as avatar for this Team.
          example: 6eb07268bcfadd309905ffb1579354084c24655c
        membership:
          properties:
            uid:
              type: string
            entitlements:
              items:
                properties:
                  entitlement:
                    type: string
                required:
                  - entitlement
                type: object
              type: array
            teamId:
              type: string
            confirmed:
              type: boolean
            accessRequestedAt:
              type: number
            role:
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
            teamRoles:
              items:
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
              type: array
            teamPermissions:
              items:
                type: string
                enum:
                  - IntegrationManager
                  - CreateProject
                  - FullProductionDeployment
                  - UsageViewer
                  - EnvVariableManager
                  - EnvironmentManager
                  - V0Builder
                  - V0Chatter
                  - V0Viewer
              type: array
            createdAt:
              type: number
            created:
              type: number
            joinedFrom:
              properties:
                origin:
                  type: string
                  enum:
                    - link
                    - saml
                    - mail
                    - import
                    - teams
                    - github
                    - gitlab
                    - bitbucket
                    - dsync
                    - feedback
                    - organization-teams
                commitId:
                  type: string
                repoId:
                  type: string
                repoPath:
                  type: string
                gitUserId:
                  oneOf:
                    - type: string
                    - type: number
                gitUserLogin:
                  type: string
                ssoUserId:
                  type: string
                ssoConnectedAt:
                  type: number
                idpUserId:
                  type: string
                dsyncUserId:
                  type: string
                dsyncConnectedAt:
                  type: number
              required:
                - origin
              type: object
          required:
            - confirmed
            - role
            - createdAt
            - created
          type: object
          description: The membership of the authenticated User in relation to the Team.
        createdAt:
          type: number
          description: UNIX timestamp (in milliseconds) when the Team was created.
          example: 1630748523395
      required:
        - creatorId
        - updatedAt
        - description
        - stagingPrefix
        - id
        - slug
        - name
        - avatar
        - membership
        - createdAt
      type: object
      description: Data representing a Team.
      additionalProperties: true
    TeamLimited:
      properties:
        limited:
          type: boolean
          description: >-
            Property indicating that this Team data contains only limited
            information, due to the authentication token missing privileges to
            read the full Team data or due to team having MFA enforced and the
            user not having MFA enabled. Re-login with the Team's configured
            SAML Single Sign-On provider in order to upgrade the authentication
            token with the necessary privileges.
        limitedBy:
          items:
            type: string
            enum:
              - scope
              - mfa
          type: array
        saml:
          properties:
            connection:
              properties:
                type:
                  type: string
                  description: The Identity Provider "type", for example Okta.
                  example: OktaSAML
                status:
                  type: string
                  description: Current status of the connection.
                  example: linked
                state:
                  type: string
                  description: Current state of the connection.
                  example: active
                connectedAt:
                  type: number
                  description: >-
                    Timestamp (in milliseconds) of when the configuration was
                    connected.
                  example: 1611796915677
                lastReceivedWebhookEvent:
                  type: number
                  description: >-
                    Timestamp (in milliseconds) of when the last webhook event
                    was received from WorkOS.
                  example: 1611796915677
              required:
                - type
                - status
                - state
                - connectedAt
              type: object
              description: Information for the SAML Single Sign-On configuration.
            directory:
              properties:
                type:
                  type: string
                  description: The Identity Provider "type", for example Okta.
                  example: OktaSAML
                state:
                  type: string
                  description: Current state of the connection.
                  example: active
                connectedAt:
                  type: number
                  description: >-
                    Timestamp (in milliseconds) of when the configuration was
                    connected.
                  example: 1611796915677
                lastReceivedWebhookEvent:
                  type: number
                  description: >-
                    Timestamp (in milliseconds) of when the last webhook event
                    was received from WorkOS.
                  example: 1611796915677
              required:
                - type
                - state
                - connectedAt
              type: object
              description: Information for the Directory Sync configuration.
            enforced:
              type: boolean
              description: >-
                When `true`, interactions with the Team **must** be done with an
                authentication token that has been authenticated with the Team's
                SAML Single Sign-On provider.
          required:
            - enforced
          type: object
          description: >-
            When "Single Sign-On (SAML)" is configured, this object contains
            information that allows the client-side to identify whether or not
            this Team has SAML enforced.
        id:
          type: string
          description: The Team's unique identifier.
          example: team_nllPyCtREAqxxdyFKbbMDlxd
        slug:
          type: string
          description: The Team's slug, which is unique across the Vercel platform.
          example: my-team
        name:
          nullable: true
          type: string
          description: >-
            Name associated with the Team account, or `null` if none has been
            provided.
          example: My Team
        avatar:
          nullable: true
          type: string
          description: The ID of the file used as avatar for this Team.
          example: 6eb07268bcfadd309905ffb1579354084c24655c
        membership:
          properties:
            uid:
              type: string
            entitlements:
              items:
                properties:
                  entitlement:
                    type: string
                required:
                  - entitlement
                type: object
              type: array
            teamId:
              type: string
            confirmed:
              type: boolean
            accessRequestedAt:
              type: number
            role:
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
            teamRoles:
              items:
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
              type: array
            teamPermissions:
              items:
                type: string
                enum:
                  - IntegrationManager
                  - CreateProject
                  - FullProductionDeployment
                  - UsageViewer
                  - EnvVariableManager
                  - EnvironmentManager
                  - V0Builder
                  - V0Chatter
                  - V0Viewer
              type: array
            createdAt:
              type: number
            created:
              type: number
            joinedFrom:
              properties:
                origin:
                  type: string
                  enum:
                    - link
                    - saml
                    - mail
                    - import
                    - teams
                    - github
                    - gitlab
                    - bitbucket
                    - dsync
                    - feedback
                    - organization-teams
                commitId:
                  type: string
                repoId:
                  type: string
                repoPath:
                  type: string
                gitUserId:
                  oneOf:
                    - type: string
                    - type: number
                gitUserLogin:
                  type: string
                ssoUserId:
                  type: string
                ssoConnectedAt:
                  type: number
                idpUserId:
                  type: string
                dsyncUserId:
                  type: string
                dsyncConnectedAt:
                  type: number
              required:
                - origin
              type: object
          required:
            - confirmed
            - role
            - createdAt
            - created
          type: object
          description: The membership of the authenticated User in relation to the Team.
        createdAt:
          type: number
          description: UNIX timestamp (in milliseconds) when the Team was created.
          example: 1630748523395
      required:
        - limited
        - limitedBy
        - id
        - slug
        - name
        - avatar
        - membership
        - createdAt
      type: object
      description: >-
        A limited form of data representing a Team, due to the authentication
        token missing privileges to read the full Team data.

````

--------------------------------------------------------------------------------
title: "List team members"

last_updated: "2025-11-07T00:37:16.110Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/teams/list-team-members"
--------------------------------------------------------------------------------

# List team members

> Get a paginated list of team members for the provided team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v3/teams/{teamId}/members
paths:
  path: /v3/teams/{teamId}/members
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
        limit:
          schema:
            - type: number
              required: false
              description: Limit how many teams should be returned
              minimum: 1
              example: 20
        since:
          schema:
            - type: number
              required: false
              description: >-
                Timestamp in milliseconds to only include members added since
                then.
              example: 1540095775951
        until:
          schema:
            - type: number
              required: false
              description: >-
                Timestamp in milliseconds to only include members added until
                then.
              example: 1540095775951
        search:
          schema:
            - type: string
              required: false
              description: Search team members by their name, username, and email.
        role:
          schema:
            - type: enum<string>
              enum:
                - OWNER
                - MEMBER
                - DEVELOPER
                - SECURITY
                - BILLING
                - VIEWER
                - VIEWER_FOR_PLUS
                - CONTRIBUTOR
              required: false
              description: Only return members with the specified team role.
              example: OWNER
        excludeProject:
          schema:
            - type: string
              required: false
              description: Exclude members who belong to the specified project.
        eligibleMembersForProjectId:
          schema:
            - type: string
              required: false
              description: >-
                Include team members who are eligible to be members of the
                specified project.
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getTeamMembers
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.getTeamMembers({
              limit: 20,
              since: 1540095775951,
              until: 1540095775951,
              role: "OWNER",
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
              members:
                allOf:
                  - items:
                      properties:
                        avatar:
                          type: string
                          description: ID of the file for the Avatar of this member.
                          example: 123a6c5209bc3778245d011443644c8d27dc2c50
                        confirmed:
                          type: boolean
                          description: >-
                            Boolean that indicates if this member was confirmed
                            by an owner.
                          example: true
                        email:
                          type: string
                          description: The email of this member.
                          example: jane.doe@example.com
                        github:
                          properties:
                            login:
                              type: string
                          type: object
                          description: Information about the GitHub account for this user.
                        gitlab:
                          properties:
                            login:
                              type: string
                          type: object
                          description: Information about the GitLab account of this user.
                        bitbucket:
                          properties:
                            login:
                              type: string
                          type: object
                          description: >-
                            Information about the Bitbucket account of this
                            user.
                        role:
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
                          description: Role of this user in the team.
                          example: OWNER
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
                        accessRequestedAt:
                          type: number
                          description: >-
                            Timestamp in milliseconds for when this team member
                            was accepted by an owner.
                          example: 1588820733602
                        joinedFrom:
                          properties:
                            origin:
                              type: string
                              enum:
                                - teams
                                - link
                                - mail
                                - import
                                - github
                                - gitlab
                                - bitbucket
                                - saml
                                - dsync
                                - feedback
                                - organization-teams
                            commitId:
                              type: string
                            repoId:
                              type: string
                            repoPath:
                              type: string
                            gitUserId:
                              oneOf:
                                - type: string
                                - type: number
                            gitUserLogin:
                              type: string
                            ssoUserId:
                              type: string
                            ssoConnectedAt:
                              type: number
                            idpUserId:
                              type: string
                            dsyncUserId:
                              type: string
                            dsyncConnectedAt:
                              type: number
                          required:
                            - origin
                          type: object
                          description: >-
                            Map with information about the members origin if
                            they joined by requesting access.
                        projects:
                          items:
                            properties:
                              name:
                                type: string
                              id:
                                type: string
                              role:
                                type: string
                                enum:
                                  - ADMIN
                                  - PROJECT_DEVELOPER
                                  - PROJECT_VIEWER
                            required:
                              - name
                              - id
                            type: object
                            description: Array of project memberships
                          type: array
                          description: Array of project memberships
                      required:
                        - confirmed
                        - email
                        - role
                        - uid
                        - username
                        - createdAt
                      type: object
                    type: array
              emailInviteCodes:
                allOf:
                  - items:
                      properties:
                        accessGroups:
                          items:
                            type: string
                          type: array
                        id:
                          type: string
                        email:
                          type: string
                        role:
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
                        teamRoles:
                          items:
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
                          type: array
                        teamPermissions:
                          items:
                            type: string
                            enum:
                              - IntegrationManager
                              - CreateProject
                              - FullProductionDeployment
                              - UsageViewer
                              - EnvVariableManager
                              - EnvironmentManager
                              - V0Builder
                              - V0Chatter
                              - V0Viewer
                          type: array
                        isDSyncUser:
                          type: boolean
                        createdAt:
                          type: number
                        expired:
                          type: boolean
                        projects:
                          additionalProperties:
                            type: string
                            enum:
                              - ADMIN
                              - PROJECT_DEVELOPER
                              - PROJECT_VIEWER
                          type: object
                        entitlements:
                          items:
                            type: string
                          type: array
                      required:
                        - id
                        - isDSyncUser
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
            requiredProperties:
              - members
              - pagination
        examples:
          example:
            value:
              members:
                - avatar: 123a6c5209bc3778245d011443644c8d27dc2c50
                  confirmed: true
                  email: jane.doe@example.com
                  github:
                    login: <string>
                  gitlab:
                    login: <string>
                  bitbucket:
                    login: <string>
                  role: OWNER
                  uid: zTuNVUXEAvvnNN3IaqinkyMw
                  username: jane-doe
                  name: Jane Doe
                  createdAt: 1588720733602
                  accessRequestedAt: 1588820733602
                  joinedFrom:
                    origin: teams
                    commitId: <string>
                    repoId: <string>
                    repoPath: <string>
                    gitUserId: <string>
                    gitUserLogin: <string>
                    ssoUserId: <string>
                    ssoConnectedAt: 123
                    idpUserId: <string>
                    dsyncUserId: <string>
                    dsyncConnectedAt: 123
                  projects:
                    - name: <string>
                      id: <string>
                      role: ADMIN
              emailInviteCodes:
                - accessGroups:
                    - <string>
                  id: <string>
                  email: <string>
                  role: OWNER
                  teamRoles:
                    - OWNER
                  teamPermissions:
                    - IntegrationManager
                  isDSyncUser: true
                  createdAt: 123
                  expired: true
                  projects: {}
                  entitlements:
                    - <string>
              pagination:
                hasNext: true
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
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Remove a Team Member"

last_updated: "2025-11-07T00:37:16.098Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/teams/remove-a-team-member"
--------------------------------------------------------------------------------

# Remove a Team Member

> Remove a Team Member from the Team, or dismiss a user that requested access, or leave a team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/teams/{teamId}/members/{uid}
paths:
  path: /v1/teams/{teamId}/members/{uid}
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
        uid:
          schema:
            - type: string
              required: true
              description: The user ID of the member.
              example: ndlgr43fadlPyCtREAqxxdyFK
        teamId:
          schema:
            - type: string
              required: true
              description: The unique team identifier
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query:
        newDefaultTeamId:
          schema:
            - type: string
              required: false
              description: >-
                The ID of the team to set as the new default team for the
                Northstar user.
              example: team_nllPyCtREAqxxdyFKbbMDlxd
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: removeTeamMember
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.RemoveTeamMember(ctx, \"ndlgr43fadlPyCtREAqxxdyFK\", \"<id>\", vercel.String(\"team_nllPyCtREAqxxdyFKbbMDlxd\"))\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: removeTeamMember
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.removeTeamMember({
              uid: "ndlgr43fadlPyCtREAqxxdyFK",
              newDefaultTeamId: "team_nllPyCtREAqxxdyFKbbMDlxd",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
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
                    description: ID of the team.
            requiredProperties:
              - id
        examples:
          example:
            value:
              id: <string>
        description: Successfully removed a member of the team.
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
            description: |-
              You do not have permission to access this resource.
              Not authorized to update the team.
        examples: {}
        description: |-
          You do not have permission to access this resource.
          Not authorized to update the team.
    '404': {}
    '503': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Request access to a team"

last_updated: "2025-11-07T00:37:15.945Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/teams/request-access-to-a-team"
--------------------------------------------------------------------------------

# Request access to a team

> Request access to a team as a member. An owner has to approve the request. Only 10 users can request access to a team at the same time.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams/{teamId}/request
paths:
  path: /v1/teams/{teamId}/request
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
        teamId:
          schema:
            - type: string
              required: true
              description: The unique team identifier
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              joinedFrom:
                allOf:
                  - type: object
                    additionalProperties: false
                    required:
                      - origin
                    properties:
                      origin:
                        type: string
                        enum:
                          - import
                          - teams
                          - github
                          - gitlab
                          - bitbucket
                          - feedback
                          - organization-teams
                        description: The origin of the request.
                        example: github
                      commitId:
                        type: string
                        description: The commit sha if the origin is a git provider.
                        example: f498d25d8bd654b578716203be73084b31130cd7
                      repoId:
                        type: string
                        description: The ID of the repository for the given Git provider.
                        example: '67753070'
                      repoPath:
                        type: string
                        description: The path to the repository for the given Git provider.
                        example: jane-doe/example
                      gitUserId:
                        description: >-
                          The ID of the Git account of the user who requests
                          access.
                        example: 103053343
                        oneOf:
                          - type: string
                          - type: number
                      gitUserLogin:
                        type: string
                        description: >-
                          The login name for the Git account of the user who
                          requests access.
                        example: jane-doe
            required: true
            requiredProperties:
              - joinedFrom
            additionalProperties: false
        examples:
          example:
            value:
              joinedFrom:
                origin: github
                commitId: f498d25d8bd654b578716203be73084b31130cd7
                repoId: '67753070'
                repoPath: jane-doe/example
                gitUserId: 103053343
                gitUserLogin: jane-doe
    codeSamples:
      - label: requestAccessToTeam
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.RequestAccessToTeam(ctx, \"<id>\", &operations.RequestAccessToTeamRequestBody{\n        JoinedFrom: operations.JoinedFrom{\n            Origin: operations.OriginGithub,\n            CommitID: vercel.String(\"f498d25d8bd654b578716203be73084b31130cd7\"),\n            RepoID: vercel.String(\"67753070\"),\n            RepoPath: vercel.String(\"jane-doe/example\"),\n            GitUserID: vercel.Pointer(operations.CreateGitUserIDNumber(\n                103053343,\n            )),\n            GitUserLogin: vercel.String(\"jane-doe\"),\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: requestAccessToTeam
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.requestAccessToTeam({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                joinedFrom: {
                  origin: "github",
                  commitId: "f498d25d8bd654b578716203be73084b31130cd7",
                  repoId: "67753070",
                  repoPath: "jane-doe/example",
                  gitUserId: 103053343,
                  gitUserLogin: "jane-doe",
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
              teamSlug:
                allOf:
                  - type: string
              teamName:
                allOf:
                  - type: string
              confirmed:
                allOf:
                  - type: boolean
              joinedFrom:
                allOf:
                  - properties:
                      origin:
                        type: string
                        enum:
                          - import
                          - teams
                          - github
                          - gitlab
                          - bitbucket
                          - feedback
                          - organization-teams
                          - link
                          - mail
                          - saml
                          - dsync
                      commitId:
                        type: string
                      repoId:
                        type: string
                      repoPath:
                        type: string
                      gitUserId:
                        oneOf:
                          - type: string
                          - type: number
                      gitUserLogin:
                        type: string
                      ssoUserId:
                        type: string
                      ssoConnectedAt:
                        type: number
                      idpUserId:
                        type: string
                      dsyncUserId:
                        type: string
                      dsyncConnectedAt:
                        type: number
                    required:
                      - origin
                    type: object
              accessRequestedAt:
                allOf:
                  - type: number
              github:
                allOf:
                  - nullable: true
                    properties:
                      login:
                        type: string
                    type: object
              gitlab:
                allOf:
                  - nullable: true
                    properties:
                      login:
                        type: string
                    type: object
              bitbucket:
                allOf:
                  - nullable: true
                    properties:
                      login:
                        type: string
                    type: object
            requiredProperties:
              - teamSlug
              - teamName
              - github
              - gitlab
              - bitbucket
        examples:
          example:
            value:
              teamSlug: <string>
              teamName: <string>
              confirmed: true
              joinedFrom:
                origin: import
                commitId: <string>
                repoId: <string>
                repoPath: <string>
                gitUserId: <string>
                gitUserLogin: <string>
                ssoUserId: <string>
                ssoConnectedAt: 123
                idpUserId: <string>
                dsyncUserId: <string>
                dsyncConnectedAt: 123
              accessRequestedAt: 123
              github:
                login: <string>
              gitlab:
                login: <string>
              bitbucket:
                login: <string>
        description: Successfuly requested access to the team.
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
            description: The team was not found.
        examples: {}
        description: The team was not found.
    '503': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update a Team"

last_updated: "2025-11-07T00:37:15.930Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/teams/update-a-team"
--------------------------------------------------------------------------------

# Update a Team

> Update the information of a Team specified by the `teamId` parameter. The request body should contain the information that will be updated on the Team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v2/teams/{teamId}
paths:
  path: /v2/teams/{teamId}
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
        teamId:
          schema:
            - type: string
              required: true
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query:
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
              avatar:
                allOf:
                  - type: string
                    format: regex
                    description: The hash value of an uploaded image.
              description:
                allOf:
                  - type: string
                    maxLength: 140
                    example: >-
                      Our mission is to make cloud computing accessible to
                      everyone
                    description: A short text that describes the team.
              emailDomain:
                allOf:
                  - type: string
                    format: regex
                    example: example.com
                    nullable: true
              name:
                allOf:
                  - type: string
                    maxLength: 256
                    example: My Team
                    description: The name of the team.
              previewDeploymentSuffix:
                allOf:
                  - type: string
                    format: hostname
                    example: example.dev
                    description: Suffix that will be used for all preview deployments.
                    nullable: true
              regenerateInviteCode:
                allOf:
                  - type: boolean
                    example: true
                    description: Create a new invite code and replace the current one.
              saml:
                allOf:
                  - type: object
                    additionalProperties: false
                    properties:
                      enforced:
                        type: boolean
                        example: true
                        description: >-
                          Require that members of the team use SAML Single
                          Sign-On.
                      roles:
                        type: object
                        description: Directory groups to role or access group mappings.
                        additionalProperties:
                          anyOf:
                            - type: string
                              enum:
                                - OWNER
                                - MEMBER
                                - DEVELOPER
                                - SECURITY
                                - BILLING
                                - VIEWER
                                - VIEWER_FOR_PLUS
                                - CONTRIBUTOR
                            - type: object
                              additionalProperties: false
                              required:
                                - accessGroupId
                              properties:
                                accessGroupId:
                                  type: string
                                  pattern: ^ag_[A-z0-9_ -]+$
              slug:
                allOf:
                  - type: string
                    example: my-team
                    description: A new slug for the team.
              enablePreviewFeedback:
                allOf:
                  - type: string
                    example: 'on'
                    description: 'Enable preview toolbar: one of on, off or default.'
              enableProductionFeedback:
                allOf:
                  - type: string
                    example: 'on'
                    description: 'Enable production toolbar: one of on, off or default.'
              sensitiveEnvironmentVariablePolicy:
                allOf:
                  - type: string
                    example: 'on'
                    description: >-
                      Sensitive environment variable policy: one of on, off or
                      default.
              remoteCaching:
                allOf:
                  - type: object
                    description: Whether or not remote caching is enabled for the team
                    additionalProperties: false
                    properties:
                      enabled:
                        type: boolean
                        example: true
                        description: Enable or disable remote caching for the team.
              hideIpAddresses:
                allOf:
                  - type: boolean
                    example: false
                    description: Display or hide IP addresses in Monitoring queries.
              hideIpAddressesInLogDrains:
                allOf:
                  - type: boolean
                    example: false
                    description: Display or hide IP addresses in Log Drains.
              defaultDeploymentProtection:
                allOf:
                  - type: object
                    description: Default deployment protection settings for new projects.
                    additionalProperties: false
                    properties:
                      passwordProtection:
                        additionalProperties: false
                        description: Allows to protect project deployments with a password
                        properties:
                          deploymentType:
                            description: >-
                              Specify if the password will apply to every
                              Deployment Target or just Preview
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
                        additionalProperties: false
                        description: >-
                          Ensures visitors to your Preview Deployments are
                          logged into Vercel and have a minimum of Viewer access
                          on your team
                        properties:
                          deploymentType:
                            default: preview
                            description: >-
                              Specify if the Vercel Authentication (SSO
                              Protection) will apply to every Deployment Target
                              or just Preview
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
              defaultExpirationSettings:
                allOf:
                  - properties:
                      expiration:
                        description: The time period to keep non-production deployments for
                        example: 1y
                        type: string
                        enum:
                          - 3y
                          - 2y
                          - 1y
                          - 6m
                          - 3m
                          - 2m
                          - 1m
                          - 2w
                          - 1w
                          - 1d
                          - unlimited
                      expirationProduction:
                        description: The time period to keep production deployments for
                        example: 1y
                        type: string
                        enum:
                          - 3y
                          - 2y
                          - 1y
                          - 6m
                          - 3m
                          - 2m
                          - 1m
                          - 2w
                          - 1w
                          - 1d
                          - unlimited
                      expirationCanceled:
                        description: The time period to keep canceled deployments for
                        example: 1y
                        type: string
                        enum:
                          - 1y
                          - 6m
                          - 3m
                          - 2m
                          - 1m
                          - 2w
                          - 1w
                          - 1d
                          - unlimited
                      expirationErrored:
                        description: The time period to keep errored deployments for
                        example: 1y
                        type: string
                        enum:
                          - 1y
                          - 6m
                          - 3m
                          - 2m
                          - 1m
                          - 2w
                          - 1w
                          - 1d
                          - unlimited
                    type: object
                    additionalProperties: false
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              avatar: <string>
              description: Our mission is to make cloud computing accessible to everyone
              emailDomain: example.com
              name: My Team
              previewDeploymentSuffix: example.dev
              regenerateInviteCode: true
              saml:
                enforced: true
                roles: {}
              slug: my-team
              enablePreviewFeedback: 'on'
              enableProductionFeedback: 'on'
              sensitiveEnvironmentVariablePolicy: 'on'
              remoteCaching:
                enabled: true
              hideIpAddresses: false
              hideIpAddressesInLogDrains: false
              defaultDeploymentProtection:
                passwordProtection:
                  deploymentType: all
                  password: <string>
                ssoProtection:
                  deploymentType: preview
              defaultExpirationSettings:
                expiration: 1y
                expirationProduction: 1y
                expirationCanceled: 1y
                expirationErrored: 1y
    codeSamples:
      - label: patchTeam
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.PatchTeam(ctx, \"<id>\", nil, &operations.PatchTeamRequestBody{\n        Description: vercel.String(\"Our mission is to make cloud computing accessible to everyone\"),\n        EmailDomain: vercel.String(\"example.com\"),\n        Name: vercel.String(\"My Team\"),\n        PreviewDeploymentSuffix: vercel.String(\"example.dev\"),\n        RegenerateInviteCode: vercel.Bool(true),\n        Saml: &operations.Saml{\n            Enforced: vercel.Bool(true),\n        },\n        Slug: vercel.String(\"my-team\"),\n        EnablePreviewFeedback: vercel.String(\"on\"),\n        EnableProductionFeedback: vercel.String(\"on\"),\n        SensitiveEnvironmentVariablePolicy: vercel.String(\"on\"),\n        RemoteCaching: &operations.RemoteCaching{\n            Enabled: vercel.Bool(true),\n        },\n        HideIPAddresses: vercel.Bool(false),\n        HideIPAddressesInLogDrains: vercel.Bool(false),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Team != nil {\n        // handle response\n    }\n}"
      - label: patchTeam
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.patchTeam({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                description: "Our mission is to make cloud computing accessible to everyone",
                emailDomain: "example.com",
                name: "My Team",
                previewDeploymentSuffix: "example.dev",
                regenerateInviteCode: true,
                saml: {
                  enforced: true,
                },
                slug: "my-team",
                enablePreviewFeedback: "on",
                enableProductionFeedback: "on",
                sensitiveEnvironmentVariablePolicy: "on",
                remoteCaching: {
                  enabled: true,
                },
                hideIpAddresses: false,
                hideIpAddressesInLogDrains: false,
                defaultExpirationSettings: {
                  expiration: "1y",
                  expirationProduction: "1y",
                  expirationCanceled: "1y",
                  expirationErrored: "1y",
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
              connect:
                allOf:
                  - properties:
                      enabled:
                        type: boolean
                    type: object
              creatorId:
                allOf:
                  - type: string
                    description: The ID of the user who created the Team.
                    example: R6efeCJQ2HKXywuasPDc0fOWB
              updatedAt:
                allOf:
                  - type: number
                    description: >-
                      Timestamp (in milliseconds) of when the Team was last
                      updated.
                    example: 1611796915677
              emailDomain:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      Hostname that'll be matched with emails on sign-up to
                      automatically join the Team.
                    example: example.com
              saml:
                allOf:
                  - properties:
                      connection:
                        properties:
                          type:
                            type: string
                            description: The Identity Provider "type", for example Okta.
                            example: OktaSAML
                          status:
                            type: string
                            description: Current status of the connection.
                            example: linked
                          state:
                            type: string
                            description: Current state of the connection.
                            example: active
                          connectedAt:
                            type: number
                            description: >-
                              Timestamp (in milliseconds) of when the
                              configuration was connected.
                            example: 1611796915677
                          lastReceivedWebhookEvent:
                            type: number
                            description: >-
                              Timestamp (in milliseconds) of when the last
                              webhook event was received from WorkOS.
                            example: 1611796915677
                        required:
                          - type
                          - status
                          - state
                          - connectedAt
                        type: object
                        description: Information for the SAML Single Sign-On configuration.
                      directory:
                        properties:
                          type:
                            type: string
                            description: The Identity Provider "type", for example Okta.
                            example: OktaSAML
                          state:
                            type: string
                            description: Current state of the connection.
                            example: active
                          connectedAt:
                            type: number
                            description: >-
                              Timestamp (in milliseconds) of when the
                              configuration was connected.
                            example: 1611796915677
                          lastReceivedWebhookEvent:
                            type: number
                            description: >-
                              Timestamp (in milliseconds) of when the last
                              webhook event was received from WorkOS.
                            example: 1611796915677
                        required:
                          - type
                          - state
                          - connectedAt
                        type: object
                        description: Information for the Directory Sync configuration.
                      enforced:
                        type: boolean
                        description: >-
                          When `true`, interactions with the Team **must** be
                          done with an authentication token that has been
                          authenticated with the Team's SAML Single Sign-On
                          provider.
                      defaultRedirectUri:
                        type: string
                        enum:
                          - vercel.com
                          - v0.dev
                          - v0.app
                        description: >-
                          The default redirect URI to use after successful SAML
                          authentication.
                      roles:
                        additionalProperties:
                          oneOf:
                            - properties:
                                accessGroupId:
                                  type: string
                              required:
                                - accessGroupId
                              type: object
                              description: >-
                                When "Directory Sync" is configured, this object
                                contains a mapping of which Directory Group (by
                                ID) should be assigned to which Vercel Team
                                "role".
                            - type: string
                              enum:
                                - OWNER
                                - MEMBER
                                - DEVELOPER
                                - SECURITY
                                - BILLING
                                - VIEWER
                                - VIEWER_FOR_PLUS
                                - CONTRIBUTOR
                        type: object
                        description: >-
                          When "Directory Sync" is configured, this object
                          contains a mapping of which Directory Group (by ID)
                          should be assigned to which Vercel Team "role".
                    required:
                      - enforced
                    type: object
                    description: >-
                      When "Single Sign-On (SAML)" is configured, this object
                      contains information regarding the configuration of the
                      Identity Provider (IdP).
              inviteCode:
                allOf:
                  - type: string
                    description: >-
                      Code that can be used to join this Team. Only visible to
                      Team owners.
                    example: hasihf9e89
              description:
                allOf:
                  - nullable: true
                    type: string
                    description: A short description of the Team.
                    example: >-
                      Our mission is to make cloud computing accessible to
                      everyone.
              defaultRoles:
                allOf:
                  - properties:
                      teamRoles:
                        items:
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
                        type: array
                      teamPermissions:
                        items:
                          type: string
                          enum:
                            - IntegrationManager
                            - CreateProject
                            - FullProductionDeployment
                            - UsageViewer
                            - EnvVariableManager
                            - EnvironmentManager
                            - V0Builder
                            - V0Chatter
                            - V0Viewer
                        type: array
                    type: object
                    description: Default roles for the team.
              stagingPrefix:
                allOf:
                  - type: string
                    description: The prefix that is prepended to automatic aliases.
              resourceConfig:
                allOf:
                  - properties:
                      concurrentBuilds:
                        type: number
                        description: >-
                          The total amount of concurrent builds that can be
                          used.
                      elasticConcurrencyEnabled:
                        type: boolean
                        description: >-
                          Whether every build for this team / user has elastic
                          concurrency enabled automatically.
                      edgeConfigSize:
                        type: number
                        description: >-
                          The maximum size in kilobytes of an Edge Config. Only
                          specified if a custom limit is set.
                      edgeConfigs:
                        type: number
                        description: >-
                          The maximum number of edge configs an account can
                          create.
                      kvDatabases:
                        type: number
                        description: >-
                          The maximum number of kv databases an account can
                          create.
                      blobStores:
                        type: number
                        description: >-
                          The maximum number of blob stores an account can
                          create.
                      postgresDatabases:
                        type: number
                        description: >-
                          The maximum number of postgres databases an account
                          can create.
                      buildEntitlements:
                        properties:
                          enhancedBuilds:
                            type: boolean
                        type: object
                    type: object
              previewDeploymentSuffix:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      The hostname that is current set as preview deployment
                      suffix.
                    example: example.dev
              platform:
                allOf:
                  - type: boolean
                    description: Whether the team is a platform team.
                    example: true
              disableHardAutoBlocks:
                allOf:
                  - oneOf:
                      - type: number
                      - type: boolean
              remoteCaching:
                allOf:
                  - properties:
                      enabled:
                        type: boolean
                    type: object
                    description: Is remote caching enabled for this team
              defaultDeploymentProtection:
                allOf:
                  - properties:
                      passwordProtection:
                        properties:
                          deploymentType:
                            type: string
                        required:
                          - deploymentType
                        type: object
                      ssoProtection:
                        properties:
                          deploymentType:
                            type: string
                        required:
                          - deploymentType
                        type: object
                    type: object
                    description: Default deployment protection for this team
              defaultExpirationSettings:
                allOf:
                  - properties:
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
                    description: Default deployment expiration settings for this team
              enablePreviewFeedback:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - default
                      - 'on'
                      - 'off'
                      - on-force
                      - off-force
                      - default-force
                    description: Whether toolbar is enabled on preview deployments
              enableProductionFeedback:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - default
                      - 'on'
                      - 'off'
                      - on-force
                      - off-force
                      - default-force
                    description: Whether toolbar is enabled on production deployments
              sensitiveEnvironmentVariablePolicy:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - default
                      - 'on'
                      - 'off'
                    description: Sensitive environment variable policy for this team
              hideIpAddresses:
                allOf:
                  - nullable: true
                    type: boolean
                    description: >-
                      Indicates if IP addresses should be accessible in
                      observability (o11y) tooling
              hideIpAddressesInLogDrains:
                allOf:
                  - nullable: true
                    type: boolean
                    description: >-
                      Indicates if IP addresses should be accessible in log
                      drains
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
              id:
                allOf:
                  - type: string
                    description: The Team's unique identifier.
                    example: team_nllPyCtREAqxxdyFKbbMDlxd
              slug:
                allOf:
                  - type: string
                    description: >-
                      The Team's slug, which is unique across the Vercel
                      platform.
                    example: my-team
              name:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      Name associated with the Team account, or `null` if none
                      has been provided.
                    example: My Team
              avatar:
                allOf:
                  - nullable: true
                    type: string
                    description: The ID of the file used as avatar for this Team.
                    example: 6eb07268bcfadd309905ffb1579354084c24655c
              membership:
                allOf:
                  - properties:
                      uid:
                        type: string
                      entitlements:
                        items:
                          properties:
                            entitlement:
                              type: string
                          required:
                            - entitlement
                          type: object
                        type: array
                      teamId:
                        type: string
                      confirmed:
                        type: boolean
                      accessRequestedAt:
                        type: number
                      role:
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
                      teamRoles:
                        items:
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
                        type: array
                      teamPermissions:
                        items:
                          type: string
                          enum:
                            - IntegrationManager
                            - CreateProject
                            - FullProductionDeployment
                            - UsageViewer
                            - EnvVariableManager
                            - EnvironmentManager
                            - V0Builder
                            - V0Chatter
                            - V0Viewer
                        type: array
                      createdAt:
                        type: number
                      created:
                        type: number
                      joinedFrom:
                        properties:
                          origin:
                            type: string
                            enum:
                              - link
                              - saml
                              - mail
                              - import
                              - teams
                              - github
                              - gitlab
                              - bitbucket
                              - dsync
                              - feedback
                              - organization-teams
                          commitId:
                            type: string
                          repoId:
                            type: string
                          repoPath:
                            type: string
                          gitUserId:
                            oneOf:
                              - type: string
                              - type: number
                          gitUserLogin:
                            type: string
                          ssoUserId:
                            type: string
                          ssoConnectedAt:
                            type: number
                          idpUserId:
                            type: string
                          dsyncUserId:
                            type: string
                          dsyncConnectedAt:
                            type: number
                        required:
                          - origin
                        type: object
                    required:
                      - confirmed
                      - role
                      - createdAt
                      - created
                    type: object
                    description: >-
                      The membership of the authenticated User in relation to
                      the Team.
              createdAt:
                allOf:
                  - type: number
                    description: >-
                      UNIX timestamp (in milliseconds) when the Team was
                      created.
                    example: 1630748523395
            description: Data representing a Team.
            refIdentifier: '#/components/schemas/Team'
            requiredProperties:
              - creatorId
              - updatedAt
              - description
              - stagingPrefix
              - id
              - slug
              - name
              - avatar
              - membership
              - createdAt
        examples:
          example:
            value:
              connect:
                enabled: true
              creatorId: R6efeCJQ2HKXywuasPDc0fOWB
              updatedAt: 1611796915677
              emailDomain: example.com
              saml:
                connection:
                  type: OktaSAML
                  status: linked
                  state: active
                  connectedAt: 1611796915677
                  lastReceivedWebhookEvent: 1611796915677
                directory:
                  type: OktaSAML
                  state: active
                  connectedAt: 1611796915677
                  lastReceivedWebhookEvent: 1611796915677
                enforced: true
                defaultRedirectUri: vercel.com
                roles: {}
              inviteCode: hasihf9e89
              description: Our mission is to make cloud computing accessible to everyone.
              defaultRoles:
                teamRoles:
                  - OWNER
                teamPermissions:
                  - IntegrationManager
              stagingPrefix: <string>
              resourceConfig:
                concurrentBuilds: 123
                elasticConcurrencyEnabled: true
                edgeConfigSize: 123
                edgeConfigs: 123
                kvDatabases: 123
                blobStores: 123
                postgresDatabases: 123
                buildEntitlements:
                  enhancedBuilds: true
              previewDeploymentSuffix: example.dev
              platform: true
              disableHardAutoBlocks: 123
              remoteCaching:
                enabled: true
              defaultDeploymentProtection:
                passwordProtection:
                  deploymentType: <string>
                ssoProtection:
                  deploymentType: <string>
              defaultExpirationSettings:
                expirationDays: 123
                expirationDaysProduction: 123
                expirationDaysCanceled: 123
                expirationDaysErrored: 123
                deploymentsToKeep: 123
              enablePreviewFeedback: default
              enableProductionFeedback: default
              sensitiveEnvironmentVariablePolicy: default
              hideIpAddresses: true
              hideIpAddressesInLogDrains: true
              ipBuckets:
                - bucket: <string>
                  supportUntil: 123
              id: team_nllPyCtREAqxxdyFKbbMDlxd
              slug: my-team
              name: My Team
              avatar: 6eb07268bcfadd309905ffb1579354084c24655c
              membership:
                uid: <string>
                entitlements:
                  - entitlement: <string>
                teamId: <string>
                confirmed: true
                accessRequestedAt: 123
                role: OWNER
                teamRoles:
                  - OWNER
                teamPermissions:
                  - IntegrationManager
                createdAt: 123
                created: 123
                joinedFrom:
                  origin: link
                  commitId: <string>
                  repoId: <string>
                  repoPath: <string>
                  gitUserId: <string>
                  gitUserLogin: <string>
                  ssoUserId: <string>
                  ssoConnectedAt: 123
                  idpUserId: <string>
                  dsyncUserId: <string>
                  dsyncConnectedAt: 123
              createdAt: 1630748523395
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
            description: |-
              You do not have permission to access this resource.
              Not authorized to update the team. Must be an OWNER.
        examples: {}
        description: |-
          You do not have permission to access this resource.
          Not authorized to update the team. Must be an OWNER.
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
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update a Team Member"

last_updated: "2025-11-07T00:37:15.960Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/teams/update-a-team-member"
--------------------------------------------------------------------------------

# Update a Team Member

> Update the membership of a Team Member on the Team specified by `teamId`, such as changing the _role_ of the member, or confirming a request to join the Team for an unconfirmed member. The authenticated user must be an `OWNER` of the Team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/teams/{teamId}/members/{uid}
paths:
  path: /v1/teams/{teamId}/members/{uid}
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
        uid:
          schema:
            - type: string
              required: true
              description: The ID of the member.
              example: ndfasllgPyCtREAqxxdyFKb
        teamId:
          schema:
            - type: string
              required: true
              description: The unique team identifier
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              confirmed:
                allOf:
                  - type: boolean
                    enum:
                      - true
                    description: Accept a user who requested access to the team.
                    example: true
              role:
                allOf:
                  - type: string
                    description: The role in the team of the member.
                    example:
                      - MEMBER
                      - VIEWER
                    default: MEMBER
              projects:
                allOf:
                  - type: array
                    items:
                      type: object
                      additionalProperties: false
                      required:
                        - role
                        - projectId
                      properties:
                        projectId:
                          type: string
                          maxLength: 256
                          example: prj_ndlgr43fadlPyCtREAqxxdyFK
                          description: The ID of the project.
                        role:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_VIEWER
                            - PROJECT_DEVELOPER
                            - null
                          example: ADMIN
                          description: >-
                            The project role of the member that will be added.
                            \"null\" will remove this project level role.
                          nullable: true
              joinedFrom:
                allOf:
                  - additionalProperties: false
                    type: object
                    properties:
                      ssoUserId:
                        nullable: true
            required: true
        examples:
          example:
            value:
              confirmed: true
              role:
                - MEMBER
                - VIEWER
              projects:
                - projectId: prj_ndlgr43fadlPyCtREAqxxdyFK
                  role: ADMIN
              joinedFrom:
                ssoUserId: <any>
    codeSamples:
      - label: updateTeamMember
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.UpdateTeamMember(ctx, \"ndfasllgPyCtREAqxxdyFKb\", \"<id>\", &operations.UpdateTeamMemberRequestBody{\n        Confirmed: vercel.Bool(true),\n        Role: vercel.String(\"[\\\"MEMBER\\\",\\\"VIEWER\\\"]\"),\n        Projects: []operations.UpdateTeamMemberProjects{\n            operations.UpdateTeamMemberProjects{\n                ProjectID: \"prj_ndlgr43fadlPyCtREAqxxdyFK\",\n                Role: operations.UpdateTeamMemberRoleAdmin.ToPointer(),\n            },\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateTeamMember
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.updateTeamMember({
              uid: "ndfasllgPyCtREAqxxdyFKb",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                confirmed: true,
                role: "[\"MEMBER\",\"VIEWER\"]",
                projects: [
                  {
                    projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",
                    role: "ADMIN",
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
              id:
                allOf:
                  - type: string
                    description: ID of the team.
            requiredProperties:
              - id
        examples:
          example:
            value:
              id: <string>
        description: Successfully updated the membership.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              One of the provided values in the request body is invalid.

              One of the provided values in the request query is invalid.

              Cannot disconnect SSO from a Team member that does not have a SSO
              connection.

              Cannot confirm a member that is already confirmed.

              Cannot confirm a member that did not request access.
        examples: {}
        description: >-
          One of the provided values in the request body is invalid.

          One of the provided values in the request query is invalid.

          Cannot disconnect SSO from a Team member that does not have a SSO
          connection.

          Cannot confirm a member that is already confirmed.

          Cannot confirm a member that did not request access.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              The request is not authorized.

              Team members can only be updated by an owner, or by the
              authenticated user if they are only disconnecting their SAML
              connection to the Team.
        examples: {}
        description: >-
          The request is not authorized.

          Team members can only be updated by an owner, or by the authenticated
          user if they are only disconnecting their SAML connection to the Team.
    '402': {}
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
              The provided user is not part of this team.
              A user with the specified ID does not exist.
        examples: {}
        description: |-
          The provided user is not part of this team.
          A user with the specified ID does not exist.
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Delete User Account"

last_updated: "2025-11-07T00:37:15.904Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/user/delete-user-account"
--------------------------------------------------------------------------------

# Delete User Account

> Initiates the deletion process for the currently authenticated User, by sending a deletion confirmation email. The email contains a link that the user needs to visit in order to proceed with the deletion process.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/user
paths:
  path: /v1/user
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              reasons:
                allOf:
                  - type: array
                    description: >-
                      Optional array of objects that describe the reason why the
                      User account is being deleted.
                    items:
                      type: object
                      description: >-
                        An object describing the reason why the User account is
                        being deleted.
                      required:
                        - slug
                        - description
                      additionalProperties: false
                      properties:
                        slug:
                          type: string
                          description: >-
                            Idenitifier slug of the reason why the User account
                            is being deleted.
                        description:
                          type: string
                          description: >-
                            Description of the reason why the User account is
                            being deleted.
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              reasons:
                - slug: <string>
                  description: <string>
    codeSamples:
      - label: requestDelete
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.User.RequestDelete(ctx, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: requestDelete
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.user.requestDelete({});

            console.log(result);
          }

          run();
  response:
    '202':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: Unique identifier of the User who has initiated deletion.
              email:
                allOf:
                  - type: string
                    description: Email address of the User who has initiated deletion.
              message:
                allOf:
                  - type: string
                    description: User deletion progress status.
                    example: Verification email sent
            requiredProperties:
              - id
              - email
              - message
        examples:
          example:
            value:
              id: <string>
              email: <string>
              message: Verification email sent
        description: >-
          Response indicating that the User deletion process has been initiated,
          and a confirmation email has been sent.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
    '401': {}
    '402': {}
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
title: "Get the User"

last_updated: "2025-11-07T00:37:16.445Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/user/get-the-user"
--------------------------------------------------------------------------------

# Get the User

> Retrieves information related to the currently authenticated User.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/user
paths:
  path: /v2/user
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
      - label: getAuthUser
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.User.GetAuthUser(ctx)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getAuthUser
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.user.getAuthUser();

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              user:
                allOf:
                  - oneOf:
                      - $ref: '#/components/schemas/AuthUser'
                      - $ref: '#/components/schemas/AuthUserLimited'
            description: Successful response.
            requiredProperties:
              - user
        examples:
          example:
            value:
              user:
                createdAt: 1630748523395
                softBlock:
                  blockedAt: 123
                  reason: SUBSCRIPTION_CANCELED
                  blockedDueToOverageType: analyticsUsage
                billing: {}
                resourceConfig:
                  nodeType: <string>
                  concurrentBuilds: 123
                  elasticConcurrencyEnabled: true
                  buildEntitlements:
                    enhancedBuilds: true
                  buildQueue:
                    configuration: SKIP_NAMESPACE_QUEUE
                  awsAccountType: <string>
                  awsAccountIds:
                    - <string>
                  cfZoneName: <string>
                  imageOptimizationType: <string>
                  edgeConfigs: 123
                  edgeConfigSize: 123
                  edgeFunctionMaxSizeBytes: 123
                  edgeFunctionExecutionTimeoutMs: 123
                  serverlessFunctionMaxMemorySize: 123
                  kvDatabases: 123
                  postgresDatabases: 123
                  blobStores: 123
                  integrationStores: 123
                  cronJobs: 123
                  cronJobsPerProject: 123
                  microfrontendGroupsPerTeam: 123
                  microfrontendProjectsPerGroup: 123
                  flagsExplorerOverridesThreshold: 123
                  flagsExplorerUnlimitedOverrides: true
                  customEnvironmentsPerProject: 123
                  buildMachine:
                    purchaseType: enhanced
                    isDefaultBuildMachine: true
                    cores: 123
                    memory: 123
                  security:
                    customRules: 123
                    ipBlocks: 123
                    ipBypass: 123
                    rateLimit: 123
                stagingPrefix: <string>
                activeDashboardViews:
                  - scopeId: <string>
                    viewPreference: list
                    favoritesViewPreference: open
                    recentsViewPreference: open
                importFlowGitNamespace: <string>
                importFlowGitNamespaceId: <string>
                importFlowGitProvider: gitlab
                preferredScopesAndGitNamespaces:
                  - scopeId: <string>
                    gitNamespaceId: <string>
                dismissedToasts:
                  - name: <string>
                    dismissals:
                      - scopeId: <string>
                        createdAt: 123
                favoriteProjectsAndSpaces:
                  - teamId: <string>
                    projectId: <string>
                hasTrialAvailable: true
                remoteCaching:
                  enabled: true
                dataCache:
                  excessBillingEnabled: true
                featureBlocks:
                  webAnalytics:
                    blockedFrom: 123
                    blockedUntil: 123
                    isCurrentlyBlocked: true
                id: AEIIDYVk59zbFF2Sxfyxxmua
                email: me@example.com
                name: John Doe
                username: jdoe
                avatar: 22cb30c85ff45ac4c72de8981500006b28114aa1
                defaultTeamId: <string>
        description: Successful response.
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
    '409': {}
  deprecated: false
  type: path
components:
  schemas:
    AuthUser:
      properties:
        createdAt:
          type: number
          description: UNIX timestamp (in milliseconds) when the User account was created.
          example: 1630748523395
        softBlock:
          nullable: true
          properties:
            blockedAt:
              type: number
            reason:
              type: string
              enum:
                - SUBSCRIPTION_CANCELED
                - SUBSCRIPTION_EXPIRED
                - UNPAID_INVOICE
                - ENTERPRISE_TRIAL_ENDED
                - FAIR_USE_LIMITS_EXCEEDED
                - BLOCKED_FOR_PLATFORM_ABUSE
            blockedDueToOverageType:
              type: string
              enum:
                - analyticsUsage
                - artifacts
                - bandwidth
                - blobTotalAdvancedRequests
                - blobTotalAvgSizeInBytes
                - blobTotalGetResponseObjectSizeInBytes
                - blobTotalSimpleRequests
                - connectDataTransfer
                - dataCacheRead
                - dataCacheWrite
                - edgeConfigRead
                - edgeConfigWrite
                - edgeFunctionExecutionUnits
                - edgeMiddlewareInvocations
                - edgeRequestAdditionalCpuDuration
                - edgeRequest
                - elasticConcurrencyBuildSlots
                - fastDataTransfer
                - fastOriginTransfer
                - fluidCpuDuration
                - fluidDuration
                - functionDuration
                - functionInvocation
                - imageOptimizationCacheRead
                - imageOptimizationCacheWrite
                - imageOptimizationTransformation
                - logDrainsVolume
                - monitoringMetric
                - blobDataTransfer
                - observabilityEvent
                - onDemandConcurrencyMinutes
                - runtimeCacheRead
                - runtimeCacheWrite
                - serverlessFunctionExecution
                - sourceImages
                - wafOwaspExcessBytes
                - wafOwaspRequests
                - wafRateLimitRequest
                - webAnalyticsEvent
          required:
            - blockedAt
            - reason
          type: object
          description: >-
            When the User account has been "soft blocked", this property will
            contain the date when the restriction was enacted, and the
            identifier for why.
        billing:
          nullable: true
          type: object
          description: >-
            An object containing billing infomation associated with the User
            account.
        resourceConfig:
          properties:
            nodeType:
              type: string
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            concurrentBuilds:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            elasticConcurrencyEnabled:
              type: boolean
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            buildEntitlements:
              properties:
                enhancedBuilds:
                  type: boolean
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
              type: object
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            buildQueue:
              properties:
                configuration:
                  type: string
                  enum:
                    - SKIP_NAMESPACE_QUEUE
                    - WAIT_FOR_NAMESPACE_QUEUE
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
              type: object
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            awsAccountType:
              type: string
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            awsAccountIds:
              items:
                type: string
              type: array
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            cfZoneName:
              type: string
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            imageOptimizationType:
              type: string
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            edgeConfigs:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            edgeConfigSize:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            edgeFunctionMaxSizeBytes:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            edgeFunctionExecutionTimeoutMs:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            serverlessFunctionMaxMemorySize:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            kvDatabases:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            postgresDatabases:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            blobStores:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            integrationStores:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            cronJobs:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            cronJobsPerProject:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            microfrontendGroupsPerTeam:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            microfrontendProjectsPerGroup:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            flagsExplorerOverridesThreshold:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            flagsExplorerUnlimitedOverrides:
              type: boolean
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            customEnvironmentsPerProject:
              type: number
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            buildMachine:
              properties:
                purchaseType:
                  type: string
                  enum:
                    - enhanced
                    - turbo
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
                isDefaultBuildMachine:
                  type: boolean
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
                cores:
                  type: number
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
                memory:
                  type: number
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
              type: object
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
            security:
              properties:
                customRules:
                  type: number
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
                ipBlocks:
                  type: number
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
                ipBypass:
                  type: number
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
                rateLimit:
                  type: number
                  description: >-
                    An object containing infomation related to the amount of
                    platform resources may be allocated to the User account.
              type: object
              description: >-
                An object containing infomation related to the amount of
                platform resources may be allocated to the User account.
          type: object
          description: >-
            An object containing infomation related to the amount of platform
            resources may be allocated to the User account.
        stagingPrefix:
          type: string
          description: >-
            Prefix that will be used in the URL of "Preview" deployments created
            by the User account.
        activeDashboardViews:
          items:
            properties:
              scopeId:
                type: string
              viewPreference:
                nullable: true
                type: string
                enum:
                  - list
                  - cards
              favoritesViewPreference:
                nullable: true
                type: string
                enum:
                  - open
                  - closed
              recentsViewPreference:
                nullable: true
                type: string
                enum:
                  - open
                  - closed
            required:
              - scopeId
            type: object
            description: set of dashboard view preferences (cards or list) per scopeId
          type: array
          description: set of dashboard view preferences (cards or list) per scopeId
        importFlowGitNamespace:
          nullable: true
          oneOf:
            - type: string
            - type: number
        importFlowGitNamespaceId:
          nullable: true
          oneOf:
            - type: string
            - type: number
        importFlowGitProvider:
          nullable: true
          type: string
          enum:
            - gitlab
            - bitbucket
            - github
            - github-limited
            - github-custom-host
        preferredScopesAndGitNamespaces:
          items:
            properties:
              scopeId:
                type: string
              gitNamespaceId:
                nullable: true
                oneOf:
                  - type: string
                  - type: number
            required:
              - scopeId
              - gitNamespaceId
            type: object
          type: array
        dismissedToasts:
          items:
            properties:
              name:
                type: string
              dismissals:
                items:
                  properties:
                    scopeId:
                      type: string
                    createdAt:
                      type: number
                  required:
                    - scopeId
                    - createdAt
                  type: object
                type: array
            required:
              - name
              - dismissals
            type: object
            description: A record of when, under a certain scopeId, a toast was dismissed
          type: array
          description: A record of when, under a certain scopeId, a toast was dismissed
        favoriteProjectsAndSpaces:
          items:
            properties:
              teamId:
                type: string
              projectId:
                type: string
            required:
              - teamId
              - projectId
            type: object
            description: >-
              A list of projects and spaces across teams that a user has marked
              as a favorite.
          type: array
          description: >-
            A list of projects and spaces across teams that a user has marked as
            a favorite.
        hasTrialAvailable:
          type: boolean
          description: Whether the user has a trial available for a paid plan subscription.
        remoteCaching:
          properties:
            enabled:
              type: boolean
          type: object
          description: remote caching settings
        dataCache:
          properties:
            excessBillingEnabled:
              type: boolean
          type: object
          description: data cache settings
        featureBlocks:
          properties:
            webAnalytics:
              properties:
                blockedFrom:
                  type: number
                blockedUntil:
                  type: number
                isCurrentlyBlocked:
                  type: boolean
              required:
                - isCurrentlyBlocked
              type: object
          type: object
          description: Feature blocks for the user
        id:
          type: string
          description: The User's unique identifier.
          example: AEIIDYVk59zbFF2Sxfyxxmua
        email:
          type: string
          description: Email address associated with the User account.
          example: me@example.com
        name:
          nullable: true
          type: string
          description: >-
            Name associated with the User account, or `null` if none has been
            provided.
          example: John Doe
        username:
          type: string
          description: Unique username associated with the User account.
          example: jdoe
        avatar:
          nullable: true
          type: string
          description: >-
            SHA1 hash of the avatar for the User account. Can be used in
            conjuction with the ... endpoint to retrieve the avatar image.
          example: 22cb30c85ff45ac4c72de8981500006b28114aa1
        defaultTeamId:
          nullable: true
          type: string
          description: The user's default team.
      required:
        - createdAt
        - softBlock
        - billing
        - resourceConfig
        - stagingPrefix
        - hasTrialAvailable
        - id
        - email
        - name
        - username
        - avatar
        - defaultTeamId
      type: object
      description: Data for the currently authenticated User.
    AuthUserLimited:
      properties:
        limited:
          type: boolean
          description: >-
            Property indicating that this User data contains only limited
            information, due to the authentication token missing privileges to
            read the full User data. Re-login with email, GitHub, GitLab or
            Bitbucket in order to upgrade the authentication token with the
            necessary privileges.
        id:
          type: string
          description: The User's unique identifier.
          example: AEIIDYVk59zbFF2Sxfyxxmua
        email:
          type: string
          description: Email address associated with the User account.
          example: me@example.com
        name:
          nullable: true
          type: string
          description: >-
            Name associated with the User account, or `null` if none has been
            provided.
          example: John Doe
        username:
          type: string
          description: Unique username associated with the User account.
          example: jdoe
        avatar:
          nullable: true
          type: string
          description: >-
            SHA1 hash of the avatar for the User account. Can be used in
            conjuction with the ... endpoint to retrieve the avatar image.
          example: 22cb30c85ff45ac4c72de8981500006b28114aa1
        defaultTeamId:
          nullable: true
          type: string
          description: The user's default team.
      required:
        - limited
        - id
        - email
        - name
        - username
        - avatar
        - defaultTeamId
      type: object
      description: >-
        A limited form of data for the currently authenticated User, due to the
        authentication token missing privileges to read the full User data.

````

--------------------------------------------------------------------------------
title: "List User Events"

last_updated: "2025-11-07T00:37:16.559Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/user/list-user-events"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./35-get-the-active-rolling-release-information-for-a-p.md) | [Index](./index.md) | [Next →](./37-list-user-events.md)
