**Navigation:** [← Previous](./20-delete-a-deployment.md) | [Index](./index.md) | [Next →](./22-update-auto-renew-for-a-domain.md)

---

# Create a DNS record

> Creates a DNS record for a domain.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/domains/{domain}/records
paths:
  path: /v2/domains/{domain}/records
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
        domain:
          schema:
            - type: string
              required: true
              description: The domain used to create the DNS record.
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              type:
                allOf:
                  - &ref_0
                    description: >-
                      The type of record, it could be one of the valid DNS
                      records.
                    type: string
                    enum:
                      - A
                      - AAAA
                      - ALIAS
                      - CAA
                      - CNAME
                      - HTTPS
                      - MX
                      - SRV
                      - TXT
                      - NS
                  - description: Must be of type `A`.
                    type: string
                    enum:
                      - A
              name:
                allOf:
                  - description: A subdomain name or an empty string for the root domain.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: The record value must be a valid IPv4 address.
                    type: string
                    format: ipv4
                    example: 192.0.2.42
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - value
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `AAAA`.
                    type: string
                    enum:
                      - AAAA
              name:
                allOf:
                  - description: A subdomain name or an empty string for the root domain.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: An AAAA record pointing to an IPv6 address.
                    type: string
                    format: ipv6
                    example: 2001:DB8::42
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - value
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `ALIAS`.
                    type: string
                    enum:
                      - ALIAS
              name:
                allOf:
                  - description: A subdomain name or an empty string for the root domain.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: >-
                      An ALIAS virtual record pointing to a hostname resolved to
                      an A record on server side.
                    type: string
                    example: cname.vercel-dns.com
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - value
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `CAA`.
                    type: string
                    enum:
                      - CAA
              name:
                allOf:
                  - description: A subdomain name or an empty string for the root domain.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: >-
                      A CAA record to specify which Certificate Authorities
                      (CAs) are allowed to issue certificates for the domain.
                    type: string
                    example: 0 issue \"letsencrypt.org\"
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - value
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `CNAME`.
                    type: string
                    enum:
                      - CNAME
              name:
                allOf:
                  - description: A subdomain name or an empty string for the root domain.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: A CNAME record mapping to another domain name.
                    type: string
                    example: cname.vercel-dns.com
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `MX`.
                    type: string
                    enum:
                      - MX
              name:
                allOf:
                  - description: A subdomain name or an empty string for the root domain.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: >-
                      An MX record specifying the mail server responsible for
                      accepting messages on behalf of the domain name.
                    type: string
                    example: 10 mail.example.com.
              mxPriority:
                allOf:
                  - type: number
                    minimum: 0
                    maximum: 65535
                    example: 10
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - value
              - name
              - mxPriority
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `SRV`.
                    type: string
                    enum:
                      - SRV
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              srv:
                allOf:
                  - type: object
                    additionalProperties: false
                    required:
                      - weight
                      - port
                      - priority
                      - target
                    properties:
                      priority:
                        anyOf:
                          - type: number
                            minimum: 0
                            maximum: 65535
                            example: 10
                        nullable: true
                      weight:
                        anyOf:
                          - type: number
                            minimum: 0
                            maximum: 65535
                            example: 10
                        nullable: true
                      port:
                        anyOf:
                          - type: number
                            minimum: 0
                            maximum: 65535
                            example: 5000
                        nullable: true
                      target:
                        type: string
                        example: host.example.com
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - name
              - srv
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `TXT`.
                    type: string
                    enum:
                      - TXT
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: A TXT record containing arbitrary text.
                    type: string
                    example: hello
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - value
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `NS`.
                    type: string
                    enum:
                      - NS
              name:
                allOf:
                  - description: A subdomain name.
                    type: string
                    example: subdomain
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              value:
                allOf:
                  - description: An NS domain value.
                    type: string
                    example: ns1.example.com
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - name
            additionalProperties: false
          - type: object
            properties:
              type:
                allOf:
                  - *ref_0
                  - description: Must be of type `HTTPS`.
                    type: string
                    enum:
                      - HTTPS
              ttl:
                allOf:
                  - description: >-
                      The TTL value. Must be a number between 60 and 2147483647.
                      Default value is 60.
                    type: number
                    minimum: 60
                    maximum: 2147483647
                    example: 60
              https:
                allOf:
                  - type: object
                    additionalProperties: false
                    required:
                      - priority
                      - target
                    properties:
                      priority:
                        anyOf:
                          - type: number
                            minimum: 0
                            maximum: 65535
                            example: 10
                        nullable: true
                      target:
                        type: string
                        example: host.example.com
                      params:
                        type: string
                        example: alpn=h2,h3
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            requiredProperties:
              - type
              - name
              - https
            additionalProperties: false
        examples:
          example:
            value:
              name: subdomain
              type: A
              ttl: 60
              value: 192.0.2.42
              comment: used to verify ownership of domain
    codeSamples:
      - label: createRecord
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.DNS.CreateRecord(ctx, \"example.com\", nil, nil, vercel.Pointer(operations.CreateCreateRecordRequestBodyTen(\n        operations.Ten{\n            Type: operations.CreateRecordRequestBodyDNSRequest10TypeCname,\n            TTL: vercel.Float64(60),\n            HTTPS: operations.RequestBodyHTTPS{\n                Priority: vercel.Float64(10),\n                Target: \"host.example.com\",\n                Params: vercel.String(\"alpn=h2,h3\"),\n            },\n            Comment: vercel.String(\"used to verify ownership of domain\"),\n        },\n    )))\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: createRecord
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.dns.createRecord({
              domain: "example.com",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                type: "NS",
                ttl: 60,
                srv: {
                  priority: 10,
                  weight: 10,
                  port: 5000,
                  target: "host.example.com",
                },
                comment: "used to verify ownership of domain",
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
              updated:
                allOf:
                  - type: number
            requiredProperties:
              - uid
              - updated
          - type: object
            properties:
              uid:
                allOf:
                  - type: string
                    description: The id of the newly created DNS record
                    example: rec_V0fra8eEgQwEpFhYG2vTzC3K
            requiredProperties:
              - uid
        examples:
          example:
            value:
              uid: <string>
              updated: 123
        description: Successful response showing the uid of the newly created DNS record.
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
    '404': {}
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Delete a DNS record"

last_updated: "2025-11-07T00:37:09.234Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/dns/delete-a-dns-record"
--------------------------------------------------------------------------------

# Delete a DNS record

> Removes an existing DNS record from a domain name.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v2/domains/{domain}/records/{recordId}
paths:
  path: /v2/domains/{domain}/records/{recordId}
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
              example: example.com
        recordId:
          schema:
            - type: string
              required: true
              example: rec_V0fra8eEgQwEpFhYG2vTzC3K
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
      - label: removeRecord
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.DNS.RemoveRecord(ctx, \"example.com\", \"rec_V0fra8eEgQwEpFhYG2vTzC3K\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: removeRecord
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.dns.removeRecord({
              domain: "example.com",
              recordId: "rec_V0fra8eEgQwEpFhYG2vTzC3K",
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
        description: Successful response by removing the specified DNS record.
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
title: "List existing DNS records"

last_updated: "2025-11-07T00:37:09.268Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/dns/list-existing-dns-records"
--------------------------------------------------------------------------------

# List existing DNS records

> Retrieves a list of DNS records created for a domain name. By default it returns 20 records if no limit is provided. The rest can be retrieved using the pagination options.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/domains/{domain}/records
paths:
  path: /v4/domains/{domain}/records
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
        limit:
          schema:
            - type: string
              required: false
              description: Maximum number of records to list from a request.
              example: 20
        since:
          schema:
            - type: string
              required: false
              description: Get records created after this JavaScript timestamp.
              example: 1609499532000
        until:
          schema:
            - type: string
              required: false
              description: Get records created before this JavaScript timestamp.
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
      - label: getRecords
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.DNS.GetRecords(ctx, operations.GetRecordsRequest{\n        Domain: \"example.com\",\n        Limit: vercel.String(\"20\"),\n        Since: vercel.String(\"1609499532000\"),\n        Until: vercel.String(\"1612264332000\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: getRecords
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.dns.getRecords({
              domain: "example.com",
              limit: "20",
              since: "1609499532000",
              until: "1612264332000",
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
          - type: string
          - type: object
            properties:
              records:
                allOf:
                  - items:
                      properties:
                        id:
                          type: string
                        slug:
                          type: string
                        name:
                          type: string
                        type:
                          type: string
                          enum:
                            - A
                            - AAAA
                            - ALIAS
                            - CAA
                            - CNAME
                            - HTTPS
                            - MX
                            - SRV
                            - TXT
                            - NS
                        value:
                          type: string
                        mxPriority:
                          type: number
                        priority:
                          type: number
                        creator:
                          type: string
                        created:
                          nullable: true
                          type: number
                        updated:
                          nullable: true
                          type: number
                        createdAt:
                          nullable: true
                          type: number
                        updatedAt:
                          nullable: true
                          type: number
                        ttl:
                          type: number
                        comment:
                          type: string
                      required:
                        - id
                        - slug
                        - name
                        - type
                        - value
                        - creator
                        - created
                        - updated
                        - createdAt
                        - updatedAt
                      type: object
                    type: array
            requiredProperties:
              - records
          - type: object
            properties:
              records:
                allOf:
                  - items:
                      properties:
                        id:
                          type: string
                        slug:
                          type: string
                        name:
                          type: string
                        type:
                          type: string
                          enum:
                            - A
                            - AAAA
                            - ALIAS
                            - CAA
                            - CNAME
                            - HTTPS
                            - MX
                            - SRV
                            - TXT
                            - NS
                        value:
                          type: string
                        mxPriority:
                          type: number
                        priority:
                          type: number
                        creator:
                          type: string
                        created:
                          nullable: true
                          type: number
                        updated:
                          nullable: true
                          type: number
                        createdAt:
                          nullable: true
                          type: number
                        updatedAt:
                          nullable: true
                          type: number
                        ttl:
                          type: number
                        comment:
                          type: string
                      required:
                        - id
                        - slug
                        - name
                        - type
                        - value
                        - creator
                        - created
                        - updated
                        - createdAt
                        - updatedAt
                      type: object
                    type: array
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            description: Successful response retrieving a list of paginated DNS records.
            requiredProperties:
              - records
              - pagination
        examples:
          example:
            value: <string>
        description: Successful response retrieving a list of paginated DNS records.
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
title: "Update an existing DNS record"

last_updated: "2025-11-07T00:37:09.223Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/dns/update-an-existing-dns-record"
--------------------------------------------------------------------------------

# Update an existing DNS record

> Updates an existing DNS record for a domain name.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/domains/records/{recordId}
paths:
  path: /v1/domains/records/{recordId}
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
        recordId:
          schema:
            - type: string
              required: true
              description: The id of the DNS record
              example: rec_2qn7pzrx89yxy34vezpd31y9
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
                    description: The name of the DNS record
                    example: example-1
                    nullable: true
              value:
                allOf:
                  - type: string
                    description: The value of the DNS record
                    example: google.com
                    nullable: true
              type:
                allOf:
                  - enum:
                      - A
                      - AAAA
                      - ALIAS
                      - CAA
                      - CNAME
                      - HTTPS
                      - MX
                      - SRV
                      - TXT
                      - NS
                    type: string
                    description: The type of the DNS record
                    example: A
                    maxLength: 255
                    nullable: true
              ttl:
                allOf:
                  - type: integer
                    description: The Time to live (TTL) value of the DNS record
                    example: '60'
                    minimum: 60
                    maximum: 2147483647
                    nullable: true
              mxPriority:
                allOf:
                  - type: integer
                    description: The MX priority value of the DNS record
                    nullable: true
              srv:
                allOf:
                  - additionalProperties: false
                    required:
                      - target
                      - weight
                      - port
                      - priority
                    properties:
                      target:
                        type: string
                        description: ''
                        example: example2.com.
                        maxLength: 255
                        nullable: true
                      weight:
                        description: ''
                        type: integer
                        nullable: true
                      port:
                        description: ''
                        type: integer
                        nullable: true
                      priority:
                        description: ''
                        type: integer
                        nullable: true
                    type: object
                    nullable: true
              https:
                allOf:
                  - additionalProperties: false
                    required:
                      - priority
                      - target
                    properties:
                      priority:
                        description: ''
                        type: integer
                        nullable: true
                      target:
                        type: string
                        description: ''
                        example: example2.com.
                        maxLength: 255
                        nullable: true
                      params:
                        description: ''
                        type: string
                        nullable: true
                    type: object
                    nullable: true
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this DNS record is for
                    example: used to verify ownership of domain
                    maxLength: 500
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              name: example-1
              value: google.com
              type: A
              ttl: '60'
              mxPriority: 123
              srv:
                target: example2.com.
                weight: 123
                port: 123
                priority: 123
              https:
                priority: 123
                target: example2.com.
                params: <string>
              comment: used to verify ownership of domain
    codeSamples:
      - label: updateRecord
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.DNS.UpdateRecord(ctx, \"rec_2qn7pzrx89yxy34vezpd31y9\", nil, nil, &operations.UpdateRecordRequestBody{\n        Name: vercel.String(\"example-1\"),\n        Value: vercel.String(\"google.com\"),\n        Type: operations.UpdateRecordTypeA.ToPointer(),\n        TTL: vercel.Int64(60),\n        Srv: &operations.Srv{\n            Target: vercel.String(\"example2.com.\"),\n            Weight: vercel.Int64(97604),\n            Port: vercel.Int64(570172),\n            Priority: vercel.Int64(199524),\n        },\n        HTTPS: &operations.HTTPS{\n            Priority: vercel.Int64(35000),\n            Target: vercel.String(\"example2.com.\"),\n        },\n        Comment: vercel.String(\"used to verify ownership of domain\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateRecord
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.dns.updateRecord({
              recordId: "rec_2qn7pzrx89yxy34vezpd31y9",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "example-1",
                value: "google.com",
                type: "A",
                ttl: 60,
                srv: null,
                https: null,
                comment: "used to verify ownership of domain",
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
              createdAt:
                allOf:
                  - nullable: true
                    type: number
              creator:
                allOf:
                  - type: string
              domain:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
              recordType:
                allOf:
                  - type: string
                    enum:
                      - A
                      - AAAA
                      - ALIAS
                      - CAA
                      - CNAME
                      - HTTPS
                      - MX
                      - SRV
                      - TXT
                      - NS
              ttl:
                allOf:
                  - type: number
              type:
                allOf:
                  - type: string
                    enum:
                      - record
                      - record-sys
              value:
                allOf:
                  - type: string
              comment:
                allOf:
                  - type: string
            requiredProperties:
              - creator
              - domain
              - id
              - name
              - recordType
              - type
              - value
        examples:
          example:
            value:
              createdAt: 123
              creator: <string>
              domain: <string>
              id: <string>
              name: <string>
              recordType: A
              ttl: 123
              type: record
              value: <string>
              comment: <string>
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
    '404': {}
    '409': {}
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Buy a domain"

last_updated: "2025-11-07T00:37:09.298Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-a-domain"
--------------------------------------------------------------------------------

# Buy a domain

> Buy a domain

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/registrar/domains/{domain}/buy
paths:
  path: /v1/registrar/domains/{domain}/buy
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
                    description: >-
                      Whether the domain should be auto-renewed before it
                      expires. This can be configured later through the Vercel
                      Dashboard or the [Update auto-renew for a
                      domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-auto-renew-for-a-domain)
                      endpoint.
              years:
                allOf:
                  - type: number
                    description: The number of years to purchase the domain for.
              expectedPrice:
                allOf:
                  - type: number
                    description: >-
                      The expected price for the domain. Use the [Get price data
                      for a
                      domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-price-data-for-a-domain)
                      endpoint to retrieve the price data for a domain.
                    minimum: 0.01
              contactInformation:
                allOf:
                  - type: object
                    required:
                      - firstName
                      - lastName
                      - email
                      - phone
                      - address1
                      - city
                      - state
                      - zip
                      - country
                    properties:
                      firstName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      lastName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      email:
                        $ref: '#/components/schemas/EmailAddress'
                      phone:
                        $ref: '#/components/schemas/E164PhoneNumber'
                      address1:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      address2:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      city:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      state:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      zip:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      country:
                        $ref: '#/components/schemas/CountryCode'
                      companyName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      fax:
                        $ref: '#/components/schemas/E164PhoneNumber'
                      additional:
                        type: object
                        properties: {}
                    additionalProperties: false
                    description: >-
                      The contact information for the domain. Some TLDs require
                      additional contact information. Use the [Get contact info
                      schema](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-contact-info-schema)
                      endpoint to retrieve the required fields.
            required: true
            requiredProperties:
              - autoRenew
              - years
              - expectedPrice
              - contactInformation
            additionalProperties: false
        examples:
          example:
            value:
              autoRenew: true
              years: 123
              expectedPrice: 1.01
              contactInformation:
                firstName: <string>
                lastName: <string>
                email: <string>
                phone: <string>
                address1: <string>
                address2: <string>
                city: <string>
                state: <string>
                zip: <string>
                country: <string>
                companyName: <string>
                fax: <string>
                additional: {}
    codeSamples:
      - label: buySingleDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.buySingleDomain({
              domain: "metallic-simple.com",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                autoRenew: false,
                years: 7602.67,
                expectedPrice: 7390.34,
                contactInformation: {
                  firstName: "Lexie",
                  lastName: "Lemke",
                  email: "Lionel21@gmail.com",
                  phone: "550.220.6330 x258",
                  address1: "<value>",
                  city: "Spencerport",
                  state: "West Virginia",
                  zip: "46432",
                  country: "Sweden",
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
              orderId:
                allOf:
                  - type: string
              _links:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      required:
                        - href
                        - method
                      properties:
                        href:
                          type: string
                        method:
                          type: string
                          enum:
                            - GET
                            - POST
                            - PUT
                            - DELETE
                            - PATCH
                      additionalProperties: false
            requiredProperties:
              - orderId
              - _links
            additionalProperties: false
        examples:
          example:
            value:
              orderId: <string>
              _links: {}
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
                      - domain_too_short
              message:
                allOf:
                  - type: string
            description: The domain name (excluding the TLD) is too short.
            refIdentifier: '#/components/schemas/DomainTooShort'
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
                      - order_too_expensive
              message:
                allOf:
                  - type: string
            description: The total price of the order is too high.
            refIdentifier: '#/components/schemas/OrderTooExpensive'
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
                      - invalid_additional_contact_info
              message:
                allOf:
                  - type: string
            description: Additional contact information provided for the TLD is invalid.
            refIdentifier: '#/components/schemas/InvalidAdditionalContactInfo'
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
                      - additional_contact_info_required
              message:
                allOf:
                  - type: string
            description: Additional contact information is required for the TLD.
            refIdentifier: '#/components/schemas/AdditionalContactInfoRequired'
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
                      - expected_price_mismatch
              message:
                allOf:
                  - type: string
            description: The expected price passed does not match the actual price.
            refIdentifier: '#/components/schemas/ExpectedPriceMismatch'
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
                      - domain_not_available
              message:
                allOf:
                  - type: string
            description: The domain is not available.
            refIdentifier: '#/components/schemas/DomainNotAvailable'
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
                      - tld_not_supported
              message:
                allOf:
                  - type: string
            description: The TLD is not currently supported.
            refIdentifier: '#/components/schemas/TldNotSupported'
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
              code: domain_too_short
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
    NonEmptyTrimmedString:
      type: string
      description: a non empty string
      title: nonEmptyString
      pattern: ^\S[\s\S]*\S$|^\S$|^$
      minLength: 1
    EmailAddress:
      type: string
      description: a non empty string
      title: nonEmptyString
      minLength: 1
    E164PhoneNumber:
      type: string
      description: A valid E.164 phone number
      title: nonEmptyString
      minLength: 1
      pattern: ^(?=(?:\D*\d){7,15}$)\+[1-9]\d{0,2}\.?\d+$
    CountryCode:
      type: string
      description: A valid ISO 3166-1 alpha-2 country code
      title: nonEmptyString
      minLength: 1
      pattern: ^[A-Z]{2}$

````

--------------------------------------------------------------------------------
title: "Buy multiple domains"

last_updated: "2025-11-07T00:37:09.571Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-multiple-domains"
--------------------------------------------------------------------------------

# Buy multiple domains

> Buy multiple domains at once

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/registrar/domains/buy
paths:
  path: /v1/registrar/domains/buy
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
              required: false
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              domains:
                allOf:
                  - type: array
                    minItems: 1
                    items:
                      type: object
                      required:
                        - domainName
                        - autoRenew
                        - years
                        - expectedPrice
                      properties:
                        domainName:
                          $ref: '#/components/schemas/DomainName'
                        autoRenew:
                          type: boolean
                          description: >-
                            Whether the domain should be auto-renewed before it
                            expires. This can be configured later through the
                            Vercel Dashboard or the [Update auto-renew for a
                            domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-auto-renew-for-a-domain)
                            endpoint.
                        years:
                          type: number
                          description: The number of years to purchase the domain for.
                        expectedPrice:
                          type: number
                          description: >-
                            The expected price for the domain. Use the [Get
                            price data for a
                            domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-price-data-for-a-domain)
                            endpoint to retrieve the price data for a domain.
                          minimum: 0.01
                      additionalProperties: false
              contactInformation:
                allOf:
                  - type: object
                    required:
                      - firstName
                      - lastName
                      - email
                      - phone
                      - address1
                      - city
                      - state
                      - zip
                      - country
                    properties:
                      firstName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      lastName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      email:
                        $ref: '#/components/schemas/EmailAddress'
                      phone:
                        $ref: '#/components/schemas/E164PhoneNumber'
                      address1:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      address2:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      city:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      state:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      zip:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      country:
                        $ref: '#/components/schemas/CountryCode'
                      companyName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      fax:
                        $ref: '#/components/schemas/E164PhoneNumber'
                      additional:
                        type: object
                        properties: {}
                    additionalProperties: false
                    description: >-
                      The contact information for the domain. Some TLDs require
                      additional contact information. Use the [Get contact info
                      schema](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-contact-info-schema)
                      endpoint to retrieve the required fields.
            required: true
            requiredProperties:
              - domains
              - contactInformation
            additionalProperties: false
        examples:
          example:
            value:
              domains:
                - domainName: <string>
                  autoRenew: true
                  years: 123
                  expectedPrice: 1.01
              contactInformation:
                firstName: <string>
                lastName: <string>
                email: <string>
                phone: <string>
                address1: <string>
                address2: <string>
                city: <string>
                state: <string>
                zip: <string>
                country: <string>
                companyName: <string>
                fax: <string>
                additional: {}
    codeSamples:
      - label: buyDomains
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.buyDomains({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                domains: [],
                contactInformation: {
                  firstName: "Leonie",
                  lastName: "Johnston",
                  email: "Anna_Fisher13@hotmail.com",
                  phone: "(688) 699-0656",
                  address1: "<value>",
                  city: "Rennerland",
                  state: "New Jersey",
                  zip: "70054",
                  country: "Peru",
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
              orderId:
                allOf:
                  - type: string
              _links:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      required:
                        - href
                        - method
                      properties:
                        href:
                          type: string
                        method:
                          type: string
                          enum:
                            - GET
                            - POST
                            - PUT
                            - DELETE
                            - PATCH
                      additionalProperties: false
            requiredProperties:
              - orderId
              - _links
            additionalProperties: false
        examples:
          example:
            value:
              orderId: <string>
              _links: {}
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
                      - domain_too_short
              message:
                allOf:
                  - type: string
            description: The domain name (excluding the TLD) is too short.
            refIdentifier: '#/components/schemas/DomainTooShort'
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
                      - order_too_expensive
              message:
                allOf:
                  - type: string
            description: The total price of the order is too high.
            refIdentifier: '#/components/schemas/OrderTooExpensive'
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
                      - too_many_domains
              message:
                allOf:
                  - type: string
            description: The number of domains in the order is too high.
            refIdentifier: '#/components/schemas/TooManyDomains'
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
                      - invalid_additional_contact_info
              message:
                allOf:
                  - type: string
            description: Additional contact information provided for the TLD is invalid.
            refIdentifier: '#/components/schemas/InvalidAdditionalContactInfo'
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
                      - additional_contact_info_required
              message:
                allOf:
                  - type: string
            description: Additional contact information is required for the TLD.
            refIdentifier: '#/components/schemas/AdditionalContactInfoRequired'
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
                      - duplicate_domains
              message:
                allOf:
                  - type: string
            description: Duplicate domains were provided.
            refIdentifier: '#/components/schemas/DuplicateDomains'
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
                      - expected_price_mismatch
              message:
                allOf:
                  - type: string
            description: The expected price passed does not match the actual price.
            refIdentifier: '#/components/schemas/ExpectedPriceMismatch'
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
                      - domain_not_available
              message:
                allOf:
                  - type: string
            description: The domain is not available.
            refIdentifier: '#/components/schemas/DomainNotAvailable'
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
                      - tld_not_supported
              message:
                allOf:
                  - type: string
            description: The TLD is not currently supported.
            refIdentifier: '#/components/schemas/TldNotSupported'
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
              code: domain_too_short
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
    DomainName:
      type: string
    NonEmptyTrimmedString:
      type: string
      description: a non empty string
      title: nonEmptyString
      pattern: ^\S[\s\S]*\S$|^\S$|^$
      minLength: 1
    EmailAddress:
      type: string
      description: a non empty string
      title: nonEmptyString
      minLength: 1
    E164PhoneNumber:
      type: string
      description: A valid E.164 phone number
      title: nonEmptyString
      minLength: 1
      pattern: ^(?=(?:\D*\d){7,15}$)\+[1-9]\d{0,2}\.?\d+$
    CountryCode:
      type: string
      description: A valid ISO 3166-1 alpha-2 country code
      title: nonEmptyString
      minLength: 1
      pattern: ^[A-Z]{2}$

````

--------------------------------------------------------------------------------
title: "Get a domain order"

last_updated: "2025-11-07T00:37:09.266Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-a-domain-order"
--------------------------------------------------------------------------------

# Get a domain order

> Get information about a domain order by its ID

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/orders/{orderId}
paths:
  path: /v1/registrar/orders/{orderId}
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
        orderId:
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
    body: {}
    codeSamples:
      - label: getOrder
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.getOrder({
              orderId: "<id>",
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
              orderId:
                allOf:
                  - type: string
              domains:
                allOf:
                  - type: array
                    items:
                      anyOf:
                        - type: object
                          required:
                            - purchaseType
                            - autoRenew
                            - years
                            - domainName
                            - status
                            - price
                          properties:
                            purchaseType:
                              type: string
                              enum:
                                - purchase
                            autoRenew:
                              type: boolean
                            years:
                              type: number
                              description: >-
                                The number of years the domain is being
                                purchased for.
                            domainName:
                              $ref: '#/components/schemas/DomainName'
                            status:
                              type: string
                              enum:
                                - pending
                                - completed
                                - failed
                                - refunded
                                - refund-failed
                            price:
                              type: number
                              description: The price for the domain.
                              minimum: 0.01
                          additionalProperties: false
                        - type: object
                          required:
                            - purchaseType
                            - years
                            - domainName
                            - status
                            - price
                          properties:
                            purchaseType:
                              type: string
                              enum:
                                - renewal
                            years:
                              type: number
                              description: >-
                                The number of years the domain is being renewed
                                for.
                            domainName:
                              $ref: '#/components/schemas/DomainName'
                            status:
                              type: string
                              enum:
                                - pending
                                - completed
                                - failed
                                - refunded
                                - refund-failed
                            price:
                              type: number
                              description: The price for the domain.
                              minimum: 0.01
                          additionalProperties: false
                        - type: object
                          required:
                            - purchaseType
                            - autoRenew
                            - years
                            - domainName
                            - status
                            - price
                          properties:
                            purchaseType:
                              type: string
                              enum:
                                - transfer
                            autoRenew:
                              type: boolean
                            years:
                              type: number
                              description: >-
                                The number of years the domain is being
                                transferred for.
                            domainName:
                              $ref: '#/components/schemas/DomainName'
                            status:
                              type: string
                              enum:
                                - pending
                                - completed
                                - failed
                                - refunded
                                - refund-failed
                            price:
                              type: number
                              description: The price for the domain.
                              minimum: 0.01
                          additionalProperties: false
              status:
                allOf:
                  - type: string
                    enum:
                      - draft
                      - purchasing
                      - completed
                      - failed
              error:
                allOf:
                  - anyOf:
                      - type: object
                        required:
                          - code
                        properties:
                          code:
                            type: string
                            enum:
                              - payment-failed
                        additionalProperties: false
                      - type: object
                        required:
                          - code
                          - details
                        properties:
                          code:
                            type: string
                            enum:
                              - tld-outage
                          details:
                            type: object
                            required:
                              - tlds
                            properties:
                              tlds:
                                type: array
                                items:
                                  type: object
                                  required:
                                    - tldName
                                    - endsAt
                                  properties:
                                    tldName:
                                      type: string
                                    endsAt:
                                      type: string
                                  additionalProperties: false
                            additionalProperties: false
                        additionalProperties: false
                      - type: object
                        required:
                          - code
                          - details
                        properties:
                          code:
                            type: string
                            enum:
                              - price-mismatch
                          details:
                            type: object
                            required:
                              - expectedPrice
                            properties:
                              expectedPrice:
                                type: number
                              actualPrice:
                                type: number
                            additionalProperties: false
                        additionalProperties: false
                      - type: object
                        required:
                          - code
                        properties:
                          code:
                            type: string
                            enum:
                              - unexpected-error
                        additionalProperties: false
            requiredProperties:
              - orderId
              - domains
              - status
            additionalProperties: false
        examples:
          example:
            value:
              orderId: <string>
              domains:
                - purchaseType: purchase
                  autoRenew: true
                  years: 123
                  domainName: <string>
                  status: pending
                  price: 1.01
              status: draft
              error:
                code: payment-failed
        description: Success
    '400':
      application/json:
        schemaArray:
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
              issues:
                - path:
                    - <string>
                  message: <string>
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
                      - not_found
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/NotFound'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 404
              code: not_found
              message: <string>
        description: NotFound
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
    DomainName:
      type: string

````

--------------------------------------------------------------------------------
title: "Get a domain's transfer status"

last_updated: "2025-11-07T00:37:09.479Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-a-domains-transfer-status"
--------------------------------------------------------------------------------

# Get a domain's transfer status

> Get the transfer status for a domain

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/domains/{domain}/transfer
paths:
  path: /v1/registrar/domains/{domain}/transfer
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
      query:
        teamId:
          schema:
            - type: string
              required: false
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getDomainTransferIn
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.getDomainTransferIn({
              domain: "unsung-antelope.com",
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
              status:
                allOf:
                  - type: string
                    enum:
                      - canceled
                      - canceled_pending_refund
                      - completed
                      - created
                      - failed
                      - pending
                      - pending_insert
                      - pending_new_auth_code
                      - pending_transfer
                      - pending_unlock
                      - rejected
                      - submitting_transfer
            requiredProperties:
              - status
            additionalProperties: false
        examples:
          example:
            value:
              status: canceled
        description: Success
    '400':
      application/json:
        schemaArray:
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
              issues:
                - path:
                    - <string>
                  message: <string>
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
                      - not_found
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/NotFound'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 404
              code: not_found
              message: <string>
        description: NotFound
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
title: "Get availability for a domain"

last_updated: "2025-11-07T00:37:09.448Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-availability-for-a-domain"
--------------------------------------------------------------------------------

# Get availability for a domain

> Get availability for a specific domain. If the domain is available, it can be purchased using the [Buy a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-a-domain) endpoint or the [Buy multiple domains](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-multiple-domains) endpoint.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/domains/{domain}/availability
paths:
  path: /v1/registrar/domains/{domain}/availability
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
      query:
        teamId:
          schema:
            - type: string
              required: false
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getDomainAvailability
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.getDomainAvailability({
              domain: "hungry-birdbath.info",
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
              available:
                allOf:
                  - type: boolean
            requiredProperties:
              - available
            additionalProperties: false
        examples:
          example:
            value:
              available: true
        description: Success
    '400':
      application/json:
        schemaArray:
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
              issues:
                - path:
                    - <string>
                  message: <string>
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
                      - not_found
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/NotFound'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 404
              code: not_found
              message: <string>
        description: NotFound
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
title: "Get availability for multiple domains"

last_updated: "2025-11-07T00:37:09.225Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-availability-for-multiple-domains"
--------------------------------------------------------------------------------

# Get availability for multiple domains

> Get availability for multiple domains. If the domains are available, they can be purchased using the [Buy a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-a-domain) endpoint or the [Buy multiple domains](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-multiple-domains) endpoint.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/registrar/domains/availability
paths:
  path: /v1/registrar/domains/availability
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
              required: false
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              domains:
                allOf:
                  - type: array
                    minItems: 1
                    items:
                      $ref: '#/components/schemas/DomainName'
                    description: an array of at most 50 item(s)
                    title: maxItems(50)
                    maxItems: 50
            required: true
            requiredProperties:
              - domains
            additionalProperties: false
        examples:
          example:
            value:
              domains:
                - <string>
    codeSamples:
      - label: getBulkAvailability
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.getBulkAvailability({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                domains: [
                  "<value 1>",
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
              results:
                allOf:
                  - type: array
                    items:
                      type: object
                      required:
                        - domain
                        - available
                      properties:
                        domain:
                          $ref: '#/components/schemas/DomainName'
                        available:
                          type: boolean
                      additionalProperties: false
            requiredProperties:
              - results
            additionalProperties: false
        examples:
          example:
            value:
              results:
                - domain: <string>
                  available: true
        description: Success
    '400':
      application/json:
        schemaArray:
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
              issues:
                - path:
                    - <string>
                  message: <string>
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
        examples:
          example:
            value:
              status: 403
              code: not_authorized_for_scope
              message: <string>
        description: NotAuthorizedForScope
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
    DomainName:
      type: string

````

--------------------------------------------------------------------------------
title: "Get contact info schema"

last_updated: "2025-11-07T00:37:09.282Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-contact-info-schema"
--------------------------------------------------------------------------------

# Get contact info schema

> Some TLDs require additional contact information. Use this endpoint to get the schema for the tld-specific contact information for a domain.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/domains/{domain}/contact-info/schema
paths:
  path: /v1/registrar/domains/{domain}/contact-info/schema
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
      query:
        teamId:
          schema:
            - type: string
              required: false
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getContactInfoSchema
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.getContactInfoSchema({
              domain: "tricky-issue.name",
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
            properties: {}
        examples:
          example:
            value: {}
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
                      - bad_request
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/BadRequest'
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
              code: bad_request
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
        examples:
          example:
            value:
              status: 403
              code: not_authorized_for_scope
              message: <string>
        description: NotAuthorizedForScope
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
title: "Get price data for a domain"

last_updated: "2025-11-07T00:37:09.282Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-price-data-for-a-domain"
--------------------------------------------------------------------------------

# Get price data for a domain

> Get price data for a specific domain

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/domains/{domain}/price
paths:
  path: /v1/registrar/domains/{domain}/price
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
      query:
        years:
          schema:
            - type: string
              required: false
              description: a string to be decoded into a number
        teamId:
          schema:
            - type: string
              required: false
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getDomainPrice
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.getDomainPrice({
              domain: "excited-dwell.org",
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
              years:
                allOf:
                  - type: number
              purchasePrice:
                allOf:
                  - type: number
                    description: >-
                      The price for purchasing this domain for the given number
                      of years. If null, the domain is not available for
                      purchase for the given number of years.
                    minimum: 0.01
                    nullable: true
              renewalPrice:
                allOf:
                  - type: number
                    description: >-
                      The price for renewing this domain for the given number of
                      years. If null, the domain cannot be renewed for the given
                      number of years.
                    minimum: 0.01
                    nullable: true
              transferPrice:
                allOf:
                  - type: number
                    description: >-
                      The price for transferring this domain in for the given
                      number of years. If null, the domain cannot be transferred
                      in for the given number of years.
                    minimum: 0.01
                    nullable: true
            requiredProperties:
              - years
              - purchasePrice
              - renewalPrice
              - transferPrice
            additionalProperties: false
        examples:
          example:
            value:
              years: 123
              purchasePrice: 1.01
              renewalPrice: 1.01
              transferPrice: 1.01
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
                      - bad_request
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/BadRequest'
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
                      - domain_too_short
              message:
                allOf:
                  - type: string
            description: The domain name (excluding the TLD) is too short.
            refIdentifier: '#/components/schemas/DomainTooShort'
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
                      - tld_not_supported
              message:
                allOf:
                  - type: string
            description: The TLD is not currently supported.
            refIdentifier: '#/components/schemas/TldNotSupported'
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
              code: bad_request
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
        examples:
          example:
            value:
              status: 403
              code: not_authorized_for_scope
              message: <string>
        description: NotAuthorizedForScope
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
title: "Get supported TLDs"

last_updated: "2025-11-07T00:37:09.902Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-supported-tlds"
--------------------------------------------------------------------------------

# Get supported TLDs

> Get a list of TLDs supported by Vercel

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/tlds/supported
paths:
  path: /v1/registrar/tlds/supported
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
              required: false
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getSupportedTlds
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.getSupportedTlds({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
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
                - type: string
            description: A list of the TLDs supported by Vercel.
        examples:
          example:
            value:
              - <string>
        description: A list of the TLDs supported by Vercel.
    '400':
      application/json:
        schemaArray:
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
              issues:
                - path:
                    - <string>
                  message: <string>
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
        examples:
          example:
            value:
              status: 403
              code: not_authorized_for_scope
              message: <string>
        description: NotAuthorizedForScope
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
title: "Get the auth code for a domain"

last_updated: "2025-11-07T00:37:09.891Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-the-auth-code-for-a-domain"
--------------------------------------------------------------------------------

# Get the auth code for a domain

> Get the auth code for a domain. This is required to transfer a domain from Vercel to another registrar.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/domains/{domain}/auth-code
paths:
  path: /v1/registrar/domains/{domain}/auth-code
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
      query:
        teamId:
          schema:
            - type: string
              required: false
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getDomainAuthCode
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.getDomainAuthCode({
              domain: "ruddy-coil.org",
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
              authCode:
                allOf:
                  - type: string
            requiredProperties:
              - authCode
            additionalProperties: false
        examples:
          example:
            value:
              authCode: <string>
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

````

--------------------------------------------------------------------------------
title: "Get TLD price data"

last_updated: "2025-11-07T00:37:10.035Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-tld-price-data"
--------------------------------------------------------------------------------

# Get TLD price data

> Get price data for a specific TLD. This only reflects base prices for the given TLD. Premium domains may have different prices. Use the [Get price data for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-price-data-for-a-domain) endpoint to get the price data for a specific domain.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/tlds/{tld}/price
paths:
  path: /v1/registrar/tlds/{tld}/price
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
        tld:
          schema:
            - type: string
              required: true
      query:
        years:
          schema:
            - type: string
              required: false
              description: a string to be decoded into a number
        teamId:
          schema:
            - type: string
              required: false
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getTldPrice
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.getTldPrice({
              tld: "<value>",
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
              years:
                allOf:
                  - type: number
                    description: The number of years the returned price is for.
              purchasePrice:
                allOf:
                  - type: number
                    description: >-
                      The base TLD price for purchasing a domain for the given
                      number of years. If null, the TLD does not support
                      purchasing domains for the given number of years.
                    minimum: 0.01
                    nullable: true
              renewalPrice:
                allOf:
                  - type: number
                    description: >-
                      The base TLD price for renewing a domain for the given
                      number of years. If null, the TLD does not support
                      renewing domains for the given number of years.
                    minimum: 0.01
                    nullable: true
              transferPrice:
                allOf:
                  - type: number
                    description: >-
                      The base TLD price for transferring a domain in for the
                      given number of years. If null, the TLD does not support
                      transferring domains in for the given number of years.
                    minimum: 0.01
                    nullable: true
            requiredProperties:
              - years
              - purchasePrice
              - renewalPrice
              - transferPrice
            additionalProperties: false
        examples:
          example:
            value:
              years: 123
              purchasePrice: 1.01
              renewalPrice: 1.01
              transferPrice: 1.01
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
                      - tld_not_supported
              message:
                allOf:
                  - type: string
            description: The TLD is not currently supported.
            refIdentifier: '#/components/schemas/TldNotSupported'
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
              code: tld_not_supported
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
        examples:
          example:
            value:
              status: 403
              code: not_authorized_for_scope
              message: <string>
        description: NotAuthorizedForScope
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
title: "Renew a domain"

last_updated: "2025-11-07T00:37:09.875Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/renew-a-domain"
--------------------------------------------------------------------------------

# Renew a domain

> Renew a domain

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/registrar/domains/{domain}/renew
paths:
  path: /v1/registrar/domains/{domain}/renew
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
              years:
                allOf:
                  - type: number
                    description: The number of years to renew the domain for.
              expectedPrice:
                allOf:
                  - type: number
                    description: >-
                      The expected price for the domain. Use the [Get price data
                      for a
                      domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-price-data-for-a-domain)
                      endpoint to retrieve the price data for a domain.
                    minimum: 0.01
              contactInformation:
                allOf:
                  - type: object
                    required:
                      - firstName
                      - lastName
                      - email
                      - phone
                      - address1
                      - city
                      - state
                      - zip
                      - country
                    properties:
                      firstName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      lastName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      email:
                        $ref: '#/components/schemas/EmailAddress'
                      phone:
                        $ref: '#/components/schemas/E164PhoneNumber'
                      address1:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      address2:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      city:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      state:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      zip:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      country:
                        $ref: '#/components/schemas/CountryCode'
                      companyName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      fax:
                        $ref: '#/components/schemas/E164PhoneNumber'
                    additionalProperties: false
            required: true
            requiredProperties:
              - years
              - expectedPrice
            additionalProperties: false
        examples:
          example:
            value:
              years: 123
              expectedPrice: 1.01
              contactInformation:
                firstName: <string>
                lastName: <string>
                email: <string>
                phone: <string>
                address1: <string>
                address2: <string>
                city: <string>
                state: <string>
                zip: <string>
                country: <string>
                companyName: <string>
                fax: <string>
    codeSamples:
      - label: renewDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.renewDomain({
              domain: "scaly-daughter.biz",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                years: 1981.72,
                expectedPrice: 7096.16,
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
              orderId:
                allOf:
                  - type: string
              _links:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      required:
                        - href
                        - method
                      properties:
                        href:
                          type: string
                        method:
                          type: string
                          enum:
                            - GET
                            - POST
                            - PUT
                            - DELETE
                            - PATCH
                      additionalProperties: false
            requiredProperties:
              - orderId
              - _links
            additionalProperties: false
        examples:
          example:
            value:
              orderId: <string>
              _links: {}
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
                      - bad_request
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/BadRequest'
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
                      - domain_too_short
              message:
                allOf:
                  - type: string
            description: The domain name (excluding the TLD) is too short.
            refIdentifier: '#/components/schemas/DomainTooShort'
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
              status:
                allOf:
                  - type: number
                    enum:
                      - 400
              code:
                allOf:
                  - type: string
                    enum:
                      - expected_price_mismatch
              message:
                allOf:
                  - type: string
            description: The expected price passed does not match the actual price.
            refIdentifier: '#/components/schemas/ExpectedPriceMismatch'
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
                      - domain_not_available
              message:
                allOf:
                  - type: string
            description: The domain is not available.
            refIdentifier: '#/components/schemas/DomainNotAvailable'
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
                      - tld_not_supported
              message:
                allOf:
                  - type: string
            description: The TLD is not currently supported.
            refIdentifier: '#/components/schemas/TldNotSupported'
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
              code: bad_request
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
    NonEmptyTrimmedString:
      type: string
      description: a non empty string
      title: nonEmptyString
      pattern: ^\S[\s\S]*\S$|^\S$|^$
      minLength: 1
    EmailAddress:
      type: string
      description: a non empty string
      title: nonEmptyString
      minLength: 1
    E164PhoneNumber:
      type: string
      description: A valid E.164 phone number
      title: nonEmptyString
      minLength: 1
      pattern: ^(?=(?:\D*\d){7,15}$)\+[1-9]\d{0,2}\.?\d+$
    CountryCode:
      type: string
      description: A valid ISO 3166-1 alpha-2 country code
      title: nonEmptyString
      minLength: 1
      pattern: ^[A-Z]{2}$

````

--------------------------------------------------------------------------------
title: "Transfer-in a domain"

last_updated: "2025-11-07T00:37:10.009Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/transfer-in-a-domain"
--------------------------------------------------------------------------------

# Transfer-in a domain

> Transfer a domain in from another registrar

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/registrar/domains/{domain}/transfer
paths:
  path: /v1/registrar/domains/{domain}/transfer
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
              authCode:
                allOf:
                  - type: string
              autoRenew:
                allOf:
                  - type: boolean
                    description: >-
                      Whether the domain should be auto-renewed before it
                      expires. This can be configured later through the Vercel
                      Dashboard or the [Update auto-renew for a
                      domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-auto-renew-for-a-domain)
                      endpoint.
              years:
                allOf:
                  - type: number
                    description: >-
                      The number of years to renew the domain for once it is
                      transferred in. This must be a valid number of transfer
                      years for the TLD.
              expectedPrice:
                allOf:
                  - type: number
                    description: >-
                      The expected price for the domain. Use the [Get price data
                      for a
                      domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-price-data-for-a-domain)
                      endpoint to retrieve the price data for a domain.
                    minimum: 0.01
              contactInformation:
                allOf:
                  - type: object
                    required:
                      - firstName
                      - lastName
                      - email
                      - phone
                      - address1
                      - city
                      - state
                      - zip
                      - country
                    properties:
                      firstName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      lastName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      email:
                        $ref: '#/components/schemas/EmailAddress'
                      phone:
                        $ref: '#/components/schemas/E164PhoneNumber'
                      address1:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      address2:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      city:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      state:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      zip:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      country:
                        $ref: '#/components/schemas/CountryCode'
                      companyName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      fax:
                        $ref: '#/components/schemas/E164PhoneNumber'
                    additionalProperties: false
            required: true
            requiredProperties:
              - authCode
              - autoRenew
              - years
              - expectedPrice
              - contactInformation
            additionalProperties: false
        examples:
          example:
            value:
              authCode: <string>
              autoRenew: true
              years: 123
              expectedPrice: 1.01
              contactInformation:
                firstName: <string>
                lastName: <string>
                email: <string>
                phone: <string>
                address1: <string>
                address2: <string>
                city: <string>
                state: <string>
                zip: <string>
                country: <string>
                companyName: <string>
                fax: <string>
    codeSamples:
      - label: transferInDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.transferInDomain({
              domain: "silky-fund.org",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                authCode: "<value>",
                autoRenew: true,
                years: 298.08,
                expectedPrice: 5092.5,
                contactInformation: {
                  firstName: "Gabrielle",
                  lastName: "Hackett",
                  email: "Keshawn99@yahoo.com",
                  phone: "(758) 385-1802 x13762",
                  address1: "<value>",
                  city: "Pattiestead",
                  state: "Idaho",
                  zip: "64653-9022",
                  country: "Bolivia",
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
              orderId:
                allOf:
                  - type: string
              _links:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      required:
                        - href
                        - method
                      properties:
                        href:
                          type: string
                        method:
                          type: string
                          enum:
                            - GET
                            - POST
                            - PUT
                            - DELETE
                            - PATCH
                      additionalProperties: false
            requiredProperties:
              - orderId
              - _links
            additionalProperties: false
        examples:
          example:
            value:
              orderId: <string>
              _links: {}
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
                      - bad_request
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/BadRequest'
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
                      - domain_already_owned
              message:
                allOf:
                  - type: string
            description: The domain is already owned by another team or user.
            refIdentifier: '#/components/schemas/DomainAlreadyOwned'
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
                      - domain_too_short
              message:
                allOf:
                  - type: string
            description: The domain name (excluding the TLD) is too short.
            refIdentifier: '#/components/schemas/DomainTooShort'
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
                      - dnssec_enabled
              message:
                allOf:
                  - type: string
            description: >-
              The operation cannot be completed because DNSSEC is enabled for
              the domain.
            refIdentifier: '#/components/schemas/DNSSECEnabled'
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
                      - expected_price_mismatch
              message:
                allOf:
                  - type: string
            description: The expected price passed does not match the actual price.
            refIdentifier: '#/components/schemas/ExpectedPriceMismatch'
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
                      - domain_not_available
              message:
                allOf:
                  - type: string
            description: The domain is not available.
            refIdentifier: '#/components/schemas/DomainNotAvailable'
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
                      - tld_not_supported
              message:
                allOf:
                  - type: string
            description: The TLD is not currently supported.
            refIdentifier: '#/components/schemas/TldNotSupported'
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
              code: bad_request
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
    NonEmptyTrimmedString:
      type: string
      description: a non empty string
      title: nonEmptyString
      pattern: ^\S[\s\S]*\S$|^\S$|^$
      minLength: 1
    EmailAddress:
      type: string
      description: a non empty string
      title: nonEmptyString
      minLength: 1
    E164PhoneNumber:
      type: string
      description: A valid E.164 phone number
      title: nonEmptyString
      minLength: 1
      pattern: ^(?=(?:\D*\d){7,15}$)\+[1-9]\d{0,2}\.?\d+$
    CountryCode:
      type: string
      description: A valid ISO 3166-1 alpha-2 country code
      title: nonEmptyString
      minLength: 1
      pattern: ^[A-Z]{2}$

````

--------------------------------------------------------------------------------
title: "Update auto-renew for a domain"

last_updated: "2025-11-07T00:37:09.890Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-auto-renew-for-a-domain"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./20-delete-a-deployment.md) | [Index](./index.md) | [Next →](./22-update-auto-renew-for-a-domain.md)
