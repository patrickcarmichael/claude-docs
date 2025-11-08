# SDKs

**Navigation:** [← Previous](./02-build-an-mcp-server.md) | [Index](./index.md) | [Next →](./04-sampling.md)

---

# SDKs
Source: https://modelcontextprotocol.io/docs/sdk

Official SDKs for building with Model Context Protocol

Build MCP servers and clients using our official SDKs. All SDKs provide the same core functionality and full protocol support.


## Available SDKs

<CardGroup cols={3}>
  <Card title="TypeScript" icon="square-js" href="https://github.com/modelcontextprotocol/typescript-sdk" />

  <Card title="Python" icon="python" href="https://github.com/modelcontextprotocol/python-sdk" />

  <Card title="Go" icon="golang" href="https://github.com/modelcontextprotocol/go-sdk" />

  <Card title="Kotlin" icon="square-k" href="https://github.com/modelcontextprotocol/kotlin-sdk" />

  <Card title="Swift" icon="swift" href="https://github.com/modelcontextprotocol/swift-sdk" />

  <Card title="Java" icon="java" href="https://github.com/modelcontextprotocol/java-sdk" />

  <Card title="C#" icon="square-c" href="https://github.com/modelcontextprotocol/csharp-sdk" />

  <Card title="Ruby" icon="gem" href="https://github.com/modelcontextprotocol/ruby-sdk" />

  <Card title="Rust" icon="rust" href="https://github.com/modelcontextprotocol/rust-sdk" />

  <Card title="PHP" icon="php" href="https://github.com/modelcontextprotocol/php-sdk" />
</CardGroup>


## Getting Started

Each SDK provides the same functionality but follows the idioms and best practices of its language. All SDKs support:

* Creating MCP servers that expose tools, resources, and prompts
* Building MCP clients that can connect to any MCP server
* Local and remote transport protocols
* Protocol compliance with type safety

Visit the SDK page for your chosen language to find installation instructions, documentation, and examples.


## Next Steps

Ready to start building with MCP? Choose your path:

<CardGroup cols={2}>
  <Card title="Build a Server" icon="server" href="/docs/develop/build-server">
    Learn how to create your first MCP server
  </Card>

  <Card title="Build a Client" icon="computer" href="/docs/develop/build-client">
    Create applications that connect to MCP servers
  </Card>
</CardGroup>



# MCP Inspector
Source: https://modelcontextprotocol.io/docs/tools/inspector

In-depth guide to using the MCP Inspector for testing and debugging Model Context Protocol servers

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is an interactive developer tool for testing and debugging MCP servers. While the [Debugging Guide](/legacy/tools/debugging) covers the Inspector as part of the overall debugging toolkit, this document provides a detailed exploration of the Inspector's features and capabilities.


## Getting started

### Installation and basic usage

The Inspector runs directly through `npx` without requiring installation:

```bash  theme={null}
npx @modelcontextprotocol/inspector <command>
```

```bash  theme={null}
npx @modelcontextprotocol/inspector <command> <arg1> <arg2>
```

#### Inspecting servers from npm or PyPI

A common way to start server packages from [npm](https://npmjs.com) or [PyPI](https://pypi.org).

<Tabs>
  <Tab title="npm package">
    ```bash  theme={null}
    npx -y @modelcontextprotocol/inspector npx <package-name> <args>
    # For example
    npx -y @modelcontextprotocol/inspector npx @modelcontextprotocol/server-filesystem /Users/username/Desktop
    ```
  </Tab>

  <Tab title="PyPI package">
    ```bash  theme={null}
    npx @modelcontextprotocol/inspector uvx <package-name> <args>
    # For example
    npx @modelcontextprotocol/inspector uvx mcp-server-git --repository ~/code/mcp/servers.git
    ```
  </Tab>
</Tabs>

#### Inspecting locally developed servers

To inspect servers locally developed or downloaded as a repository, the most common
way is:

<Tabs>
  <Tab title="TypeScript">
    ```bash  theme={null}
    npx @modelcontextprotocol/inspector node path/to/server/index.js args...
    ```
  </Tab>

  <Tab title="Python">
    ```bash  theme={null}
    npx @modelcontextprotocol/inspector \
      uv \
      --directory path/to/server \
      run \
      package-name \
      args...
    ```
  </Tab>
</Tabs>

Please carefully read any attached README for the most accurate instructions.


## Feature overview

<Frame caption="The MCP Inspector interface">
  <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-inspector.png?fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=83b12e2a457c96ef4ad17c7357236290" data-og-width="2888" width="2888" data-og-height="1761" height="1761" data-path="images/mcp-inspector.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-inspector.png?w=280&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=63e7263fbdf5f473064f37dac99ae8e5 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-inspector.png?w=560&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=78dcf971172e8790fc672f19ead2796d 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-inspector.png?w=840&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=8c4ce11c7901888cd967f461df66a0f3 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-inspector.png?w=1100&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=279b84d4729737f1241514cb30de3b40 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-inspector.png?w=1650&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=ac5dcc45e291ba2f2954d3a22c918029 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-inspector.png?w=2500&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=4fbcddae467e84daef4739e0816ab698 2500w" />
</Frame>

The Inspector provides several features for interacting with your MCP server:

### Server connection pane

* Allows selecting the [transport](/legacy/concepts/transports) for connecting to the server
* For local servers, supports customizing the command-line arguments and environment

### Resources tab

* Lists all available resources
* Shows resource metadata (MIME types, descriptions)
* Allows resource content inspection
* Supports subscription testing

### Prompts tab

* Displays available prompt templates
* Shows prompt arguments and descriptions
* Enables prompt testing with custom arguments
* Previews generated messages

### Tools tab

* Lists available tools
* Shows tool schemas and descriptions
* Enables tool testing with custom inputs
* Displays tool execution results

### Notifications pane

* Presents all logs recorded from the server
* Shows notifications received from the server


## Best practices

### Development workflow

1. Start Development
   * Launch Inspector with your server
   * Verify basic connectivity
   * Check capability negotiation

2. Iterative testing
   * Make server changes
   * Rebuild the server
   * Reconnect the Inspector
   * Test affected features
   * Monitor messages

3. Test edge cases
   * Invalid inputs
   * Missing prompt arguments
   * Concurrent operations
   * Verify error handling and error responses


## Next steps

<CardGroup cols={2}>
  <Card title="Inspector Repository" icon="github" href="https://github.com/modelcontextprotocol/inspector">
    Check out the MCP Inspector source code
  </Card>

  <Card title="Debugging Guide" icon="bug" href="/legacy/tools/debugging">
    Learn about broader debugging strategies
  </Card>
</CardGroup>



# Understanding Authorization in MCP
Source: https://modelcontextprotocol.io/docs/tutorials/security/authorization

Learn how to implement secure authorization for MCP servers using OAuth 2.1 to protect sensitive resources and operations

Authorization in the Model Context Protocol (MCP) secures access to sensitive resources and operations exposed by MCP servers. If your MCP server handles user data or administrative actions, authorization ensures only permitted users can access its endpoints.

MCP uses standardized authorization flows to build trust between MCP clients and MCP servers. Its design doesn't focus on one specific authorization or identity system, but rather follows the conventions outlined for [OAuth 2.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13). For detailed information, see the [Authorization specification](/specification/2025-06-18/basic/authorization).


## When Should You Use Authorization?

While authorization for MCP servers is **optional**, it is strongly recommended when:

* Your server accesses user-specific data (emails, documents, databases)
* You need to audit who performed which actions
* Your server grants access to its APIs that require user consent
* You're building for enterprise environments with strict access controls
* You want to implement rate limiting or usage tracking per user

<Tip>
  **Authorization for Local MCP Servers**

  For MCP servers using the [STDIO transport](/specification/2025-06-18/basic/transports#stdio), you can use environment-based credentials or credentials provided by third-party libraries embedded directly in the MCP server instead. Because a STDIO-built MCP server runs locally, it has access to a range of flexible options when it comes to acquiring user credentials that may or may not rely on in-browser authentication and authorization flows.

  OAuth flows, in turn, are designed for HTTP-based transports where the MCP server is remotely-hosted and the client uses OAuth to establish that a user is authorized to access said remote server.
</Tip>


## The Authorization Flow: Step by Step

Let's walk through what happens when a client wants to connect to your protected MCP server:

<Steps>
  <Step title="Initial Handshake">
    When your MCP client first tries to connect, your server responds with a `401 Unauthorized` and tells the client where to find authorization information, captured in a [Protected Resource Metadata (PRM) document](https://datatracker.ietf.org/doc/html/rfc9728). The document is hosted by the MCP server, follows a predictable path pattern, and is provided to the client in the `resource_metadata` parameter within the `WWW-Authenticate` header.

    ```http  theme={null}
    HTTP/1.1 401 Unauthorized
    WWW-Authenticate: Bearer realm="mcp",
      resource_metadata="https://your-server.com/.well-known/oauth-protected-resource"
    ```

    This tells the client that authorization is required for the MCP server and where to get the necessary information to kickstart the authorization flow.
  </Step>

  <Step title="Protected Resource Metadata Discovery">
    With the URI pointer to the PRM document, the client will fetch the metadata to learn about the authorization server, supported scopes, and other resource information. The data is typically encapsulated in a JSON blob, similar to the one below.

    ```json  theme={null}
    {
      "resource": "https://your-server.com/mcp",
      "authorization_servers": ["https://auth.your-server.com"],
      "scopes_supported": ["mcp:tools", "mcp:resources"]
    }
    ```

    You can see a more comprehensive example in [RFC 9728 Section 3.2](https://datatracker.ietf.org/doc/html/rfc9728#name-protected-resource-metadata-r).
  </Step>

  <Step title="Authorization Server Discovery">
    Next, the client discovers what the authorization server can do by fetching its metadata. If the PRM document lists more than one authorization server, the client can decide which one to use.

    With an authorization server selected, the client will then construct a standard metadata URI and issue a request to the [OpenID Connect (OIDC) Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html) or [OAuth 2.0 Auth Server Metadata](https://datatracker.ietf.org/doc/html/rfc8414) endpoints (depending on authorization server support)
    and retrieve another set of metadata properties that will allow it to know the endpoints it needs to complete the authorization flow.

    ```json  theme={null}
    {
      "issuer": "https://auth.your-server.com",
      "authorization_endpoint": "https://auth.your-server.com/authorize",
      "token_endpoint": "https://auth.your-server.com/token",
      "registration_endpoint": "https://auth.your-server.com/register"
    }
    ```
  </Step>

  <Step title="Client Registration">
    With all the metadata out of the way, the client now needs to make sure that it's registered with the authorization server. This can be done in two ways.

    First, the client can be **pre-registered** with a given authorization server, in which case it can have embedded client registration information that it uses to complete the authorization flow.

    Alternatively, the client can use **Dynamic Client Registration** (DCR) to dynamically register itself with the authorization server. The latter scenario requires the authorization server to support DCR. If the authorization server does support DCR, the client will send a request to the `registration_endpoint` with its information:

    ```json  theme={null}
    {
      "client_name": "My MCP Client",
      "redirect_uris": ["http://localhost:3000/callback"],
      "grant_types": ["authorization_code", "refresh_token"],
      "response_types": ["code"]
    }
    ```

    If the registration succeeds, the authorization server will return a JSON blob with client registration information.

    <Tip>
      **No DCR or Pre-Registration**

      In case an MCP client connects to an MCP server that doesn't use an authorization server that supports DCR and the client is not pre-registered with said authorization server, it's the responsibility of the client developer to provide an affordance for the end-user to enter client information manually.
    </Tip>
  </Step>

  <Step title="User Authorization">
    The client will now need to open a browser to the `/authorize` endpoint, where the user can log in and grant the required permissions. The authorization server will then redirect back to the client with an authorization code that the client exchanges for tokens:

    ```json  theme={null}
    {
      "access_token": "eyJhbGciOiJSUzI1NiIs...",
      "refresh_token": "def502...",
      "token_type": "Bearer",
      "expires_in": 3600
    }
    ```

    The access token is what the client will use to authenticate requests to the MCP server. This step follows standard [OAuth 2.1 authorization code with PKCE](https://oauth.net/2/grant-types/authorization-code/) conventions.
  </Step>

  <Step title="Making Authenticated Requests">
    Finally, the client can make requests to your MCP server using the access token embedded in the `Authorization` header:

    ```http  theme={null}
    GET /mcp HTTP/1.1
    Host: your-server.com
    Authorization: Bearer eyJhbGciOiJSUzI1NiIs...
    ```

    The MCP server will need to validate the token and process the request if the token is valid and has the required permissions.
  </Step>
</Steps>


## Implementation Example

To get started with a practical implementation, we will use a [Keycloak](https://www.keycloak.org/) authorization server hosted in a Docker container. Keycloak is an open-source authorization server that can be easily deployed locally for testing and experimentation.

Make sure that you download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/). We will need it to deploy Keycloak on our development machine.

### Keycloak Setup

From your terminal application, run the following command to start the Keycloak container:

```bash  theme={null}
docker run -p 127.0.0.1:8080:8080 -e KC_BOOTSTRAP_ADMIN_USERNAME=admin -e KC_BOOTSTRAP_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak start-dev
```

This command will pull the Keycloak container image locally and bootstrap the basic configuration. It will run on port `8080` and have an `admin` user with `admin` password.

<Warning>
  **Not for Production**

  The configuration above may be suitable for testing and experimentation; however, you should never use it in production. Refer to the [Configuring Keycloak for production](https://www.keycloak.org/server/configuration-production) guide for additional details on how to deploy the authorization server for scenarios that require reliability, security, and high availability.
</Warning>

You will be able to access the Keycloak authorization server from your browser at `http://localhost:8080`.

<Frame>
  <img src="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-browser.png?fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=cba689d986e113cbe937d732ac0558b6" alt="Keycloak admin dashboard authentication dialog." data-og-width="1834" width="1834" data-og-height="1450" height="1450" data-path="images/tutorial-authorization/keycloak-browser.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-browser.png?w=280&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=6f32c1c9aa75a0533213ef708e0486f9 280w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-browser.png?w=560&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=a93c454733e5d23dea996ac4243b5ba7 560w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-browser.png?w=840&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=08f456b670f8c07ec91489abd44e1102 840w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-browser.png?w=1100&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=6f38eebb04db868078b62adc377c673d 1100w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-browser.png?w=1650&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=5e6ab1e9d62b82781152096fe6ee4c62 1650w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-browser.png?w=2500&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=26faaf97617cb789b0492ea580245dc0 2500w" />
</Frame>

When running with the default configuration, Keycloak will already support many of the capabilities that we need for MCP servers, including Dynamic Client Registration. You can check this by looking at the OIDC configuration, available at:

```http  theme={null}
http://localhost:8080/realms/master/.well-known/openid-configuration
```

We will also need to set up Keycloak to support our scopes and allow our host (local machine) to dynamically register clients, as the default policies restrict anonymous dynamic client registration.

Go to **Client scopes** in the Keycloak dashboard and create a new `mcp:tools` scope. We will use this to access all of the tools on our MCP server.

<Frame>
  <img src="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-scopes.png?fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=3cd49dc2e070027609ae495751e0db58" alt="Configuring Keycloak scopes." data-og-width="1999" width="1999" data-og-height="1710" height="1710" data-path="images/tutorial-authorization/keycloak-scopes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-scopes.png?w=280&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=63647c72d96cc867eff23f6f193c97a3 280w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-scopes.png?w=560&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=d28690bb063e22a3f677c23df8a338bf 560w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-scopes.png?w=840&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=4e9dc9972f1449f20c2a5559fbfdde06 840w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-scopes.png?w=1100&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=b3a21b321612781d41ab018fcd19bca0 1100w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-scopes.png?w=1650&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=345993151f644fe6aca724a605c168f6 1650w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-scopes.png?w=2500&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=ac6152d64434b7cf8a8e74a4128b0f4f 2500w" />
</Frame>

After creating the scope, make sure that you assign its type to **Default** and have flipped the **Include in token scope** switch, as this will be needed for token validation.

Let's now also set up an **audience** for our Keycloak-issued tokens. An audience is important to configure because it embeds the intended destination directly into the issued access token. This helps your MCP server to verify that the token it got was actually meant for it rather than some other API. This is key to help avoid token passthrough scenarios.

To do this, open your `mcp:tools` client scope and click on **Mappers**, followed by **Configure a new mapper**. Select **Audience**.

<Frame>
  <img src="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/scope-add-audience.gif?s=6ea9cf20c397f4c79c491c2e39019272" alt="Configuring an audience for a token in Keycloak." data-og-width="1080" width="1080" data-og-height="921" height="921" data-path="images/tutorial-authorization/scope-add-audience.gif" data-optimize="true" data-opv="3" />
</Frame>

For **Name**, use `audience-config`. Add a value for **Included Custom Audience**, set to `http://localhost:3000`. This will be the URI of our test server.

<Warning>
  **Not for Production**

  The audience configuration above is meant for testing. For production scenarios, additional set-up and configuration will be required to ensure that audiences are properly constrained for issued tokens. Specifically, the audience needs to be based on the resource parameter passed from the client, not a fixed value.
</Warning>

Now, navigate to **Clients**, then **Client registration**, and then **Trusted Hosts**. Disable the **Client URIs Must Match** setting and add the hosts from which you're testing. You can get your current host IP by running the `ifconfig` command on Linux or macOS, or `ipconfig` on Windows. You can see the IP address you need to add by looking at the keycloak logs for a line that looks like `Failed to verify remote host : 192.168.215.1`. Check that the IP address is associated with your host. This may be for a bridge network depending on your docker setup.

<Frame>
  <img src="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-client.gif?s=b5d40b36a5f1ea1e818821bb8ea77f6b" alt="Setting up client registration details in Keycloak." data-og-width="1199" width="1199" data-og-height="1027" height="1027" data-path="images/tutorial-authorization/keycloak-client.gif" data-optimize="true" data-opv="3" />
</Frame>

<Warning>
  **Getting the Host**

  If you are running Keycloak from a container, you will also be able to see the host IP from the Terminal in the container logs.
</Warning>

Lastly, we need to register a new client that we can use with the **MCP server itself** to talk to Keycloak for things like [token introspection](https://oauth.net/2/token-introspection/). To do that:

1. Go to **Clients**.
2. Click **Create client**.
3. Give your client a unique **Client ID** and click **Next**.
4. Enable **Client authentication** and click **Next**.
5. Click **Save**.

Worth noting that token introspection is just *one of* the available approaches to validate tokens. This can also be done with the help of standalone libraries, specific to each language and platform.

When you open the client details, go to **Credentials** and take note of the **Client Secret**.

<Frame>
  <img src="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-client-auth.gif?s=7152c41a5746994fd399024bc4659e40" alt="Creating a new client in Keycloak." data-og-width="1200" width="1200" data-og-height="1023" height="1023" data-path="images/tutorial-authorization/keycloak-client-auth.gif" data-optimize="true" data-opv="3" />
</Frame>

<Warning>
  **Handling Secrets**

  Never embed client credentials directly in your code. We recommend using environment variables or specialized solutions for secret storage.
</Warning>

With Keycloak configured, every time the authorization flow is triggered, your MCP server will receive a token like this:

```text  theme={null}
eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI1TjcxMGw1WW5MWk13WGZ1VlJKWGtCS3ZZMzZzb3JnRG5scmlyZ2tlTHlzIn0.eyJleHAiOjE3NTU1NDA4MTcsImlhdCI6MTc1NTU0MDc1NywiYXV0aF90aW1lIjoxNzU1NTM4ODg4LCJqdGkiOiJvbnJ0YWM6YjM0MDgwZmYtODQwNC02ODY3LTgxYmUtMTIzMWI1MDU5M2E4IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9tYXN0ZXIiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjMwMDAiLCJzdWIiOiIzM2VkNmM2Yi1jNmUwLTQ5MjgtYTE2MS1mMmY2OWM3YTAzYjkiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiI3OTc1YTViNi04YjU5LTRhODUtOWNiYS04ZmFlYmRhYjg5NzQiLCJzaWQiOiI4ZjdlYzI3Ni0zNThmLTRjY2MtYjMxMy1kYjA4MjkwZjM3NmYiLCJzY29wZSI6Im1jcDp0b29scyJ9.P5xCRtXORly0R0EXjyqRCUx-z3J4uAOWNAvYtLPXroykZuVCCJ-K1haiQSwbURqfsVOMbL7jiV-sD6miuPzI1tmKOkN_Yct0Vp-azvj7U5rEj7U6tvPfMkg2Uj_jrIX0KOskyU2pVvGZ-5BgqaSvwTEdsGu_V3_E0xDuSBq2uj_wmhqiyTFm5lJ1WkM3Hnxxx1_AAnTj7iOKMFZ4VCwMmk8hhSC7clnDauORc0sutxiJuYUZzxNiNPkmNeQtMCGqWdP1igcbWbrfnNXhJ6NswBOuRbh97_QraET3hl-CNmyS6C72Xc0aOwR_uJ7xVSBTD02OaQ1JA6kjCATz30kGYg
```

Decoded, it will look like this:

```json  theme={null}
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "5N710l5YnLZMwXfuVRJXkBKvY36sorgDnlrirgkeLys"
}.{
  "exp": 1755540817,
  "iat": 1755540757,
  "auth_time": 1755538888,
  "jti": "onrtac:b34080ff-8404-6867-81be-1231b50593a8",
  "iss": "http://localhost:8080/realms/master",
  "aud": "http://localhost:3000",
  "sub": "33ed6c6b-c6e0-4928-a161-f2f69c7a03b9",
  "typ": "Bearer",
  "azp": "7975a5b6-8b59-4a85-9cba-8faebdab8974",
  "sid": "8f7ec276-358f-4ccc-b313-db08290f376f",
  "scope": "mcp:tools"
}.[Signature]
```

<Warning>
  **Embedded Audience**

  Notice the `aud` claim embedded in the token - it's currently set to be the URI of the test MCP server and it's inferred from the scope that we've previously configured. This will be important in our implementation to validate.
</Warning>

### MCP Server Setup

We will now set up our MCP server to use the locally-running Keycloak authorization server. Depending on your programming language preference, you can use one of the supported [MCP SDKs](/docs/sdk).

For our testing purposes, we will create an extremely simple MCP server that exposes two tools - one for addition and another for multiplication. The server will require authorization to access these.

<Tabs>
  <Tab title="TypeScript">
    You can see the complete TypeScript project in the [sample repository](https://github.com/localden/min-ts-mcp-auth).

    Prior to running the code below, ensure that you have a `.env` file with the following content:

    ```env  theme={null}
    # Server host/port
    HOST=localhost
    PORT=3000

    # Auth server location
    AUTH_HOST=localhost
    AUTH_PORT=8080
    AUTH_REALM=master

    # Keycloak OAuth client credentials
    OAUTH_CLIENT_ID=<YOUR_SERVER_CLIENT_ID>
    OAUTH_CLIENT_SECRET=<YOUR_SERVER_CLIENT_SECRET>
    ```

    `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET` are associated with the MCP server client we created earlier.

    In addition to implementing the MCP authorization specification, the server below also does token introspection via Keycloak to make sure that the token it receives from the client is valid. It also implements basic logging to allow you to easily diagnose any issues.

    ```typescript  theme={null}
    import "dotenv/config";
    import express from "express";
    import { randomUUID } from "node:crypto";
    import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
    import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
    import { isInitializeRequest } from "@modelcontextprotocol/sdk/types.js";
    import { z } from "zod";
    import cors from "cors";
    import {
      mcpAuthMetadataRouter,
      getOAuthProtectedResourceMetadataUrl,
    } from "@modelcontextprotocol/sdk/server/auth/router.js";
    import { requireBearerAuth } from "@modelcontextprotocol/sdk/server/auth/middleware/bearerAuth.js";
    import { OAuthMetadata } from "@modelcontextprotocol/sdk/shared/auth.js";
    import { checkResourceAllowed } from "@modelcontextprotocol/sdk/shared/auth-utils.js";
    const CONFIG = {
      host: process.env.HOST || "localhost",
      port: Number(process.env.PORT) || 3000,
      auth: {
        host: process.env.AUTH_HOST || process.env.HOST || "localhost",
        port: Number(process.env.AUTH_PORT) || 8080,
        realm: process.env.AUTH_REALM || "master",
        clientId: process.env.OAUTH_CLIENT_ID || "mcp-server",
        clientSecret: process.env.OAUTH_CLIENT_SECRET || "",
      },
    };

    function createOAuthUrls() {
      const authBaseUrl = new URL(
        `http://${CONFIG.auth.host}:${CONFIG.auth.port}/realms/${CONFIG.auth.realm}/`,
      );
      return {
        issuer: authBaseUrl.toString(),
        introspection_endpoint: new URL(
          "protocol/openid-connect/token/introspect",
          authBaseUrl,
        ).toString(),
        authorization_endpoint: new URL(
          "protocol/openid-connect/auth",
          authBaseUrl,
        ).toString(),
        token_endpoint: new URL(
          "protocol/openid-connect/token",
          authBaseUrl,
        ).toString(),
      };
    }

    function createRequestLogger() {
      return (req: any, res: any, next: any) => {
        const start = Date.now();
        res.on("finish", () => {
          const ms = Date.now() - start;
          console.log(
            `${req.method} ${req.originalUrl} -> ${res.statusCode} ${ms}ms`,
          );
        });
        next();
      };
    }

    const app = express();

    app.use(
      express.json({
        verify: (req: any, _res, buf) => {
          req.rawBody = buf?.toString() ?? "";
        },
      }),
    );

    app.use(
      cors({
        origin: "*",
        exposedHeaders: ["Mcp-Session-Id"],
      }),
    );

    app.use(createRequestLogger());

    const mcpServerUrl = new URL(`http://${CONFIG.host}:${CONFIG.port}`);
    const oauthUrls = createOAuthUrls();

    const oauthMetadata: OAuthMetadata = {
      ...oauthUrls,
      response_types_supported: ["code"],
    };

    const tokenVerifier = {
      verifyAccessToken: async (token: string) => {
        const endpoint = oauthMetadata.introspection_endpoint;

        if (!endpoint) {
          console.error("[auth] no introspection endpoint in metadata");
          throw new Error("No token verification endpoint available in metadata");
        }

        const params = new URLSearchParams({
          token: token,
          client_id: CONFIG.auth.clientId,
        });

        if (CONFIG.auth.clientSecret) {
          params.set("client_secret", CONFIG.auth.clientSecret);
        }

        let response: Response;
        try {
          response = await fetch(endpoint, {
            method: "POST",
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
            },
            body: params.toString(),
          });
        } catch (e) {
          console.error("[auth] introspection fetch threw", e);
          throw e;
        }

        if (!response.ok) {
          const txt = await response.text();
          console.error("[auth] introspection non-OK", { status: response.status });

          try {
            const obj = JSON.parse(txt);
            console.log(JSON.stringify(obj, null, 2));
          } catch {
            console.error(txt);
          }
          throw new Error(`Invalid or expired token: ${txt}`);
        }

        let data: any;
        try {
          data = await response.json();
        } catch (e) {
          const txt = await response.text();
          console.error("[auth] failed to parse introspection JSON", {
            error: String(e),
            body: txt,
          });
          throw e;
        }

        if (data.active === false) {
          throw new Error("Inactive token");
        }

        if (!data.aud) {
          throw new Error("Resource indicator (aud) missing");
        }

        const audiences: string[] = Array.isArray(data.aud) ? data.aud : [data.aud];
        const allowed = audiences.some((a) =>
          checkResourceAllowed({
            requestedResource: a,
            configuredResource: mcpServerUrl,
          }),
        );
        if (!allowed) {
          throw new Error(
            `None of the provided audiences are allowed. Expected ${mcpServerUrl}, got: ${audiences.join(", ")}`,
          );
        }

        return {
          token,
          clientId: data.client_id,
          scopes: data.scope ? data.scope.split(" ") : [],
          expiresAt: data.exp,
        };
      },
    };
    app.use(
      mcpAuthMetadataRouter({
        oauthMetadata,
        resourceServerUrl: mcpServerUrl,
        scopesSupported: ["mcp:tools"],
        resourceName: "MCP Demo Server",
      }),
    );

    const authMiddleware = requireBearerAuth({
      verifier: tokenVerifier,
      requiredScopes: [],
      resourceMetadataUrl: getOAuthProtectedResourceMetadataUrl(mcpServerUrl),
    });

    const transports: { [sessionId: string]: StreamableHTTPServerTransport } = {};

    function createMcpServer() {
      const server = new McpServer({
        name: "example-server",
        version: "1.0.0",
      });

      server.registerTool(
        "add",
        {
          title: "Addition Tool",
          description: "Add two numbers together",
          inputSchema: {
            a: z.number().describe("First number to add"),
            b: z.number().describe("Second number to add"),
          },
        },
        async ({ a, b }) => ({
          content: [{ type: "text", text: `${a} + ${b} = ${a + b}` }],
        }),
      );

      server.registerTool(
        "multiply",
        {
          title: "Multiplication Tool",
          description: "Multiply two numbers together",
          inputSchema: {
            x: z.number().describe("First number to multiply"),
            y: z.number().describe("Second number to multiply"),
          },
        },
        async ({ x, y }) => ({
          content: [{ type: "text", text: `${x} × ${y} = ${x * y}` }],
        }),
      );

      return server;
    }

    const mcpPostHandler = async (req: express.Request, res: express.Response) => {
      const sessionId = req.headers["mcp-session-id"] as string | undefined;
      let transport: StreamableHTTPServerTransport;

      if (sessionId && transports[sessionId]) {
        transport = transports[sessionId];
      } else if (!sessionId && isInitializeRequest(req.body)) {
        transport = new StreamableHTTPServerTransport({
          sessionIdGenerator: () => randomUUID(),
          onsessioninitialized: (sessionId) => {
            transports[sessionId] = transport;
          },
        });

        transport.onclose = () => {
          if (transport.sessionId) {
            delete transports[transport.sessionId];
          }
        };

        const server = createMcpServer();
        await server.connect(transport);
      } else {
        res.status(400).json({
          jsonrpc: "2.0",
          error: {
            code: -32000,
            message: "Bad Request: No valid session ID provided",
          },
          id: null,
        });
        return;
      }

      await transport.handleRequest(req, res, req.body);
    };

    const handleSessionRequest = async (
      req: express.Request,
      res: express.Response,
    ) => {
      const sessionId = req.headers["mcp-session-id"] as string | undefined;
      if (!sessionId || !transports[sessionId]) {
        res.status(400).send("Invalid or missing session ID");
        return;
      }

      const transport = transports[sessionId];
      await transport.handleRequest(req, res);
    };

    app.post("/", authMiddleware, mcpPostHandler);
    app.get("/", authMiddleware, handleSessionRequest);
    app.delete("/", authMiddleware, handleSessionRequest);

    app.listen(CONFIG.port, CONFIG.host, () => {
      console.log(`🚀 MCP Server running on ${mcpServerUrl.origin}`);
      console.log(`📡 MCP endpoint available at ${mcpServerUrl.origin}`);
      console.log(
        `🔐 OAuth metadata available at ${getOAuthProtectedResourceMetadataUrl(mcpServerUrl)}`,
      );
    });
    ```

    When you run the server, you can add it to your MCP client, such as Visual Studio Code, by providing the MCP server endpoint.

    For more details about implementing MCP servers in TypeScript, refer to the [TypeScript SDK documentation](https://github.com/modelcontextprotocol/typescript-sdk).
  </Tab>

  <Tab title="Python">
    You can see the complete Python project in the [sample repository](https://github.com/localden/min-py-mcp-auth).

    To simplify our authorization interaction, in Python scenarios we rely on [FastMCP](https://gofastmcp.com/getting-started/welcome). A lot of the conventions around authorization, like the endpoints and token validation logic, are consistent across languages, but some offer simpler ways in integrating them in production scenarios.

    Prior to writing the actual server, we need to set up our configuration in `config.py` - the contents are entirely based on your local server setup:

    ```python  theme={null}
    """Configuration settings for the MCP auth server."""

    import os
    from typing import Optional


    class Config:
        """Configuration class that loads from environment variables with sensible defaults."""

        # Server settings
        HOST: str = os.getenv("HOST", "localhost")
        PORT: int = int(os.getenv("PORT", "3000"))

        # Auth server settings
        AUTH_HOST: str = os.getenv("AUTH_HOST", "localhost")
        AUTH_PORT: int = int(os.getenv("AUTH_PORT", "8080"))
        AUTH_REALM: str = os.getenv("AUTH_REALM", "master")

        # OAuth client settings
        OAUTH_CLIENT_ID: str = os.getenv("OAUTH_CLIENT_ID", "mcp-server")
        OAUTH_CLIENT_SECRET: str = os.getenv("OAUTH_CLIENT_SECRET", "UO3rmozkFFkXr0QxPTkzZ0LMXDidIikB")

        # Server settings
        MCP_SCOPE: str = os.getenv("MCP_SCOPE", "mcp:tools")
        OAUTH_STRICT: bool = os.getenv("OAUTH_STRICT", "false").lower() in ("true", "1", "yes")
        TRANSPORT: str = os.getenv("TRANSPORT", "streamable-http")

        @property
        def server_url(self) -> str:
            """Build the server URL."""
            return f"http://{self.HOST}:{self.PORT}"

        @property
        def auth_base_url(self) -> str:
            """Build the auth server base URL."""
            return f"http://{self.AUTH_HOST}:{self.AUTH_PORT}/realms/{self.AUTH_REALM}/"

        def validate(self) -> None:
            """Validate configuration."""
            if self.TRANSPORT not in ["sse", "streamable-http"]:
                raise ValueError(f"Invalid transport: {self.TRANSPORT}. Must be 'sse' or 'streamable-http'")


    # Global configuration instance
    config = Config()

    ```

    The server implementation is as follows:

    ```python  theme={null}
    import datetime
    import logging
    from typing import Any

    from pydantic import AnyHttpUrl

    from mcp.server.auth.settings import AuthSettings
    from mcp.server.fastmcp.server import FastMCP

    from .config import config
    from .token_verifier import IntrospectionTokenVerifier

    logger = logging.getLogger(__name__)


    def create_oauth_urls() -> dict[str, str]:
        """Create OAuth URLs based on configuration (Keycloak-style)."""
        from urllib.parse import urljoin

        auth_base_url = config.auth_base_url

        return {
            "issuer": auth_base_url,
            "introspection_endpoint": urljoin(auth_base_url, "protocol/openid-connect/token/introspect"),
            "authorization_endpoint": urljoin(auth_base_url, "protocol/openid-connect/auth"),
            "token_endpoint": urljoin(auth_base_url, "protocol/openid-connect/token"),
        }


    def create_server() -> FastMCP:
        """Create and configure the FastMCP server."""

        config.validate()

        oauth_urls = create_oauth_urls()

        token_verifier = IntrospectionTokenVerifier(
            introspection_endpoint=oauth_urls["introspection_endpoint"],
            server_url=config.server_url,
            client_id=config.OAUTH_CLIENT_ID,
            client_secret=config.OAUTH_CLIENT_SECRET,
        )

        app = FastMCP(
            name="MCP Resource Server",
            instructions="Resource Server that validates tokens via Authorization Server introspection",
            host=config.HOST,
            port=config.PORT,
            debug=True,
            streamable_http_path="/",
            token_verifier=token_verifier,
            auth=AuthSettings(
                issuer_url=AnyHttpUrl(oauth_urls["issuer"]),
                required_scopes=[config.MCP_SCOPE],
                resource_server_url=AnyHttpUrl(config.server_url),
            ),
        )

        @app.tool()
        async def add_numbers(a: float, b: float) -> dict[str, Any]:
            """
            Add two numbers together.
            This tool demonstrates basic arithmetic operations with OAuth authentication.

            Args:
                a: The first number to add
                b: The second number to add
            """
            result = a + b
            return {
                "operation": "addition",
                "operand_a": a,
                "operand_b": b,
                "result": result,
                "timestamp": datetime.datetime.now().isoformat()
            }

        @app.tool()
        async def multiply_numbers(x: float, y: float) -> dict[str, Any]:
            """
            Multiply two numbers together.
            This tool demonstrates basic arithmetic operations with OAuth authentication.

            Args:
                x: The first number to multiply
                y: The second number to multiply
            """
            result = x * y
            return {
                "operation": "multiplication",
                "operand_x": x,
                "operand_y": y,
                "result": result,
                "timestamp": datetime.datetime.now().isoformat()
            }

        return app


    def main() -> int:
        """
        Run the MCP Resource Server.

        This server:
        - Provides RFC 9728 Protected Resource Metadata
        - Validates tokens via Authorization Server introspection
        - Serves MCP tools requiring authentication

        Configuration is loaded from config.py and environment variables.
        """
        logging.basicConfig(level=logging.INFO)

        try:
            config.validate()
            oauth_urls = create_oauth_urls()

        except ValueError as e:
            logger.error("Configuration error: %s", e)
            return 1

        try:
            mcp_server = create_server()

            logger.info("Starting MCP Server on %s:%s", config.HOST, config.PORT)
            logger.info("Authorization Server: %s", oauth_urls["issuer"])
            logger.info("Transport: %s", config.TRANSPORT)

            mcp_server.run(transport=config.TRANSPORT)
            return 0

        except Exception:
            logger.exception("Server error")
            return 1


    if __name__ == "__main__":
        exit(main())
    ```

    Lastly, the token verification logic is delegated entirely to `token_verifier.py`, ensuring that we can use the Keycloak introspection endpoint to verify the validity of any credential artifacts

    ```python  theme={null}
    """Token verifier implementation using OAuth 2.0 Token Introspection (RFC 7662)."""

    import logging
    from typing import Any

    from mcp.server.auth.provider import AccessToken, TokenVerifier
    from mcp.shared.auth_utils import check_resource_allowed, resource_url_from_server_url

    logger = logging.getLogger(__name__)


    class IntrospectionTokenVerifier(TokenVerifier):
        """Token verifier that uses OAuth 2.0 Token Introspection (RFC 7662).
        """

        def __init__(
            self,
            introspection_endpoint: str,
            server_url: str,
            client_id: str,
            client_secret: str,
        ):
            self.introspection_endpoint = introspection_endpoint
            self.server_url = server_url
            self.client_id = client_id
            self.client_secret = client_secret
            self.resource_url = resource_url_from_server_url(server_url)

        async def verify_token(self, token: str) -> AccessToken | None:
            """Verify token via introspection endpoint."""
            import httpx

            if not self.introspection_endpoint.startswith(("https://", "http://localhost", "http://127.0.0.1")):
                return None

            timeout = httpx.Timeout(10.0, connect=5.0)
            limits = httpx.Limits(max_connections=10, max_keepalive_connections=5)

            async with httpx.AsyncClient(
                timeout=timeout,
                limits=limits,
                verify=True,
            ) as client:
                try:
                    form_data = {
                        "token": token,
                        "client_id": self.client_id,
                        "client_secret": self.client_secret,
                    }
                    headers = {"Content-Type": "application/x-www-form-urlencoded"}

                    response = await client.post(
                        self.introspection_endpoint,
                        data=form_data,
                        headers=headers,
                    )

                    if response.status_code != 200:
                        return None

                    data = response.json()
                    if not data.get("active", False):
                        return None

                    if not self._validate_resource(data):
                        return None

                    return AccessToken(
                        token=token,
                        client_id=data.get("client_id", "unknown"),
                        scopes=data.get("scope", "").split() if data.get("scope") else [],
                        expires_at=data.get("exp"),
                        resource=data.get("aud"),  # Include resource in token
                    )

                except Exception as e:
                    return None

        def _validate_resource(self, token_data: dict[str, Any]) -> bool:
            """Validate token was issued for this resource server.

            Rules:
            - Reject if 'aud' missing.
            - Accept if any audience entry matches the derived resource URL.
            - Supports string or list forms per JWT spec.
            """
            if not self.server_url or not self.resource_url:
                return False

            aud: list[str] | str | None = token_data.get("aud")
            if isinstance(aud, list):
                return any(self._is_valid_resource(a) for a in aud)
            if isinstance(aud, str):
                return self._is_valid_resource(aud)
            return False

        def _is_valid_resource(self, resource: str) -> bool:
            """Check if the given resource matches our server."""
            return check_resource_allowed(self.resource_url, resource)
    ```

    For more details, see the [Python SDK documentation](https://github.com/modelcontextprotocol/python-sdk).
  </Tab>

  <Tab title="C#">
    You can see the complete C# project in the [sample repository](https://github.com/localden/min-cs-mcp-auth).

    To set up authorization in your MCP server using the MCP C# SDK, you can lean on the standard ASP.NET Core builder pattern. Instead of using the introspection endpoint provided by Keycloak, we will use built-in ASP.NET Core capabilities for token validation.

    ```csharp  theme={null}
    using Microsoft.AspNetCore.Authentication.JwtBearer;
    using Microsoft.IdentityModel.Tokens;
    using ModelContextProtocol.AspNetCore.Authentication;
    using ProtectedMcpServer.Tools;
    using System.Security.Claims;

    var builder = WebApplication.CreateBuilder(args);

    var serverUrl = "http://localhost:3000/";
    var authorizationServerUrl = "http://localhost:8080/realms/master/";

    builder.Services.AddAuthentication(options =>
    {
        options.DefaultChallengeScheme = McpAuthenticationDefaults.AuthenticationScheme;
        options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
    })
    .AddJwtBearer(options =>
    {
        options.Authority = authorizationServerUrl;
        var normalizedServerAudience = serverUrl.TrimEnd('/');
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidIssuer = authorizationServerUrl,
            ValidAudiences = new[] { normalizedServerAudience, serverUrl },
            AudienceValidator = (audiences, securityToken, validationParameters) =>
            {
                if (audiences == null) return false;
                foreach (var aud in audiences)
                {
                    if (string.Equals(aud.TrimEnd('/'), normalizedServerAudience, StringComparison.OrdinalIgnoreCase))
                    {
                        return true;
                    }
                }
                return false;
            }
        };

        options.RequireHttpsMetadata = false; // Set to true in production

        options.Events = new JwtBearerEvents
        {
            OnTokenValidated = context =>
            {
                var name = context.Principal?.Identity?.Name ?? "unknown";
                var email = context.Principal?.FindFirstValue("preferred_username") ?? "unknown";
                Console.WriteLine($"Token validated for: {name} ({email})");
                return Task.CompletedTask;
            },
            OnAuthenticationFailed = context =>
            {
                Console.WriteLine($"Authentication failed: {context.Exception.Message}");
                return Task.CompletedTask;
            },
        };
    })
    .AddMcp(options =>
    {
        options.ResourceMetadata = new()
        {
            Resource = new Uri(serverUrl),
            ResourceDocumentation = new Uri("https://docs.example.com/api/math"),
            AuthorizationServers = { new Uri(authorizationServerUrl) },
            ScopesSupported = ["mcp:tools"]
        };
    });

    builder.Services.AddAuthorization();

    builder.Services.AddHttpContextAccessor();
    builder.Services.AddMcpServer()
        .WithTools<MathTools>()
        .WithHttpTransport();

    var app = builder.Build();

    app.UseAuthentication();
    app.UseAuthorization();

    app.MapMcp().RequireAuthorization();

    Console.WriteLine($"Starting MCP server with authorization at {serverUrl}");
    Console.WriteLine($"Using Keycloak server at {authorizationServerUrl}");
    Console.WriteLine($"Protected Resource Metadata URL: {serverUrl}.well-known/oauth-protected-resource");
    Console.WriteLine("Exposed Math tools: Add, Multiply");
    Console.WriteLine("Press Ctrl+C to stop the server");

    app.Run(serverUrl);
    ```

    For more details, see the [C# SDK documentation](https://github.com/modelcontextprotocol/csharp-sdk).
  </Tab>
</Tabs>


## Testing the MCP Server

For testing purposes, we will be using [Visual Studio Code](https://code.visualstudio.com), but any client that supports MCP and the new authorization specification will fit.

Press <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> and select **MCP: Add server...**. Select **HTTP** and enter `http://localhost:3000`. Give the server a unique name to be used inside Visual Studio Code. In `mcp.json` you should now see an entry like this:

```json  theme={null}
"my-mcp-server-18676652": {
  "url": "http://localhost:3000",
  "type": "http"
}
```

On connection, you will be taken to the browser, where you will be prompted to consent to Visual Studio Code having access to the `mcp:tools` scope.

<Frame>
  <img src="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=d5183fb7c257993aed1b2246f0bbbb27" alt="Keycloak consent form for VS Code." data-og-width="1915" width="1915" data-og-height="1536" height="1536" data-path="images/tutorial-authorization/keycloak-vscode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?w=280&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=93bb132878b75189c0cf198a59d3b053 280w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?w=560&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=155520f0a1b88422247d9910cb59899f 560w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?w=840&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=4fd24398061374fd940b05d97701dcbc 840w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?w=1100&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=e949784fc78e1f44bc8d3edeb218220b 1100w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?w=1650&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=30fc4dbf14307aac8a2ae938b112ef5b 1650w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?w=2500&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=3a0b543da5988dd95b1a447b138c83be 2500w" />
</Frame>

After consenting, you will see the tools listed right above the server entry in `mcp.json`.

<Frame>
  <img src="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=f7c34d1bf115fe6934e01b4a5a91168b" alt="Tools listed in VS Code." data-og-width="496" width="496" data-og-height="160" height="160" data-path="images/tutorial-authorization/tools-vs-code.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?w=280&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=9e66d87c84323d4efafb9fa80b58b611 280w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?w=560&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=4b2ef221709a1696272241badcfd7c42 560w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?w=840&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=ce16053621cc5b24a5f5a83fe541feaa 840w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?w=1100&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=59f05ee1ee685b60b0b3fe884cd732f8 1100w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?w=1650&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=ea1afa55bd8f26278d2317ef0ef1a8fb 1650w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?w=2500&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=1f6dd6a4d23ee579f73421689c4c2daa 2500w" />
</Frame>

You will be able to invoke individual tools with the help of the `#` sign in the chat view.

<Frame>
  <img src="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=76cbef68e48821a3c5467bd20c7e89fe" alt="Invoking MCP tools in VS Code." data-og-width="1276" width="1276" data-og-height="396" height="396" data-path="images/tutorial-authorization/tools-vs-code-invoke.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?w=280&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=7f5687389fe8bf48369a45738ec07795 280w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?w=560&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=dcc4a1857264bda9f2566e50db51704f 560w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?w=840&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=2774a73e612220975ee6d491430b9ee5 840w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?w=1100&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=014f88a40adddb9faf5f93306dea376c 1100w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?w=1650&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=d938978e4507cd933695cce01ee49901 1650w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?w=2500&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=0250d29b2e115324e0b94a4796938bad 2500w" />
</Frame>


## Common Pitfalls and How to Avoid Them

For comprehensive security guidance, including attack vectors, mitigation strategies, and implementation best practices, make sure to read through [Security Best Practices](/specification/draft/basic/security_best_practices). A few key issues are called out below.

* **Do not implement token validation or authorization logic by yourself**. Use off-the-shelf, well-tested, and secure libraries for things like token validation or authorization decisions. Doing everything from scratch means that you're more likely to implement things incorrectly unless you are a security expert.
* **Use short-lived access tokens**. Depending on the authorization server used, this setting might be customizable. We recommend to not use long-lived tokens - if a malicious actor steals them, they will be able to maintain their access for longer periods.
* **Always validate tokens**. Just because your server received a token does not mean that the token is valid or that it's meant for your server. Always verify that what your MCP server is getting from the client matches the required constraints.
* **Store tokens in secure, encrypted storage**. In certain scenarios, you might need to cache tokens server-side. If that is the case, ensure that the storage has the right access controls and cannot be easily exfiltrated by malicious parties with access to your server. You should also implement robust cache eviction policies to ensure that your MCP server is not re-using expired or otherwise invalid tokens.
* **Enforce HTTPS in production**. Do not accept tokens or redirect callbacks over plain HTTP except for `localhost` during development.
* **Least-privilege scopes**. Don't use catch‑all scopes. Split access per tool or capability where possible and verify required scopes per route/tool on the resource server.
* **Don't log credentials**. Never log `Authorization` headers, tokens, codes, or secrets. Scrub query strings and headers. Redact sensitive fields in structured logs.
* **Separate app vs. resource server credentials**. Don't reuse your MCP server's client secret for end‑user flows. Store all secrets in a proper secret manager, not in source control.
* **Return proper challenges**. On 401, include `WWW-Authenticate` with `Bearer`, `realm`, and `resource_metadata` so clients can discover how to authenticate.
* **DCR (Dynamic Client Registration) controls**. If enabled, be aware of constraints specific to your organization, such as trusted hosts, required vetting, and audited registrations. Unauthenticated DCR means that anyone can register any client with your authorization server.
* **Multi‑tenant/realm mix-ups**. Pin to a single issuer/tenant unless explicitly multi‑tenant. Reject tokens from other realms even if signed by the same authorization server.
* **Audience/resource indicator misuse**. Don't configure or accept generic audiences (like `api`) or unrelated resources. Require the audience/resource to match your configured server.
* **Error detail leakage**. Return generic messages to clients, but log detailed reasons with correlation IDs internally to aid troubleshooting without exposing internals.
* **Session identifier hardening**. Treat `Mcp-Session-Id` as untrusted input; never tie authorization to it. Regenerate on auth changes and validate lifecycle server‑side.


## Related Standards and Documentation

MCP authorization builds on these well-established standards:

* **[OAuth 2.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13)**: The core authorization framework
* **[RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414)**: Authorization Server Metadata discovery
* **[RFC 7591](https://datatracker.ietf.org/doc/html/rfc7591)**: Dynamic Client Registration
* **[RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728)**: Protected Resource Metadata
* **[RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707)**: Resource Indicators

For additional details, refer to:

* [Authorization Specification](/specification/draft/basic/authorization)
* [Security Best Practices](/specification/draft/basic/security_best_practices)
* [Available MCP SDKs](/docs/sdk)

Understanding these standards will help you implement authorization correctly and troubleshoot issues when they arise.



# Architecture
Source: https://modelcontextprotocol.io/specification/2025-06-18/architecture/index



<div id="enable-section-numbers" />

The Model Context Protocol (MCP) follows a client-host-server architecture where each
host can run multiple client instances. This architecture enables users to integrate AI
capabilities across applications while maintaining clear security boundaries and
isolating concerns. Built on JSON-RPC, MCP provides a stateful session protocol focused
on context exchange and sampling coordination between clients and servers.


## Core Components

```mermaid  theme={null}
graph LR
    subgraph "Application Host Process"
        H[Host]
        C1[Client 1]
        C2[Client 2]
        C3[Client 3]
        H --> C1
        H --> C2
        H --> C3
    end

    subgraph "Local machine"
        S1[Server 1<br>Files & Git]
        S2[Server 2<br>Database]
        R1[("Local<br>Resource A")]
        R2[("Local<br>Resource B")]

        C1 --> S1
        C2 --> S2
        S1 <--> R1
        S2 <--> R2
    end

    subgraph "Internet"
        S3[Server 3<br>External APIs]
        R3[("Remote<br>Resource C")]

        C3 --> S3
        S3 <--> R3
    end
```

### Host

The host process acts as the container and coordinator:

* Creates and manages multiple client instances
* Controls client connection permissions and lifecycle
* Enforces security policies and consent requirements
* Handles user authorization decisions
* Coordinates AI/LLM integration and sampling
* Manages context aggregation across clients

### Clients

Each client is created by the host and maintains an isolated server connection:

* Establishes one stateful session per server
* Handles protocol negotiation and capability exchange
* Routes protocol messages bidirectionally
* Manages subscriptions and notifications
* Maintains security boundaries between servers

A host application creates and manages multiple clients, with each client having a 1:1
relationship with a particular server.

### Servers

Servers provide specialized context and capabilities:

* Expose resources, tools and prompts via MCP primitives
* Operate independently with focused responsibilities
* Request sampling through client interfaces
* Must respect security constraints
* Can be local processes or remote services


## Design Principles

MCP is built on several key design principles that inform its architecture and
implementation:

1. **Servers should be extremely easy to build**
   * Host applications handle complex orchestration responsibilities
   * Servers focus on specific, well-defined capabilities
   * Simple interfaces minimize implementation overhead
   * Clear separation enables maintainable code

2. **Servers should be highly composable**
   * Each server provides focused functionality in isolation
   * Multiple servers can be combined seamlessly
   * Shared protocol enables interoperability
   * Modular design supports extensibility

3. **Servers should not be able to read the whole conversation, nor "see into" other
   servers**
   * Servers receive only necessary contextual information
   * Full conversation history stays with the host
   * Each server connection maintains isolation
   * Cross-server interactions are controlled by the host
   * Host process enforces security boundaries

4. **Features can be added to servers and clients progressively**
   * Core protocol provides minimal required functionality
   * Additional capabilities can be negotiated as needed
   * Servers and clients evolve independently
   * Protocol designed for future extensibility
   * Backwards compatibility is maintained


## Capability Negotiation

The Model Context Protocol uses a capability-based negotiation system where clients and
servers explicitly declare their supported features during initialization. Capabilities
determine which protocol features and primitives are available during a session.

* Servers declare capabilities like resource subscriptions, tool support, and prompt
  templates
* Clients declare capabilities like sampling support and notification handling
* Both parties must respect declared capabilities throughout the session
* Additional capabilities can be negotiated through extensions to the protocol

```mermaid  theme={null}
sequenceDiagram
    participant Host
    participant Client
    participant Server

    Host->>+Client: Initialize client
    Client->>+Server: Initialize session with capabilities
    Server-->>Client: Respond with supported capabilities

    Note over Host,Server: Active Session with Negotiated Features

    loop Client Requests
        Host->>Client: User- or model-initiated action
        Client->>Server: Request (tools/resources)
        Server-->>Client: Response
        Client-->>Host: Update UI or respond to model
    end

    loop Server Requests
        Server->>Client: Request (sampling)
        Client->>Host: Forward to AI
        Host-->>Client: AI response
        Client-->>Server: Response
    end

    loop Notifications
        Server--)Client: Resource updates
        Client--)Server: Status changes
    end

    Host->>Client: Terminate
    Client->>-Server: End session
    deactivate Server
```

Each capability unlocks specific protocol features for use during the session. For
example:

* Implemented [server features](/specification/2025-06-18/server) must be advertised in the
  server's capabilities
* Emitting resource subscription notifications requires the server to declare
  subscription support
* Tool invocation requires the server to declare tool capabilities
* [Sampling](/specification/2025-06-18/client) requires the client to declare support in its
  capabilities

This capability negotiation ensures clients and servers have a clear understanding of
supported functionality while maintaining protocol extensibility.



# Authorization
Source: https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization



<div id="enable-section-numbers" />

<Info>**Protocol Revision**: 2025-06-18</Info>


## Introduction

### Purpose and Scope

The Model Context Protocol provides authorization capabilities at the transport level,
enabling MCP clients to make requests to restricted MCP servers on behalf of resource
owners. This specification defines the authorization flow for HTTP-based transports.

### Protocol Requirements

Authorization is **OPTIONAL** for MCP implementations. When supported:

* Implementations using an HTTP-based transport **SHOULD** conform to this specification.
* Implementations using an STDIO transport **SHOULD NOT** follow this specification, and
  instead retrieve credentials from the environment.
* Implementations using alternative transports **MUST** follow established security best
  practices for their protocol.

### Standards Compliance

This authorization mechanism is based on established specifications listed below, but
implements a selected subset of their features to ensure security and interoperability
while maintaining simplicity:

* OAuth 2.1 IETF DRAFT ([draft-ietf-oauth-v2-1-13](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13))
* OAuth 2.0 Authorization Server Metadata
  ([RFC8414](https://datatracker.ietf.org/doc/html/rfc8414))
* OAuth 2.0 Dynamic Client Registration Protocol
  ([RFC7591](https://datatracker.ietf.org/doc/html/rfc7591))
* OAuth 2.0 Protected Resource Metadata ([RFC9728](https://datatracker.ietf.org/doc/html/rfc9728))


## Authorization Flow

### Roles

A protected *MCP server* acts as an [OAuth 2.1 resource server](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-13.html#name-roles),
capable of accepting and responding to protected resource requests using access tokens.

An *MCP client* acts as an [OAuth 2.1 client](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-13.html#name-roles),
making protected resource requests on behalf of a resource owner.

The *authorization server* is responsible for interacting with the user (if necessary) and issuing access tokens for use at the MCP server.
The implementation details of the authorization server are beyond the scope of this specification. It may be hosted with the
resource server or a separate entity. The [Authorization Server Discovery section](#authorization-server-discovery)
specifies how an MCP server indicates the location of its corresponding authorization server to a client.

### Overview

1. Authorization servers **MUST** implement OAuth 2.1 with appropriate security
   measures for both confidential and public clients.

2. Authorization servers and MCP clients **SHOULD** support the OAuth 2.0 Dynamic Client Registration
   Protocol ([RFC7591](https://datatracker.ietf.org/doc/html/rfc7591)).

3. MCP servers **MUST** implement OAuth 2.0 Protected Resource Metadata ([RFC9728](https://datatracker.ietf.org/doc/html/rfc9728)).
   MCP clients **MUST** use OAuth 2.0 Protected Resource Metadata for authorization server discovery.

4. Authorization servers **MUST** provide OAuth 2.0 Authorization
   Server Metadata ([RFC8414](https://datatracker.ietf.org/doc/html/rfc8414)).
   MCP clients **MUST** use the OAuth 2.0 Authorization Server Metadata.

### Authorization Server Discovery

This section describes the mechanisms by which MCP servers advertise their associated
authorization servers to MCP clients, as well as the discovery process through which MCP
clients can determine authorization server endpoints and supported capabilities.

#### Authorization Server Location

MCP servers **MUST** implement the OAuth 2.0 Protected Resource Metadata ([RFC9728](https://datatracker.ietf.org/doc/html/rfc9728))
specification to indicate the locations of authorization servers. The Protected Resource Metadata document returned by the MCP server **MUST** include
the `authorization_servers` field containing at least one authorization server.

The specific use of `authorization_servers` is beyond the scope of this specification; implementers should consult
OAuth 2.0 Protected Resource Metadata ([RFC9728](https://datatracker.ietf.org/doc/html/rfc9728)) for
guidance on implementation details.

Implementors should note that Protected Resource Metadata documents can define multiple authorization servers. The responsibility for selecting which authorization server to use lies with the MCP client, following the guidelines specified in
[RFC9728 Section 7.6 "Authorization Servers"](https://datatracker.ietf.org/doc/html/rfc9728#name-authorization-servers).

MCP servers **MUST** use the HTTP header `WWW-Authenticate` when returning a *401 Unauthorized* to indicate the location of the resource server metadata URL
as described in [RFC9728 Section 5.1 "WWW-Authenticate Response"](https://datatracker.ietf.org/doc/html/rfc9728#name-www-authenticate-response).

MCP clients **MUST** be able to parse `WWW-Authenticate` headers and respond appropriately to `HTTP 401 Unauthorized` responses from the MCP server.

#### Server Metadata Discovery

MCP clients **MUST** follow the OAuth 2.0 Authorization Server Metadata [RFC8414](https://datatracker.ietf.org/doc/html/rfc8414)
specification to obtain the information required to interact with the authorization server.

#### Sequence Diagram

The following diagram outlines an example flow:

```mermaid  theme={null}
sequenceDiagram
    participant C as Client
    participant M as MCP Server (Resource Server)
    participant A as Authorization Server

    C->>M: MCP request without token
    M-->>C: HTTP 401 Unauthorized with WWW-Authenticate header
    Note over C: Extract resource_metadata<br />from WWW-Authenticate

    C->>M: GET /.well-known/oauth-protected-resource
    M-->>C: Resource metadata with authorization server URL
    Note over C: Validate RS metadata,<br />build AS metadata URL

    C->>A: GET /.well-known/oauth-authorization-server
    A-->>C: Authorization server metadata

    Note over C,A: OAuth 2.1 authorization flow happens here

    C->>A: Token request
    A-->>C: Access token

    C->>M: MCP request with access token
    M-->>C: MCP response
    Note over C,M: MCP communication continues with valid token
```

### Dynamic Client Registration

MCP clients and authorization servers **SHOULD** support the
OAuth 2.0 Dynamic Client Registration Protocol [RFC7591](https://datatracker.ietf.org/doc/html/rfc7591)
to allow MCP clients to obtain OAuth client IDs without user interaction. This provides a
standardized way for clients to automatically register with new authorization servers, which is crucial
for MCP because:

* Clients may not know all possible MCP servers and their authorization servers in advance.
* Manual registration would create friction for users.
* It enables seamless connection to new MCP servers and their authorization servers.
* Authorization servers can implement their own registration policies.

Any authorization servers that *do not* support Dynamic Client Registration need to provide
alternative ways to obtain a client ID (and, if applicable, client credentials). For one of
these authorization servers, MCP clients will have to either:

1. Hardcode a client ID (and, if applicable, client credentials) specifically for the MCP client to use when
   interacting with that authorization server, or
2. Present a UI to users that allows them to enter these details, after registering an
   OAuth client themselves (e.g., through a configuration interface hosted by the
   server).

### Authorization Flow Steps

The complete Authorization flow proceeds as follows:

```mermaid  theme={null}
sequenceDiagram
    participant B as User-Agent (Browser)
    participant C as Client
    participant M as MCP Server (Resource Server)
    participant A as Authorization Server

    C->>M: MCP request without token
    M->>C: HTTP 401 Unauthorized with WWW-Authenticate header
    Note over C: Extract resource_metadata URL from WWW-Authenticate

    C->>M: Request Protected Resource Metadata
    M->>C: Return metadata

    Note over C: Parse metadata and extract authorization server(s)<br/>Client determines AS to use

    C->>A: GET /.well-known/oauth-authorization-server
    A->>C: Authorization server metadata response

    alt Dynamic client registration
        C->>A: POST /register
        A->>C: Client Credentials
    end

    Note over C: Generate PKCE parameters<br/>Include resource parameter
    C->>B: Open browser with authorization URL + code_challenge + resource
    B->>A: Authorization request with resource parameter
    Note over A: User authorizes
    A->>B: Redirect to callback with authorization code
    B->>C: Authorization code callback
    C->>A: Token request + code_verifier + resource
    A->>C: Access token (+ refresh token)
    C->>M: MCP request with access token
    M-->>C: MCP response
    Note over C,M: MCP communication continues with valid token
```

#### Resource Parameter Implementation

MCP clients **MUST** implement Resource Indicators for OAuth 2.0 as defined in [RFC 8707](https://www.rfc-editor.org/rfc/rfc8707.html)
to explicitly specify the target resource for which the token is being requested. The `resource` parameter:

1. **MUST** be included in both authorization requests and token requests.
2. **MUST** identify the MCP server that the client intends to use the token with.
3. **MUST** use the canonical URI of the MCP server as defined in [RFC 8707 Section 2](https://www.rfc-editor.org/rfc/rfc8707.html#name-access-token-request).

##### Canonical Server URI

For the purposes of this specification, the canonical URI of an MCP server is defined as the resource identifier as specified in
[RFC 8707 Section 2](https://www.rfc-editor.org/rfc/rfc8707.html#section-2) and aligns with the `resource` parameter in
[RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728).

MCP clients **SHOULD** provide the most specific URI that they can for the MCP server they intend to access, following the guidance in [RFC 8707](https://www.rfc-editor.org/rfc/rfc8707). While the canonical form uses lowercase scheme and host components, implementations **SHOULD** accept uppercase scheme and host components for robustness and interoperability.

Examples of valid canonical URIs:

* `https://mcp.example.com/mcp`
* `https://mcp.example.com`
* `https://mcp.example.com:8443`
* `https://mcp.example.com/server/mcp` (when path component is necessary to identify individual MCP server)

Examples of invalid canonical URIs:

* `mcp.example.com` (missing scheme)
* `https://mcp.example.com#fragment` (contains fragment)

> **Note:** While both `https://mcp.example.com/` (with trailing slash) and `https://mcp.example.com` (without trailing slash) are technically valid absolute URIs according to [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986), implementations **SHOULD** consistently use the form without the trailing slash for better interoperability unless the trailing slash is semantically significant for the specific resource.

For example, if accessing an MCP server at `https://mcp.example.com`, the authorization request would include:

```
&resource=https%3A%2F%2Fmcp.example.com
```

MCP clients **MUST** send this parameter regardless of whether authorization servers support it.

### Access Token Usage

#### Token Requirements

Access token handling when making requests to MCP servers **MUST** conform to the requirements defined in
[OAuth 2.1 Section 5 "Resource Requests"](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13#section-5).
Specifically:

1. MCP client **MUST** use the Authorization request header field defined in
   [OAuth 2.1 Section 5.1.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13#section-5.1.1):

```
Authorization: Bearer <access-token>
```

Note that authorization **MUST** be included in every HTTP request from client to server,
even if they are part of the same logical session.

2. Access tokens **MUST NOT** be included in the URI query string

Example request:

```http  theme={null}
GET /mcp HTTP/1.1
Host: mcp.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

#### Token Handling

MCP servers, acting in their role as an OAuth 2.1 resource server, **MUST** validate access tokens as described in
[OAuth 2.1 Section 5.2](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13#section-5.2).
MCP servers **MUST** validate that access tokens were issued specifically for them as the intended audience,
according to [RFC 8707 Section 2](https://www.rfc-editor.org/rfc/rfc8707.html#section-2).
If validation fails, servers **MUST** respond according to
[OAuth 2.1 Section 5.3](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13#section-5.3)
error handling requirements. Invalid or expired tokens **MUST** receive a HTTP 401
response.

MCP clients **MUST NOT** send tokens to the MCP server other than ones issued by the MCP server's authorization server.

Authorization servers **MUST** only accept tokens that are valid for use with their
own resources.

MCP servers **MUST NOT** accept or transit any other tokens.

### Error Handling

Servers **MUST** return appropriate HTTP status codes for authorization errors:

| Status Code | Description  | Usage                                      |
| ----------- | ------------ | ------------------------------------------ |
| 401         | Unauthorized | Authorization required or token invalid    |
| 403         | Forbidden    | Invalid scopes or insufficient permissions |
| 400         | Bad Request  | Malformed authorization request            |


## Security Considerations

Implementations **MUST** follow OAuth 2.1 security best practices as laid out in [OAuth 2.1 Section 7. "Security Considerations"](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13#name-security-considerations).

### Token Audience Binding and Validation

[RFC 8707](https://www.rfc-editor.org/rfc/rfc8707.html) Resource Indicators provide critical security benefits by binding tokens to their intended
audiences **when the Authorization Server supports the capability**. To enable current and future adoption:

* MCP clients **MUST** include the `resource` parameter in authorization and token requests as specified in the [Resource Parameter Implementation](#resource-parameter-implementation) section
* MCP servers **MUST** validate that tokens presented to them were specifically issued for their use

The [Security Best Practices document](/specification/2025-06-18/basic/security_best_practices#token-passthrough)
outlines why token audience validation is crucial and why token passthrough is explicitly forbidden.

### Token Theft

Attackers who obtain tokens stored by the client, or tokens cached or logged on the server can access protected resources with
requests that appear legitimate to resource servers.

Clients and servers **MUST** implement secure token storage and follow OAuth best practices,
as outlined in [OAuth 2.1, Section 7.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13#section-7.1).

Authorization servers **SHOULD** issue short-lived access tokens to reduce the impact of leaked tokens.
For public clients, authorization servers **MUST** rotate refresh tokens as described in [OAuth 2.1 Section 4.3.1 "Token Endpoint Extension"](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13#section-4.3.1).

### Communication Security

Implementations **MUST** follow [OAuth 2.1 Section 1.5 "Communication Security"](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13#section-1.5).

Specifically:

1. All authorization server endpoints **MUST** be served over HTTPS.
2. All redirect URIs **MUST** be either `localhost` or use HTTPS.

### Authorization Code Protection

An attacker who has gained access to an authorization code contained in an authorization response can try to redeem the authorization code for an access token or otherwise make use of the authorization code.
(Further described in [OAuth 2.1 Section 7.5](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13#section-7.5))

To mitigate this, MCP clients **MUST** implement PKCE according to [OAuth 2.1 Section 7.5.2](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13#section-7.5.2).
PKCE helps prevent authorization code interception and injection attacks by requiring clients to create a secret verifier-challenge pair, ensuring that only the original requestor can exchange an authorization code for tokens.

### Open Redirection

An attacker may craft malicious redirect URIs to direct users to phishing sites.

MCP clients **MUST** have redirect URIs registered with the authorization server.

Authorization servers **MUST** validate exact redirect URIs against pre-registered values to prevent redirection attacks.

MCP clients **SHOULD** use and verify state parameters in the authorization code flow
and discard any results that do not include or have a mismatch with the original state.

Authorization servers **MUST** take precautions to prevent redirecting user agents to untrusted URI's, following suggestions laid out in [OAuth 2.1 Section 7.12.2](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13#section-7.12.2)

Authorization servers **SHOULD** only automatically redirect the user agent if it trusts the redirection URI. If the URI is not trusted, the authorization server MAY inform the user and rely on the user to make the correct decision.

### Confused Deputy Problem

Attackers can exploit MCP servers acting as intermediaries to third-party APIs, leading to [confused deputy vulnerabilities](/specification/2025-06-18/basic/security_best_practices#confused-deputy-problem).
By using stolen authorization codes, they can obtain access tokens without user consent.

MCP proxy servers using static client IDs **MUST** obtain user consent for each dynamically
registered client before forwarding to third-party authorization servers (which may require additional consent).

### Access Token Privilege Restriction

An attacker can gain unauthorized access or otherwise compromise an MCP server if the server accepts tokens issued for other resources.

This vulnerability has two critical dimensions:

1. **Audience validation failures.** When an MCP server doesn't verify that tokens were specifically intended for it (for example, via the audience claim, as mentioned in [RFC9068](https://www.rfc-editor.org/rfc/rfc9068.html)), it may accept tokens originally issued for other services. This breaks a fundamental OAuth security boundary, allowing attackers to reuse legitimate tokens across different services than intended.
2. **Token passthrough.** If the MCP server not only accepts tokens with incorrect audiences but also forwards these unmodified tokens to downstream services, it can potentially cause the ["confused deputy" problem](#confused-deputy-problem), where the downstream API may incorrectly trust the token as if it came from the MCP server or assume the token was validated by the upstream API. See the [Token Passthrough section](/specification/2025-06-18/basic/security_best_practices#token-passthrough) of the Security Best Practices guide for additional details.

MCP servers **MUST** validate access tokens before processing the request, ensuring the access token is issued specifically for the MCP server, and take all necessary steps to ensure no data is returned to unauthorized parties.

A MCP server **MUST** follow the guidelines in [OAuth 2.1 - Section 5.2](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-13.html#section-5.2) to validate inbound tokens.

MCP servers **MUST** only accept tokens specifically intended for themselves and **MUST** reject tokens that do not include them in the audience claim or otherwise verify that they are the intended recipient of the token. See the [Security Best Practices Token Passthrough section](/specification/2025-06-18/basic/security_best_practices#token-passthrough) for details.

If the MCP server makes requests to upstream APIs, it may act as an OAuth client to them. The access token used at the upstream API is a separate token, issued by the upstream authorization server. The MCP server **MUST NOT** pass through the token it received from the MCP client.

MCP clients **MUST** implement and use the `resource` parameter as defined in [RFC 8707 - Resource Indicators for OAuth 2.0](https://www.rfc-editor.org/rfc/rfc8707.html)
to explicitly specify the target resource for which the token is being requested. This requirement aligns with the recommendation in
[RFC 9728 Section 7.4](https://datatracker.ietf.org/doc/html/rfc9728#section-7.4). This ensures that access tokens are bound to their intended resources and
cannot be misused across different services.



# Overview
Source: https://modelcontextprotocol.io/specification/2025-06-18/basic/index



<div id="enable-section-numbers" />

<Info>**Protocol Revision**: 2025-06-18</Info>

The Model Context Protocol consists of several key components that work together:

* **Base Protocol**: Core JSON-RPC message types
* **Lifecycle Management**: Connection initialization, capability negotiation, and
  session control
* **Authorization**: Authentication and authorization framework for HTTP-based transports
* **Server Features**: Resources, prompts, and tools exposed by servers
* **Client Features**: Sampling and root directory lists provided by clients
* **Utilities**: Cross-cutting concerns like logging and argument completion

All implementations **MUST** support the base protocol and lifecycle management
components. Other components **MAY** be implemented based on the specific needs of the
application.

These protocol layers establish clear separation of concerns while enabling rich
interactions between clients and servers. The modular design allows implementations to
support exactly the features they need.


## Messages

All messages between MCP clients and servers **MUST** follow the
[JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification. The protocol defines
these types of messages:

### Requests

Requests are sent from the client to the server or vice versa, to initiate an operation.

```typescript  theme={null}
{
  jsonrpc: "2.0";
  id: string | number;
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

* Requests **MUST** include a string or integer ID.
* Unlike base JSON-RPC, the ID **MUST NOT** be `null`.
* The request ID **MUST NOT** have been previously used by the requestor within the same
  session.

### Responses

Responses are sent in reply to requests, containing the result or error of the operation.

```typescript  theme={null}
{
  jsonrpc: "2.0";
  id: string | number;
  result?: {
    [key: string]: unknown;
  }
  error?: {
    code: number;
    message: string;
    data?: unknown;
  }
}
```

* Responses **MUST** include the same ID as the request they correspond to.
* **Responses** are further sub-categorized as either **successful results** or
  **errors**. Either a `result` or an `error` **MUST** be set. A response **MUST NOT**
  set both.
* Results **MAY** follow any JSON object structure, while errors **MUST** include an
  error code and message at minimum.
* Error codes **MUST** be integers.

### Notifications

Notifications are sent from the client to the server or vice versa, as a one-way message.
The receiver **MUST NOT** send a response.

```typescript  theme={null}
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

* Notifications **MUST NOT** include an ID.


## Auth

MCP provides an [Authorization](/specification/2025-06-18/basic/authorization) framework for use with HTTP.
Implementations using an HTTP-based transport **SHOULD** conform to this specification,
whereas implementations using STDIO transport **SHOULD NOT** follow this specification,
and instead retrieve credentials from the environment.

Additionally, clients and servers **MAY** negotiate their own custom authentication and
authorization strategies.

For further discussions and contributions to the evolution of MCP’s auth mechanisms, join
us in
[GitHub Discussions](https://github.com/modelcontextprotocol/specification/discussions)
to help shape the future of the protocol!


## Schema

The full specification of the protocol is defined as a
[TypeScript schema](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-06-18/schema.ts).
This is the source of truth for all protocol messages and structures.

There is also a
[JSON Schema](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-06-18/schema.json),
which is automatically generated from the TypeScript source of truth, for use with
various automated tooling.

### General fields

#### `_meta`

The `_meta` property/parameter is reserved by MCP to allow clients and servers
to attach additional metadata to their interactions.

Certain key names are reserved by MCP for protocol-level metadata, as specified below;
implementations MUST NOT make assumptions about values at these keys.

Additionally, definitions in the [schema](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-06-18/schema.ts)
may reserve particular names for purpose-specific metadata, as declared in those definitions.

**Key name format:** valid `_meta` key names have two segments: an optional **prefix**, and a **name**.

**Prefix:**

* If specified, MUST be a series of labels separated by dots (`.`), followed by a slash (`/`).
  * Labels MUST start with a letter and end with a letter or digit; interior characters can be letters, digits, or hyphens (`-`).
* Any prefix beginning with zero or more valid labels, followed by `modelcontextprotocol` or `mcp`, followed by any valid label,
  is **reserved** for MCP use.
  * For example: `modelcontextprotocol.io/`, `mcp.dev/`, `api.modelcontextprotocol.org/`, and `tools.mcp.com/` are all reserved.

**Name:**

* Unless empty, MUST begin and end with an alphanumeric character (`[a-z0-9A-Z]`).
* MAY contain hyphens (`-`), underscores (`_`), dots (`.`), and alphanumerics in between.



# Lifecycle
Source: https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle



<div id="enable-section-numbers" />

<Info>**Protocol Revision**: 2025-06-18</Info>

The Model Context Protocol (MCP) defines a rigorous lifecycle for client-server
connections that ensures proper capability negotiation and state management.

1. **Initialization**: Capability negotiation and protocol version agreement
2. **Operation**: Normal protocol communication
3. **Shutdown**: Graceful termination of the connection

```mermaid  theme={null}
sequenceDiagram
    participant Client
    participant Server

    Note over Client,Server: Initialization Phase
    activate Client
    Client->>+Server: initialize request
    Server-->>Client: initialize response
    Client--)Server: initialized notification

    Note over Client,Server: Operation Phase
    rect rgb(200, 220, 250)
        note over Client,Server: Normal protocol operations
    end

    Note over Client,Server: Shutdown
    Client--)-Server: Disconnect
    deactivate Server
    Note over Client,Server: Connection closed
```


## Lifecycle Phases

### Initialization

The initialization phase **MUST** be the first interaction between client and server.
During this phase, the client and server:

* Establish protocol version compatibility
* Exchange and negotiate capabilities
* Share implementation details

The client **MUST** initiate this phase by sending an `initialize` request containing:

* Protocol version supported
* Client capabilities
* Client implementation information

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "roots": {
        "listChanged": true
      },
      "sampling": {},
      "elicitation": {}
    },
    "clientInfo": {
      "name": "ExampleClient",
      "title": "Example Client Display Name",
      "version": "1.0.0"
    }
  }
}
```

The server **MUST** respond with its own capabilities and information:

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "logging": {},
      "prompts": {
        "listChanged": true
      },
      "resources": {
        "subscribe": true,
        "listChanged": true
      },
      "tools": {
        "listChanged": true
      }
    },
    "serverInfo": {
      "name": "ExampleServer",
      "title": "Example Server Display Name",
      "version": "1.0.0"
    },
    "instructions": "Optional instructions for the client"
  }
}
```

After successful initialization, the client **MUST** send an `initialized` notification
to indicate it is ready to begin normal operations:

```json  theme={null}
{
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```

* The client **SHOULD NOT** send requests other than
  [pings](/specification/2025-06-18/basic/utilities/ping) before the server has responded to the
  `initialize` request.
* The server **SHOULD NOT** send requests other than
  [pings](/specification/2025-06-18/basic/utilities/ping) and
  [logging](/specification/2025-06-18/server/utilities/logging) before receiving the `initialized`
  notification.

#### Version Negotiation

In the `initialize` request, the client **MUST** send a protocol version it supports.
This **SHOULD** be the *latest* version supported by the client.

If the server supports the requested protocol version, it **MUST** respond with the same
version. Otherwise, the server **MUST** respond with another protocol version it
supports. This **SHOULD** be the *latest* version supported by the server.

If the client does not support the version in the server's response, it **SHOULD**
disconnect.

<Note>
  If using HTTP, the client **MUST** include the `MCP-Protocol-Version: <protocol-version>` HTTP header on all subsequent requests to the MCP
  server.
  For details, see [the Protocol Version Header section in Transports](/specification/2025-06-18/basic/transports#protocol-version-header).
</Note>

#### Capability Negotiation

Client and server capabilities establish which optional protocol features will be
available during the session.

Key capabilities include:

| Category | Capability     | Description                                                                               |
| -------- | -------------- | ----------------------------------------------------------------------------------------- |
| Client   | `roots`        | Ability to provide filesystem [roots](/specification/2025-06-18/client/roots)             |
| Client   | `sampling`     | Support for LLM [sampling](/specification/2025-06-18/client/sampling) requests            |
| Client   | `elicitation`  | Support for server [elicitation](/specification/2025-06-18/client/elicitation) requests   |
| Client   | `experimental` | Describes support for non-standard experimental features                                  |
| Server   | `prompts`      | Offers [prompt templates](/specification/2025-06-18/server/prompts)                       |
| Server   | `resources`    | Provides readable [resources](/specification/2025-06-18/server/resources)                 |
| Server   | `tools`        | Exposes callable [tools](/specification/2025-06-18/server/tools)                          |
| Server   | `logging`      | Emits structured [log messages](/specification/2025-06-18/server/utilities/logging)       |
| Server   | `completions`  | Supports argument [autocompletion](/specification/2025-06-18/server/utilities/completion) |
| Server   | `experimental` | Describes support for non-standard experimental features                                  |

Capability objects can describe sub-capabilities like:

* `listChanged`: Support for list change notifications (for prompts, resources, and
  tools)
* `subscribe`: Support for subscribing to individual items' changes (resources only)

### Operation

During the operation phase, the client and server exchange messages according to the
negotiated capabilities.

Both parties **MUST**:

* Respect the negotiated protocol version
* Only use capabilities that were successfully negotiated

### Shutdown

During the shutdown phase, one side (usually the client) cleanly terminates the protocol
connection. No specific shutdown messages are defined—instead, the underlying transport
mechanism should be used to signal connection termination:

#### stdio

For the stdio [transport](/specification/2025-06-18/basic/transports), the client **SHOULD** initiate
shutdown by:

1. First, closing the input stream to the child process (the server)
2. Waiting for the server to exit, or sending `SIGTERM` if the server does not exit
   within a reasonable time
3. Sending `SIGKILL` if the server does not exit within a reasonable time after `SIGTERM`

The server **MAY** initiate shutdown by closing its output stream to the client and
exiting.

#### HTTP

For HTTP [transports](/specification/2025-06-18/basic/transports), shutdown is indicated by closing the
associated HTTP connection(s).


## Timeouts

Implementations **SHOULD** establish timeouts for all sent requests, to prevent hung
connections and resource exhaustion. When the request has not received a success or error
response within the timeout period, the sender **SHOULD** issue a [cancellation
notification](/specification/2025-06-18/basic/utilities/cancellation) for that request and stop waiting for
a response.

SDKs and other middleware **SHOULD** allow these timeouts to be configured on a
per-request basis.

Implementations **MAY** choose to reset the timeout clock when receiving a [progress
notification](/specification/2025-06-18/basic/utilities/progress) corresponding to the request, as this
implies that work is actually happening. However, implementations **SHOULD** always
enforce a maximum timeout, regardless of progress notifications, to limit the impact of a
misbehaving client or server.


## Error Handling

Implementations **SHOULD** be prepared to handle these error cases:

* Protocol version mismatch
* Failure to negotiate required capabilities
* Request [timeouts](#timeouts)

Example initialization error:

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Unsupported protocol version",
    "data": {
      "supported": ["2024-11-05"],
      "requested": "1.0.0"
    }
  }
}
```



# Security Best Practices
Source: https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices



<div id="enable-section-numbers" />


## Introduction

### Purpose and Scope

This document provides security considerations for the Model Context Protocol (MCP), complementing the MCP Authorization specification. This document identifies security risks, attack vectors, and best practices specific to MCP implementations.

The primary audience for this document includes developers implementing MCP authorization flows, MCP server operators, and security professionals evaluating MCP-based systems. This document should be read alongside the MCP Authorization specification and [OAuth 2.0 security best practices](https://datatracker.ietf.org/doc/html/rfc9700).


## Attacks and Mitigations

This section gives a detailed description of attacks on MCP implementations, along with potential countermeasures.

### Confused Deputy Problem

Attackers can exploit MCP servers proxying other resource servers, creating "[confused deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem)" vulnerabilities.

#### Terminology

**MCP Proxy Server**
: An MCP server that connects MCP clients to third-party APIs, offering MCP features while delegating operations and acting as a single OAuth client to the third-party API server.

**Third-Party Authorization Server**
: Authorization server that protects the third-party API. It may lack dynamic client registration support, requiring MCP proxy to use a static client ID for all requests.

**Third-Party API**
: The protected resource server that provides the actual API functionality. Access to this
API requires tokens issued by the third-party authorization server.

**Static Client ID**
: A fixed OAuth 2.0 client identifier used by the MCP proxy server when communicating with
the third-party authorization server. This Client ID refers to the MCP server acting as a client
to the Third-Party API. It is the same value for all MCP server to Third-Party API interactions regardless of
which MCP client initiated the request.

#### Architecture and Attack Flows

##### Normal OAuth proxy usage (preserves user consent)

```mermaid  theme={null}
sequenceDiagram
    participant UA as User-Agent (Browser)
    participant MC as MCP Client
    participant M as MCP Proxy Server
    participant TAS as Third-Party Authorization Server

    Note over UA,M: Initial Auth flow completed

    Note over UA,TAS: Step 1: Legitimate user consent for Third Party Server

    M->>UA: Redirect to third party authorization server
    UA->>TAS: Authorization request (client_id: mcp-proxy)
    TAS->>UA: Authorization consent screen
    Note over UA: Review consent screen
    UA->>TAS: Approve
    TAS->>UA: Set consent cookie for client ID: mcp-proxy
    TAS->>UA: 3P Authorization code + redirect to mcp-proxy-server.com
    UA->>M: 3P Authorization code
    Note over M,TAS: Exchange 3P code for 3P token
    Note over M: Generate MCP authorization code
    M->>UA: Redirect to MCP Client with MCP authorization code

    Note over M,UA: Exchange code for token, etc.
```

##### Malicious OAuth proxy usage (skips user consent)

```mermaid  theme={null}
sequenceDiagram
    participant UA as User-Agent (Browser)
    participant M as MCP Proxy Server
    participant TAS as Third-Party Authorization Server
    participant A as Attacker


    Note over UA,A: Step 2: Attack (leveraging existing cookie, skipping consent)
    A->>M: Dynamically register malicious client, redirect_uri: attacker.com
    A->>UA: Sends malicious link
    UA->>TAS: Authorization request (client_id: mcp-proxy) + consent cookie
    rect rgba(255, 17, 0, 0.67)
    TAS->>TAS: Cookie present, consent skipped
    end

   TAS->>UA: 3P Authorization code + redirect to mcp-proxy-server.com
   UA->>M: 3P Authorization code
   Note over M,TAS: Exchange 3P code for 3P token
   Note over M: Generate MCP authorization code
   M->>UA: Redirect to attacker.com with MCP Authorization code
   UA->>A: MCP Authorization code delivered to attacker.com
   Note over M,A: Attacker exchanges MCP code for MCP token
   A->>M: Attacker impersonates user to MCP server
```

#### Attack Description

When an MCP proxy server uses a static client ID to authenticate with a third-party
authorization server that does not support dynamic client registration, the following
attack becomes possible:

1. A user authenticates normally through the MCP proxy server to access the third-party API
2. During this flow, the third-party authorization server sets a cookie on the user agent
   indicating consent for the static client ID
3. An attacker later sends the user a malicious link containing a crafted authorization request which contains a malicious redirect URI along with a new dynamically registered client ID
4. When the user clicks the link, their browser still has the consent cookie from the previous legitimate request
5. The third-party authorization server detects the cookie and skips the consent screen
6. The MCP authorization code is redirected to the attacker's server (specified in the crafted redirect\_uri during dynamic client registration)
7. The attacker exchanges the stolen authorization code for access tokens for the MCP server without the user's explicit approval
8. Attacker now has access to the third-party API as the compromised user

#### Mitigation

MCP proxy servers using static client IDs **MUST** obtain user consent for each dynamically
registered client before forwarding to third-party authorization servers (which may require additional consent).

### Token Passthrough

"Token passthrough" is an anti-pattern where an MCP server accepts tokens from an MCP client without validating that the tokens were properly issued *to the MCP server* and "passing them through" to the downstream API.

#### Risks

Token passthrough is explicitly forbidden in the [authorization specification](/specification/2025-06-18/basic/authorization) as it introduces a number of security risks, that include:

* **Security Control Circumvention**
  * The MCP Server or downstream APIs might implement important security controls like rate limiting, request validation, or traffic monitoring, that depend on the token audience or other credential constraints. If clients can obtain and use tokens directly with the downstream APIs without the MCP server validating them properly or ensuring that the tokens are issued for the right service, they bypass these controls.
* **Accountability and Audit Trail Issues**
  * The MCP Server will be unable to identify or distinguish between MCP Clients when clients are calling with an upstream-issued access token which may be opaque to the MCP Server.
  * The downstream Resource Server’s logs may show requests that appear to come from a different source with a different identity, rather than the MCP server that is actually forwarding the tokens.
  * Both factors make incident investigation, controls, and auditing more difficult.
  * If the MCP Server passes tokens without validating their claims (e.g., roles, privileges, or audience) or other metadata, a malicious actor in possession of a stolen token can use the server as a proxy for data exfiltration.
* **Trust Boundary Issues**
  * The downstream Resource Server grants trust to specific entities. This trust might include assumptions about origin or client behavior patterns. Breaking this trust boundary could lead to unexpected issues.
  * If the token is accepted by multiple services without proper validation, an attacker compromising one service can use the token to access other connected services.
* **Future Compatibility Risk**
  * Even if an MCP Server starts as a "pure proxy" today, it might need to add security controls later. Starting with proper token audience separation makes it easier to evolve the security model.

#### Mitigation

MCP servers **MUST NOT** accept any tokens that were not explicitly issued for the MCP server.

### Session Hijacking

Session hijacking is an attack vector where a client is provided a session ID by the server, and an unauthorized party is able to obtain and use that same session ID to impersonate the original client and perform unauthorized actions on their behalf.

#### Session Hijack Prompt Injection

```mermaid  theme={null}
sequenceDiagram
    participant Client
    participant ServerA
    participant Queue
    participant ServerB
    participant Attacker

    Client->>ServerA: Initialize (connect to streamable HTTP server)
    ServerA-->>Client: Respond with session ID

    Attacker->>ServerB: Access/guess session ID
    Note right of Attacker: Attacker knows/guesses session ID

    Attacker->>ServerB: Trigger event (malicious payload, using session ID)
    ServerB->>Queue: Enqueue event (keyed by session ID)

    ServerA->>Queue: Poll for events (using session ID)
    Queue-->>ServerA: Event data (malicious payload)

    ServerA-->>Client: Async response (malicious payload)
    Client->>Client: Acts based on malicious payload
```

#### Session Hijack Impersonation

```mermaid  theme={null}
sequenceDiagram
    participant Client
    participant Server
    participant Attacker

    Client->>Server: Initialize (login/authenticate)
    Server-->>Client: Respond with session ID (persistent session created)

    Attacker->>Server: Access/guess session ID
    Note right of Attacker: Attacker knows/guesses session ID

    Attacker->>Server: Make API call (using session ID, no re-auth)
    Server-->>Attacker: Respond as if Attacker is Client (session hijack)
```

#### Attack Description

When you have multiple stateful HTTP servers that handle MCP requests, the following attack vectors are possible:

**Session Hijack Prompt Injection**

1. The client connects to **Server A** and receives a session ID.

2. The attacker obtains an existing session ID and sends a malicious event to **Server B** with said session ID.
   * When a server supports [redelivery/resumable streams](/specification/2025-06-18/basic/transports#resumability-and-redelivery), deliberately terminating the request before receiving the response could lead to it being resumed by the original client via the GET request for server sent events.
   * If a particular server initiates server sent events as a consequence of a tool call such as a `notifications/tools/list_changed`, where it is possible to affect the tools that are offered by the server, a client could end up with tools that they were not aware were enabled.

3. **Server B** enqueues the event (associated with session ID) into a shared queue.

4. **Server A** polls the queue for events using the session ID and retrieves the malicious payload.

5. **Server A** sends the malicious payload to the client as an asynchronous or resumed response.

6. The client receives and acts on the malicious payload, leading to potential compromise.

**Session Hijack Impersonation**

1. The MCP client authenticates with the MCP server, creating a persistent session ID.
2. The attacker obtains the session ID.
3. The attacker makes calls to the MCP server using the session ID.
4. MCP server does not check for additional authorization and treats the attacker as a legitimate user, allowing unauthorized access or actions.

#### Mitigation

To prevent session hijacking and event injection attacks, the following mitigations should be implemented:

MCP servers that implement authorization **MUST** verify all inbound requests.
MCP Servers **MUST NOT** use sessions for authentication.

MCP servers **MUST** use secure, non-deterministic session IDs.
Generated session IDs (e.g., UUIDs) **SHOULD** use secure random number generators. Avoid predictable or sequential session identifiers that could be guessed by an attacker. Rotating or expiring session IDs can also reduce the risk.

MCP servers **SHOULD** bind session IDs to user-specific information.
When storing or transmitting session-related data (e.g., in a queue), combine the session ID with information unique to the authorized user, such as their internal user ID. Use a key format like `<user_id>:<session_id>`. This ensures that even if an attacker guesses a session ID, they cannot impersonate another user as the user ID is derived from the user token and not provided by the client.

MCP servers can optionally leverage additional unique identifiers.



# Transports
Source: https://modelcontextprotocol.io/specification/2025-06-18/basic/transports



<div id="enable-section-numbers" />

<Info>**Protocol Revision**: 2025-06-18</Info>

MCP uses JSON-RPC to encode messages. JSON-RPC messages **MUST** be UTF-8 encoded.

The protocol currently defines two standard transport mechanisms for client-server
communication:

1. [stdio](#stdio), communication over standard in and standard out
2. [Streamable HTTP](#streamable-http)

Clients **SHOULD** support stdio whenever possible.

It is also possible for clients and servers to implement
[custom transports](#custom-transports) in a pluggable fashion.


## stdio

In the **stdio** transport:

* The client launches the MCP server as a subprocess.
* The server reads JSON-RPC messages from its standard input (`stdin`) and sends messages
  to its standard output (`stdout`).
* Messages are individual JSON-RPC requests, notifications, or responses.
* Messages are delimited by newlines, and **MUST NOT** contain embedded newlines.
* The server **MAY** write UTF-8 strings to its standard error (`stderr`) for logging
  purposes. Clients **MAY** capture, forward, or ignore this logging.
* The server **MUST NOT** write anything to its `stdout` that is not a valid MCP message.
* The client **MUST NOT** write anything to the server's `stdin` that is not a valid MCP
  message.

```mermaid  theme={null}
sequenceDiagram
    participant Client
    participant Server Process

    Client->>+Server Process: Launch subprocess
    loop Message Exchange
        Client->>Server Process: Write to stdin
        Server Process->>Client: Write to stdout
        Server Process--)Client: Optional logs on stderr
    end
    Client->>Server Process: Close stdin, terminate subprocess
    deactivate Server Process
```


## Streamable HTTP

<Info>
  This replaces the [HTTP+SSE
  transport](/specification/2024-11-05/basic/transports#http-with-sse) from
  protocol version 2024-11-05. See the [backwards compatibility](#backwards-compatibility)
  guide below.
</Info>

In the **Streamable HTTP** transport, the server operates as an independent process that
can handle multiple client connections. This transport uses HTTP POST and GET requests.
Server can optionally make use of
[Server-Sent Events](https://en.wikipedia.org/wiki/Server-sent_events) (SSE) to stream
multiple server messages. This permits basic MCP servers, as well as more feature-rich
servers supporting streaming and server-to-client notifications and requests.

The server **MUST** provide a single HTTP endpoint path (hereafter referred to as the
**MCP endpoint**) that supports both POST and GET methods. For example, this could be a
URL like `https://example.com/mcp`.

#### Security Warning

When implementing Streamable HTTP transport:

1. Servers **MUST** validate the `Origin` header on all incoming connections to prevent DNS rebinding attacks
2. When running locally, servers **SHOULD** bind only to localhost (127.0.0.1) rather than all network interfaces (0.0.0.0)
3. Servers **SHOULD** implement proper authentication for all connections

Without these protections, attackers could use DNS rebinding to interact with local MCP servers from remote websites.

### Sending Messages to the Server

Every JSON-RPC message sent from the client **MUST** be a new HTTP POST request to the
MCP endpoint.

1. The client **MUST** use HTTP POST to send JSON-RPC messages to the MCP endpoint.
2. The client **MUST** include an `Accept` header, listing both `application/json` and
   `text/event-stream` as supported content types.
3. The body of the POST request **MUST** be a single JSON-RPC *request*, *notification*, or *response*.
4. If the input is a JSON-RPC *response* or *notification*:
   * If the server accepts the input, the server **MUST** return HTTP status code 202
     Accepted with no body.
   * If the server cannot accept the input, it **MUST** return an HTTP error status code
     (e.g., 400 Bad Request). The HTTP response body **MAY** comprise a JSON-RPC *error
     response* that has no `id`.
5. If the input is a JSON-RPC *request*, the server **MUST** either
   return `Content-Type: text/event-stream`, to initiate an SSE stream, or
   `Content-Type: application/json`, to return one JSON object. The client **MUST**
   support both these cases.
6. If the server initiates an SSE stream:
   * The SSE stream **SHOULD** eventually include JSON-RPC *response* for the
     JSON-RPC *request* sent in the POST body.
   * The server **MAY** send JSON-RPC *requests* and *notifications* before sending the
     JSON-RPC *response*. These messages **SHOULD** relate to the originating client
     *request*.
   * The server **SHOULD NOT** close the SSE stream before sending the JSON-RPC *response*
     for the received JSON-RPC *request*, unless the [session](#session-management)
     expires.
   * After the JSON-RPC *response* has been sent, the server **SHOULD** close the SSE
     stream.
   * Disconnection **MAY** occur at any time (e.g., due to network conditions).
     Therefore:
     * Disconnection **SHOULD NOT** be interpreted as the client cancelling its request.
     * To cancel, the client **SHOULD** explicitly send an MCP `CancelledNotification`.
     * To avoid message loss due to disconnection, the server **MAY** make the stream
       [resumable](#resumability-and-redelivery).

### Listening for Messages from the Server

1. The client **MAY** issue an HTTP GET to the MCP endpoint. This can be used to open an
   SSE stream, allowing the server to communicate to the client, without the client first
   sending data via HTTP POST.
2. The client **MUST** include an `Accept` header, listing `text/event-stream` as a
   supported content type.
3. The server **MUST** either return `Content-Type: text/event-stream` in response to
   this HTTP GET, or else return HTTP 405 Method Not Allowed, indicating that the server
   does not offer an SSE stream at this endpoint.
4. If the server initiates an SSE stream:
   * The server **MAY** send JSON-RPC *requests* and *notifications* on the stream.
   * These messages **SHOULD** be unrelated to any concurrently-running JSON-RPC
     *request* from the client.
   * The server **MUST NOT** send a JSON-RPC *response* on the stream **unless**
     [resuming](#resumability-and-redelivery) a stream associated with a previous client
     request.
   * The server **MAY** close the SSE stream at any time.
   * The client **MAY** close the SSE stream at any time.

### Multiple Connections

1. The client **MAY** remain connected to multiple SSE streams simultaneously.
2. The server **MUST** send each of its JSON-RPC messages on only one of the connected
   streams; that is, it **MUST NOT** broadcast the same message across multiple streams.
   * The risk of message loss **MAY** be mitigated by making the stream
     [resumable](#resumability-and-redelivery).

### Resumability and Redelivery

To support resuming broken connections, and redelivering messages that might otherwise be
lost:

1. Servers **MAY** attach an `id` field to their SSE events, as described in the
   [SSE standard](https://html.spec.whatwg.org/multipage/server-sent-events.html#event-stream-interpretation).
   * If present, the ID **MUST** be globally unique across all streams within that
     [session](#session-management)—or all streams with that specific client, if session
     management is not in use.
2. If the client wishes to resume after a broken connection, it **SHOULD** issue an HTTP
   GET to the MCP endpoint, and include the
   [`Last-Event-ID`](https://html.spec.whatwg.org/multipage/server-sent-events.html#the-last-event-id-header)
   header to indicate the last event ID it received.
   * The server **MAY** use this header to replay messages that would have been sent
     after the last event ID, *on the stream that was disconnected*, and to resume the
     stream from that point.
   * The server **MUST NOT** replay messages that would have been delivered on a
     different stream.

In other words, these event IDs should be assigned by servers on a *per-stream* basis, to
act as a cursor within that particular stream.

### Session Management

An MCP "session" consists of logically related interactions between a client and a
server, beginning with the [initialization phase](/specification/2025-06-18/basic/lifecycle). To support
servers which want to establish stateful sessions:

1. A server using the Streamable HTTP transport **MAY** assign a session ID at
   initialization time, by including it in an `Mcp-Session-Id` header on the HTTP
   response containing the `InitializeResult`.
   * The session ID **SHOULD** be globally unique and cryptographically secure (e.g., a
     securely generated UUID, a JWT, or a cryptographic hash).
   * The session ID **MUST** only contain visible ASCII characters (ranging from 0x21 to
     0x7E).
2. If an `Mcp-Session-Id` is returned by the server during initialization, clients using
   the Streamable HTTP transport **MUST** include it in the `Mcp-Session-Id` header on
   all of their subsequent HTTP requests.
   * Servers that require a session ID **SHOULD** respond to requests without an
     `Mcp-Session-Id` header (other than initialization) with HTTP 400 Bad Request.
3. The server **MAY** terminate the session at any time, after which it **MUST** respond
   to requests containing that session ID with HTTP 404 Not Found.
4. When a client receives HTTP 404 in response to a request containing an
   `Mcp-Session-Id`, it **MUST** start a new session by sending a new `InitializeRequest`
   without a session ID attached.
5. Clients that no longer need a particular session (e.g., because the user is leaving
   the client application) **SHOULD** send an HTTP DELETE to the MCP endpoint with the
   `Mcp-Session-Id` header, to explicitly terminate the session.
   * The server **MAY** respond to this request with HTTP 405 Method Not Allowed,
     indicating that the server does not allow clients to terminate sessions.

### Sequence Diagram

```mermaid  theme={null}
sequenceDiagram
    participant Client
    participant Server

    note over Client, Server: initialization

    Client->>+Server: POST InitializeRequest
    Server->>-Client: InitializeResponse<br>Mcp-Session-Id: 1868a90c...

    Client->>+Server: POST InitializedNotification<br>Mcp-Session-Id: 1868a90c...
    Server->>-Client: 202 Accepted

    note over Client, Server: client requests
    Client->>+Server: POST ... request ...<br>Mcp-Session-Id: 1868a90c...

    alt single HTTP response
      Server->>Client: ... response ...
    else server opens SSE stream
      loop while connection remains open
          Server-)Client: ... SSE messages from server ...
      end
      Server-)Client: SSE event: ... response ...
    end
    deactivate Server

    note over Client, Server: client notifications/responses
    Client->>+Server: POST ... notification/response ...<br>Mcp-Session-Id: 1868a90c...
    Server->>-Client: 202 Accepted

    note over Client, Server: server requests
    Client->>+Server: GET<br>Mcp-Session-Id: 1868a90c...
    loop while connection remains open
        Server-)Client: ... SSE messages from server ...
    end
    deactivate Server

```

### Protocol Version Header

If using HTTP, the client **MUST** include the `MCP-Protocol-Version: <protocol-version>` HTTP header on all subsequent requests to the MCP
server, allowing the MCP server to respond based on the MCP protocol version.

For example: `MCP-Protocol-Version: 2025-06-18`

The protocol version sent by the client **SHOULD** be the one [negotiated during
initialization](/specification/2025-06-18/basic/lifecycle#version-negotiation).

For backwards compatibility, if the server does *not* receive an `MCP-Protocol-Version`
header, and has no other way to identify the version - for example, by relying on the
protocol version negotiated during initialization - the server **SHOULD** assume protocol
version `2025-03-26`.

If the server receives a request with an invalid or unsupported
`MCP-Protocol-Version`, it **MUST** respond with `400 Bad Request`.

### Backwards Compatibility

Clients and servers can maintain backwards compatibility with the deprecated [HTTP+SSE
transport](/specification/2024-11-05/basic/transports#http-with-sse) (from
protocol version 2024-11-05) as follows:

**Servers** wanting to support older clients should:

* Continue to host both the SSE and POST endpoints of the old transport, alongside the
  new "MCP endpoint" defined for the Streamable HTTP transport.
  * It is also possible to combine the old POST endpoint and the new MCP endpoint, but
    this may introduce unneeded complexity.

**Clients** wanting to support older servers should:

1. Accept an MCP server URL from the user, which may point to either a server using the
   old transport or the new transport.
2. Attempt to POST an `InitializeRequest` to the server URL, with an `Accept` header as
   defined above:
   * If it succeeds, the client can assume this is a server supporting the new Streamable
     HTTP transport.
   * If it fails with an HTTP 4xx status code (e.g., 405 Method Not Allowed or 404 Not
     Found):
     * Issue a GET request to the server URL, expecting that this will open an SSE stream
       and return an `endpoint` event as the first event.
     * When the `endpoint` event arrives, the client can assume this is a server running
       the old HTTP+SSE transport, and should use that transport for all subsequent
       communication.


## Custom Transports

Clients and servers **MAY** implement additional custom transport mechanisms to suit
their specific needs. The protocol is transport-agnostic and can be implemented over any
communication channel that supports bidirectional message exchange.

Implementers who choose to support custom transports **MUST** ensure they preserve the
JSON-RPC message format and lifecycle requirements defined by MCP. Custom transports
**SHOULD** document their specific connection establishment and message exchange patterns
to aid interoperability.



# Cancellation
Source: https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/cancellation



<div id="enable-section-numbers" />

<Info>**Protocol Revision**: 2025-06-18</Info>

The Model Context Protocol (MCP) supports optional cancellation of in-progress requests
through notification messages. Either side can send a cancellation notification to
indicate that a previously-issued request should be terminated.


## Cancellation Flow

When a party wants to cancel an in-progress request, it sends a `notifications/cancelled`
notification containing:

* The ID of the request to cancel
* An optional reason string that can be logged or displayed

```json  theme={null}
{
  "jsonrpc": "2.0",
  "method": "notifications/cancelled",
  "params": {
    "requestId": "123",
    "reason": "User requested cancellation"
  }
}
```


## Behavior Requirements

1. Cancellation notifications **MUST** only reference requests that:
   * Were previously issued in the same direction
   * Are believed to still be in-progress
2. The `initialize` request **MUST NOT** be cancelled by clients
3. Receivers of cancellation notifications **SHOULD**:
   * Stop processing the cancelled request
   * Free associated resources
   * Not send a response for the cancelled request
4. Receivers **MAY** ignore cancellation notifications if:
   * The referenced request is unknown
   * Processing has already completed
   * The request cannot be cancelled
5. The sender of the cancellation notification **SHOULD** ignore any response to the
   request that arrives afterward


## Timing Considerations

Due to network latency, cancellation notifications may arrive after request processing
has completed, and potentially after a response has already been sent.

Both parties **MUST** handle these race conditions gracefully:

```mermaid  theme={null}
sequenceDiagram
   participant Client
   participant Server

   Client->>Server: Request (ID: 123)
   Note over Server: Processing starts
   Client--)Server: notifications/cancelled (ID: 123)
   alt
      Note over Server: Processing may have<br/>completed before<br/>cancellation arrives
   else If not completed
      Note over Server: Stop processing
   end
```


## Implementation Notes

* Both parties **SHOULD** log cancellation reasons for debugging
* Application UIs **SHOULD** indicate when cancellation is requested


## Error Handling

Invalid cancellation notifications **SHOULD** be ignored:

* Unknown request IDs
* Already completed requests
* Malformed notifications

This maintains the "fire and forget" nature of notifications while allowing for race
conditions in asynchronous communication.



# Ping
Source: https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/ping



<div id="enable-section-numbers" />

<Info>**Protocol Revision**: 2025-06-18</Info>

The Model Context Protocol includes an optional ping mechanism that allows either party
to verify that their counterpart is still responsive and the connection is alive.


## Overview

The ping functionality is implemented through a simple request/response pattern. Either
the client or server can initiate a ping by sending a `ping` request.


## Message Format

A ping request is a standard JSON-RPC request with no parameters:

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": "123",
  "method": "ping"
}
```


## Behavior Requirements

1. The receiver **MUST** respond promptly with an empty response:

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": "123",
  "result": {}
}
```

2. If no response is received within a reasonable timeout period, the sender **MAY**:
   * Consider the connection stale
   * Terminate the connection
   * Attempt reconnection procedures


## Usage Patterns

```mermaid  theme={null}
sequenceDiagram
    participant Sender
    participant Receiver

    Sender->>Receiver: ping request
    Receiver->>Sender: empty response
```


## Implementation Considerations

* Implementations **SHOULD** periodically issue pings to detect connection health
* The frequency of pings **SHOULD** be configurable
* Timeouts **SHOULD** be appropriate for the network environment
* Excessive pinging **SHOULD** be avoided to reduce network overhead


## Error Handling

* Timeouts **SHOULD** be treated as connection failures
* Multiple failed pings **MAY** trigger connection reset
* Implementations **SHOULD** log ping failures for diagnostics



# Progress
Source: https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/progress



<div id="enable-section-numbers" />

<Info>**Protocol Revision**: 2025-06-18</Info>

The Model Context Protocol (MCP) supports optional progress tracking for long-running
operations through notification messages. Either side can send progress notifications to
provide updates about operation status.


## Progress Flow

When a party wants to *receive* progress updates for a request, it includes a
`progressToken` in the request metadata.

* Progress tokens **MUST** be a string or integer value
* Progress tokens can be chosen by the sender using any means, but **MUST** be unique
  across all active requests.

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "some_method",
  "params": {
    "_meta": {
      "progressToken": "abc123"
    }
  }
}
```

The receiver **MAY** then send progress notifications containing:

* The original progress token
* The current progress value so far
* An optional "total" value
* An optional "message" value

```json  theme={null}
{
  "jsonrpc": "2.0",
  "method": "notifications/progress",
  "params": {
    "progressToken": "abc123",
    "progress": 50,
    "total": 100,
    "message": "Reticulating splines..."
  }
}
```

* The `progress` value **MUST** increase with each notification, even if the total is
  unknown.
* The `progress` and the `total` values **MAY** be floating point.
* The `message` field **SHOULD** provide relevant human readable progress information.


## Behavior Requirements

1. Progress notifications **MUST** only reference tokens that:
   * Were provided in an active request
   * Are associated with an in-progress operation

2. Receivers of progress requests **MAY**:
   * Choose not to send any progress notifications
   * Send notifications at whatever frequency they deem appropriate
   * Omit the total value if unknown

```mermaid  theme={null}
sequenceDiagram
    participant Sender
    participant Receiver

    Note over Sender,Receiver: Request with progress token
    Sender->>Receiver: Method request with progressToken

    Note over Sender,Receiver: Progress updates
    Receiver-->>Sender: Progress notification (0.2/1.0)
    Receiver-->>Sender: Progress notification (0.6/1.0)
    Receiver-->>Sender: Progress notification (1.0/1.0)

    Note over Sender,Receiver: Operation complete
    Receiver->>Sender: Method response
```


## Implementation Notes

* Senders and receivers **SHOULD** track active progress tokens
* Both parties **SHOULD** implement rate limiting to prevent flooding
* Progress notifications **MUST** stop after completion



# Key Changes
Source: https://modelcontextprotocol.io/specification/2025-06-18/changelog



<div id="enable-section-numbers" />

This document lists changes made to the Model Context Protocol (MCP) specification since
the previous revision, [2025-03-26](/specification/2025-03-26).


## Major changes

1. Remove support for JSON-RPC **[batching](https://www.jsonrpc.org/specification#batch)**
   (PR [#416](https://github.com/modelcontextprotocol/specification/pull/416))
2. Add support for [structured tool output](/specification/2025-06-18/server/tools#structured-content)
   (PR [#371](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/371))
3. Classify MCP servers as [OAuth Resource Servers](/specification/2025-06-18/basic/authorization#authorization-server-discovery),
   adding protected resource metadata to discover the corresponding Authorization server.
   (PR [#338](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/338))
4. Require MCP clients to implement Resource Indicators as described in [RFC 8707](https://www.rfc-editor.org/rfc/rfc8707.html) to prevent
   malicious servers from obtaining access tokens.
   (PR [#734](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/734))
5. Clarify [security considerations](/specification/2025-06-18/basic/authorization#security-considerations) and best practices
   in the authorization spec and in a new [security best practices page](/specification/2025-06-18/basic/security_best_practices).
6. Add support for **[elicitation](/specification/2025-06-18/client/elicitation)**, enabling servers to request additional
   information from users during interactions.
   (PR [#382](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/382))
7. Add support for **[resource links](/specification/2025-06-18/server/tools#resource-links)** in
   tool call results. (PR [#603](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/603))
8. Require [negotiated protocol version to be specified](/specification/2025-06-18/basic/transports#protocol-version-header)
   via `MCP-Protocol-Version` header in subsequent requests when using HTTP (PR [#548](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/548)).
9. Change **SHOULD** to **MUST** in [Lifecycle Operation](/specification/2025-06-18/basic/lifecycle#operation)


## Other schema changes

1. Add `_meta` field to additional interface types (PR [#710](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/710)),
   and specify [proper usage](/specification/2025-06-18/basic#meta).
2. Add `context` field to `CompletionRequest`, providing for completion requests to include
   previously-resolved variables (PR [#598](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/598)).
3. Add `title` field for human-friendly display names, so that `name` can be used as a programmatic
   identifier (PR [#663](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/663))


## Full changelog

For a complete list of all changes that have been made since the last protocol revision,
[see GitHub](https://github.com/modelcontextprotocol/specification/compare/2025-03-26...2025-06-18).



# Elicitation
Source: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation



<div id="enable-section-numbers" />

<Info>**Protocol Revision**: 2025-06-18</Info>

<Note>
  Elicitation is newly introduced in this version of the MCP specification and its design may evolve in future protocol versions.
</Note>

The Model Context Protocol (MCP) provides a standardized way for servers to request additional
information from users through the client during interactions. This flow allows clients to
maintain control over user interactions and data sharing while enabling servers to gather
necessary information dynamically.
Servers request structured data from users with JSON schemas to validate responses.


## User Interaction Model

Elicitation in MCP allows servers to implement interactive workflows by enabling user input
requests to occur *nested* inside other MCP server features.

Implementations are free to expose elicitation through any interface pattern that suits
their needs—the protocol itself does not mandate any specific user interaction
model.

<Warning>
  For trust & safety and security:

  * Servers **MUST NOT** use elicitation to request sensitive information.

  Applications **SHOULD**:

  * Provide UI that makes it clear which server is requesting information
  * Allow users to review and modify their responses before sending
  * Respect user privacy and provide clear decline and cancel options
</Warning>


## Capabilities

Clients that support elicitation **MUST** declare the `elicitation` capability during
[initialization](/specification/2025-06-18/basic/lifecycle#initialization):

```json  theme={null}
{
  "capabilities": {
    "elicitation": {}
  }
}
```


## Protocol Messages

### Creating Elicitation Requests

To request information from a user, servers send an `elicitation/create` request:

#### Simple Text Request

**Request:**

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "elicitation/create",
  "params": {
    "message": "Please provide your GitHub username",
    "requestedSchema": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      },
      "required": ["name"]
    }
  }
}
```

**Response:**

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "action": "accept",
    "content": {
      "name": "octocat"
    }
  }
}
```

#### Structured Data Request

**Request:**

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "elicitation/create",
  "params": {
    "message": "Please provide your contact information",
    "requestedSchema": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Your full name"
        },
        "email": {
          "type": "string",
          "format": "email",
          "description": "Your email address"
        },
        "age": {
          "type": "number",
          "minimum": 18,
          "description": "Your age"
        }
      },
      "required": ["name", "email"]
    }
  }
}
```

**Response:**

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "action": "accept",
    "content": {
      "name": "Monalisa Octocat",
      "email": "octocat@github.com",
      "age": 30
    }
  }
}
```

**Reject Response Example:**

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "action": "decline"
  }
}
```

**Cancel Response Example:**

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "action": "cancel"
  }
}
```


## Message Flow

```mermaid  theme={null}
sequenceDiagram
    participant User
    participant Client
    participant Server

    Note over Server,Client: Server initiates elicitation
    Server->>Client: elicitation/create

    Note over Client,User: Human interaction
    Client->>User: Present elicitation UI
    User-->>Client: Provide requested information

    Note over Server,Client: Complete request
    Client-->>Server: Return user response

    Note over Server: Continue processing with new information
```


## Request Schema

The `requestedSchema` field allows servers to define the structure of the expected response using a restricted subset of JSON Schema. To simplify implementation for clients, elicitation schemas are limited to flat objects with primitive properties only:

```json  theme={null}
"requestedSchema": {
  "type": "object",
  "properties": {
    "propertyName": {
      "type": "string",
      "title": "Display Name",
      "description": "Description of the property"
    },
    "anotherProperty": {
      "type": "number",
      "minimum": 0,
      "maximum": 100
    }
  },
  "required": ["propertyName"]
}
```

### Supported Schema Types

The schema is restricted to these primitive types:

1. **String Schema**

   ```json  theme={null}
   {
     "type": "string",
     "title": "Display Name",
     "description": "Description text",
     "minLength": 3,
     "maxLength": 50,
     "format": "email" // Supported: "email", "uri", "date", "date-time"
   }
   ```

   Supported formats: `email`, `uri`, `date`, `date-time`

2. **Number Schema**

   ```json  theme={null}
   {
     "type": "number", // or "integer"
     "title": "Display Name",
     "description": "Description text",
     "minimum": 0,
     "maximum": 100
   }
   ```

3. **Boolean Schema**

   ```json  theme={null}
   {
     "type": "boolean",
     "title": "Display Name",
     "description": "Description text",
     "default": false
   }
   ```

4. **Enum Schema**
   ```json  theme={null}
   {
     "type": "string",
     "title": "Display Name",
     "description": "Description text",
     "enum": ["option1", "option2", "option3"],
     "enumNames": ["Option 1", "Option 2", "Option 3"]
   }
   ```

Clients can use this schema to:

1. Generate appropriate input forms
2. Validate user input before sending
3. Provide better guidance to users

Note that complex nested structures, arrays of objects, and other advanced JSON Schema features are intentionally not supported to simplify client implementation.


## Response Actions

Elicitation responses use a three-action model to clearly distinguish between different user actions:

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "action": "accept", // or "decline" or "cancel"
    "content": {
      "propertyName": "value",
      "anotherProperty": 42
    }
  }
}
```

The three response actions are:

1. **Accept** (`action: "accept"`): User explicitly approved and submitted with data
   * The `content` field contains the submitted data matching the requested schema
   * Example: User clicked "Submit", "OK", "Confirm", etc.

2. **Decline** (`action: "decline"`): User explicitly declined the request
   * The `content` field is typically omitted
   * Example: User clicked "Reject", "Decline", "No", etc.

3. **Cancel** (`action: "cancel"`): User dismissed without making an explicit choice
   * The `content` field is typically omitted
   * Example: User closed the dialog, clicked outside, pressed Escape, etc.

Servers should handle each state appropriately:

* **Accept**: Process the submitted data
* **Decline**: Handle explicit decline (e.g., offer alternatives)
* **Cancel**: Handle dismissal (e.g., prompt again later)


## Security Considerations

1. Servers **MUST NOT** request sensitive information through elicitation
2. Clients **SHOULD** implement user approval controls
3. Both parties **SHOULD** validate elicitation content against the provided schema
4. Clients **SHOULD** provide clear indication of which server is requesting information
5. Clients **SHOULD** allow users to decline elicitation requests at any time
6. Clients **SHOULD** implement rate limiting
7. Clients **SHOULD** present elicitation requests in a way that makes it clear what information is being requested and why



# Roots
Source: https://modelcontextprotocol.io/specification/2025-06-18/client/roots



<div id="enable-section-numbers" />

<Info>**Protocol Revision**: 2025-06-18</Info>

The Model Context Protocol (MCP) provides a standardized way for clients to expose
filesystem "roots" to servers. Roots define the boundaries of where servers can operate
within the filesystem, allowing them to understand which directories and files they have
access to. Servers can request the list of roots from supporting clients and receive
notifications when that list changes.


## User Interaction Model

Roots in MCP are typically exposed through workspace or project configuration interfaces.

For example, implementations could offer a workspace/project picker that allows users to
select directories and files the server should have access to. This can be combined with
automatic workspace detection from version control systems or project files.

However, implementations are free to expose roots through any interface pattern that
suits their needs—the protocol itself does not mandate any specific user
interaction model.


## Capabilities

Clients that support roots **MUST** declare the `roots` capability during
[initialization](/specification/2025-06-18/basic/lifecycle#initialization):

```json  theme={null}
{
  "capabilities": {
    "roots": {
      "listChanged": true
    }
  }
}
```

`listChanged` indicates whether the client will emit notifications when the list of roots
changes.


## Protocol Messages

### Listing Roots

To retrieve roots, servers send a `roots/list` request:

**Request:**

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "roots/list"
}
```

**Response:**

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "roots": [
      {
        "uri": "file:///home/user/projects/myproject",
        "name": "My Project"
      }
    ]
  }
}
```

### Root List Changes

When roots change, clients that support `listChanged` **MUST** send a notification:

```json  theme={null}
{
  "jsonrpc": "2.0",
  "method": "notifications/roots/list_changed"
}
```


## Message Flow

```mermaid  theme={null}
sequenceDiagram
    participant Server
    participant Client

    Note over Server,Client: Discovery
    Server->>Client: roots/list
    Client-->>Server: Available roots

    Note over Server,Client: Changes
    Client--)Server: notifications/roots/list_changed
    Server->>Client: roots/list
    Client-->>Server: Updated roots
```


## Data Types

### Root

A root definition includes:

* `uri`: Unique identifier for the root. This **MUST** be a `file://` URI in the current
  specification.
* `name`: Optional human-readable name for display purposes.

Example roots for different use cases:

#### Project Directory

```json  theme={null}
{
  "uri": "file:///home/user/projects/myproject",
  "name": "My Project"
}
```

#### Multiple Repositories

```json  theme={null}
[
  {
    "uri": "file:///home/user/repos/frontend",
    "name": "Frontend Repository"
  },
  {
    "uri": "file:///home/user/repos/backend",
    "name": "Backend Repository"
  }
]
```


## Error Handling

Clients **SHOULD** return standard JSON-RPC errors for common failure cases:

* Client does not support roots: `-32601` (Method not found)
* Internal errors: `-32603`

Example error:

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32601,
    "message": "Roots not supported",
    "data": {
      "reason": "Client does not have roots capability"
    }
  }
}
```


## Security Considerations

1. Clients **MUST**:
   * Only expose roots with appropriate permissions
   * Validate all root URIs to prevent path traversal
   * Implement proper access controls
   * Monitor root accessibility

2. Servers **SHOULD**:
   * Handle cases where roots become unavailable
   * Respect root boundaries during operations
   * Validate all paths against provided roots


## Implementation Guidelines

1. Clients **SHOULD**:
   * Prompt users for consent before exposing roots to servers
   * Provide clear user interfaces for root management
   * Validate root accessibility before exposing
   * Monitor for root changes

2. Servers **SHOULD**:
   * Check for roots capability before usage
   * Handle root list changes gracefully
   * Respect root boundaries in operations
   * Cache root information appropriately



---

**Navigation:** [← Previous](./02-build-an-mcp-server.md) | [Index](./index.md) | [Next →](./04-sampling.md)
