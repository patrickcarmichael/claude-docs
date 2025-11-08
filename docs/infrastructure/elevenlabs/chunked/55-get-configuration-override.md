**Navigation:** [← Previous](./54-create-mcp-server.md) | [Index](./index.md) | Next →

# Get configuration override

GET https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}

Retrieve configuration overrides for a specific MCP tool.

Reference: https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Mcp Tool Configuration Override
  version: endpoint_conversationalAi/mcpServers/toolConfigs.get
paths:
  /v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}:
    get:
      operationId: get
      summary: Get Mcp Tool Configuration Override
      description: Retrieve configuration overrides for a specific MCP tool.
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
        - name: tool_name
          in: path
          description: Name of the MCP tool to retrieve config overrides for.
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
                $ref: '#/components/schemas/MCPToolConfigOverride'
        '404':
          description: Tool config override not found
          content: {}
        '422':
          description: Validation Error
          content: {}
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

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.mcpServers.toolConfigs.get("mcp_server_id", "tool_name");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.mcp_servers.tool_configs.get(
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

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name"

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

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")! as URL,
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


# Update configuration override

PATCH https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}
Content-Type: application/json

Update configuration overrides for a specific MCP tool.

Reference: https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/update


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update Mcp Tool Configuration Override
  version: endpoint_conversationalAi/mcpServers/toolConfigs.update
paths:
  /v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}:
    patch:
      operationId: update
      summary: Update Mcp Tool Configuration Override
      description: Update configuration overrides for a specific MCP tool.
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
        - name: tool_name
          in: path
          description: Name of the MCP tool to update config overrides for.
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
        '404':
          description: Tool config override not found
          content: {}
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MCPToolConfigOverrideUpdateRequestModel'
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
    MCPToolConfigOverrideUpdateRequestModel:
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
    await client.conversationalAi.mcpServers.toolConfigs.update("mcp_server_id", "tool_name", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.mcp_servers.tool_configs.update(
    mcp_server_id="mcp_server_id",
    tool_name="tool_name"
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

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name"

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

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")

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
HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")! as URL,
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


# Delete configuration override

DELETE https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}

Remove configuration overrides for a specific MCP tool.

Reference: https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/delete


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete Mcp Tool Configuration Override
  version: endpoint_conversationalAi/mcpServers/toolConfigs.delete
paths:
  /v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}:
    delete:
      operationId: delete
      summary: Delete Mcp Tool Configuration Override
      description: Remove configuration overrides for a specific MCP tool.
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
        - name: tool_name
          in: path
          description: Name of the MCP tool to remove config overrides for.
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
    await client.conversationalAi.mcpServers.toolConfigs.delete("mcp_server_id", "tool_name");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.mcp_servers.tool_configs.delete(
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

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name"

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

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")! as URL,
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


# Create Single Use Token

POST https://api.elevenlabs.io/v1/single-use-token/{token_type}

Generate a time limited single-use token with embedded authentication for frontend clients.

Reference: https://elevenlabs.io/docs/api-reference/single-use/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create Single Use Token
  version: endpoint_tokens/singleUse.create
paths:
  /v1/single-use-token/{token_type}:
    post:
      operationId: create
      summary: Create Single Use Token
      description: >-
        Generate a time limited single-use token with embedded authentication
        for frontend clients.
      tags:
        - - subpackage_tokens
          - subpackage_tokens/singleUse
      parameters:
        - name: token_type
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/SingleUseTokenType'
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
                $ref: '#/components/schemas/SingleUseTokenResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    SingleUseTokenType:
      type: string
      enum:
        - value: realtime_scribe
    SingleUseTokenResponseModel:
      type: object
      properties:
        token:
          type: string
      required:
        - token

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.tokens.singleUse.create("realtime_scribe");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.tokens.single_use.create(
    token_type="realtime_scribe"
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

	url := "https://api.elevenlabs.io/v1/single-use-token/realtime_scribe"

	req, _ := http.NewRequest("POST", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/single-use-token/realtime_scribe")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/single-use-token/realtime_scribe")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/single-use-token/realtime_scribe', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/single-use-token/realtime_scribe");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/single-use-token/realtime_scribe")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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


# List voices

GET https://api.elevenlabs.io/v1/voices

Returns a list of all available voices for a user.

Reference: https://elevenlabs.io/docs/api-reference/legacy/voices/get-all


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List voices
  version: endpoint_voices.get_all
paths:
  /v1/voices:
    get:
      operationId: get-all
      summary: List voices
      description: Returns a list of all available voices for a user.
      tags:
        - - subpackage_voices
      parameters:
        - name: show_legacy
          in: query
          description: >-
            If set to true, legacy premade voices will be included in responses
            from /v1/voices
          required: false
          schema:
            type:
              - boolean
              - 'null'
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
                $ref: '#/components/schemas/GetVoicesResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    SpeakerSeparationResponseModelStatus:
      type: string
      enum:
        - value: not_started
        - value: pending
        - value: completed
        - value: failed
    UtteranceResponseModel:
      type: object
      properties:
        start:
          type: number
          format: double
        end:
          type: number
          format: double
      required:
        - start
        - end
    SpeakerResponseModel:
      type: object
      properties:
        speaker_id:
          type: string
        duration_secs:
          type: number
          format: double
        utterances:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/UtteranceResponseModel'
      required:
        - speaker_id
        - duration_secs
    SpeakerSeparationResponseModel:
      type: object
      properties:
        voice_id:
          type: string
        sample_id:
          type: string
        status:
          $ref: '#/components/schemas/SpeakerSeparationResponseModelStatus'
        speakers:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/SpeakerResponseModel'
        selected_speaker_ids:
          type:
            - array
            - 'null'
          items:
            type: string
      required:
        - voice_id
        - sample_id
        - status
    SampleResponseModel:
      type: object
      properties:
        sample_id:
          type: string
        file_name:
          type: string
        mime_type:
          type: string
        size_bytes:
          type: integer
        hash:
          type: string
        duration_secs:
          type:
            - number
            - 'null'
          format: double
        remove_background_noise:
          type:
            - boolean
            - 'null'
        has_isolated_audio:
          type:
            - boolean
            - 'null'
        has_isolated_audio_preview:
          type:
            - boolean
            - 'null'
        speaker_separation:
          oneOf:
            - $ref: '#/components/schemas/SpeakerSeparationResponseModel'
            - type: 'null'
        trim_start:
          type:
            - integer
            - 'null'
        trim_end:
          type:
            - integer
            - 'null'
    VoiceResponseModelCategory:
      type: string
      enum:
        - value: generated
        - value: cloned
        - value: premade
        - value: professional
        - value: famous
        - value: high_quality
    FineTuningResponseModelState:
      type: string
      enum:
        - value: not_started
        - value: queued
        - value: fine_tuning
        - value: fine_tuned
        - value: failed
        - value: delayed
    RecordingResponseModel:
      type: object
      properties:
        recording_id:
          type: string
        mime_type:
          type: string
        size_bytes:
          type: integer
        upload_date_unix:
          type: integer
        transcription:
          type: string
      required:
        - recording_id
        - mime_type
        - size_bytes
        - upload_date_unix
        - transcription
    VerificationAttemptResponseModel:
      type: object
      properties:
        text:
          type: string
        date_unix:
          type: integer
        accepted:
          type: boolean
        similarity:
          type: number
          format: double
        levenshtein_distance:
          type: number
          format: double
        recording:
          oneOf:
            - $ref: '#/components/schemas/RecordingResponseModel'
            - type: 'null'
      required:
        - text
        - date_unix
        - accepted
        - similarity
        - levenshtein_distance
    ManualVerificationFileResponseModel:
      type: object
      properties:
        file_id:
          type: string
        file_name:
          type: string
        mime_type:
          type: string
        size_bytes:
          type: integer
        upload_date_unix:
          type: integer
      required:
        - file_id
        - file_name
        - mime_type
        - size_bytes
        - upload_date_unix
    ManualVerificationResponseModel:
      type: object
      properties:
        extra_text:
          type: string
        request_time_unix:
          type: integer
        files:
          type: array
          items:
            $ref: '#/components/schemas/ManualVerificationFileResponseModel'
      required:
        - extra_text
        - request_time_unix
        - files
    FineTuningResponseModel:
      type: object
      properties:
        is_allowed_to_fine_tune:
          type: boolean
        state:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/FineTuningResponseModelState'
        verification_failures:
          type: array
          items:
            type: string
        verification_attempts_count:
          type: integer
        manual_verification_requested:
          type: boolean
        language:
          type:
            - string
            - 'null'
        progress:
          type:
            - object
            - 'null'
          additionalProperties:
            type: number
            format: double
        message:
          type:
            - object
            - 'null'
          additionalProperties:
            type: string
        dataset_duration_seconds:
          type:
            - number
            - 'null'
          format: double
        verification_attempts:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VerificationAttemptResponseModel'
        slice_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        manual_verification:
          oneOf:
            - $ref: '#/components/schemas/ManualVerificationResponseModel'
            - type: 'null'
        max_verification_attempts:
          type:
            - integer
            - 'null'
        next_max_verification_attempts_reset_unix_ms:
          type:
            - integer
            - 'null'
        finetuning_state:
          description: Any type
    VoiceSettingsResponseModel:
      type: object
      properties:
        stability:
          type:
            - number
            - 'null'
          format: double
        use_speaker_boost:
          type:
            - boolean
            - 'null'
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
        style:
          type:
            - number
            - 'null'
          format: double
        speed:
          type:
            - number
            - 'null'
          format: double
    voice_sharing_state:
      type: string
      enum:
        - value: enabled
        - value: disabled
        - value: copied
        - value: copied_disabled
    VoiceSharingResponseModelCategory:
      type: string
      enum:
        - value: generated
        - value: cloned
        - value: premade
        - value: professional
        - value: famous
        - value: high_quality
    review_status:
      type: string
      enum:
        - value: not_requested
        - value: pending
        - value: declined
        - value: allowed
        - value: allowed_with_changes
    VoiceSharingModerationCheckResponseModel:
      type: object
      properties:
        date_checked_unix:
          type:
            - integer
            - 'null'
        name_value:
          type:
            - string
            - 'null'
        name_check:
          type:
            - boolean
            - 'null'
        description_value:
          type:
            - string
            - 'null'
        description_check:
          type:
            - boolean
            - 'null'
        sample_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        sample_checks:
          type:
            - array
            - 'null'
          items:
            type: number
            format: double
        captcha_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        captcha_checks:
          type:
            - array
            - 'null'
          items:
            type: number
            format: double
    ReaderResourceResponseModelResourceType:
      type: string
      enum:
        - value: read
        - value: collection
    ReaderResourceResponseModel:
      type: object
      properties:
        resource_type:
          $ref: '#/components/schemas/ReaderResourceResponseModelResourceType'
        resource_id:
          type: string
      required:
        - resource_type
        - resource_id
    VoiceSharingResponseModel:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/voice_sharing_state'
        history_item_sample_id:
          type:
            - string
            - 'null'
        date_unix:
          type: integer
        whitelisted_emails:
          type: array
          items:
            type: string
        public_owner_id:
          type: string
        original_voice_id:
          type: string
        financial_rewards_enabled:
          type: boolean
        free_users_allowed:
          type: boolean
        live_moderation_enabled:
          type: boolean
        rate:
          type:
            - number
            - 'null'
          format: double
        fiat_rate:
          type:
            - number
            - 'null'
          format: double
        notice_period:
          type: integer
        disable_at_unix:
          type:
            - integer
            - 'null'
        voice_mixing_allowed:
          type: boolean
        featured:
          type: boolean
        category:
          $ref: '#/components/schemas/VoiceSharingResponseModelCategory'
        reader_app_enabled:
          type:
            - boolean
            - 'null'
        image_url:
          type:
            - string
            - 'null'
        ban_reason:
          type:
            - string
            - 'null'
        liked_by_count:
          type: integer
        cloned_by_count:
          type: integer
        name:
          type: string
        description:
          type:
            - string
            - 'null'
        labels:
          type: object
          additionalProperties:
            type: string
        review_status:
          $ref: '#/components/schemas/review_status'
        review_message:
          type:
            - string
            - 'null'
        enabled_in_library:
          type: boolean
        instagram_username:
          type:
            - string
            - 'null'
        twitter_username:
          type:
            - string
            - 'null'
        youtube_username:
          type:
            - string
            - 'null'
        tiktok_username:
          type:
            - string
            - 'null'
        moderation_check:
          oneOf:
            - $ref: '#/components/schemas/VoiceSharingModerationCheckResponseModel'
            - type: 'null'
        reader_restricted_on:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ReaderResourceResponseModel'
    VerifiedVoiceLanguageResponseModel:
      type: object
      properties:
        language:
          type: string
        model_id:
          type: string
        accent:
          type:
            - string
            - 'null'
        locale:
          type:
            - string
            - 'null'
        preview_url:
          type:
            - string
            - 'null'
      required:
        - language
        - model_id
    VoiceResponseModelSafetyControl:
      type: string
      enum:
        - value: NONE
        - value: BAN
        - value: CAPTCHA
        - value: ENTERPRISE_BAN
        - value: ENTERPRISE_CAPTCHA
    VoiceVerificationResponseModel:
      type: object
      properties:
        requires_verification:
          type: boolean
        is_verified:
          type: boolean
        verification_failures:
          type: array
          items:
            type: string
        verification_attempts_count:
          type: integer
        language:
          type:
            - string
            - 'null'
        verification_attempts:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VerificationAttemptResponseModel'
      required:
        - requires_verification
        - is_verified
        - verification_failures
        - verification_attempts_count
    VoiceResponseModel:
      type: object
      properties:
        voice_id:
          type: string
        name:
          type: string
        samples:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/SampleResponseModel'
        category:
          $ref: '#/components/schemas/VoiceResponseModelCategory'
        fine_tuning:
          oneOf:
            - $ref: '#/components/schemas/FineTuningResponseModel'
            - type: 'null'
        labels:
          type: object
          additionalProperties:
            type: string
        description:
          type:
            - string
            - 'null'
        preview_url:
          type:
            - string
            - 'null'
        available_for_tiers:
          type: array
          items:
            type: string
        settings:
          oneOf:
            - $ref: '#/components/schemas/VoiceSettingsResponseModel'
            - type: 'null'
        sharing:
          oneOf:
            - $ref: '#/components/schemas/VoiceSharingResponseModel'
            - type: 'null'
        high_quality_base_model_ids:
          type: array
          items:
            type: string
        verified_languages:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VerifiedVoiceLanguageResponseModel'
        safety_control:
          oneOf:
            - $ref: '#/components/schemas/VoiceResponseModelSafetyControl'
            - type: 'null'
        voice_verification:
          oneOf:
            - $ref: '#/components/schemas/VoiceVerificationResponseModel'
            - type: 'null'
        permission_on_resource:
          type:
            - string
            - 'null'
        is_owner:
          type:
            - boolean
            - 'null'
        is_legacy:
          type: boolean
        is_mixed:
          type: boolean
        favorited_at_unix:
          type:
            - integer
            - 'null'
        created_at_unix:
          type:
            - integer
            - 'null'
      required:
        - voice_id
    GetVoicesResponseModel:
      type: object
      properties:
        voices:
          type: array
          items:
            $ref: '#/components/schemas/VoiceResponseModel'
      required:
        - voices

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.voices.getAll({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.voices.get_all()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/voices"

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

url = URI("https://api.elevenlabs.io/v1/voices")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/voices");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices")! as URL,
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


# Voice design

POST https://api.elevenlabs.io/v1/text-to-voice/create-previews
Content-Type: application/json

Create a voice from a text prompt.

Reference: https://elevenlabs.io/docs/api-reference/legacy/voices/create-previews


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Voice design
  version: endpoint_textToVoice.create_previews
paths:
  /v1/text-to-voice/create-previews:
    post:
      operationId: create-previews
      summary: Voice design
      description: Create a voice from a text prompt.
      tags:
        - - subpackage_textToVoice
      parameters:
        - name: output_format
          in: query
          description: The output format of the generated audio.
          required: false
          schema:
            $ref: >-
              #/components/schemas/V1TextToVoiceCreatePreviewsPostParametersOutputFormat
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
                $ref: '#/components/schemas/VoicePreviewsResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VoicePreviewsRequestModel'
components:
  schemas:
    V1TextToVoiceCreatePreviewsPostParametersOutputFormat:
      type: string
      enum:
        - value: mp3_22050_32
        - value: mp3_24000_48
        - value: mp3_44100_32
        - value: mp3_44100_64
        - value: mp3_44100_96
        - value: mp3_44100_128
        - value: mp3_44100_192
        - value: pcm_8000
        - value: pcm_16000
        - value: pcm_22050
        - value: pcm_24000
        - value: pcm_32000
        - value: pcm_44100
        - value: pcm_48000
        - value: ulaw_8000
        - value: alaw_8000
        - value: opus_48000_32
        - value: opus_48000_64
        - value: opus_48000_96
        - value: opus_48000_128
        - value: opus_48000_192
    VoicePreviewsRequestModel:
      type: object
      properties:
        voice_description:
          type: string
        text:
          type:
            - string
            - 'null'
        auto_generate_text:
          type: boolean
        loudness:
          type: number
          format: double
        quality:
          type: number
          format: double
        seed:
          type:
            - integer
            - 'null'
        guidance_scale:
          type: number
          format: double
      required:
        - voice_description
    VoicePreviewResponseModel:
      type: object
      properties:
        audio_base_64:
          type: string
        generated_voice_id:
          type: string
        media_type:
          type: string
        duration_secs:
          type: number
          format: double
        language:
          type:
            - string
            - 'null'
      required:
        - audio_base_64
        - generated_voice_id
        - media_type
        - duration_secs
        - language
    VoicePreviewsResponseModel:
      type: object
      properties:
        previews:
          type: array
          items:
            $ref: '#/components/schemas/VoicePreviewResponseModel'
        text:
          type: string
      required:
        - previews
        - text

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.textToVoice.createPreviews({
        voiceDescription: "A sassy squeaky mouse",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_voice.create_previews(
    voice_description="A sassy squeaky mouse"
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

	url := "https://api.elevenlabs.io/v1/text-to-voice/create-previews"

	payload := strings.NewReader("{\n  \"voice_description\": \"A sassy squeaky mouse\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-voice/create-previews")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"voice_description\": \"A sassy squeaky mouse\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-voice/create-previews")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"voice_description\": \"A sassy squeaky mouse\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-voice/create-previews', [
  'body' => '{
  "voice_description": "A sassy squeaky mouse"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-voice/create-previews");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"voice_description\": \"A sassy squeaky mouse\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["voice_description": "A sassy squeaky mouse"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-voice/create-previews")! as URL,
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


# Save a voice preview

POST https://api.elevenlabs.io/v1/text-to-voice/create-voice-from-preview

Add a generated voice to the voice library.

Reference: https://elevenlabs.io/docs/api-reference/legacy/voices/save-a-voice-preview


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Save a voice preview
  version: endpoint_.saveAVoicePreview
paths:
  /v1/text-to-voice/create-voice-from-preview:
    post:
      operationId: save-a-voice-preview
      summary: Save a voice preview
      description: Add a generated voice to the voice library.
      tags:
        - []
      parameters:
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.saveAVoicePreview();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.save_a_voice_preview()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/text-to-voice/create-voice-from-preview"

	req, _ := http.NewRequest("POST", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/text-to-voice/create-voice-from-preview")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-voice/create-voice-from-preview")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-voice/create-voice-from-preview', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-voice/create-voice-from-preview");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-voice/create-voice-from-preview")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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


# Add To Knowledge Base

POST https://api.elevenlabs.io/v1/convai/knowledge-base
Content-Type: multipart/form-data

Upload a file or webpage URL to create a knowledge base document. <br> <Note> After creating the document, update the agent's knowledge base by calling [Update agent](/docs/api-reference/agents/update). </Note>

Reference: https://elevenlabs.io/docs/api-reference/legacy/knowledge-base/add-to-knowledge-base


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Add To Knowledge Base
  version: endpoint_conversationalAi.add_to_knowledge_base
paths:
  /v1/convai/knowledge-base:
    post:
      operationId: add-to-knowledge-base
      summary: Add To Knowledge Base
      description: >-
        Upload a file or webpage URL to create a knowledge base document. <br>
        <Note> After creating the document, update the agent's knowledge base by
        calling [Update agent](/docs/api-reference/agents/update). </Note>
      tags:
        - - subpackage_conversationalAi
      parameters:
        - name: agent_id
          in: query
          required: false
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
                $ref: '#/components/schemas/AddKnowledgeBaseResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                name:
                  type:
                    - string
                    - 'null'
                url:
                  type: string
components:
  schemas:
    AddKnowledgeBaseResponseModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
      required:
        - id
        - name

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.addToKnowledgeBase({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.add_to_knowledge_base()

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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base', [
  'multipart' => [
    [
        'name' => 'file',
        'filename' => '<file1>',
        'contents' => null
    ]
  ]
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
]
let parameters = [
  [
    "name": "name",
    "value": 
  ],
  [
    "name": "url",
    "value": 
  ],
  [
    "name": "file",
    "fileName": "<file1>"
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base")! as URL,
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
**Navigation:** [← Previous](./54-create-mcp-server.md) | [Index](./index.md) | Next →
