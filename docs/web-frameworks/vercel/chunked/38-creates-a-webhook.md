**Navigation:** [← Previous](./37-list-user-events.md) | [Index](./index.md) | [Next →](./39-session-tracing.md)

---

# Creates a webhook

> Creates a webhook

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/webhooks
paths:
  path: /v1/webhooks
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
              url:
                allOf:
                  - format: uri
                    pattern: ^https?://
                    type: string
              events:
                allOf:
                  - minItems: 1
                    type: array
                    items:
                      type: string
                      enum:
                        - budget.reached
                        - budget.reset
                        - domain.created
                        - domain.dns.records.changed
                        - domain.transfer-in.started
                        - domain.transfer-in.completed
                        - domain.transfer-in.failed
                        - domain.certificate.add
                        - domain.certificate.add.failed
                        - domain.certificate.renew
                        - domain.certificate.renew.failed
                        - domain.certificate.deleted
                        - domain.renewal
                        - domain.renewal.failed
                        - domain.auto-renew.changed
                        - deployment.created
                        - deployment.cleanup
                        - deployment.error
                        - deployment.canceled
                        - deployment.succeeded
                        - deployment.ready
                        - deployment.check-rerequested
                        - deployment.promoted
                        - deployment.integration.action.start
                        - deployment.integration.action.cancel
                        - deployment.integration.action.cleanup
                        - deployment.checkrun.start
                        - deployment.checkrun.cancel
                        - edge-config.created
                        - edge-config.deleted
                        - edge-config.items.updated
                        - firewall.attack
                        - integration-configuration.permission-upgraded
                        - integration-configuration.removed
                        - integration-configuration.scope-change-confirmed
                        - integration-resource.project-connected
                        - integration-resource.project-disconnected
                        - project.created
                        - project.removed
                        - project.domain.created
                        - project.domain.updated
                        - project.domain.deleted
                        - project.domain.verified
                        - project.domain.unverified
                        - project.domain.moved
                        - project.rolling-release.started
                        - project.rolling-release.aborted
                        - project.rolling-release.completed
                        - project.rolling-release.approved
                        - deployment.checks.failed
                        - deployment.checks.succeeded
                        - deployment-checks-completed
                        - deployment-ready
                        - deployment-prepared
                        - deployment-error
                        - deployment-check-rerequested
                        - deployment-canceled
                        - project-created
                        - project-removed
                        - domain-created
                        - deployment
                        - integration-configuration-permission-updated
                        - integration-configuration-removed
                        - integration-configuration-scope-change-confirmed
                        - marketplace.member.changed
                        - marketplace.invoice.created
                        - marketplace.invoice.paid
                        - marketplace.invoice.notpaid
                        - marketplace.invoice.refunded
                        - observability.anomaly
                        - observability.anomaly-error
                        - observability.usage-anomaly
                        - observability.error-anomaly
                        - observability.anomaly-botId
                        - test-webhook
                      x-speakeasy-enums:
                        budget.reached: BudgetReached
                        budget.reset: BudgetReset
                        domain.created: DomainCreated
                        domain.dns.records.changed: DomainDnsRecordsChanged
                        domain.transfer-in.started: DomainTransferInStarted
                        domain.transfer-in.completed: DomainTransferInCompleted
                        domain.transfer-in.failed: DomainTransferInFailed
                        domain.certificate.add: DomainCertificateAdd
                        domain.certificate.add.failed: DomainCertificateAddFailed
                        domain.certificate.renew: DomainCertificateRenew
                        domain.certificate.renew.failed: DomainCertificateRenewFailed
                        domain.certificate.deleted: DomainCertificateDeleted
                        domain.renewal: DomainRenewal
                        domain.renewal.failed: DomainRenewalFailed
                        domain.auto-renew.changed: DomainAutoRenewChanged
                        deployment.created: DeploymentCreated
                        deployment.cleanup: DeploymentCleanup
                        deployment.error: DeploymentError
                        deployment.canceled: DeploymentCanceled
                        deployment.succeeded: DeploymentSucceeded
                        deployment.ready: DeploymentReady
                        deployment.check-rerequested: DeploymentCheckRerequested
                        deployment.promoted: DeploymentPromoted
                        deployment.integration.action.start: DeploymentIntegrationActionStart
                        deployment.integration.action.cancel: DeploymentIntegrationActionCancel
                        deployment.integration.action.cleanup: DeploymentIntegrationActionCleanup
                        deployment.checkrun.start: DeploymentCheckrunStart
                        deployment.checkrun.cancel: DeploymentCheckrunCancel
                        edge-config.created: EdgeConfigCreated
                        edge-config.deleted: EdgeConfigDeleted
                        edge-config.items.updated: EdgeConfigItemsUpdated
                        firewall.attack: FirewallAttack
                        integration-configuration.permission-upgraded: IntegrationConfigurationPermissionUpgraded
                        integration-configuration.removed: IntegrationConfigurationRemoved
                        integration-configuration.scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmed
                        integration-resource.project-connected: IntegrationResourceProjectConnected
                        integration-resource.project-disconnected: IntegrationResourceProjectDisconnected
                        project.created: ProjectCreated
                        project.removed: ProjectRemoved
                        project.domain.created: ProjectDomainCreated
                        project.domain.updated: ProjectDomainUpdated
                        project.domain.deleted: ProjectDomainDeleted
                        project.domain.verified: ProjectDomainVerified
                        project.domain.unverified: ProjectDomainUnverified
                        project.domain.moved: ProjectDomainMoved
                        project.rolling-release.started: ProjectRollingReleaseStarted
                        project.rolling-release.aborted: ProjectRollingReleaseAborted
                        project.rolling-release.completed: ProjectRollingReleaseCompleted
                        project.rolling-release.approved: ProjectRollingReleaseApproved
                        deployment.checks.failed: DeploymentChecksFailed
                        deployment.checks.succeeded: DeploymentChecksSucceeded
                        deployment-checks-completed: DeploymentChecksCompleted
                        deployment-ready: DeploymentReadyHyphen
                        deployment-prepared: DeploymentPreparedHyphen
                        deployment-error: DeploymentErrorHyphen
                        deployment-check-rerequested: DeploymentCheckRerequestedHyphen
                        deployment-canceled: DeploymentCanceledHyphen
                        project-created: ProjectCreatedHyphen
                        project-removed: ProjectRemovedHyphen
                        domain-created: DomainCreatedHyphen
                        deployment: Deployment
                        integration-configuration-permission-updated: IntegrationConfigurationPermissionUpdatedHyphen
                        integration-configuration-removed: IntegrationConfigurationRemovedHyphen
                        integration-configuration-scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmedHyphen
                        marketplace.invoice.created: MarketplaceInvoiceCreated
                        marketplace.invoice.paid: MarketplaceInvoicePaid
                        marketplace.invoice.notpaid: MarketplaceInvoiceNotpaid
                        marketplace.invoice.refunded: MarketplaceInvoiceRefunded
                        observability.anomaly: ObservabilityAnomaly
                        observability.anomaly-error: ObservabilityAnomalyError
                        test-webhook: TestWebhook
              projectIds:
                allOf:
                  - minItems: 1
                    maxItems: 50
                    type: array
                    items:
                      pattern: ^[a-zA-z0-9_]+$
                      type: string
            required: true
            requiredProperties:
              - url
              - events
            additionalProperties: false
        examples:
          example:
            value:
              url: <string>
              events:
                - budget.reached
              projectIds:
                - <string>
    codeSamples:
      - label: createWebhook
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Webhooks.CreateWebhook(ctx, nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createWebhook
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.webhooks.createWebhook({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                url: "https://experienced-sailor.biz/",
                events: [
                  "domain.auto-renew.changed",
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
              secret:
                allOf:
                  - type: string
                    description: The webhook secret used to sign the payload
              events:
                allOf:
                  - items:
                      type: string
                      enum:
                        - budget.reached
                        - budget.reset
                        - domain.created
                        - domain.dns.records.changed
                        - domain.transfer-in.started
                        - domain.transfer-in.completed
                        - domain.transfer-in.failed
                        - domain.certificate.add
                        - domain.certificate.add.failed
                        - domain.certificate.renew
                        - domain.certificate.renew.failed
                        - domain.certificate.deleted
                        - domain.renewal
                        - domain.renewal.failed
                        - domain.auto-renew.changed
                        - deployment.created
                        - deployment.cleanup
                        - deployment.error
                        - deployment.canceled
                        - deployment.succeeded
                        - deployment.ready
                        - deployment.check-rerequested
                        - deployment.promoted
                        - deployment.integration.action.start
                        - deployment.integration.action.cancel
                        - deployment.integration.action.cleanup
                        - deployment.checkrun.start
                        - deployment.checkrun.cancel
                        - edge-config.created
                        - edge-config.deleted
                        - edge-config.items.updated
                        - firewall.attack
                        - integration-configuration.permission-upgraded
                        - integration-configuration.removed
                        - integration-configuration.scope-change-confirmed
                        - integration-resource.project-connected
                        - integration-resource.project-disconnected
                        - project.created
                        - project.removed
                        - project.domain.created
                        - project.domain.updated
                        - project.domain.deleted
                        - project.domain.verified
                        - project.domain.unverified
                        - project.domain.moved
                        - project.rolling-release.started
                        - project.rolling-release.aborted
                        - project.rolling-release.completed
                        - project.rolling-release.approved
                        - deployment.checks.failed
                        - deployment.checks.succeeded
                        - deployment-checks-completed
                        - deployment-ready
                        - deployment-prepared
                        - deployment-error
                        - deployment-check-rerequested
                        - deployment-canceled
                        - project-created
                        - project-removed
                        - domain-created
                        - deployment
                        - integration-configuration-permission-updated
                        - integration-configuration-removed
                        - integration-configuration-scope-change-confirmed
                        - marketplace.member.changed
                        - marketplace.invoice.created
                        - marketplace.invoice.paid
                        - marketplace.invoice.notpaid
                        - marketplace.invoice.refunded
                        - observability.anomaly
                        - observability.anomaly-error
                        - observability.usage-anomaly
                        - observability.error-anomaly
                        - observability.anomaly-botId
                        - test-webhook
                      description: The webhooks events
                      example: deployment.created
                      x-speakeasy-enums:
                        budget.reached: BudgetReached
                        budget.reset: BudgetReset
                        domain.created: DomainCreated
                        domain.dns.records.changed: DomainDnsRecordsChanged
                        domain.transfer-in.started: DomainTransferInStarted
                        domain.transfer-in.completed: DomainTransferInCompleted
                        domain.transfer-in.failed: DomainTransferInFailed
                        domain.certificate.add: DomainCertificateAdd
                        domain.certificate.add.failed: DomainCertificateAddFailed
                        domain.certificate.renew: DomainCertificateRenew
                        domain.certificate.renew.failed: DomainCertificateRenewFailed
                        domain.certificate.deleted: DomainCertificateDeleted
                        domain.renewal: DomainRenewal
                        domain.renewal.failed: DomainRenewalFailed
                        domain.auto-renew.changed: DomainAutoRenewChanged
                        deployment.created: DeploymentCreated
                        deployment.cleanup: DeploymentCleanup
                        deployment.error: DeploymentError
                        deployment.canceled: DeploymentCanceled
                        deployment.succeeded: DeploymentSucceeded
                        deployment.ready: DeploymentReady
                        deployment.check-rerequested: DeploymentCheckRerequested
                        deployment.promoted: DeploymentPromoted
                        deployment.integration.action.start: DeploymentIntegrationActionStart
                        deployment.integration.action.cancel: DeploymentIntegrationActionCancel
                        deployment.integration.action.cleanup: DeploymentIntegrationActionCleanup
                        deployment.checkrun.start: DeploymentCheckrunStart
                        deployment.checkrun.cancel: DeploymentCheckrunCancel
                        edge-config.created: EdgeConfigCreated
                        edge-config.deleted: EdgeConfigDeleted
                        edge-config.items.updated: EdgeConfigItemsUpdated
                        firewall.attack: FirewallAttack
                        integration-configuration.permission-upgraded: IntegrationConfigurationPermissionUpgraded
                        integration-configuration.removed: IntegrationConfigurationRemoved
                        integration-configuration.scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmed
                        integration-resource.project-connected: IntegrationResourceProjectConnected
                        integration-resource.project-disconnected: IntegrationResourceProjectDisconnected
                        project.created: ProjectCreated
                        project.removed: ProjectRemoved
                        project.domain.created: ProjectDomainCreated
                        project.domain.updated: ProjectDomainUpdated
                        project.domain.deleted: ProjectDomainDeleted
                        project.domain.verified: ProjectDomainVerified
                        project.domain.unverified: ProjectDomainUnverified
                        project.domain.moved: ProjectDomainMoved
                        project.rolling-release.started: ProjectRollingReleaseStarted
                        project.rolling-release.aborted: ProjectRollingReleaseAborted
                        project.rolling-release.completed: ProjectRollingReleaseCompleted
                        project.rolling-release.approved: ProjectRollingReleaseApproved
                        deployment.checks.failed: DeploymentChecksFailed
                        deployment.checks.succeeded: DeploymentChecksSucceeded
                        deployment-checks-completed: DeploymentChecksCompleted
                        deployment-ready: DeploymentReadyHyphen
                        deployment-prepared: DeploymentPreparedHyphen
                        deployment-error: DeploymentErrorHyphen
                        deployment-check-rerequested: DeploymentCheckRerequestedHyphen
                        deployment-canceled: DeploymentCanceledHyphen
                        project-created: ProjectCreatedHyphen
                        project-removed: ProjectRemovedHyphen
                        domain-created: DomainCreatedHyphen
                        deployment: Deployment
                        integration-configuration-permission-updated: IntegrationConfigurationPermissionUpdatedHyphen
                        integration-configuration-removed: IntegrationConfigurationRemovedHyphen
                        integration-configuration-scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmedHyphen
                        marketplace.invoice.created: MarketplaceInvoiceCreated
                        marketplace.invoice.paid: MarketplaceInvoicePaid
                        marketplace.invoice.notpaid: MarketplaceInvoiceNotpaid
                        marketplace.invoice.refunded: MarketplaceInvoiceRefunded
                        observability.anomaly: ObservabilityAnomaly
                        observability.anomaly-error: ObservabilityAnomalyError
                        test-webhook: TestWebhook
                    type: array
                    description: The webhooks events
                    example: deployment.created
              id:
                allOf:
                  - type: string
                    description: The webhook id
                    example: account_hook_GflD6EYyo7F4ViYS
              url:
                allOf:
                  - type: string
                    description: A string with the URL of the webhook
                    example: https://my-webhook.com
              ownerId:
                allOf:
                  - type: string
                    description: The unique ID of the team the webhook belongs to
                    example: ZspSRT4ljIEEmMHgoDwKWDei
              createdAt:
                allOf:
                  - type: number
                    description: >-
                      A number containing the date when the webhook was created
                      in in milliseconds
                    example: 1567024758130
              updatedAt:
                allOf:
                  - type: number
                    description: >-
                      A number containing the date when the webhook was updated
                      in in milliseconds
                    example: 1567024758130
              projectIds:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: The ID of the projects the webhook is associated with
                    example:
                      - prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
            requiredProperties:
              - secret
              - events
              - id
              - url
              - ownerId
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              secret: <string>
              events: deployment.created
              id: account_hook_GflD6EYyo7F4ViYS
              url: https://my-webhook.com
              ownerId: ZspSRT4ljIEEmMHgoDwKWDei
              createdAt: 1567024758130
              updatedAt: 1567024758130
              projectIds:
                - prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
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
title: "Deletes a webhook"

last_updated: "2025-11-07T00:37:16.424Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/webhooks/deletes-a-webhook"
--------------------------------------------------------------------------------

# Deletes a webhook

> Deletes a webhook

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/webhooks/{id}
paths:
  path: /v1/webhooks/{id}
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
      - label: deleteWebhook
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Webhooks.DeleteWebhook(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: deleteWebhook
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.webhooks.deleteWebhook({
              id: "<id>",
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
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get a list of webhooks"

last_updated: "2025-11-07T00:37:16.452Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/webhooks/get-a-list-of-webhooks"
--------------------------------------------------------------------------------

# Get a list of webhooks

> Get a list of webhooks

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/webhooks
paths:
  path: /v1/webhooks
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
        projectId:
          schema:
            - type: string
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
      - label: getWebhooks
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Webhooks.GetWebhooks(ctx, nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: getWebhooks
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.webhooks.getWebhooks({
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
                    projectsMetadata:
                      nullable: true
                      items:
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
                    events:
                      items:
                        type: string
                        enum:
                          - budget.reached
                          - budget.reset
                          - domain.created
                          - domain.dns.records.changed
                          - domain.transfer-in.started
                          - domain.transfer-in.completed
                          - domain.transfer-in.failed
                          - domain.certificate.add
                          - domain.certificate.add.failed
                          - domain.certificate.renew
                          - domain.certificate.renew.failed
                          - domain.certificate.deleted
                          - domain.renewal
                          - domain.renewal.failed
                          - domain.auto-renew.changed
                          - deployment.created
                          - deployment.cleanup
                          - deployment.error
                          - deployment.canceled
                          - deployment.succeeded
                          - deployment.ready
                          - deployment.check-rerequested
                          - deployment.promoted
                          - deployment.integration.action.start
                          - deployment.integration.action.cancel
                          - deployment.integration.action.cleanup
                          - deployment.checkrun.start
                          - deployment.checkrun.cancel
                          - edge-config.created
                          - edge-config.deleted
                          - edge-config.items.updated
                          - firewall.attack
                          - integration-configuration.permission-upgraded
                          - integration-configuration.removed
                          - integration-configuration.scope-change-confirmed
                          - integration-resource.project-connected
                          - integration-resource.project-disconnected
                          - project.created
                          - project.removed
                          - project.domain.created
                          - project.domain.updated
                          - project.domain.deleted
                          - project.domain.verified
                          - project.domain.unverified
                          - project.domain.moved
                          - project.rolling-release.started
                          - project.rolling-release.aborted
                          - project.rolling-release.completed
                          - project.rolling-release.approved
                          - deployment.checks.failed
                          - deployment.checks.succeeded
                          - deployment-checks-completed
                          - deployment-ready
                          - deployment-prepared
                          - deployment-error
                          - deployment-check-rerequested
                          - deployment-canceled
                          - project-created
                          - project-removed
                          - domain-created
                          - deployment
                          - integration-configuration-permission-updated
                          - integration-configuration-removed
                          - integration-configuration-scope-change-confirmed
                          - marketplace.member.changed
                          - marketplace.invoice.created
                          - marketplace.invoice.paid
                          - marketplace.invoice.notpaid
                          - marketplace.invoice.refunded
                          - observability.anomaly
                          - observability.anomaly-error
                          - observability.usage-anomaly
                          - observability.error-anomaly
                          - observability.anomaly-botId
                          - test-webhook
                        description: The webhooks events
                        example: deployment.created
                        x-speakeasy-enums:
                          budget.reached: BudgetReached
                          budget.reset: BudgetReset
                          domain.created: DomainCreated
                          domain.dns.records.changed: DomainDnsRecordsChanged
                          domain.transfer-in.started: DomainTransferInStarted
                          domain.transfer-in.completed: DomainTransferInCompleted
                          domain.transfer-in.failed: DomainTransferInFailed
                          domain.certificate.add: DomainCertificateAdd
                          domain.certificate.add.failed: DomainCertificateAddFailed
                          domain.certificate.renew: DomainCertificateRenew
                          domain.certificate.renew.failed: DomainCertificateRenewFailed
                          domain.certificate.deleted: DomainCertificateDeleted
                          domain.renewal: DomainRenewal
                          domain.renewal.failed: DomainRenewalFailed
                          domain.auto-renew.changed: DomainAutoRenewChanged
                          deployment.created: DeploymentCreated
                          deployment.cleanup: DeploymentCleanup
                          deployment.error: DeploymentError
                          deployment.canceled: DeploymentCanceled
                          deployment.succeeded: DeploymentSucceeded
                          deployment.ready: DeploymentReady
                          deployment.check-rerequested: DeploymentCheckRerequested
                          deployment.promoted: DeploymentPromoted
                          deployment.integration.action.start: DeploymentIntegrationActionStart
                          deployment.integration.action.cancel: DeploymentIntegrationActionCancel
                          deployment.integration.action.cleanup: DeploymentIntegrationActionCleanup
                          deployment.checkrun.start: DeploymentCheckrunStart
                          deployment.checkrun.cancel: DeploymentCheckrunCancel
                          edge-config.created: EdgeConfigCreated
                          edge-config.deleted: EdgeConfigDeleted
                          edge-config.items.updated: EdgeConfigItemsUpdated
                          firewall.attack: FirewallAttack
                          integration-configuration.permission-upgraded: IntegrationConfigurationPermissionUpgraded
                          integration-configuration.removed: IntegrationConfigurationRemoved
                          integration-configuration.scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmed
                          integration-resource.project-connected: IntegrationResourceProjectConnected
                          integration-resource.project-disconnected: IntegrationResourceProjectDisconnected
                          project.created: ProjectCreated
                          project.removed: ProjectRemoved
                          project.domain.created: ProjectDomainCreated
                          project.domain.updated: ProjectDomainUpdated
                          project.domain.deleted: ProjectDomainDeleted
                          project.domain.verified: ProjectDomainVerified
                          project.domain.unverified: ProjectDomainUnverified
                          project.domain.moved: ProjectDomainMoved
                          project.rolling-release.started: ProjectRollingReleaseStarted
                          project.rolling-release.aborted: ProjectRollingReleaseAborted
                          project.rolling-release.completed: ProjectRollingReleaseCompleted
                          project.rolling-release.approved: ProjectRollingReleaseApproved
                          deployment.checks.failed: DeploymentChecksFailed
                          deployment.checks.succeeded: DeploymentChecksSucceeded
                          deployment-checks-completed: DeploymentChecksCompleted
                          deployment-ready: DeploymentReadyHyphen
                          deployment-prepared: DeploymentPreparedHyphen
                          deployment-error: DeploymentErrorHyphen
                          deployment-check-rerequested: DeploymentCheckRerequestedHyphen
                          deployment-canceled: DeploymentCanceledHyphen
                          project-created: ProjectCreatedHyphen
                          project-removed: ProjectRemovedHyphen
                          domain-created: DomainCreatedHyphen
                          deployment: Deployment
                          integration-configuration-permission-updated: IntegrationConfigurationPermissionUpdatedHyphen
                          integration-configuration-removed: IntegrationConfigurationRemovedHyphen
                          integration-configuration-scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmedHyphen
                          marketplace.invoice.created: MarketplaceInvoiceCreated
                          marketplace.invoice.paid: MarketplaceInvoicePaid
                          marketplace.invoice.notpaid: MarketplaceInvoiceNotpaid
                          marketplace.invoice.refunded: MarketplaceInvoiceRefunded
                          observability.anomaly: ObservabilityAnomaly
                          observability.anomaly-error: ObservabilityAnomalyError
                          test-webhook: TestWebhook
                      type: array
                      description: The webhooks events
                      example: deployment.created
                    id:
                      type: string
                      description: The webhook id
                      example: account_hook_GflD6EYyo7F4ViYS
                    url:
                      type: string
                      description: A string with the URL of the webhook
                      example: https://my-webhook.com
                    ownerId:
                      type: string
                      description: The unique ID of the team the webhook belongs to
                      example: ZspSRT4ljIEEmMHgoDwKWDei
                    createdAt:
                      type: number
                      description: >-
                        A number containing the date when the webhook was
                        created in in milliseconds
                      example: 1567024758130
                    updatedAt:
                      type: number
                      description: >-
                        A number containing the date when the webhook was
                        updated in in milliseconds
                      example: 1567024758130
                    projectIds:
                      items:
                        type: string
                      type: array
                      description: The ID of the projects the webhook is associated with
                      example:
                        - prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                  required:
                    - projectsMetadata
                    - events
                    - id
                    - url
                    - ownerId
                    - createdAt
                    - updatedAt
                  type: object
          - type: array
            items:
              allOf:
                - properties:
                    events:
                      items:
                        type: string
                        enum:
                          - budget.reached
                          - budget.reset
                          - domain.created
                          - domain.dns.records.changed
                          - domain.transfer-in.started
                          - domain.transfer-in.completed
                          - domain.transfer-in.failed
                          - domain.certificate.add
                          - domain.certificate.add.failed
                          - domain.certificate.renew
                          - domain.certificate.renew.failed
                          - domain.certificate.deleted
                          - domain.renewal
                          - domain.renewal.failed
                          - domain.auto-renew.changed
                          - deployment.created
                          - deployment.cleanup
                          - deployment.error
                          - deployment.canceled
                          - deployment.succeeded
                          - deployment.ready
                          - deployment.check-rerequested
                          - deployment.promoted
                          - deployment.integration.action.start
                          - deployment.integration.action.cancel
                          - deployment.integration.action.cleanup
                          - deployment.checkrun.start
                          - deployment.checkrun.cancel
                          - edge-config.created
                          - edge-config.deleted
                          - edge-config.items.updated
                          - firewall.attack
                          - integration-configuration.permission-upgraded
                          - integration-configuration.removed
                          - integration-configuration.scope-change-confirmed
                          - integration-resource.project-connected
                          - integration-resource.project-disconnected
                          - project.created
                          - project.removed
                          - project.domain.created
                          - project.domain.updated
                          - project.domain.deleted
                          - project.domain.verified
                          - project.domain.unverified
                          - project.domain.moved
                          - project.rolling-release.started
                          - project.rolling-release.aborted
                          - project.rolling-release.completed
                          - project.rolling-release.approved
                          - deployment.checks.failed
                          - deployment.checks.succeeded
                          - deployment-checks-completed
                          - deployment-ready
                          - deployment-prepared
                          - deployment-error
                          - deployment-check-rerequested
                          - deployment-canceled
                          - project-created
                          - project-removed
                          - domain-created
                          - deployment
                          - integration-configuration-permission-updated
                          - integration-configuration-removed
                          - integration-configuration-scope-change-confirmed
                          - marketplace.member.changed
                          - marketplace.invoice.created
                          - marketplace.invoice.paid
                          - marketplace.invoice.notpaid
                          - marketplace.invoice.refunded
                          - observability.anomaly
                          - observability.anomaly-error
                          - observability.usage-anomaly
                          - observability.error-anomaly
                          - observability.anomaly-botId
                          - test-webhook
                        description: The webhooks events
                        example: deployment.created
                        x-speakeasy-enums:
                          budget.reached: BudgetReached
                          budget.reset: BudgetReset
                          domain.created: DomainCreated
                          domain.dns.records.changed: DomainDnsRecordsChanged
                          domain.transfer-in.started: DomainTransferInStarted
                          domain.transfer-in.completed: DomainTransferInCompleted
                          domain.transfer-in.failed: DomainTransferInFailed
                          domain.certificate.add: DomainCertificateAdd
                          domain.certificate.add.failed: DomainCertificateAddFailed
                          domain.certificate.renew: DomainCertificateRenew
                          domain.certificate.renew.failed: DomainCertificateRenewFailed
                          domain.certificate.deleted: DomainCertificateDeleted
                          domain.renewal: DomainRenewal
                          domain.renewal.failed: DomainRenewalFailed
                          domain.auto-renew.changed: DomainAutoRenewChanged
                          deployment.created: DeploymentCreated
                          deployment.cleanup: DeploymentCleanup
                          deployment.error: DeploymentError
                          deployment.canceled: DeploymentCanceled
                          deployment.succeeded: DeploymentSucceeded
                          deployment.ready: DeploymentReady
                          deployment.check-rerequested: DeploymentCheckRerequested
                          deployment.promoted: DeploymentPromoted
                          deployment.integration.action.start: DeploymentIntegrationActionStart
                          deployment.integration.action.cancel: DeploymentIntegrationActionCancel
                          deployment.integration.action.cleanup: DeploymentIntegrationActionCleanup
                          deployment.checkrun.start: DeploymentCheckrunStart
                          deployment.checkrun.cancel: DeploymentCheckrunCancel
                          edge-config.created: EdgeConfigCreated
                          edge-config.deleted: EdgeConfigDeleted
                          edge-config.items.updated: EdgeConfigItemsUpdated
                          firewall.attack: FirewallAttack
                          integration-configuration.permission-upgraded: IntegrationConfigurationPermissionUpgraded
                          integration-configuration.removed: IntegrationConfigurationRemoved
                          integration-configuration.scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmed
                          integration-resource.project-connected: IntegrationResourceProjectConnected
                          integration-resource.project-disconnected: IntegrationResourceProjectDisconnected
                          project.created: ProjectCreated
                          project.removed: ProjectRemoved
                          project.domain.created: ProjectDomainCreated
                          project.domain.updated: ProjectDomainUpdated
                          project.domain.deleted: ProjectDomainDeleted
                          project.domain.verified: ProjectDomainVerified
                          project.domain.unverified: ProjectDomainUnverified
                          project.domain.moved: ProjectDomainMoved
                          project.rolling-release.started: ProjectRollingReleaseStarted
                          project.rolling-release.aborted: ProjectRollingReleaseAborted
                          project.rolling-release.completed: ProjectRollingReleaseCompleted
                          project.rolling-release.approved: ProjectRollingReleaseApproved
                          deployment.checks.failed: DeploymentChecksFailed
                          deployment.checks.succeeded: DeploymentChecksSucceeded
                          deployment-checks-completed: DeploymentChecksCompleted
                          deployment-ready: DeploymentReadyHyphen
                          deployment-prepared: DeploymentPreparedHyphen
                          deployment-error: DeploymentErrorHyphen
                          deployment-check-rerequested: DeploymentCheckRerequestedHyphen
                          deployment-canceled: DeploymentCanceledHyphen
                          project-created: ProjectCreatedHyphen
                          project-removed: ProjectRemovedHyphen
                          domain-created: DomainCreatedHyphen
                          deployment: Deployment
                          integration-configuration-permission-updated: IntegrationConfigurationPermissionUpdatedHyphen
                          integration-configuration-removed: IntegrationConfigurationRemovedHyphen
                          integration-configuration-scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmedHyphen
                          marketplace.invoice.created: MarketplaceInvoiceCreated
                          marketplace.invoice.paid: MarketplaceInvoicePaid
                          marketplace.invoice.notpaid: MarketplaceInvoiceNotpaid
                          marketplace.invoice.refunded: MarketplaceInvoiceRefunded
                          observability.anomaly: ObservabilityAnomaly
                          observability.anomaly-error: ObservabilityAnomalyError
                          test-webhook: TestWebhook
                      type: array
                      description: The webhooks events
                      example: deployment.created
                    id:
                      type: string
                      description: The webhook id
                      example: account_hook_GflD6EYyo7F4ViYS
                    url:
                      type: string
                      description: A string with the URL of the webhook
                      example: https://my-webhook.com
                    ownerId:
                      type: string
                      description: The unique ID of the team the webhook belongs to
                      example: ZspSRT4ljIEEmMHgoDwKWDei
                    createdAt:
                      type: number
                      description: >-
                        A number containing the date when the webhook was
                        created in in milliseconds
                      example: 1567024758130
                    updatedAt:
                      type: number
                      description: >-
                        A number containing the date when the webhook was
                        updated in in milliseconds
                      example: 1567024758130
                    projectIds:
                      items:
                        type: string
                      type: array
                      description: The ID of the projects the webhook is associated with
                      example:
                        - prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                  required:
                    - events
                    - id
                    - url
                    - ownerId
                    - createdAt
                    - updatedAt
                  type: object
        examples:
          example:
            value:
              - projectsMetadata:
                  - id: <string>
                    name: <string>
                    framework: blitzjs
                    latestDeployment: <string>
                events: deployment.created
                id: account_hook_GflD6EYyo7F4ViYS
                url: https://my-webhook.com
                ownerId: ZspSRT4ljIEEmMHgoDwKWDei
                createdAt: 1567024758130
                updatedAt: 1567024758130
                projectIds:
                  - prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
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
title: "Get a webhook"

last_updated: "2025-11-07T00:37:16.390Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/webhooks/get-a-webhook"
--------------------------------------------------------------------------------

# Get a webhook

> Get a webhook

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/webhooks/{id}
paths:
  path: /v1/webhooks/{id}
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
      - label: getWebhook
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Webhooks.GetWebhook(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getWebhook
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.webhooks.getWebhook({
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
              events:
                allOf:
                  - items:
                      type: string
                      enum:
                        - budget.reached
                        - budget.reset
                        - domain.created
                        - domain.dns.records.changed
                        - domain.transfer-in.started
                        - domain.transfer-in.completed
                        - domain.transfer-in.failed
                        - domain.certificate.add
                        - domain.certificate.add.failed
                        - domain.certificate.renew
                        - domain.certificate.renew.failed
                        - domain.certificate.deleted
                        - domain.renewal
                        - domain.renewal.failed
                        - domain.auto-renew.changed
                        - deployment.created
                        - deployment.cleanup
                        - deployment.error
                        - deployment.canceled
                        - deployment.succeeded
                        - deployment.ready
                        - deployment.check-rerequested
                        - deployment.promoted
                        - deployment.integration.action.start
                        - deployment.integration.action.cancel
                        - deployment.integration.action.cleanup
                        - deployment.checkrun.start
                        - deployment.checkrun.cancel
                        - edge-config.created
                        - edge-config.deleted
                        - edge-config.items.updated
                        - firewall.attack
                        - integration-configuration.permission-upgraded
                        - integration-configuration.removed
                        - integration-configuration.scope-change-confirmed
                        - integration-resource.project-connected
                        - integration-resource.project-disconnected
                        - project.created
                        - project.removed
                        - project.domain.created
                        - project.domain.updated
                        - project.domain.deleted
                        - project.domain.verified
                        - project.domain.unverified
                        - project.domain.moved
                        - project.rolling-release.started
                        - project.rolling-release.aborted
                        - project.rolling-release.completed
                        - project.rolling-release.approved
                        - deployment.checks.failed
                        - deployment.checks.succeeded
                        - deployment-checks-completed
                        - deployment-ready
                        - deployment-prepared
                        - deployment-error
                        - deployment-check-rerequested
                        - deployment-canceled
                        - project-created
                        - project-removed
                        - domain-created
                        - deployment
                        - integration-configuration-permission-updated
                        - integration-configuration-removed
                        - integration-configuration-scope-change-confirmed
                        - marketplace.member.changed
                        - marketplace.invoice.created
                        - marketplace.invoice.paid
                        - marketplace.invoice.notpaid
                        - marketplace.invoice.refunded
                        - observability.anomaly
                        - observability.anomaly-error
                        - observability.usage-anomaly
                        - observability.error-anomaly
                        - observability.anomaly-botId
                        - test-webhook
                      description: The webhooks events
                      example: deployment.created
                      x-speakeasy-enums:
                        budget.reached: BudgetReached
                        budget.reset: BudgetReset
                        domain.created: DomainCreated
                        domain.dns.records.changed: DomainDnsRecordsChanged
                        domain.transfer-in.started: DomainTransferInStarted
                        domain.transfer-in.completed: DomainTransferInCompleted
                        domain.transfer-in.failed: DomainTransferInFailed
                        domain.certificate.add: DomainCertificateAdd
                        domain.certificate.add.failed: DomainCertificateAddFailed
                        domain.certificate.renew: DomainCertificateRenew
                        domain.certificate.renew.failed: DomainCertificateRenewFailed
                        domain.certificate.deleted: DomainCertificateDeleted
                        domain.renewal: DomainRenewal
                        domain.renewal.failed: DomainRenewalFailed
                        domain.auto-renew.changed: DomainAutoRenewChanged
                        deployment.created: DeploymentCreated
                        deployment.cleanup: DeploymentCleanup
                        deployment.error: DeploymentError
                        deployment.canceled: DeploymentCanceled
                        deployment.succeeded: DeploymentSucceeded
                        deployment.ready: DeploymentReady
                        deployment.check-rerequested: DeploymentCheckRerequested
                        deployment.promoted: DeploymentPromoted
                        deployment.integration.action.start: DeploymentIntegrationActionStart
                        deployment.integration.action.cancel: DeploymentIntegrationActionCancel
                        deployment.integration.action.cleanup: DeploymentIntegrationActionCleanup
                        deployment.checkrun.start: DeploymentCheckrunStart
                        deployment.checkrun.cancel: DeploymentCheckrunCancel
                        edge-config.created: EdgeConfigCreated
                        edge-config.deleted: EdgeConfigDeleted
                        edge-config.items.updated: EdgeConfigItemsUpdated
                        firewall.attack: FirewallAttack
                        integration-configuration.permission-upgraded: IntegrationConfigurationPermissionUpgraded
                        integration-configuration.removed: IntegrationConfigurationRemoved
                        integration-configuration.scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmed
                        integration-resource.project-connected: IntegrationResourceProjectConnected
                        integration-resource.project-disconnected: IntegrationResourceProjectDisconnected
                        project.created: ProjectCreated
                        project.removed: ProjectRemoved
                        project.domain.created: ProjectDomainCreated
                        project.domain.updated: ProjectDomainUpdated
                        project.domain.deleted: ProjectDomainDeleted
                        project.domain.verified: ProjectDomainVerified
                        project.domain.unverified: ProjectDomainUnverified
                        project.domain.moved: ProjectDomainMoved
                        project.rolling-release.started: ProjectRollingReleaseStarted
                        project.rolling-release.aborted: ProjectRollingReleaseAborted
                        project.rolling-release.completed: ProjectRollingReleaseCompleted
                        project.rolling-release.approved: ProjectRollingReleaseApproved
                        deployment.checks.failed: DeploymentChecksFailed
                        deployment.checks.succeeded: DeploymentChecksSucceeded
                        deployment-checks-completed: DeploymentChecksCompleted
                        deployment-ready: DeploymentReadyHyphen
                        deployment-prepared: DeploymentPreparedHyphen
                        deployment-error: DeploymentErrorHyphen
                        deployment-check-rerequested: DeploymentCheckRerequestedHyphen
                        deployment-canceled: DeploymentCanceledHyphen
                        project-created: ProjectCreatedHyphen
                        project-removed: ProjectRemovedHyphen
                        domain-created: DomainCreatedHyphen
                        deployment: Deployment
                        integration-configuration-permission-updated: IntegrationConfigurationPermissionUpdatedHyphen
                        integration-configuration-removed: IntegrationConfigurationRemovedHyphen
                        integration-configuration-scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmedHyphen
                        marketplace.invoice.created: MarketplaceInvoiceCreated
                        marketplace.invoice.paid: MarketplaceInvoicePaid
                        marketplace.invoice.notpaid: MarketplaceInvoiceNotpaid
                        marketplace.invoice.refunded: MarketplaceInvoiceRefunded
                        observability.anomaly: ObservabilityAnomaly
                        observability.anomaly-error: ObservabilityAnomalyError
                        test-webhook: TestWebhook
                    type: array
                    description: The webhooks events
                    example: deployment.created
              id:
                allOf:
                  - type: string
                    description: The webhook id
                    example: account_hook_GflD6EYyo7F4ViYS
              url:
                allOf:
                  - type: string
                    description: A string with the URL of the webhook
                    example: https://my-webhook.com
              ownerId:
                allOf:
                  - type: string
                    description: The unique ID of the team the webhook belongs to
                    example: ZspSRT4ljIEEmMHgoDwKWDei
              createdAt:
                allOf:
                  - type: number
                    description: >-
                      A number containing the date when the webhook was created
                      in in milliseconds
                    example: 1567024758130
              updatedAt:
                allOf:
                  - type: number
                    description: >-
                      A number containing the date when the webhook was updated
                      in in milliseconds
                    example: 1567024758130
              projectIds:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: The ID of the projects the webhook is associated with
                    example:
                      - prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
            requiredProperties:
              - events
              - id
              - url
              - ownerId
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              events: deployment.created
              id: account_hook_GflD6EYyo7F4ViYS
              url: https://my-webhook.com
              ownerId: ZspSRT4ljIEEmMHgoDwKWDei
              createdAt: 1567024758130
              updatedAt: 1567024758130
              projectIds:
                - prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
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
title: "Errors"

last_updated: "2025-11-07T00:37:16.166Z"
source: "https://vercel.com/docs/rest-api/reference/errors"
--------------------------------------------------------------------------------

# Errors

> List of general and specific errors you may encounter when using the REST API.

## Generic Errors

These error codes are consistent for all endpoints.

### Forbidden

You're not authorized to use the endpoint. This usually happens due to missing an user token.

<Note>Similar to the HTTP 403 Forbidden error.</Note>

```json error-response-forbidden theme={"system"}
{
  "error": {
    "code": "forbidden",
    "message": "Not authorized"
  }
}
```

### Rate Limited

You exceeded the maximum allotted requests.

The limit of request is per endpoint basis so you could continue using another endpoints even if some of them give you this error.

```json error-response-rate-limited theme={"system"}
{
  "error": {
    "code": "rate_limited",
    "message": "The rate limit of 6 exceeded for 'api-www-user-update-username'. Try again in 7 days",
    "limit": {
      "remaining": 0,
      "reset": 1571432075,
      "resetMs": 1571432075563,
      "total": 6
    }
  }
}
```

### Bad Request

There was an error with the request, the `error.message` would contain information about the issue.

```json error-response-bad-request theme={"system"}
{
  "error": {
    "code": "bad_request",
    "message": "An english description of the error that just occurred"
  }
}
```

### Internal Server Error

This errors is similar to the HTTP 500 Internal Server Error error code.

```json error-response-internal-server-error theme={"system"}
{
  "error": {
    "code": "internal_server_error",
    "message": "An unexpected internal error occurred"
  }
}
```

### Resource Not Found

The requested resource could not be found

```json error-response-not-Found theme={"system"}
{
  "error": {
    "code": "not_found",
    "message": "Could not find the RESOURCE: ID"
  }
}
```

### Method Unknown

The endpoint you're requesting does not handle the method you defined. The error message will contain the methods the endpoint responds to.

```json error-response-method-unknown theme={"system"}
{
  "error": {
    "code": "method_unknown",
    "message": "This endpoint only responds to METHOD"
  }
}
```

## Deployment Errors

These error codes can happen when using any [deployment related endpoint](/endpoints/deployments/get-deployment-events).

### Missing Files

Some of the files you defined when creating the deployment are missing.

```json error-response-missing-files theme={"system"}
{
  "error": {
    "code": "missing_files",
    "message": "Missing files",
    "missing": []
  }
}
```

### No Files in the Deployment

You tried to create an empty deployment.

```json error-response-no-files theme={"system"}
{
  "error": {
    "code": "no_files",
    "message": "No files in the deployment"
  }
}
```

### Too Many Environment Variables

The limit of environment variables per deployment is 100 and you defined more. The error message indicates the amount you define.

```json error-response-too-many-env-keys theme={"system"}
{
  "error": {
    "code": "env_too_many_keys",
    "message": "Too many env vars have been supplied (100 max allowed, but got #)"
  }
}
```

<Note>
  `#`is your number of variables.
</Note>

### Environment Variable Key with Invalid Characters

Some environment variable name contains an invalid character. The only valid characters are letters, digits and `_`.

The error message will contain the `KEY` with the problem.

```json error-response-env-key-invalid-characters theme={"system"}
{
  "error": {
    "code": "env_key_invalid_characters",
    "message": "The env key "KEY" contains invalid characters. Only letters, digits and \`_\` are allowed",
    "key": KEY
  }
}
```

### Environment Variable Key with a Long Name

An environment variable name is too long, the maximum permitted name is 256 characters.

The error message contains the environment `KEY`.

```json error-response-env-key-invalid-length theme={"system"}
{
  "error": {
    "code": "env_key_invalid_length",
    "message": "The env key "KEY" exceeds the 256 length limit",
    "key": KEY
  }
}
```

### Environment Variable Value with a Long Name

An environment variable value contains a value too long, the maximum permitted value is 65536 characters.

The error message contains the environment `KEY`.

```json error-response-env-value-invalid-length theme={"system"}
{
  "error": {
    "code": "env_value_invalid_length",
    "message": "The env value for "KEY" exceeds the 65536 length limit",
    "key": KEY,
    "value": VALUE
  }
}
```

### Environment Variable Value Is an Object without UID

The value of an environment variable is object but it doesn't have a `uid`.

The error message contains the environment `KEY` which has the error.

```json error-response-env-value-invalid-type theme={"system"}
{
  "error": {
    "code": "env_value_invalid_type_missing_uid",
    "message": "The env key "KEY" passed an object as a value with no \`uid\` key"
  }
}
```

### Environment Variable Value Is an Object with Unknown Props

The value of an environment variable is an object with unknown attributes, it only can have a `uid` key inside the object.

```json error-response-env-value-invalid-type theme={"system"}
{
  "error": {
    "code": "env_value_invalid_type_unknown_props",
    "message": "The env key "KEY" passed an object with unknown properties. Only \`uid\` is allowed when passing an object"
  }
}
```

### Environment Variable Value with an Invalid Type

An environment variable value passed is of an unsupported type.

The error message contains the environment `KEY`.

```json error-response-env-value-invalid-type theme={"system"}
{
  "error": {
    "code": "env_value_invalid_type",
    "message": "The env key "KEY" passed an unsupported type for its value",
    "key": KEY
  }
}
```

### Not Allowed to Access a Secret

You're trying to use a secret but you don't have access to it.

```json error-response-secret-forbidden theme={"system"}
{
  "error": {
    "code": "env_secret_forbidden",
    "message": "Not allowed to access secret \\"NAME\\"",
    "uid": UID
  }
}
```

### Missing Secret

You're trying to use a secret as an environment value and it doesn't exists.

```json error-response-secret-missing theme={"system"}
{
  "error": {
    "code": "env_secret_missing",
    "message": "Could not find a secret by uid "UID"",
    "uid": UID
  }
}
```

## Domain Errors

These error code could happen when using any [domains related endpoints](/endpoints/domains-registrar/buy-a-domain).

### Domain Forbidden

You don't have access to the domain, this usually mean this domains is owned by another account or team.

The domain is specified in the message and the `DOMAIN` key.

```json error-response-forbidden theme={"system"}
{
  "error": {
    "code": "forbidden",
    "message": "You don't have access to \\"DOMAIN\\"",
    "domain": DOMAIN
  }
}
```

### Domain Not Found

The domain name could not be found in our system. Try to [add it first](/endpoints/domains-registrar/transfer-in-a-domain).

```json error-response-not-found theme={"system"}
{
  "error": {
    "code": "not_found",
    "message": "Domain name not found"
  }
}
```

### Missing Domain Name

The domain name wasn't specified in the URL. This means you tried to use an endpoint which require you to define the domain name in the URL but didn't defined it.

```json error-response-missing-name theme={"system"}
{
  "error": {
    "code": "missing_name",
    "message": "The URL was expected to include the domain name. Example: /domains/google.com"
  }
}
```

### Conflicting Aliases

You must [remove the aliases](/endpoints/aliases/delete-an-alias#delete-an-alias) described in the error before removing the domains.

The aliases are specified in the `ALIASES` key.

```json error-response-conflict-alias theme={"system"}
{
  "error": {
    "code": "conflict_aliases",
    "message": "The following aliases must be removed before removing the domain: ALIASES",
    "aliases": ALIASES
  }
}
```

### Not Modified

When trying to modify a domain nothing was required to change.

```json error-response-not-modified theme={"system"}
{
  "error": {
    "code": "not_modified",
    "message": "Nothing to do"
  }
}
```

### Missing Name for Domain

When trying to add a domain the name wasn't present in the request body.

```json error-response-missing-name theme={"system"}
{
  "error": {
    "code": "missing_name",
    "message": "The `name` field in the body was expected but is not present in the body payload. Example value: `example.com`"
  }
}
```

### Invalid Name for Domain

The domain name defined in the request body is invalid.

The name is specified in the error as the `NAME` key.

```json error-response-invalid-name theme={"system"}
{
  "error": {
    "code": "invalid_name",
    "message": "The \`name\` field contains an invalid domain name ("NAME")",
    "name": NAME
  }
}
```

### Custom Domain Needs a Plan Upgrade

In order to add a custom domain to your account or team you need to upgrade to a paid plan.

```json error-response-domain-needs-upgrade theme={"system"}
{
  "error": {
    "code": "custom_domain_needs_upgrade",
    "message": "Domain name creation requires a premium account."
  }
}
```

### Domain Already Exists

The domain name you're trying to add already exists.

The domain name and its current ID are received in the `NAME` and `DOMAIN_ID` keys.

```json error-response-not-modified theme={"system"}
{
  "error": {
    "code": "not_modified",
    "message": "The domain "NAME" already exists",
    "name": NAME,
    "uid": DOMAIN_ID
  }
}
```

### Can't Create the Domain

The domain name can't be created. Most probably it couldn't be verified.

```json error-response-forbidden theme={"system"}
{
  "error": {
    "code": "forbidden",
    "message": "You don't have permission to create a domain"
  }
}
```

### Failed to Add Domain after Purchase

We were able to purchase a domain for you but we had an error when trying to add it to your account. Please contact us on **[Contact Support](https://vercel.com/help)**.

```json error-response-failed-add-domain theme={"system"}
{
  "error": {
    "code": "failed_to_add_domain",
    "message": "The domain was bought but couldn't be added.
  }
}
```

### Unable to Determine the Domain Price

We're unable to determine the domain price of a domain.

```json error-response-service-unavailable theme={"system"}
{
  "error": {
    "code": "service_unavailable",
    "message": "Failed to determine the domain price"
  }
}
```

### Domain price mismatch

The `expectedPrice` supplied in the request body does not match the actual domain price, which is specified in the `actualPrice` key.

```json error-response-price-mismatch theme={"system"}
{
  "error": {
    "code": "price_mismatch",
    "message": "The expected price does not match the actual price",
    "price": ACTUAL_PRICE
  }
}
```

### Domain Is Not Available

The domain name is not available to be purchased.

```json error-response-not-available theme={"system"}
{
  "error": {
    "code": "not_available",
    "message": "Domain is not available"
  }
}
```

### Invalid Domain Name

The domain name or TLD is invalid or not supported.

```json error-response-invalid-domain theme={"system"}
{
  "error": {
    "code": "invalid_domain",
    "message": "Invalid domain or TLD"
  }
}
```

### Missing DNS Record Name

The DNS record key `name` is required and was not provided. It could be [any valid DNS record](https://en.wikipedia.org/wiki/List_of_DNS_record_types).

```json error-response-missing-type theme={"system"}
{
  "error": {
    "code": "missing_type",
    "message": "Missing `type` parameter"
  }
}
```

## DNS Errors

These error code could happen when using any [DNS related endpoint](/endpoints/dns/list-existing-dns-records).

### Missing DNS Record Name

The DNS record key `name` is required and was not provided. It should be either a subdomain or `@` for the domain itself.

```json error-response-missing-Name theme={"system"}
{
  "error": {
    "code": "missing_name",
    "message": "Missing `name` parameter"
  }
}
```

### Missing DNS Record Type

The DNS record key `name` is required and was not provided. It could be [any valid DNS record](https://en.wikipedia.org/wiki/List_of_DNS_record_types).

```json error-response-missing-type theme={"system"}
{
  "error": {
    "code": "missing_type",
    "message": "Missing `type` parameter"
  }
}
```

## OAuth2 errors

These errors could occur when using any [OAuth2 related endpoint](https://vercel.com/docs/integrations/vercel-api-integrations#create-an-access-token).

### Client Not Found

The OAuth2 client ID could not be found or doesn't exist.

```json error-response-not-found theme={"system"}
{
  "error": {
    "code": "not_found",
    "message": "OAuth client doesn't not found: CLIENT_ID"
  }
}
```


--------------------------------------------------------------------------------
title: "Deployment Automation"

last_updated: "2025-11-07T00:37:16.170Z"
source: "https://vercel.com/docs/rest-api/reference/examples/deployments-automation"
--------------------------------------------------------------------------------

# Deployment Automation

> Learn how to use the Vercel SDK through real-life examples.

## Create a deployment

In this example, you will trigger a new deployment from a GitHub repository and then retrieve its status.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function createAndCheckDeployment() {
  try {
    // Create a new deployment
    const createResponse = await vercel.deployments.createDeployment({
      requestBody: {
        name: 'my-project', //The project name used in the deployment URL
        target: 'production',
        gitSource: {
          type: 'github',
          repo: 'repo-name',
          ref: 'main',
          org: 'org-name', //For a personal account, the org-name is your GH username
        },
      },
    });

    console.log(
      `Deployment created: ID ${createResponse.id} and status ${createResponse.status}`,
    );
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

createAndCheckDeployment();
```

## Create a deployment with alias

In this example, you will create a deployment, wait for it to complete, and then create an alias if successful.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function createDeploymentAndAlias() {
  try {
    // Create a new deployment
    const createResponse = await vercel.deployments.createDeployment({
      requestBody: {
        name: 'my-project', //The project name used in the deployment URL
        target: 'production',
        gitSource: {
          type: 'github',
          repo: 'repo-name',
          ref: 'main',
          org: 'org-name', //For a personal account, the org-name is your GH username
        },
      },
    });

    const deploymentId = createResponse.id;

    console.log(
      `Deployment created: ID ${deploymentId} and status ${createResponse.status}`,
    );

    // Check deployment status
    let deploymentStatus;
    let deploymentURL;
    do {
      await new Promise((resolve) => setTimeout(resolve, 5000)); // Wait 5 seconds between checks

      const statusResponse = await vercel.deployments.getDeployment({
        idOrUrl: deploymentId,
        withGitRepoInfo: 'true',
      });

      deploymentStatus = statusResponse.status;
      deploymentURL = statusResponse.url;
      console.log(`Deployment status: ${deploymentStatus}`);
    } while (
      deploymentStatus === 'BUILDING' ||
      deploymentStatus === 'INITIALIZING'
    );

    if (deploymentStatus === 'READY') {
      console.log(`Deployment successful. URL: ${deploymentURL}`);

      const aliasResponse = await vercel.aliases.assignAlias({
        id: deploymentId,
        requestBody: {
          alias: `my-project-alias.vercel.app`,
          redirect: null,
        },
      });

      console.log(`Alias created: ${aliasResponse.alias}`);
    } else {
      console.log('Deployment failed or was canceled');
    }
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

createDeploymentAndAlias();
```


--------------------------------------------------------------------------------
title: "Domain Management"

last_updated: "2025-11-07T00:37:16.169Z"
source: "https://vercel.com/docs/rest-api/reference/examples/domain-management"
--------------------------------------------------------------------------------

# Domain Management

> Learn how to use the Vercel SDK through real-life examples.

## Add a domain

In this example, you will add a new domain to a project and check its configuration.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function addAndReviewDomain() {
  const domain = 'www.example.com';

  try {
    // Add a new domain
    const addDomainResponse = await vercel.projects.addProjectDomain({
      idOrName: 'my-project', //The project name used in the deployment URL
      requestBody: {
        name: domain,
      },
    });

    console.log(`Domain added: ${addDomainResponse.name}`);
    console.log('Domain Details:', JSON.stringify(addDomainResponse, null, 2));
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

addAndReviewDomain();
```

## Add a domain, verify it and setup a redirect

In this example, you will add a custom domain, verify it, and set up a redirect from a subdomain to the main domain.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function setupDomainWithRedirect() {
  const mainDomain = 'example.com';
  const subDomain = 'hello.example.com';
  const projectName = 'my-project'; //The project name used in the deployment URL

  try {
    // Add main domain
    const mainDomainResponse = await vercel.projects.addProjectDomain({
      idOrName: projectName,
      requestBody: {
        name: mainDomain,
      },
    });

    console.log(`Main domain added: ${mainDomainResponse.name}`);

    const checkConfiguration = await vercel.domains.getDomainConfig({
      domain: mainDomain,
    });

    if (mainDomainResponse.verified && !checkConfiguration.misconfigured) {
      // Add subdomain with 301 redirect to main domain
      const subDomainResponse = await vercel.projects.addProjectDomain({
        idOrName: projectName,
        requestBody: {
          name: subDomain,
          redirect: `https://${mainDomain}`,
          redirectStatusCode: 301,
        },
      });

      console.log(`Subdomain added and redirect set up: ${subDomain}`);
    }
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

setupDomainWithRedirect();
```


--------------------------------------------------------------------------------
title: "Environment Variables"

last_updated: "2025-11-07T00:37:16.410Z"
source: "https://vercel.com/docs/rest-api/reference/examples/environment-variables"
--------------------------------------------------------------------------------

# Environment Variables

> Learn how to use the Vercel SDK through real-life examples.

## Add environment variables to a project

In this example, you will add new environment variables to a project and list the details of the added values.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});
const projectName = 'my-project'; //The project name used in the deployment URL

async function addAndListEnvVars() {
  try {
    // Add new environment variables
    const addResponse = await vercel.projects.createProjectEnv({
      idOrName: projectName,
      upsert: 'true',
      requestBody: [
        {
          key: 'API_KEY',
          value: 'secret_value',
          target: ['production', 'preview'],
          type: 'encrypted',
        },
        {
          key: 'DEBUG',
          value: 'true',
          target: ['development'],
          type: 'plain',
        },
      ],
    });
    console.log(
      'Added environment variables:',
      JSON.stringify(addResponse, null, 2),
    );
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

addAndListEnvVars();
```

## Manage variables across projects

In this example, you manage environment variables across multiple projects and environments.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';
import { OneTarget } from '@vercel/sdk/models/operations/createprojectenv';

const PROJECTS = ['project-id-1', 'project-id-2', 'project-id-3'];
const environments = ['development', 'preview', 'production'];
const VERCEL_TOKEN = process.env.VERCEL_TOKEN;

const vercel = new Vercel({
  bearerToken: VERCEL_TOKEN,
});

async function manageEnvironmentVariables() {
  try {
    const variables = [
      { key: 'API_URL', value: 'https://api.example.com' },
      { key: 'DEBUG', value: 'true', environments: ['development', 'preview'] },
      {
        key: 'SECRET_KEY',
        value: 'super-secret-key',
        encrypt: true,
        environments: ['production', 'preview'],
      },
    ];

    for (const projectId of PROJECTS) {
      console.log(`Managing environment variables for project: ${projectId}`);
      for (const variable of variables) {
        const targets =
          (variable.environments as OneTarget[]) ||
          (environments as OneTarget[]);

        const addEnv = await vercel.projects.createProjectEnv({
          idOrName: projectId,
          upsert: 'true',
          requestBody: {
            key: variable.key,
            value: variable.value,
            target: targets,
            type: variable.encrypt ? 'encrypted' : 'plain',
          },
        });
        console.log(addEnv.created);
      }
      const readEnvs = await vercel.projects.filterProjectEnvs({
        idOrName: projectId,
      });
      console.log(
        'Env Details for ',
        projectId,
        ':',
        JSON.stringify(readEnvs, null, 2),
      );
    }
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

manageEnvironmentVariables();
```


--------------------------------------------------------------------------------
title: "Vercel WAF Management"

last_updated: "2025-11-07T00:37:16.327Z"
source: "https://vercel.com/docs/rest-api/reference/examples/firewall-management"
--------------------------------------------------------------------------------

# Vercel WAF Management

> Learn how to use the Vercel SDK through real-life examples.

## Add custom rules

In this example, you create a new custom rule to protect your application against SQL injection threats.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function insertCustomRule() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", //Not required but sometimes needed if the endpoint requires that you authenticate as a specific team - your token should also have access to this scope
    requestBody: {
      action: "rules.insert",
      id: null, // null for new rules
      value: {
        active: true,
        name: "Block SQL Injection Attempts",
        description: "Block requests with SQL injection patterns in query parameters",
        conditionGroup: [
          {
            conditions: [
              {
                op: "inc", // Contains
                type: "query",
                value: "SELECT",
              },
            ],
          },
        ],
        action: {
          mitigate: {
            action: "deny",
            rateLimit: null,
            redirect: null,
            actionDuration: null,
          },
        },
      },
    },
  });
}

insertCustomRule()
```

## Modify existing rules

In this example, you update an existing custom rule's configuration. This is useful When you need to programmatically adjust conditions, actions, or status of an existing rule.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function updateExistingRule() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", //Not required but sometimes needed if the endpoint requires that you authenticate as a specific team - your token should also have access to this scope
    requestBody: {
      action: "rules.update",
      id: "existing-rule-id", //You can find the id by using the rules array of the Read Firewall Configuration endpoint
      value: {
        active: true,
        name: "Updated Rule Name",
        description: "Updated rule description",
        conditionGroup: [
          {
            conditions: [
              {
                op: "pre",
                type: "path",
                value: "/admin",
              },
            ],
          },
        ],
        action: {
          mitigate: {
            action: "challenge", // Changed from previous setting
            rateLimit: null,
            redirect: null,
            actionDuration: null,
          },
        },
      },
    },
  });
}

updateExistingRule()
```

## Delete custom rules

In this example, you delete an existing custom rule.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function deleteRule() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", //Not required but sometimes needed if the endpoint requires that you authenticate as a specific team - your token should also have access to this scope
    requestBody: {
      action: "rules.remove",
      id: "rule-to-delete-id", //You can find the id by using the rules array of the Read Firewall Configuration endpoint
      value: null, // No value needed for deletion
    },
  });
}

deleteRule()
```

## Change rule priority

This parameter applies when you have more than one custom rule in your project. By default, the priority is determined based on the order in which the rules are added. You can change this in the Vercel dashboard by re-ordering the rules in the [Firewall Configure](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#custom-rule-configuration) project page **or** by using the endpoint below.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function reorderRules() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", //Not required but sometimes needed if the endpoint requires that you authenticate as a specific team - your token should also have access to this scope
    requestBody: {
      action: "rules.priority",
      id: "rule-to-update-priority-id", //You can find the id by using the rules array of the Read Firewall Configuration endpoint
      value: 1, //Use the rules array of the Read Firewall Configuration endpoint to determine what array position you would like this rule to move to. The minimum is 0 and the maximum is the length of the array
    },
  });
}

reorderRules()

```

## Custom system bypass rule

The [WAF system bypass rules](https://vercel.com/docs/vercel-firewall/vercel-waf/system-bypass-rules) allow you to have specific IP addresses or CIDRs bypass the system-level mitigations such as [DDoS Mitigation](https://vercel.com/docs/vercel-firewall/ddos-mitigation). For more complex filters, you can use REST API directly.

For example, to allow mobile applications to bypass the system-level mitigations, use the following code to create a [Custom Rule](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules) in your project. This condition will match mobile devices as well as other clients that emit mobile `user_agent` values.

<Note>
  Bypassing system-level mitigations with the API is currently in beta. Contact [support](https://vercel.com/help) if you would like to use it.
</Note>

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
});

async function run() {
  const result = await vercel.security.updateFirewallConfig({
    projectId: "<your_project_id>",
    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
    requestBody: {
      action: "rules.insert",
      id: null,
      value: {
        name: "Mobile App Bypass Security Rule",
        description: "Custom system bypass rule targeting mobile applications",
        active: true,
        conditionGroup: [
          {
            conditions: [
              {
                type: "user_agent",
                op: "re",
                neg: false,
                value: "Mobile|Android|iPhone|iPad"
              }
            ]
          }
        ],
        action: {
          mitigate: {
            action: "bypass",
            bypassSystem: true
          }
        }
      }
    },
  });

  // Handle the result
  console.log(result);
}

run();
```

## Update an OWASP rule

In this example, you update a specific rule from the [OWASP ruleset](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets#configure-owasp-core-ruleset) in your project using `crs.update`. You specify the rule to update by using its name in the `id` field.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function updateOwaspRule() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", // Not required in all cases
    requestBody: {
      action: "crs.update",
      id: "xss", // eg. "sd", "max", "lfi", "rfi", "rce", "php", "gen", "xss", "sqli", "sf", "java"
      value: {
        active: true, // Enable the rule
        action: "log", // e.g. "deny" | "log" 
      },
    },
  });
}

updateOwaspRule()
```

## Disable all OWASP rules

This example disables all [OWASP rules](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets#configure-owasp-core-ruleset) for the project. It is a shortcut equivalent to setting every OWASP rule to `active = false`.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function disableOWASPRules() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", // Not required in all cases
    requestBody: {
      action: "crs.disable",
      id: null,
      value: null,
    },
  });
}

disableOWASPRules()
```

## Update a managed ruleset

Use `managedRules.update`  with the ruleset name as `id` to enable/disable the ruleset and update the firewall action for that [managed ruleset](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets) for the project.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function updateManagedRuleset() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", // Not required in all cases
    requestBody: {
      action: "managedRules.update",
      id: "bot_protection", // eg. "owasp", "bot_protection", "ai_bots", "bot_filter"
      value: {
        active: true, // Enable the ruleset
        action: "log", // e.g. "deny" | "log" | "challenge"
      },
    },
  });
}

updateManagedRuleset()
```


--------------------------------------------------------------------------------
title: "Integrations"

last_updated: "2025-11-07T00:37:16.169Z"
source: "https://vercel.com/docs/rest-api/reference/examples/integrations"
--------------------------------------------------------------------------------

# Integrations

> Learn how to use the Vercel SDK through real-life examples.

## List integration information

In this example, you list the available integrations in your account.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function listAccountIntegrations() {
  try {
    // List available integrations in the account connected with the Vercel token
    const integrationsResponse = await vercel.integrations.getConfigurations({
      view: 'account',
    });

    integrationsResponse.forEach((config) => {
      console.log(
        `- ${config.slug}: ${
          config.installationType ? `${config.installationType}` : ``
        }integration installed in ${config.projects?.join(' ')}`,
      );
    });
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

listAccountIntegrations();
```


--------------------------------------------------------------------------------
title: "Logs and Monitoring"

last_updated: "2025-11-07T00:37:16.178Z"
source: "https://vercel.com/docs/rest-api/reference/examples/logs-monitoring"
--------------------------------------------------------------------------------

# Logs and Monitoring

> Learn how to use the Vercel SDK through real-life examples.

## Get deployment logs and check status

In this example, you retrieve the deployment logs and check the deployment status.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function getLogsAndStatus() {
  try {
    // Get deployment logs
    const logsResponse = await vercel.deployments.getDeploymentEvents({
      idOrUrl: 'project-name-uniqueid.vercel.app',
    });
    if (Array.isArray(logsResponse)) {
      if ('deploymentId' in logsResponse[0]) {
        const deploymentID = logsResponse[0].deploymentId;
        const deploymentStatus = await vercel.deployments.getDeployment({
          idOrUrl: deploymentID,
        });
        console.log(
          `Deployment with id, ${deploymentID} status is ${deploymentStatus.status}`,
        );
      }
      //Display logs with log type, timestamp and text
      for (const item of result) {
        if ('text' in item) {
          console.log(
            `${item.type} at ${new Date(item.created).toLocaleTimeString()}: ${
              item.text
            }`,
          );
        }
      }
    }
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

getLogsAndStatus();
```

## Aggregate logs and send alerts

Create a custom monitoring system that aggregates logs from multiple deployments, analyzes them for errors, and sends alerts if certain thresholds are exceeded.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';
import * as nodemailer from 'nodemailer';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});
const ALERT_EMAIL = 'alerts@example.com';

interface Log {
  type: string;
  created: number;
  text: string;
}

async function monitorDeployments() {
  try {
    // Get recent deployments
    const deploymentsResponse = await vercel.deployments.getDeployments({
      limit: 5,
      projectId: 'my-project', //The project name used in the deployment URL
    });

    let totalErrors = 0;
    let totalWarnings = 0;

    for (const deployment of deploymentsResponse.deployments) {
      console.log(`Analyzing deployment: ${deployment.uid}`);
      const logsResponse = await vercel.deployments.getDeploymentEvents({
        idOrUrl: deployment.uid,
      });

      if (Array.isArray(logsResponse)) {
        const logs = logsResponse as Log[];
        const errors = logs.filter((log) => log.type === 'error');
        const warnings = logs.filter((log) => log.type === 'warning');
        totalErrors += errors.length;
        totalWarnings += warnings.length;
        console.log(`Errors: ${errors.length}, Warnings: ${warnings.length}`);
        errors.forEach((error) => console.log(`Error: ${error.text}`));
      }
    }

    console.log(
      `Total Errors: ${totalErrors}, Total Warnings: ${totalWarnings}`,
    );

    // Send alert if thresholds are exceeded
    if (totalErrors > 10 || totalWarnings > 20) {
      const transporter = nodemailer.createTransport({
        host: 'smtp.example.com',
        port: 587,
        secure: false,
        auth: {
          user: 'your_email@example.com',
          pass: process.env.email_pwd,
        },
      });

      await transporter.sendMail({
        from: '"Vercel Monitor" <monitor@example.com>',
        to: ALERT_EMAIL,
        subject: 'Deployment Alert: High number of errors or warnings',
        text: `Alert: ${totalErrors} errors and ${totalWarnings} warnings detected in recent deployments.`,
      });

      console.log('Alert email sent');
    }
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

monitorDeployments();
```


--------------------------------------------------------------------------------
title: "Project Management"

last_updated: "2025-11-07T00:37:16.194Z"
source: "https://vercel.com/docs/rest-api/reference/examples/project-management"
--------------------------------------------------------------------------------

# Project Management

> Learn how to use the Vercel SDK through real-life examples.

## Create a new project

In this example, you will create a new project and retrieve its details. You will use the following method:

* Create project

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function createAndGetProject() {
  try {
    const createResponse = await vercel.projects.createProject({
      requestBody: {
        name: 'my-new-project',
        framework: 'nextjs',
      },
    });

    console.log(`Project created: ${createResponse.id}`);
    console.log('Project Details:', JSON.stringify(createResponse, null, 2));
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

createAndGetProject();
```

## Create a new project with additional setup

In this example, you will create a new project, add environment variables, and set up automatic GitHub deployments.

* Create project
* Create env

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function setupProjectWithGitHub() {
  try {
    // Create a new project with GH integration
    const createResponse = await vercel.projects.createProject({
      requestBody: {
        name: 'advanced-project',
        framework: 'nextjs',
        gitRepository: {
          repo: 'your-username-or-orgname/your-repo-name', //The repository should have been created before and the GH account is connected to your Vercel account
          type: 'github',
        },
      },
    });

    console.log(`Project created: ${createResponse.id}`);

    const envResponse = await vercel.projects.createProjectEnv({
      idOrName: createResponse.id,
      upsert: 'true',
      requestBody: [
        {
          key: 'DATABASE_URL',
          value: 'postgresql://user:pass@host:5432/db',
          type: 'encrypted', // Encrypted when saved and viewable in the Vercel dashboard with correct permissions
          target: ['production', 'preview'],
        },
        {
          key: 'API_KEY',
          value: 'your-api-key',
          type: 'encrypted', // Encrypted when saved and viewable in the Vercel dashboard with correct permissions
          target: ['production'],
        },
        {
          key: 'API_URL',
          value: 'your-api-url',
          type: 'plain',
          target: ['production', 'preview'],
        },
      ],
    });

    console.log('Environment variables added:', envResponse.created);
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

setupProjectWithGitHub();
```


--------------------------------------------------------------------------------
title: "Rolling Releases Management"

last_updated: "2025-11-07T00:37:16.162Z"
source: "https://vercel.com/docs/rest-api/reference/examples/rolling-releases"
--------------------------------------------------------------------------------

# Rolling Releases Management

> Learn how to use the Vercel SDK to manage Rolling Releases through real-life examples.

## Updating your project's rolling release configuration

In this example, you configure rolling releases for your project with multiple stages. This allows you to gradually roll out deployments to production, starting with a small percentage of traffic and progressively increasing it.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function setRollingReleaseConfig() {
  const result = await vercel.rollingRelease.updateRollingReleaseConfig({
    idOrName: "your-project-id", // Can be project ID or URL-encoded project name
    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional - required if your token is scoped to multiple teams
    slug: "my-team-url-slug", // Optional - alternative to teamId
    requestBody: {
      target: "production",
      stages: [
        {
          targetPercentage: 5,     // Start with 5% of traffic
          duration: 300           // Wait 5 minutes before next stage
        },
        {
          targetPercentage: 25,    // Then 25% of traffic
          duration: 600           // Wait 10 minutes
        },
        {
          targetPercentage: 50,    // Then 50% of traffic
          duration: 900           // Wait 15 minutes if approved
        },
        {
          targetPercentage: 100,   // Finally, 100% of traffic
        }
      ]
    }
  });

  console.log("Rolling Release Configuration Updated:", result.rollingRelease);
}

setRollingReleaseConfig();
```

## Approve the next stage of a rolling release

In this example, you manually approve advancing a rolling release to the next stage. This is useful when you have stages configured with `requireApproval: true` and want to control the rollout progression.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function approveNextStage() {
  const projectId = "your-project-id";

  try {
    // First, get the current rolling release status to understand the current state
    const currentStatus = await vercel.rollingRelease.getActiveRollingRelease({
      idOrName: projectId,
      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional
    });

    if (!currentStatus.rollingRelease || currentStatus.rollingRelease.state !== "ACTIVE") {
      console.log("No active rolling release found for this project");
      return;
    }

    const { rollingRelease } = currentStatus;

    console.log(`Current stage: ${rollingRelease.activeStage?.index} (${rollingRelease.activeStage?.targetPercentage}% traffic)`);
    console.log(`Next stage: ${rollingRelease.nextStage?.index} (${rollingRelease.nextStage?.targetPercentage}% traffic)`);

    if (!rollingRelease.nextStage) {
      console.log("Rolling release is already at the final stage");
      return;
    }

    if (!rollingRelease.nextStage.requireApproval) {
      console.log("Next stage does not require manual approval");
      return;
    }

    // Approve advancing to the next stage
    const approvalResult = await vercel.rollingRelease.approveRollingReleaseStage({
      idOrName: projectId,
      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional
      requestBody: {
        nextStageIndex: rollingRelease.nextStage.index,
        canaryDeploymentId: rollingRelease.canaryDeployment?.id || "",
      },
    });

    console.log("✓ Rolling release stage approved successfully!");
    console.log(`Advanced to stage ${approvalResult.rollingRelease?.activeStage?.index} (${approvalResult.rollingRelease?.activeStage?.targetPercentage}% traffic)`);

    // Display updated rollout information
    if (approvalResult.rollingRelease?.nextStage) {
      console.log(`Next stage will be: ${approvalResult.rollingRelease.nextStage.index} (${approvalResult.rollingRelease.nextStage.targetPercentage}% traffic)`);
    } else {
      console.log("This was the final stage - rolling release will complete automatically");
    }

  } catch (error) {
    console.error("Failed to approve rolling release stage:", error);
  }
}

approveNextStage();
```

## Force completion of a rolling release

In this example, you force-complete an active rolling release, immediately promoting the canary deployment to serve 100% of traffic. This is useful for emergency situations or when you want to skip remaining stages.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function forceCompleteRollingRelease() {
  const projectId = "your-project-id";

  try {
    // First, get the current rolling release status
    const currentStatus = await vercel.rollingRelease.getActiveRollingRelease({
      idOrName: projectId,
      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional
    });

    if (!currentStatus.rollingRelease || currentStatus.rollingRelease.state !== "ACTIVE") {
      console.log("No active rolling release found for this project");
      return;
    }

    const { rollingRelease } = currentStatus;

    console.log(`Current rolling release state: ${rollingRelease.state}`);
    console.log(`Current stage: ${rollingRelease.activeStage?.index} (${rollingRelease.activeStage?.targetPercentage}% traffic)`);
    console.log(`Canary deployment: ${rollingRelease.canaryDeployment?.name} (${rollingRelease.canaryDeployment?.id})`);

    if (!rollingRelease.canaryDeployment?.id) {
      console.error("No canary deployment found to complete");
      return;
    }

    // Confirm the action (in a real scenario, you might want additional checks)
    console.log("⚠️  WARNING: This will immediately promote the canary deployment to 100% traffic");
    console.log(`   Skipping ${rollingRelease.stages?.length - (rollingRelease.activeStage?.index || 0) - 1} remaining stages`);

    // Force complete the rolling release
    const completionResult = await vercel.rollingRelease.completeRollingRelease({
      idOrName: projectId,
      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional
      requestBody: {
        canaryDeploymentId: rollingRelease.canaryDeployment.id,
      },
    });

    console.log("✓ Rolling release completed successfully!");
    console.log(`Final state: ${completionResult.rollingRelease?.state}`);

    // The canary deployment is now the current deployment serving 100% traffic
    if (completionResult.rollingRelease?.currentDeployment) {
      console.log(`New production deployment: ${completionResult.rollingRelease.currentDeployment.name}`);
      console.log(`Production URL: ${completionResult.rollingRelease.currentDeployment.url}`);
    }

    // Log completion time
    if (completionResult.rollingRelease?.updatedAt) {
      const completedAt = new Date(completionResult.rollingRelease.updatedAt);
      console.log(`Completed at: ${completedAt.toISOString()}`);
    }

  } catch (error) {
    console.error("Failed to complete rolling release:", error);

    // Handle specific error cases
    if (error.response?.status === 404) {
      console.error("Project not found or no rolling release configuration exists");
    } else if (error.response?.status === 400) {
      console.error("Invalid request - check the canary deployment ID");
    } else if (error.response?.status === 403) {
      console.error("Insufficient permissions to complete rolling release");
    }
  }
}

forceCompleteRollingRelease();
```


--------------------------------------------------------------------------------
title: "Team and User Management"

last_updated: "2025-11-07T00:37:16.657Z"
source: "https://vercel.com/docs/rest-api/reference/examples/team-management"
--------------------------------------------------------------------------------

# Team and User Management

> Learn how to use the Vercel SDK through real-life examples.

## Invite a user to a team

In this example, you will find your team id and invite a new member to that team with a specific role.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function inviteTeamMember() {
  try {
    // Invite a new team member
    const availableTeams = (await vercel.teams.getTeams({})).teams;
    const myTeam = availableTeams.filter(
      (team) => team.slug === 'my-team-slug',
    );
    if (myTeam.length > 0) {
      const teamid = myTeam[0].id;
      const inviteResponse = await vercel.teams.inviteUserToTeam({
        teamId: teamid,
        requestBody: {
          email: 'john@example.com',
          role: 'MEMBER',
        },
      });
      console.log(
        `User with role ${inviteResponse.role} invited: ${inviteResponse.username}`,
      );
    }
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

inviteTeamMember();
```


--------------------------------------------------------------------------------
title: "Using the Vercel SDK"

last_updated: "2025-11-07T00:37:16.655Z"
source: "https://vercel.com/docs/rest-api/reference/sdk"
--------------------------------------------------------------------------------

# Using the Vercel SDK

> Interact programmatically with your Vercel account using the SDK.

The `@vercel/sdk` is a type-safe Typescript SDK that allows you to access the resources and methods of the Vercel REST API.

<Note>To view the methods for all endpoints, and explore code examples, see the [reference endpoints documentation](/endpoints).</Note>

## Installing Vercel SDK

To download and install Vercel SDK, run the following command:

<CodeGroup>
  ```bash pnpm theme={"system"}
  pnpm i @vercel/sdk
  ```

  ```bash npm theme={"system"}
  npm i @vercel/sdk
  ```

  ```bash yarn theme={"system"}
  yarn add @vercel/sdk
  ```
</CodeGroup>

### Authentication

Vercel Access Tokens are required to authenticate and use the Vercel SDK.

Once you have [created a token](/welcome#creating-an-access-token), you can use it to initialize the SDK as follows:

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: '<YOUR_BEARER_TOKEN_HERE>',
});
```

### Troubleshooting

Make sure that you create a token with the correct Vercel [scope](https://vercel.com/docs/dashboard-features#scope-selector).
If you face permission (403) errors when you are already sending a token, it can be one of the following problems:

* The token you are using has expired. Check the expiry date of the token in the Vercel dashboard.
* The token does not have access to the correct scope, either not the right team or it does not have account level access.
* The resource or operation you are trying to use is not available for that team. For example, AccessGroups is an Enterprise only feature and you are using a token for a team on the pro plan.

### Examples

Learn how to use Vercel SDK through the following categories of examples:

* [Deployments Automation](/examples/deployments-automation)
* [Project Management](/examples/project-management)
* [Domain Management](/examples/domain-management)
* [Team Management](/examples/team-management)
* [Environment Variables](/examples/environment-variables)
* [Logs and Monitoring](/examples/logs-monitoring)
* [Integrations](/examples/integrations)


--------------------------------------------------------------------------------
title: "Using the REST API"

last_updated: "2025-11-07T00:37:16.696Z"
source: "https://vercel.com/docs/rest-api/reference/welcome"
--------------------------------------------------------------------------------

# Using the REST API

> Interact programmatically with your Vercel account using the SDK or direct HTTP requests.

<Note>To view all endpoints, and explore code examples with the SDK and direct API calls, see the [reference endpoints documentation](/endpoints).</Note>

You can deploy new versions of web applications, manage custom domains, retrieve information about deployments, and manage secrets and environment variables for projects.

The API supports any programming language or framework that can send HTTP requests.

To interact with the API, you can:

* [Use the Vercel SDK](/sdk) by first instantiating with your token
* Use the language of your choice by calling the endpoints directly and [providing your token](#authentication)

## API Basics

Our API is exposed as an HTTP/1 and HTTP/2 service over SSL. All endpoints live under the URL `https://api.vercel.com` and then generally follow the REST architecture.

### Server Specs

#### HTTP and TLS

The API supports HTTP versions 1, 1.1, and 2, although HTTP/2 is preferred.

TLS versions 1.2 and 1.3 are supported, with resumption.

For more information on TLS support, refer to the SSL Labs report.

### Content Type

All requests must be encoded as JSON with the Content-Type: application/json header. If not otherwise specified, responses from the Vercel API, including errors, are encoded exclusively as JSON as well.

### Authentication

Vercel Access Tokens are required to authenticate and use the Vercel API.

```js  theme={"system"}
  Authorization: Bearer <TOKEN>
```

#### Creating an Access Token

Access Tokens can be created and managed from inside your [account settings](https://vercel.com/account/tokens).

<img className="block dark:hidden" src="https://assets.vercel.com/image/upload/v1701697368/docs-assets/static/docs/rest-api/create-token-light.png" />

<img className="hidden  dark:block" src="https://assets.vercel.com/image/upload/v1701697369/docs-assets/static/docs/rest-api/create-token-dark.png" />

1. In the upper-right corner of your [dashboard](https://vercel.com/dashboard), click your profile picture, then select **Settings**
2. Select **Tokens** from the sidebar
3. Enter a descriptive name for the token
4. Choose the scope from the list of Teams in the drop-down menu. The scope ensures that only your specified Team(s) can use an Access Token
5. From the drop-down, select an expiration date for the Token
6. Click **Create Token**
7. Once you've created an Access Token, securely store the value as it will not be shown again.

#### Expiration

Setting an expiration date on an Access Token is highly recommended and is considered one of the standard security practices that helps keep your information secure. You can select from a default list of expiration dates ranging from 1 day to 1 year. You can view the expiration date of your Access Tokens on the [tokens page.](https://vercel.com/account/tokens)

#### Accessing Resources Owned by a Team

By default, you can access resources contained within your own user account (personal).

To access resources owned by a team, or create a project for a *specific* team, you must first find the [Team ID](https://vercel.com/docs/teams-and-accounts/create-or-join-a-team#find-your-team-id).

After you obtained the Team ID, append it as a query string at the end of the API endpoint URL:

```js  theme={"system"}
https://api.vercel.com/v6/deployments?teamId=[teamID]
```

#### Failed Authentication

If authentication is unsuccessful for a request, the [error status code](#errors) **403** is returned.

## Types

The following is a list of the types of data used within the Vercel API:

| Name        | Definition                                                             | Example                      |
| ----------- | ---------------------------------------------------------------------- | ---------------------------- |
| **ID**      | A unique value used to identify resources.                             | `"V0fra8eEgQwEpFhYG2vTzC3K"` |
| **String**  | A string is a sequence of characters used to represent text.           | `"value"`                    |
| **Integer** | An integer is a number without decimals.                               | `1234`                       |
| **Float**   | A float is a number with decimals.                                     | `12.34`                      |
| **Map**     | A data structure with a list of values assigned to a unique key.       | `{ "key": "value" }`         |
| **List**    | A data structure with only a list of values separated by a comma.      | `["value", 1234, 12.34]`     |
| **Enum**    | An Enum is a String with only a few possible valid values.             | `A` or `B`                   |
| **Date**    | An Integer representing a date in milliseconds since the UNIX epoch.   | `1540095775941`              |
| **IsoDate** | A String representing a date in the 8601 format.                       | `YYYY-MM-DDTHH:mm:ssZ`       |
| **Boolean** | A Boolean is a type of two possible values representing true or false. | `true`                       |

## Pagination

When the API response includes an array of records, a pagination object is returned when the total number of records present is greater than the limit per request. The default value of this limit is 20 but it can be changed by passing a value to the query parameter `limit` when the request is made. The maximum possible value of `limit` is 100.

You can then use the pagination object to make additional requests and obtain all the records.

The pagination object is structured as shown in the example below:

```json pagination-structure theme={"system"}
{
  "pagination": {
    "count": 20, //Amount of items in the current page.
    "next": 1555072968396, //Timestamp that must be used to request the next page.
    "prev": 1555413045188 //Timestamp that must be used to request the previous page.
  }
}
```

In order to obtain the records for the next batch, perform the following actions:

1. Send a request to the same API endpoint
2. Include the query parameter `until` with a value equal to the timestamp value of `next` returned in the previous request
3. Repeat this sequence until the pagination object has a `next` value of `null`

This is an example of applying this sequence with `Node.js` to save all the projects in your personal account to a `json` file:

```js pagination-example.js theme={"system"}
const axios = require('axios');
const fs = require('fs');
const vercelToken = 'yourtokenvalue'; //Replace with your token
const apiEndPt = 'https://api.vercel.com/v9/projects';

let config = {
  method: 'get',
  url: apiEndPt,
  headers: {
    Authorization: 'Bearer ' + vercelToken,
  },
};
let results = [];

(function loop() {
  axios(config)
    .then(function (response) {
      results.push(...response.data.projects);
      if (response.data.pagination.next !== null) {
        config.url = `${apiEndPt}?until=${response.data.pagination.next}`;
        loop();
      } else {
        //you can use the final results object and for example save it to a json file
        fs.writeFileSync('projects.json', JSON.stringify(results));
      }
    })
    .catch(function (error) {
      console.log(error);
    });
})();
```

## Rate Limits

We limit the number of calls you can make over a certain period of time.
Rate limits vary and are specified by the following header in all responses:

| Header                  | Description                                                                  |
| ----------------------- | ---------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | The maximum number of requests that the consumer is permitted to make.       |
| `X-RateLimit-Remaining` | The number of requests remaining in the current rate limit window.           |
| `X-RateLimit-Reset`     | The time at which the current rate limit window resets in UTC epoch seconds. |

When the rate limit is **exceeded**, an error is returned with the status "**429 Too Many Requests**":

```json error-response theme={"system"}
{
  "error": {
    "code": "too_many_requests",
    "message": "Rate limit exceeded"
  }
}
```

<Note>
  You can find the complete list of rate limits in the [limits
  documentation](https://vercel.com/docs/limits#rate-limits).
</Note>

## Versioning

All endpoints and examples are designated with a specific version. Versions vary per endpoint and are not global.

The response shape of a certain endpoint is not guaranteed to be fixed over time. In particular, we might add new keys to responses without bumping a version endpoint, which will be noted in the changelog.

To ensure the security and correctness of your application, make sure to only read the keys from the response that your application needs. Don't proxy entire responses to third-parties without validation.

Old versions of each endpoint are supported for as long as possible. When we intend to deprecate, we will notify users in the changelog section.

Endpoint versions follow the base URL and come before the endpoint. For example:

```js version-endpoint theme={"system"}
https://api.vercel.com/v6/deployments`
```

This examples uses version `6` of the [deployments
endpoint](/endpoints/deployments/get-deployment-events).


--------------------------------------------------------------------------------
title: "Rewrites on Vercel"
description: "Learn how to use rewrites to send users to different URLs without modifying the visible URL."
last_updated: "null"
source: "https://vercel.com/docs/rewrites"
--------------------------------------------------------------------------------

# Rewrites on Vercel

Copy page

Ask AI about this page

Last updated October 31, 2025

A rewrite routes a request to a different destination without changing the URL in the browser. Unlike redirects, the user won't see the URL change.

There are two main types:

1.  Same-application rewrites – Route requests to different pages within your Vercel project.
2.  External rewrites – Forward requests to an external API or website.

The /.well-known path is reserved and cannot be redirected or rewritten. Only Enterprise teams can configure custom SSL. [Contact sales](/contact/sales) to learn more.

## [Setting up rewrites](#setting-up-rewrites)

Rewrites are defined in a `vercel.json` file in your project's root directory:

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/source-path",
      "destination": "/destination-path"
    }
  ]
}
```

For all configuration options, see the [project configuration](/docs/project-configuration#rewrites) docs.

## [Same-application rewrites](#same-application-rewrites)

Same-application rewrites route requests to different destinations within your project. Common uses include:

*   Friendly URLs: Transform `/products/t-shirts` into `/catalog?category=t-shirts`
*   Device-specific content: Show different layouts based on device type
*   A/B testing: Route users to different versions of a page
*   Country-specific content: Show region-specific content based on the user's location

Example: Route image resize requests to a serverless function:

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/resize/:width/:height",
      "destination": "/api/sharp"
    }
  ]
}
```

This converts a request like `/resize/800/600` to `/api/sharp?width=800&height=600`.

Example: Route UK visitors to a UK-specific section:

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/:path((?!uk/).*)",
      "has": [
        { "type": "header", "key": "x-vercel-ip-country", "value": "GB" }
      ],
      "destination": "/uk/:path*"
    }
  ]
}
```

This routes a UK visitor requesting `/about` to `/uk/about`.

## [External rewrites](#external-rewrites)

External rewrites forward requests to APIs or websites outside your Vercel project, effectively allowing Vercel to function as a reverse proxy or standalone CDN. You can use this feature to:

*   Proxy API requests: Hide your actual API endpoint
*   Combine multiple services: Merge multiple backends under one domain
*   Create microfrontends: Combine multiple Vercel applications into a single website
*   Add caching: Cache external API responses at the edge
*   Serve externally hosted content: Serve content that is not hosted on Vercel.

Example: Forward API requests to an external endpoint:

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/api/:path*",
      "destination": "https://api.example.com/:path*"
    }
  ]
}
```

A request to `/api/users` will be forwarded to `https://api.example.com/users` without changing the URL in the browser.

### [Caching external rewrites](#caching-external-rewrites)

The CDN can cache external rewrites for better performance. There are three approaches to enable caching:

1.  Directly from your API (preferred): When you control the backend API, the API itself can return [`CDN-Cache-Control`](/docs/headers/cache-control-headers#cdn-cache-control-header) or [`Vercel-CDN-Cache-Control`](/docs/headers/cache-control-headers#cdn-cache-control-header) headers in its response:
    
    `CDN-Cache-Control: max-age=60`
    
    This will cache API responses at the edge for 60 seconds.
    
2.  Using Vercel Configuration: When you can't modify the backend API, set the caching headers in your Vercel configuration:
    
    vercel.json
    
    ```
    {
      "$schema": "https://openapi.vercel.sh/vercel.json",
      "rewrites": [
        {
          "source": "/api/:path*",
          "destination": "https://api.example.com/:path*"
        }
      ],
      "headers": [
        {
          "source": "/api/:path*",
          "headers": [
            {
              "key": "CDN-Cache-Control",
              "value": "max-age=60"
            }
          ]
        }
      ]
    }
    ```
    
    This will cache API responses at the edge for 60 seconds.
    
3.  Using `x-vercel-enable-rewrite-caching` (fallback): Use this approach only when you cannot control the caching headers from the external API and need to respect the `Cache-Control` header:
    
    vercel.json
    
    ```
    {
      "$schema": "https://openapi.vercel.sh/vercel.json",
      "headers": [
        {
          "source": "/api/:path*",
          "headers": [{ "key": "x-vercel-enable-rewrite-caching", "value": "1" }]
        }
      ]
    }
    ```
    
    This instructs Vercel to respect the `Cache-Control` header from the external API.
    

For more information on caching headers and detailed options, see the [Cache-Control headers documentation](/docs/headers/cache-control-headers).

### [Draining external rewrites](#draining-external-rewrites)

You can export external rewrite data by draining logs from your application. External rewrite events appear in your runtime logs, allowing you to monitor proxy requests, track external API calls, and analyze traffic patterns to your backend services.

To get started, configure a [logs drain](/docs/drains/using-drains).

### [Observing external rewrites](#observing-external-rewrites)

You can observe your external rewrite performance using Observability. The External Rewrites tab shows request counts, connection latency, and traffic patterns for your proxied requests, helping you monitor backend performance and validate that rewrites are working as expected.

Learn more in the [Observability Insights](/docs/observability/insights#external-rewrites) documentation.

## [Framework considerations](#framework-considerations)

External rewrites work universally with all frameworks, making them ideal for API proxying, microfrontend architectures, and serving content from external origins through Vercel's global edge network as a reverse proxy or standalone CDN.

For same-application rewrites, always prefer your framework's native routing capabilities:

*   Next.js: [Next.js rewrites](https://nextjs.org/docs/api-reference/next.config.js/rewrites)
*   Astro: [Astro routing](/docs/frameworks/astro#rewrites)
*   SvelteKit: [SvelteKit routing](/docs/frameworks/sveltekit#rewrites)

Use `vercel.json` rewrites for same-application routing only when your framework doesn't provide native routing features. Always consult your framework's documentation for the recommended approach.

## [Testing rewrites](#testing-rewrites)

Use Vercel's preview deployments to test your rewrites before going to production. Each pull request creates a unique preview URL where you can verify your rewrites work correctly.

## [Wildcard path forwarding](#wildcard-path-forwarding)

You can capture and forward parts of a path using wildcards:

```
{
  "rewrites": [
    {
      "source": "/docs/:path*",
      "destination": "/help/:path*"
    }
  ]
}
```

Some redirects and rewrites configurations can accidentally become gateways for semantic attacks. Learn how to check and protect your configurations with the [Enhancing Security for Redirects and Rewrites guide](/guides/enhancing-security-for-redirects-and-rewrites).

A request to `/docs/getting-started/install` will be forwarded to `/help/getting-started/install`.

You can also capture multiple path segments:

```
{
  "rewrites": [
    {
      "source": "/blog/:year/:month/:slug*",
      "destination": "/posts?date=:year-:month&slug=:slug*"
    }
  ]
}
```

## [Using regular expressions](#using-regular-expressions)

For more complex patterns, you can use regular expressions with capture groups:

```
{
  "rewrites": [
    {
      "source": "^/articles/(\\d{4})/(\\d{2})/(.+)$",
      "destination": "/archive?year=$1&month=$2&slug=$3"
    }
  ]
}
```

This converts `/articles/2023/05/hello-world` to `/archive?year=2023&month=05&slug=hello-world`.

You can also use named capture groups:

```
{
  "rewrites": [
    {
      "source": "^/products/(?<category>[a-z]+)/(?<id>\\d+)$",
      "destination": "/shop?category=$category&item=$id"
    }
  ]
}
```

This converts `/products/shirts/123` to `/shop?category=shirts&item=123`.

## [When to use each type](#when-to-use-each-type)

*   Same-application rewrites: Use when routing within your own application
*   External rewrites: Use when connecting to external APIs, creating microfrontends, or using Vercel as a reverse proxy or standalone CDN for third-party content

--------------------------------------------------------------------------------
title: "Rolling Releases"
description: "Learn how to use Rolling Releases for more cautious deployments."
last_updated: "null"
source: "https://vercel.com/docs/rolling-releases"
--------------------------------------------------------------------------------

# Rolling Releases

Copy page

Ask AI about this page

Last updated September 24, 2025

Rolling Releases are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Rolling Releases allow you to roll out new deployments to a small fraction of your users before promoting them to everyone.

Once Rolling Releases is enabled, new deployments won't be immediately served to 100% of traffic. Instead, Vercel will direct a configurable fraction of your visitors, for example, 5%, to the new deployment. The rest of your traffic will be routed to your previous production deployment.

You can leave your rollout in this state for as long as you want, and Vercel will show you a breakdown of key metrics, such as [Speed Insights](/docs/speed-insights), between the canary and current deployment. You can also compare these deployments with other metrics you gather with your own observability dashboards. When you're ready, or when a configurable period of time has passed, you can promote the prospective deployment to 100% of traffic. At any point, you can use [Instant Rollback](/docs/instant-rollback) to revert from the current release candidate.

## [Configuring Rolling Releases](#configuring-rolling-releases)

1.  From your [dashboard](/dashboard), navigate to your Project Settings.
2.  Select Build & Deployment in the left sidebar.
3.  Scroll to the Rolling Releases section.

We highly recommend enabling [Skew Protection](/docs/skew-protection) with Rolling Releases. This ensures that every user, whether they get the prior deployment or the release candidate, communicates with the backend code from the matching deployment. Without Skew Protection, users may experience inconsistencies between client and server versions during rollouts.

Once you've enabled Rolling Releases, you need to configure two or more stages for your release. Stages are the distinct traffic ratios you want to serve as your release candidate rolls out. Each stage must send a larger fraction of traffic to the release candidate. The last stage must always be 100%, representing the full promotion of the release candidate. Many projects only need two stages, with a single fractional stage before final promotion, but you can configure more stages as needed.

A stage configured for 0% of traffic is a special case. Vercel will not automatically direct any visitors to the release candidate in this case, but it can be accessed by forcing a value for the rolling release cookie. See [setting the rolling release cookie](#setting-the-rolling-release-cookie) for more information.

Once Rolling Releases are configured for the project, any subsequent rollout will use the project's current rolling release configuration. Each new rollout clones the rolling release configuration. Therefore, editing the configuration will not impact any rollouts that are currently in progress.

## [Managing Rolling Releases](#managing-rolling-releases)

You can manage Rolling releases on the [project's settings page](/docs/project-configuration/project-settings) or via the API or CLI.

### [Starting a rolling release](#starting-a-rolling-release)

When you enable Rolling Releases in your [project's settings](/docs/project-configuration/project-settings), any action that promotes a deployment to production will initiate a new rolling release. This includes:

*   Pushing a commit to your git branch, if your project automatically promotes new commits.
*   Selecting the Promote menu option on a deployment on the Deployments page.
*   Promoting a deployment [via the CLI](/docs/cli/promote).

The rolling release will proceed to its first stage, sending a portion of traffic to the release candidate.

If a rolling release is in progress when one of the promote actions triggers, the project's state won't change. The active rolling release must be resolved (either completed or aborted) before starting a new one.

### [Observability](#observability)

While a rolling release is in progress, it will be prominently indicated in several locations:

*   The Deployments page has a section summarizing the current rolling release status.
*   The release candidate is badged "Canary" in the Deployments list, and indicates the fraction of traffic it is receiving.

Furthermore, the Observability tab for your project has a Rolling Releases section. This lets you examine Vercel-gathered metrics about the actual traffic mix between your deployments and comparative performance differences between them. You can use these metrics to help you decide whether you want to advance or abort a rolling release.

#### [Metrics stored outside of Vercel](#metrics-stored-outside-of-vercel)

You may have observability metrics gathered by platforms other than Vercel. To leverage these metrics to help make decisions about rolling releases, you will need to ensure that these metrics can distinguish between behaviors observed on the base deployment and ones on the canary. The easiest way to do this is to propagate Vercel's deployment ID to your other observability systems.

### [Advancing a rolling release](#advancing-a-rolling-release)

Both the Deployments page and the Rolling Releases Observability tab have controls to change the state of the current release with a button to advance the release to its next stage. If the next stage is the final stage, the release candidate will be fully promoted to be your current production deployment, and the project exits the rolling release state.

### [Aborting a rolling release](#aborting-a-rolling-release)

If the metrics on the release candidate are unacceptable to you, there are several ways to abort the rolling release:

*   Use the Abort button on the Rolling Releases page.
*   Use [Instant Rollback](/docs/instant-rollback) to roll back to any prior deployment, including the base deployment for the current rolling release.

This will leave your project in a rolled-back state, as with Instant Rollback. When you're ready, you can select any deployment to promote to initiate a new rolling release. The project will exit rollback status once that rolling release completes.

## [Understanding Rolling Releases](#understanding-rolling-releases)

Rolling Releases should work out-of-the-box for most projects, but the implementation details may be significant for some users.

When a user requests a page from a project's production deployment with an active rolling release, Vercel assigns this user to a random bucket that is stored in a cookie on the client. We use client-identifying information such as the client's IP address to perform this bucket assignment. This allows the same device to see the same deployment even when in incognito mode. It also ensures that in race conditions such as multiple simultaneous requests from the same client, all requests resolve to the same target deployment.

Buckets are divided among the two releases at the fraction requested in the current rolling release stage. When the rolling release advances to a later stage, clients assigned to some buckets will now be assigned to a different deployment, and will receive the new deployment at that time.

Note that while we attempt to divide user sessions among the two deployments at the configured fraction, not all users behave the same. If a particularly high-traffic user is placed into one bucket, the observed fraction of total requests between the two deployments may not match the requested fraction. Likewise, note that randomized assignment based on hashing may not achieve precisely the desired diversion rate, especially when the number of sessions is small.

### [Why Rolling Releases needs Skew Protection](#why-rolling-releases-needs-skew-protection)

Rolling Releases impact which deployment a user gets when they make a page load. Skew Protection ensures that backend API requests made from a particular deployment are served by a backend implementation from the same deployment.

When a new user loads a page from a project with an active rolling release, they might receive a page from either deployment. Skew Protection ensures that, whichever deployment they are served, their backend calls are consistent with the page that they loaded.

If the rolling release stage is advanced, the user may be eligible for a new deployment. On their next page load or refresh, they will fetch that page from the new deployment. Until they refresh, Skew Protection will continue to ensure that they use backends consistent with the page they are currently on.

### [Setting the Rolling Release cookie](#setting-the-rolling-release-cookie)

You can modify the Rolling Release cookie on a client by issuing a request that includes a special query parameter. Requests that include `vcrrForceStable=true` in the URL will always get the base release for the current rolling release. Likewise, `vcrrForceCanary=true` will force the cookie to target the current canary, including for a rolling release stage configured for 0% of traffic.

This forced cookie is good only for the duration of a single rolling release. When that rolling release is completed or aborted and a new rolling release starts, the cookie will get re-processed to a random value.

Be aware that anybody is capable of setting `vcrrForceCanary=true` on a URL. 0% canaries are not served by default, but they are not securely hidden from users.

## [Manage rolling releases programmatically with the REST API](#manage-rolling-releases-programmatically-with-the-rest-api)

The Rolling Releases REST API allows you to programmatically manage rolling release configurations and monitor active releases. Common use cases include:

*   CI/CD integration: Automate rolling release workflows as part of your deployment pipeline
*   Monitoring and observability: Track the status and progress of active rolling releases
*   Update configuration: Enable/disable rolling releases, add/remove stages, and more
*   Custom tooling: Build internal dashboards or tools that interact with rolling release data

For detailed API specifications, request/response schemas, and code examples:

*   [API reference](https://vercel.com/docs/rest-api/reference/endpoints/rolling-release)
*   [Examples using the SDK](https://vercel.com/docs/rest-api/reference/examples/rolling-releases)

--------------------------------------------------------------------------------
title: "Routing Middleware"
description: "Learn how you can use Routing Middleware, code that executes before a request is processed on a site, to provide speed and personalization to your users."
last_updated: "null"
source: "https://vercel.com/docs/routing-middleware"
--------------------------------------------------------------------------------

# Routing Middleware

Copy page

Ask AI about this page

Last updated October 27, 2025

Routing Middleware is available on [all plans](/docs/plans)

Routing Middleware executes code _before_ a request is processed on a site, and are built on top of [fluid compute](/docs/fluid-compute). Based on the request, you can modify the response.

Because it runs globally before the cache, Routing Middleware is an effective way of providing personalization to statically generated content. Depending on the incoming request, you can execute custom logic, rewrite, redirect, add headers and more, before returning a response.

The default runtime for Routing Middlewares is [Edge](/docs/functions/runtimes/edge). See [runtime options](#runtime-options) for information on how to change the runtime of your Routing Middleware.

## [Creating a Routing Middleware](#creating-a-routing-middleware)

You can use Routing Middleware with [any framework](/docs/frameworks). To add a Routing Middleware to your app, you need to create a `middleware.ts` file at your project's root directory.

middleware.ts

TypeScript

TypeScriptJavaScript

```
export default function middleware(request: Request) {
  const url = new URL(request.url);
 
  // Redirect old paths
  if (url.pathname === '/old-page') {
    return new Response(null, {
      status: 302,
      headers: { Location: '/new-page' },
    });
  }
 
  // Continue to next handler
  return new Response('Hello from your Middleware!');
}
```

The `middleware.ts` file should be at the same level as your `app` or `pages` directory (even if you're using a `src` directory). See the [Quickstart](/docs/routing-middleware/getting-started) guide for more information.

## [Logging](#logging)

Routing Middleware has full support for the [`console`](https://developer.mozilla.org/docs/Web/API/Console) API, including `time`, `debug`, `timeEnd`. Logs will appear inside your Vercel project by clicking View Functions Logs next to the deployment.

## [Using a database with Routing Middleware](#using-a-database-with-routing-middleware)

If your Routing Middleware depends on a database far away from one of [our supported regions](/docs/regions), the overall latency of API requests could be slower than expected, due to network latency while connecting to the database from an edge region. To avoid this issue, use a global database. Vercel has multiple global storage products, including [Edge Config](/docs/edge-config) and [Vercel Blob](/docs/storage/vercel-blob). You can also explore the storage category of the [Vercel Marketplace](/marketplace?category=storage) to learn which option is best for you.

## [Limits on requests](#limits-on-requests)

The following limits apply to requests processed by Routing Middleware:

| Name | Limit |
| --- | --- |
| Maximum URL length | 14 KB |
| Maximum request body length | 4 MB |
| Maximum number of request headers | 64 |
| Maximum request headers length | 16 KB |

## [Runtime options](#runtime-options)

Routing Middleware is available on the [Node.js](/docs/functions/runtimes/node-js), [Bun](/docs/functions/runtimes/bun), and [Edge](/docs/functions/runtimes/edge) runtimes. The default runtime for Routing Middleware is Edge. You can change the runtime to Node.js by exporting a [`config`](/docs/routing-middleware/api#config-object) object with a `runtime` property in your `middleware.ts` file.

To use the Bun runtime, set [`bunVersion`](/docs/project-configuration#bunversion) in your `vercel.json` file and your runtime config to `nodejs`.

Next.js (/app)Next.js (/pages)Other frameworks

middleware.ts

TypeScript

TypeScriptJavaScript

```
export const config = {
  runtime: 'nodejs', // or 'edge' (default)
};
export default function middleware(request: Request) {
  // Your middleware logic here
  return new Response('Hello from your Middleware!');
}
```

## [Pricing](#pricing)

Routing Middleware is priced using the [fluid compute](/docs/fluid-compute) model, which means you are charged by the amount of compute resources used by your Routing Middleware. See the [fluid compute pricing documentation](/docs/functions/usage-and-pricing) for more information.

## [Observability](#observability)

The [Vercel Observability dashboard](/docs/observability) provides visibility into your routing middleware usage, including invocation counts and performance metrics. You can get more [insights](/docs/observability/insights) with [Observability Plus](/docs/observability/observability-plus):

*   Analyze invocations by request path
*   Break down actions by type, such as redirects or rewrites
*   View rewrite targets and frequency
*   Use the query builder for custom insights

## [More resources](#more-resources)

Learn more about Routing Middleware by exploring the following resources:

*   [Getting Started with Routing Middleware](/docs/routing-middleware/getting-started)
*   [Routing Middleware API Reference](/docs/routing-middleware/api)
*   [Fluid compute](/docs/fluid-compute)
*   [Runtimes](/docs/functions/runtimes)

--------------------------------------------------------------------------------
title: "Routing Middleware API"
description: "Learn how you can use Routing Middleware, code that executes before a request is processed on a site, to provide speed and personalization to your users."
last_updated: "null"
source: "https://vercel.com/docs/routing-middleware/api"
--------------------------------------------------------------------------------

# Routing Middleware API

Copy page

Ask AI about this page

Last updated October 27, 2025

## [Routing Middleware file location and name](#routing-middleware-file-location-and-name)

The Routing Middleware file should be named `middleware.ts` and placed at the root of your project, at the same level as your `package.json` file. This is where Vercel will look for the Routing Middleware when processing requests.

The Routing Middleware must be a default export, with the function being named anything you like. For example, you can name it `router`, `middleware`, or any other name that makes sense for your application.

middleware.ts

```
export default function middleware() {}
```

## [`config` object](#config-object)

Routing Middleware will be invoked for every route in your project. If you only want it to be run on specific paths, you can define those either with a [custom matcher config](#match-paths-based-on-custom-matcher-config) or with [conditional statements](/docs/routing-middleware/api#match-paths-based-on-conditional-statements).

You can also use the [`runtime` option](#config-properties) to [specify which runtime](#specify-runtime) you would like to use. The default is `edge`.

While the `config` option is the preferred method, as it does not get invoked on every request, you can also use conditional statements to only run the Routing Middleware when it matches specific paths.

### [Match paths based on custom matcher config](#match-paths-based-on-custom-matcher-config)

To decide which route the Routing Middleware should be run on, you can use a custom matcher config to filter on specific paths. The matcher property can be used to define either a single path, or using an array syntax for multiple paths.

#### [Match a single path](#match-a-single-path)

middleware.ts

```
export const config = {
  matcher: '/about/:path*',
};
```

#### [Match multiple paths](#match-multiple-paths)

middleware.ts

```
export const config = {
  matcher: ['/about/:path*', '/dashboard/:path*'],
};
```

#### [Match using regex](#match-using-regex)

The matcher config has full [regex](https://developer.mozilla.org/docs/Web/JavaScript/Guide/Regular_Expressions) support for cases such as negative lookaheads or character matching.

#### [Match based on a negative lookahead](#match-based-on-a-negative-lookahead)

To match all request paths except for the ones starting with:

*   `api` (API routes)
*   `_next/static` (static files)
*   `favicon.ico` (favicon file)

middleware.ts

```
export const config = {
  matcher: ['/((?!api|_next/static|favicon.ico).*)'],
};
```

#### [Match based on character matching](#match-based-on-character-matching)

To match `/blog/123` but not `/blog/abc`:

middleware.ts

```
export const config = {
  matcher: ['/blog/:slug(\\d{1,})'],
};
```

For help on writing your own regex path matcher, see [Path to regexp](https://github.com/pillarjs/path-to-regexp#path-to-regexp-1).

### [Match paths based on conditional statements](#match-paths-based-on-conditional-statements)

middleware.ts

```
import { rewrite } from '@vercel/functions';
 
export default function middleware(request: Request) {
  const url = new URL(request.url);
 
  if (url.pathname.startsWith('/about')) {
    return rewrite(new URL('/about-2', request.url));
  }
 
  if (url.pathname.startsWith('/dashboard')) {
    return rewrite(new URL('/dashboard/user', request.url));
  }
}
```

See the [helper methods](#routing-middleware-helper-methods) below for more information on using the `@vercel/functions` package.

### [Specify runtime](#specify-runtime)

To change the runtime from the `edge` default, update the `runtime` option as follows:

middleware.ts

```
export const config = {
  runtime: 'nodejs', // or 'edge' (default)
};
```

To use the Bun runtime with Routing Middleware, set the [`bunVersion`](/docs/project-configuration#bunversion) property in your `vercel.json` file as well as using the `runtime` config shown above to `nodejs`:

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "bunVersion": "1.x"
}
```

### [`config` properties](#config-properties)

| Property | Type | Description |
| --- | --- | --- |
| `matcher` | `string / string[]` | A string or array of strings that define the paths the Middleware should be run on |
| `runtime` | `string` (`edge` or `nodejs`) | A string that defines the Middleware runtime and defaults to `edge` |

## [Routing Middleware signature](#routing-middleware-signature)

The Routing Middleware signature is made up of two parameters: `request` and `context`. The `request` parameter is an instance of the [Request](/docs/functions/edge-functions/edge-functions-api#request) object, and the `context` parameter is an object containing the [`waitUntil`](/docs/functions/edge-functions/edge-functions-api#waituntil) method. Both parameters are optional.

| Parameter | Description | Next.js (/app) or (/pages) | Other Frameworks |
| --- | --- | --- | --- |
| `request` | An instance of the [Request](/docs/functions/edge-functions/edge-functions-api#request) object | [`Request`](https://developer.mozilla.org/docs/Web/API/Request) or [`NextRequest`](https://nextjs.org/docs/api-reference/next/server#nextrequest) | [`Request`](https://developer.mozilla.org/docs/Web/API/Request) |
| `context` | An extension to the standard [`Request`](https://developer.mozilla.org/docs/Web/API/Request) object | [`NextFetchEvent`](https://nextjs.org/docs/api-reference/next/server#nextfetchevent) | [`RequestContext`](/docs/functions/edge-functions/edge-functions-api#requestcontext) |

Routing Middleware comes with built in helpers that are based on the native [`FetchEvent`](https://developer.mozilla.org/docs/Web/API/FetchEvent), [`Response`](https://developer.mozilla.org/docs/Web/API/Response), and [`Request`](https://developer.mozilla.org/docs/Web/API/Request) objects.

[See the section on Routing Middleware helpers for more information](#routing-middleware-helper-methods).

Next.js (/app)Next.js (/pages)Other frameworks

middleware.ts

TypeScript

TypeScriptJavaScript

```
// config with custom matcher
export const config = {
  matcher: '/about/:path*',
};
 
export default function middleware(request: Request) {
  return Response.redirect(new URL('/about-2', request.url));
}
```

If you're not using a framework, you must either add `"type": "module"` to your `package.json` or change your JavaScript Functions' file extensions from `.js` to `.mjs`

### [Request](#request)

The `Request` object represents an HTTP request. It is a wrapper around the [Fetch API](https://developer.mozilla.org/docs/Web/API/Fetch_API) `Request` object. When using TypeScript, you do not need to import the `Request` object, as it is already available in the global scope.

#### [Request properties](#request-properties)

| Property | Type | Description |
| --- | --- | --- |
| `url` | `string` | The URL of the request |
| `method` | `string` | The HTTP method of the request |
| `headers` | `Headers` | The headers of the request |
| `body` | [`ReadableStream`](https://developer.mozilla.org/docs/Web/API/ReadableStream) | The body of the request |
| `bodyUsed` | `boolean` | Whether the body has been read |
| `cache` | `string` | The cache mode of the request |
| `credentials` | `string` | The credentials mode of the request |
| `destination` | `string` | The destination of the request |
| `integrity` | `string` | The integrity of the request |
| `redirect` | `string` | The redirect mode of the request |
| `referrer` | `string` | The referrer of the request |
| `referrerPolicy` | `string` | The referrer policy of the request |
| `mode` | `string` | The mode of the request |
| `signal` | [`AbortSignal`](https://developer.mozilla.org/docs/Web/API/AbortSignal) | The signal of the request |
| `arrayBuffer` | `function` | Returns a promise that resolves with an ArrayBuffer |
| `blob` | `function` | Returns a promise that resolves with a Blob |
| `formData` | `function` | Returns a promise that resolves with a FormData |
| `json` | `function` | Returns a promise that resolves with a JSON object |
| `text` | `function` | Returns a promise that resolves with a string |
| `clone` | `function` | Returns a clone of the request |

To learn more about the [`NextRequest`](https://nextjs.org/docs/api-reference/next/server#nextrequest) object and its properties, visit the [Next.js documentation](https://nextjs.org/docs/api-reference/next/server#nextrequest).

### [`waitUntil()`](#waituntil)

The `waitUntil()` method is from the [`ExtendableEvent`](https://developer.mozilla.org/docs/Web/API/ExtendableEvent/waitUntil) interface. It accepts a [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) as an argument, which will keep the function running until the `Promise` resolves.

It can be used to keep the function running after a response has been sent. This is useful when you have an async task that you want to keep running after returning a response.

The example below will:

*   Send a response immediately
*   Keep the function running for ten seconds
*   Fetch a product and log it to the console

Next.js (/app)Next.js (/pages)Other frameworks

middleware.ts

TypeScript

TypeScriptJavaScript

```
import type { NextFetchEvent } from 'next/server';
 
export const config = {
  matcher: '/',
};
 
const wait = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));
 
async function getProduct() {
  const res = await fetch('https://api.vercel.app/products/1');
  await wait(10000);
  return res.json();
}
 
export default function middleware(request: Request, context: NextFetchEvent) {
  context.waitUntil(getProduct().then((json) => console.log({ json })));
 
  return new Response(JSON.stringify({ hello: 'world' }), {
    status: 200,
    headers: { 'content-type': 'application/json' },
  });
}
```

If you're not using a framework, you must either add `"type": "module"` to your `package.json` or change your JavaScript Functions' file extensions from `.js` to `.mjs`

#### [Context properties](#context-properties)

| Property | Type | Description |
| --- | --- | --- |
| [`waitUntil`](https://developer.mozilla.org/docs/Web/API/ExtendableEvent/waitUntil) | `(promise: Promise<unknown>): void` | Prolongs the execution of the function until the promise passed to `waitUntil` is resolved |

## [Routing Middleware helper methods](#routing-middleware-helper-methods)

You can use Vercel-specific helper methods to access a request's [geolocation](#geolocation), [IP Address](/docs/functions/functions-api-reference/vercel-functions-package#ipaddress), and more when deploying Middleware on Vercel.

You can access these helper methods with the `request` and `response` objects in your middleware handler method.

These helpers are exclusive to Vercel, and will not work on other providers, even if your app is built with Next.js.

### [Geolocation](#geolocation)

The `geo` helper object returns geolocation information for the incoming request. It has the following properties:

| Property | Description |
| --- | --- |
| `city` | The city that the request originated from |
| `country` | The country that the request originated from |
| `latitude` | The latitude of the client |
| `longitude` | The longitude of the client |
| `region` | The [CDN region](/docs/regions) that received the request |

Each property returns a `string`, or `undefined`.

Next.js (/app)Next.js (/pages)Other frameworks

middleware.ts

TypeScript

TypeScriptJavaScript

```
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
 
// The country to block from accessing the secret page
const BLOCKED_COUNTRY = 'SE';
 
// Trigger this middleware to run on the `/secret-page` route
export const config = {
  matcher: '/secret-page',
};
 
export default function middleware(request: NextRequest) {
  const country = request.geo?.country ?? 'US';
 
  console.log(`Visitor from ${country}`);
 
  const url = request.nextUrl.clone();
  url.pathname = country === BLOCKED_COUNTRY ? '/login' : '/secret-page';
 
  return NextResponse.rewrite(url);
}
```

### [IP Address](#ip-address)

The `ip` object returns the IP address of the request from the headers, or `undefined`.

middleware.ts

TypeScript

TypeScriptJavaScript

```
import { ipAddress } from '@vercel/functions';
import { next } from '@vercel/functions';
 
export default function middleware(request: Request) {
  const ip = ipAddress(request);
  return next({
    headers: { 'x-your-ip-address': ip || 'unknown' },
  });
}
```

### [`RequestContext`](#requestcontext)

The `RequestContext` is an extension of the standard `Request` object, which contains the [`waitUntil`](#waitUntil) function. The following example works in middleware for all frameworks:

middleware.ts

TypeScript

TypeScriptJavaScript

```
import type { RequestContext } from '@vercel/functions';
 
export default function handler(request: Request, context: RequestContext) {
  context.waitUntil(getAlbum().then((json) => console.log({ json })));
 
  return new Response(
    `Hello there, from ${request.url} I'm an Vercel Function!`,
  );
}
 
export const config = {
  matcher: '/',
};
 
const wait = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));
 
async function getAlbum() {
  const res = await fetch('https://jsonplaceholder.typicode.com/albums/1');
  await wait(10000);
  return res.json();
}
```

### [Rewrites](#rewrites)

The `NextResponse.rewrite()` helper returns a response that rewrites the request to a different URL.

Next.js (/app)Next.js (/pages)Other frameworks

middleware.ts

TypeScript

TypeScriptJavaScript

```
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
// Trigger this middleware to run on the `/about` route
export const config = {
  matcher: '/about',
};
 
export default function middleware(request: NextRequest) {
  // Rewrite to URL
  return NextResponse.rewrite('/about-2');
}
```

### [Continuing the Routing Middleware chain](#continuing-the-routing-middleware-chain)

The `NextResponse.next()` helper returns a Response that instructs the function to continue the middleware chain. It takes the following optional parameters:

| Parameter | type | Description |
| --- | --- | --- |
| `headers` | `Headers[]` or `Headers` | The headers you want to set |
| `status` | `number` | The status code |
| `statusText` | `string` | The status text |

The following example adds a custom header, then continues the Routing Middleware chain:

Next.js (/app)Next.js (/pages)Other frameworks

middleware.ts

TypeScript

TypeScriptJavaScript

```
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
 
export function middleware(request: NextRequest) {
  // Clone the request headers and set a new header `x-hello-from-middleware1`
  const requestHeaders = new Headers(request.headers);
  requestHeaders.set('x-hello-from-middleware1', 'hello');
 
  // You can also set request headers in NextResponse.next
  const response = NextResponse.next({
    request: {
      // New request headers
      headers: requestHeaders,
    },
  });
 
  // Set a new response header `x-hello-from-middleware2`
  response.headers.set('x-hello-from-middleware2', 'hello');
  return response;
}
```

#### [`next()` no-op example](#next-no-op-example)

This no-op example will return a `200 OK` response with no further action:

Next.js (/app)Next.js (/pages)Other frameworks

middleware.ts

TypeScript

TypeScriptJavaScript

```
import { NextResponse } from 'next/server';
export default function middleware() {
  return NextResponse.next();
}
```

## [More resources](#more-resources)

*   [Redirect with unique tokens](/guides/use-crypto-web-api)

--------------------------------------------------------------------------------
title: "Getting Started with Routing Middleware"
description: "Learn how you can use Routing Middleware, code that executes before a request is processed on a site, to provide speed and personalization to your users."
last_updated: "null"
source: "https://vercel.com/docs/routing-middleware/getting-started"
--------------------------------------------------------------------------------

# Getting Started with Routing Middleware

Copy page

Ask AI about this page

Last updated October 27, 2025

Routing Middleware lets you to run code before your pages load, giving you control over incoming requests. It runs close to your users for fast response times and are perfect for redirects, authentication, and request modification.

Routing Middleware is available on the [Node.js](/docs/functions/runtimes/node-js), [Bun](/docs/functions/runtimes/bun), and [Edge](/docs/functions/runtimes/edge) runtimes. Edge is the default runtime for Routing Middleware. To use Node.js, configure the `runtime` in your middleware config. To use Bun, set [`bunVersion`](/docs/project-configuration#bunversion) in your `vercel.json` file.

## [What you will learn](#what-you-will-learn)

*   Create your first Routing Middleware
*   Redirect users based on URLs
*   Add conditional logic to handle different scenarios
*   Configure which paths your Routing Middleware runs on

## [Prerequisites](#prerequisites)

*   A Vercel project
*   Basic knowledge of JavaScript/TypeScript

## [Creating a Routing Middleware](#creating-a-routing-middleware)

The following steps will guide you through creating your first Routing Middleware.

1.  ### [Create a new file for your Routing Middleware](#create-a-new-file-for-your-routing-middleware)
    
    Create a file called `middleware.ts` in your project root (same level as your `package.json`) and add the following code:
    
    middleware.ts
    
    ```
    export const config = {
      runtime: 'nodejs', // optional: use 'nodejs' or omit for 'edge' (default)
    };
     
    export default function middleware(request: Request) {
      console.log('Request to:', request.url);
      return new Response('Logging request URL from Middleware');
    }
    ```
    
    *   Every request to your site will trigger this function
    *   You log the request URL to see what's being accessed
    *   You return a response to prove the middleware is running
    *   The `runtime` config is optional and defaults to `edge`. To use Bun, set [`bunVersion`](/docs/project-configuration#bunversion) in `vercel.json` instead
    
    Deploy your project and visit any page. You should see "Logging request URL from Middleware" instead of your normal page content.
    
2.  ### [Redirecting users](#redirecting-users)
    
    To redirect users based on their URL, add a new route to your project called `/blog`, and modify your `middleware.ts` to include a redirect condition.
    
    middleware.ts
    
    ```
    export const config = {
      runtime: 'nodejs', // optional: use 'nodejs' or omit for 'edge' (default)
    };
     
    export default function middleware(request: Request) {
      const url = new URL(request.url);
     
      // Redirect old blog path to new one
      if (url.pathname === '/old-blog') {
        return new Response(null, {
          status: 302,
          headers: { Location: '/blog' },
        });
      }
     
      // Let other requests continue normally
      return new Response('Other pages work normally');
    }
    ```
    
    *   You use `new URL(request.url)` to parse the incoming URL
    *   You check if the path matches `/old-blog`
    *   If it does, you return a redirect response (status 302)
    *   The `Location` header tells the browser where to go
    
    Try visiting `/old-blog` - you should be redirected to `/blog`.
    
3.  ### [Configure which paths trigger the middleware](#configure-which-paths-trigger-the-middleware)
    
    By default, Routing Middleware runs on every request. To limit it to specific paths, you can use the [`config`](/docs/routing-middleware/api#config-object) object:
    
    middleware.ts
    
    ```
    export default function middleware(request: Request) {
      const url = new URL(request.url);
     
      // Only handle specific redirects
      if (url.pathname === '/old-blog') {
        return new Response(null, {
          status: 302,
          headers: { Location: '/blog' },
        });
      }
     
      return new Response('Middleware processed this request');
    }
     
    // Configure which paths trigger the Middleware
    export const config = {
      matcher: [
        // Run on all paths except static files
        '/((?!_next/static|_next/image|favicon.ico).*)',
        // Or be more specific:
        // '/blog/:path*',
        // '/api/:path*'
      ],
    };
    ```
    
    *   The [`matcher`](/docs/routing-middleware/api#match-paths-based-on-custom-matcher-config) array defines which paths trigger your Routing Middleware
    *   The regex excludes static files (images, CSS, etc.) for better performance
    *   You can also use simple patterns like `/blog/:path*` for specific sections
    
    See the [API Reference](/docs/routing-middleware/api) for more details on the `config` object and matcher patterns.
    
4.  ### [Debugging Routing Middleware](#debugging-routing-middleware)
    
    When things don't work as expected:
    
    1.  Check the logs: Use `console.log()` liberally and check your [Vercel dashboard](/dashboard) Logs tab
    2.  Test the matcher: Make sure your paths are actually triggering the Routing Middleware
    3.  Verify headers: Log `request.headers` to see what's available
    4.  Test locally: Routing Middleware works in development too so you can debug before deploying
    
    middleware.ts
    
    ```
    export default function middleware(request: Request) {
      // Debug logging
      console.log('URL:', request.url);
      console.log('Method:', request.method);
      console.log('Headers:', Object.fromEntries(request.headers.entries()));
     
      // Your middleware logic here...
    }
    ```
    

## [More resources](#more-resources)

Learn more about Routing Middleware by exploring the following resources:

*   [Routing Middleware](/docs/routing-middleware)
*   [Routing Middleware API Reference](/docs/routing-middleware/api)

--------------------------------------------------------------------------------
title: "SAML Single Sign-On"
description: "Learn how to configure SAML SSO for your organization on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/saml"
--------------------------------------------------------------------------------

# SAML Single Sign-On

Copy page

Ask AI about this page

Last updated October 31, 2025

SAML is available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Those with the [owner](/docs/rbac/access-roles#owner-role) role can access this feature

To manage the [members](/docs/rbac/managing-team-members) of your team through a third-party identity provider like [Okta](https://www.okta.com/) or [Auth0](https://auth0.com/), you can set up the Security Assertion Markup Language (SAML) [feature](#configuring-saml-sso) from your team's settings.

Once enabled, all team members will be able to log in or access [Preview](/docs/deployments/preview-deployments) and Production Deployments using your [selected identity provider](/docs/saml#saml-providers). Any new users signing up with SAML will automatically be added to your team.

For Enterprise customers, you can also automatically manage team member roles and provisioning by setting up [Directory Sync](/docs/directory-sync).

![The SAML SSO settings for a Team.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fsaml-options.png&w=3840&q=75)![The SAML SSO settings for a Team.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fsaml-options-dark.png&w=3840&q=75)

The SAML SSO settings for a Team.

## [Configuring SAML SSO](#configuring-saml-sso)

1.  To configure SAML SSO for your team, you must be an [owner](/docs/rbac/access-roles/team-level-roles) of the team
2.  From your [dashboard](/dashboard), ensure your team is selected in the scope selector
3.  Navigate to the Settings tab and select Security & Privacy
4.  Navigate to the SAML Single Sign-On section. Click Configure and follow the walkthrough to configure SAML SSO for your team with your identity provider of choice
5.  As a further step, you may want to [enforce SAML SSO](#enforcing-saml) for your team

Pro teams will first need to purchase the SAML SSO add-on from their [Billing settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fsettings%2Fbilling%23paid-add-ons) before it can be configured.

## [Enforcing SAML](#enforcing-saml)

For additional security, SAML SSO can be enforced for a team so that all [team members](/docs/rbac/managing-team-members) cannot access any team information unless their current session was authenticated with SAML SSO.

1.  To enforce SAML SSO for your team, you must be an [owner](/docs/rbac/access-roles/team-level-roles) and currently be authenticated with SAML SSO. This ensures that your configuration is working properly before tightening access to your team information
2.  From your [dashboard](/dashboard), navigate to the Settings tab and select Security & Privacy. Then go to the SAML Single Sign-On section
3.  Toggle the Require Team Members to login with SAML switch to Enabled

![SAML SSO configured and enforced.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fsaml-enforced.png&w=3840&q=75)![SAML SSO configured and enforced.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fsaml-enforced-dark.png&w=3840&q=75)

SAML SSO configured and enforced.

When modifying your SAML configuration, the option for enforcing will automatically be turned off. Please verify your new configuration is working correctly by re-authenticating with SAML SSO before re-enabling the option.

## [Authenticating with SAML SSO](#authenticating-with-saml-sso)

Once you have configured SAML, your [team members](/docs/rbac/managing-team-members) can use SAML SSO to log in or sign up to Vercel. To login:

1.  Select the Continue with SAML SSO button on the authentication page, then enter your team's URL. Your team slug is the identifier in the URLs for your team. For example, the identifier for vercel.com/acme is `acme`.
2.  Select Continue with SAML SSO again to be redirected to the third-party authentication provider to finish authenticating. Once completed, you will be logged into Vercel.

SAML SSO sessions last for 24 hours before users must re-authenticate with the third-party SAML provider.

### [Customizing the login page](#customizing-the-login-page)

You can choose to share a Vercel login page that only shows the option to log in with SAML SSO. This prevents your team members from logging in with an account that's not managed by your identity provider.

To use this page, you can set the `saml` query param to your team URL. For example:

```
https://vercel.com/login?saml=team_id
```

![Vercel's login page showing only the SAML SSO login button.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fsaml-login-custom-light.png&w=1080&q=75)![Vercel's login page showing only the SAML SSO login button.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fsaml-login-custom-dark.png&w=1080&q=75)

Vercel's login page showing only the SAML SSO login button.

## [Managing team members](#managing-team-members)

When using SAML SSO, team members can authenticate through your identity provider, but team membership must be managed manually through the Vercel dashboard.

For automatic provisioning and de-provisioning of team members based on your identity provider, consider upgrading to [Directory Sync](/docs/directory-sync), which is available on Enterprise plans.

## [SAML providers](#saml-providers)

Vercel supports the following third-party SAML providers:

*   [Okta](https://www.okta.com/)
*   [Auth0](https://auth0.com/)
*   [Google](https://accounts.google.com/)
*   [Microsoft Entra (formerly Azure Active Directory)](https://www.microsoft.com/en-in/security/business/identity-access/microsoft-entra-single-sign-on)
*   [Microsoft ADFS](https://docs.microsoft.com/en-us/windows-server/identity/active-directory-federation-services)
*   [OneLogin](https://onelogin.com/)
*   [Duo](https://duo.com/product/single-sign-on-sso/)
*   [JumpCloud](https://jumpcloud.com/)
*   [PingFederate](https://www.pingidentity.com/en/platform/capabilities/single-sign-on.html)
*   [ADP](https://apps.adp.com/en-US/home)
*   [Keycloak](https://www.keycloak.org/)
*   [Cyberark](https://www.cyberark.com/products/single-sign-on/)
*   [OpenID](https://openid.net/)
*   [VMware](https://kb.vmware.com/s/article/2034918)
*   [LastPass](https://www.lastpass.com/)
*   [miniOrange](https://www.miniorange.com/products/single-sign-on-sso)
*   [NetIQ](https://www.microfocus.com/en-us/cyberres/identity-access-management/secure-login)
*   [Oracle Cloud](https://docs.oracle.com/en/cloud/paas/content-cloud/administer/enable-single-sign-sso.html)
*   [Salesforce](https://help.salesforce.com/s/articleView?id=sf.sso_about.htm&type=5)
*   [CAS](https://www.apereo.org/projects/cas)
*   [ClassLink](https://www.classlink.com/)
*   [Cloudflare](https://developers.cloudflare.com/cloudflare-one/applications/configure-apps/dash-sso-apps/)
*   [SimpleSAMLphp](https://simplesamlphp.org/)

--------------------------------------------------------------------------------
title: "Vercel security overview"
description: "Vercel provides built-in and customizable features to ensure that your site is secure."
last_updated: "null"
source: "https://vercel.com/docs/security"
--------------------------------------------------------------------------------

# Vercel security overview

Copy page

Ask AI about this page

Last updated April 11, 2025

Cloud-deployed web applications face constant security threats, with attackers launching millions of malicious attacks weekly. Your application, users, and business require robust security measures to stay protected.

A comprehensive security strategy requires both active protection, robust policies, and compliance frameworks:

*   [Security governance and policies](#governance-and-policies) ensure long-term organizational safety, maintain regulatory adherence, and establish consistent security practices across teams.
*   A [Multi-layered protection](#multi-layered-protection) system provides active security against immediate threats and attacks.

## [Governance and policies](#governance-and-policies)

### [Compliance measures](#compliance-measures)

Learn about the [protection and compliance measures](/docs/security/compliance) Vercel takes to ensure the security of your data, including DDoS mitigation, SOC2 Type 2 compliance, Data encryption, and more.

### [Shared responsibility model](#shared-responsibility-model)

A [shared responsibility model](/docs/security/shared-responsibility) is a framework designed to split tasks and obligations between two groups in cloud computing. The model divides duties to ensure security, maintenance, and service functionality.

### [Encryption](#encryption)

Out of the box, every Deployment on Vercel is served over an [HTTPS connection](/docs/security/encryption). The SSL certificates for these unique URLs are automatically generated free of charge.

## [Multi-layered protection](#multi-layered-protection)

Understand how Vercel protects every incoming request with [multiple layers](/docs/security/firewall-concepts#how-vercel-secures-requests) of firewall and deployment protection.

### [Vercel firewall](#vercel-firewall)

The Vercel firewall helps to protect your applications and websites from malicious attacks and unauthorized access through:

*   An enterprise-grade platform-wide firewall available for free for all customers with no configuration required that includes automatic [DDoS mitigation](/docs/security/ddos-mitigation) and protection against low quality traffic.
*   A [Web Application Firewall (WAF)](/docs/security/vercel-waf) that supports custom rules, managed rulesets, and allows customers to challenge automated traffic. You can customize the WAF at the project level.
*   [Observability](/docs/vercel-firewall/firewall-observability) into network traffic and firewall activity, including the access to firewall logs.

--------------------------------------------------------------------------------
title: "Access Control"
description: "Learn about the protection and compliance measures Vercel takes to ensure the security of your data, including DDoS mitigation, SOC 2 compliance and more."
last_updated: "null"
source: "https://vercel.com/docs/security/access-control"
--------------------------------------------------------------------------------

# Access Control

Copy page

Ask AI about this page

Last updated July 18, 2025

Deployments can be protected with [Password protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection) and [SSO protection](/docs/security/deployment-protection#advanced-deployment-protection). Password protection is available for Teams on Pro and Enterprise plans, while SSO protection is only available for Teams on the Enterprise plan. Both methods can be used to protect [Preview](/docs/deployments/environments#preview-environment-pre-production) and [Production](/docs/deployments/environments#production-environment) deployments.

## [Password protection](#password-protection)

Password protection applies to Preview deployments and Production deployments. This feature can be enabled through the Teams Project dashboard. [Read more about in the documentation here](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection).

## [Vercel Authentication](#vercel-authentication)

Vercel Authentication protection applies to Preview deployments and Production deployments. When enabled, a person with a Personal Account that is a member of a Team, can use their login credentials to access the deployment. This feature can be enabled through the Teams Project dashboard.

Both Password protection, and Vercel Authentication can be enabled at the same time. When this is the case, the person trying to access the deployment will be presented with an option to use either method to access the deployment.

[Read more about in the documentation here](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication).

--------------------------------------------------------------------------------
title: "Security & Compliance Measures"
description: "Learn about the protection and compliance measures Vercel takes to ensure the security of your data, including DDoS mitigation and SOC 2 compliance."
last_updated: "null"
source: "https://vercel.com/docs/security/compliance"
--------------------------------------------------------------------------------

# Security & Compliance Measures

Copy page

Ask AI about this page

Last updated October 29, 2025

This page covers the protection and compliance measures Vercel takes to ensure the security of your data, including [DDoS mitigation](/docs/security/ddos-mitigation), [SOC2 Type 2 compliance](#soc-2-type-2), [Data encryption](#data-encryption), and more.

To understand how security responsibilities are divided between you (the customer) and Vercel, see the [shared responsibility model](/docs/security/shared-responsibility). It explains who is responsible for each aspect of keeping your cloud services secure and running smoothly.

## [Compliance](#compliance)

### [SOC 2 Type 2](#soc-2-type-2)

System and Organization Control 2 Type 2 ([SOC 2](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2)) is a compliance framework developed by the American Institute of Certified Public Accountants ([AICPA](https://us.aicpa.org/forthepublic)) that focuses on how an organization's services remain secure and protect customer data. The framework contains 5 Trust Services Categories ([TSCs](https://www.schellman.com/blog/soc-examinations/soc-2-trust-services-criteria-with-tsc)), which contain criteria to evaluate the controls and service commitments of an organization.

Vercel has a SOC 2 Type 2 attestation for Security, Confidentiality, and Availability.

More information is available at [security.vercel.com](https://security.vercel.com/).

### [ISO 27001:2022](#iso-27001:2022)

ISO 27001 is an internationally recognized standard, developed by the International Organization for Standardization (ISO) and International Electrotechnical Commission (IEC), that provides organizations with a systematic approach to securing confidential company and customer information.

Vercel is ISO 27001:2022 certified. Our certificate is available [here](https://www.schellman.com/certificate-directory?certificateNumber=1868222-1).

### [GDPR](#gdpr)

The EU General Data Protection Regulation (GDPR), is a comprehensive data protection law that governs the use, sharing, transfer, and processing of EU personal data. For UK personal data, the provisions of the EU GDPR have been incorporated into UK law as the UK GDPR.

Vercel supports GDPR compliance, which means that we commit to the following:

*   Implement and maintain appropriate technical and organizational security measures surrounding customer data
*   Notify our customers without undue delay of any data breaches
*   Impose similar data protection obligations on our sub-processors as we do for ourselves
*   Respond to applicable [data subjects rights](/legal/privacy-policy#eea), including requests for access, correction, and/or deletion of their personal data
*   Rely on the EU Standard Contractual Clauses and the UK Addendum as valid data transfer mechanisms when transferring personal data outside the EEA

For more information on how Vercel protects your personal data, and the data of your customers, refer to our [Privacy Policy](/legal/privacy-policy) and [Data Processing Addendum](/legal/dpa).

### [PCI DSS](#pci-dss)

Payment Card Industry Data Security Standard (PCI DSS) is a standard that defines the security and privacy requirements for payment card processing. PCI compliance requires that businesses who handle customer credit card information adhere to a set of information security standards.

In alignment with Vercel’s [shared responsibility model](/docs/security/shared-responsibility), Vercel serves as a service provider to customers who process payment and cardholder data. Customers should select an appropriate payment gateway provider to integrate an `iframe` into their application. This ensures that any information entered in the `iframe` goes directly to their payment processor and is isolated from their application’s managed infrastructure on Vercel.

[Learn about PCI DSS iframe integration](/docs/security/pci-dss).

Vercel provides both a Self-Assessment Questionnaire D (SAQ-D) Attestation of Compliance (AOC) for service providers and a Self-Assessment Questionnaire A (SAQ-A) Attestation of Compliance (AOC) for merchants under PCI DSS v4.0.

PCI DSS compliance is a shared responsibility between Vercel and its customers. To help customers better understand their responsibilities, Vercel also provides a Responsibility Matrix which outlines the security and compliance obligations between Vercel and its customers.

A copy of our PCI DSS compliance documentation can be obtained through our [Trust Center](https://security.vercel.com).

[Contact us](https://vercel.com/contact/sales/security) for more details about our SAQ-D and SAQ-A AOC reports or Responsibility Matrix.

### [HIPAA](#hipaa)

Certain businesses, covered entities, and business associates, are required to comply with these regulations to ensure that health data is transmitted without compromising its security. The [Health Information Portability and Accountability Act](https://www.hhs.gov/hipaa/) (HIPAA) is one of the most important sectoral regulations related to privacy within the United States (US). The Secretary for the [Health and Human Services](https://www.hhs.gov/) (HHS) developed a set of required national standards designed to protect the confidentiality, integrity, and availability of health data. Certain businesses, covered entities and business associates, are required to comply to these regulations to ensure that health data is transmitted without compromising its security.

Vercel supports HIPAA compliance as a business associate by committing to the following:

*   Implementing and maintaining appropriate technical and organizational security measures designed to safeguard a customer's [Protected Health Information](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html#:~:text=Information%20is%20Protected-,Protected%20Health%20Information.,health%20information%20(PHI).%22) (PHI)
*   Notifying customers of any data breaches without undue delay
*   Signing Business Associate Agreements (BAAs) with enterprise customers

#### [Additional protection](#additional-protection)

Customers subject to HIPAA may enable [Vercel Secure Compute (available on Enterprise plans)](/docs/secure-compute) for additional layers of protection. This allows customers to have more control over which resources they allow to have access to their information through:

*   Private, isolated cloud environments
*   Dedicated outgoing IP addresses

[VPC peering and VPN support](/docs/secure-compute#vpn-support) (built on top of Secure Compute) allows customers to create fewer entry points into their networks by establishing secure tunnels within their AWS infrastructure.

[Learn](https://security.vercel.com/?itemUid=aec41c33-0f3a-4030-ac59-49adfd4a975b&source=click) about how Vercel supports HIPAA compliance.

[Contact us](https://vercel.com/contact/sales/security) to request a BAA or to add Secure Compute to your plan.

### [EU-U.S Data Privacy Framework](#eu-u.s-data-privacy-framework)

The EU-U.S [Data Privacy Framework](https://www.dataprivacyframework.gov) (DPF) provides U.S. organizations a reliable mechanism for transferring personal data from the European Union (EU), United Kingdom (UK), and Switzerland to the United States (U.S.) while ensuring data protection that is consistent with EU, UK, and Swiss law.

The International Trade Administration (ITA) within the U.S. Department of Commerce administers the DPF program, enabling eligible U.S.-based organizations to certify their compliance with the framework.

Vercel is certified under the EU-U.S. Data Privacy Framework. To view our public listing, visit the [Data Privacy Framework website](https://www.dataprivacyframework.gov/list).

Vercel's certification provides adequate data protection for transferring personal data outside of the EU, UK, and Switzerland under the EU/UK [General Data Protection Regulation](https://gdpr-info.eu/) (GDPR) and UK Data Protection Act 2018, as well as the [Swiss Federal Act on Data Protection](https://www.fedlex.admin.ch/eli/cc/2022/491/en) (FADP).

[Learn more](https://security.vercel.com/?itemName=data_privacy&source=click) about Vercel's data privacy practices or visit our [Privacy Notice](https://vercel.com/legal/privacy-policy) for more information.

### [TISAX](#tisax)

The [Trusted Information Security Assessment Exchange](https://enx.com/tisax) (TISAX) is a recognized standard in the automotive industry, developed by the German Association of the Automotive Industry (VDA) and governed by the ENX Association. TISAX standardizes information security and privacy principles across the automotive supply chain.

Vercel has achieved TISAX Assessment Level 2 (AL2), which covers requirements for handling information with a high need for protection. This assessment supports customers operating in the automotive and manufacturing sectors by:

*   Reducing the time and cost of third party service provider security and privacy reviews
*   Aligning with Original Equipment Manufacturer (OEM) and various automotive supply chain requirements
*   Supporting compliance across regulated environments

TISAX results are not intended for the general public. Vercel's assessment results are available to registered ENX participants through the [ENX Portal](https://portal.enx.com/en-US/TISAX/tisaxassessmentresults).

[Contact us](https://vercel.com/contact/sales/security) for more information.

## [Infrastructure](#infrastructure)

The Vercel CDN and deployment platform primarily uses Amazon Web Services (AWS), and currently has [19 different regions](/docs/regions) and an Anycast network with global IP addresses.

We use a multi-layered security approach that combines people, processes, and technology, including centralized IAM, to regulate access to production resources.

We use cloud security processes to develop and implement procedures for provisioning, configuring, managing, monitoring, and accessing cloud resources. Any changes made in production environments are managed through change control using Infrastructure as Code (IaC).

To ensure always-on security, Vercel's edge infrastructure uses a combination of cloud-native and vendor tooling, including cloud security posture management tooling for continuous scanning and alerting.

When an AWS outage occurs in a region, Vercel will automatically route traffic to the nearest available edge, ensuring network resilience.

### [Where does my data live?](#where-does-my-data-live)

Vercel operates on a shared responsibility model with customers. Customers have the ability to select their preferred region for deploying their code. The default location for Vercel functions is the U.S., but there are dozens of [regions](/docs/regions#region-list) globally that can be used.

Additionally, Vercel may transfer data to and in the United States and anywhere else in the world where Vercel or its service providers maintain data processing operations. Please see Vercel's [Data Processing Addendum](https://vercel.com/legal/dpa) for further details.

### [Failover strategy](#failover-strategy)

*   Vercel uses [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) and our Anycast network to automatically reroute traffic to another region in case of regional failure
*   [Vercel Functions](/docs/functions/configuring-functions/region#automatic-failover) have multiple availability zone redundancy by default. Multi-region redundancy is available depending on your runtime
*   Our core database and data plane is a globally replicated database with rapid manual failover, using multiple availability zones

#### [Regional failover](#regional-failover)

With region-based failover, Vercel data is replicated across multiple regions, and a failover is triggered when an outage occurs in a region. Rapid failover is then provided to secondary regions, allowing users continuous access to critical applications and services with minimal disruption.

#### [Resiliency testing](#resiliency-testing)

To meet RTO/RPO goals, Vercel conducts recurring resiliency testing. This testing simulates regional failures. Throughout testing, service statuses are also monitored to benchmark recovery time, and alert on any disruptions.

### [Data encryption](#data-encryption)

Vercel encrypts data at rest (when on disk) with 256 bit Advanced Encryption Standard (AES-256). While data is in transit (on route between source and destination), Vercel uses HTTPS/TLS 1.3.

If you need isolated runtime infrastructure, you can use [Vercel Secure Compute](/docs/secure-compute) to create a private, isolated cloud environment with dedicated outgoing IP addresses.

### [Data backup](#data-backup)

Vercel backs-up customer data at an interval of every two hours, each backup is persisted for 30 days, and is globally replicated for resiliency against regional disasters. Automatic backups are taken without affecting the performance or availability of the database operations.

All backups are stored separately in a storage service. If a database instance is deleted, all associated backups are also automatically deleted. Backups are periodically tested by the Vercel engineering team.

These backups are not available to customers and are created for Vercel's infrastructure's use in case of disaster.

### [Do Enterprise accounts run on a different infrastructure?](#do-enterprise-accounts-run-on-a-different-infrastructure)

Enterprise Teams on Vercel have their own build infrastructure ensuring isolation from Hobby/Pro accounts on Vercel.

### [Penetration testing and Audit scans](#penetration-testing-and-audit-scans)

Vercel conducts regular penetration testing through third-party penetration testers, and has daily code reviews and static analysis checks.

--------------------------------------------------------------------------------
title: "PCI DSS iframe Integration"
description: "Learn how to integrate an iframe into your application to support PCI DSS compliance."
last_updated: "null"
source: "https://vercel.com/docs/security/pci-dss"
--------------------------------------------------------------------------------

# PCI DSS iframe Integration

Copy page

Ask AI about this page

Last updated June 26, 2025

## [Benefits of using an `iframe`](#benefits-of-using-an-iframe)

When you use an [`iframe`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) to process payments, you create a secure conduit between your end users and your payment provider.

In accordance with Vercel's [shared responsibility model](/docs/security/shared-responsibility), this approach facilitates:

*   Data isolation: The payment card information entered in the `iframe` is isolated from Vercel’s environment and does not pass through Vercel's managed infrastructure
*   Direct data transmission: Information entered in the `iframe` is sent directly to your payment processor so that Vercel never processes, stores, or has access to your end users’ payment card data
*   Reduced PCI DSS scope: With isolation and direct data transmission, the scope of PCI DSS compliance is reduced. This simplifies compliance efforts and enhances security

## [Integrate an `iframe` for payment processing](#integrate-an-iframe-for-payment-processing)

1.  Select a [payment provider](https://www.pcisecuritystandards.org/glossary/payment-processor/) that offers the following:
    
    *   End-to-end encryption
    *   Data tokenization
    *   Built-in fraud detection
    *   3DS authentication protocol
    *   Compliance with latest PCI DSS requirements
2.  Embed the provider’s `iframe` in your application’s payment page
    
    This is an example code for a payment processor's `iframe`:
    
    paymentProcessor.tsx
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    const PaymentProcessorIframe = (): JSX.Element => {
      const paymentProcessorIframeURL = `https://${PAYMENT_PROCESSOR_BASE_URL}.com/secure-payment-form`;
     
      return (
        <div className="container mx-auto my-10 rounded bg-white p-5 shadow-md">
          <iframe
            src={paymentProcessorIframeURL}
            frameBorder="0"
            width="100%"
            height="500px"
            sandbox="allow-forms allow-top-navigation allow-same-origin"
            className="h-auto w-full"
          />
        </div>
      );
    };
     
    export default PaymentProcessorIframe;
    ```
    
    The `sandbox` attribute and its values are often required by the payment processor:
    
    *   `allow-forms`: Enables form submissions in the `iframe`, essential for payment data entry
    *   `allow-top-navigation`: Allows the `iframe` to change the full page URL. This is useful for post-transaction redirections
    *   `allow-same-origin`: Permits the `iframe` to interact with resources from the hosting page's origin. This is important for functionality but slightly reduces isolation

--------------------------------------------------------------------------------
title: "Reverse Proxy Servers and Vercel"
description: "Learn why reverse proxy servers are not recommended with Vercel's firewall."
last_updated: "null"
source: "https://vercel.com/docs/security/reverse-proxy"
--------------------------------------------------------------------------------

# Reverse Proxy Servers and Vercel

Copy page

Ask AI about this page

Last updated September 23, 2025

We do not recommend placing a reverse proxy server in front of your Vercel project as it affects the Vercel's firewall in the following ways:

*   Vercel's CDN loses visibility into the traffic, which reduces the effectiveness of the firewall in identifying suspicious activity.
*   Real end-user IP addresses cannot be accurately identified.
*   If the reverse proxy undergoes a malicious attack, this traffic can be forwarded to the Vercel project and cause usage spikes.
*   If the reverse proxy is compromised, Vercel's firewall cannot automatically purge the cache.

## [Using a reverse proxy server](#using-a-reverse-proxy-server)

However, you may still need to use a reverse proxy server. For example, your organization has legacy web applications protected by a reverse proxy and mandates that your Vercel project also uses this reverse proxy.

In such a case, you want to ensure that Vercel's [platform-wide firewall](/docs/vercel-firewall#platform-wide-firewall) does not block this proxy server due to the reasons mentioned above.

### [Prerequisites](#prerequisites)

*   TLS setup: Disable HTTP→HTTPS redirection for `http://<DOMAIN>/.well-known/acme-challenge/*` on port 80
*   Cache control: Never cache `https://<DOMAIN>/.well-known/vercel/*` paths
*   Plan eligibility:
    *   Hobby/Pro: Verified Proxy Lite only
    *   Enterprise: Lite + Advanced (self-hosted/geolocation preservation)

### [Automatic vs. Manual enablement](#automatic-vs.-manual-enablement)

Verified Proxy is automatically enabled for the providers listed below on all plans. Any other provider or a self-hosted proxy (for example, Nginx, HAProxy, etc) requires a manual onboarding process (Enterprise only).

### [Supported providers (Verified Proxy Lite)](#supported-providers-verified-proxy-lite)

| Provider | Required Header | Configuration |
| --- | --- | --- |
| Fastly | `Fastly-Client-IP` | A built-in header. No additional configuration required. |
| Google Cloud Load Balancing | `X-GCP-Connecting-IP` | Add a custom header: `X-GCP-Connecting-IP: {client_ip_address}` using their [built-in variables](https://cloud.google.com/load-balancing/docs/https/custom-headers#variables). |
| Cloudflare | `CF-Connecting-IP` | A built-in header. No additional configuration required. |
| AWS CloudFront | `CloudFront-Viewer-Address` | Enable the header via the [Origin Request Policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/adding-cloudfront-headers.html#cloudfront-headers-viewer-location). |
| Imperva CDN (Cloud WAF) | `Incap-Client-IP` | A built-in header. No additional configuration required. |
| Akamai | `True-Client-IP` | Enable the header via the property manager. Clients may be able to spoof the header; work with Akamai to harden the configuration. You must also enable the [Origin IP ACL](https://techdocs.akamai.com/origin-ip-acl/docs/welcome) feature. |
| Azure Front Door | `X-Azure-ClientIP` | A built-in header. No additional configuration required. |
| F5 | `X-F5-True-Client-IP` | Add a custom header: `X-F5-True-Client-IP: {client_ip_address}` |

### [Self-hosted reverse proxies (Verified Proxy Advanced)](#self-hosted-reverse-proxies-verified-proxy-advanced)

Verified Proxy Advanced is available on [Enterprise plans](/docs/plans/enterprise)

Ensure that the following requirements are met if you are running self-hosted reverse proxies:

*   Your proxy must have static egress IP addresses assigned. We cannot support dynamic IP addresses.
*   Your proxy must send a custom request header that carries the real client IP (e.g. `x-${team-slug}-connecting-ip`).
*   Your proxy must enable SNI (Server Name Indication) on outbound TLS connections.
*   Use consistent and predictable Vercel project domains for onboarding. For example, use \*.vercel.example.com and ensure your Proxy always sends traffic to those specific hostnames.

For detailed setup instructions, please contact your Customer Success Manager (CSM) or Account Executive (AE).

## [More resources](#more-resources)

*   [Can I use Vercel as a reverse proxy?](/guides/vercel-reverse-proxy-rewrites-external)

--------------------------------------------------------------------------------
title: "Shared Responsibility Model"
description: "Discover the essentials of our Shared Responsibility Model, outlining the key roles and responsibilities for customers, Vercel, and shared aspects in ensuring secure and efficient cloud computing services."
last_updated: "null"
source: "https://vercel.com/docs/security/shared-responsibility"
--------------------------------------------------------------------------------

# Shared Responsibility Model

Copy page

Ask AI about this page

Last updated September 15, 2025

A shared responsibility model is a framework designed to split tasks and obligations between two groups in cloud computing. The model divides duties to ensure security, maintenance, and service functionality.

When using a cloud platform such as Vercel, it is important to understand where your security responsibilities lie, and where Vercel takes responsibility. This is especially important when it comes to handling data, such as user account information, payment details, source code and other sensitive information.

The customer handles their data, applications, and user access management. This includes data encryption, safeguarding sensitive information, and assigning appropriate permissions to users.

Vercel manages infrastructure components, such as compute, storage, and networking. Our role is to guarantee that the platform is secure, dependable, and maintained.

![The shared responsibility model for Vercel.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fshared-responsibility-model-light-mode.png&w=3840&q=75)![The shared responsibility model for Vercel.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fshared-responsibility-model-dark-mode.png&w=3840&q=75)

The shared responsibility model for Vercel.

## [Customer responsibilities](#customer-responsibilities)

*   Security Requirements Assessment: Customers are responsible for evaluating and deciding whether Vercel's platform and the security protection provided meet the specific needs and requirements for their application. By choosing to use our platform, customers acknowledge and accept the level of security coverage offered by Vercel
    *   Handling Malicious Traffic: Customers are responsible for addressing any costs and resource consumption related to malicious traffic. They should assess their security requirements and implement additional safeguards beyond the [protections](/docs/security) provided by Vercel
    *   Payment Transactions: Customers subject to PCI DSS compliance are responsible for choosing an appropriate payment gateway provider to integrate an [iframe into their application](/docs/security/pci-dss). Vercel provides a Responsibility Matrix, available in our [Trust Center](https://security.vercel.com), that further outlines the security and compliance responsibilities between Vercel and its customers.
*   Client-side Data: Customers are responsible for the security and management of data on their clients' devices
*   Source Code: Customers are responsible for securely storing, and maintaining their source code at all times
*   Server-side Encryption: Customers are responsible for encrypting their server-side data, whether it's stored in the file system or in a database
*   Identity & Access Management (IAM): Customers choose and implement their desired level of access control regarding their IAM configuration with tools provided by Vercel
*   Region Selection for Compute: Customers are responsible for selecting the appropriate regions for their compute resources based on their requirements and compliance needs
*   Production Checklist: Customers are responsible for implementing and adhering to recommended best practices provided in [Vercel's production checklist](/docs/production-checklist). The customer must ensure these guidelines for optimizing application performance and security are properly followed and integrated into their application's development and deployment processes
*   Spend Management: Customers are responsible for enabling [Spend Management](/docs/spend-management) to set a reasonable spend amount and configure actions based on the amount as needed

## [Shared responsibilities](#shared-responsibilities)

*   Information and Data: Customers control and own their data. By design, customers determine the access to their data and are responsible for securing and protecting it while in their possession. Vercel does not have visibility into customers' data until they provide it to us. Once in our possession, it is our responsibility to protect and secure it. This shared responsibility ensures the safety and privacy of our customers' data
    *   Integrations: Customers are responsible for deciding which Vercel services to use and the data that is collected or needed to provide those services. This includes making choices about optional features such as [monitoring](/docs/observability/monitoring) and [analytics](/docs/analytics), which give customers more information about their end users. Integrations with third-party services should also be considered in this context, as they can impact the data collected and shared
*   Encryption & Data Integrity: Vercel is responsible for [encryption](/docs/security/encryption) and data integrity for data in transit (when in motion between systems or locations) and at rest for the services Vercel controls. However, customers must ensure that all integrations and third-party services used to interact with Vercel are properly secured. This includes proxies, WAFs, CMSs, and integrations with other third-party services
    *   User Code & Environment Variables: Customers are responsible for managing their application's code, including the exposure of [environment variables](/docs/environment-variables). By providing code and setting environment variables, customers authorize Vercel to build and deploy their application based on the provided parameters. It is essential for customers to ensure proper handling of sensitive information, such as API keys or other secrets, to maintain the security of their application and data
*   Authentication: Customers handle their app's authentication with tools like [NextAuth.js](https://next-auth.js.org/getting-started/introduction). Vercel manages platform authentication and provides [deployment protection](/docs/security/deployment-protection) to help secure the platform for Pro and Hobby users, who authenticate using the [CLI](/docs/cli/login). Enterprise users can access Single Sign-On (SSO). Vercel deployments can be protected in the following ways: [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication), [SSO](/docs/saml), or [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection)
*   Log Management: While Vercel provides access to short-term [runtime logs](/docs/runtime-logs) for debugging purposes, it is the customer's responsibility to set up [log drains](/docs/drains) for long-term log retention, data auditing, or additional visibility into their application's performance

## [Vercel responsibilities](#vercel-responsibilities)

*   Infrastructure: Vercel is responsible for the security and availability of the underlying infrastructure used to provide our services. Vercel maintains strict security protocols and regularly performs upgrades to ensure that our infrastructure is up to date and secure
    *   Multiple Availability Zones and Globally Located Edge Locations: Vercel makes use of [19 different regions](/docs/regions), which are strategically placed around the globe to provide fast and reliable content delivery to customers
*   Compute: Vercel provides a compute environment for customer applications that utilizes Vercel Functions and containers to ensure the secure execution of customer code and middleware. Industry-standard security practices are used to isolate customer applications and ensure they are not impacted by other applications running on the platform
*   Storage: Vercel is responsible for the security and reliability of storage environments for customer data. This includes the storage of application code, configuration files, and other data required to run customer applications. Vercel uses industry-standard encryption and access controls to ensure that customer data is protected from unauthorized access
*   Networking: Vercel is responsible for providing a secure and reliable networking environment for customer applications. This includes the network infrastructure used to connect customer applications to the internet, as well as the firewalls and other security measures used to protect them from unauthorized access. Industry-standard security practices are used to monitor network traffic and detect and respond to potential security threats

--------------------------------------------------------------------------------
title: "Session tracing"
description: "Learn how to trace your sessions to understand performance and infrastructure details."
last_updated: "null"
source: "https://vercel.com/docs/session-tracing"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./37-list-user-events.md) | [Index](./index.md) | [Next →](./39-session-tracing.md)
