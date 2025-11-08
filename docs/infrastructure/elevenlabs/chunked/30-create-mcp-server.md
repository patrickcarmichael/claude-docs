**Navigation:** [← Previous](./29-delete-secret.md) | [Index](./index.md) | [Next →](./31-get-configuration-override.md)

# Create MCP server

POST https://api.elevenlabs.io/v1/convai/mcp-servers
Content-Type: application/json

Create a new MCP server configuration in the workspace.

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/mcp/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create Mcp Server
  version: endpoint_conversationalAi/mcpServers.create
paths:
  /v1/convai/mcp-servers:
    post:
      operationId: create
      summary: Create Mcp Server
      description: Create a new MCP server configuration in the workspace.
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/mcpServers
      parameters:
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MCPServerResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MCPServerRequestModel'
components:
  schemas:
    MCPApprovalPolicy:
      type: string
      enum:
        - value: auto_approve_all
        - value: require_approval_all
        - value: require_approval_per_tool
    MCPToolApprovalPolicy:
      type: string
      enum:
        - value: auto_approved
        - value: requires_approval
    MCPToolApprovalHash:
      type: object
      properties:
        tool_name:
          type: string
        tool_hash:
          type: string
        approval_policy:
          $ref: '#/components/schemas/MCPToolApprovalPolicy'
      required:
        - tool_name
        - tool_hash
    MCPServerTransport:
      type: string
      enum:
        - value: SSE
        - value: STREAMABLE_HTTP
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
    McpServerConfigInputUrl:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
    ConvAIUserSecretDBModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        encrypted_value:
          type: string
        nonce:
          type: string
      required:
        - id
        - name
        - encrypted_value
        - nonce
    McpServerConfigInputSecretToken:
      oneOf:
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIUserSecretDBModel'
    ConvAIDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
    McpServerConfigInputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    ToolCallSoundType:
      type: string
      enum:
        - value: typing
        - value: elevator1
        - value: elevator2
        - value: elevator3
        - value: elevator4
    ToolCallSoundBehavior:
      type: string
      enum:
        - value: auto
        - value: always
    ToolExecutionMode:
      type: string
      enum:
        - value: immediate
        - value: post_tool_speech
        - value: async
    DynamicVariableAssignment:
      type: object
      properties:
        source:
          type: string
          enum:
            - type: stringLiteral
              value: response
        dynamic_variable:
          type: string
        value_path:
          type: string
      required:
        - dynamic_variable
        - value_path
    MCPToolConfigOverride:
      type: object
      properties:
        tool_name:
          type: string
        force_pre_tool_speech:
          type:
            - boolean
            - 'null'
        disable_interruptions:
          type:
            - boolean
            - 'null'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundBehavior'
            - type: 'null'
        execution_mode:
          oneOf:
            - $ref: '#/components/schemas/ToolExecutionMode'
            - type: 'null'
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
      required:
        - tool_name
    MCPServerConfig-Input:
      type: object
      properties:
        approval_policy:
          $ref: '#/components/schemas/MCPApprovalPolicy'
        tool_approval_hashes:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolApprovalHash'
        transport:
          $ref: '#/components/schemas/MCPServerTransport'
        url:
          $ref: '#/components/schemas/McpServerConfigInputUrl'
        secret_token:
          oneOf:
            - $ref: '#/components/schemas/McpServerConfigInputSecretToken'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/McpServerConfigInputRequestHeaders'
        name:
          type: string
        description:
          type: string
        force_pre_tool_speech:
          type: boolean
        disable_interruptions:
          type: boolean
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        tool_config_overrides:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolConfigOverride'
      required:
        - url
        - name
    MCPServerRequestModel:
      type: object
      properties:
        config:
          $ref: '#/components/schemas/MCPServerConfig-Input'
      required:
        - config
    McpServerConfigOutputUrl:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
    McpServerConfigOutputSecretToken:
      oneOf:
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIUserSecretDBModel'
    McpServerConfigOutputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    MCPServerConfig-Output:
      type: object
      properties:
        approval_policy:
          $ref: '#/components/schemas/MCPApprovalPolicy'
        tool_approval_hashes:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolApprovalHash'
        transport:
          $ref: '#/components/schemas/MCPServerTransport'
        url:
          $ref: '#/components/schemas/McpServerConfigOutputUrl'
        secret_token:
          oneOf:
            - $ref: '#/components/schemas/McpServerConfigOutputSecretToken'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/McpServerConfigOutputRequestHeaders'
        name:
          type: string
        description:
          type: string
        force_pre_tool_speech:
          type: boolean
        disable_interruptions:
          type: boolean
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        tool_config_overrides:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolConfigOverride'
      required:
        - url
        - name
    ResourceAccessInfoRole:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
        creator_name:
          type: string
        creator_email:
          type: string
        role:
          $ref: '#/components/schemas/ResourceAccessInfoRole'
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
    DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    DependentAvailableAgentIdentifier:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: available
        created_at_unix_secs:
          type: integer
        access_level:
          $ref: '#/components/schemas/DependentAvailableAgentIdentifierAccessLevel'
      required:
        - id
        - name
        - created_at_unix_secs
        - access_level
    DependentUnknownAgentIdentifier:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: unknown
    McpServerResponseModelDependentAgentsItems:
      oneOf:
        - $ref: '#/components/schemas/DependentAvailableAgentIdentifier'
        - $ref: '#/components/schemas/DependentUnknownAgentIdentifier'
    MCPServerMetadataResponseModel:
      type: object
      properties:
        created_at:
          type: integer
        owner_user_id:
          type:
            - string
            - 'null'
      required:
        - created_at
    MCPServerResponseModel:
      type: object
      properties:
        id:
          type: string
        config:
          $ref: '#/components/schemas/MCPServerConfig-Output'
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
        dependent_agents:
          type: array
          items:
            $ref: '#/components/schemas/McpServerResponseModelDependentAgentsItems'
        metadata:
          $ref: '#/components/schemas/MCPServerMetadataResponseModel'
      required:
        - id
        - config
        - metadata

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.mcpServers.create({
        config: {
            url: "string",
            name: "string",
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.mcp_servers.create(
    config={
        "url": "string",
        "name": "string"
    }
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers"

	payload := strings.NewReader("{\n  \"config\": {\n    \"url\": \"string\",\n    \"name\": \"string\"\n  }\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"config\": {\n    \"url\": \"string\",\n    \"name\": \"string\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/mcp-servers")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"config\": {\n    \"url\": \"string\",\n    \"name\": \"string\"\n  }\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/mcp-servers', [
  'body' => '{
  "config": {
    "url": "string",
    "name": "string"
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"config\": {\n    \"url\": \"string\",\n    \"name\": \"string\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["config": [
    "url": "string",
    "name": "string"
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


# List MCP servers

GET https://api.elevenlabs.io/v1/convai/mcp-servers

Retrieve all MCP server configurations available in the workspace.

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/mcp/list


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List Mcp Servers
  version: endpoint_conversationalAi/mcpServers.list
paths:
  /v1/convai/mcp-servers:
    get:
      operationId: list
      summary: List Mcp Servers
      description: Retrieve all MCP server configurations available in the workspace.
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/mcpServers
      parameters:
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MCPServersResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    MCPApprovalPolicy:
      type: string
      enum:
        - value: auto_approve_all
        - value: require_approval_all
        - value: require_approval_per_tool
    MCPToolApprovalPolicy:
      type: string
      enum:
        - value: auto_approved
        - value: requires_approval
    MCPToolApprovalHash:
      type: object
      properties:
        tool_name:
          type: string
        tool_hash:
          type: string
        approval_policy:
          $ref: '#/components/schemas/MCPToolApprovalPolicy'
      required:
        - tool_name
        - tool_hash
    MCPServerTransport:
      type: string
      enum:
        - value: SSE
        - value: STREAMABLE_HTTP
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
    McpServerConfigOutputUrl:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
    ConvAIUserSecretDBModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        encrypted_value:
          type: string
        nonce:
          type: string
      required:
        - id
        - name
        - encrypted_value
        - nonce
    McpServerConfigOutputSecretToken:
      oneOf:
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIUserSecretDBModel'
    ConvAIDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
    McpServerConfigOutputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    ToolCallSoundType:
      type: string
      enum:
        - value: typing
        - value: elevator1
        - value: elevator2
        - value: elevator3
        - value: elevator4
    ToolCallSoundBehavior:
      type: string
      enum:
        - value: auto
        - value: always
    ToolExecutionMode:
      type: string
      enum:
        - value: immediate
        - value: post_tool_speech
        - value: async
    DynamicVariableAssignment:
      type: object
      properties:
        source:
          type: string
          enum:
            - type: stringLiteral
              value: response
        dynamic_variable:
          type: string
        value_path:
          type: string
      required:
        - dynamic_variable
        - value_path
    MCPToolConfigOverride:
      type: object
      properties:
        tool_name:
          type: string
        force_pre_tool_speech:
          type:
            - boolean
            - 'null'
        disable_interruptions:
          type:
            - boolean
            - 'null'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundBehavior'
            - type: 'null'
        execution_mode:
          oneOf:
            - $ref: '#/components/schemas/ToolExecutionMode'
            - type: 'null'
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
      required:
        - tool_name
    MCPServerConfig-Output:
      type: object
      properties:
        approval_policy:
          $ref: '#/components/schemas/MCPApprovalPolicy'
        tool_approval_hashes:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolApprovalHash'
        transport:
          $ref: '#/components/schemas/MCPServerTransport'
        url:
          $ref: '#/components/schemas/McpServerConfigOutputUrl'
        secret_token:
          oneOf:
            - $ref: '#/components/schemas/McpServerConfigOutputSecretToken'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/McpServerConfigOutputRequestHeaders'
        name:
          type: string
        description:
          type: string
        force_pre_tool_speech:
          type: boolean
        disable_interruptions:
          type: boolean
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        tool_config_overrides:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolConfigOverride'
      required:
        - url
        - name
    ResourceAccessInfoRole:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
        creator_name:
          type: string
        creator_email:
          type: string
        role:
          $ref: '#/components/schemas/ResourceAccessInfoRole'
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
    DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    DependentAvailableAgentIdentifier:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: available
        created_at_unix_secs:
          type: integer
        access_level:
          $ref: '#/components/schemas/DependentAvailableAgentIdentifierAccessLevel'
      required:
        - id
        - name
        - created_at_unix_secs
        - access_level
    DependentUnknownAgentIdentifier:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: unknown
    McpServerResponseModelDependentAgentsItems:
      oneOf:
        - $ref: '#/components/schemas/DependentAvailableAgentIdentifier'
        - $ref: '#/components/schemas/DependentUnknownAgentIdentifier'
    MCPServerMetadataResponseModel:
      type: object
      properties:
        created_at:
          type: integer
        owner_user_id:
          type:
            - string
            - 'null'
      required:
        - created_at
    MCPServerResponseModel:
      type: object
      properties:
        id:
          type: string
        config:
          $ref: '#/components/schemas/MCPServerConfig-Output'
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
        dependent_agents:
          type: array
          items:
            $ref: '#/components/schemas/McpServerResponseModelDependentAgentsItems'
        metadata:
          $ref: '#/components/schemas/MCPServerMetadataResponseModel'
      required:
        - id
        - config
        - metadata
    MCPServersResponseModel:
      type: object
      properties:
        mcp_servers:
          type: array
          items:
            $ref: '#/components/schemas/MCPServerResponseModel'
      required:
        - mcp_servers

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.mcpServers.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.mcp_servers.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("xi-api-key", "xi-api-key")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/mcp-servers")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/mcp-servers', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


# Get MCP server

GET https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}

Retrieve a specific MCP server configuration from the workspace.

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/mcp/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Mcp Server
  version: endpoint_conversationalAi/mcpServers.get
paths:
  /v1/convai/mcp-servers/{mcp_server_id}:
    get:
      operationId: get
      summary: Get Mcp Server
      description: Retrieve a specific MCP server configuration from the workspace.
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/mcpServers
      parameters:
        - name: mcp_server_id
          in: path
          description: ID of the MCP Server.
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MCPServerResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    MCPApprovalPolicy:
      type: string
      enum:
        - value: auto_approve_all
        - value: require_approval_all
        - value: require_approval_per_tool
    MCPToolApprovalPolicy:
      type: string
      enum:
        - value: auto_approved
        - value: requires_approval
    MCPToolApprovalHash:
      type: object
      properties:
        tool_name:
          type: string
        tool_hash:
          type: string
        approval_policy:
          $ref: '#/components/schemas/MCPToolApprovalPolicy'
      required:
        - tool_name
        - tool_hash
    MCPServerTransport:
      type: string
      enum:
        - value: SSE
        - value: STREAMABLE_HTTP
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
    McpServerConfigOutputUrl:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
    ConvAIUserSecretDBModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        encrypted_value:
          type: string
        nonce:
          type: string
      required:
        - id
        - name
        - encrypted_value
        - nonce
    McpServerConfigOutputSecretToken:
      oneOf:
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIUserSecretDBModel'
    ConvAIDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
    McpServerConfigOutputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    ToolCallSoundType:
      type: string
      enum:
        - value: typing
        - value: elevator1
        - value: elevator2
        - value: elevator3
        - value: elevator4
    ToolCallSoundBehavior:
      type: string
      enum:
        - value: auto
        - value: always
    ToolExecutionMode:
      type: string
      enum:
        - value: immediate
        - value: post_tool_speech
        - value: async
    DynamicVariableAssignment:
      type: object
      properties:
        source:
          type: string
          enum:
            - type: stringLiteral
              value: response
        dynamic_variable:
          type: string
        value_path:
          type: string
      required:
        - dynamic_variable
        - value_path
    MCPToolConfigOverride:
      type: object
      properties:
        tool_name:
          type: string
        force_pre_tool_speech:
          type:
            - boolean
            - 'null'
        disable_interruptions:
          type:
            - boolean
            - 'null'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundBehavior'
            - type: 'null'
        execution_mode:
          oneOf:
            - $ref: '#/components/schemas/ToolExecutionMode'
            - type: 'null'
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
      required:
        - tool_name
    MCPServerConfig-Output:
      type: object
      properties:
        approval_policy:
          $ref: '#/components/schemas/MCPApprovalPolicy'
        tool_approval_hashes:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolApprovalHash'
        transport:
          $ref: '#/components/schemas/MCPServerTransport'
        url:
          $ref: '#/components/schemas/McpServerConfigOutputUrl'
        secret_token:
          oneOf:
            - $ref: '#/components/schemas/McpServerConfigOutputSecretToken'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/McpServerConfigOutputRequestHeaders'
        name:
          type: string
        description:
          type: string
        force_pre_tool_speech:
          type: boolean
        disable_interruptions:
          type: boolean
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        tool_config_overrides:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolConfigOverride'
      required:
        - url
        - name
    ResourceAccessInfoRole:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
        creator_name:
          type: string
        creator_email:
          type: string
        role:
          $ref: '#/components/schemas/ResourceAccessInfoRole'
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
    DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    DependentAvailableAgentIdentifier:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: available
        created_at_unix_secs:
          type: integer
        access_level:
          $ref: '#/components/schemas/DependentAvailableAgentIdentifierAccessLevel'
      required:
        - id
        - name
        - created_at_unix_secs
        - access_level
    DependentUnknownAgentIdentifier:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: unknown
    McpServerResponseModelDependentAgentsItems:
      oneOf:
        - $ref: '#/components/schemas/DependentAvailableAgentIdentifier'
        - $ref: '#/components/schemas/DependentUnknownAgentIdentifier'
    MCPServerMetadataResponseModel:
      type: object
      properties:
        created_at:
          type: integer
        owner_user_id:
          type:
            - string
            - 'null'
      required:
        - created_at
    MCPServerResponseModel:
      type: object
      properties:
        id:
          type: string
        config:
          $ref: '#/components/schemas/MCPServerConfig-Output'
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
        dependent_agents:
          type: array
          items:
            $ref: '#/components/schemas/McpServerResponseModelDependentAgentsItems'
        metadata:
          $ref: '#/components/schemas/MCPServerMetadataResponseModel'
      required:
        - id
        - config
        - metadata

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.mcpServers.get("mcp_server_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.mcp_servers.get(
    mcp_server_id="mcp_server_id"
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("xi-api-key", "xi-api-key")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


# Update MCP server configuration

PATCH https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}
Content-Type: application/json

Update the configuration settings for an MCP server.

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/mcp/update


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update Mcp Server Configuration
  version: endpoint_conversationalAi/mcpServers.update
paths:
  /v1/convai/mcp-servers/{mcp_server_id}:
    patch:
      operationId: update
      summary: Update Mcp Server Configuration
      description: Update the configuration settings for an MCP server.
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/mcpServers
      parameters:
        - name: mcp_server_id
          in: path
          description: ID of the MCP Server.
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MCPServerResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MCPServerConfigUpdateRequestModel'
components:
  schemas:
    MCPApprovalPolicy:
      type: string
      enum:
        - value: auto_approve_all
        - value: require_approval_all
        - value: require_approval_per_tool
    ToolCallSoundType:
      type: string
      enum:
        - value: typing
        - value: elevator1
        - value: elevator2
        - value: elevator3
        - value: elevator4
    ToolCallSoundBehavior:
      type: string
      enum:
        - value: auto
        - value: always
    ToolExecutionMode:
      type: string
      enum:
        - value: immediate
        - value: post_tool_speech
        - value: async
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
    ConvAIDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
    McpServerConfigUpdateRequestModelRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    MCPServerConfigUpdateRequestModel:
      type: object
      properties:
        approval_policy:
          oneOf:
            - $ref: '#/components/schemas/MCPApprovalPolicy'
            - type: 'null'
        force_pre_tool_speech:
          type:
            - boolean
            - 'null'
        disable_interruptions:
          type:
            - boolean
            - 'null'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundBehavior'
            - type: 'null'
        execution_mode:
          oneOf:
            - $ref: '#/components/schemas/ToolExecutionMode'
            - type: 'null'
        request_headers:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: >-
              #/components/schemas/McpServerConfigUpdateRequestModelRequestHeaders
    MCPToolApprovalPolicy:
      type: string
      enum:
        - value: auto_approved
        - value: requires_approval
    MCPToolApprovalHash:
      type: object
      properties:
        tool_name:
          type: string
        tool_hash:
          type: string
        approval_policy:
          $ref: '#/components/schemas/MCPToolApprovalPolicy'
      required:
        - tool_name
        - tool_hash
    MCPServerTransport:
      type: string
      enum:
        - value: SSE
        - value: STREAMABLE_HTTP
    McpServerConfigOutputUrl:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
    ConvAIUserSecretDBModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        encrypted_value:
          type: string
        nonce:
          type: string
      required:
        - id
        - name
        - encrypted_value
        - nonce
    McpServerConfigOutputSecretToken:
      oneOf:
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIUserSecretDBModel'
    McpServerConfigOutputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    DynamicVariableAssignment:
      type: object
      properties:
        source:
          type: string
          enum:
            - type: stringLiteral
              value: response
        dynamic_variable:
          type: string
        value_path:
          type: string
      required:
        - dynamic_variable
        - value_path
    MCPToolConfigOverride:
      type: object
      properties:
        tool_name:
          type: string
        force_pre_tool_speech:
          type:
            - boolean
            - 'null'
        disable_interruptions:
          type:
            - boolean
            - 'null'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundBehavior'
            - type: 'null'
        execution_mode:
          oneOf:
            - $ref: '#/components/schemas/ToolExecutionMode'
            - type: 'null'
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
      required:
        - tool_name
    MCPServerConfig-Output:
      type: object
      properties:
        approval_policy:
          $ref: '#/components/schemas/MCPApprovalPolicy'
        tool_approval_hashes:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolApprovalHash'
        transport:
          $ref: '#/components/schemas/MCPServerTransport'
        url:
          $ref: '#/components/schemas/McpServerConfigOutputUrl'
        secret_token:
          oneOf:
            - $ref: '#/components/schemas/McpServerConfigOutputSecretToken'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/McpServerConfigOutputRequestHeaders'
        name:
          type: string
        description:
          type: string
        force_pre_tool_speech:
          type: boolean
        disable_interruptions:
          type: boolean
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        tool_config_overrides:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolConfigOverride'
      required:
        - url
        - name
    ResourceAccessInfoRole:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
        creator_name:
          type: string
        creator_email:
          type: string
        role:
          $ref: '#/components/schemas/ResourceAccessInfoRole'
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
    DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    DependentAvailableAgentIdentifier:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: available
        created_at_unix_secs:
          type: integer
        access_level:
          $ref: '#/components/schemas/DependentAvailableAgentIdentifierAccessLevel'
      required:
        - id
        - name
        - created_at_unix_secs
        - access_level
    DependentUnknownAgentIdentifier:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: unknown
    McpServerResponseModelDependentAgentsItems:
      oneOf:
        - $ref: '#/components/schemas/DependentAvailableAgentIdentifier'
        - $ref: '#/components/schemas/DependentUnknownAgentIdentifier'
    MCPServerMetadataResponseModel:
      type: object
      properties:
        created_at:
          type: integer
        owner_user_id:
          type:
            - string
            - 'null'
      required:
        - created_at
    MCPServerResponseModel:
      type: object
      properties:
        id:
          type: string
        config:
          $ref: '#/components/schemas/MCPServerConfig-Output'
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
        dependent_agents:
          type: array
          items:
            $ref: '#/components/schemas/McpServerResponseModelDependentAgentsItems'
        metadata:
          $ref: '#/components/schemas/MCPServerMetadataResponseModel'
      required:
        - id
        - config
        - metadata

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.mcpServers.update("mcp_server_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.mcp_servers.update(
    mcp_server_id="mcp_server_id"
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


# Update MCP server approval policy

PATCH https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/approval-policy
Content-Type: application/json

Update the approval policy configuration for an MCP server. DEPRECATED: Use PATCH /mcp-servers/{id} endpoint instead.

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/mcp/approval-policies/update


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update Mcp Server Approval Policy
  version: endpoint_conversationalAi/mcpServers/approvalPolicy.update
paths:
  /v1/convai/mcp-servers/{mcp_server_id}/approval-policy:
    patch:
      operationId: update
      summary: Update Mcp Server Approval Policy
      description: >-
        Update the approval policy configuration for an MCP server. DEPRECATED:
        Use PATCH /mcp-servers/{id} endpoint instead.
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/mcpServers
          - subpackage_conversationalAi/mcpServers/approvalPolicy
      parameters:
        - name: mcp_server_id
          in: path
          description: ID of the MCP Server.
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MCPServerResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MCPApprovalPolicyUpdateRequestModel'
components:
  schemas:
    MCPApprovalPolicy:
      type: string
      enum:
        - value: auto_approve_all
        - value: require_approval_all
        - value: require_approval_per_tool
    MCPApprovalPolicyUpdateRequestModel:
      type: object
      properties:
        approval_policy:
          $ref: '#/components/schemas/MCPApprovalPolicy'
      required:
        - approval_policy
    MCPToolApprovalPolicy:
      type: string
      enum:
        - value: auto_approved
        - value: requires_approval
    MCPToolApprovalHash:
      type: object
      properties:
        tool_name:
          type: string
        tool_hash:
          type: string
        approval_policy:
          $ref: '#/components/schemas/MCPToolApprovalPolicy'
      required:
        - tool_name
        - tool_hash
    MCPServerTransport:
      type: string
      enum:
        - value: SSE
        - value: STREAMABLE_HTTP
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
    McpServerConfigOutputUrl:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
    ConvAIUserSecretDBModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        encrypted_value:
          type: string
        nonce:
          type: string
      required:
        - id
        - name
        - encrypted_value
        - nonce
    McpServerConfigOutputSecretToken:
      oneOf:
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIUserSecretDBModel'
    ConvAIDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
    McpServerConfigOutputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    ToolCallSoundType:
      type: string
      enum:
        - value: typing
        - value: elevator1
        - value: elevator2
        - value: elevator3
        - value: elevator4
    ToolCallSoundBehavior:
      type: string
      enum:
        - value: auto
        - value: always
    ToolExecutionMode:
      type: string
      enum:
        - value: immediate
        - value: post_tool_speech
        - value: async
    DynamicVariableAssignment:
      type: object
      properties:
        source:
          type: string
          enum:
            - type: stringLiteral
              value: response
        dynamic_variable:
          type: string
        value_path:
          type: string
      required:
        - dynamic_variable
        - value_path
    MCPToolConfigOverride:
      type: object
      properties:
        tool_name:
          type: string
        force_pre_tool_speech:
          type:
            - boolean
            - 'null'
        disable_interruptions:
          type:
            - boolean
            - 'null'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundBehavior'
            - type: 'null'
        execution_mode:
          oneOf:
            - $ref: '#/components/schemas/ToolExecutionMode'
            - type: 'null'
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
      required:
        - tool_name
    MCPServerConfig-Output:
      type: object
      properties:
        approval_policy:
          $ref: '#/components/schemas/MCPApprovalPolicy'
        tool_approval_hashes:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolApprovalHash'
        transport:
          $ref: '#/components/schemas/MCPServerTransport'
        url:
          $ref: '#/components/schemas/McpServerConfigOutputUrl'
        secret_token:
          oneOf:
            - $ref: '#/components/schemas/McpServerConfigOutputSecretToken'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/McpServerConfigOutputRequestHeaders'
        name:
          type: string
        description:
          type: string
        force_pre_tool_speech:
          type: boolean
        disable_interruptions:
          type: boolean
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        tool_config_overrides:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolConfigOverride'
      required:
        - url
        - name
    ResourceAccessInfoRole:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
        creator_name:
          type: string
        creator_email:
          type: string
        role:
          $ref: '#/components/schemas/ResourceAccessInfoRole'
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
    DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    DependentAvailableAgentIdentifier:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: available
        created_at_unix_secs:
          type: integer
        access_level:
          $ref: '#/components/schemas/DependentAvailableAgentIdentifierAccessLevel'
      required:
        - id
        - name
        - created_at_unix_secs
        - access_level
    DependentUnknownAgentIdentifier:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: unknown
    McpServerResponseModelDependentAgentsItems:
      oneOf:
        - $ref: '#/components/schemas/DependentAvailableAgentIdentifier'
        - $ref: '#/components/schemas/DependentUnknownAgentIdentifier'
    MCPServerMetadataResponseModel:
      type: object
      properties:
        created_at:
          type: integer
        owner_user_id:
          type:
            - string
            - 'null'
      required:
        - created_at
    MCPServerResponseModel:
      type: object
      properties:
        id:
          type: string
        config:
          $ref: '#/components/schemas/MCPServerConfig-Output'
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
        dependent_agents:
          type: array
          items:
            $ref: '#/components/schemas/McpServerResponseModelDependentAgentsItems'
        metadata:
          $ref: '#/components/schemas/MCPServerMetadataResponseModel'
      required:
        - id
        - config
        - metadata

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.mcpServers.approvalPolicy.update("mcp_server_id", {
        approvalPolicy: "auto_approve_all",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.mcp_servers.approval_policy.update(
    mcp_server_id="mcp_server_id",
    approval_policy="auto_approve_all"
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/approval-policy"

	payload := strings.NewReader("{\n  \"approval_policy\": \"auto_approve_all\"\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/approval-policy")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"approval_policy\": \"auto_approve_all\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/approval-policy")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"approval_policy\": \"auto_approve_all\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/approval-policy', [
  'body' => '{
  "approval_policy": "auto_approve_all"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/approval-policy");
var request = new RestRequest(Method.PATCH);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"approval_policy\": \"auto_approve_all\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["approval_policy": "auto_approve_all"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/approval-policy")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


# Create MCP server tool approval

POST https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-approvals
Content-Type: application/json

Add approval for a specific MCP tool when using per-tool approval mode.

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/mcp/approval-policies/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create Mcp Server Tool Approval
  version: endpoint_conversationalAi/mcpServers/toolApprovals.create
paths:
  /v1/convai/mcp-servers/{mcp_server_id}/tool-approvals:
    post:
      operationId: create
      summary: Create Mcp Server Tool Approval
      description: Add approval for a specific MCP tool when using per-tool approval mode.
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/mcpServers
          - subpackage_conversationalAi/mcpServers/toolApprovals
      parameters:
        - name: mcp_server_id
          in: path
          description: ID of the MCP Server.
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MCPServerResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MCPToolAddApprovalRequestModel'
components:
  schemas:
    McpToolAddApprovalRequestModelInputSchema:
      type: object
      properties: {}
    MCPToolApprovalPolicy:
      type: string
      enum:
        - value: auto_approved
        - value: requires_approval
    MCPToolAddApprovalRequestModel:
      type: object
      properties:
        tool_name:
          type: string
        tool_description:
          type: string
        input_schema:
          $ref: '#/components/schemas/McpToolAddApprovalRequestModelInputSchema'
        approval_policy:
          $ref: '#/components/schemas/MCPToolApprovalPolicy'
      required:
        - tool_name
        - tool_description
    MCPApprovalPolicy:
      type: string
      enum:
        - value: auto_approve_all
        - value: require_approval_all
        - value: require_approval_per_tool
    MCPToolApprovalHash:
      type: object
      properties:
        tool_name:
          type: string
        tool_hash:
          type: string
        approval_policy:
          $ref: '#/components/schemas/MCPToolApprovalPolicy'
      required:
        - tool_name
        - tool_hash
    MCPServerTransport:
      type: string
      enum:
        - value: SSE
        - value: STREAMABLE_HTTP
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
    McpServerConfigOutputUrl:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
    ConvAIUserSecretDBModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        encrypted_value:
          type: string
        nonce:
          type: string
      required:
        - id
        - name
        - encrypted_value
        - nonce
    McpServerConfigOutputSecretToken:
      oneOf:
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIUserSecretDBModel'
    ConvAIDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
    McpServerConfigOutputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    ToolCallSoundType:
      type: string
      enum:
        - value: typing
        - value: elevator1
        - value: elevator2
        - value: elevator3
        - value: elevator4
    ToolCallSoundBehavior:
      type: string
      enum:
        - value: auto
        - value: always
    ToolExecutionMode:
      type: string
      enum:
        - value: immediate
        - value: post_tool_speech
        - value: async
    DynamicVariableAssignment:
      type: object
      properties:
        source:
          type: string
          enum:
            - type: stringLiteral
              value: response
        dynamic_variable:
          type: string
        value_path:
          type: string
      required:
        - dynamic_variable
        - value_path
    MCPToolConfigOverride:
      type: object
      properties:
        tool_name:
          type: string
        force_pre_tool_speech:
          type:
            - boolean
            - 'null'
        disable_interruptions:
          type:
            - boolean
            - 'null'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundBehavior'
            - type: 'null'
        execution_mode:
          oneOf:
            - $ref: '#/components/schemas/ToolExecutionMode'
            - type: 'null'
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
      required:
        - tool_name
    MCPServerConfig-Output:
      type: object
      properties:
        approval_policy:
          $ref: '#/components/schemas/MCPApprovalPolicy'
        tool_approval_hashes:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolApprovalHash'
        transport:
          $ref: '#/components/schemas/MCPServerTransport'
        url:
          $ref: '#/components/schemas/McpServerConfigOutputUrl'
        secret_token:
          oneOf:
            - $ref: '#/components/schemas/McpServerConfigOutputSecretToken'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/McpServerConfigOutputRequestHeaders'
        name:
          type: string
        description:
          type: string
        force_pre_tool_speech:
          type: boolean
        disable_interruptions:
          type: boolean
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        tool_config_overrides:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolConfigOverride'
      required:
        - url
        - name
    ResourceAccessInfoRole:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
        creator_name:
          type: string
        creator_email:
          type: string
        role:
          $ref: '#/components/schemas/ResourceAccessInfoRole'
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
    DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    DependentAvailableAgentIdentifier:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: available
        created_at_unix_secs:
          type: integer
        access_level:
          $ref: '#/components/schemas/DependentAvailableAgentIdentifierAccessLevel'
      required:
        - id
        - name
        - created_at_unix_secs
        - access_level
    DependentUnknownAgentIdentifier:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: unknown
    McpServerResponseModelDependentAgentsItems:
      oneOf:
        - $ref: '#/components/schemas/DependentAvailableAgentIdentifier'
        - $ref: '#/components/schemas/DependentUnknownAgentIdentifier'
    MCPServerMetadataResponseModel:
      type: object
      properties:
        created_at:
          type: integer
        owner_user_id:
          type:
            - string
            - 'null'
      required:
        - created_at
    MCPServerResponseModel:
      type: object
      properties:
        id:
          type: string
        config:
          $ref: '#/components/schemas/MCPServerConfig-Output'
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
        dependent_agents:
          type: array
          items:
            $ref: '#/components/schemas/McpServerResponseModelDependentAgentsItems'
        metadata:
          $ref: '#/components/schemas/MCPServerMetadataResponseModel'
      required:
        - id
        - config
        - metadata

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.mcpServers.toolApprovals.create("mcp_server_id", {
        toolName: "string",
        toolDescription: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.mcp_servers.tool_approvals.create(
    mcp_server_id="mcp_server_id",
    tool_name="string",
    tool_description="string"
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals"

	payload := strings.NewReader("{\n  \"tool_name\": \"string\",\n  \"tool_description\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tool_name\": \"string\",\n  \"tool_description\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"tool_name\": \"string\",\n  \"tool_description\": \"string\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals', [
  'body' => '{
  "tool_name": "string",
  "tool_description": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"tool_name\": \"string\",\n  \"tool_description\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "tool_name": "string",
  "tool_description": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


# Delete MCP server tool approval

DELETE https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-approvals/{tool_name}

Remove approval for a specific MCP tool when using per-tool approval mode.

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/mcp/approval-policies/delete


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete Mcp Server Tool Approval
  version: endpoint_conversationalAi/mcpServers/toolApprovals.delete
paths:
  /v1/convai/mcp-servers/{mcp_server_id}/tool-approvals/{tool_name}:
    delete:
      operationId: delete
      summary: Delete Mcp Server Tool Approval
      description: >-
        Remove approval for a specific MCP tool when using per-tool approval
        mode.
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/mcpServers
          - subpackage_conversationalAi/mcpServers/toolApprovals
      parameters:
        - name: mcp_server_id
          in: path
          description: ID of the MCP Server.
          required: true
          schema:
            type: string
        - name: tool_name
          in: path
          description: Name of the MCP tool to remove approval for.
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MCPServerResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    MCPApprovalPolicy:
      type: string
      enum:
        - value: auto_approve_all
        - value: require_approval_all
        - value: require_approval_per_tool
    MCPToolApprovalPolicy:
      type: string
      enum:
        - value: auto_approved
        - value: requires_approval
    MCPToolApprovalHash:
      type: object
      properties:
        tool_name:
          type: string
        tool_hash:
          type: string
        approval_policy:
          $ref: '#/components/schemas/MCPToolApprovalPolicy'
      required:
        - tool_name
        - tool_hash
    MCPServerTransport:
      type: string
      enum:
        - value: SSE
        - value: STREAMABLE_HTTP
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
    McpServerConfigOutputUrl:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
    ConvAIUserSecretDBModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        encrypted_value:
          type: string
        nonce:
          type: string
      required:
        - id
        - name
        - encrypted_value
        - nonce
    McpServerConfigOutputSecretToken:
      oneOf:
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIUserSecretDBModel'
    ConvAIDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
    McpServerConfigOutputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    ToolCallSoundType:
      type: string
      enum:
        - value: typing
        - value: elevator1
        - value: elevator2
        - value: elevator3
        - value: elevator4
    ToolCallSoundBehavior:
      type: string
      enum:
        - value: auto
        - value: always
    ToolExecutionMode:
      type: string
      enum:
        - value: immediate
        - value: post_tool_speech
        - value: async
    DynamicVariableAssignment:
      type: object
      properties:
        source:
          type: string
          enum:
            - type: stringLiteral
              value: response
        dynamic_variable:
          type: string
        value_path:
          type: string
      required:
        - dynamic_variable
        - value_path
    MCPToolConfigOverride:
      type: object
      properties:
        tool_name:
          type: string
        force_pre_tool_speech:
          type:
            - boolean
            - 'null'
        disable_interruptions:
          type:
            - boolean
            - 'null'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundBehavior'
            - type: 'null'
        execution_mode:
          oneOf:
            - $ref: '#/components/schemas/ToolExecutionMode'
            - type: 'null'
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
      required:
        - tool_name
    MCPServerConfig-Output:
      type: object
      properties:
        approval_policy:
          $ref: '#/components/schemas/MCPApprovalPolicy'
        tool_approval_hashes:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolApprovalHash'
        transport:
          $ref: '#/components/schemas/MCPServerTransport'
        url:
          $ref: '#/components/schemas/McpServerConfigOutputUrl'
        secret_token:
          oneOf:
            - $ref: '#/components/schemas/McpServerConfigOutputSecretToken'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/McpServerConfigOutputRequestHeaders'
        name:
          type: string
        description:
          type: string
        force_pre_tool_speech:
          type: boolean
        disable_interruptions:
          type: boolean
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        tool_config_overrides:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolConfigOverride'
      required:
        - url
        - name
    ResourceAccessInfoRole:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
        creator_name:
          type: string
        creator_email:
          type: string
        role:
          $ref: '#/components/schemas/ResourceAccessInfoRole'
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
    DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    DependentAvailableAgentIdentifier:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: available
        created_at_unix_secs:
          type: integer
        access_level:
          $ref: '#/components/schemas/DependentAvailableAgentIdentifierAccessLevel'
      required:
        - id
        - name
        - created_at_unix_secs
        - access_level
    DependentUnknownAgentIdentifier:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: unknown
    McpServerResponseModelDependentAgentsItems:
      oneOf:
        - $ref: '#/components/schemas/DependentAvailableAgentIdentifier'
        - $ref: '#/components/schemas/DependentUnknownAgentIdentifier'
    MCPServerMetadataResponseModel:
      type: object
      properties:
        created_at:
          type: integer
        owner_user_id:
          type:
            - string
            - 'null'
      required:
        - created_at
    MCPServerResponseModel:
      type: object
      properties:
        id:
          type: string
        config:
          $ref: '#/components/schemas/MCPServerConfig-Output'
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
        dependent_agents:
          type: array
          items:
            $ref: '#/components/schemas/McpServerResponseModelDependentAgentsItems'
        metadata:
          $ref: '#/components/schemas/MCPServerMetadataResponseModel'
      required:
        - id
        - config
        - metadata

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.mcpServers.toolApprovals.delete("mcp_server_id", "tool_name");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.mcp_servers.tool_approvals.delete(
    mcp_server_id="mcp_server_id",
    tool_name="tool_name"
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals/tool_name"

	req, _ := http.NewRequest("DELETE", url, nil)

	req.Header.Add("xi-api-key", "xi-api-key")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals/tool_name")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals/tool_name")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals/tool_name', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals/tool_name");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals/tool_name")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


# Create configuration override

POST https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-configs
Content-Type: application/json

Create configuration overrides for a specific MCP tool.

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/mcp/tool-configuration/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create Mcp Tool Configuration Override
  version: endpoint_conversationalAi/mcpServers/toolConfigs.create
paths:
  /v1/convai/mcp-servers/{mcp_server_id}/tool-configs:
    post:
      operationId: create
      summary: Create Mcp Tool Configuration Override
      description: Create configuration overrides for a specific MCP tool.
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/mcpServers
          - subpackage_conversationalAi/mcpServers/toolConfigs
      parameters:
        - name: mcp_server_id
          in: path
          description: ID of the MCP Server.
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MCPServerResponseModel'
        '409':
          description: Tool config override already exists
          content: {}
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MCPToolConfigOverrideCreateRequestModel'
components:
  schemas:
    ToolCallSoundType:
      type: string
      enum:
        - value: typing
        - value: elevator1
        - value: elevator2
        - value: elevator3
        - value: elevator4
    ToolCallSoundBehavior:
      type: string
      enum:
        - value: auto
        - value: always
    ToolExecutionMode:
      type: string
      enum:
        - value: immediate
        - value: post_tool_speech
        - value: async
    DynamicVariableAssignment:
      type: object
      properties:
        source:
          type: string
          enum:
            - type: stringLiteral
              value: response
        dynamic_variable:
          type: string
        value_path:
          type: string
      required:
        - dynamic_variable
        - value_path
    MCPToolConfigOverrideCreateRequestModel:
      type: object
      properties:
        force_pre_tool_speech:
          type:
            - boolean
            - 'null'
        disable_interruptions:
          type:
            - boolean
            - 'null'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundBehavior'
            - type: 'null'
        execution_mode:
          oneOf:
            - $ref: '#/components/schemas/ToolExecutionMode'
            - type: 'null'
        assignments:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
        tool_name:
          type: string
      required:
        - tool_name
    MCPApprovalPolicy:
      type: string
      enum:
        - value: auto_approve_all
        - value: require_approval_all
        - value: require_approval_per_tool
    MCPToolApprovalPolicy:
      type: string
      enum:
        - value: auto_approved
        - value: requires_approval
    MCPToolApprovalHash:
      type: object
      properties:
        tool_name:
          type: string
        tool_hash:
          type: string
        approval_policy:
          $ref: '#/components/schemas/MCPToolApprovalPolicy'
      required:
        - tool_name
        - tool_hash
    MCPServerTransport:
      type: string
      enum:
        - value: SSE
        - value: STREAMABLE_HTTP
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
    McpServerConfigOutputUrl:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
    ConvAIUserSecretDBModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        encrypted_value:
          type: string
        nonce:
          type: string
      required:
        - id
        - name
        - encrypted_value
        - nonce
    McpServerConfigOutputSecretToken:
      oneOf:
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIUserSecretDBModel'
    ConvAIDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
    McpServerConfigOutputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    MCPToolConfigOverride:
      type: object
      properties:
        tool_name:
          type: string
        force_pre_tool_speech:
          type:
            - boolean
            - 'null'
        disable_interruptions:
          type:
            - boolean
            - 'null'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundBehavior'
            - type: 'null'
        execution_mode:
          oneOf:
            - $ref: '#/components/schemas/ToolExecutionMode'
            - type: 'null'
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
      required:
        - tool_name
    MCPServerConfig-Output:
      type: object
      properties:
        approval_policy:
          $ref: '#/components/schemas/MCPApprovalPolicy'
        tool_approval_hashes:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolApprovalHash'
        transport:
          $ref: '#/components/schemas/MCPServerTransport'
        url:
          $ref: '#/components/schemas/McpServerConfigOutputUrl'
        secret_token:
          oneOf:
            - $ref: '#/components/schemas/McpServerConfigOutputSecretToken'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/McpServerConfigOutputRequestHeaders'
        name:
          type: string
        description:
          type: string
        force_pre_tool_speech:
          type: boolean
        disable_interruptions:
          type: boolean
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        tool_config_overrides:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolConfigOverride'
      required:
        - url
        - name
    ResourceAccessInfoRole:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
        creator_name:
          type: string
        creator_email:
          type: string
        role:
          $ref: '#/components/schemas/ResourceAccessInfoRole'
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
    DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    DependentAvailableAgentIdentifier:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: available
        created_at_unix_secs:
          type: integer
        access_level:
          $ref: '#/components/schemas/DependentAvailableAgentIdentifierAccessLevel'
      required:
        - id
        - name
        - created_at_unix_secs
        - access_level
    DependentUnknownAgentIdentifier:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: unknown
    McpServerResponseModelDependentAgentsItems:
      oneOf:
        - $ref: '#/components/schemas/DependentAvailableAgentIdentifier'
        - $ref: '#/components/schemas/DependentUnknownAgentIdentifier'
    MCPServerMetadataResponseModel:
      type: object
      properties:
        created_at:
          type: integer
        owner_user_id:
          type:
            - string
            - 'null'
      required:
        - created_at
    MCPServerResponseModel:
      type: object
      properties:
        id:
          type: string
        config:
          $ref: '#/components/schemas/MCPServerConfig-Output'
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
        dependent_agents:
          type: array
          items:
            $ref: '#/components/schemas/McpServerResponseModelDependentAgentsItems'
        metadata:
          $ref: '#/components/schemas/MCPServerMetadataResponseModel'
      required:
        - id
        - config
        - metadata

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.mcpServers.toolConfigs.create("mcp_server_id", {
        toolName: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.mcp_servers.tool_configs.create(
    mcp_server_id="mcp_server_id",
    tool_name="string"
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs"

	payload := strings.NewReader("{\n  \"tool_name\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tool_name\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"tool_name\": \"string\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs', [
  'body' => '{
  "tool_name": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"tool_name\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["tool_name": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


---
**Navigation:** [← Previous](./29-delete-secret.md) | [Index](./index.md) | [Next →](./31-get-configuration-override.md)
