**Navigation:** [← Previous](./34-update-the-data-cache-feature.md) | [Index](./index.md) | [Next →](./36-get-a-team.md)

---

# Get the active rolling release information for a project

> Return the Rolling Release for a project, regardless of whether the rollout is active, aborted, or completed. If the feature is enabled but no deployment has occurred yet, null will be returned.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/rolling-release
paths:
  path: /v1/projects/{idOrName}/rolling-release
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
              description: Project ID or project name (URL-encoded)
      query:
        state:
          schema:
            - type: enum<string>
              enum:
                - ACTIVE
                - COMPLETE
                - ABORTED
              required: false
              description: Filter by rolling release state
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
      - label: getRollingRelease
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.rollingRelease.getRollingRelease({
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
              rollingRelease:
                allOf:
                  - nullable: true
                    properties:
                      state:
                        type: string
                        enum:
                          - ACTIVE
                          - COMPLETE
                          - ABORTED
                        description: The current state of the rolling release
                        example: ACTIVE
                      currentDeployment:
                        nullable: true
                        properties:
                          id:
                            type: string
                            description: A string holding the unique ID of the deployment
                            example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
                          name:
                            type: string
                            description: >-
                              The name of the project associated with the
                              deployment at the time that the deployment was
                              created
                            example: my-project
                          url:
                            type: string
                            description: A string with the unique URL of the deployment
                            example: my-instant-deployment-3ij3cxz9qr.now.sh
                          target:
                            nullable: true
                            type: string
                            enum:
                              - staging
                              - production
                            description: >-
                              If defined, either `staging` if a staging alias in
                              the format `<project>.<team>.now.sh` was assigned
                              upon creation, or `production` if the aliases from
                              `alias` were assigned. `null` value indicates the
                              "preview" deployment.
                            example: null
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
                            description: Where was the deployment created from
                            example: cli
                          createdAt:
                            type: number
                            description: >-
                              A number containing the date when the deployment
                              was created in milliseconds
                            example: 1540257589405
                          readyState:
                            type: string
                            enum:
                              - BUILDING
                              - ERROR
                              - INITIALIZING
                              - QUEUED
                              - READY
                              - CANCELED
                            description: >-
                              The state of the deployment depending on the
                              process of deploying, or if it is ready or in an
                              error state
                            example: READY
                          readyStateAt:
                            type: number
                        required:
                          - id
                          - name
                          - url
                          - createdAt
                          - readyState
                        type: object
                        description: The current deployment receiving production traffic
                        example:
                          id: dpl_abc123
                          name: my-shop@main
                          url: my-shop.vercel.app
                          target: production
                          source: git
                          createdAt: 1716206500000
                          readyState: READY
                          readyStateAt: 1716206800000
                      canaryDeployment:
                        nullable: true
                        properties:
                          id:
                            type: string
                            description: A string holding the unique ID of the deployment
                            example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
                          name:
                            type: string
                            description: >-
                              The name of the project associated with the
                              deployment at the time that the deployment was
                              created
                            example: my-project
                          url:
                            type: string
                            description: A string with the unique URL of the deployment
                            example: my-instant-deployment-3ij3cxz9qr.now.sh
                          target:
                            nullable: true
                            type: string
                            enum:
                              - staging
                              - production
                            description: >-
                              If defined, either `staging` if a staging alias in
                              the format `<project>.<team>.now.sh` was assigned
                              upon creation, or `production` if the aliases from
                              `alias` were assigned. `null` value indicates the
                              "preview" deployment.
                            example: null
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
                            description: Where was the deployment created from
                            example: cli
                          createdAt:
                            type: number
                            description: >-
                              A number containing the date when the deployment
                              was created in milliseconds
                            example: 1540257589405
                          readyState:
                            type: string
                            enum:
                              - BUILDING
                              - ERROR
                              - INITIALIZING
                              - QUEUED
                              - READY
                              - CANCELED
                            description: >-
                              The state of the deployment depending on the
                              process of deploying, or if it is ready or in an
                              error state
                            example: READY
                          readyStateAt:
                            type: number
                        required:
                          - id
                          - name
                          - url
                          - createdAt
                          - readyState
                        type: object
                        description: The canary deployment being rolled out
                        example:
                          id: dpl_def456
                          name: my-shop@9c7e2f4
                          url: 9c7e2f4-my-shop.vercel.app
                          target: production
                          source: git
                          createdAt: 1716210100000
                          readyState: READY
                          readyStateAt: 1716210400000
                      queuedDeploymentId:
                        nullable: true
                        type: string
                        description: >-
                          The ID of a deployment queued for the next rolling
                          release
                        example: dpl_ghi789
                      advancementType:
                        type: string
                        enum:
                          - automatic
                          - manual-approval
                        description: The advancement type of the rolling release
                        example: manual-approval
                      stages:
                        items:
                          properties:
                            index:
                              type: number
                              description: The zero-based index of the stage
                              example: 0
                            isFinalStage:
                              type: boolean
                              description: >-
                                Whether or not this stage is the final stage
                                (targetPercentage === 100)
                              example: false
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
                            duration:
                              nullable: true
                              type: number
                              description: >-
                                Duration in seconds for automatic advancement,
                                null for manual stages or the final stage
                              example: null
                            linearShift:
                              type: boolean
                              description: >-
                                Whether to linearly shift traffic over the
                                duration of this stage
                              example: false
                          required:
                            - index
                            - isFinalStage
                            - targetPercentage
                            - requireApproval
                            - duration
                          type: object
                          description: All stages configured for this rolling release
                          example:
                            - index: 0
                              isFinalStage: false
                              targetPercentage: 5
                              requireApproval: true
                              duration: null
                            - index: 1
                              isFinalStage: false
                              targetPercentage: 25
                              requireApproval: true
                              duration: null
                            - index: 2
                              isFinalStage: false
                              targetPercentage: 60
                              requireApproval: true
                              duration: null
                            - index: 3
                              isFinalStage: true
                              targetPercentage: 100
                              requireApproval: false
                              duration: null
                        type: array
                        description: All stages configured for this rolling release
                        example:
                          - index: 0
                            isFinalStage: false
                            targetPercentage: 5
                            requireApproval: true
                            duration: null
                          - index: 1
                            isFinalStage: false
                            targetPercentage: 25
                            requireApproval: true
                            duration: null
                          - index: 2
                            isFinalStage: false
                            targetPercentage: 60
                            requireApproval: true
                            duration: null
                          - index: 3
                            isFinalStage: true
                            targetPercentage: 100
                            requireApproval: false
                            duration: null
                      activeStage:
                        nullable: true
                        properties:
                          index:
                            type: number
                            description: The zero-based index of the stage
                            example: 0
                          isFinalStage:
                            type: boolean
                            description: >-
                              Whether or not this stage is the final stage
                              (targetPercentage === 100)
                            example: false
                          targetPercentage:
                            type: number
                            description: >-
                              The percentage of traffic to serve to the canary
                              deployment (0-100)
                            example: 25
                          requireApproval:
                            type: boolean
                            description: >-
                              Whether or not this stage requires manual approval
                              to proceed
                          duration:
                            nullable: true
                            type: number
                            description: >-
                              Duration in seconds for automatic advancement,
                              null for manual stages or the final stage
                            example: null
                          linearShift:
                            type: boolean
                            description: >-
                              Whether to linearly shift traffic over the
                              duration of this stage
                            example: false
                        required:
                          - index
                          - isFinalStage
                          - targetPercentage
                          - requireApproval
                          - duration
                        type: object
                        description: >-
                          The currently active stage, null if the rollout is
                          aborted
                        example:
                          index: 1
                          isFinalStage: false
                          targetPercentage: 25
                          requireApproval: true
                          duration: null
                      nextStage:
                        nullable: true
                        properties:
                          index:
                            type: number
                            description: The zero-based index of the stage
                            example: 0
                          isFinalStage:
                            type: boolean
                            description: >-
                              Whether or not this stage is the final stage
                              (targetPercentage === 100)
                            example: false
                          targetPercentage:
                            type: number
                            description: >-
                              The percentage of traffic to serve to the canary
                              deployment (0-100)
                            example: 25
                          requireApproval:
                            type: boolean
                            description: >-
                              Whether or not this stage requires manual approval
                              to proceed
                          duration:
                            nullable: true
                            type: number
                            description: >-
                              Duration in seconds for automatic advancement,
                              null for manual stages or the final stage
                            example: null
                          linearShift:
                            type: boolean
                            description: >-
                              Whether to linearly shift traffic over the
                              duration of this stage
                            example: false
                        required:
                          - index
                          - isFinalStage
                          - targetPercentage
                          - requireApproval
                          - duration
                        type: object
                        description: >-
                          The next stage to be activated, null if not in ACTIVE
                          state
                        example:
                          index: 2
                          isFinalStage: false
                          targetPercentage: 60
                          requireApproval: true
                          duration: null
                      startedAt:
                        type: number
                        description: >-
                          Unix timestamp in milliseconds when the rolling
                          release started
                        example: 1716210500000
                      updatedAt:
                        type: number
                        description: >-
                          Unix timestamp in milliseconds when the rolling
                          release was last updated
                        example: 1716210600000
                    required:
                      - state
                      - currentDeployment
                      - canaryDeployment
                      - queuedDeploymentId
                      - advancementType
                      - stages
                      - activeStage
                      - nextStage
                      - startedAt
                      - updatedAt
                    type: object
                    description: >-
                      Rolling release information including configuration and
                      document details, or null if no rolling release exists
            description: >-
              The response format for rolling release endpoints that return
              rolling release information
            requiredProperties:
              - rollingRelease
        examples:
          example:
            value:
              rollingRelease:
                state: ACTIVE
                currentDeployment:
                  id: dpl_abc123
                  name: my-shop@main
                  url: my-shop.vercel.app
                  target: production
                  source: git
                  createdAt: 1716206500000
                  readyState: READY
                  readyStateAt: 1716206800000
                canaryDeployment:
                  id: dpl_def456
                  name: my-shop@9c7e2f4
                  url: 9c7e2f4-my-shop.vercel.app
                  target: production
                  source: git
                  createdAt: 1716210100000
                  readyState: READY
                  readyStateAt: 1716210400000
                queuedDeploymentId: dpl_ghi789
                advancementType: manual-approval
                stages:
                  - index: 0
                    isFinalStage: false
                    targetPercentage: 5
                    requireApproval: true
                    duration: null
                  - index: 1
                    isFinalStage: false
                    targetPercentage: 25
                    requireApproval: true
                    duration: null
                  - index: 2
                    isFinalStage: false
                    targetPercentage: 60
                    requireApproval: true
                    duration: null
                  - index: 3
                    isFinalStage: true
                    targetPercentage: 100
                    requireApproval: false
                    duration: null
                activeStage:
                  index: 1
                  isFinalStage: false
                  targetPercentage: 25
                  requireApproval: true
                  duration: null
                nextStage:
                  index: 2
                  isFinalStage: false
                  targetPercentage: 60
                  requireApproval: true
                  duration: null
                startedAt: 1716210500000
                updatedAt: 1716210600000
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
title: "Update the active rolling release to the next stage for a project"

last_updated: "2025-11-07T00:37:15.425Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/rolling-release/update-the-active-rolling-release-to-the-next-stage-for-a-project"
--------------------------------------------------------------------------------

# Update the active rolling release to the next stage for a project

> Advance a rollout to the next stage. This is only needed when rolling releases is configured to require manual approval.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{idOrName}/rolling-release/approve-stage
paths:
  path: /v1/projects/{idOrName}/rolling-release/approve-stage
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
              description: Project ID or project name (URL-encoded)
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
              nextStageIndex:
                allOf:
                  - description: The index of the stage to transition to
                    type: number
              canaryDeploymentId:
                allOf:
                  - description: >-
                      The id of the canary deployment to approve for the next
                      stage
                    type: string
            requiredProperties:
              - nextStageIndex
              - canaryDeploymentId
        examples:
          example:
            value:
              nextStageIndex: 123
              canaryDeploymentId: <string>
    codeSamples:
      - label: approveRollingReleaseStage
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.rollingRelease.approveRollingReleaseStage({
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
              rollingRelease:
                allOf:
                  - nullable: true
                    properties:
                      state:
                        type: string
                        enum:
                          - ACTIVE
                          - COMPLETE
                          - ABORTED
                        description: The current state of the rolling release
                        example: ACTIVE
                      currentDeployment:
                        nullable: true
                        properties:
                          id:
                            type: string
                            description: A string holding the unique ID of the deployment
                            example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
                          name:
                            type: string
                            description: >-
                              The name of the project associated with the
                              deployment at the time that the deployment was
                              created
                            example: my-project
                          url:
                            type: string
                            description: A string with the unique URL of the deployment
                            example: my-instant-deployment-3ij3cxz9qr.now.sh
                          target:
                            nullable: true
                            type: string
                            enum:
                              - staging
                              - production
                            description: >-
                              If defined, either `staging` if a staging alias in
                              the format `<project>.<team>.now.sh` was assigned
                              upon creation, or `production` if the aliases from
                              `alias` were assigned. `null` value indicates the
                              "preview" deployment.
                            example: null
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
                            description: Where was the deployment created from
                            example: cli
                          createdAt:
                            type: number
                            description: >-
                              A number containing the date when the deployment
                              was created in milliseconds
                            example: 1540257589405
                          readyState:
                            type: string
                            enum:
                              - BUILDING
                              - ERROR
                              - INITIALIZING
                              - QUEUED
                              - READY
                              - CANCELED
                            description: >-
                              The state of the deployment depending on the
                              process of deploying, or if it is ready or in an
                              error state
                            example: READY
                          readyStateAt:
                            type: number
                        required:
                          - id
                          - name
                          - url
                          - createdAt
                          - readyState
                        type: object
                        description: The current deployment receiving production traffic
                        example:
                          id: dpl_abc123
                          name: my-shop@main
                          url: my-shop.vercel.app
                          target: production
                          source: git
                          createdAt: 1716206500000
                          readyState: READY
                          readyStateAt: 1716206800000
                      canaryDeployment:
                        nullable: true
                        properties:
                          id:
                            type: string
                            description: A string holding the unique ID of the deployment
                            example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
                          name:
                            type: string
                            description: >-
                              The name of the project associated with the
                              deployment at the time that the deployment was
                              created
                            example: my-project
                          url:
                            type: string
                            description: A string with the unique URL of the deployment
                            example: my-instant-deployment-3ij3cxz9qr.now.sh
                          target:
                            nullable: true
                            type: string
                            enum:
                              - staging
                              - production
                            description: >-
                              If defined, either `staging` if a staging alias in
                              the format `<project>.<team>.now.sh` was assigned
                              upon creation, or `production` if the aliases from
                              `alias` were assigned. `null` value indicates the
                              "preview" deployment.
                            example: null
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
                            description: Where was the deployment created from
                            example: cli
                          createdAt:
                            type: number
                            description: >-
                              A number containing the date when the deployment
                              was created in milliseconds
                            example: 1540257589405
                          readyState:
                            type: string
                            enum:
                              - BUILDING
                              - ERROR
                              - INITIALIZING
                              - QUEUED
                              - READY
                              - CANCELED
                            description: >-
                              The state of the deployment depending on the
                              process of deploying, or if it is ready or in an
                              error state
                            example: READY
                          readyStateAt:
                            type: number
                        required:
                          - id
                          - name
                          - url
                          - createdAt
                          - readyState
                        type: object
                        description: The canary deployment being rolled out
                        example:
                          id: dpl_def456
                          name: my-shop@9c7e2f4
                          url: 9c7e2f4-my-shop.vercel.app
                          target: production
                          source: git
                          createdAt: 1716210100000
                          readyState: READY
                          readyStateAt: 1716210400000
                      queuedDeploymentId:
                        nullable: true
                        type: string
                        description: >-
                          The ID of a deployment queued for the next rolling
                          release
                        example: dpl_ghi789
                      advancementType:
                        type: string
                        enum:
                          - automatic
                          - manual-approval
                        description: The advancement type of the rolling release
                        example: manual-approval
                      stages:
                        items:
                          properties:
                            index:
                              type: number
                              description: The zero-based index of the stage
                              example: 0
                            isFinalStage:
                              type: boolean
                              description: >-
                                Whether or not this stage is the final stage
                                (targetPercentage === 100)
                              example: false
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
                            duration:
                              nullable: true
                              type: number
                              description: >-
                                Duration in seconds for automatic advancement,
                                null for manual stages or the final stage
                              example: null
                            linearShift:
                              type: boolean
                              description: >-
                                Whether to linearly shift traffic over the
                                duration of this stage
                              example: false
                          required:
                            - index
                            - isFinalStage
                            - targetPercentage
                            - requireApproval
                            - duration
                          type: object
                          description: All stages configured for this rolling release
                          example:
                            - index: 0
                              isFinalStage: false
                              targetPercentage: 5
                              requireApproval: true
                              duration: null
                            - index: 1
                              isFinalStage: false
                              targetPercentage: 25
                              requireApproval: true
                              duration: null
                            - index: 2
                              isFinalStage: false
                              targetPercentage: 60
                              requireApproval: true
                              duration: null
                            - index: 3
                              isFinalStage: true
                              targetPercentage: 100
                              requireApproval: false
                              duration: null
                        type: array
                        description: All stages configured for this rolling release
                        example:
                          - index: 0
                            isFinalStage: false
                            targetPercentage: 5
                            requireApproval: true
                            duration: null
                          - index: 1
                            isFinalStage: false
                            targetPercentage: 25
                            requireApproval: true
                            duration: null
                          - index: 2
                            isFinalStage: false
                            targetPercentage: 60
                            requireApproval: true
                            duration: null
                          - index: 3
                            isFinalStage: true
                            targetPercentage: 100
                            requireApproval: false
                            duration: null
                      activeStage:
                        nullable: true
                        properties:
                          index:
                            type: number
                            description: The zero-based index of the stage
                            example: 0
                          isFinalStage:
                            type: boolean
                            description: >-
                              Whether or not this stage is the final stage
                              (targetPercentage === 100)
                            example: false
                          targetPercentage:
                            type: number
                            description: >-
                              The percentage of traffic to serve to the canary
                              deployment (0-100)
                            example: 25
                          requireApproval:
                            type: boolean
                            description: >-
                              Whether or not this stage requires manual approval
                              to proceed
                          duration:
                            nullable: true
                            type: number
                            description: >-
                              Duration in seconds for automatic advancement,
                              null for manual stages or the final stage
                            example: null
                          linearShift:
                            type: boolean
                            description: >-
                              Whether to linearly shift traffic over the
                              duration of this stage
                            example: false
                        required:
                          - index
                          - isFinalStage
                          - targetPercentage
                          - requireApproval
                          - duration
                        type: object
                        description: >-
                          The currently active stage, null if the rollout is
                          aborted
                        example:
                          index: 1
                          isFinalStage: false
                          targetPercentage: 25
                          requireApproval: true
                          duration: null
                      nextStage:
                        nullable: true
                        properties:
                          index:
                            type: number
                            description: The zero-based index of the stage
                            example: 0
                          isFinalStage:
                            type: boolean
                            description: >-
                              Whether or not this stage is the final stage
                              (targetPercentage === 100)
                            example: false
                          targetPercentage:
                            type: number
                            description: >-
                              The percentage of traffic to serve to the canary
                              deployment (0-100)
                            example: 25
                          requireApproval:
                            type: boolean
                            description: >-
                              Whether or not this stage requires manual approval
                              to proceed
                          duration:
                            nullable: true
                            type: number
                            description: >-
                              Duration in seconds for automatic advancement,
                              null for manual stages or the final stage
                            example: null
                          linearShift:
                            type: boolean
                            description: >-
                              Whether to linearly shift traffic over the
                              duration of this stage
                            example: false
                        required:
                          - index
                          - isFinalStage
                          - targetPercentage
                          - requireApproval
                          - duration
                        type: object
                        description: >-
                          The next stage to be activated, null if not in ACTIVE
                          state
                        example:
                          index: 2
                          isFinalStage: false
                          targetPercentage: 60
                          requireApproval: true
                          duration: null
                      startedAt:
                        type: number
                        description: >-
                          Unix timestamp in milliseconds when the rolling
                          release started
                        example: 1716210500000
                      updatedAt:
                        type: number
                        description: >-
                          Unix timestamp in milliseconds when the rolling
                          release was last updated
                        example: 1716210600000
                    required:
                      - state
                      - currentDeployment
                      - canaryDeployment
                      - queuedDeploymentId
                      - advancementType
                      - stages
                      - activeStage
                      - nextStage
                      - startedAt
                      - updatedAt
                    type: object
                    description: >-
                      Rolling release information including configuration and
                      document details, or null if no rolling release exists
            description: >-
              The response format for rolling release endpoints that return
              rolling release information
            requiredProperties:
              - rollingRelease
        examples:
          example:
            value:
              rollingRelease:
                state: ACTIVE
                currentDeployment:
                  id: dpl_abc123
                  name: my-shop@main
                  url: my-shop.vercel.app
                  target: production
                  source: git
                  createdAt: 1716206500000
                  readyState: READY
                  readyStateAt: 1716206800000
                canaryDeployment:
                  id: dpl_def456
                  name: my-shop@9c7e2f4
                  url: 9c7e2f4-my-shop.vercel.app
                  target: production
                  source: git
                  createdAt: 1716210100000
                  readyState: READY
                  readyStateAt: 1716210400000
                queuedDeploymentId: dpl_ghi789
                advancementType: manual-approval
                stages:
                  - index: 0
                    isFinalStage: false
                    targetPercentage: 5
                    requireApproval: true
                    duration: null
                  - index: 1
                    isFinalStage: false
                    targetPercentage: 25
                    requireApproval: true
                    duration: null
                  - index: 2
                    isFinalStage: false
                    targetPercentage: 60
                    requireApproval: true
                    duration: null
                  - index: 3
                    isFinalStage: true
                    targetPercentage: 100
                    requireApproval: false
                    duration: null
                activeStage:
                  index: 1
                  isFinalStage: false
                  targetPercentage: 25
                  requireApproval: true
                  duration: null
                nextStage:
                  index: 2
                  isFinalStage: false
                  targetPercentage: 60
                  requireApproval: true
                  duration: null
                startedAt: 1716210500000
                updatedAt: 1716210600000
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update the rolling release settings for the project"

last_updated: "2025-11-07T00:37:15.605Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/rolling-release/update-the-rolling-release-settings-for-the-project"
--------------------------------------------------------------------------------

# Update the rolling release settings for the project

> Update (or disable) Rolling Releases for a project. Changing the config never alters a rollout that's already in-flight. It only affects the next production deployment. This also applies to disabling Rolling Releases. If you want to also stop the current rollout, call this endpoint to disable the feature, and then call either the /complete or /abort endpoint. Note: Enabling Rolling Releases automatically enables skew protection on the project with the default value if it wasn't configured already.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/projects/{idOrName}/rolling-release/config
paths:
  path: /v1/projects/{idOrName}/rolling-release/config
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
              description: Project ID or project name (URL-encoded)
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
      - label: updateRollingReleaseConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.rollingRelease.updateRollingReleaseConfig({
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
              rollingRelease:
                allOf:
                  - nullable: true
            requiredProperties:
              - rollingRelease
          - type: object
            properties:
              rollingRelease:
                allOf:
                  - nullable: true
                    properties:
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
                            A stage object configured for a rolling release once
                            a new deployment is triggered the first stage will
                            be read in the proxy for first time visitors, and if
                            a RNG < targetPercentage then it will serve the new
                            deployment. Upon approval the next stage will be
                            read, etc.
                        type: array
                    type: object
            requiredProperties:
              - rollingRelease
        examples:
          example:
            value:
              rollingRelease: <any>
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
title: "Create System Bypass Rule"

last_updated: "2025-11-07T00:37:15.349Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/security/create-system-bypass-rule"
--------------------------------------------------------------------------------

# Create System Bypass Rule

> Create new system bypass rules

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/security/firewall/bypass
paths:
  path: /v1/security/firewall/bypass
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
        projectId:
          schema:
            - type: string
              required: true
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
              domain:
                allOf:
                  - &ref_0
                    type: string
                    pattern: ([a-z]+[a-z.]+)$
                    maxLength: 2544
              projectScope:
                allOf:
                  - &ref_1
                    type: boolean
                    description: >-
                      If the specified bypass will apply to all domains for a
                      project.
              sourceIp:
                allOf:
                  - &ref_2
                    type: string
              allSources:
                allOf:
                  - &ref_3
                    type: boolean
              ttl:
                allOf:
                  - &ref_4
                    type: number
                    description: Time to live in milliseconds
              note:
                allOf:
                  - &ref_5
                    type: string
                    maxLength: 500
            requiredProperties:
              - domain
            additionalProperties: false
          - type: object
            properties:
              domain:
                allOf:
                  - *ref_0
              projectScope:
                allOf:
                  - *ref_1
              sourceIp:
                allOf:
                  - *ref_2
              allSources:
                allOf:
                  - *ref_3
              ttl:
                allOf:
                  - *ref_4
              note:
                allOf:
                  - *ref_5
            requiredProperties:
              - projectScope
            additionalProperties: false
        examples:
          example:
            value:
              domain: <string>
              projectScope: true
              sourceIp: <string>
              allSources: true
              ttl: 123
              note: <string>
    codeSamples:
      - label: addBypassIp
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.addBypassIp({
              projectId: "<id>",
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
              ok:
                allOf:
                  - type: boolean
              result:
                allOf:
                  - items:
                      properties:
                        OwnerId:
                          type: string
                        Id:
                          type: string
                        Domain:
                          type: string
                        Ip:
                          type: string
                        ProjectId:
                          type: string
                        Note:
                          type: string
                        IsProjectRule:
                          type: boolean
                      required:
                        - OwnerId
                        - Id
                        - Domain
                        - ProjectId
                        - Note
                        - IsProjectRule
                      type: object
                    type: array
              pagination:
                allOf:
                  - nullable: true
            requiredProperties:
              - ok
              - result
              - pagination
          - type: object
            properties:
              ok:
                allOf:
                  - type: boolean
              result:
                allOf:
                  - items:
                      properties:
                        OwnerId:
                          type: string
                        Id:
                          type: string
                        Domain:
                          type: string
                        Ip:
                          type: string
                        Action:
                          type: string
                          enum:
                            - block
                            - bypass
                        ProjectId:
                          type: string
                        IsProjectRule:
                          type: boolean
                        Note:
                          type: string
                        CreatedAt:
                          type: string
                        ActorId:
                          type: string
                        UpdatedAt:
                          type: string
                        UpdatedAtHour:
                          type: string
                        DeletedAt:
                          type: string
                        ExpiresAt:
                          nullable: true
                          type: number
                      required:
                        - OwnerId
                        - Id
                        - Domain
                        - Ip
                        - CreatedAt
                        - UpdatedAt
                        - UpdatedAtHour
                      type: object
                    type: array
            requiredProperties:
              - ok
        examples:
          example:
            value:
              ok: true
              result:
                - OwnerId: <string>
                  Id: <string>
                  Domain: <string>
                  Ip: <string>
                  ProjectId: <string>
                  Note: <string>
                  IsProjectRule: true
              pagination: <any>
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Put Firewall Configuration"

last_updated: "2025-11-07T00:37:15.292Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/security/put-firewall-configuration"
--------------------------------------------------------------------------------

# Put Firewall Configuration

> Set the firewall configuration to provided rules and settings. Creates or overwrite the existing firewall configuration.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/security/firewall/config
paths:
  path: /v1/security/firewall/config
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
        projectId:
          schema:
            - type: string
              required: true
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
              firewallEnabled:
                allOf:
                  - type: boolean
              managedRules:
                allOf:
                  - type: object
                    additionalProperties:
                      anyOf: []
              crs:
                allOf:
                  - type: object
                    properties:
                      sd:
                        type: object
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        additionalProperties: false
                        description: >-
                          Scanner Detection - Detect and prevent reconnaissance
                          activities from network scanning tools.
                      ma:
                        type: object
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        additionalProperties: false
                        description: >-
                          Multipart Attack - Block attempts to bypass security
                          controls using multipart/form-data encoding.
                      lfi:
                        type: object
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        additionalProperties: false
                        description: >-
                          Local File Inclusion Attack - Prevent unauthorized
                          access to local files through web applications.
                      rfi:
                        type: object
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        additionalProperties: false
                        description: >-
                          Remote File Inclusion Attack - Prohibit unauthorized
                          upload or execution of remote files.
                      rce:
                        type: object
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        additionalProperties: false
                        description: >-
                          Remote Execution Attack - Prevent unauthorized
                          execution of remote scripts or commands.
                      php:
                        type: object
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        additionalProperties: false
                        description: >-
                          PHP Attack - Safeguard against vulnerability exploits
                          in PHP-based applications.
                      gen:
                        type: object
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        additionalProperties: false
                        description: >-
                          Generic Attack - Provide broad protection from various
                          undefined or novel attack vectors.
                      xss:
                        type: object
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        additionalProperties: false
                        description: >-
                          XSS Attack - Prevent injection of malicious scripts
                          into trusted webpages.
                      sqli:
                        type: object
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        additionalProperties: false
                        description: >-
                          SQL Injection Attack - Prohibit unauthorized use of
                          SQL commands to manipulate databases.
                      sf:
                        type: object
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        additionalProperties: false
                        description: >-
                          Session Fixation Attack - Prevent unauthorized
                          takeover of user sessions by enforcing unique session
                          IDs.
                      java:
                        type: object
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        additionalProperties: false
                        description: >-
                          Java Attack - Mitigate risks of exploitation targeting
                          Java-based applications or components.
                    additionalProperties: false
                    description: Custom Ruleset
              rules:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        name:
                          type: string
                          maxLength: 160
                        description:
                          type: string
                          maxLength: 256
                        active:
                          type: boolean
                        conditionGroup:
                          type: array
                          items:
                            type: object
                            properties:
                              conditions:
                                type: array
                                items:
                                  type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - host
                                        - path
                                        - method
                                        - header
                                        - query
                                        - cookie
                                        - target_path
                                        - route
                                        - raw_path
                                        - ip_address
                                        - region
                                        - protocol
                                        - scheme
                                        - environment
                                        - user_agent
                                        - geo_continent
                                        - geo_country
                                        - geo_country_region
                                        - geo_city
                                        - geo_as_number
                                        - ja4_digest
                                        - ja3_digest
                                        - rate_limit_api_id
                                      description: >-
                                        [Parameter](https://vercel.com/docs/security/vercel-waf/rule-configuration#parameters)
                                        from the incoming traffic.
                                    op:
                                      type: string
                                      enum:
                                        - re
                                        - eq
                                        - neq
                                        - ex
                                        - nex
                                        - inc
                                        - ninc
                                        - pre
                                        - suf
                                        - sub
                                        - gt
                                        - gte
                                        - lt
                                        - lte
                                    neg:
                                      type: boolean
                                    key:
                                      type: string
                                    value:
                                      anyOf:
                                        - type: string
                                        - type: array
                                          items:
                                            type: string
                                          maxItems: 75
                                        - type: number
                                  required:
                                    - type
                                    - op
                                  additionalProperties: false
                                maxItems: 65
                            required:
                              - conditions
                            additionalProperties: false
                          maxItems: 25
                        action:
                          type: object
                          properties:
                            mitigate:
                              type: object
                              properties:
                                action:
                                  type: string
                                  enum:
                                    - log
                                    - challenge
                                    - deny
                                    - bypass
                                    - rate_limit
                                    - redirect
                                rateLimit:
                                  anyOf:
                                    - type: object
                                      properties:
                                        algo:
                                          type: string
                                          enum:
                                            - fixed_window
                                            - token_bucket
                                        window:
                                          type: number
                                        limit:
                                          type: number
                                        keys:
                                          type: array
                                          items:
                                            type: string
                                        action:
                                          anyOf:
                                            - type: string
                                              enum:
                                                - log
                                                - challenge
                                                - deny
                                                - rate_limit
                                            - {}
                                          nullable: true
                                      required:
                                        - algo
                                        - window
                                        - limit
                                        - keys
                                      additionalProperties: false
                                    - {}
                                  nullable: true
                                redirect:
                                  anyOf:
                                    - type: object
                                      properties:
                                        location:
                                          type: string
                                        permanent:
                                          type: boolean
                                      required:
                                        - location
                                        - permanent
                                      additionalProperties: false
                                    - {}
                                  nullable: true
                                actionDuration:
                                  type: string
                                  nullable: true
                                bypassSystem:
                                  type: boolean
                                  nullable: true
                              required:
                                - action
                              additionalProperties: false
                          additionalProperties: false
                      required:
                        - name
                        - active
                        - conditionGroup
                        - action
                      additionalProperties: false
              ips:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        hostname:
                          type: string
                        ip:
                          type: string
                        notes:
                          type: string
                        action:
                          type: string
                          enum:
                            - deny
                            - challenge
                            - log
                            - bypass
                      required:
                        - hostname
                        - ip
                        - action
                      additionalProperties: false
              botIdEnabled:
                allOf:
                  - type: boolean
            required: true
            requiredProperties:
              - firewallEnabled
            additionalProperties: false
        examples:
          example:
            value:
              firewallEnabled: true
              managedRules: {}
              crs:
                sd:
                  active: true
                  action: deny
                ma:
                  active: true
                  action: deny
                lfi:
                  active: true
                  action: deny
                rfi:
                  active: true
                  action: deny
                rce:
                  active: true
                  action: deny
                php:
                  active: true
                  action: deny
                gen:
                  active: true
                  action: deny
                xss:
                  active: true
                  action: deny
                sqli:
                  active: true
                  action: deny
                sf:
                  active: true
                  action: deny
                java:
                  active: true
                  action: deny
              rules:
                - id: <string>
                  name: <string>
                  description: <string>
                  active: true
                  conditionGroup:
                    - conditions:
                        - type: host
                          op: re
                          neg: true
                          key: <string>
                          value: <string>
                  action:
                    mitigate:
                      action: log
                      rateLimit:
                        algo: fixed_window
                        window: 123
                        limit: 123
                        keys:
                          - <string>
                        action: log
                      redirect:
                        location: <string>
                        permanent: true
                      actionDuration: <string>
                      bypassSystem: true
              ips:
                - id: <string>
                  hostname: <string>
                  ip: <string>
                  notes: <string>
                  action: deny
              botIdEnabled: true
    codeSamples:
      - label: putFirewallConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Security.PutFirewallConfig(ctx, \"<id>\", nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: putFirewallConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.putFirewallConfig({
              projectId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                firewallEnabled: true,
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
              active:
                allOf:
                  - properties:
                      ownerId:
                        type: string
                      projectKey:
                        type: string
                      id:
                        type: string
                      version:
                        type: number
                      updatedAt:
                        type: string
                      firewallEnabled:
                        type: boolean
                      crs:
                        properties:
                          sd:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                            required:
                              - active
                              - action
                            type: object
                            description: >-
                              Scanner Detection - Detect and prevent
                              reconnaissance activities from network scanning
                              tools.
                          ma:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                            required:
                              - active
                              - action
                            type: object
                            description: >-
                              Multipart Attack - Block attempts to bypass
                              security controls using multipart/form-data
                              encoding.
                          lfi:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                            required:
                              - active
                              - action
                            type: object
                            description: >-
                              Local File Inclusion Attack - Prevent unauthorized
                              access to local files through web applications.
                          rfi:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                            required:
                              - active
                              - action
                            type: object
                            description: >-
                              Remote File Inclusion Attack - Prohibit
                              unauthorized upload or execution of remote files.
                          rce:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                            required:
                              - active
                              - action
                            type: object
                            description: >-
                              Remote Execution Attack - Prevent unauthorized
                              execution of remote scripts or commands.
                          php:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                            required:
                              - active
                              - action
                            type: object
                            description: >-
                              PHP Attack - Safeguard against vulnerability
                              exploits in PHP-based applications.
                          gen:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                            required:
                              - active
                              - action
                            type: object
                            description: >-
                              Generic Attack - Provide broad protection from
                              various undefined or novel attack vectors.
                          xss:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                            required:
                              - active
                              - action
                            type: object
                            description: >-
                              XSS Attack - Prevent injection of malicious
                              scripts into trusted webpages.
                          sqli:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                            required:
                              - active
                              - action
                            type: object
                            description: >-
                              SQL Injection Attack - Prohibit unauthorized use
                              of SQL commands to manipulate databases.
                          sf:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                            required:
                              - active
                              - action
                            type: object
                            description: >-
                              Session Fixation Attack - Prevent unauthorized
                              takeover of user sessions by enforcing unique
                              session IDs.
                          java:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                            required:
                              - active
                              - action
                            type: object
                            description: >-
                              Java Attack - Mitigate risks of exploitation
                              targeting Java-based applications or components.
                        required:
                          - sd
                          - ma
                          - lfi
                          - rfi
                          - rce
                          - php
                          - gen
                          - xss
                          - sqli
                          - sf
                          - java
                        type: object
                        description: Custom Ruleset
                      rules:
                        items:
                          properties:
                            id:
                              type: string
                            name:
                              type: string
                            description:
                              type: string
                            active:
                              type: boolean
                            conditionGroup:
                              items:
                                properties:
                                  conditions:
                                    items:
                                      properties:
                                        type:
                                          type: string
                                          enum:
                                            - host
                                            - path
                                            - method
                                            - header
                                            - query
                                            - cookie
                                            - target_path
                                            - route
                                            - raw_path
                                            - ip_address
                                            - protocol
                                            - region
                                            - scheme
                                            - environment
                                            - user_agent
                                            - geo_continent
                                            - geo_country
                                            - geo_country_region
                                            - geo_city
                                            - geo_as_number
                                            - ja4_digest
                                            - ja3_digest
                                            - rate_limit_api_id
                                            - server_action
                                        op:
                                          type: string
                                          enum:
                                            - re
                                            - eq
                                            - ex
                                            - inc
                                            - pre
                                            - suf
                                            - sub
                                            - gt
                                            - gte
                                            - lt
                                            - lte
                                            - nex
                                            - ninc
                                            - neq
                                        neg:
                                          type: boolean
                                        key:
                                          type: string
                                        value:
                                          oneOf:
                                            - type: string
                                            - type: number
                                            - items:
                                                type: string
                                              type: array
                                      required:
                                        - type
                                        - op
                                      type: object
                                    type: array
                                required:
                                  - conditions
                                type: object
                              type: array
                            action:
                              properties:
                                mitigate:
                                  properties:
                                    action:
                                      type: string
                                      enum:
                                        - deny
                                        - log
                                        - challenge
                                        - bypass
                                        - rate_limit
                                        - redirect
                                    rateLimit:
                                      nullable: true
                                      properties:
                                        algo:
                                          type: string
                                          enum:
                                            - fixed_window
                                            - token_bucket
                                        window:
                                          type: number
                                        limit:
                                          type: number
                                        keys:
                                          items:
                                            type: string
                                          type: array
                                        action:
                                          nullable: true
                                          type: string
                                          enum:
                                            - deny
                                            - log
                                            - challenge
                                            - rate_limit
                                      required:
                                        - algo
                                        - window
                                        - limit
                                        - keys
                                      type: object
                                    redirect:
                                      nullable: true
                                      properties:
                                        location:
                                          type: string
                                        permanent:
                                          type: boolean
                                      required:
                                        - location
                                        - permanent
                                      type: object
                                    actionDuration:
                                      nullable: true
                                      type: string
                                    bypassSystem:
                                      nullable: true
                                      type: boolean
                                  required:
                                    - action
                                  type: object
                              type: object
                          required:
                            - id
                            - name
                            - active
                            - conditionGroup
                            - action
                          type: object
                        type: array
                      ips:
                        items:
                          properties:
                            id:
                              type: string
                            hostname:
                              type: string
                            ip:
                              type: string
                            notes:
                              type: string
                            action:
                              type: string
                              enum:
                                - deny
                                - log
                                - challenge
                                - bypass
                          required:
                            - id
                            - hostname
                            - ip
                            - action
                          type: object
                        type: array
                      changes:
                        items:
                          type: object
                        type: array
                      managedRules:
                        properties:
                          bot_protection:
                            properties:
                              active:
                                type: boolean
                              action:
                                type: string
                                enum:
                                  - deny
                                  - log
                                  - challenge
                              updatedAt:
                                type: string
                              userId:
                                type: string
                              username:
                                type: string
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
                                  - deny
                                  - log
                                  - challenge
                              updatedAt:
                                type: string
                              userId:
                                type: string
                              username:
                                type: string
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
                                  - deny
                                  - log
                                  - challenge
                              updatedAt:
                                type: string
                              userId:
                                type: string
                              username:
                                type: string
                            required:
                              - active
                            type: object
                        type: object
                      botIdEnabled:
                        type: boolean
                    required:
                      - ownerId
                      - projectKey
                      - id
                      - version
                      - updatedAt
                      - firewallEnabled
                      - crs
                      - rules
                      - ips
                      - changes
                    type: object
            requiredProperties:
              - active
        examples:
          example:
            value:
              active:
                ownerId: <string>
                projectKey: <string>
                id: <string>
                version: 123
                updatedAt: <string>
                firewallEnabled: true
                crs:
                  sd:
                    active: true
                    action: deny
                  ma:
                    active: true
                    action: deny
                  lfi:
                    active: true
                    action: deny
                  rfi:
                    active: true
                    action: deny
                  rce:
                    active: true
                    action: deny
                  php:
                    active: true
                    action: deny
                  gen:
                    active: true
                    action: deny
                  xss:
                    active: true
                    action: deny
                  sqli:
                    active: true
                    action: deny
                  sf:
                    active: true
                    action: deny
                  java:
                    active: true
                    action: deny
                rules:
                  - id: <string>
                    name: <string>
                    description: <string>
                    active: true
                    conditionGroup:
                      - conditions:
                          - type: host
                            op: re
                            neg: true
                            key: <string>
                            value: <string>
                    action:
                      mitigate:
                        action: deny
                        rateLimit:
                          algo: fixed_window
                          window: 123
                          limit: 123
                          keys:
                            - <string>
                          action: deny
                        redirect:
                          location: <string>
                          permanent: true
                        actionDuration: <string>
                        bypassSystem: true
                ips:
                  - id: <string>
                    hostname: <string>
                    ip: <string>
                    notes: <string>
                    action: deny
                changes:
                  - {}
                managedRules:
                  bot_protection:
                    active: true
                    action: deny
                    updatedAt: <string>
                    userId: <string>
                    username: <string>
                  ai_bots:
                    active: true
                    action: deny
                    updatedAt: <string>
                    userId: <string>
                    username: <string>
                  owasp:
                    active: true
                    action: deny
                    updatedAt: <string>
                    userId: <string>
                    username: <string>
                botIdEnabled: true
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
title: "Read active attack data"

last_updated: "2025-11-07T00:37:15.333Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/security/read-active-attack-data"
--------------------------------------------------------------------------------

# Read active attack data

> Retrieve active attack data within the last N days (default: 1 day)

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/attack-status
paths:
  path: /v1/security/firewall/attack-status
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
              required: true
        since:
          schema:
            - type: number
              required: false
              minimum: 1
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
      - label: getActiveAttackStatus
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.getActiveAttackStatus({
              projectId: "<id>",
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
          - type: object
            properties:
              anomalies:
                allOf:
                  - items:
                      properties:
                        projectId:
                          type: string
                        ownerId:
                          type: string
                        startTime:
                          type: number
                        endTime:
                          nullable: true
                          type: number
                        atMinute:
                          type: number
                        state:
                          type: string
                        affectedHostMap:
                          additionalProperties:
                            properties:
                              anomalyAlerts:
                                additionalProperties:
                                  properties:
                                    at_minute:
                                      type: string
                                    zscore:
                                      type: number
                                    total_requests_minute:
                                      type: number
                                    avg_requests:
                                      type: number
                                    stddev_requests:
                                      type: number
                                  required:
                                    - at_minute
                                    - zscore
                                    - total_requests_minute
                                    - avg_requests
                                    - stddev_requests
                                  type: object
                                type: object
                              ddosAlerts:
                                additionalProperties:
                                  properties:
                                    atMinute:
                                      type: string
                                    totalReqs:
                                      type: number
                                  required:
                                    - atMinute
                                    - totalReqs
                                  type: object
                                type: object
                            type: object
                          type: object
                      required:
                        - projectId
                        - ownerId
                        - startTime
                        - endTime
                        - atMinute
                        - affectedHostMap
                      type: object
                    type: array
            requiredProperties:
              - anomalies
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
title: "Read Firewall Actions by Project"

last_updated: "2025-11-07T00:37:15.485Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/security/read-firewall-actions-by-project"
--------------------------------------------------------------------------------

# Read Firewall Actions by Project

> Retrieve firewall actions for a project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/events
paths:
  path: /v1/security/firewall/events
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security: []
    parameters:
      path: {}
      query:
        projectId:
          schema:
            - type: string
              required: true
        startTimestamp:
          schema:
            - type: number
              required: false
        endTimestamp:
          schema:
            - type: number
              required: false
        hosts:
          schema:
            - type: string
              required: false
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: get_/v1/security/firewall/events
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel();

          async function run() {
            const result = await vercel.security.getV1SecurityFirewallEvents({
              projectId: "<id>",
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
              actions:
                allOf:
                  - items:
                      properties:
                        startTime:
                          type: string
                        endTime:
                          type: string
                        isActive:
                          type: boolean
                        action_type:
                          type: string
                        host:
                          type: string
                        public_ip:
                          type: string
                        count:
                          type: number
                      required:
                        - startTime
                        - endTime
                        - isActive
                        - action_type
                        - host
                        - public_ip
                        - count
                      type: object
                    type: array
            requiredProperties:
              - actions
        examples:
          example:
            value:
              actions:
                - startTime: <string>
                  endTime: <string>
                  isActive: true
                  action_type: <string>
                  host: <string>
                  public_ip: <string>
                  count: 123
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Read Firewall Configuration"

last_updated: "2025-11-07T00:37:15.323Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/security/read-firewall-configuration"
--------------------------------------------------------------------------------

# Read Firewall Configuration

> Retrieve the specified firewall configuration for a project. The deployed configVersion will be `active`

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/config/{configVersion}
paths:
  path: /v1/security/firewall/config/{configVersion}
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
        configVersion:
          schema:
            - type: string
              required: true
              description: The deployed configVersion for the firewall configuration
      query:
        projectId:
          schema:
            - type: string
              required: true
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
      - label: getFirewallConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Security.GetFirewallConfig(ctx, \"<id>\", \"<value>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getFirewallConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.getFirewallConfig({
              projectId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              configVersion: "<value>",
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
              ownerId:
                allOf:
                  - type: string
              projectKey:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
              version:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: string
              firewallEnabled:
                allOf:
                  - type: boolean
              crs:
                allOf:
                  - properties:
                      sd:
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        type: object
                        description: >-
                          Scanner Detection - Detect and prevent reconnaissance
                          activities from network scanning tools.
                      ma:
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        type: object
                        description: >-
                          Multipart Attack - Block attempts to bypass security
                          controls using multipart/form-data encoding.
                      lfi:
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        type: object
                        description: >-
                          Local File Inclusion Attack - Prevent unauthorized
                          access to local files through web applications.
                      rfi:
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        type: object
                        description: >-
                          Remote File Inclusion Attack - Prohibit unauthorized
                          upload or execution of remote files.
                      rce:
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        type: object
                        description: >-
                          Remote Execution Attack - Prevent unauthorized
                          execution of remote scripts or commands.
                      php:
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        type: object
                        description: >-
                          PHP Attack - Safeguard against vulnerability exploits
                          in PHP-based applications.
                      gen:
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        type: object
                        description: >-
                          Generic Attack - Provide broad protection from various
                          undefined or novel attack vectors.
                      xss:
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        type: object
                        description: >-
                          XSS Attack - Prevent injection of malicious scripts
                          into trusted webpages.
                      sqli:
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        type: object
                        description: >-
                          SQL Injection Attack - Prohibit unauthorized use of
                          SQL commands to manipulate databases.
                      sf:
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        type: object
                        description: >-
                          Session Fixation Attack - Prevent unauthorized
                          takeover of user sessions by enforcing unique session
                          IDs.
                      java:
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                        required:
                          - active
                          - action
                        type: object
                        description: >-
                          Java Attack - Mitigate risks of exploitation targeting
                          Java-based applications or components.
                    required:
                      - sd
                      - ma
                      - lfi
                      - rfi
                      - rce
                      - php
                      - gen
                      - xss
                      - sqli
                      - sf
                      - java
                    type: object
                    description: Custom Ruleset
              rules:
                allOf:
                  - items:
                      properties:
                        id:
                          type: string
                        name:
                          type: string
                        description:
                          type: string
                        active:
                          type: boolean
                        conditionGroup:
                          items:
                            properties:
                              conditions:
                                items:
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - host
                                        - path
                                        - method
                                        - header
                                        - query
                                        - cookie
                                        - target_path
                                        - route
                                        - raw_path
                                        - ip_address
                                        - protocol
                                        - region
                                        - scheme
                                        - environment
                                        - user_agent
                                        - geo_continent
                                        - geo_country
                                        - geo_country_region
                                        - geo_city
                                        - geo_as_number
                                        - ja4_digest
                                        - ja3_digest
                                        - rate_limit_api_id
                                        - server_action
                                      description: >-
                                        [Parameter](https://vercel.com/docs/security/vercel-waf/rule-configuration#parameters)
                                        from the incoming traffic.
                                    op:
                                      type: string
                                      enum:
                                        - re
                                        - eq
                                        - ex
                                        - inc
                                        - pre
                                        - suf
                                        - sub
                                        - gt
                                        - gte
                                        - lt
                                        - lte
                                        - nex
                                        - ninc
                                        - neq
                                    neg:
                                      type: boolean
                                    key:
                                      type: string
                                    value:
                                      oneOf:
                                        - type: string
                                        - type: number
                                        - items:
                                            type: string
                                          type: array
                                  required:
                                    - type
                                    - op
                                  type: object
                                type: array
                            required:
                              - conditions
                            type: object
                          type: array
                        action:
                          properties:
                            mitigate:
                              properties:
                                action:
                                  type: string
                                  enum:
                                    - deny
                                    - log
                                    - challenge
                                    - bypass
                                    - rate_limit
                                    - redirect
                                rateLimit:
                                  nullable: true
                                  properties:
                                    algo:
                                      type: string
                                      enum:
                                        - fixed_window
                                        - token_bucket
                                    window:
                                      type: number
                                    limit:
                                      type: number
                                    keys:
                                      items:
                                        type: string
                                      type: array
                                    action:
                                      nullable: true
                                      type: string
                                      enum:
                                        - deny
                                        - log
                                        - challenge
                                        - rate_limit
                                  required:
                                    - algo
                                    - window
                                    - limit
                                    - keys
                                  type: object
                                redirect:
                                  nullable: true
                                  properties:
                                    location:
                                      type: string
                                    permanent:
                                      type: boolean
                                  required:
                                    - location
                                    - permanent
                                  type: object
                                actionDuration:
                                  nullable: true
                                  type: string
                                bypassSystem:
                                  nullable: true
                                  type: boolean
                              required:
                                - action
                              type: object
                          type: object
                      required:
                        - id
                        - name
                        - active
                        - conditionGroup
                        - action
                      type: object
                    type: array
              ips:
                allOf:
                  - items:
                      properties:
                        id:
                          type: string
                        hostname:
                          type: string
                        ip:
                          type: string
                        notes:
                          type: string
                        action:
                          type: string
                          enum:
                            - deny
                            - log
                            - challenge
                            - bypass
                      required:
                        - id
                        - hostname
                        - ip
                        - action
                      type: object
                    type: array
              changes:
                allOf:
                  - items:
                      type: object
                    type: array
              managedRules:
                allOf:
                  - properties:
                      bot_protection:
                        properties:
                          active:
                            type: boolean
                          action:
                            type: string
                            enum:
                              - deny
                              - log
                              - challenge
                          updatedAt:
                            type: string
                          userId:
                            type: string
                          username:
                            type: string
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
                              - deny
                              - log
                              - challenge
                          updatedAt:
                            type: string
                          userId:
                            type: string
                          username:
                            type: string
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
                              - deny
                              - log
                              - challenge
                          updatedAt:
                            type: string
                          userId:
                            type: string
                          username:
                            type: string
                        required:
                          - active
                        type: object
                    type: object
              botIdEnabled:
                allOf:
                  - type: boolean
            requiredProperties:
              - ownerId
              - projectKey
              - id
              - version
              - updatedAt
              - firewallEnabled
              - crs
              - rules
              - ips
              - changes
        examples:
          example:
            value:
              ownerId: <string>
              projectKey: <string>
              id: <string>
              version: 123
              updatedAt: <string>
              firewallEnabled: true
              crs:
                sd:
                  active: true
                  action: deny
                ma:
                  active: true
                  action: deny
                lfi:
                  active: true
                  action: deny
                rfi:
                  active: true
                  action: deny
                rce:
                  active: true
                  action: deny
                php:
                  active: true
                  action: deny
                gen:
                  active: true
                  action: deny
                xss:
                  active: true
                  action: deny
                sqli:
                  active: true
                  action: deny
                sf:
                  active: true
                  action: deny
                java:
                  active: true
                  action: deny
              rules:
                - id: <string>
                  name: <string>
                  description: <string>
                  active: true
                  conditionGroup:
                    - conditions:
                        - type: host
                          op: re
                          neg: true
                          key: <string>
                          value: <string>
                  action:
                    mitigate:
                      action: deny
                      rateLimit:
                        algo: fixed_window
                        window: 123
                        limit: 123
                        keys:
                          - <string>
                        action: deny
                      redirect:
                        location: <string>
                        permanent: true
                      actionDuration: <string>
                      bypassSystem: true
              ips:
                - id: <string>
                  hostname: <string>
                  ip: <string>
                  notes: <string>
                  action: deny
              changes:
                - {}
              managedRules:
                bot_protection:
                  active: true
                  action: deny
                  updatedAt: <string>
                  userId: <string>
                  username: <string>
                ai_bots:
                  active: true
                  action: deny
                  updatedAt: <string>
                  userId: <string>
                  username: <string>
                owasp:
                  active: true
                  action: deny
                  updatedAt: <string>
                  userId: <string>
                  username: <string>
              botIdEnabled: true
        description: >-
          If the firewall configuration includes a [custom managed
          ruleset](https://vercel.com/docs/security/vercel-waf/managed-rulesets),
          it will include a `crs` item that has the following values: sd:
          Scanner Detection ma: Multipart Attack lfi: Local File Inclusion
          Attack rfi: Remote File Inclusion Attack rce: Remote Execution Attack
          php: PHP Attack gen: Generic Attack xss: XSS Attack sqli: SQL
          Injection Attack sf: Session Fixation Attack java: Java Attack
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
title: "Read System Bypass"

last_updated: "2025-11-07T00:37:15.291Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/security/read-system-bypass"
--------------------------------------------------------------------------------

# Read System Bypass

> Retrieve the system bypass rules configured for the specified project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/bypass
paths:
  path: /v1/security/firewall/bypass
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
              required: true
        limit:
          schema:
            - type: number
              required: false
              maximum: 256
              example: 10
        sourceIp:
          schema:
            - type: string
              required: false
              description: Filter by source IP
              maxLength: 49
        domain:
          schema:
            - type: string
              required: false
              description: Filter by domain
              maxLength: 2544
        projectScope:
          schema:
            - type: boolean
              required: false
              description: Filter by project scoped rules
        offset:
          schema:
            - type: string
              required: false
              description: Used for pagination. Retrieves results after the provided id
              maxLength: 2560
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
      - label: getBypassIp
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.getBypassIp({
              projectId: "<id>",
              limit: 10,
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
              result:
                allOf:
                  - items:
                      properties:
                        OwnerId:
                          type: string
                        Id:
                          type: string
                        Domain:
                          type: string
                        Ip:
                          type: string
                        Action:
                          type: string
                          enum:
                            - block
                            - bypass
                        ProjectId:
                          type: string
                        IsProjectRule:
                          type: boolean
                        Note:
                          type: string
                        CreatedAt:
                          type: string
                        ActorId:
                          type: string
                        UpdatedAt:
                          type: string
                        UpdatedAtHour:
                          type: string
                        DeletedAt:
                          type: string
                        ExpiresAt:
                          nullable: true
                          type: number
                      required:
                        - OwnerId
                        - Id
                        - Domain
                        - Ip
                        - CreatedAt
                        - UpdatedAt
                        - UpdatedAtHour
                      type: object
                    type: array
              pagination:
                allOf:
                  - properties:
                      OwnerId:
                        type: string
                      Id:
                        type: string
                    required:
                      - OwnerId
                      - Id
                    type: object
            requiredProperties:
              - result
        examples:
          example:
            value:
              result:
                - OwnerId: <string>
                  Id: <string>
                  Domain: <string>
                  Ip: <string>
                  Action: block
                  ProjectId: <string>
                  IsProjectRule: true
                  Note: <string>
                  CreatedAt: <string>
                  ActorId: <string>
                  UpdatedAt: <string>
                  UpdatedAtHour: <string>
                  DeletedAt: <string>
                  ExpiresAt: 123
              pagination:
                OwnerId: <string>
                Id: <string>
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Remove System Bypass Rule"

last_updated: "2025-11-07T00:37:15.329Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/security/remove-system-bypass-rule"
--------------------------------------------------------------------------------

# Remove System Bypass Rule

> Remove system bypass rules

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/security/firewall/bypass
paths:
  path: /v1/security/firewall/bypass
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
      query:
        projectId:
          schema:
            - type: string
              required: true
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
              domain:
                allOf:
                  - &ref_0
                    type: string
                    pattern: ([a-z]+[a-z.]+)$
                    maxLength: 2544
              projectScope:
                allOf:
                  - &ref_1
                    type: boolean
              sourceIp:
                allOf:
                  - &ref_2
                    type: string
              allSources:
                allOf:
                  - &ref_3
                    type: boolean
              note:
                allOf:
                  - &ref_4
                    type: string
                    maxLength: 500
            requiredProperties:
              - domain
            additionalProperties: false
          - type: object
            properties:
              domain:
                allOf:
                  - *ref_0
              projectScope:
                allOf:
                  - *ref_1
              sourceIp:
                allOf:
                  - *ref_2
              allSources:
                allOf:
                  - *ref_3
              note:
                allOf:
                  - *ref_4
            requiredProperties:
              - projectScope
            additionalProperties: false
        examples:
          example:
            value:
              domain: <string>
              projectScope: true
              sourceIp: <string>
              allSources: true
              note: <string>
    codeSamples:
      - label: removeBypassIp
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.removeBypassIp({
              projectId: "<id>",
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
              ok:
                allOf:
                  - type: boolean
            requiredProperties:
              - ok
        examples:
          example:
            value:
              ok: true
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update Attack Challenge mode"

last_updated: "2025-11-07T00:37:15.551Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/security/update-attack-challenge-mode"
--------------------------------------------------------------------------------

# Update Attack Challenge mode

> Update the setting for determining if the project has Attack Challenge mode enabled.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/security/attack-mode
paths:
  path: /v1/security/attack-mode
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
              projectId:
                allOf:
                  - type: string
              attackModeEnabled:
                allOf:
                  - type: boolean
              attackModeActiveUntil:
                allOf:
                  - type: number
                    nullable: true
            required: true
            requiredProperties:
              - projectId
              - attackModeEnabled
        examples:
          example:
            value:
              projectId: <string>
              attackModeEnabled: true
              attackModeActiveUntil: 123
    codeSamples:
      - label: updateAttackChallengeMode
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Security.UpdateAttackChallengeMode(ctx, nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateAttackChallengeMode
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.updateAttackChallengeMode({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                projectId: "<id>",
                attackModeEnabled: false,
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
              attackModeEnabled:
                allOf:
                  - type: boolean
              attackModeUpdatedAt:
                allOf:
                  - type: number
            requiredProperties:
              - attackModeEnabled
              - attackModeUpdatedAt
        examples:
          example:
            value:
              attackModeEnabled: true
              attackModeUpdatedAt: 123
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
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update Firewall Configuration"

last_updated: "2025-11-07T00:37:16.068Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/security/update-firewall-configuration"
--------------------------------------------------------------------------------

# Update Firewall Configuration

> Process updates to modify the existing firewall config for a project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/security/firewall/config
paths:
  path: /v1/security/firewall/config
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
        projectId:
          schema:
            - type: string
              required: true
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
              action:
                allOf:
                  - type: string
                    enum:
                      - firewallEnabled
              id:
                allOf:
                  - nullable: true
              value:
                allOf:
                  - type: boolean
            required: true
            description: Enable Firewall
            requiredProperties:
              - action
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - rules.insert
              id:
                allOf:
                  - nullable: true
              value:
                allOf:
                  - type: object
                    properties:
                      name:
                        type: string
                        maxLength: 160
                      description:
                        type: string
                        maxLength: 256
                      active:
                        type: boolean
                      conditionGroup:
                        type: array
                        items:
                          type: object
                          properties:
                            conditions:
                              type: array
                              items:
                                type: object
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - host
                                      - path
                                      - method
                                      - header
                                      - query
                                      - cookie
                                      - target_path
                                      - route
                                      - raw_path
                                      - ip_address
                                      - region
                                      - protocol
                                      - scheme
                                      - environment
                                      - user_agent
                                      - geo_continent
                                      - geo_country
                                      - geo_country_region
                                      - geo_city
                                      - geo_as_number
                                      - ja4_digest
                                      - ja3_digest
                                      - rate_limit_api_id
                                      - server_action
                                  op:
                                    type: string
                                    enum:
                                      - re
                                      - eq
                                      - neq
                                      - ex
                                      - nex
                                      - inc
                                      - ninc
                                      - pre
                                      - suf
                                      - sub
                                      - gt
                                      - gte
                                      - lt
                                      - lte
                                  neg:
                                    type: boolean
                                  key:
                                    type: string
                                  value:
                                    oneOf:
                                      - type: string
                                      - type: array
                                        items:
                                          type: string
                                        maxItems: 75
                                      - type: number
                                required:
                                  - type
                                  - op
                                additionalProperties: false
                              maxItems: 65
                          required:
                            - conditions
                          additionalProperties: false
                        maxItems: 25
                      action:
                        type: object
                        properties:
                          mitigate:
                            type: object
                            properties:
                              action:
                                type: string
                                enum:
                                  - log
                                  - challenge
                                  - deny
                                  - bypass
                                  - rate_limit
                                  - redirect
                              rateLimit:
                                anyOf:
                                  - type: object
                                    properties:
                                      algo:
                                        type: string
                                        enum:
                                          - fixed_window
                                          - token_bucket
                                      window:
                                        type: number
                                      limit:
                                        type: number
                                      keys:
                                        type: array
                                        items:
                                          type: string
                                      action:
                                        anyOf:
                                          - type: string
                                            enum:
                                              - log
                                              - challenge
                                              - deny
                                              - rate_limit
                                          - {}
                                        nullable: true
                                    required:
                                      - algo
                                      - window
                                      - limit
                                      - keys
                                    additionalProperties: false
                                  - {}
                                nullable: true
                              redirect:
                                anyOf:
                                  - type: object
                                    properties:
                                      location:
                                        type: string
                                      permanent:
                                        type: boolean
                                    required:
                                      - location
                                      - permanent
                                    additionalProperties: false
                                  - {}
                                nullable: true
                              actionDuration:
                                type: string
                                nullable: true
                              bypassSystem:
                                type: boolean
                                nullable: true
                            required:
                              - action
                            additionalProperties: false
                        additionalProperties: false
                    required:
                      - name
                      - active
                      - conditionGroup
                      - action
                    additionalProperties: false
            required: true
            description: Add a custom rule
            requiredProperties:
              - action
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - rules.update
              id:
                allOf:
                  - type: string
              value:
                allOf:
                  - type: object
                    properties:
                      name:
                        type: string
                        maxLength: 160
                      description:
                        type: string
                        maxLength: 256
                      active:
                        type: boolean
                      conditionGroup:
                        type: array
                        items:
                          type: object
                          properties:
                            conditions:
                              type: array
                              items:
                                type: object
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - host
                                      - path
                                      - method
                                      - header
                                      - query
                                      - cookie
                                      - target_path
                                      - route
                                      - raw_path
                                      - ip_address
                                      - region
                                      - protocol
                                      - scheme
                                      - environment
                                      - user_agent
                                      - geo_continent
                                      - geo_country
                                      - geo_country_region
                                      - geo_city
                                      - geo_as_number
                                      - ja4_digest
                                      - ja3_digest
                                      - rate_limit_api_id
                                      - server_action
                                  op:
                                    type: string
                                    enum:
                                      - re
                                      - eq
                                      - neq
                                      - ex
                                      - nex
                                      - inc
                                      - ninc
                                      - pre
                                      - suf
                                      - sub
                                      - gt
                                      - gte
                                      - lt
                                      - lte
                                  neg:
                                    type: boolean
                                  key:
                                    type: string
                                  value:
                                    anyOf:
                                      - type: string
                                      - type: array
                                        items:
                                          type: string
                                        maxItems: 75
                                      - type: number
                                required:
                                  - type
                                  - op
                                additionalProperties: false
                              maxItems: 65
                          required:
                            - conditions
                          additionalProperties: false
                        maxItems: 25
                      action:
                        type: object
                        properties:
                          mitigate:
                            type: object
                            properties:
                              action:
                                type: string
                                enum:
                                  - log
                                  - challenge
                                  - deny
                                  - bypass
                                  - rate_limit
                                  - redirect
                              rateLimit:
                                anyOf:
                                  - type: object
                                    properties:
                                      algo:
                                        type: string
                                        enum:
                                          - fixed_window
                                          - token_bucket
                                      window:
                                        type: number
                                      limit:
                                        type: number
                                      keys:
                                        type: array
                                        items:
                                          type: string
                                      action:
                                        anyOf:
                                          - type: string
                                            enum:
                                              - log
                                              - challenge
                                              - deny
                                              - rate_limit
                                          - {}
                                        nullable: true
                                    required:
                                      - algo
                                      - window
                                      - limit
                                      - keys
                                    additionalProperties: false
                                  - {}
                                nullable: true
                              redirect:
                                anyOf:
                                  - type: object
                                    properties:
                                      location:
                                        type: string
                                      permanent:
                                        type: boolean
                                    required:
                                      - location
                                      - permanent
                                    additionalProperties: false
                                  - {}
                                nullable: true
                              actionDuration:
                                type: string
                                nullable: true
                              bypassSystem:
                                type: boolean
                                nullable: true
                            required:
                              - action
                            additionalProperties: false
                        additionalProperties: false
                    required:
                      - name
                      - active
                      - conditionGroup
                      - action
                    additionalProperties: false
            required: true
            description: Update a custom rule
            requiredProperties:
              - action
              - id
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - rules.remove
              id:
                allOf:
                  - type: string
              value:
                allOf:
                  - nullable: true
            required: true
            description: Remove a custom rule
            requiredProperties:
              - action
              - id
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - rules.priority
              id:
                allOf:
                  - type: string
              value:
                allOf:
                  - type: number
            required: true
            description: Reorder a custom rule
            requiredProperties:
              - action
              - id
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - crs.update
              id:
                allOf:
                  - type: string
                    enum:
                      - sd
                      - ma
                      - lfi
                      - rfi
                      - rce
                      - php
                      - gen
                      - xss
                      - sqli
                      - sf
                      - java
              value:
                allOf:
                  - type: object
                    properties:
                      active:
                        type: boolean
                      action:
                        type: string
                        enum:
                          - deny
                          - log
                    required:
                      - active
                      - action
                    additionalProperties: false
            required: true
            description: Enable a managed rule
            requiredProperties:
              - action
              - id
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - crs.disable
              id:
                allOf:
                  - nullable: true
              value:
                allOf:
                  - nullable: true
            required: true
            description: Disable a managed rule
            requiredProperties:
              - action
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - ip.insert
              id:
                allOf:
                  - nullable: true
              value:
                allOf:
                  - type: object
                    properties:
                      hostname:
                        type: string
                      ip:
                        type: string
                      notes:
                        type: string
                      action:
                        type: string
                        enum:
                          - deny
                          - challenge
                          - log
                          - bypass
                    required:
                      - hostname
                      - ip
                      - action
                    additionalProperties: false
            required: true
            description: Add an IP Blocking rule
            requiredProperties:
              - action
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - ip.update
              id:
                allOf:
                  - type: string
              value:
                allOf:
                  - type: object
                    properties:
                      hostname:
                        type: string
                      ip:
                        type: string
                      notes:
                        type: string
                      action:
                        type: string
                        enum:
                          - deny
                          - challenge
                          - log
                          - bypass
                    required:
                      - hostname
                      - ip
                      - action
                    additionalProperties: false
            required: true
            description: Update an IP Blocking rule
            requiredProperties:
              - action
              - id
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - ip.remove
              id:
                allOf:
                  - type: string
              value:
                allOf:
                  - nullable: true
            required: true
            description: Remove an IP Blocking rule
            requiredProperties:
              - action
              - id
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
                    enum:
                      - managedRules.update
              id:
                allOf:
                  - type: string
                    enum:
                      - ai_bots
                      - bot_filter
                      - bot_protection
                      - owasp
              value:
                allOf:
                  - type: object
                    properties:
                      action:
                        type: string
                        enum:
                          - log
                          - challenge
                          - deny
                      active:
                        type: boolean
                    required:
                      - active
                    additionalProperties: false
            required: true
            description: Update a managed ruleset
            requiredProperties:
              - action
              - id
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
                    enum:
                      - ai_bots
                      - bot_filter
                      - bot_protection
                      - owasp
              value:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
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
                      additionalProperties: false
            required: true
            description: Update a managed rule group
            requiredProperties:
              - action
              - id
              - value
            additionalProperties: false
          - type: object
            properties:
              action:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
              value:
                allOf:
                  - type: boolean
            required: true
            description: Toggle bot ID
            requiredProperties:
              - action
              - value
            additionalProperties: false
        examples:
          example:
            value:
              action: firewallEnabled
              id: <any>
              value: true
    codeSamples:
      - label: updateFirewallConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Security.UpdateFirewallConfig(ctx, \"<id>\", nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateFirewallConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.security.updateFirewallConfig({
              projectId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                action: "ip.remove",
                id: "<id>",
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
title: "Create a Team"

last_updated: "2025-11-07T00:37:15.900Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/teams/create-a-team"
--------------------------------------------------------------------------------

# Create a Team

> Create a new Team under your account. You need to send a POST request with the desired Team slug, and optionally the Team name.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams
paths:
  path: /v1/teams
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              slug:
                allOf:
                  - example: a-random-team
                    description: The desired slug for the Team
                    type: string
                    maxLength: 48
              name:
                allOf:
                  - example: A Random Team
                    description: >-
                      The desired name for the Team. It will be generated from
                      the provided slug if nothing is provided
                    type: string
                    maxLength: 256
              attribution:
                allOf:
                  - type: object
                    description: Attribution information for the session or current page
                    properties:
                      sessionReferrer:
                        type: string
                        description: Session referrer
                      landingPage:
                        type: string
                        description: Session landing page
                      pageBeforeConversionPage:
                        type: string
                        description: Referrer to the signup page
                      utm:
                        type: object
                        properties:
                          utmSource:
                            type: string
                            description: UTM source
                          utmMedium:
                            type: string
                            description: UTM medium
                          utmCampaign:
                            type: string
                            description: UTM campaign
                          utmTerm:
                            type: string
                            description: UTM term
            required: true
            requiredProperties:
              - slug
            additionalProperties: false
        examples:
          example:
            value:
              slug: a-random-team
              name: A Random Team
              attribution:
                sessionReferrer: <string>
                landingPage: <string>
                pageBeforeConversionPage: <string>
                utm:
                  utmSource: <string>
                  utmMedium: <string>
                  utmCampaign: <string>
                  utmTerm: <string>
    codeSamples:
      - label: createTeam
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.CreateTeam(ctx, &operations.CreateTeamRequestBody{\n        Slug: \"a-random-team\",\n        Name: vercel.String(\"A Random Team\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createTeam
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.createTeam({
              slug: "a-random-team",
              name: "A Random Team",
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
                    description: Id of the created team
                    example: team_nLlpyC6RE1qxqglFKbrMxlud
              slug:
                allOf:
                  - type: string
            description: The team was created successfully
            requiredProperties:
              - id
              - slug
        examples:
          example:
            value:
              id: team_nLlpyC6RE1qxqglFKbrMxlud
              slug: <string>
        description: The team was created successfully
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              The slug is already in use
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          The slug is already in use
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
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Delete a Team"

last_updated: "2025-11-07T00:37:15.930Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/teams/delete-a-team"
--------------------------------------------------------------------------------

# Delete a Team

> Delete a team under your account. You need to send a `DELETE` request with the desired team `id`. An optional array of reasons for deletion may also be sent.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/teams/{teamId}
paths:
  path: /v1/teams/{teamId}
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
        teamId:
          schema:
            - type: string
              required: true
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query:
        newDefaultTeamId:
          schema:
            - type: string
              required: false
              description: Id of the team to be set as the new default team
              example: team_LLHUOMOoDlqOp8wPE4kFo9pE
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
              reasons:
                allOf:
                  - type: array
                    description: >-
                      Optional array of objects that describe the reason why the
                      team is being deleted.
                    items:
                      type: object
                      description: >-
                        An object describing the reason why the team is being
                        deleted.
                      required:
                        - slug
                        - description
                      additionalProperties: false
                      properties:
                        slug:
                          type: string
                          description: >-
                            Idenitifier slug of the reason why the team is being
                            deleted.
                        description:
                          type: string
                          description: >-
                            Description of the reason why the team is being
                            deleted.
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              reasons:
                - slug: <string>
                  description: <string>
    codeSamples:
      - label: deleteTeam
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.DeleteTeam(ctx, \"<id>\", vercel.String(\"team_LLHUOMOoDlqOp8wPE4kFo9pE\"), nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: deleteTeam
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.deleteTeam({
              newDefaultTeamId: "team_LLHUOMOoDlqOp8wPE4kFo9pE",
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
              id:
                allOf:
                  - type: string
                    description: The ID of the deleted Team
                    example: team_LLHUOMOoDlqOp8wPE4kFo9pE
              newDefaultTeamIdError:
                allOf:
                  - type: boolean
                    description: >-
                      Signifies whether the default team update has failed, when
                      newDefaultTeamId is provided in request query.
                    example: true
            description: The Team was successfully deleted
            requiredProperties:
              - id
        examples:
          example:
            value:
              id: team_LLHUOMOoDlqOp8wPE4kFo9pE
              newDefaultTeamIdError: true
        description: The Team was successfully deleted
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
            description: |-
              You do not have permission to access this resource.
              The authenticated user can't access the team
        examples: {}
        description: |-
          You do not have permission to access this resource.
          The authenticated user can't access the team
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Delete a Team invite code"

last_updated: "2025-11-07T00:37:15.913Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/teams/delete-a-team-invite-code"
--------------------------------------------------------------------------------

# Delete a Team invite code

> Delete an active Team invite code.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/teams/{teamId}/invites/{inviteId}
paths:
  path: /v1/teams/{teamId}/invites/{inviteId}
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
        inviteId:
          schema:
            - type: string
              required: true
              description: The Team invite code ID.
              example: 2wn2hudbr4chb1ecywo9dvzo7g9sscs6mzcz8htdde0txyom4l
        teamId:
          schema:
            - type: string
              required: true
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: deleteTeamInviteCode
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Teams.DeleteTeamInviteCode(ctx, \"2wn2hudbr4chb1ecywo9dvzo7g9sscs6mzcz8htdde0txyom4l\", \"team_LLHUOMOoDlqOp8wPE4kFo9pE\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: deleteTeamInviteCode
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.teams.deleteTeamInviteCode({
              inviteId: "2wn2hudbr4chb1ecywo9dvzo7g9sscs6mzcz8htdde0txyom4l",
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
        description: Successfully deleted Team invite code.
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
              Invite managed by directory sync
              Not authorized to access this team.
        examples: {}
        description: |-
          You do not have permission to access this resource.
          Invite managed by directory sync
          Not authorized to access this team.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Team invite code not found.
        examples: {}
        description: Team invite code not found.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get a Team"

last_updated: "2025-11-07T00:37:15.944Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/teams/get-a-team"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./34-update-the-data-cache-feature.md) | [Index](./index.md) | [Next →](./36-get-a-team.md)
