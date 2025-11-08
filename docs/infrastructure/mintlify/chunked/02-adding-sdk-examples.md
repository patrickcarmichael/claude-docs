**Navigation:** [← Previous](./01-ai-native.md) | [Index](./index.md) | [Next →](./03-mermaid.md)

# Adding SDK examples
Source: https://mintlify.com/docs/api-playground/adding-sdk-examples

Display language-specific code samples alongside your API endpoints to show developers how to use your SDKs

If your users interact with your API using an SDK rather than directly through a network request, you can use the `x-codeSamples` extension to add code samples to your OpenAPI document and display them in your OpenAPI pages.

This property can be added to any request method and has the following schema.

<ParamField body="lang" type="string" required>
  The language of the code sample.
</ParamField>

<ParamField body="label" type="string">
  The label for the sample. This is useful when providing multiple examples for a single endpoint.
</ParamField>

<ParamField body="source" type="string" required>
  The source code of the sample.
</ParamField>

Here is an example of code samples for a plant tracking app, which has both a Bash CLI tool and a JavaScript SDK.

```yaml  theme={null}
paths:
  /plants:
    get:
      # ...
      x-codeSamples:
        - lang: bash
          label: List all unwatered plants
          source: |
            planter list -u
        - lang: javascript
          label: List all unwatered plants
          source: |
            const planter = require('planter');
            planter.list({ unwatered: true });
        - lang: bash
          label: List all potted plants
          source: |
            planter list -p
        - lang: javascript
          label: List all potted plants
          source: |
            const planter = require('planter');
            planter.list({ potted: true });
```



# Playground
Source: https://mintlify.com/docs/api-playground/asyncapi/playground

Enable users to interact with your websockets




# AsyncAPI setup
Source: https://mintlify.com/docs/api-playground/asyncapi/setup

Create websocket reference pages with AsyncAPI


## Add an AsyncAPI specification file

To begin to create pages for your websockets, make sure you have a valid AsyncAPI schema document in either JSON or YAML format that follows the [AsyncAPI specification](https://www.asyncapi.com/docs/reference/specification/v3.0.0). Your schema must follow the AsyncAPI specification 3.0+.

<Tip>
  To make sure your AsyncAPI schema is valid, you can paste it into the
  [AsyncAPI Studio](https://studio.asyncapi.com/)
</Tip>


## Auto-populate websockets pages

You can add an `asyncapi` field to any tab or group in the navigation of your `docs.json`. This field can contain either the path to an AsyncAPI schema document in your docs repo, the URL of a hosted AsyncAPI schema document, or an array of links to AsyncAPI schema documents. Mintlify will automatically generate a page for each AsyncAPI websocket channel.

**Examples with Tabs:**

<CodeGroup>
  ```json Local File {5} theme={null}
  "navigation": {
    "tabs": [
      {
          "tab": "API Reference",
          "asyncapi": "/path/to/asyncapi.json"
      }
    ]
  }

  ```

  ```json Remote URL {5} theme={null}
  "navigation": {
    "tabs": [
      {
          "tab": "API Reference",
          "asyncapi": "https://github.com/asyncapi/spec/blob/master/examples/simple-asyncapi.yml"
      }
    ]
  }
  ```
</CodeGroup>

**Examples with Groups:**

```json {8-11} theme={null}
"navigation": {
  "tabs": [
    {
      "tab": "AsyncAPI",
      "groups": [
        {
          "group": "Websockets",
          "asyncapi": {
            "source": "/path/to/asyncapi.json",
            "directory": "api-reference"
          }
        }
      ]
    }
  ]
}
```

<Note>
  The directory field is optional. If not specified, the files will be placed in
  the **api-reference** folder of the docs repo.
</Note>


## Channel page

If you want more control over how you order your channels or if you want to just reference a single channel, you can create an MDX file with the `asyncapi` field in the frontmatter.

```mdx  theme={null}
---
title: "Websocket Channel"
asyncapi: "/path/to/asyncapi.json channelName"
---
```



# Complex data types
Source: https://mintlify.com/docs/api-playground/complex-data-types

Describe APIs with flexible schemas, optional properties, and multiple data formats using `oneOf`, `anyOf`, and `allOf` keywords

When your API accepts multiple data formats, has conditional fields, or uses inheritance patterns, OpenAPI's schema composition keywords help you document these flexible structures. Using `oneOf`, `anyOf`, and `allOf`, you can describe APIs that handle different input types or combine multiple schemas into comprehensive data models.


## `oneOf`, `anyOf`, `allOf` keywords

For complex data types, OpenAPI provides keywords for combining schemas:

* `allOf`: Combines multiple schemas (like merging objects or extending a base schema). Functions like an `and` operator.
* `anyOf`: Accepts data matching any of the provided schemas. Functions like an `or` operator.
* `oneOf`: Accepts data matching exactly one of the provided schemas. Functions like an `exclusive-or` operator.

<Warning>Mintlify treats `oneOf` and `anyOf` identically since the practical difference rarely affects using the API.</Warning>

For detailed specifications of these keywords see the [OpenAPI documentation](https://swagger.io/docs/specification/data-models/oneof-anyof-allof-not/).

<Info>The `not` keyword is currently unsupported.</Info>

### Combining schemas with `allOf`

When you use `allOf`, Mintlify performs some preprocessing on your OpenAPI document to display complex combinations in a readable way. For example, when you combine two object schemas with `allOf`, Mintlify combines the properties of both into a single object. This becomes especially useful when leveraging OpenAPI's reusable [components](https://swagger.io/docs/specification/components/).

```yaml  theme={null}
org_with_users:
  allOf:
    - $ref: '#/components/schemas/Org'
    - type: object
      properties:
        users:
          type: array
          description: An array containing all users in the organization

# ...
components:
  schemas:
    Org:
      type: object
      properties:
        id:
          type: string
          description: The ID of the organization
```

<ParamField body="org_with_users" type="object">
  <Expandable>
    <ParamField body="id" type="string">
      The ID of the organization
    </ParamField>

    <ParamField body="users" type="object[]">
      An array containing all users in the organization
    </ParamField>
  </Expandable>
</ParamField>

### Providing options with `oneOf` and `anyOf`

When you use `oneOf` or `anyOf`, the options are displayed in a tabbed container. Specify a `title` field in each subschema to give your options names. For example, here's how you might display two different types of delivery addresses:

```yaml  theme={null}
delivery_address:
  oneOf:
    - title: StreetAddress
      type: object
      properties:
        address_line_1:
          type: string
          description: The street address of the recipient
        # ...
    - title: POBox
      type: object
      properties:
        box_number:
          type: string
          description: The number of the PO Box
        # ...
```

<ParamField body="delivery_address" type="object">
  <div className="mt-4 rounded-xl border border-gray-100 px-4 pb-4 pt-2 dark:border-white/10">
    <Tabs>
      <Tab title="StreetAddress">
        <ParamField body="address_line_1" type="string">
          The street address of the residence
        </ParamField>
      </Tab>

      <Tab title="POBox">
        <ParamField body="box_number" type="string">
          The number of the PO Box
        </ParamField>
      </Tab>
    </Tabs>
  </div>
</ParamField>



# Managing page visibility
Source: https://mintlify.com/docs/api-playground/managing-page-visibility

Control which endpoints from your OpenAPI specification appear in your documentation navigation

You can control which OpenAPI operations get published as documentation pages and their visibility in navigation. This is useful for internal-only endpoints, deprecated operations, beta features, or endpoints that should be accessible via direct URL but not discoverable through site navigation.

If your pages are autogenerated from an OpenAPI document, you can manage page visibility with the `x-hidden` and `x-excluded` extensions.


## `x-hidden`

The `x-hidden` extension creates a page for an endpoint, but hides it from navigation. The page is only accessible by navigating directly to its URL.

Common use cases for `x-hidden` are:

* Endpoints you want to document, but not promote.
* Pages that you will link to from other content.
* Endpoints for specific users.


## `x-excluded`

The `x-excluded` extension completely excludes an endpoint from your documentation.

Common use cases for `x-excluded` are:

* Internal-only endpoints.
* Deprecated endpoints that you don't want to document.
* Beta features that are not ready for public documentation.


## Implementation

Add the `x-hidden` or `x-excluded` extension under the HTTP method in your OpenAPI specification.

Here are examples of how to use each property in an OpenAPI schema document for an endpoint and a webhook path.

```json {11, 19} theme={null}
"paths": {
  "/plants": {
    "get": {
      "description": "Returns all plants from the store",
      "parameters": { /*...*/ },
      "responses": { /*...*/ }
    }
  },
  "/hidden_plants": {
    "get": {
      "x-hidden": true,
      "description": "Returns all somewhat secret plants from the store",
      "parameters": { /*...*/ },
      "responses": { /*...*/ }
    }
  },
  "/secret_plants": {
    "get": {
      "x-excluded": true,
      "description": "Returns all top secret plants from the store (do not publish this endpoint!)",
      "parameters": { /*...*/ },
      "responses": { /*...*/ }
    }
  }
},
```

```json {9, 15} theme={null}
"webhooks": {
  "/plants_hook": {
    "post": {
      "description": "Webhook for information about a new plant added to the store",
    }
  },
  "/hidden_plants_hook": {
    "post": {
      "x-hidden": true,
      "description": "Webhook for somewhat secret information about a new plant added to the store"
    }
  },
  "/secret_plants_hook": {
    "post": {
      "x-excluded": true,
      "description": "Webhook for top secret information about a new plant added to the store (do not publish this endpoint!)"
    }
  }
}
```



# Authentication
Source: https://mintlify.com/docs/api-playground/mdx/authentication

You can set authentication parameters to let users use their real API keys.


## Enabling authentication

You can add an authentication method to your `docs.json` to enable it globally on every page or you can set it on a per-page basis.

A page's authentication method will override a global method if both are set.

### Bearer token

<CodeGroup>
  ```json docs.json theme={null}
  "api": {
      "mdx": {
        "auth": {
          "method": "bearer"
        }
      }
  }
  ```

  ```mdx Page Metadata theme={null}
  ---
  title: "Your page title"
  authMethod: "bearer"
  ---
  ```
</CodeGroup>

### Basic authentication

<CodeGroup>
  ```json docs.json theme={null}
  "api": {
      "mdx": {
        "auth": {
          "method": "basic"
        }
      }
  }
  ```

  ```mdx Page Metadata theme={null}
  ---
  title: "Your page title"
  authMethod: "basic"
  ---
  ```
</CodeGroup>

### API key

<CodeGroup>
  ```json docs.json theme={null}
  "api": {
      "mdx": {
        "auth": {
          "method": "key",
          "name": "x-api-key"
        }
      }
  }
  ```

  ```mdx Page Metadata theme={null}
  ---
  title: "Your page title"
  authMethod: "key"
  ---
  ```
</CodeGroup>

### None

The "none" authentication method is useful to disable authentication on a specific endpoint after setting a default in docs.json.

<CodeGroup>
  ```mdx Page Metadata theme={null}
  ---
  title: "Your page title"
  authMethod: "none"
  ---
  ```
</CodeGroup>



# MDX setup
Source: https://mintlify.com/docs/api-playground/mdx/configuration

Generate docs pages for your API endpoints using `MDX`

You can manually define API endpoints in individual `MDX` files rather than using an OpenAPI specification. This method provides flexibility for custom content, but we recommend generating API documentation from an OpenAPI specification file for most projects because it is more maintainable and feature-rich. However, creating `MDX` pages for an API can be useful to document small APIs or for prototyping.

To generate pages for API endpoints using `MDX`, configure your API settings in `docs.json`, create individual `MDX` files for each endpoint, and use components like `<ParamFields />` to define parameters. From these definitions, Mintlify generates interactive API playgrounds, request examples, and response examples.

<Steps>
  <Step title="Configure your API">
    In your `docs.json` file, define your base URL and auth method:

    ```json  theme={null}
     "api": {
      "mdx": {
        "server": "https://mintlify.com/api", // string array for multiple base URLs
        "auth": {
          "method": "key",
          "name": "x-api-key" // options: bearer, basic, key.
        }
      }
    }
    ```

    If you want to hide the API playground, use the `display` field. You do not need to include an auth method if you hide the playground.

    ```json  theme={null}
    "api": {
      "playground": {
        "display": "none"
      }
    }
    ```

    Find a full list of API configurations in [Settings](/organize/settings#api-configurations).
  </Step>

  <Step title="Create your endpoint pages">
    Each API endpoint page should have a corresponding `MDX` file. At the top of each file, define `title` and `api`:

    ```mdx  theme={null}
    ---
    title: 'Create new user'
    api: 'POST https://api.mintlify.com/user'
    ---
    ```

    You can specify path parameters by adding the parameter name to the path, wrapped with `{}`:

    ```bash  theme={null}
    https://api.example.com/v1/endpoint/{userId}
    ```

    <Note>
      If you have a `server` field configured in `docs.json`, you can use relative paths like `/v1/endpoint`.
    </Note>

    You can override the globally-defined display mode for the API playground for a page by adding `playground` to the frontmatter:

    ```mdx  theme={null}
    ---
    title: 'Create new user'
    api: 'POST https://api.mintlify.com/user'
    playground: 'none'
    ---
    ```

    * `playground: 'interactive'` - Display the interactive playground.
    * `playground: 'simple'` - Display a copyable endpoint with no playground.
    * `playground: 'none'` - Hide the playground.
  </Step>

  <Step title="Add your endpoints to your docs">
    Add your endpoint pages to the sidebar by adding the paths to the `navigation` field in your `docs.json`. Learn more about structuring your docs in [Navigation](/organize/navigation).
  </Step>
</Steps>


## Enabling authentication

You can add an authentication method to your `docs.json` to enable it globally on every page or you can set it on a per-page basis.

A page's authentication method will override a global method if both are set.

### Bearer token

<CodeGroup>
  ```json docs.json theme={null}
  "api": {
      "mdx": {
        "auth": {
          "method": "bearer"
        }
      }
  }
  ```

  ```mdx Page Metadata theme={null}
  ---
  title: "Your page title"
  authMethod: "bearer"
  ---
  ```
</CodeGroup>

### Basic authentication

<CodeGroup>
  ```json docs.json theme={null}
  "api": {
      "mdx": {
        "auth": {
          "method": "basic"
        }
      }
  }
  ```

  ```mdx Page Metadata theme={null}
  ---
  title: "Your page title"
  authMethod: "basic"
  ---
  ```
</CodeGroup>

### API key

<CodeGroup>
  ```json docs.json theme={null}
  "api": {
      "mdx": {
        "auth": {
          "method": "key",
          "name": "x-api-key"
        }
      }
  }
  ```

  ```mdx Page Metadata theme={null}
  ---
  title: "Your page title"
  authMethod: "key"
  ---
  ```
</CodeGroup>

### None

The `none` authentication method is useful to disable authentication on a specific endpoint after setting a default in docs.json.

<CodeGroup>
  ```mdx Page Metadata theme={null}
  ---
  title: "Your page title"
  authMethod: "none"
  ---
  ```
</CodeGroup>



# Multiple responses
Source: https://mintlify.com/docs/api-playground/multiple-responses

Show response variations for the same endpoint

If your API returns different responses based on input parameters, user context, or other conditions of the request, you can document multiple response examples with the `examples` property.

This property can be added to any response and has the following schema.

```yaml  theme={null}
responses:
  "200":
    description: Successful response
    content:
      application/json:
        schema:
          $ref: "#/components/schemas/YourResponseSchema"
        examples:
          us:
            summary: Response for United States
            value:
              countryCode: "US"
              currencyCode: "USD"
              taxRate: 0.0825
          gb:
            summary: Response for United Kingdom
            value:
              countryCode: "GB"
              currencyCode: "GBP"
              taxRate: 0.20
```



# OpenAPI setup
Source: https://mintlify.com/docs/api-playground/openapi-setup

Reference OpenAPI endpoints in your docs pages

OpenAPI is a specification for describing APIs. Mintlify supports OpenAPI 3.0+ documents to generate interactive API documentation and keep it up to date.


## Add an OpenAPI specification file

To document your endpoints with OpenAPI, you need a valid OpenAPI document in either JSON or YAML format that follows the [OpenAPI specification 3.0+](https://swagger.io/specification/).

You can create API pages from a single or multiple OpenAPI documents.

### Describing your API

We recommend the following resources to learn about and construct your OpenAPI documents.

* [Swagger's OpenAPI Guide](https://swagger.io/docs/specification/v3_0/basic-structure/) to learn the OpenAPI syntax.
* [The OpenAPI specification Markdown sources](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/) to reference details of the latest OpenAPI specification.
* [Swagger Editor](https://editor.swagger.io/) to edit, validate, and debug your OpenAPI document.
* [The Mint CLI](https://www.npmjs.com/package/mint) to validate your OpenAPI document with the command: `mint openapi-check <openapiFilenameOrUrl>`.

<Note>
  Swagger's OpenAPI Guide is for OpenAPI v3.0, but nearly all of the information
  is applicable to v3.1. For more information on the differences between v3.0
  and v3.1, see [Migrating from OpenAPI 3.0 to
  3.1.0](https://www.openapis.org/blog/2021/02/16/migrating-from-openapi-3-0-to-3-1-0)
  in the OpenAPI blog.
</Note>

### Specifying the URL for your API

To enable Mintlify features like the API playground, add a `servers` field to your OpenAPI document with your API's base URL.

```json  theme={null}
{
  "servers": [
    {
      "url": "https://api.example.com/v1"
    }
  ]
}
```

In an OpenAPI document, different API endpoints are specified by their paths, like `/users/{id}` or simply `/`. The base URL defines where these paths should be appended. For more information on how to configure the `servers` field, see [API Server and Base Path](https://swagger.io/docs/specification/api-host-and-base-path/) in the OpenAPI documentation.

The API playground uses these server URLs to determine where to send requests. If you specify multiple servers, a dropdown will allow users to toggle between servers. If you do not specify a server, the API playground will use simple mode since it cannot send requests without a base URL.

If your API has endpoints that exist at different URLs, you can [override the server field](https://swagger.io/docs/specification/v3_0/api-host-and-base-path/#overriding-servers) for a given path or operation.

### Specifying authentication

To enable authentication in your API documentation and playground, configure the `securitySchemes` and `security` fields in your OpenAPI document. The API descriptions and API Playground will add authentication fields based on the security configurations in your OpenAPI document.

<Steps>
  <Step title="Define your authentication method.">
    Add a `securitySchemes` field to define how users authenticate.

    This example shows a configuration for bearer authentication.

    ```json  theme={null}
    {
      "components": {
        "securitySchemes": {
          "bearerAuth": {
            "type": "http",
            "scheme": "bearer"
          }
        }
      }
    }
    ```
  </Step>

  <Step title="Apply authentication to your endpoints.">
    Add a `security` field to require authentication.

    ```json  theme={null}
    {
      "security": [
        {
          "bearerAuth": []
        }
      ]
    }
    ```
  </Step>
</Steps>

Common authentication types include:

* [API Keys](https://swagger.io/docs/specification/authentication/api-keys/): For header, query, or cookie-based keys.
* [Bearer](https://swagger.io/docs/specification/authentication/bearer-authentication/): For JWT or OAuth tokens.
* [Basic](https://swagger.io/docs/specification/authentication/basic-authentication/): For username and password.

If different endpoints within your API require different methods of authentication, you can [override the security field](https://swagger.io/docs/specification/authentication/#:~:text=you%20can%20apply%20them%20to%20the%20whole%20API%20or%20individual%20operations%20by%20adding%20the%20security%20section%20on%20the%20root%20level%20or%20operation%20level%2C%20respectively.) for a given operation.

For more information on defining and applying authentication, see [Authentication](https://swagger.io/docs/specification/authentication/) in the OpenAPI documentation.


## `x-mint` extension

The `x-mint` extension is a custom OpenAPI extension that provides additional control over how your API documentation is generated and displayed.

### Metadata

Override the default metadata for generated API pages by adding `x-mint: metadata` to any operation. You can use any metadata field that would be valid in `MDX` frontmatter except for `openapi`:

```json {7-13} theme={null}
{
  "paths": {
    "/users": {
      "get": {
        "summary": "Get users",
        "description": "Retrieve a list of users",
        "x-mint": {
          "metadata": {
            "title": "List all users",
            "description": "Fetch paginated user data with filtering options",
            "og:title": "Display a list of users"
          }
        },
        "parameters": [
          {
            // Parameter configuration
          }
        ]
      }
    }
  }
}
```

### Content

Add content before the auto-generated API documentation using `x-mint: content`:

```json {6-8} theme={null}
{
  "paths": {
    "/users": {
      "post": {
        "summary": "Create user",
        "x-mint": {
          "content": "## Prerequisites\n\nThis endpoint requires admin privileges and has rate limiting.\n\n<Note>User emails must be unique across the system.</Note>"
        },
        "parameters": [
          {
            // Parameter configuration
          }
        ]
      }
    }
  }
}
```

The `content` extension supports all Mintlify MDX components and formatting.

### Href

Change the URL of the endpoint page in your docs using `x-mint: href`:

```json {6-8, 14-16} theme={null}
{
  "paths": {
    "/legacy-endpoint": {
      "get": {
        "summary": "Legacy endpoint",
        "x-mint": {
          "href": "/deprecated-endpoints/legacy-endpoint"
        }
      }
    },
    "/documented-elsewhere": {
      "post": {
        "summary": "Special endpoint",
        "x-mint": {
          "href": "/guides/special-endpoint-guide"
        }
      }
    }
  }
}
```

When `x-mint: href` is present, the navigation entry will link directly to the specified URL instead of generating an API page.

### MCP

Selectively expose endpoints as Model Context Protocol (MCP) tools by using `x-mint: mcp`. Only enable endpoints that are safe for public access through AI tools.

<ResponseField name="mcp" type="object">
  The MCP configuration for the endpoint.

  <Expandable title="MCP">
    <ResponseField name="enabled" type="boolean">
      Whether to expose the endpoint as an MCP tool. Takes precedence over the file-level configuration.
    </ResponseField>

    <ResponseField name="name" type="string">
      The name of the MCP tool.
    </ResponseField>

    <ResponseField name="description" type="string">
      The description of the MCP tool.
    </ResponseField>
  </Expandable>
</ResponseField>

<CodeGroup>
  ```json Selective enablement {6-9} wrap theme={null}
  {
    "paths": {
      "/users": {
        "post": {
          "summary": "Create user",
          "x-mint": {
            "mcp": {
              "enabled": true
            },
            // ...
          }
        }
      },
      "/users": {
        "delete": {
          "summary": "Delete user (admin only)",
          // No `x-mint: mcp` so this endpoint is not exposed as an MCP tool
          // ...
        }
      }
    }
  }
  ```

  ```json Global enablement {3-5, 9-13} wrap theme={null}
  {
    "openapi": "3.1.0",
    "x-mcp": {
        "enabled": true // All endpoints are exposed as MCP tools by default
      },
    "paths": {
      "/api/admin/delete": {
        "delete": {
          "x-mint": {
            "mcp": {
              "enabled": false // Disable MCP for this endpoint
            }
          },
          "summary": "Delete resources"
        }
      }
    }
  }
  ```
</CodeGroup>

For more information, see [Model Context Protocol](/ai/model-context-protocol).


## Auto-populate API pages

Add an `openapi` field to any navigation element in your `docs.json` to automatically generate pages for OpenAPI endpoints. You can control where these pages appear in your navigation structure, as dedicated API sections or with other pages.

The `openapi` field accepts either a file path in your docs repo or a URL to a hosted OpenAPI document.

Generated endpoint pages have these default metadata values:

* `title`: The operation's `summary` field, if present. If there is no `summary`, the title is generated from the HTTP method and endpoint.
* `description`: The operation's `description` field, if present.
* `version`: The `version` value from the parent anchor or tab, if present.
* `deprecated`: The operation's `deprecated` field. If `true`, a deprecated label will appear next to the endpoint title in the side navigation and on the endpoint page.

<Tip>
  To exclude specific endpoints from your auto-generated API pages, add the
  [x-hidden](/api-playground/managing-page-visibility#x-hidden)
  property to the operation in your OpenAPI spec.
</Tip>

There are two approaches for adding endpoint pages into your documentation:

1. **Dedicated API sections**: Reference OpenAPI specs in navigation elements for dedicated API sections.
2. **Selective endpoints**: Reference specific endpoints in your navigation alongside other pages.

### Dedicated API sections

Generate dedicated API sections by adding an `openapi` field to a navigation element and no other pages. All endpoints in the specification will be included:

```json {5} theme={null}
"navigation": {
  "tabs": [
    {
        "tab": "API Reference",
        "openapi": "https://petstore3.swagger.io/api/v3/openapi.json"
    }
  ]
}
```

You can use multiple OpenAPI specifications in different navigation sections:

```json {8-11, 15-18} theme={null}
"navigation": {
  "tabs": [
    {
      "tab": "API Reference",
      "groups": [
        {
          "group": "Users",
          "openapi": {
            "source": "/path/to/openapi-1.json",
            "directory": "api-reference"
          }
        },
        {
          "group": "Admin",
          "openapi": {
            "source": "/path/to/openapi-2.json",
            "directory": "api-reference"
          }
        }
      ]
    }
  ]
}
```

<Note>
  The `directory` field is optional and specifies where generated API pages are
  stored in your docs repo. If not specified, defaults to the `api-reference`
  directory of your repo.
</Note>

### Selective endpoints

When you want more control over where endpoints appear in your documentation, you can reference specific endpoints in your navigation. This approach allows you to generate pages for API endpoints alongside other content.

#### Set a default OpenAPI spec

Configure a default OpenAPI specification for a navigation element. Then reference specific endpoints in the `pages` field:

```json {12, 15-16} theme={null}
"navigation": {
  "tabs": [
    {
      "tab": "Getting started",
      "pages": [
        "quickstart",
        "installation"
      ]
    },
    {
      "tab": "API reference",
      "openapi": "/path/to/openapi.json",
      "pages": [
        "api-overview",
        "GET /users",
        "POST /users",
        "guides/authentication"
      ]
    }
  ]
}
```

Any page entry matching the format `METHOD /path` will generate an API page for that endpoint using the default OpenAPI spec.

#### OpenAPI spec inheritance

OpenAPI specifications are inherited down the navigation hierarchy. Child navigation elements inherit their parent's OpenAPI specification unless they define their own:

```json {3, 7-8, 11, 13-14} theme={null}
{
  "group": "API reference",
  "openapi": "/path/to/openapi-v1.json",
  "pages": [
    "overview",
    "authentication",
    "GET /users",
    "POST /users",
    {
      "group": "Orders",
      "openapi": "/path/to/openapi-v2.json",
      "pages": [
        "GET /orders",
        "POST /orders"
      ]
    }
  ]
}
```

#### Individual endpoints

Reference specific endpoints without setting a default OpenAPI specification by including the file path:

```json {5-6} theme={null}
"navigation": {
  "pages": [
    "introduction",
    "user-guides",
    "/path/to/openapi-v1.json POST /users",
    "/path/to/openapi-v2.json GET /orders"
  ]
}
```

This approach is useful when you need individual endpoints from different specs or only want to include select endpoints.


## Create `MDX` files for API pages

For control over individual endpoint pages, create `MDX` pages for each operation. This lets you customize page metadata, add content, omit certain operations, or reorder pages in your navigation at the page level.

See an [example MDX OpenAPI page from MindsDB](https://github.com/mindsdb/mindsdb/blob/main/docs/rest/databases/create-databases.mdx?plain=1) and how it appears in their [live documentation](https://docs.mindsdb.com/rest/databases/create-databases).

### Manually specify files

Create an `MDX` page for each endpoint and specify which OpenAPI operation to display using the `openapi` field in the frontmatter.

When you reference an OpenAPI operation this way, the name, description, parameters, responses, and API playground are automatically generated from your OpenAPI document.

If you have multiple OpenAPI files, include the file path in your reference to ensure Mintlify finds the correct OpenAPI document. If you have only one OpenAPI file, Mintlify will detect it automatically.

<Note>
  This approach works regardless of whether you have set a default OpenAPI spec
  in your navigation. You can reference any endpoint from any OpenAPI spec by
  including the file path in the frontmatter.
</Note>

If you want to reference an external OpenAPI file, add the file's URL to your `docs.json`.

<CodeGroup>
  ```mdx Example theme={null}
  ---
  title: "Get users"
  description: "Returns all plants from the system that the user has access to"
  openapi: "/path/to/openapi-1.json GET /users"
  deprecated: true
  version: "1.0"
  ---
  ```

  ```mdx Format theme={null}
  ---
  title: "title of the page"
  description: "description of the page"
  openapi: openapi-file-path method path
  deprecated: boolean (not required)
  version: "version-string" (not required)
  ---
  ```
</CodeGroup>

<Note>
  The method and path must exactly match the definition in your OpenAPI
  specification. If the endpoint doesn't exist in the OpenAPI file, the page
  will be empty.
</Note>

### Autogenerate `MDX` files

Use our Mintlify [scraper](https://www.npmjs.com/package/@mintlify/scraping) to autogenerate `MDX` pages for large OpenAPI documents.

<Note>
  Your OpenAPI document must be valid or the files will not autogenerate.
</Note>

The scraper generates:

* An `MDX` page for each operation in the `paths` field of your OpenAPI document.
* If your OpenAPI document is version 3.1+, an `MDX` page for each operation in the `webhooks` field of your OpenAPI document.
* An array of navigation entries that you can add to your `docs.json`.

<Steps>
  <Step title="Generate `MDX` files.">
    ```bash  theme={null}
    npx @mintlify/scraping@latest openapi-file <path-to-openapi-file>
    ```
  </Step>

  <Step title="Specify an output folder.">
    ```bash  theme={null}
    npx @mintlify/scraping@latest openapi-file <path-to-openapi-file> -o api-reference
    ```

    Add the `-o` flag to specify a folder to populate the files into. If a folder is not specified, the files will populate in the working directory.
  </Step>
</Steps>

### Create `MDX` files for OpenAPI schemas

You can create individual pages for any OpenAPI schema defined in an OpenAPI document's `components.schemas` field:

<CodeGroup>
  ```mdx Example theme={null}
  ---
  openapi-schema: OrderItem
  ---
  ```

  ```mdx Format theme={null}
  ---
  openapi-schema: "schema-key"
  ---
  ```
</CodeGroup>

If you have schemas with the same name in multiple files, you can also specify the OpenAPI file:

<CodeGroup>
  ```mdx Example theme={null}
  ---
  openapi-schema: en-schema.json OrderItem
  ---
  ```

  ```mdx Format theme={null}
  ---
  openapi-schema: "path-to-schema-file schema-key"
  ---
  ```
</CodeGroup>


## Webhooks

Webhooks are HTTP callbacks that your API sends to notify external systems when events occur. Webhooks are supported in OpenAPI 3.1+ documents.

### Define webhooks in your OpenAPI specification

Add a `webhooks` field to your OpenAPI document alongside the `paths` field.

For more information on defining webhooks, see [Webhooks](https://spec.openapis.org/oas/v3.1.0#oasWebhooks) in the OpenAPI documentation.

### Reference webhooks in MDX files

When creating MDX pages for webhooks, use `webhook` instead of HTTP methods like `GET` or `POST`:

```mdx  theme={null}
---
title: "Example webhook"
description: "Triggered when an event occurs"
openapi: "path/to/openapi-file webhook example-webhook-name"
---
```

<Note>
  The webhook name must exactly match the key defined in your OpenAPI
  specification's `webhooks` field.
</Note>



# Playground
Source: https://mintlify.com/docs/api-playground/overview

Enable users to interact with your API


## Overview

The API playground is an interactive environment that lets users test and explore your API endpoints. Developers can craft API requests, submit them, and view responses without leaving your documentation.

<Frame>
  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-light.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=f83551b5d84cf27a44ed1d9418ca61be" alt="API playground for the trigger an update endpoint." className="block dark:hidden" data-og-width="2534" width="2534" data-og-height="1022" height="1022" data-path="images/playground/API-playground-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-light.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=87a778f73c13b231ae61b3b3e4ead063 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-light.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=fb0ce88ecd599c819dd780738b87c24d 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-light.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e7cf7572fa5fcd7205c8ebcfda839f64 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-light.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=81337643c958f66b3962e16ac569afcd 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-light.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=94ab7ee928898ec25390934c8897a867 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-light.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=440d9f8a2d8dcbbf55d665d20e6408ed 2500w" />

  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-dark.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=5a0dc3fd3ca0a5766c599c00a5910dba" alt="API playground for the trigger an update endpoint." className="hidden dark:block" data-og-width="2534" width="2534" data-og-height="1022" height="1022" data-path="images/playground/API-playground-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-dark.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e3ffd7bdd28940bc42bff50ffac5b169 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-dark.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=fdf601c84aeb05836c8e711722fbd2ee 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-dark.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=45b0f029d05636ca86b99b4d1590ddb3 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-dark.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=5e7389355d83faf84d9625c84396868f 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-dark.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=f826d034daefdb906bed0ed0ac6b668e 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/playground/API-playground-dark.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=a530b0340d9ad9a29b72a164fc7dabe5 2500w" />
</Frame>

The playground is automatically generated from your OpenAPI specification or AsyncAPI schema so any updates to your API are automatically reflected in the playground. You can also manually create API reference pages after defining a base URL and authentication method in your `docs.json`.

We recommend generating your API playground from an OpenAPI specification. See [OpenAPI Setup](/api-playground/openapi-setup) for more information on creating your OpenAPI document.


## Getting started

<Steps>
  <Step title="Add your OpenAPI specification file.">
    <Info>
      Make sure that your OpenAPI specification file is valid using the [Swagger Editor](https://editor.swagger.io/) or [Mint CLI](https://www.npmjs.com/package/mint).
    </Info>

    ```bash {3} theme={null}
    /your-project
      |- docs.json
      |- openapi.json
    ```
  </Step>

  <Step title="Configure `docs.json`.">
    Update your `docs.json` to reference your OpenAPI specification. Add an `openapi` property to any navigation element to auto-populate your docs with pages for each endpoint specified in your OpenAPI document.

    This example generates a page for each endpoint specified in `openapi.json` and organize them under the "API reference" group in your navigation.

    ```json  theme={null}
    "navigation": {
      "groups": [
        {
          "group": "API reference",
          "openapi": "openapi.json"
        }
      ]
    }
    ```

    To generate pages for only specific endpoints, list the endpoints in the `pages` property of the navigation element.

    This example generates pages for only the `GET /users` and `POST /users` endpoints. To generate other endpoint pages, add additional endpoints to the `pages` array.

    ```json  theme={null}
    "navigation": {
      "groups": [
          {
            "group": "API reference",
            "openapi": "openapi.json",
            "pages": [
              "GET /users",
              "POST /users"
            ]
          }
      ]
    }
    ```
  </Step>
</Steps>


## Customizing your playground

You can customize your API playground by defining the following properties in your `docs.json`.

<ResponseField name="playground" type="object">
  Configurations for the API playground.

  <Expandable title="playground" defaultOpen="True">
    <ResponseField name="display" type="&#x22;interactive&#x22; | &#x22;simple&#x22; | &#x22;none&#x22;">
      The display mode of the API playground.

      * `"interactive"`: Display the interactive playground.
      * `"simple"`: Display a copyable endpoint with no playground.
      * `"none"`: Display nothing.

      Defaults to `interactive`.
    </ResponseField>

    <ResponseField name="proxy" type="boolean" defaultOpen="True">
      Whether to pass API requests through a proxy server. Defaults to `true`.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="examples" type="object">
  Configurations for the autogenerated API examples.

  <Expandable title="examples" defaultOpen="True">
    <ResponseField name="languages" type="array of string">
      Example languages for the autogenerated API snippets.

      Languages display in the order specified.
    </ResponseField>

    <ResponseField name="defaults" type="&#x22;required&#x22; | &#x22;all&#x22;">
      Whether to show optional parameters in API examples. Defaults to `all`.
    </ResponseField>

    <ResponseField name="prefill" type="boolean">
      Whether to prefill the API playground with data from schema examples. When enabled, the playground automatically populates request fields with example values from your OpenAPI specification. Defaults to `false`.
    </ResponseField>
  </Expandable>
</ResponseField>

### Example configuration

```json  theme={null}
{
 "api": {
   "playground": {
     "display": "interactive"
   },
   "examples": {
     "languages": ["curl", "python", "javascript"],
     "defaults": "required",
     "prefill": true
   }
 }
}
```

This example configures the API playground to be interactive with example code snippets for cURL, Python, and JavaScript. Only required parameters are shown in the code snippets, and the playground prefills the request body with example values.

### Custom endpoint pages

When you need more control over your API documentation, use the `x-mint` extension in your OpenAPI specification or create individual `MDX` pages for your endpoints.

Both options allow you to:

* Customize page metadata
* Add additional content like examples
* Control playground behavior per page

The `x-mint` extension is recommended so that all of your API documentation is automatically generated from your OpenAPI specification and maintained in one file.

Individual `MDX` pages are recommended for small APIs or when you want to experiment with changes on a per-page basis.

For more information, see [x-mint extension](/api-playground/openapi-setup#x-mint-extension) and [MDX Setup](/api-playground/mdx/configuration).


## Further reading

* [AsyncAPI Setup](/api-playground/asyncapi/setup) for more information on creating your AsyncAPI schema to generate WebSocket reference pages.



# Troubleshooting
Source: https://mintlify.com/docs/api-playground/troubleshooting

Common issues with API References

If your API pages aren't displaying correctly, check these common configuration issues:

<AccordionGroup>
  <Accordion title="All of my OpenAPI pages are completely blank">
    In this scenario, it's likely that either Mintlify cannot find your OpenAPI document,
    or your OpenAPI document is invalid.

    Running `mint dev` locally should reveal some of these issues.

    To verify your OpenAPI document will pass validation:

    1. Visit [this validator](https://editor.swagger.io/)
    2. Switch to the "Validate text" tab
    3. Paste in your OpenAPI document
    4. Click "Validate it!"

    If the text box that appears below has a green border, your document has passed validation.
    This is the exact validation package Mintlify uses to validate OpenAPI documents, so if your document
    passes validation here, there's a great chance the problem is elsewhere.

    Additionally, Mintlify does not support OpenAPI 2.0. If your document uses this version of the specification,
    you could encounter this issue. You can convert your document at [editor.swagger.io](https://editor.swagger.io/) (under Edit > Convert to OpenAPI 3):

    <Frame>
            <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/convert-oas-3.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3a45e89b8847e632d20b0ae9b3b5d689" alt="Screenshot of the Swagger Editor with the Edit menu expanded and the &#x22;Convert to OpenAPI 3&#x22; menu item highlighted." data-og-width="1454" width="1454" data-og-height="592" height="592" data-path="images/convert-oas-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/convert-oas-3.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=d70f54b55ffb02814cd1669f13adcc6a 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/convert-oas-3.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b77ae4b1a8f4cfea8fefa8a095e63845 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/convert-oas-3.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=081b2f5f2597709a7c261dc590192c78 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/convert-oas-3.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1a22f178270fdafd548a22139b09fb05 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/convert-oas-3.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1560b49e5d0197e873181f13c920486a 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/convert-oas-3.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=dcb5e1911ab293b36a911b2303ce5e0c 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="One of my OpenAPI pages is completely blank">
    This is usually caused by a misspelled `openapi` field in the page metadata. Make sure
    the HTTP method and path match the HTTP method and path in the OpenAPI document exactly.

    Here's an example of how things might go wrong:

    ```mdx get-user.mdx theme={null}
    ---
    openapi: "GET /users/{id}/"
    ---
    ```

    ```yaml openapi.yaml theme={null}
    paths:
      "/users/{id}":
        get: ...
    ```

    Notice that the path in the `openapi` field has a trailing slash, whereas the path in the OpenAPI
    document does not.

    Another common issue is a misspelled filename. If you are specifying a particular OpenAPI document
    in the `openapi` field, ensure the filename is correct. For example, if you have two OpenAPI
    documents `openapi/v1.json` and `openapi/v2.json`, your metadata might look like this:

    ```mdx api-reference/v1/users/get-user.mdx theme={null}
    ---
    openapi: "v1 GET /users/{id}"
    ---
    ```
  </Accordion>

  <Accordion title="Requests from the API Playground don't work">
    If you have a custom domain configured, this could be an issue with your reverse proxy. By
    default, requests made via the API Playground start with a `POST` request to the
    `/_mintlify/api/request` path on the docs site. If your reverse proxy is configured to only allow `GET`
    requests, then all of these requests will fail. To fix this, configure your reverse proxy to
    allow `POST` requests to the `/_mintlify/api/request` path.

    Alternatively, if your reverse proxy prevents you from accepting `POST` requests, you can configure Mintlify to send requests directly to your backend with the `api.playground.proxy` setting in the `docs.json`, as described in the [settings documentation](/organize/settings#param-proxy). When using this configuration, you will need to configure CORS on your server since requests will come directly from users' browsers rather than through your proxy.
  </Accordion>

  <Accordion title="OpenAPI navigation entries are not generating pages">
    If you are using an OpenAPI navigation configuration, but the pages aren't generating, check these common issues:

    1. **Missing default OpenAPI spec**: Ensure you have an `openapi` field set for the navigation element:

    ```json {5} theme={null}
    "navigation": {
      "groups": [
        {
          "group": "API reference",
          "openapi": "/path/to/openapi.json",
          "pages": [
            "GET /users",
            "POST /users"
          ]
        }
      ]
    }
    ```

    2. **OpenAPI spec inheritance**: If using nested navigation, ensure child groups inherit the correct OpenAPI spec or specify their own.

    3. **Validation issues**: Use `mint openapi-check <path-to-openapi-file>` to verify your OpenAPI document is valid.
  </Accordion>

  <Accordion title="Some OpenAPI operations appear in navigation but others don't">
    1. **Hidden operations**: Operations marked with `x-hidden: true` in your OpenAPI spec won't appear in auto-generated navigation.
    2. **Invalid operations**: Operations with validation errors in the OpenAPI spec may be skipped. Check your OpenAPI document for syntax errors.
    3. **Manual vs automatic inclusion**: If you reference any endpoints from an OpenAPI spec, only the explicitly referenced operations will appear in navigation. No other pages will be automatically added. This includes operations that are referenced in child navigation elements.
  </Accordion>

  <Accordion title="Mixed navigation (OpenAPI and MDX pages) not working correctly">
    When combining OpenAPI operations with regular documentation pages in navigation:

    1. **File conflicts**: You cannot have both an `MDX` file and a navigation entry for the same operation. For example, if you have `get-users.mdx`, do not also include `"GET /users"` in your navigation.  If you need to have a file that shares a name with an operation, use the `x-mint` extension for the endpoint to have the href point to a different location.
    2. **Path resolution**: Navigation entries that don't match OpenAPI operations will be treated as file paths. Ensure your `MDX` files exist at the expected locations.
    3. **Case sensitivity**: OpenAPI operation matching is case-sensitive. Ensure HTTP methods are uppercase in navigation entries.
  </Accordion>
</AccordionGroup>



# Accordions
Source: https://mintlify.com/docs/components/accordions

Collapsible components to show and hide content

Accordions allow users to expand and collapse content sections. Use accordions for progressive disclosure and to organize information.


## Single accordion

<Accordion title="I am an Accordion.">
  You can put any content in here, including other components, like code:

  ```java HelloWorld.java theme={null}
   class HelloWorld {
       public static void main(String[] args) {
           System.out.println("Hello, World!");
       }
   }
  ```
</Accordion>

````mdx Accordion example theme={null}
<Accordion title="I am an Accordion.">
  You can put any content in here, including other components, like code:

   ```java HelloWorld.java
    class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello, World!");
        }
    }
  ```
</Accordion>
````


## Accordion Groups

Group related accordions together using `<AccordionGroup>`. This creates a cohesive section of accordions that can be individually expanded or collapsed.

<AccordionGroup>
  <Accordion title="Getting started">
    You can put other components inside Accordions.

    ```java HelloWorld.java theme={null}
    class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello, World!");
        }
    }
    ```
  </Accordion>

  <Accordion title="Advanced features" icon="bot">
    Add icons to make accordions more visually distinct and scannable.
  </Accordion>

  <Accordion title="Troubleshooting">
    Keep related content organized into groups.
  </Accordion>
</AccordionGroup>

````mdx Accordion Group Example theme={null}
<AccordionGroup>
  <Accordion title="Getting started">
    You can put other components inside Accordions.

    ```java HelloWorld.java
    class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello, World!");
        }
    }
    ```
  </Accordion>

  <Accordion title="Advanced features" icon="alien-8bit">
    Add icons to make accordions more visually distinct and scannable.
  </Accordion>

  <Accordion title="Troubleshooting">
    Keep related content organized into groups.
  </Accordion>
</AccordionGroup>
````


## Properties

<ResponseField name="title" type="string" required>
  Title in the Accordion preview.
</ResponseField>

<ResponseField name="description" type="string">
  Detail below the title in the Accordion preview.
</ResponseField>

<ResponseField name="defaultOpen" type="boolean" default="false">
  Whether the Accordion is open by default.
</ResponseField>

<ResponseField name="icon" type="string">
  The icon to display.

  Options:

  * [Font Awesome icon](https://fontawesome.com/icons) name
  * [Lucide icon](https://lucide.dev/icons) name
  * JSX-compatible SVG code wrapped in curly braces
  * URL to an externally hosted icon
  * Path to an icon file in your project

  For custom SVG icons:

  1. Convert your SVG using the [SVGR converter](https://react-svgr.com/playground/).
  2. Paste your SVG code into the SVG input field.
  3. Copy the complete `<svg>...</svg>` element from the JSX output field.
  4. Wrap the JSX-compatible SVG code in curly braces: `icon={<svg ...> ... </svg>}`.
  5. Adjust `height` and `width` as needed.
</ResponseField>

<ResponseField name="iconType" type="string">
  The [Font Awesome](https://fontawesome.com/icons) icon style. Only used with Font Awesome icons.

  Options: `regular`, `solid`, `light`, `thin`, `sharp-solid`, `duotone`, `brands`.
</ResponseField>



# Banner
Source: https://mintlify.com/docs/components/banner

Add a banner to display important site-wide announcements and notifications

Use banners to display important announcements, updates, or notifications across your entire documentation site. Banners appear at the top of every page, support Markdown formatting, and can be made dismissible. Banners use the color defined by the `colors.dark` property in your `docs.json`.

To add a banner, use the `banner` property in your `docs.json`:

<CodeGroup>
  ```json Product announcements wrap theme={null}
  "banner": {
    "content": "🚀 Version 2.0 is now live! See our [changelog](/changelog) for details.",
    "dismissible": true 
  }
  ```

  ```json Maintenance notices wrap theme={null}
  "banner": {
    "content": "⚠️ Scheduled maintenance: API will be unavailable December 15, 2-4 AM UTC",
    "dismissible": false
  }
  ```

  ```json Required actions wrap theme={null}
  "banner": {
    "content": "**Action required:** Migrate to our new version by January 1. [Migration guide](/migration)",
    "dismissible": true
  }
  ```
</CodeGroup>


## Properties

<ResponseField name="content" type="string" required>
  The banner message. Supports plain text and Markdown formatting.
</ResponseField>

<ResponseField name="dismissible" type="boolean">
  Whether users can dismiss the banner. When `true`, users can close the banner and it won't reappear for their session. Defaults to `false`.
</ResponseField>



# Callouts
Source: https://mintlify.com/docs/components/callouts

Use callouts to add eye-catching context to your content

Callouts can be styled as a Note, Warning, Info, Tip, Check, Danger, or create your own callout:

<Note>This adds a note in the content</Note>

```mdx  theme={null}
<Note>This adds a note in the content</Note>
```

<Warning>This raises a warning to watch out for</Warning>

```mdx  theme={null}
<Warning>This raises a warning to watch out for</Warning>
```

<Info>This draws attention to important information</Info>

```mdx  theme={null}
<Info>This draws attention to important information</Info>
```

<Tip>This suggests a helpful tip</Tip>

```mdx  theme={null}
<Tip>This suggests a helpful tip</Tip>
```

<Check>This brings us a checked status</Check>

```mdx  theme={null}
<Check>This brings us a checked status</Check>
```

<Danger>This is a danger callout</Danger>

```mdx  theme={null}
<Danger>This is a danger callout</Danger>
```

<Callout icon="key" color="#FFC107" iconType="regular"> This is a custom callout</Callout>

```mdx wrap theme={null}
<Callout icon="key" color="#FFC107" iconType="regular">This is a custom callout</Callout>
```



# Cards
Source: https://mintlify.com/docs/components/cards

Highlight main points or links with customizable layouts and icons

Use cards to create visual containers for content. Cards are flexible containers that can include text, icons, images, and links.


## Basic card

<Card title="Card title" icon="text" href="/components/columns">
  This is how you use a card with an icon and a link. Clicking on this card
  brings you to the Columns page.
</Card>

```mdx Card example theme={null}
<Card title="Card title" icon="text" href="/components/columns">
  This is how you use a card with an icon and a link. Clicking on this card
  brings you to the Columns page.
</Card>
```


## Card variations

Cards support several layout and styling options to fit different content needs.

### Horizontal layout

Add the `horizontal` property to display cards in a more compact, horizontal layout.

<Card title="Horizontal card" icon="text" horizontal>
  This is an example of a horizontal card.
</Card>

```mdx Horizontal card example theme={null}
<Card title="Horizontal card" icon="text" horizontal>
  This is an example of a horizontal card.
</Card>
```

### Image cards

Add an `img` property to display an image at the top of the card.

<Card title="Image card" img="https://mintlify-assets.b-cdn.net/yosemite.jpg">
  This is an example of a card with an image.
</Card>

```mdx Image card example theme={null}
<Card title="Image card" img="/images/card-with-image.png">
  This is an example of a card with an image.
</Card>
```

### Link cards with custom CTAs

You can customize the call-to-action text and control whether an arrow appears. By default, arrows only show for external links.

<Card title="Link card" icon="link" href="/components/columns" arrow="true" cta="Click here">
  This is an example of a card with an icon and a link. Clicking on this card brings you to the Columns page.
</Card>

```mdx Link card example theme={null}
<Card
  title="Link card"
  icon="link"
  href="/components/columns"
  arrow="true"
  cta="Click here"
>
  This is an example of a card with an icon and a link. Clicking on this card brings you to the Columns page.
</Card>
```


## Grouping cards

Use the [Columns component](/components/columns) to organize multiple cards side by side.

<Columns cols={2}>
  <Card title="First card" icon="panel-left-close">
    This is the first card.
  </Card>

  <Card title="Second card" icon="panel-right-close">
    This is the second card.
  </Card>
</Columns>

```mdx Columns example theme={null}
<Columns cols={2}>
  <Card title="First card" icon="panel-left-close">
    This is the first card.
  </Card>
  <Card title="Second card" icon="panel-right-close">
    This is the second card.
  </Card>
</Columns>
```


## Properties

<ResponseField name="title" type="string" required>
  The title displayed on the card
</ResponseField>

<ResponseField name="icon" type="string">
  The icon to display.

  Options:

  * [Font Awesome icon](https://fontawesome.com/icons) name
  * [Lucide icon](https://lucide.dev/icons) name
  * JSX-compatible SVG code wrapped in curly braces
  * URL to an externally hosted icon
  * Path to an icon file in your project

  For custom SVG icons:

  1. Convert your SVG using the [SVGR converter](https://react-svgr.com/playground/).
  2. Paste your SVG code into the SVG input field.
  3. Copy the complete `<svg>...</svg>` element from the JSX output field.
  4. Wrap the JSX-compatible SVG code in curly braces: `icon={<svg ...> ... </svg>}`.
  5. Adjust `height` and `width` as needed.
</ResponseField>

<ResponseField name="iconType" type="string">
  The [Font Awesome](https://fontawesome.com/icons) icon style. Only used with Font Awesome icons.

  Options: `regular`, `solid`, `light`, `thin`, `sharp-solid`, `duotone`, `brands`.
</ResponseField>

<ResponseField name="color" type="string">
  Icon color as a hex code (for example, `#FF6B6B`).
</ResponseField>

<ResponseField name="href" type="string">
  URL to navigate to when the card is clicked.
</ResponseField>

<ResponseField name="horizontal" type="boolean">
  Display the card in a compact horizontal layout.
</ResponseField>

<ResponseField name="img" type="string">
  URL or local path to an image displayed at the top of the card.
</ResponseField>

<ResponseField name="cta" type="string">
  Custom text for the action button.
</ResponseField>

<ResponseField name="arrow" type="boolean">
  Show or hide the link arrow icon.
</ResponseField>



# Code groups
Source: https://mintlify.com/docs/components/code-groups

Display multiple code examples in one component

Use the `CodeGroup` component to display multiple code blocks in a tabbed interface, allowing users to compare implementations across different programming languages or see alternative approaches for the same task.

<CodeGroup>
  ```javascript helloWorld.js theme={null}
  console.log("Hello World");
  ```

  ```python hello_world.py theme={null}
  print('Hello World!')
  ```

  ```java HelloWorld.java theme={null}
  class HelloWorld {
      public static void main(String[] args) {
          System.out.println("Hello, World!");
      }
  }
  ```
</CodeGroup>

Code groups inherit global styling from your `docs.json` file. Customize your theme using `styling.codeblocks`. See [Settings](/organize/settings#styling) for configuration options.


## Creating code groups

To create a code group, wrap multiple code blocks with `<CodeGroup>` tags. Each code block must include a title, which becomes the tab label.

````mdx  theme={null}
<CodeGroup>

```javascript helloWorld.js
console.log("Hello World");
```

```python hello_world.py
print('Hello World!')
```

```java HelloWorld.java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

</CodeGroup>
````


## Language dropdown

You can replace the tabs in a code group with a dropdown menu to toggle between languages using the `dropdown` prop.

<CodeGroup dropdown>
  ```javascript helloWorld.js theme={null}
  console.log("Hello World");
  ```

  ```python hello_world.py theme={null}
  print('Hello World!')
  ```

  ```java HelloWorld.java theme={null}
  class HelloWorld {
      public static void main(String[] args) {
          System.out.println("Hello, World!");
      }
  }
  ```
</CodeGroup>

````mdx highlight=1 theme={null}
<CodeGroup dropdown>

```javascript helloWorld.js
console.log("Hello World");
```

```python hello_world.py
print('Hello World!')
```

```java HelloWorld.java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```
</CodeGroup>
````



# Columns
Source: https://mintlify.com/docs/components/columns

Show cards side by side in a grid format

The `Columns` component lets you group multiple `Card` components together. It's most often used to put cards in a grid, by specifying the number of grid columns.

<Columns cols={2}>
  <Card title="Get started" icon="rocket">
    Set up your project with our quickstart guide.
  </Card>

  <Card title="API reference" icon="code">
    Explore endpoints, parameters, and examples for your API.
  </Card>
</Columns>

```mdx Columns example theme={null}
<Columns cols={2}>
  <Card title="Get started">
    Set up your project with our quickstart guide.
  </Card>
  <Card title="API reference">
    Explore endpoints, parameters, and examples for your API.
  </Card>
</Columns>
```


## Properties

<ResponseField name="cols" default={2}>
  The number of columns per row.
</ResponseField>



# Examples
Source: https://mintlify.com/docs/components/examples

Display code blocks in the right sidebar on desktop devices

The `<RequestExample>` and `<ResponseExample>` components display code blocks in the right sidebar to create a two-column layout that keeps examples visible while users scroll through your content. These components are designed for API documentation, but they work on all pages.

Common use cases:

* API endpoint documentation with request and response examples
* Configuration examples alongside explanatory text
* Code samples that users reference while following instructions
* Before and after examples in tutorials

On mobile devices, `<RequestExample>` and `<ResponseExample>` components display as regular code blocks and can be scrolled past.

<RequestExample>
  ```bash Request theme={null}
    curl --request POST \
      --url https://dog-api.kinduff.com/api/facts
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  { "status": "success" }
  ```
</ResponseExample>


## RequestExample

Use `<RequestExample>` to pins code examples in the right sidebar. This component works similarly to the [CodeGroup](/components/code-groups) component, but displays the code in the sidebar instead of inline.

You can include multiple code blocks inside a single `<RequestExample>`. Each code block must have a title attribute.

````mdx RequestExample theme={null}
<RequestExample>

```bash Request
  curl --request POST \
    --url https://dog-api.kinduff.com/api/facts
```

</RequestExample>
````


## ResponseExample

The `<ResponseExample>` component pins code examples in the right sidebar beneath any `<RequestExample>` content on the same page.

````mdx ResponseExample theme={null}
<ResponseExample>

```json Response
{ "status": "success" }
```

</ResponseExample>
````



# Expandables
Source: https://mintlify.com/docs/components/expandables

Toggle to display nested properties

Use expandables to show and hide nested content within response fields. Expandables are particularly useful for displaying complex object properties in API documentation.

<ResponseField name="user" type="User Object">
  <Expandable title="properties">
    <ResponseField name="full_name" type="string">
      The full name of the user
    </ResponseField>

    <ResponseField name="is_over_21" type="boolean">
      Whether the user is over 21 years old
    </ResponseField>
  </Expandable>
</ResponseField>

```mdx Expandable example theme={null}
<ResponseField name="user" type="User Object">
  <Expandable title="properties">
    <ResponseField name="full_name" type="string">
      The full name of the user
    </ResponseField>

    <ResponseField name="is_over_21" type="boolean">
      Whether the user is over 21 years old
    </ResponseField>
  </Expandable>
</ResponseField>
```


## Properties

<ResponseField name="title" type="string">
  The name of the object you are showing.
</ResponseField>

<ResponseField name="defaultOpen" type="boolean" default="false">
  Set to `true` for the expandable to open when the page loads
</ResponseField>



# Fields
Source: https://mintlify.com/docs/components/fields

Set parameters for your API or SDK references

Use fields to document API parameters and responses. There are two types of fields: parameter fields and response fields.


## Parameter field

The `<ParamField>` component is used to define parameters for your APIs or SDKs. Adding a `ParamField` automatically adds an [API Playground](/api-playground/overview).

<ParamField path="param" type="string" required>
  An example of a parameter field
</ParamField>

```mdx  theme={null}
<ParamField path="param" type="string" required>
  An example of a parameter field
</ParamField>
```

### Properties

<ParamField body="query, path, body, or header" type="string">
  Whether the parameter is a query, path, body, or header. Followed by the
  parameter name.
</ParamField>

<ParamField body="type" type="string">
  Expected type of the parameter's value.

  Supports `number`, `string`, `boolean`, `object`.

  Arrays can be defined using the `[]` suffix. For example `string[]`.
</ParamField>

<ParamField body="required" type="boolean">
  Indicate whether the parameter is required.
</ParamField>

<ParamField body="deprecated" type="boolean">
  Indicate whether the parameter is deprecated.
</ParamField>

<ParamField body="default" type="any">
  Default value populated when the request value is empty
</ParamField>

<ParamField body="placeholder" type="string">
  Placeholder text for the input in the playground.
</ParamField>

<ParamField body="children" type="string">
  Description of the parameter (Markdown-enabled).
</ParamField>


## Response field

The `<ResponseField>` component defines the return values of an API.

<ResponseField name="response" type="string" required>
  An example of a response field
</ResponseField>

```mdx  theme={null}
<ResponseField name="response" type="string" required>
  A response field example
</ResponseField>
```

### Properties

<ResponseField name="name" type="string" required>
  The name of the response value.
</ResponseField>

<ResponseField name="type" type="string" required>
  Expected type of the response value. This can be any arbitrary string.
</ResponseField>

<ResponseField name="default" type="string">
  The default value.
</ResponseField>

<ResponseField name="required" type="boolean">
  Indicate whether the response is required.
</ResponseField>

<ResponseField name="deprecated" type="boolean">
  Whether a field is deprecated.
</ResponseField>

<ResponseField name="pre" type="string[]">
  Labels that are shown before the name of the field.
</ResponseField>

<ResponseField name="post" type="string[]">
  Labels that are shown after the name of the field.
</ResponseField>



# Frames
Source: https://mintlify.com/docs/components/frames

Wrap images or other components in a container

Use frames to display images, diagrams, or other visual content with consistent styling and optional captions. Frames center content and provide visual separation from surrounding text.

<Frame>
  <img src="https://mintlify-assets.b-cdn.net/yellowstone.jpeg" alt="Photograph of a lake surrounded by trees with mountains in the distance in Yellowstone National Park." />
</Frame>


## Captions

You can add additional context to an image using the optional `caption` prop.

<Frame caption="Yosemite National Park is visited by over 3.5 million people every year">
  <img src="https://mintlify-assets.b-cdn.net/yosemite.jpg" alt="Photograph of Yosemite Valley." />
</Frame>


## Properties

<ResponseField name="caption" type="string">
  Optional caption text to show centered under your component.
</ResponseField>

<CodeGroup>
  ```mdx Frame theme={null}
  <Frame>
    <img src="/path/image.jpg" alt="Descriptive alt text" />
  </Frame>
  ```

  ```mdx Frame with a caption theme={null}
  <Frame caption="Caption text">
    <img src="/path/image.jpg" alt="Descriptive alt text" />
  </Frame>
  ```
</CodeGroup>



# Icons
Source: https://mintlify.com/docs/components/icons

Use icons from popular icon libraries

Use icons from Font Awesome, Lucide, SVGs, external URLs, or files in your project to enhance your documentation.

<Icon icon="flag" size={32} />

```mdx Icon example theme={null}
<Icon icon="flag" size={32} />
```


## Inline icons

Icons are placed inline when used within a sentence, paragraph, or heading. <Icon icon="flag" iconType="solid" /> Use icons for decoration or to add visual emphasis.

```markdown Inline icon example theme={null}
Icons are placed inline when used within a sentence, paragraph, or heading. <Icon icon="flag" iconType="solid" /> Use icons for decoration or to add visual emphasis.
```


## Properties

<ResponseField name="icon" type="string" required>
  The icon to display.

  Options:

  * [Font Awesome icon](https://fontawesome.com/icons) name
  * [Lucide icon](https://lucide.dev/icons) name
  * JSX-compatible SVG code wrapped in curly braces
  * URL to an externally hosted icon
  * Path to an icon file in your project

  For custom SVG icons:

  1. Convert your SVG using the [SVGR converter](https://react-svgr.com/playground/).
  2. Paste your SVG code into the SVG input field.
  3. Copy the complete `<svg>...</svg>` element from the JSX output field.
  4. Wrap the JSX-compatible SVG code in curly braces: `icon={<svg ...> ... </svg>}`.
  5. Adjust `height` and `width` as needed.
</ResponseField>

<ResponseField name="iconType" type="string">
  The [Font Awesome](https://fontawesome.com/icons) icon style. Only used with Font Awesome icons.

  Options: `regular`, `solid`, `light`, `thin`, `sharp-solid`, `duotone`, `brands`.
</ResponseField>

<ResponseField name="color" type="string">
  The color of the icon as a hex code (for example, `#FF5733`).
</ResponseField>

<ResponseField name="size" type="number">
  The size of the icon in pixels.
</ResponseField>



---
**Navigation:** [← Previous](./01-ai-native.md) | [Index](./index.md) | [Next →](./03-mermaid.md)
