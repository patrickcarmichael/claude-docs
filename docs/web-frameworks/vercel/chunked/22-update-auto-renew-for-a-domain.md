**Navigation:** [← Previous](./21-create-a-dns-record.md) | [Index](./index.md) | [Next →](./23-update-an-existing-drain.md)

---

# Update auto-renew for a domain

> Update the auto-renew setting for a domain

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/registrar/domains/{domain}/auto-renew
paths:
  path: /v1/registrar/domains/{domain}/auto-renew
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
        domain:
          schema:
            - type: string
              required: true
      query:
        teamId:
          schema:
            - type: string
              required: false
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              autoRenew:
                allOf:
                  - type: boolean
            required: true
            requiredProperties:
              - autoRenew
            additionalProperties: false
        examples:
          example:
            value:
              autoRenew: true
    codeSamples:
      - label: updateDomainAutoRenew
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.domainsRegistrar.updateDomainAutoRenew({
              domain: "worthwhile-dwell.net",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                autoRenew: true,
              },
            });


          }

          run();
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Success
        examples: {}
        description: Success
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 400
              code:
                allOf:
                  - type: string
                    enum:
                      - domain_already_renewing
              message:
                allOf:
                  - type: string
            description: The domain is already renewing.
            refIdentifier: '#/components/schemas/DomainAlreadyRenewing'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 400
              code:
                allOf:
                  - type: string
                    enum:
                      - domain_not_renewable
              message:
                allOf:
                  - type: string
            description: The domain is not renewable.
            refIdentifier: '#/components/schemas/DomainNotRenewable'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 400
              code:
                allOf:
                  - type: string
                    enum:
                      - domain_not_registered
              message:
                allOf:
                  - type: string
            description: The domain is not registered with Vercel.
            refIdentifier: '#/components/schemas/DomainNotRegistered'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
          - type: object
            properties:
              issues:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/Issue'
              message:
                allOf:
                  - type: string
            description: The request did not match the expected schema
            refIdentifier: '#/components/schemas/HttpApiDecodeError'
            requiredProperties:
              - issues
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 400
              code: domain_already_renewing
              message: <string>
        description: There was something wrong with the request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 401
              code:
                allOf:
                  - type: string
                    enum:
                      - unauthorized
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Unauthorized'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 401
              code: unauthorized
              message: <string>
        description: Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 403
              code:
                allOf:
                  - type: string
                    enum:
                      - not_authorized_for_scope
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/NotAuthorizedForScope'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 403
              code:
                allOf:
                  - type: string
                    enum:
                      - forbidden
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Forbidden'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 403
              code: not_authorized_for_scope
              message: <string>
        description: NotAuthorizedForScope
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 404
              code:
                allOf:
                  - type: string
                    enum:
                      - domain_not_found
              message:
                allOf:
                  - type: string
            description: The domain was not found in our system.
            refIdentifier: '#/components/schemas/DomainNotFound'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 404
              code: domain_not_found
              message: <string>
        description: The domain was not found in our system.
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 429
              code:
                allOf:
                  - type: string
                    enum:
                      - too_many_requests
              message:
                allOf:
                  - type: string
              retryAfter:
                allOf:
                  - type: object
                    required:
                      - value
                      - str
                    properties:
                      value:
                        type: number
                      str:
                        type: string
                    additionalProperties: false
              limit:
                allOf:
                  - type: object
                    required:
                      - total
                      - remaining
                      - reset
                    properties:
                      total:
                        type: number
                      remaining:
                        type: number
                      reset:
                        type: number
                    additionalProperties: false
            refIdentifier: '#/components/schemas/TooManyRequests'
            requiredProperties:
              - status
              - code
              - message
              - retryAfter
              - limit
            additionalProperties: false
        examples:
          example:
            value:
              status: 429
              code: too_many_requests
              message: <string>
              retryAfter:
                value: 123
                str: <string>
              limit:
                total: 123
                remaining: 123
                reset: 123
        description: TooManyRequests
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 500
              code:
                allOf:
                  - type: string
                    enum:
                      - internal_server_error
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/InternalServerError'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 500
              code: internal_server_error
              message: <string>
        description: InternalServerError
  deprecated: false
  type: path
components:
  schemas:
    Issue:
      type: object
      required:
        - path
        - message
      properties:
        path:
          type: array
          items:
            $ref: '#/components/schemas/PropertyKey'
          description: The path to the property where the issue occurred
        message:
          type: string
          description: A descriptive message explaining the issue
      additionalProperties: false
      description: >-
        Represents an error encountered while parsing a value to match the
        schema
    PropertyKey:
      anyOf:
        - type: string
        - type: number
        - type: object
          required:
            - _tag
            - key
          properties:
            _tag:
              type: string
              enum:
                - symbol
            key:
              type: string
          additionalProperties: false
          description: an object to be decoded into a globally shared symbol

````

--------------------------------------------------------------------------------
title: "Update nameservers for a domain"

last_updated: "2025-11-07T00:37:09.950Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-nameservers-for-a-domain"
--------------------------------------------------------------------------------

# Update nameservers for a domain

> Update the nameservers for a domain. Pass an empty array to use Vercel's default nameservers.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/registrar/domains/{domain}/nameservers
paths:
  path: /v1/registrar/domains/{domain}/nameservers
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
        domain:
          schema:
            - type: string
              required: true
      query:
        teamId:
          schema:
            - type: string
              required: false
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              nameservers:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/Nameserver'
            required: true
            requiredProperties:
              - nameservers
            additionalProperties: false
        examples:
          example:
            value:
              nameservers:
                - <string>
    codeSamples:
      - label: updateDomainNameservers
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.domainsRegistrar.updateDomainNameservers({
              domain: "unique-formula.biz",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                nameservers: [
                  "<value 1>",
                ],
              },
            });


          }

          run();
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Success
        examples: {}
        description: Success
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 400
              code:
                allOf:
                  - type: string
                    enum:
                      - domain_not_registered
              message:
                allOf:
                  - type: string
            description: The domain is not registered with Vercel.
            refIdentifier: '#/components/schemas/DomainNotRegistered'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
          - type: object
            properties:
              issues:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/Issue'
              message:
                allOf:
                  - type: string
            description: The request did not match the expected schema
            refIdentifier: '#/components/schemas/HttpApiDecodeError'
            requiredProperties:
              - issues
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 400
              code: domain_not_registered
              message: <string>
        description: There was something wrong with the request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 401
              code:
                allOf:
                  - type: string
                    enum:
                      - unauthorized
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Unauthorized'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 401
              code: unauthorized
              message: <string>
        description: Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 403
              code:
                allOf:
                  - type: string
                    enum:
                      - not_authorized_for_scope
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/NotAuthorizedForScope'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 403
              code:
                allOf:
                  - type: string
                    enum:
                      - forbidden
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Forbidden'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 403
              code: not_authorized_for_scope
              message: <string>
        description: NotAuthorizedForScope
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 404
              code:
                allOf:
                  - type: string
                    enum:
                      - domain_not_found
              message:
                allOf:
                  - type: string
            description: The domain was not found in our system.
            refIdentifier: '#/components/schemas/DomainNotFound'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 404
              code: domain_not_found
              message: <string>
        description: The domain was not found in our system.
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 429
              code:
                allOf:
                  - type: string
                    enum:
                      - too_many_requests
              message:
                allOf:
                  - type: string
              retryAfter:
                allOf:
                  - type: object
                    required:
                      - value
                      - str
                    properties:
                      value:
                        type: number
                      str:
                        type: string
                    additionalProperties: false
              limit:
                allOf:
                  - type: object
                    required:
                      - total
                      - remaining
                      - reset
                    properties:
                      total:
                        type: number
                      remaining:
                        type: number
                      reset:
                        type: number
                    additionalProperties: false
            refIdentifier: '#/components/schemas/TooManyRequests'
            requiredProperties:
              - status
              - code
              - message
              - retryAfter
              - limit
            additionalProperties: false
        examples:
          example:
            value:
              status: 429
              code: too_many_requests
              message: <string>
              retryAfter:
                value: 123
                str: <string>
              limit:
                total: 123
                remaining: 123
                reset: 123
        description: TooManyRequests
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 500
              code:
                allOf:
                  - type: string
                    enum:
                      - internal_server_error
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/InternalServerError'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 500
              code: internal_server_error
              message: <string>
        description: InternalServerError
  deprecated: false
  type: path
components:
  schemas:
    Issue:
      type: object
      required:
        - path
        - message
      properties:
        path:
          type: array
          items:
            $ref: '#/components/schemas/PropertyKey'
          description: The path to the property where the issue occurred
        message:
          type: string
          description: A descriptive message explaining the issue
      additionalProperties: false
      description: >-
        Represents an error encountered while parsing a value to match the
        schema
    PropertyKey:
      anyOf:
        - type: string
        - type: number
        - type: object
          required:
            - _tag
            - key
          properties:
            _tag:
              type: string
              enum:
                - symbol
            key:
              type: string
          additionalProperties: false
          description: an object to be decoded into a globally shared symbol
    Nameserver:
      type: string

````

--------------------------------------------------------------------------------
title: "Add an existing domain to the Vercel platform"

last_updated: "2025-11-07T00:37:10.060Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains/add-an-existing-domain-to-the-vercel-platform"
--------------------------------------------------------------------------------

# Add an existing domain to the Vercel platform

> This endpoint is used for adding a new apex domain name with Vercel for the authenticating user. Note: This endpoint is no longer used for initiating domain transfers from external registrars to Vercel. For this, please use the endpoint [Transfer-in a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/transfer-in-a-domain).

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v7/domains
paths:
  path: /v7/domains
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
              method:
                allOf:
                  - &ref_0
                    description: >-
                      The domain operation to perform. It can be either `add` or
                      `move-in`.
                    type: string
                    example: add
                  - description: The domain operation to perform.
                    type: string
                    example: add
              name:
                allOf:
                  - description: The domain name you want to add.
                    type: string
                    example: example.com
              cdnEnabled:
                allOf:
                  - description: >-
                      Whether the domain has the Vercel Edge Network enabled or
                      not.
                    type: boolean
                    example: true
              zone:
                allOf:
                  - type: boolean
            description: add
            requiredProperties:
              - name
            additionalProperties: false
          - type: object
            properties:
              method:
                allOf:
                  - *ref_0
                  - description: The domain operation to perform.
                    type: string
                    example: move-in
              name:
                allOf:
                  - description: The domain name you want to add.
                    type: string
                    example: example.com
              token:
                allOf:
                  - description: The move-in token from Move Requested email.
                    type: string
                    example: fdhfr820ad#@FAdlj$$
            description: move-in
            requiredProperties:
              - method
              - name
            additionalProperties: false
          - type: object
            properties:
              method:
                allOf:
                  - *ref_0
                  - description: The domain operation to perform.
                    type: string
                    example: transfer-in
              name:
                allOf:
                  - description: The domain name you want to add.
                    type: string
                    example: example.com
              authCode:
                allOf:
                  - description: The authorization code assigned to the domain.
                    type: string
                    example: fdhfr820ad#@FAdlj$$
              expectedPrice:
                allOf:
                  - description: >-
                      The price you expect to be charged for the required 1 year
                      renewal.
                    type: number
                    example: 8
            description: transfer-in
            deprecated: true
            requiredProperties:
              - method
              - name
            additionalProperties: false
        examples:
          example:
            value:
              name: example.com
              cdnEnabled: true
              zone: true
              method: add
    codeSamples:
      - label: createOrTransferDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.createOrTransferDomain({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "example.com",
                method: "add",
                token: "fdhfr820ad#@FAdlj$$",
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
              domain:
                allOf:
                  - properties:
                      verified:
                        type: boolean
                        description: If the domain has the ownership verified.
                        example: true
                      nameservers:
                        items:
                          type: string
                        type: array
                        description: A list of the current nameservers of the domain.
                        example:
                          - ns1.nameserver.net
                          - ns2.nameserver.net
                      intendedNameservers:
                        items:
                          type: string
                        type: array
                        description: >-
                          A list of the intended nameservers for the domain to
                          point to Vercel DNS.
                        example:
                          - ns1.vercel-dns.com
                          - ns2.vercel-dns.com
                      customNameservers:
                        items:
                          type: string
                        type: array
                        description: >-
                          A list of custom nameservers for the domain to point
                          to. Only applies to domains purchased with Vercel.
                        example:
                          - ns1.nameserver.net
                          - ns2.nameserver.net
                      creator:
                        properties:
                          username:
                            type: string
                          email:
                            type: string
                          customerId:
                            nullable: true
                            type: string
                          isDomainReseller:
                            type: boolean
                          id:
                            type: string
                        required:
                          - username
                          - email
                          - id
                        type: object
                        description: >-
                          An object containing information of the domain
                          creator, including the user's id, username, and email.
                        example:
                          id: ZspSRT4ljIEEmMHgoDwKWDei
                          username: vercel_user
                          email: demo@example.com
                      registrar:
                        type: string
                        enum:
                          - new
                        description: >-
                          Whether or not the domain is registered with Name.com.
                          If set to `true`, the domain is registered with
                          Name.com.
                      name:
                        type: string
                        description: The domain name.
                        example: example.com
                      boughtAt:
                        nullable: true
                        type: number
                        description: >-
                          If it was purchased through Vercel, the timestamp in
                          milliseconds when it was purchased.
                        example: 1613602938882
                      createdAt:
                        type: number
                        description: >-
                          Timestamp in milliseconds when the domain was created
                          in the registry.
                        example: 1613602938882
                      expiresAt:
                        nullable: true
                        type: number
                        description: >-
                          Timestamp in milliseconds at which the domain is set
                          to expire. `null` if not bought with Vercel.
                        example: 1613602938882
                      id:
                        type: string
                        description: The unique identifier of the domain.
                        example: EmTbe5CEJyTk2yVAHBUWy4A3sRusca3GCwRjTC1bpeVnt1
                      orderedAt:
                        type: number
                        description: >-
                          Timestamp in milliseconds at which the domain was
                          ordered.
                        example: 1613602938882
                      renew:
                        type: boolean
                        description: >-
                          Indicates whether the domain is set to automatically
                          renew.
                        example: true
                      serviceType:
                        type: string
                        enum:
                          - zeit.world
                          - external
                          - na
                        description: >-
                          The type of service the domain is handled by.
                          `external` if the DNS is externally handled,
                          `zeit.world` if handled with Vercel, or `na` if the
                          service is not available.
                        example: zeit.world
                      transferredAt:
                        nullable: true
                        type: number
                        description: >-
                          Timestamp in milliseconds at which the domain was
                          successfully transferred into Vercel. `null` if the
                          transfer is still processing or was never transferred
                          in.
                        example: 1613602938882
                      transferStartedAt:
                        type: number
                        description: >-
                          If transferred into Vercel, timestamp in milliseconds
                          when the domain transfer was initiated.
                        example: 1613602938882
                      userId:
                        type: string
                      teamId:
                        nullable: true
                        type: string
                    required:
                      - verified
                      - nameservers
                      - intendedNameservers
                      - creator
                      - name
                      - boughtAt
                      - createdAt
                      - expiresAt
                      - id
                      - serviceType
                      - userId
                      - teamId
                    type: object
            requiredProperties:
              - domain
        examples:
          example:
            value:
              domain:
                verified: true
                nameservers:
                  - ns1.nameserver.net
                  - ns2.nameserver.net
                intendedNameservers:
                  - ns1.vercel-dns.com
                  - ns2.vercel-dns.com
                customNameservers:
                  - ns1.nameserver.net
                  - ns2.nameserver.net
                creator:
                  id: ZspSRT4ljIEEmMHgoDwKWDei
                  username: vercel_user
                  email: demo@example.com
                registrar: new
                name: example.com
                boughtAt: 1613602938882
                createdAt: 1613602938882
                expiresAt: 1613602938882
                id: EmTbe5CEJyTk2yVAHBUWy4A3sRusca3GCwRjTC1bpeVnt1
                orderedAt: 1613602938882
                renew: true
                serviceType: zeit.world
                transferredAt: 1613602938882
                transferStartedAt: 1613602938882
                userId: <string>
                teamId: <string>
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
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The domain is not allowed to be used
        examples: {}
        description: The domain is not allowed to be used
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Check a Domain Availability (deprecated)"

last_updated: "2025-11-07T00:37:09.941Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains/check-a-domain-availability-deprecated"
--------------------------------------------------------------------------------

# Check a Domain Availability (deprecated)

> This endpoint is deprecated and replaced with the endpoint [Get availability for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-availability-for-a-domain). Check if a domain name is available for purchase.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/domains/status
paths:
  path: /v4/domains/status
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
        name:
          schema:
            - type: string
              required: true
              description: >-
                The name of the domain for which we would like to check the
                status.
              example: example.com
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
      - label: checkDomainStatus
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.CheckDomainStatus(ctx, \"example.com\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: checkDomainStatus
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.checkDomainStatus({
              name: "example.com",
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
              available:
                allOf:
                  - type: boolean
            requiredProperties:
              - available
        examples:
          example:
            value:
              available: true
        description: Successful response checking if a Domain's name is available.
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
    '408': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Check the price for a domain (deprecated)"

last_updated: "2025-11-07T00:37:10.062Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains/check-the-price-for-a-domain-deprecated"
--------------------------------------------------------------------------------

# Check the price for a domain (deprecated)

> This endpoint is deprecated and replaced with the endpoint [Get price data for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-price-data-for-a-domain). Check the price to purchase a domain and how long a single purchase period is.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/domains/price
paths:
  path: /v4/domains/price
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
        name:
          schema:
            - type: string
              required: true
              description: The name of the domain for which the price needs to be checked.
              example: example.com
        type:
          schema:
            - type: enum<string>
              enum:
                - new
                - renewal
                - transfer
                - redemption
              required: false
              description: In which status of the domain the price needs to be checked.
              example: new
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
      - label: checkDomainPrice
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.CheckDomainPrice(ctx, \"example.com\", operations.QueryParamTypeNew.ToPointer(), nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: checkDomainPrice
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.checkDomainPrice({
              name: "example.com",
              type: "new",
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
              price:
                allOf:
                  - type: number
                    description: The domain price in USD.
                    example: 20
              period:
                allOf:
                  - type: number
                    description: >-
                      The number of years the domain could be held before paying
                      again.
                    example: 1
            description: >-
              Successful response which returns the price of the domain and the
              period.
            requiredProperties:
              - price
              - period
        examples:
          example:
            value:
              price: 20
              period: 1
        description: >-
          Successful response which returns the price of the domain and the
          period.
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
title: "Get a Domain's configuration"

last_updated: "2025-11-07T00:37:10.187Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains/get-a-domains-configuration"
--------------------------------------------------------------------------------

# Get a Domain's configuration

> Get a Domain's configuration.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v6/domains/{domain}/config
paths:
  path: /v6/domains/{domain}/config
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
        domain:
          schema:
            - type: string
              required: true
              description: The name of the domain.
              example: example.com
      query:
        projectIdOrName:
          schema:
            - type: string
              required: false
              description: >-
                The project id or name that will be associated with the domain.
                Use this when the domain is not yet associated with a project.
        strict:
          schema:
            - type: enum<string>
              enum:
                - 'true'
                - 'false'
              required: false
              description: >-
                When true, the response will only include the nameservers
                assigned directly to the specified domain. When false and there
                are no nameservers assigned directly to the specified domain,
                the response will include the nameservers of the domain's parent
                zone.
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
      - label: getDomainConfig
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.GetDomainConfig(ctx, \"example.com\", nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getDomainConfig
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.getDomainConfig({
              domain: "example.com",
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
              configuredBy:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - CNAME
                      - A
                      - http
                      - dns-01
                    description: >-
                      How we see the domain's configuration. - `CNAME`: Domain
                      has a CNAME pointing to Vercel. - `A`: Domain's A record
                      is resolving to Vercel. - `http`: Domain is resolving to
                      Vercel but may be behind a Proxy. - `dns-01`: Domain is
                      not resolving to Vercel but dns-01 challenge is enabled. -
                      `null`: Domain is not resolving to Vercel.
              acceptedChallenges:
                allOf:
                  - items:
                      type: string
                      enum:
                        - dns-01
                        - http-01
                      description: >-
                        Which challenge types the domain can use for issuing
                        certs.
                    type: array
                    description: >-
                      Which challenge types the domain can use for issuing
                      certs.
              recommendedIPv4:
                allOf:
                  - items:
                      properties:
                        rank:
                          type: number
                        value:
                          items:
                            type: string
                          type: array
                      required:
                        - rank
                        - value
                      type: object
                      description: >-
                        Recommended IPv4s for the domain. rank=1 is the
                        preferred value(s) to use. Only using 1 ip value is
                        acceptable.
                    type: array
                    description: >-
                      Recommended IPv4s for the domain. rank=1 is the preferred
                      value(s) to use. Only using 1 ip value is acceptable.
              recommendedCNAME:
                allOf:
                  - items:
                      properties:
                        rank:
                          type: number
                        value:
                          type: string
                      required:
                        - rank
                        - value
                      type: object
                      description: >-
                        Recommended CNAMEs for the domain. rank=1 is the
                        preferred value to use.
                    type: array
                    description: >-
                      Recommended CNAMEs for the domain. rank=1 is the preferred
                      value to use.
              misconfigured:
                allOf:
                  - type: boolean
                    description: >-
                      Whether or not the domain is configured AND we can
                      automatically generate a TLS certificate.
            requiredProperties:
              - configuredBy
              - acceptedChallenges
              - recommendedIPv4
              - recommendedCNAME
              - misconfigured
        examples:
          example:
            value:
              configuredBy: CNAME
              acceptedChallenges:
                - dns-01
              recommendedIPv4:
                - rank: 123
                  value:
                    - <string>
              recommendedCNAME:
                - rank: 123
                  value: <string>
              misconfigured: true
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
title: "Get domain transfer info (deprecated)"

last_updated: "2025-11-07T00:37:09.944Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains/get-domain-transfer-info-deprecated"
--------------------------------------------------------------------------------

# Get domain transfer info (deprecated)

> This endpoint is deprecated and replaced with the endpoint [Get a domain's transfer status](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-a-domains-transfer-status). Fetch domain transfer availability or transfer status if a transfer is in progress.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/domains/{domain}/registry
paths:
  path: /v1/domains/{domain}/registry
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
        domain:
          schema:
            - type: string
              required: true
              example: example.com
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
      - label: getDomainTransfer
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.GetDomainTransfer(ctx, \"example.com\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getDomainTransfer
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.getDomainTransfer({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              domain: "example.com",
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
              reason:
                allOf:
                  - type: string
              status:
                allOf:
                  - type: string
              transferable:
                allOf:
                  - type: boolean
              transferPolicy:
                allOf:
                  - type: string
                    enum:
                      - charge-and-renew
            requiredProperties:
              - reason
              - status
              - transferable
              - transferPolicy
          - type: object
            properties:
              transferable:
                allOf:
                  - type: boolean
                    description: Whether or not the domain is transferable
              transferPolicy:
                allOf:
                  - nullable: true
                    type: string
                    enum:
                      - charge-and-renew
                      - no-charge-no-change
                      - no-change
                      - new-term
                      - not-supported
                    description: >-
                      The domain's transfer policy (depends on TLD
                      requirements). `charge-and-renew`: transfer will charge
                      for renewal and will renew the existing domain's
                      registration. `no-charge-no-change`: transfer will have no
                      change to registration period and does not require charge.
                      `no-change`: transfer charge is required, but no change in
                      registration period. `new-term`: transfer charge is
                      required and a new registry term is set based on the
                      transfer date. `not-supported`: transfers are not
                      supported for this domain or TLD. `null`: This TLD is not
                      supported by Vercel's Registrar.
              reason:
                allOf:
                  - type: string
                    description: Description associated with transferable state.
              status:
                allOf:
                  - type: string
                    enum:
                      - completed
                      - undef
                      - pending_owner
                      - pending_admin
                      - pending_registry
                      - cancelled
                      - unknown
                    description: >-
                      The current state of an ongoing transfer. `pending_owner`:
                      Awaiting approval by domain's admin contact (every
                      transfer begins with this status). If approval is not
                      given within five days, the transfer is cancelled.
                      `pending_admin`: Waiting for approval by Vercel Registrar
                      admin. `pending_registry`: Awaiting registry approval (the
                      transfer completes after 7 days unless it is declined by
                      the current registrar). `completed`: The transfer
                      completed successfully. `cancelled`: The transfer was
                      cancelled. `undef`: No transfer exists for this domain.
                      `unknown`: This TLD is not supported by Vercel's
                      Registrar.
            requiredProperties:
              - transferable
              - transferPolicy
              - reason
              - status
        examples:
          example:
            value:
              reason: <string>
              status: <string>
              transferable: true
              transferPolicy: charge-and-renew
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get Information for a Single Domain"

last_updated: "2025-11-07T00:37:09.895Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains/get-information-for-a-single-domain"
--------------------------------------------------------------------------------

# Get Information for a Single Domain

> Get information for a single domain in an account or team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v5/domains/{domain}
paths:
  path: /v5/domains/{domain}
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
        domain:
          schema:
            - type: string
              required: true
              description: The name of the domain.
              example: example.com
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
      - label: getDomain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.GetDomain(ctx, \"example.com\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.getDomain({
              domain: "example.com",
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
              domain:
                allOf:
                  - properties:
                      suffix:
                        type: boolean
                      verified:
                        type: boolean
                        description: If the domain has the ownership verified.
                        example: true
                      nameservers:
                        items:
                          type: string
                        type: array
                        description: A list of the current nameservers of the domain.
                        example:
                          - ns1.nameserver.net
                          - ns2.nameserver.net
                      intendedNameservers:
                        items:
                          type: string
                        type: array
                        description: >-
                          A list of the intended nameservers for the domain to
                          point to Vercel DNS.
                        example:
                          - ns1.vercel-dns.com
                          - ns2.vercel-dns.com
                      customNameservers:
                        items:
                          type: string
                        type: array
                        description: >-
                          A list of custom nameservers for the domain to point
                          to. Only applies to domains purchased with Vercel.
                        example:
                          - ns1.nameserver.net
                          - ns2.nameserver.net
                      creator:
                        properties:
                          username:
                            type: string
                          email:
                            type: string
                          customerId:
                            nullable: true
                            type: string
                          isDomainReseller:
                            type: boolean
                          id:
                            type: string
                        required:
                          - username
                          - email
                          - id
                        type: object
                        description: >-
                          An object containing information of the domain
                          creator, including the user's id, username, and email.
                        example:
                          id: ZspSRT4ljIEEmMHgoDwKWDei
                          username: vercel_user
                          email: demo@example.com
                      registrar:
                        type: string
                        enum:
                          - new
                        description: >-
                          Whether or not the domain is registered with Name.com.
                          If set to `true`, the domain is registered with
                          Name.com.
                      teamId:
                        nullable: true
                        type: string
                      boughtAt:
                        nullable: true
                        type: number
                        description: >-
                          If it was purchased through Vercel, the timestamp in
                          milliseconds when it was purchased.
                        example: 1613602938882
                      name:
                        type: string
                        description: The domain name.
                        example: example.com
                      createdAt:
                        type: number
                        description: >-
                          Timestamp in milliseconds when the domain was created
                          in the registry.
                        example: 1613602938882
                      expiresAt:
                        nullable: true
                        type: number
                        description: >-
                          Timestamp in milliseconds at which the domain is set
                          to expire. `null` if not bought with Vercel.
                        example: 1613602938882
                      id:
                        type: string
                        description: The unique identifier of the domain.
                        example: EmTbe5CEJyTk2yVAHBUWy4A3sRusca3GCwRjTC1bpeVnt1
                      orderedAt:
                        type: number
                        description: >-
                          Timestamp in milliseconds at which the domain was
                          ordered.
                        example: 1613602938882
                      renew:
                        type: boolean
                        description: >-
                          Indicates whether the domain is set to automatically
                          renew.
                        example: true
                      serviceType:
                        type: string
                        enum:
                          - zeit.world
                          - external
                          - na
                        description: >-
                          The type of service the domain is handled by.
                          `external` if the DNS is externally handled,
                          `zeit.world` if handled with Vercel, or `na` if the
                          service is not available.
                        example: zeit.world
                      transferredAt:
                        nullable: true
                        type: number
                        description: >-
                          Timestamp in milliseconds at which the domain was
                          successfully transferred into Vercel. `null` if the
                          transfer is still processing or was never transferred
                          in.
                        example: 1613602938882
                      transferStartedAt:
                        type: number
                        description: >-
                          If transferred into Vercel, timestamp in milliseconds
                          when the domain transfer was initiated.
                        example: 1613602938882
                      userId:
                        type: string
                    required:
                      - suffix
                      - verified
                      - nameservers
                      - intendedNameservers
                      - creator
                      - teamId
                      - boughtAt
                      - name
                      - createdAt
                      - expiresAt
                      - id
                      - serviceType
                      - userId
                    type: object
            requiredProperties:
              - domain
        examples:
          example:
            value:
              domain:
                suffix: true
                verified: true
                nameservers:
                  - ns1.nameserver.net
                  - ns2.nameserver.net
                intendedNameservers:
                  - ns1.vercel-dns.com
                  - ns2.vercel-dns.com
                customNameservers:
                  - ns1.nameserver.net
                  - ns2.nameserver.net
                creator:
                  id: ZspSRT4ljIEEmMHgoDwKWDei
                  username: vercel_user
                  email: demo@example.com
                registrar: new
                teamId: <string>
                boughtAt: 1613602938882
                name: example.com
                createdAt: 1613602938882
                expiresAt: 1613602938882
                id: EmTbe5CEJyTk2yVAHBUWy4A3sRusca3GCwRjTC1bpeVnt1
                orderedAt: 1613602938882
                renew: true
                serviceType: zeit.world
                transferredAt: 1613602938882
                transferStartedAt: 1613602938882
                userId: <string>
        description: Successful response retrieving an information for a specific domains.
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
title: "List all the domains"

last_updated: "2025-11-07T00:37:10.060Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains/list-all-the-domains"
--------------------------------------------------------------------------------

# List all the domains

> Retrieves a list of domains registered for the authenticated user or team. By default it returns the last 20 domains if no limit is provided.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v5/domains
paths:
  path: /v5/domains
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
              description: Maximum number of domains to list from a request.
              example: 20
        since:
          schema:
            - type: number
              description: Get domains created after this JavaScript timestamp.
              example: 1609499532000
        until:
          schema:
            - type: number
              description: Get domains created before this JavaScript timestamp.
              example: 1612264332000
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
      - label: getDomains
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.GetDomains(ctx, operations.GetDomainsRequest{\n        Limit: vercel.Float64(20),\n        Since: vercel.Float64(1609499532000),\n        Until: vercel.Float64(1612264332000),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getDomains
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.getDomains({
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
                        verified:
                          type: boolean
                          description: If the domain has the ownership verified.
                          example: true
                        nameservers:
                          items:
                            type: string
                          type: array
                          description: A list of the current nameservers of the domain.
                          example:
                            - ns1.nameserver.net
                            - ns2.nameserver.net
                        intendedNameservers:
                          items:
                            type: string
                          type: array
                          description: >-
                            A list of the intended nameservers for the domain to
                            point to Vercel DNS.
                          example:
                            - ns1.vercel-dns.com
                            - ns2.vercel-dns.com
                        customNameservers:
                          items:
                            type: string
                          type: array
                          description: >-
                            A list of custom nameservers for the domain to point
                            to. Only applies to domains purchased with Vercel.
                          example:
                            - ns1.nameserver.net
                            - ns2.nameserver.net
                        creator:
                          properties:
                            username:
                              type: string
                            email:
                              type: string
                            customerId:
                              nullable: true
                              type: string
                            isDomainReseller:
                              type: boolean
                            id:
                              type: string
                          required:
                            - username
                            - email
                            - id
                          type: object
                          description: >-
                            An object containing information of the domain
                            creator, including the user's id, username, and
                            email.
                          example:
                            id: ZspSRT4ljIEEmMHgoDwKWDei
                            username: vercel_user
                            email: demo@example.com
                        registrar:
                          type: string
                          enum:
                            - new
                          description: >-
                            Whether or not the domain is registered with
                            Name.com. If set to `true`, the domain is registered
                            with Name.com.
                        teamId:
                          nullable: true
                          type: string
                        createdAt:
                          type: number
                          description: >-
                            Timestamp in milliseconds when the domain was
                            created in the registry.
                          example: 1613602938882
                        boughtAt:
                          nullable: true
                          type: number
                          description: >-
                            If it was purchased through Vercel, the timestamp in
                            milliseconds when it was purchased.
                          example: 1613602938882
                        expiresAt:
                          nullable: true
                          type: number
                          description: >-
                            Timestamp in milliseconds at which the domain is set
                            to expire. `null` if not bought with Vercel.
                          example: 1613602938882
                        id:
                          type: string
                          description: The unique identifier of the domain.
                          example: EmTbe5CEJyTk2yVAHBUWy4A3sRusca3GCwRjTC1bpeVnt1
                        name:
                          type: string
                          description: The domain name.
                          example: example.com
                        orderedAt:
                          type: number
                          description: >-
                            Timestamp in milliseconds at which the domain was
                            ordered.
                          example: 1613602938882
                        renew:
                          type: boolean
                          description: >-
                            Indicates whether the domain is set to automatically
                            renew.
                          example: true
                        serviceType:
                          type: string
                          enum:
                            - zeit.world
                            - external
                            - na
                          description: >-
                            The type of service the domain is handled by.
                            `external` if the DNS is externally handled,
                            `zeit.world` if handled with Vercel, or `na` if the
                            service is not available.
                          example: zeit.world
                        transferredAt:
                          nullable: true
                          type: number
                          description: >-
                            Timestamp in milliseconds at which the domain was
                            successfully transferred into Vercel. `null` if the
                            transfer is still processing or was never
                            transferred in.
                          example: 1613602938882
                        transferStartedAt:
                          type: number
                          description: >-
                            If transferred into Vercel, timestamp in
                            milliseconds when the domain transfer was initiated.
                          example: 1613602938882
                        userId:
                          type: string
                      required:
                        - verified
                        - nameservers
                        - intendedNameservers
                        - creator
                        - teamId
                        - createdAt
                        - boughtAt
                        - expiresAt
                        - id
                        - name
                        - serviceType
                        - userId
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
                - verified: true
                  nameservers:
                    - ns1.nameserver.net
                    - ns2.nameserver.net
                  intendedNameservers:
                    - ns1.vercel-dns.com
                    - ns2.vercel-dns.com
                  customNameservers:
                    - ns1.nameserver.net
                    - ns2.nameserver.net
                  creator:
                    id: ZspSRT4ljIEEmMHgoDwKWDei
                    username: vercel_user
                    email: demo@example.com
                  registrar: new
                  teamId: <string>
                  createdAt: 1613602938882
                  boughtAt: 1613602938882
                  expiresAt: 1613602938882
                  id: EmTbe5CEJyTk2yVAHBUWy4A3sRusca3GCwRjTC1bpeVnt1
                  name: example.com
                  orderedAt: 1613602938882
                  renew: true
                  serviceType: zeit.world
                  transferredAt: 1613602938882
                  transferStartedAt: 1613602938882
                  userId: <string>
              pagination:
                count: 20
                next: 1540095775951
                prev: 1540095775951
        description: Successful response retrieving a list of domains.
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
title: "Purchase a domain (deprecated)"

last_updated: "2025-11-07T00:37:10.268Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains/purchase-a-domain-deprecated"
--------------------------------------------------------------------------------

# Purchase a domain (deprecated)

> This endpoint is deprecated and replaced with the endpoint [Buy a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-a-domain). Purchases the specified domain.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v5/domains/buy
paths:
  path: /v5/domains/buy
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
                  - description: The domain name to purchase.
                    type: string
                    example: example.com
              expectedPrice:
                allOf:
                  - description: The price you expect to be charged for the purchase.
                    type: number
                    example: 10
              renew:
                allOf:
                  - description: >-
                      Indicates whether the domain should be automatically
                      renewed.
                    type: boolean
                    example: true
              country:
                allOf:
                  - description: The country of the domain registrant
                    type: string
                    example: US
              orgName:
                allOf:
                  - description: The company name of the domain registrant
                    type: string
                    example: Acme Inc.
              firstName:
                allOf:
                  - description: The first name of the domain registrant
                    type: string
                    example: Jane
              lastName:
                allOf:
                  - description: The last name of the domain registrant
                    type: string
                    example: Doe
              address1:
                allOf:
                  - description: The street address of the domain registrant
                    type: string
                    example: 340 S Lemon Ave Suite 4133
              city:
                allOf:
                  - description: The city of the domain registrant
                    type: string
                    example: San Francisco
              state:
                allOf:
                  - description: The state of the domain registrant
                    type: string
                    example: CA
              postalCode:
                allOf:
                  - description: The postal code of the domain registrant
                    type: string
                    example: '91789'
              phone:
                allOf:
                  - description: The phone number of the domain registrant
                    type: string
                    example: '+1.4158551452'
              email:
                allOf:
                  - description: The email of the domain registrant
                    type: string
                    example: jane.doe@someplace.com
            required: true
            requiredProperties:
              - name
              - country
              - firstName
              - lastName
              - address1
              - city
              - state
              - postalCode
              - phone
              - email
            additionalProperties: false
        examples:
          example:
            value:
              name: example.com
              expectedPrice: 10
              renew: true
              country: US
              orgName: Acme Inc.
              firstName: Jane
              lastName: Doe
              address1: 340 S Lemon Ave Suite 4133
              city: San Francisco
              state: CA
              postalCode: '91789'
              phone: '+1.4158551452'
              email: jane.doe@someplace.com
    codeSamples:
      - label: buyDomain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.BuyDomain(ctx, nil, nil, &operations.BuyDomainRequestBody{\n        Name: \"example.com\",\n        ExpectedPrice: vercel.Float64(10),\n        Renew: vercel.Bool(true),\n        Country: \"US\",\n        OrgName: vercel.String(\"Acme Inc.\"),\n        FirstName: \"Jane\",\n        LastName: \"Doe\",\n        Address1: \"340 S Lemon Ave Suite 4133\",\n        City: \"San Francisco\",\n        State: \"CA\",\n        PostalCode: \"91789\",\n        Phone: \"+1.4158551452\",\n        Email: \"jane.doe@someplace.com\",\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.TwoHundredAndOneApplicationJSONObject != nil {\n        // handle response\n    }\n}"
      - label: buyDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.buyDomain({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "example.com",
                expectedPrice: 10,
                renew: true,
                country: "US",
                orgName: "Acme Inc.",
                firstName: "Jane",
                lastName: "Doe",
                address1: "340 S Lemon Ave Suite 4133",
                city: "San Francisco",
                state: "CA",
                postalCode: "91789",
                phone: "+1.4158551452",
                email: "jane.doe@someplace.com",
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
              domain:
                allOf:
                  - properties:
                      uid:
                        type: string
                      ns:
                        items:
                          type: string
                        type: array
                      verified:
                        type: boolean
                      created:
                        type: number
                      pending:
                        type: boolean
                    required:
                      - uid
                      - ns
                      - verified
                      - created
                      - pending
                    type: object
            requiredProperties:
              - domain
        examples:
          example:
            value:
              domain:
                uid: <string>
                ns:
                  - <string>
                verified: true
                created: 123
                pending: true
        description: ''
    '202':
      application/json:
        schemaArray:
          - type: object
            properties:
              domain:
                allOf:
                  - properties:
                      uid:
                        type: string
                      ns:
                        items:
                          type: string
                        type: array
                      verified:
                        type: boolean
                      created:
                        type: number
                      pending:
                        type: boolean
                    required:
                      - uid
                      - ns
                      - verified
                      - created
                      - pending
                    type: object
            requiredProperties:
              - domain
        examples:
          example:
            value:
              domain:
                uid: <string>
                ns:
                  - <string>
                verified: true
                created: 123
                pending: true
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
    '409': {}
    '429': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Remove a domain by name"

last_updated: "2025-11-07T00:37:10.606Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains/remove-a-domain-by-name"
--------------------------------------------------------------------------------

# Remove a domain by name

> Delete a previously registered domain name from Vercel. Deleting a domain will automatically remove any associated aliases.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v6/domains/{domain}
paths:
  path: /v6/domains/{domain}
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
        domain:
          schema:
            - type: string
              required: true
              description: The name of the domain.
              example: example.com
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
      - label: deleteDomain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.DeleteDomain(ctx, \"example.com\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: deleteDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.deleteDomain({
              domain: "example.com",
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
            requiredProperties:
              - uid
        examples:
          example:
            value:
              uid: <string>
        description: Successful response removing a domain.
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
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update or move apex domain"

last_updated: "2025-11-07T00:37:10.576Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains/update-or-move-apex-domain"
--------------------------------------------------------------------------------

# Update or move apex domain

> Update or move apex domain. Note: This endpoint is no longer used for updating auto-renew or nameservers. For this, please use the endpoints [Update auto-renew for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-auto-renew-for-a-domain) and [Update nameservers for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-nameservers-for-a-domain).

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v3/domains/{domain}
paths:
  path: /v3/domains/{domain}
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
        domain:
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
              op:
                allOf:
                  - example: update
                    type: string
              renew:
                allOf:
                  - description: >-
                      This field is deprecated. Please use PATCH
                      /v1/registrar/domains/{domainName}/auto-renew instead.
                    type: boolean
                    deprecated: true
              customNameservers:
                allOf:
                  - description: >-
                      This field is deprecated. Please use PATCH
                      /v1/registrar/domains/{domainName}/nameservers instead.
                    items:
                      type: string
                    maxItems: 4
                    minItems: 0
                    type: array
                    uniqueItems: true
                    deprecated: true
              zone:
                allOf:
                  - description: >-
                      Specifies whether this is a DNS zone that intends to use
                      Vercel's nameservers.
                    type: boolean
            required: true
            description: update
            additionalProperties: false
          - type: object
            properties:
              op:
                allOf:
                  - example: move-out
                    type: string
              destination:
                allOf:
                  - description: User or team to move domain to
                    type: string
            required: true
            description: move-out
            additionalProperties: false
        examples:
          example:
            value:
              op: update
              renew: true
              customNameservers:
                - <string>
              zone: true
    codeSamples:
      - label: patchDomain
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Domains.PatchDomain(ctx, \"tight-secrecy.info\", nil, nil, vercel.Pointer(operations.CreatePatchDomainRequestBodyPatchDomainRequestBody1(\n        operations.PatchDomainRequestBody1{\n            Op: vercel.String(\"update\"),\n        },\n    )))\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: patchDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domains.patchDomain({
              domain: "flimsy-napkin.com",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                op: "update",
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
              moved:
                allOf:
                  - type: boolean
            requiredProperties:
              - moved
          - type: object
            properties:
              moved:
                allOf:
                  - type: boolean
              token:
                allOf:
                  - type: string
            requiredProperties:
              - moved
              - token
          - type: object
            properties:
              renew:
                allOf:
                  - type: boolean
              customNameservers:
                allOf:
                  - items:
                      type: string
                    type: array
              zone:
                allOf:
                  - type: boolean
        examples:
          example:
            value:
              moved: true
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
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Create a new Drain"

last_updated: "2025-11-07T00:37:10.626Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/drains/create-a-new-drain"
--------------------------------------------------------------------------------

# Create a new Drain

> Create a new Drain with the provided configuration.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/drains
paths:
  path: /v1/drains
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
              projects:
                allOf:
                  - type: string
                    enum:
                      - some
                      - all
              projectIds:
                allOf:
                  - type: array
                    items:
                      type: string
              filter:
                allOf:
                  - oneOf:
                      - type: string
                      - type: object
                        additionalProperties: false
                        required:
                          - version
                          - filter
                        properties:
                          version:
                            type: string
                          filter:
                            oneOf:
                              - type: object
                                additionalProperties: false
                                required:
                                  - type
                                properties:
                                  type:
                                    type: string
                                  project:
                                    type: object
                                    additionalProperties: false
                                    properties:
                                      ids:
                                        type: array
                                        items:
                                          type: string
                                  log:
                                    type: object
                                    additionalProperties: false
                                    properties:
                                      sources:
                                        type: array
                                        items:
                                          type: string
                                  deployment:
                                    type: object
                                    additionalProperties: false
                                    properties:
                                      environments:
                                        type: array
                                        items:
                                          type: string
                              - type: object
                                additionalProperties: false
                                required:
                                  - type
                                  - text
                                properties:
                                  type:
                                    type: string
                                  text:
                                    type: string
              schemas:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      required:
                        - version
                      properties:
                        version:
                          type: string
              delivery:
                allOf:
                  - type: object
                    oneOf:
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        properties:
                          type:
                            type: string
                          endpoint:
                            type: string
                          compression:
                            type: string
                            enum:
                              - gzip
                              - none
                          encoding:
                            type: string
                            enum:
                              - json
                              - ndjson
                          headers:
                            type: object
                            additionalProperties:
                              type: string
                          secret:
                            type: string
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        properties:
                          type:
                            type: string
                          endpoint:
                            oneOf:
                              - type: object
                                additionalProperties: false
                                required:
                                  - traces
                                properties:
                                  traces:
                                    type: string
                          encoding:
                            type: string
                            enum:
                              - proto
                              - json
                          headers:
                            type: object
                            additionalProperties:
                              type: string
                          secret:
                            type: string
                      - type: object
                        additionalProperties: false
                        required:
                          - type
                          - endpoint
                          - secret
                        properties:
                          type:
                            type: string
                          endpoint:
                            type: string
                          secret:
                            type: string
              sampling:
                allOf:
                  - type: array
                    items:
                      type: object
                      additionalProperties: false
                      required:
                        - type
                        - rate
                      properties:
                        type:
                          type: string
                        rate:
                          type: number
                          minimum: 0
                          maximum: 1
                          description: Sampling rate from 0 to 1 (e.g., 0.1 for 10%)
                        env:
                          type: string
                          enum:
                            - production
                            - preview
                          description: Environment to apply sampling to
                        requestPath:
                          type: string
                          description: Request path prefix to apply the sampling rule to
              transforms:
                allOf:
                  - type: array
                    items:
                      type: object
                      required:
                        - id
                      properties:
                        id:
                          type: string
              source:
                allOf:
                  - type: object
                    oneOf:
                      - oneOf:
                          - properties:
                              kind:
                                type: string
                                default: integration
                              externalResourceId:
                                type: string
                            additionalProperties: false
                            required:
                              - externalResourceId
                          - properties:
                              kind:
                                type: string
                                default: integration
                              resourceId:
                                type: string
                            additionalProperties: false
                            required:
                              - resourceId
                          - properties:
                              kind:
                                type: string
                                default: integration
                            additionalProperties: false
                            required:
                              - kind
                      - properties:
                          kind:
                            type: string
                            default: self-served
                        additionalProperties: false
                        required:
                          - kind
            requiredProperties:
              - name
              - projects
              - schemas
            additionalProperties: false
        examples:
          example:
            value:
              name: <string>
              projects: some
              projectIds:
                - <string>
              filter: <string>
              schemas: {}
              delivery:
                type: <string>
                endpoint: <string>
                compression: gzip
                encoding: json
                headers: {}
                secret: <string>
              sampling:
                - type: <string>
                  rate: 0.5
                  env: production
                  requestPath: <string>
              transforms:
                - id: <string>
              source:
                kind: integration
                externalResourceId: <string>
    codeSamples:
      - label: createDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.drains.createDrain({
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
              ownerId:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              createdFrom:
                allOf:
                  - type: string
                    enum:
                      - self-served
                      - integration
              updatedAt:
                allOf:
                  - type: number
              projectIds:
                allOf:
                  - items:
                      type: string
                    type: array
              schemas:
                allOf:
                  - properties:
                      log:
                        type: object
                      trace:
                        type: object
                      analytics:
                        type: object
                      speed_insights:
                        type: object
                    type: object
              delivery:
                allOf:
                  - oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - http
                          endpoint:
                            type: string
                          encoding:
                            type: string
                            enum:
                              - json
                              - ndjson
                          compression:
                            type: string
                            enum:
                              - gzip
                              - none
                          headers:
                            additionalProperties:
                              type: string
                            type: object
                          secret:
                            type: string
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - otlphttp
                          endpoint:
                            properties:
                              traces:
                                type: string
                            required:
                              - traces
                            type: object
                          encoding:
                            type: string
                            enum:
                              - json
                              - proto
                          headers:
                            additionalProperties:
                              type: string
                            type: object
                          secret:
                            type: string
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - syslog
                          endpoint:
                            type: string
                          secret:
                            type: string
                        required:
                          - type
                          - endpoint
                          - secret
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - clickhouse
                          endpoint:
                            type: string
                          table:
                            type: string
                        required:
                          - type
                          - endpoint
                          - table
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - internal
                          target:
                            type: string
                            enum:
                              - vercel-otel-traces-db
                        required:
                          - type
                          - target
                        type: object
              sampling:
                allOf:
                  - items:
                      properties:
                        type:
                          type: string
                          enum:
                            - head_sampling
                        rate:
                          type: number
                        env:
                          type: string
                          enum:
                            - production
                            - preview
                        requestPath:
                          type: string
                      required:
                        - type
                        - rate
                      type: object
                    type: array
              teamId:
                allOf:
                  - nullable: true
                    type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - enabled
                      - disabled
                      - errored
              disabledAt:
                allOf:
                  - type: number
              disabledReason:
                allOf:
                  - type: string
                    enum:
                      - disabled-by-owner
                      - feature-not-available
                      - account-plan-downgrade
                      - disabled-by-admin
              disabledBy:
                allOf:
                  - type: string
              firstErrorTimestamp:
                allOf:
                  - type: number
              configurationId:
                allOf:
                  - type: string
              clientId:
                allOf:
                  - type: string
              source:
                allOf:
                  - oneOf:
                      - properties:
                          kind:
                            type: string
                            enum:
                              - self-served
                        required:
                          - kind
                        type: object
                      - properties:
                          kind:
                            type: string
                            enum:
                              - integration
                          resourceId:
                            type: string
                          externalResourceId:
                            type: string
                          integrationId:
                            type: string
                          integrationConfigurationId:
                            type: string
                        required:
                          - kind
                          - integrationId
                          - integrationConfigurationId
                        type: object
              filter:
                allOf:
                  - type: string
              filterV2:
                allOf:
                  - oneOf:
                      - properties:
                          version:
                            type: string
                            enum:
                              - v1
                        required:
                          - version
                        type: object
                      - properties:
                          version:
                            type: string
                            enum:
                              - v2
                          filter:
                            oneOf:
                              - properties:
                                  type:
                                    type: string
                                    enum:
                                      - basic
                                  project:
                                    properties:
                                      ids:
                                        items:
                                          type: string
                                        type: array
                                    type: object
                                  log:
                                    properties:
                                      sources:
                                        items:
                                          type: string
                                        type: array
                                    type: object
                                  deployment:
                                    properties:
                                      environments:
                                        items:
                                          type: string
                                        type: array
                                    type: object
                                required:
                                  - type
                                type: object
                              - properties:
                                  type:
                                    type: string
                                    enum:
                                      - odata
                                  text:
                                    type: string
                                required:
                                  - type
                                  - text
                                type: object
                        required:
                          - version
                          - filter
                        type: object
            requiredProperties:
              - id
              - ownerId
              - name
              - createdAt
              - updatedAt
              - source
          - type: object
            properties:
              id:
                allOf:
                  - type: string
              ownerId:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              createdFrom:
                allOf:
                  - type: string
                    enum:
                      - self-served
                      - integration
              updatedAt:
                allOf:
                  - type: number
              projectIds:
                allOf:
                  - items:
                      type: string
                    type: array
              schemas:
                allOf:
                  - properties:
                      log:
                        type: object
                      trace:
                        type: object
                      analytics:
                        type: object
                      speed_insights:
                        type: object
                    type: object
              delivery:
                allOf:
                  - oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - http
                          endpoint:
                            type: string
                          encoding:
                            type: string
                            enum:
                              - json
                              - ndjson
                          compression:
                            type: string
                            enum:
                              - gzip
                              - none
                          headers:
                            additionalProperties:
                              type: string
                            type: object
                          secret:
                            type: string
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - otlphttp
                          endpoint:
                            properties:
                              traces:
                                type: string
                            required:
                              - traces
                            type: object
                          encoding:
                            type: string
                            enum:
                              - json
                              - proto
                          headers:
                            additionalProperties:
                              type: string
                            type: object
                          secret:
                            type: string
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - syslog
                          endpoint:
                            type: string
                          secret:
                            type: string
                        required:
                          - type
                          - endpoint
                          - secret
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - clickhouse
                          endpoint:
                            type: string
                          table:
                            type: string
                        required:
                          - type
                          - endpoint
                          - table
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - internal
                          target:
                            type: string
                            enum:
                              - vercel-otel-traces-db
                        required:
                          - type
                          - target
                        type: object
              sampling:
                allOf:
                  - items:
                      properties:
                        type:
                          type: string
                          enum:
                            - head_sampling
                        rate:
                          type: number
                        env:
                          type: string
                          enum:
                            - production
                            - preview
                        requestPath:
                          type: string
                      required:
                        - type
                        - rate
                      type: object
                    type: array
              teamId:
                allOf:
                  - nullable: true
                    type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - enabled
                      - disabled
                      - errored
              disabledAt:
                allOf:
                  - type: number
              disabledReason:
                allOf:
                  - type: string
                    enum:
                      - disabled-by-owner
                      - feature-not-available
                      - account-plan-downgrade
                      - disabled-by-admin
              disabledBy:
                allOf:
                  - type: string
              firstErrorTimestamp:
                allOf:
                  - type: number
              configurationId:
                allOf:
                  - type: string
              clientId:
                allOf:
                  - type: string
              source:
                allOf:
                  - oneOf:
                      - properties:
                          kind:
                            type: string
                            enum:
                              - self-served
                        required:
                          - kind
                        type: object
                      - properties:
                          kind:
                            type: string
                            enum:
                              - integration
                          resourceId:
                            type: string
                          externalResourceId:
                            type: string
                          integrationId:
                            type: string
                          integrationConfigurationId:
                            type: string
                        required:
                          - kind
                          - integrationId
                          - integrationConfigurationId
                        type: object
              filter:
                allOf:
                  - type: string
              filterV2:
                allOf:
                  - oneOf:
                      - properties:
                          version:
                            type: string
                            enum:
                              - v1
                        required:
                          - version
                        type: object
                      - properties:
                          version:
                            type: string
                            enum:
                              - v2
                          filter:
                            oneOf:
                              - properties:
                                  type:
                                    type: string
                                    enum:
                                      - basic
                                  project:
                                    properties:
                                      ids:
                                        items:
                                          type: string
                                        type: array
                                    type: object
                                  log:
                                    properties:
                                      sources:
                                        items:
                                          type: string
                                        type: array
                                    type: object
                                  deployment:
                                    properties:
                                      environments:
                                        items:
                                          type: string
                                        type: array
                                    type: object
                                required:
                                  - type
                                type: object
                              - properties:
                                  type:
                                    type: string
                                    enum:
                                      - odata
                                  text:
                                    type: string
                                required:
                                  - type
                                  - text
                                type: object
                        required:
                          - version
                          - filter
                        type: object
              integrationIcon:
                allOf:
                  - type: string
              integrationConfigurationUri:
                allOf:
                  - type: string
              integrationWebsite:
                allOf:
                  - type: string
              projectsMetadata:
                allOf:
                  - items:
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
            requiredProperties:
              - id
              - ownerId
              - name
              - createdAt
              - updatedAt
              - source
        examples:
          example:
            value:
              id: <string>
              ownerId: <string>
              name: <string>
              createdAt: 123
              createdFrom: self-served
              updatedAt: 123
              projectIds:
                - <string>
              schemas:
                log: {}
                trace: {}
                analytics: {}
                speed_insights: {}
              delivery:
                type: http
                endpoint: <string>
                encoding: json
                compression: gzip
                headers: {}
                secret: <string>
              sampling:
                - type: head_sampling
                  rate: 123
                  env: production
                  requestPath: <string>
              teamId: <string>
              status: enabled
              disabledAt: 123
              disabledReason: disabled-by-owner
              disabledBy: <string>
              firstErrorTimestamp: 123
              configurationId: <string>
              clientId: <string>
              source:
                kind: self-served
              filter: <string>
              filterV2:
                version: v1
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
title: "Delete a drain"

last_updated: "2025-11-07T00:37:10.791Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/drains/delete-a-drain"
--------------------------------------------------------------------------------

# Delete a drain

> Delete a specific Drain by passing the drain id in the URL.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/drains/{id}
paths:
  path: /v1/drains/{id}
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
      - label: deleteDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.drains.deleteDrain({
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
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Find a Drain by id"

last_updated: "2025-11-07T00:37:10.792Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/drains/find-a-drain-by-id"
--------------------------------------------------------------------------------

# Find a Drain by id

> Get the information for a specific Drain by passing the drain id in the URL.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/drains/{id}
paths:
  path: /v1/drains/{id}
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
      - label: getDrain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.drains.getDrain({
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
              ownerId:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              createdFrom:
                allOf:
                  - type: string
                    enum:
                      - self-served
                      - integration
              updatedAt:
                allOf:
                  - type: number
              projectIds:
                allOf:
                  - items:
                      type: string
                    type: array
              schemas:
                allOf:
                  - properties:
                      log:
                        type: object
                      trace:
                        type: object
                      analytics:
                        type: object
                      speed_insights:
                        type: object
                    type: object
              delivery:
                allOf:
                  - oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - http
                          endpoint:
                            type: string
                          encoding:
                            type: string
                            enum:
                              - json
                              - ndjson
                          compression:
                            type: string
                            enum:
                              - gzip
                              - none
                          headers:
                            additionalProperties:
                              type: string
                            type: object
                          secret:
                            type: string
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - otlphttp
                          endpoint:
                            properties:
                              traces:
                                type: string
                            required:
                              - traces
                            type: object
                          encoding:
                            type: string
                            enum:
                              - json
                              - proto
                          headers:
                            additionalProperties:
                              type: string
                            type: object
                          secret:
                            type: string
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - syslog
                          endpoint:
                            type: string
                          secret:
                            type: string
                        required:
                          - type
                          - endpoint
                          - secret
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - clickhouse
                          endpoint:
                            type: string
                          table:
                            type: string
                        required:
                          - type
                          - endpoint
                          - table
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - internal
                          target:
                            type: string
                            enum:
                              - vercel-otel-traces-db
                        required:
                          - type
                          - target
                        type: object
              sampling:
                allOf:
                  - items:
                      properties:
                        type:
                          type: string
                          enum:
                            - head_sampling
                        rate:
                          type: number
                        env:
                          type: string
                          enum:
                            - production
                            - preview
                        requestPath:
                          type: string
                      required:
                        - type
                        - rate
                      type: object
                    type: array
              teamId:
                allOf:
                  - nullable: true
                    type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - enabled
                      - disabled
                      - errored
              disabledAt:
                allOf:
                  - type: number
              disabledReason:
                allOf:
                  - type: string
                    enum:
                      - disabled-by-owner
                      - feature-not-available
                      - account-plan-downgrade
                      - disabled-by-admin
              disabledBy:
                allOf:
                  - type: string
              firstErrorTimestamp:
                allOf:
                  - type: number
              configurationId:
                allOf:
                  - type: string
              clientId:
                allOf:
                  - type: string
              source:
                allOf:
                  - oneOf:
                      - properties:
                          kind:
                            type: string
                            enum:
                              - self-served
                        required:
                          - kind
                        type: object
                      - properties:
                          kind:
                            type: string
                            enum:
                              - integration
                          resourceId:
                            type: string
                          externalResourceId:
                            type: string
                          integrationId:
                            type: string
                          integrationConfigurationId:
                            type: string
                        required:
                          - kind
                          - integrationId
                          - integrationConfigurationId
                        type: object
              filter:
                allOf:
                  - type: string
              filterV2:
                allOf:
                  - oneOf:
                      - properties:
                          version:
                            type: string
                            enum:
                              - v1
                        required:
                          - version
                        type: object
                      - properties:
                          version:
                            type: string
                            enum:
                              - v2
                          filter:
                            oneOf:
                              - properties:
                                  type:
                                    type: string
                                    enum:
                                      - basic
                                  project:
                                    properties:
                                      ids:
                                        items:
                                          type: string
                                        type: array
                                    type: object
                                  log:
                                    properties:
                                      sources:
                                        items:
                                          type: string
                                        type: array
                                    type: object
                                  deployment:
                                    properties:
                                      environments:
                                        items:
                                          type: string
                                        type: array
                                    type: object
                                required:
                                  - type
                                type: object
                              - properties:
                                  type:
                                    type: string
                                    enum:
                                      - odata
                                  text:
                                    type: string
                                required:
                                  - type
                                  - text
                                type: object
                        required:
                          - version
                          - filter
                        type: object
            requiredProperties:
              - id
              - ownerId
              - name
              - createdAt
              - updatedAt
              - source
          - type: object
            properties:
              id:
                allOf:
                  - type: string
              ownerId:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: number
              createdFrom:
                allOf:
                  - type: string
                    enum:
                      - self-served
                      - integration
              updatedAt:
                allOf:
                  - type: number
              projectIds:
                allOf:
                  - items:
                      type: string
                    type: array
              schemas:
                allOf:
                  - properties:
                      log:
                        type: object
                      trace:
                        type: object
                      analytics:
                        type: object
                      speed_insights:
                        type: object
                    type: object
              delivery:
                allOf:
                  - oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - http
                          endpoint:
                            type: string
                          encoding:
                            type: string
                            enum:
                              - json
                              - ndjson
                          compression:
                            type: string
                            enum:
                              - gzip
                              - none
                          headers:
                            additionalProperties:
                              type: string
                            type: object
                          secret:
                            type: string
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - otlphttp
                          endpoint:
                            properties:
                              traces:
                                type: string
                            required:
                              - traces
                            type: object
                          encoding:
                            type: string
                            enum:
                              - json
                              - proto
                          headers:
                            additionalProperties:
                              type: string
                            type: object
                          secret:
                            type: string
                        required:
                          - type
                          - endpoint
                          - encoding
                          - headers
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - syslog
                          endpoint:
                            type: string
                          secret:
                            type: string
                        required:
                          - type
                          - endpoint
                          - secret
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - clickhouse
                          endpoint:
                            type: string
                          table:
                            type: string
                        required:
                          - type
                          - endpoint
                          - table
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - internal
                          target:
                            type: string
                            enum:
                              - vercel-otel-traces-db
                        required:
                          - type
                          - target
                        type: object
              sampling:
                allOf:
                  - items:
                      properties:
                        type:
                          type: string
                          enum:
                            - head_sampling
                        rate:
                          type: number
                        env:
                          type: string
                          enum:
                            - production
                            - preview
                        requestPath:
                          type: string
                      required:
                        - type
                        - rate
                      type: object
                    type: array
              teamId:
                allOf:
                  - nullable: true
                    type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - enabled
                      - disabled
                      - errored
              disabledAt:
                allOf:
                  - type: number
              disabledReason:
                allOf:
                  - type: string
                    enum:
                      - disabled-by-owner
                      - feature-not-available
                      - account-plan-downgrade
                      - disabled-by-admin
              disabledBy:
                allOf:
                  - type: string
              firstErrorTimestamp:
                allOf:
                  - type: number
              configurationId:
                allOf:
                  - type: string
              clientId:
                allOf:
                  - type: string
              source:
                allOf:
                  - oneOf:
                      - properties:
                          kind:
                            type: string
                            enum:
                              - self-served
                        required:
                          - kind
                        type: object
                      - properties:
                          kind:
                            type: string
                            enum:
                              - integration
                          resourceId:
                            type: string
                          externalResourceId:
                            type: string
                          integrationId:
                            type: string
                          integrationConfigurationId:
                            type: string
                        required:
                          - kind
                          - integrationId
                          - integrationConfigurationId
                        type: object
              filter:
                allOf:
                  - type: string
              filterV2:
                allOf:
                  - oneOf:
                      - properties:
                          version:
                            type: string
                            enum:
                              - v1
                        required:
                          - version
                        type: object
                      - properties:
                          version:
                            type: string
                            enum:
                              - v2
                          filter:
                            oneOf:
                              - properties:
                                  type:
                                    type: string
                                    enum:
                                      - basic
                                  project:
                                    properties:
                                      ids:
                                        items:
                                          type: string
                                        type: array
                                    type: object
                                  log:
                                    properties:
                                      sources:
                                        items:
                                          type: string
                                        type: array
                                    type: object
                                  deployment:
                                    properties:
                                      environments:
                                        items:
                                          type: string
                                        type: array
                                    type: object
                                required:
                                  - type
                                type: object
                              - properties:
                                  type:
                                    type: string
                                    enum:
                                      - odata
                                  text:
                                    type: string
                                required:
                                  - type
                                  - text
                                type: object
                        required:
                          - version
                          - filter
                        type: object
              integrationIcon:
                allOf:
                  - type: string
              integrationConfigurationUri:
                allOf:
                  - type: string
              integrationWebsite:
                allOf:
                  - type: string
              projectsMetadata:
                allOf:
                  - items:
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
            requiredProperties:
              - id
              - ownerId
              - name
              - createdAt
              - updatedAt
              - source
        examples:
          example:
            value:
              id: <string>
              ownerId: <string>
              name: <string>
              createdAt: 123
              createdFrom: self-served
              updatedAt: 123
              projectIds:
                - <string>
              schemas:
                log: {}
                trace: {}
                analytics: {}
                speed_insights: {}
              delivery:
                type: http
                endpoint: <string>
                encoding: json
                compression: gzip
                headers: {}
                secret: <string>
              sampling:
                - type: head_sampling
                  rate: 123
                  env: production
                  requestPath: <string>
              teamId: <string>
              status: enabled
              disabledAt: 123
              disabledReason: disabled-by-owner
              disabledBy: <string>
              firstErrorTimestamp: 123
              configurationId: <string>
              clientId: <string>
              source:
                kind: self-served
              filter: <string>
              filterV2:
                version: v1
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
title: "Retrieve a list of all Drains"

last_updated: "2025-11-07T00:37:10.881Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/drains/retrieve-a-list-of-all-drains"
--------------------------------------------------------------------------------

# Retrieve a list of all Drains

> Allows to retrieve the list of Drains of the authenticated team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/drains
paths:
  path: /v1/drains
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
        includeMetadata:
          schema:
            - type: boolean
              default: false
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
      - label: getDrains
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.drains.getDrains({
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
              drains:
                allOf:
                  - oneOf:
                      - items:
                          properties:
                            id:
                              type: string
                            ownerId:
                              type: string
                            name:
                              type: string
                            createdAt:
                              type: number
                            createdFrom:
                              type: string
                              enum:
                                - self-served
                                - integration
                            updatedAt:
                              type: number
                            projectIds:
                              items:
                                type: string
                              type: array
                            schemas:
                              properties:
                                log:
                                  type: object
                                trace:
                                  type: object
                                analytics:
                                  type: object
                                speed_insights:
                                  type: object
                              type: object
                            delivery:
                              oneOf:
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - http
                                    endpoint:
                                      type: string
                                    encoding:
                                      type: string
                                      enum:
                                        - json
                                        - ndjson
                                    compression:
                                      type: string
                                      enum:
                                        - gzip
                                        - none
                                    headers:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - encoding
                                    - headers
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - otlphttp
                                    endpoint:
                                      properties:
                                        traces:
                                          type: string
                                      required:
                                        - traces
                                      type: object
                                    encoding:
                                      type: string
                                      enum:
                                        - json
                                        - proto
                                    headers:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - encoding
                                    - headers
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - syslog
                                    endpoint:
                                      type: string
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - secret
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - clickhouse
                                    endpoint:
                                      type: string
                                    table:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - table
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - internal
                                    target:
                                      type: string
                                      enum:
                                        - vercel-otel-traces-db
                                  required:
                                    - type
                                    - target
                                  type: object
                            sampling:
                              items:
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - head_sampling
                                  rate:
                                    type: number
                                  env:
                                    type: string
                                    enum:
                                      - production
                                      - preview
                                  requestPath:
                                    type: string
                                required:
                                  - type
                                  - rate
                                type: object
                              type: array
                            teamId:
                              nullable: true
                              type: string
                            status:
                              type: string
                              enum:
                                - enabled
                                - disabled
                                - errored
                            disabledAt:
                              type: number
                            disabledReason:
                              type: string
                              enum:
                                - disabled-by-owner
                                - feature-not-available
                                - account-plan-downgrade
                                - disabled-by-admin
                            disabledBy:
                              type: string
                            firstErrorTimestamp:
                              type: number
                            configurationId:
                              type: string
                            clientId:
                              type: string
                            source:
                              oneOf:
                                - properties:
                                    kind:
                                      type: string
                                      enum:
                                        - self-served
                                  required:
                                    - kind
                                  type: object
                                - properties:
                                    kind:
                                      type: string
                                      enum:
                                        - integration
                                    resourceId:
                                      type: string
                                    externalResourceId:
                                      type: string
                                    integrationId:
                                      type: string
                                    integrationConfigurationId:
                                      type: string
                                  required:
                                    - kind
                                    - integrationId
                                    - integrationConfigurationId
                                  type: object
                            filter:
                              type: string
                            filterV2:
                              oneOf:
                                - properties:
                                    version:
                                      type: string
                                      enum:
                                        - v1
                                  required:
                                    - version
                                  type: object
                                - properties:
                                    version:
                                      type: string
                                      enum:
                                        - v2
                                    filter:
                                      oneOf:
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - basic
                                            project:
                                              properties:
                                                ids:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            log:
                                              properties:
                                                sources:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            deployment:
                                              properties:
                                                environments:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                          required:
                                            - type
                                          type: object
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - odata
                                            text:
                                              type: string
                                          required:
                                            - type
                                            - text
                                          type: object
                                  required:
                                    - version
                                    - filter
                                  type: object
                          required:
                            - id
                            - ownerId
                            - name
                            - createdAt
                            - updatedAt
                            - source
                          type: object
                        type: array
                      - items:
                          properties:
                            id:
                              type: string
                            ownerId:
                              type: string
                            name:
                              type: string
                            createdAt:
                              type: number
                            createdFrom:
                              type: string
                              enum:
                                - self-served
                                - integration
                            updatedAt:
                              type: number
                            projectIds:
                              items:
                                type: string
                              type: array
                            schemas:
                              properties:
                                log:
                                  type: object
                                trace:
                                  type: object
                                analytics:
                                  type: object
                                speed_insights:
                                  type: object
                              type: object
                            delivery:
                              oneOf:
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - http
                                    endpoint:
                                      type: string
                                    encoding:
                                      type: string
                                      enum:
                                        - json
                                        - ndjson
                                    compression:
                                      type: string
                                      enum:
                                        - gzip
                                        - none
                                    headers:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - encoding
                                    - headers
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - otlphttp
                                    endpoint:
                                      properties:
                                        traces:
                                          type: string
                                      required:
                                        - traces
                                      type: object
                                    encoding:
                                      type: string
                                      enum:
                                        - json
                                        - proto
                                    headers:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - encoding
                                    - headers
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - syslog
                                    endpoint:
                                      type: string
                                    secret:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - secret
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - clickhouse
                                    endpoint:
                                      type: string
                                    table:
                                      type: string
                                  required:
                                    - type
                                    - endpoint
                                    - table
                                  type: object
                                - properties:
                                    type:
                                      type: string
                                      enum:
                                        - internal
                                    target:
                                      type: string
                                      enum:
                                        - vercel-otel-traces-db
                                  required:
                                    - type
                                    - target
                                  type: object
                            sampling:
                              items:
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - head_sampling
                                  rate:
                                    type: number
                                  env:
                                    type: string
                                    enum:
                                      - production
                                      - preview
                                  requestPath:
                                    type: string
                                required:
                                  - type
                                  - rate
                                type: object
                              type: array
                            teamId:
                              nullable: true
                              type: string
                            status:
                              type: string
                              enum:
                                - enabled
                                - disabled
                                - errored
                            disabledAt:
                              type: number
                            disabledReason:
                              type: string
                              enum:
                                - disabled-by-owner
                                - feature-not-available
                                - account-plan-downgrade
                                - disabled-by-admin
                            disabledBy:
                              type: string
                            firstErrorTimestamp:
                              type: number
                            configurationId:
                              type: string
                            clientId:
                              type: string
                            source:
                              oneOf:
                                - properties:
                                    kind:
                                      type: string
                                      enum:
                                        - self-served
                                  required:
                                    - kind
                                  type: object
                                - properties:
                                    kind:
                                      type: string
                                      enum:
                                        - integration
                                    resourceId:
                                      type: string
                                    externalResourceId:
                                      type: string
                                    integrationId:
                                      type: string
                                    integrationConfigurationId:
                                      type: string
                                  required:
                                    - kind
                                    - integrationId
                                    - integrationConfigurationId
                                  type: object
                            filter:
                              type: string
                            filterV2:
                              oneOf:
                                - properties:
                                    version:
                                      type: string
                                      enum:
                                        - v1
                                  required:
                                    - version
                                  type: object
                                - properties:
                                    version:
                                      type: string
                                      enum:
                                        - v2
                                    filter:
                                      oneOf:
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - basic
                                            project:
                                              properties:
                                                ids:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            log:
                                              properties:
                                                sources:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            deployment:
                                              properties:
                                                environments:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                          required:
                                            - type
                                          type: object
                                        - properties:
                                            type:
                                              type: string
                                              enum:
                                                - odata
                                            text:
                                              type: string
                                          required:
                                            - type
                                            - text
                                          type: object
                                  required:
                                    - version
                                    - filter
                                  type: object
                            integrationIcon:
                              type: string
                            integrationConfigurationUri:
                              type: string
                            integrationWebsite:
                              type: string
                            projectsMetadata:
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
                          required:
                            - id
                            - ownerId
                            - name
                            - createdAt
                            - updatedAt
                            - source
                          type: object
                        type: array
            requiredProperties:
              - drains
        examples:
          example:
            value:
              drains:
                - id: <string>
                  ownerId: <string>
                  name: <string>
                  createdAt: 123
                  createdFrom: self-served
                  updatedAt: 123
                  projectIds:
                    - <string>
                  schemas:
                    log: {}
                    trace: {}
                    analytics: {}
                    speed_insights: {}
                  delivery:
                    type: http
                    endpoint: <string>
                    encoding: json
                    compression: gzip
                    headers: {}
                    secret: <string>
                  sampling:
                    - type: head_sampling
                      rate: 123
                      env: production
                      requestPath: <string>
                  teamId: <string>
                  status: enabled
                  disabledAt: 123
                  disabledReason: disabled-by-owner
                  disabledBy: <string>
                  firstErrorTimestamp: 123
                  configurationId: <string>
                  clientId: <string>
                  source:
                    kind: self-served
                  filter: <string>
                  filterV2:
                    version: v1
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
title: "Update an existing Drain"

last_updated: "2025-11-07T00:37:10.641Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/drains/update-an-existing-drain"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./21-create-a-dns-record.md) | [Index](./index.md) | [Next →](./23-update-an-existing-drain.md)
