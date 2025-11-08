**Navigation:** [← Previous](./30-create-mcp-server.md) | [Index](./index.md) | [Next →](./32-create-speech-with-timing.md)

# Get configuration override

GET https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}

Retrieve configuration overrides for a specific MCP tool.

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/mcp/tool-configuration/get


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

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/mcp/tool-configuration/update


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

Reference: https://elevenlabs.io/docs/agents-platform/api-reference/mcp/tool-configuration/delete


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


# HIPAA

> Learn how ElevenLabs Agents, coupled with Zero Retention Mode, is designed to promote HIPAA compliance for healthcare applications. Please refer to our [compliance page](https://compliance.elevenlabs.io/) for the latest information.


## Overview

ElevenLabs Agents is one of ElevenLabs' HIPAA-eligible services, and we offer Business Associate Agreements (BAAs) to eligible customers. To the extent Covered Entities and Business Associates, as defined under HIPAA, have executed a BAA and have Zero Retention Mode engaged, ElevenLabs allows such customers to develop AI-powered voice agents for the handling Protected Health Information (PHI). The application of Zero Retention Mode is designed to promote compliance with HIPAA by limiting the processing of such PHI. You can read more about [Zero Retention Mode here](/docs/resources/zero-retention-mode).


## Controls designed to promote HIPAA compliance

When HIPAA compliance is required for a workspace, and to the extent a BAA has been executed with ElevenLabs, the following policies are enabled:

1. **Zero Retention Mode** - You can read more about [Zero Retention Mode here](/docs/resources/zero-retention-mode)
2. **LLM Provider Restrictions** - Only LLM from providers with whom we have a BAA in place are available as preconfigured options
3. **Storage Limitations** - Raw audio files and transcripts containing PHI are not retained

<Note>
  If you want to use LLMs that aren't available preconfigured in Zero Retention Mode, you can still use them in Agents Platform by:

  1. Arranging to sign a BAA directly with the LLM provider you'd like to use
  2. Using your API key with our Custom LLM integration
</Note>

To the extent Zero Retention Mode is engaged, ElevenLabs' platform is designed to ensure that PHI shared as part of a conversation is not stored or logged in any system component, including:

* Conversation transcripts
* Audio recordings
* Tool calls and results
* Data analytics
* System logs

<Warning>
  For Agents Platform, your BAA applies only to the extent provided therein. To the extent you wish
  to forego Zero Retention Mode with respect to any ElevenLabs agent, no PHI should be submitted to
  the Service in connection therewith, and such agent is no longer deemed a covered service for
  purposes of the BAA. Notwithstanding anything to the contrary, while ElevenLabs' Agents Platform
  Service, coupled with Zero Retention Mode, is designed to promote compliance with HIPAA, you are
  fully responsible for ensuring compliance with all obligations applicable to you and for ensuring
  your use of the Services is compliant with all applicable laws.
</Warning>


## Enterprise customers

<Note>
  Execution of a BAA, as may be required by HIPAA, is only available for Enterprise tier
  subscriptions. Contact your account representative to discuss further. PHI should not be submitted
  to the ElevenLabs Services unless a BAA is in place and only to the extent permitted under such
  BAA.
</Note>


## Available LLMs

When operating in Zero Retention Mode, only the following LLMs are available:

<AccordionGroup>
  <Accordion title="Google Models">
    * Gemini 2.5 Flash
    * Gemini 2.5 Flash Lite
    * Gemini 2.0 Flash
    * Gemini 2.0 Flash Lite
    * Gemini 1.5 Flash
    * Gemini 1.5 Pro
    * Gemini 1.0 Pro
  </Accordion>

  <Accordion title="Anthropic Models">
    * Claude 3.7 Sonnet
    * Claude 3.5 Sonnet
    * Claude 3.0 Haiku
  </Accordion>

  <Accordion title="Custom LLMs">
    * [Custom LLM](/docs/agents-platform/customization/llm/custom-llm) (supports any OpenAI-API
      compatible provider and requires you to bring your own API keys)
  </Accordion>
</AccordionGroup>


## Technical implementation

Zero Retention Mode implements several safeguards and is designed to:

1. **LLM Allowlist** - Prevent use of LLMs except as provided above
2. **PII Redaction** - Automatically redact sensitive fields before storage
3. **Storage Prevention** - Disable uploading of raw audio files to cloud


## Developer experience

When working with Zero Retention Mode agents:

<Steps>
  <Step title="LLMs (except the available LLMs as described above) are disabled in the UI">
    <Frame background="subtle" caption="The UI shows disabled LLM options with tooltip explanations">
      ![Redacted conversation analysis showing Zero Retention Mode in
      action](file:73d6a46d-57fa-4a4f-8053-2543fdf7112d)
    </Frame>
  </Step>

  <Step title="Content is redacted from content history">
    <Frame background="subtle" caption="All sensitive information contained within the prompt or output is redacted and not stored">
      ![Redacted conversation history showing Zero Retention Mode in
      action](file:bbf3e22a-4771-4df8-ae1b-4fc053bf1e1b)
    </Frame>
  </Step>

  <Step title="Conversation analysis is limited">
    <Frame background="subtle" caption="Minimal information is visible to ElevenLabs given Zero Retention Mode">
      ![Redacted conversation analysis showing HIPAA compliance in
      action](file:545d5108-2eba-41af-9f47-2f5c5e9b4974)
    </Frame>
  </Step>
</Steps>

### API restrictions are enforced

API calls attempting to use unavailable LLMs will receive an HTTP 400 error. Analytics data will be limited to non-sensitive metrics only.


## FAQ

<AccordionGroup>
  <Accordion title="Can I use any LLM if I am subject to HIPAA?">
    No. In such case, you can only use LLMs from the approved list. Attempts to use other LLMs will
    produce an error. You can always use a custom LLM if you need a specific model not on the
    allowlist.
  </Accordion>

  <Accordion title="Can I execute a BAA with ElevenLabs if I am subject to HIPAA?">
    BAAs are only available to enterprise customers. Please refer to your account executive to
    discuss further.
  </Accordion>

  <Accordion title="Does the application of Zero Retention Mode affect conversation quality?">
    No. Zero Retention Mode and the execution of a BAA only affects how data is stored and which
    LLMs can be used. It does not impact the quality or functionality of conversations while they
    are active.
  </Accordion>

  <Accordion title="Can I still analyze conversation data?">
    Yes, but with limitations. Conversation analytics will only include non-sensitive metadata like
    call duration and success rates. Specific content from conversations will not be available.
  </Accordion>
</AccordionGroup>


## Considerations

When building voice agents, you may consider:

1. **Use Custom LLMs** when possible, which may provide enhanced control over data processing
2. **Implement proper authentication** for all healthcare applications
3. **Validate configuration** is correct by checking redaction before launching + passing PHI


## Related resources

<CardGroup cols={2}>
  <Card title="Agents Platform Security" href="/docs/agents-platform/customization/authentication">
    Learn about securing your ElevenLabs agents
  </Card>

  <Card title="Custom LLM Integration" href="/docs/agents-platform/customization/llm/custom-llm">
    Set up your own LLM for maximum control and compliance
  </Card>
</CardGroup>



# TCPA Compliance

> Understand key TCPA requirements for using AI agents in outbound calling

<Warning title="Legal Disclaimer">
  This guide is for informational purposes only and is not comprehensive. This guide does not
  constitute legal advice. The TCPA is complex and subject to interpretation. Consult with qualified
  legal counsel to ensure your specific use of ElevenLabs Agents for outbound calling
  complies with all applicable laws and regulations. Visit our [Compliance Portal](https://elevenlabs.io/compliance) for comprehensive information on
  our certifications and practices.
</Warning>

This guide provides a high-level overview of certain key requirements under the Telephone Consumer Protection Act (TCPA) for developers and businesses using ElevenLabs Agents for outbound calls in the United States. Adherence to the TCPA is critical when making automated calls or using AI-generated voices for outbound communications.

<Note>
  The TCPA primarily governs **outbound** calls and texts. It does not generally apply to inbound
  communications initiated by the consumer. In addition to complying with the TCPA, you must also
  comply with all applicable state-level laws that may govern telemarketing, automated calls, or the
  use of AI-generated voices. Many states have enacted their own regulations that may be more
  restrictive than federal requirements.
</Note>


## Types of Consent Required

The type of consent needed under the TCPA depends on whether your outbound call using ElevenLabs AI voice is classified as **marketing** or **non-marketing**. ElevenLabs' AI-generated voices are considered "artificial or prerecorded voices" under the TCPA, triggering specific consent rules.

| Call Type using ElevenLabs AI          | Consent Required                         | Consent Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                | Sample Consent Disclosure Language (Illustrative)                                                                                                                                                                                        |
| :------------------------------------- | :--------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Marketing Call**                     | **Prior Express Written Consent (PEWC)** | 1. A **signed written agreement** from the recipient (electronic signatures under E-SIGN Act are valid).<br /><br />2. The agreement must feature a **clear and conspicuous disclosure** stating that:<br />     (A) The recipient authorizes *\[Your Company Name]* to make automated calls using an artificial/prerecorded voice to the specific phone number provided; **AND**<br />     (B) Consent is **not** a condition of purchasing any goods or services. | "By checking this box and providing my phone number, I agree to receive automated marketing calls from \[Your Company Name], including using an AI-generated voice, at the number provided. Consent is not a condition of any purchase." |
| **Non-Marketing / Informational Call** | **Prior Express Consent (PEC)**          | The consumer must have given permission to be contacted at the number provided for informational purposes (e.g., providing a phone number for appointment reminders or account updates). While not always requiring a written agreement like PEWC, consent must still be express and affirmative.                                                                                                                                                                   | "Please provide your phone number if you'd like to receive \[e.g., appointment reminders, service updates] from *\[Your Company Name]*, including automated calls using an AI-generated voice."                                          |

<Note>
  \*Signatures for PEWC can comply with the E-SIGN Act (e.g., via website form submission, email
  confirmation, or a recorded telephone keypress after clear disclosure).
</Note>


## Key Compliance Guidelines for Developers

When using ElevenLabs Agents for outbound calling:

1. **Affirmative Opt-In**: Consent must be affirmative. Pre-checked boxes for consent are not compliant.
2. **Consent Revocation**: Consumers can revoke consent at any time through "any reasonable manner" (e.g., verbal request during a call, email, text reply like "STOP").
   * Ensure your system, especially interactive AI, can recognize and process opt-out requests, for example using our [end call tool](/docs/)
   * Honor revocations promptly, and in all cases within 10 business days..
3. **Record Keeping**: Maintain clear records of all obtained consents (who, when, where, and how consent was given) and any revocations. The burden of proving consent is on the caller.
4. **Calling Time Restrictions**: Outbound calls to residential numbers are restricted to 8:00 a.m. to 9:00 p.m. in the recipient's local time zone. Implement time-zone awareness.
5. **Do-Not-Call (DNC) Lists**:
   * Maintain an internal DNC list of individuals who have asked not to be called.
   * For marketing calls, scrub lists against the National DNC Registry, unless an exception (like valid PEWC) applies.
6. **Identify the Caller**: Clearly state the name of the company at the beginning of the call.
7. **Provide a Callback Number**: Share a toll-free number that recipients can use to opt out of future calls.
8. **Enable Automated Opt-Outs for Promotional Calls**: For promotional calls, provide an automated opt-out mechanism within two seconds of identifying the company. Include brief instructions on how to use it. If the recipient opts out, the system must (i) immediately end the call and (ii) record the number on the company's internal opt-out list. If leaving a voicemail, include a toll-free number that connects to an automated opt-out system with the same functionality.


## Understanding "Marketing"

Under the TCPA, a call is generally considered **"marketing"** if its purpose is to:

* Encourage the purchase or rental of, or investment in, property, goods, or services.
* Advertise the commercial availability or quality of any property, goods, or services.

If your call includes any promotional content, it will likely be classified as marketing, requiring PEWC.



# Disclosure requirements

> Informing end users about your use of ElevenLabs Agents


## Overview

Your use of ElevenLabs Agents is subject to our [Agents Platform terms](https://elevenlabs.io/agents-terms). As outlined in those Terms, you are required to provide clear notice to your end users that:

* They are interacting with AI rather than a human
* Their conversations are being recorded and may be shared with ElevenLabs and its third-party large language model providers


## Implementation

This disclosure must be presented immediately prior to any interaction with the Agents Platform. Common implementation methods include:

* A separate screen or interstitial page
* A pop-up notice
* A persistent banner
* A verbal or pre-recorded disclosure at the start of a voice call

<Warning>
  Users must not be able to access or use the feature without first being presented with this
  notice.
</Warning>

In addition to satisfying our contractual requirements, this approach promotes transparency and builds trust by ensuring users understand the nature of the interaction.


## Sample written disclosure language

You should modify this example to reflect your specific use case while maintaining the required disclosures.

<Note title="ElevenLabs Agents">
  We use ElevenLabs Agents to help power our \[insert purposes, e.g., virtual customer service
  agents]. By clicking "Agree" and each time you interact with this AI agent, you consent to us,
  ElevenLabs, and each of our service providers (including third-party LLM providers) recording,
  viewing, storing, and sharing your communications to provide the service, improve our products and
  services, train machine learning models, and comply with applicable law.
</Note>


## Sample verbal disclosure language

Hi, I’m an AI assistant. This call may be recorded and shared with service providers for quality assurance and service improvement purposes.
For more information, please refer to our privacy policy available at: \[insert link].


## Legal disclaimer

<Warning>
  The information provided above is for general informational purposes only. Your organization is
  solely responsible for ensuring that its use of ElevenLabs Agents complies with the [Agents
  Platform Terms](https://elevenlabs.io/agents-terms) and all applicable laws and regulations. This
  guidance does not constitute legal advice. You should consult your legal counsel regarding any
  questions about legal or regulatory compliance.
</Warning>



# 11.ai integrations

> Learn about third-party integrations and their automatic Zero Retention Mode (ZRM) requirements for data privacy and compliance.


## Overview

11.ai supports various third-party integrations to seamlessly connect with your everyday applications. Some integrations automatically enable Zero Retention Mode (ZRM) to ensure compliance with industry regulations and data privacy requirements.

<Warning>
  When any integration marked with ZRM is added to an agent, all conversation data is processed in
  Zero Retention Mode, meaning no conversation transcripts, audio recordings, or personally
  identifiable information (PII) is stored or logged by ElevenLabs.
</Warning>


## Zero Retention Mode enforcement

As soon as any integration that requires ZRM is added to an agent, the entire agent automatically operates in Zero Retention Mode. This ensures:

* No call recordings are stored
* No conversation transcripts containing PII are logged
* All data is processed only in volatile memory during the request
* Compliance with healthcare (HIPAA), financial, and other regulatory requirements


## Integrations with Zero Retention Mode

The following integrations automatically enforce Zero Retention Mode to ensure compliance with data privacy policies:

| Integration     | Description                     | ZRM | Use Case                     | Compliance Requirements                  |
| --------------- | ------------------------------- | :-: | ---------------------------- | ---------------------------------------- |
| Gmail           | Email management service        |  ✅  | Email reading, organization  | Google Workspace APIs Limited Use policy |
| Google Calendar | Calendar and scheduling service |  ✅  | Event management, scheduling | Google Workspace APIs Limited Use policy |


## Google Workspace API compliance

Google integrations require Zero Retention Mode to comply with Google's Workspace APIs data policy requirements:

* **Limited Use requirements**: User data from Workspace APIs cannot be used for foundational AI/ML model training
* **Data retention restrictions**: No permanent copies of user content are created or cached beyond permitted timeframes
* **Express permission mandate**: All content access requires explicit user consent
* **Security assessment**: CASA (Cloud Application Security Assessment) certification required for restricted API scopes

<Warning>
  Google Workspace integrations are subject to additional compliance requirements and security
  assessments. Data from these integrations is processed exclusively in Zero Retention Mode with no
  storage or logging of user content.
</Warning>

<Note>
  This list is regularly updated as new integrations become available. For the most current
  information about specific integrations, please contact your ElevenLabs representative.
</Note>



# Agent tools deprecation

> Migrate from legacy `prompt.tools` to the new `prompt.tool_ids` field.


## Overview

<Info>
  The way you wire tools into your ConvAI agents is getting a refresh.
</Info>

### What's changing?

* The old request field `body.conversation_config.agent.prompt.tools` is **deprecated**.
* Use `body.conversation_config.agent.prompt.tool_ids` to list the IDs of the client or server tools your agent should use.
* **New field** `prompt.built_in_tools` is introduced for **system tools** (e.g., `end_call`, `language_detection`). These tools are referenced by **name**, not by ID.

### Critical deadlines

<Check>
  **July 14, 2025** - Last day for full backwards compatibility. You can continue using
  `prompt.tools` until this date.
</Check>

<Note>
  **July 15, 2025** - GET endpoints will stop returning the `tools` field. Only `prompt.tool_ids`
  will be included in responses.
</Note>

<Warning>
  **July 23, 2025** - Legacy `prompt.tools` field will be permanently removed. All requests
  containing this field will be rejected.
</Warning>


## Why the change?

Decoupling tools from agents brings several advantages:

* **Re-use** – the same tool can be shared across multiple agents.
* **Simpler audits** – inspect, update or delete a tool in one place.
* **Cleaner payloads** – agent configurations stay lightweight.


## What has already happened?

<Check>
  Good news — we've already migrated your data! Every tool that previously lived in `prompt.tools`
  now exists as a standalone record, and its ID is present in the agent's `prompt.tool_ids` array.
  No scripts required.
</Check>

We have **automatically migrated all existing data**:

* Every tool that was previously in an agent's `prompt.tools` array now exists as a standalone record.
* The agent's `prompt.tool_ids` array already references those new tool records.

No one-off scripts are required — your agents continue to work unchanged.


## Deprecation timeline

| Date              | Status                   | Behaviour                                                                        |
| ----------------- | ------------------------ | -------------------------------------------------------------------------------- |
| **July 14, 2025** | ✅ Full compatibility     | You may keep sending `prompt.tools`. GET responses include the `tools` field.    |
| **July 15, 2025** | ⚠️ Partial compatibility | GET endpoints stop returning the `tools` field. Only `prompt.tool_ids` included. |
| **July 23, 2025** | ❌ No compatibility       | POST and PATCH endpoints **reject** any request containing `prompt.tools`.       |


## Toolbox endpoint

All tool management lives under a dedicated endpoint:

```http title="Tool management"
POST | GET | PATCH | DELETE  https://api.elevenlabs.io/v1/convai/tools
```

Use it to:

* **Create** a tool and obtain its ID.
* **Update** it when requirements change.
* **Delete** it when it is no longer needed.

Anything that once sat in the old `tools` array now belongs here.


## Migration guide

<Error>
  System tools are **not** supported in `prompt.tool_ids`. Instead, specify them in the **new**
  `prompt.built_in_tools` field.
</Error>

If you are still using the legacy field, follow the steps below.

<Steps>
  ### 1. Stop sending `prompt.tools`

  Remove the `tools` array from your agent configuration.

  ### 2. Send the tool IDs instead

  Replace it with `prompt.tool_ids`, containing the IDs of the client or server tools the agent
  should use.

  ### 3. (Optional) Clean up

  After 23 July, delete any unused standalone tools via the toolbox endpoint.
</Steps>


## Example payloads

<Note>
  A request must include **either** `prompt.tool_ids` **or** the legacy `prompt.tools` array —
  **never both**. Sending both fields results in an error.
</Note>

<CodeBlocks>
  ```json title="Legacy format (deprecated)"
  {
    "conversation_config": {
      "agent": {
        "prompt": {
          "tools": [
            {
              "type": "client", 
              "name": "open_url",
              "description": "Open a provided URL in the user's browser."
            },
            {
              "type": "system",
              "name": "end_call", 
              "description": "",
              "response_timeout_secs": 20,
              "params": {
                "system_tool_type": "end_call"
              }
            }
          ]
        }
      }
    }
  }
  ```

  ```json title="New format (recommended) – client tool via ID + system tool"
  {
    "conversation_config": {
      "agent": {
        "prompt": {
          "tool_ids": ["tool_123456789abcdef0"],
          "built_in_tools": {
            "end_call": {
              "name": "end_call",
              "description": "",
              "response_timeout_secs": 20,
              "type": "system",
              "params": {
                "system_tool_type": "end_call"
              }
            },
            "language_detection": null,
            "transfer_to_agent": null,
            "transfer_to_number": null,
            "skip_turn": null
          }
        }
      }
    }
  }
  ```
</CodeBlocks>


## FAQ

<AccordionGroup>
  <Accordion title="Will my existing integrations break?">
    No. Until July 23, the API will silently migrate any `prompt.tools` array you send. However,
    starting July 15, GET and PATCH responses will no longer include full tool objects. After July
    23, any POST/PATCH requests containing `prompt.tools` will be rejected.
  </Accordion>

  <Accordion title="Can I mix both fields in one request?">
    No. A request must use **either** `prompt.tool_ids` **or** `prompt.tools` — never both.
  </Accordion>

  <Accordion title="How do I find a tool's ID?">
    List your tools via `GET /v1/convai/tools` or inspect the response when you create one.
  </Accordion>
</AccordionGroup>



# Introduction

> Explore the ElevenLabs API reference with comprehensive guides, code examples, and endpoint documentation


## Installation

You can interact with the API through HTTP or Websocket requests from any language, via our official Python bindings or our official Node.js libraries.

To install the official Python bindings, run the following command:

```bash
pip install elevenlabs
```

To install the official Node.js library, run the following command in your Node.js project directory:

```bash
npm install @elevenlabs/elevenlabs-js
```

<div id="overview-wave">
  <ElevenLabsWaveform color="gray" />
</div>



# API Authentication

> Learn how to authenticate your ElevenLabs API requests


## API Keys

The ElevenLabs API uses API keys for authentication. Every request to the API must include your API key, used to authenticate your requests and track usage quota.

Each API key can be scoped to one of the following:

1. **Scope restriction:** Set access restrictions by limiting which API endpoints the key can access.
2. **Credit quota:** Define custom credit limits to control usage.

**Remember that your API key is a secret.** Do not share it with others or expose it in any client-side code (browsers, apps).

All API requests should include your API key in an `xi-api-key` HTTP header as follows:

```bash
xi-api-key: ELEVENLABS_API_KEY
```

### Making requests

You can paste the command below into your terminal to run your first API request. Make sure to replace `$ELEVENLABS_API_KEY` with your secret API key.

```bash
curl 'https://api.elevenlabs.io/v1/models' \
  -H 'Content-Type: application/json' \
  -H 'xi-api-key: $ELEVENLABS_API_KEY'
```

Example with the `elevenlabs` Python package:

```python
from elevenlabs.client import ElevenLabs

elevenlabs = ElevenLabs(
  api_key='YOUR_API_KEY',
)
```

Example with the `elevenlabs` Node.js package:

```javascript
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

const elevenlabs = new ElevenLabsClient({
  apiKey: 'YOUR_API_KEY',
});
```



# Streaming

> Learn how to stream real-time audio from the ElevenLabs API using chunked transfer encoding

The ElevenLabs API supports real-time audio streaming for select endpoints, returning raw audio bytes (e.g., MP3 data) directly over HTTP using chunked transfer encoding. This allows clients to process or play audio incrementally as it is generated.

Our official [Node](https://github.com/elevenlabs/elevenlabs-js) and [Python](https://github.com/elevenlabs/elevenlabs-python) libraries include utilities to simplify handling this continuous audio stream.

Streaming is supported for the [Text to Speech API](/docs/api-reference/streaming), [Voice Changer API](/docs/api-reference/speech-to-speech-streaming) & [Audio Isolation API](/docs/api-reference/audio-isolation-stream). This section focuses on how streaming works for requests made to the Text to Speech API.

In Python, a streaming request looks like:

```python
from elevenlabs import stream
from elevenlabs.client import ElevenLabs

elevenlabs = ElevenLabs()

audio_stream = elevenlabs.text_to_speech.stream(
    text="This is a test",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2"
)

# option 1: play the streamed audio locally
stream(audio_stream)

# option 2: process the audio bytes manually
for chunk in audio_stream:
    if isinstance(chunk, bytes):
        print(chunk)
```

In Node / Typescript, a streaming request looks like:

```javascript maxLines=0
import { ElevenLabsClient, stream } from '@elevenlabs/elevenlabs-js';
import { Readable } from 'stream';

const elevenlabs = new ElevenLabsClient();

async function main() {
  const audioStream = await elevenlabs.textToSpeech.stream('JBFqnCBsd6RMkjVDRZzb', {
    text: 'This is a test',
    modelId: 'eleven_multilingual_v2',
  });

  // option 1: play the streamed audio locally
  await stream(Readable.from(audioStream));

  // option 2: process the audio manually
  for await (const chunk of audioStream) {
    console.log(chunk);
  }
}

main();
```



# WebSocket

GET /v1/text-to-speech/{voice_id}/stream-input

The Text-to-Speech WebSockets API is designed to generate audio from partial text input
while ensuring consistency throughout the generated audio. Although highly flexible,
the WebSockets API isn't a one-size-fits-all solution. It's well-suited for scenarios where:
  * The input text is being streamed or generated in chunks.
  * Word-to-audio alignment information is required.

However, it may not be the best choice when:
  * The entire input text is available upfront. Given that the generations are partial,
    some buffering is involved, which could potentially result in slightly higher latency compared
    to a standard HTTP request.
  * You want to quickly experiment or prototype. Working with WebSockets can be harder and more
    complex than using a standard HTTP API, which might slow down rapid development and testing.


Reference: https://elevenlabs.io/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-stream-input


## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: V 1 Text To Speech Voice Id Stream Input
  version: subpackage_v1TextToSpeechVoiceIdStreamInput.v1TextToSpeechVoiceIdStreamInput
  description: >
    The Text-to-Speech WebSockets API is designed to generate audio from partial
    text input

    while ensuring consistency throughout the generated audio. Although highly
    flexible,

    the WebSockets API isn't a one-size-fits-all solution. It's well-suited for
    scenarios where:
      * The input text is being streamed or generated in chunks.
      * Word-to-audio alignment information is required.

    However, it may not be the best choice when:
      * The entire input text is available upfront. Given that the generations are partial,
        some buffering is involved, which could potentially result in slightly higher latency compared
        to a standard HTTP request.
      * You want to quickly experiment or prototype. Working with WebSockets can be harder and more
        complex than using a standard HTTP API, which might slow down rapid development and testing.
channels:
  /v1/text-to-speech/{voice_id}/stream-input:
    description: >
      The Text-to-Speech WebSockets API is designed to generate audio from
      partial text input

      while ensuring consistency throughout the generated audio. Although highly
      flexible,

      the WebSockets API isn't a one-size-fits-all solution. It's well-suited
      for scenarios where:
        * The input text is being streamed or generated in chunks.
        * Word-to-audio alignment information is required.

      However, it may not be the best choice when:
        * The entire input text is available upfront. Given that the generations are partial,
          some buffering is involved, which could potentially result in slightly higher latency compared
          to a standard HTTP request.
        * You want to quickly experiment or prototype. Working with WebSockets can be harder and more
          complex than using a standard HTTP API, which might slow down rapid development and testing.
    parameters:
      voice_id:
        description: The unique identifier for the voice to use in the TTS process.
        schema:
          type: string
    bindings:
      ws:
        query:
          type: object
          properties:
            authorization:
              type: string
            model_id:
              type: string
            language_code:
              type: string
            enable_logging:
              type: boolean
            enable_ssml_parsing:
              type: boolean
            output_format:
              $ref: '#/components/schemas/output_format'
            inactivity_timeout:
              type: integer
            sync_alignment:
              type: boolean
            auto_mode:
              type: boolean
            apply_text_normalization:
              $ref: '#/components/schemas/apply_text_normalization'
            seed:
              type: integer
        headers:
          type: object
          properties:
            xi-api-key:
              type: string
    publish:
      operationId: v-1-text-to-speech-voice-id-stream-input-publish
      summary: subscribe
      description: Receive messages from the WebSocket
      message:
        name: subscribe
        title: subscribe
        description: Receive messages from the WebSocket
        payload:
          $ref: '#/components/schemas/V1TextToSpeechVoiceIdStreamInputSubscribe'
    subscribe:
      operationId: v-1-text-to-speech-voice-id-stream-input-subscribe
      summary: publish
      description: Send messages to the WebSocket
      message:
        name: publish
        title: publish
        description: Send messages to the WebSocket
        payload:
          $ref: '#/components/schemas/V1TextToSpeechVoiceIdStreamInputPublish'
servers:
  Production:
    url: wss://api.elevenlabs.io/
    protocol: wss
    x-default: true
  Production US:
    url: wss://api.us.elevenlabs.io/
    protocol: wss
  Production EU:
    url: wss://api.eu.residency.elevenlabs.io/
    protocol: wss
  Production India:
    url: wss://api.in.residency.elevenlabs.io/
    protocol: wss
components:
  schemas:
    output_format:
      type: string
      enum:
        - value: mp3_22050_32
        - value: mp3_44100_32
        - value: mp3_44100_64
        - value: mp3_44100_96
        - value: mp3_44100_128
        - value: mp3_44100_192
        - value: pcm_8000
        - value: pcm_16000
        - value: pcm_22050
        - value: pcm_24000
        - value: pcm_44100
        - value: ulaw_8000
        - value: alaw_8000
        - value: opus_48000_32
        - value: opus_48000_64
        - value: opus_48000_96
        - value: opus_48000_128
        - value: opus_48000_192
    apply_text_normalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
    NormalizedAlignment:
      type: object
      properties:
        charStartTimesMs:
          type: array
          items:
            type: integer
        charDurationsMs:
          type: array
          items:
            type: integer
        chars:
          type: array
          items:
            type: string
    Alignment:
      type: object
      properties:
        charStartTimesMs:
          type: array
          items:
            type: integer
        charDurationsMs:
          type: array
          items:
            type: integer
        chars:
          type: array
          items:
            type: string
    AudioOutput:
      type: object
      properties:
        audio:
          type: string
        normalizedAlignment:
          $ref: '#/components/schemas/NormalizedAlignment'
        alignment:
          $ref: '#/components/schemas/Alignment'
      required:
        - audio
    FinalOutput:
      type: object
      properties:
        isFinal:
          type: string
          enum:
            - type: booleanLiteral
              value: true
    V1TextToSpeechVoiceIdStreamInputSubscribe:
      oneOf:
        - $ref: '#/components/schemas/AudioOutput'
        - $ref: '#/components/schemas/FinalOutput'
    RealtimeVoiceSettings:
      type: object
      properties:
        stability:
          type: number
          format: double
        similarity_boost:
          type: number
          format: double
        style:
          type: number
          format: double
        use_speaker_boost:
          type: boolean
        speed:
          type: number
          format: double
    GenerationConfig:
      type: object
      properties:
        chunk_length_schedule:
          type: array
          items:
            type: number
            format: double
    PronunciationDictionaryLocator:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
        version_id:
          type: string
      required:
        - pronunciation_dictionary_id
        - version_id
    InitializeConnection:
      type: object
      properties:
        text:
          type: string
          enum:
            - type: stringLiteral
              value: ' '
        voice_settings:
          $ref: '#/components/schemas/RealtimeVoiceSettings'
        generation_config:
          $ref: '#/components/schemas/GenerationConfig'
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: '#/components/schemas/PronunciationDictionaryLocator'
        xi-api-key:
          type: string
        authorization:
          type: string
      required:
        - text
    SendText:
      type: object
      properties:
        text:
          type: string
        try_trigger_generation:
          type: boolean
        voice_settings:
          $ref: '#/components/schemas/RealtimeVoiceSettings'
        generator_config:
          $ref: '#/components/schemas/GenerationConfig'
        flush:
          type: boolean
      required:
        - text
    CloseConnection:
      type: object
      properties:
        text:
          type: string
          enum:
            - type: stringLiteral
              value: ''
      required:
        - text
    V1TextToSpeechVoiceIdStreamInputPublish:
      oneOf:
        - $ref: '#/components/schemas/InitializeConnection'
        - $ref: '#/components/schemas/SendText'
        - $ref: '#/components/schemas/CloseConnection'

```


# Multi-Context WebSocket

GET /v1/text-to-speech/{voice_id}/multi-stream-input

The Multi-Context Text-to-Speech WebSockets API allows for generating audio from text input
while managing multiple independent audio generation streams (contexts) over a single WebSocket connection.
This is useful for scenarios requiring concurrent or interleaved audio generations, such as dynamic
conversational AI applications.

Each context, identified by a context id, maintains its own state. You can send text to specific
contexts, flush them, or close them independently. A `close_socket` message can be used to terminate
the entire connection gracefully.

For more information on best practices for how to use this API, please see the [multi context websocket guide](/docs/cookbooks/multi-context-web-socket).


Reference: https://elevenlabs.io/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-multi-stream-input


## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: V 1 Text To Speech Voice Id Multi Stream Input
  version: >-
    subpackage_v1TextToSpeechVoiceIdMultiStreamInput.v1TextToSpeechVoiceIdMultiStreamInput
  description: >
    The Multi-Context Text-to-Speech WebSockets API allows for generating audio
    from text input

    while managing multiple independent audio generation streams (contexts) over
    a single WebSocket connection.

    This is useful for scenarios requiring concurrent or interleaved audio
    generations, such as dynamic

    conversational AI applications.


    Each context, identified by a context id, maintains its own state. You can
    send text to specific

    contexts, flush them, or close them independently. A `close_socket` message
    can be used to terminate

    the entire connection gracefully.


    For more information on best practices for how to use this API, please see
    the [multi context websocket
    guide](/docs/cookbooks/multi-context-web-socket).
channels:
  /v1/text-to-speech/{voice_id}/multi-stream-input:
    description: >
      The Multi-Context Text-to-Speech WebSockets API allows for generating
      audio from text input

      while managing multiple independent audio generation streams (contexts)
      over a single WebSocket connection.

      This is useful for scenarios requiring concurrent or interleaved audio
      generations, such as dynamic

      conversational AI applications.


      Each context, identified by a context id, maintains its own state. You can
      send text to specific

      contexts, flush them, or close them independently. A `close_socket`
      message can be used to terminate

      the entire connection gracefully.


      For more information on best practices for how to use this API, please see
      the [multi context websocket
      guide](/docs/cookbooks/multi-context-web-socket).
    parameters:
      voice_id:
        description: The unique identifier for the voice to use in the TTS process.
        schema:
          type: string
    bindings:
      ws:
        query:
          type: object
          properties:
            authorization:
              type: string
            model_id:
              type: string
            language_code:
              type: string
            enable_logging:
              type: boolean
            enable_ssml_parsing:
              type: boolean
            output_format:
              $ref: '#/components/schemas/output_format'
            inactivity_timeout:
              type: integer
            sync_alignment:
              type: boolean
            auto_mode:
              type: boolean
            apply_text_normalization:
              $ref: '#/components/schemas/apply_text_normalization'
            seed:
              type: integer
        headers:
          type: object
          properties:
            xi-api-key:
              type: string
    publish:
      operationId: v-1-text-to-speech-voice-id-multi-stream-input-publish
      summary: subscribe
      description: Receive messages from the multi-context WebSocket.
      message:
        name: subscribe
        title: subscribe
        description: Receive messages from the multi-context WebSocket.
        payload:
          $ref: '#/components/schemas/V1TextToSpeechVoiceIdMultiStreamInputSubscribe'
    subscribe:
      operationId: v-1-text-to-speech-voice-id-multi-stream-input-subscribe
      summary: publish
      description: Send messages to the multi-context WebSocket.
      message:
        name: publish
        title: publish
        description: Send messages to the multi-context WebSocket.
        payload:
          $ref: '#/components/schemas/V1TextToSpeechVoiceIdMultiStreamInputPublish'
servers:
  Production:
    url: wss://api.elevenlabs.io/
    protocol: wss
    x-default: true
  Production US:
    url: wss://api.us.elevenlabs.io/
    protocol: wss
  Production EU:
    url: wss://api.eu.residency.elevenlabs.io/
    protocol: wss
  Production India:
    url: wss://api.in.residency.elevenlabs.io/
    protocol: wss
components:
  schemas:
    output_format:
      type: string
      enum:
        - value: mp3_22050_32
        - value: mp3_44100_32
        - value: mp3_44100_64
        - value: mp3_44100_96
        - value: mp3_44100_128
        - value: mp3_44100_192
        - value: pcm_8000
        - value: pcm_16000
        - value: pcm_22050
        - value: pcm_24000
        - value: pcm_44100
        - value: ulaw_8000
        - value: alaw_8000
        - value: opus_48000_32
        - value: opus_48000_64
        - value: opus_48000_96
        - value: opus_48000_128
        - value: opus_48000_192
    apply_text_normalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
    NormalizedAlignment:
      type: object
      properties:
        charStartTimesMs:
          type: array
          items:
            type: integer
        charDurationsMs:
          type: array
          items:
            type: integer
        chars:
          type: array
          items:
            type: string
    Alignment:
      type: object
      properties:
        charStartTimesMs:
          type: array
          items:
            type: integer
        charDurationsMs:
          type: array
          items:
            type: integer
        chars:
          type: array
          items:
            type: string
    AudioOutputMulti:
      type: object
      properties:
        audio:
          type: string
        normalizedAlignment:
          oneOf:
            - $ref: '#/components/schemas/NormalizedAlignment'
            - type: 'null'
        alignment:
          oneOf:
            - $ref: '#/components/schemas/Alignment'
            - type: 'null'
        contextId:
          type: string
      required:
        - audio
    FinalOutputMulti:
      type: object
      properties:
        isFinal:
          type: string
          enum:
            - type: booleanLiteral
              value: true
        contextId:
          type: string
      required:
        - isFinal
    V1TextToSpeechVoiceIdMultiStreamInputSubscribe:
      oneOf:
        - $ref: '#/components/schemas/AudioOutputMulti'
        - $ref: '#/components/schemas/FinalOutputMulti'
    RealtimeVoiceSettings:
      type: object
      properties:
        stability:
          type: number
          format: double
        similarity_boost:
          type: number
          format: double
        style:
          type: number
          format: double
        use_speaker_boost:
          type: boolean
        speed:
          type: number
          format: double
    GenerationConfig:
      type: object
      properties:
        chunk_length_schedule:
          type: array
          items:
            type: number
            format: double
    PronunciationDictionaryLocator:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
        version_id:
          type: string
      required:
        - pronunciation_dictionary_id
        - version_id
    InitializeConnectionMulti:
      type: object
      properties:
        text:
          type: string
          enum:
            - type: stringLiteral
              value: ' '
        voice_settings:
          $ref: '#/components/schemas/RealtimeVoiceSettings'
        generation_config:
          $ref: '#/components/schemas/GenerationConfig'
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: '#/components/schemas/PronunciationDictionaryLocator'
        xi_api_key:
          type: string
        authorization:
          type: string
        context_id:
          type: string
      required:
        - text
    InitialiseContext:
      type: object
      properties:
        text:
          type: string
        voice_settings:
          $ref: '#/components/schemas/RealtimeVoiceSettings'
        generation_config:
          $ref: '#/components/schemas/GenerationConfig'
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: '#/components/schemas/PronunciationDictionaryLocator'
        xi_api_key:
          type: string
        authorization:
          type: string
        context_id:
          type: string
      required:
        - text
    SendTextMulti:
      type: object
      properties:
        text:
          type: string
        context_id:
          type: string
        flush:
          type: boolean
      required:
        - text
    FlushContextClient:
      type: object
      properties:
        context_id:
          type: string
        text:
          type: string
        flush:
          type: boolean
      required:
        - context_id
        - flush
    CloseContextClient:
      type: object
      properties:
        context_id:
          type: string
        close_context:
          type: boolean
      required:
        - context_id
        - close_context
    CloseSocketClient:
      type: object
      properties:
        close_socket:
          type: boolean
    KeepContextAlive:
      type: object
      properties:
        text:
          type: string
          enum:
            - type: stringLiteral
              value: ''
        context_id:
          type: string
      required:
        - text
        - context_id
    V1TextToSpeechVoiceIdMultiStreamInputPublish:
      oneOf:
        - $ref: '#/components/schemas/InitializeConnectionMulti'
        - $ref: '#/components/schemas/InitialiseContext'
        - $ref: '#/components/schemas/SendTextMulti'
        - $ref: '#/components/schemas/FlushContextClient'
        - $ref: '#/components/schemas/CloseContextClient'
        - $ref: '#/components/schemas/CloseSocketClient'
        - $ref: '#/components/schemas/KeepContextAlive'

```


# Create speech

POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}
Content-Type: application/json

Converts text into speech using a voice of your choice and returns audio.

Reference: https://elevenlabs.io/docs/api-reference/text-to-speech/convert


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create speech
  version: endpoint_textToSpeech.convert
paths:
  /v1/text-to-speech/{voice_id}:
    post:
      operationId: convert
      summary: Create speech
      description: >-
        Converts text into speech using a voice of your choice and returns
        audio.
      tags:
        - - subpackage_textToSpeech
      parameters:
        - name: voice_id
          in: path
          description: >-
            ID of the voice to be used. Use the [Get
            voices](/docs/api-reference/voices/search) endpoint list all the
            available voices.
          required: true
          schema:
            type: string
        - name: enable_logging
          in: query
          description: >-
            When enable_logging is set to false zero retention mode will be used
            for the request. This will mean history features are unavailable for
            this request, including request stitching. Zero retention mode may
            only be used by enterprise customers.
          required: false
          schema:
            type: boolean
        - name: optimize_streaming_latency
          in: query
          description: >
            You can turn on latency optimizations at some cost of quality. The
            best possible final latency varies by model. Possible values:

            0 - default mode (no latency optimizations)

            1 - normal latency optimizations (about 50% of possible latency
            improvement of option 3)

            2 - strong latency optimizations (about 75% of possible latency
            improvement of option 3)

            3 - max latency optimizations

            4 - max latency optimizations, but also with text normalizer turned
            off for even more latency savings (best latency, but can
            mispronounce eg numbers and dates).


            Defaults to None.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: output_format
          in: query
          description: >-
            Output format of the generated audio. Formatted as
            codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at
            32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate
            requires you to be subscribed to Creator tier or above. PCM with
            44.1kHz sample rate requires you to be subscribed to Pro tier or
            above. Note that the μ-law format (sometimes written mu-law, often
            approximated as u-law) is commonly used for Twilio audio inputs.
          required: false
          schema:
            $ref: >-
              #/components/schemas/V1TextToSpeechVoiceIdPostParametersOutputFormat
        - name: xi-api-key
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: The generated audio file
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Body_text_to_speech_full'
components:
  schemas:
    V1TextToSpeechVoiceIdPostParametersOutputFormat:
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
    PronunciationDictionaryVersionLocatorRequestModel:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
        version_id:
          type:
            - string
            - 'null'
      required:
        - pronunciation_dictionary_id
    BodyTextToSpeechFullApplyTextNormalization:
      type: string
      enum:
        - value: auto
        - value: 'on'
        - value: 'off'
    Body_text_to_speech_full:
      type: object
      properties:
        text:
          type: string
        model_id:
          type: string
        language_code:
          type:
            - string
            - 'null'
        voice_settings:
          oneOf:
            - $ref: '#/components/schemas/VoiceSettingsResponseModel'
            - type: 'null'
        pronunciation_dictionary_locators:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/PronunciationDictionaryVersionLocatorRequestModel
        seed:
          type:
            - integer
            - 'null'
        previous_text:
          type:
            - string
            - 'null'
        next_text:
          type:
            - string
            - 'null'
        previous_request_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        next_request_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        use_pvc_as_ivc:
          type: boolean
        apply_text_normalization:
          $ref: '#/components/schemas/BodyTextToSpeechFullApplyTextNormalization'
        apply_language_text_normalization:
          type: boolean
      required:
        - text

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.textToSpeech.convert("JBFqnCBsd6RMkjVDRZzb", {
        outputFormat: "mp3_44100_128",
        text: "The first move is what sets everything in motion.",
        modelId: "eleven_multilingual_v2",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.text_to_speech.convert(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    output_format="mp3_44100_128",
    text="The first move is what sets everything in motion.",
    model_id="eleven_multilingual_v2"
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

	url := "https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128"

	payload := strings.NewReader("{\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"model_id\": \"eleven_multilingual_v2\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"model_id\": \"eleven_multilingual_v2\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"model_id\": \"eleven_multilingual_v2\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128', [
  'body' => '{
  "text": "The first move is what sets everything in motion.",
  "model_id": "eleven_multilingual_v2"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"model_id\": \"eleven_multilingual_v2\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "text": "The first move is what sets everything in motion.",
  "model_id": "eleven_multilingual_v2"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128")! as URL,
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
**Navigation:** [← Previous](./30-create-mcp-server.md) | [Index](./index.md) | [Next →](./32-create-speech-with-timing.md)
