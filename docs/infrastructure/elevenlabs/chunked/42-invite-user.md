**Navigation:** [← Previous](./41-delete-voice-sample.md) | [Index](./index.md) | [Next →](./43-get-agent.md)

# Invite user

POST https://api.elevenlabs.io/v1/workspace/invites/add
Content-Type: application/json

Sends an email invitation to join your workspace to the provided email. If the user doesn't have an account they will be prompted to create one. If the user accepts this invite they will be added as a user to your workspace and your subscription using one of your seats. This endpoint may only be called by workspace administrators. If the user is already in the workspace a 400 error will be returned.

Reference: https://elevenlabs.io/docs/api-reference/workspace/invites/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Invite user
  version: endpoint_workspace/invites.create
paths:
  /v1/workspace/invites/add:
    post:
      operationId: create
      summary: Invite user
      description: >-
        Sends an email invitation to join your workspace to the provided email.
        If the user doesn't have an account they will be prompted to create one.
        If the user accepts this invite they will be added as a user to your
        workspace and your subscription using one of your seats. This endpoint
        may only be called by workspace administrators. If the user is already
        in the workspace a 400 error will be returned.
      tags:
        - - subpackage_workspace
          - subpackage_workspace/invites
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
                $ref: '#/components/schemas/AddWorkspaceInviteResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Invite_user_v1_workspace_invites_add_post
components:
  schemas:
    BodyInviteUserV1WorkspaceInvitesAddPostWorkspacePermission:
      type: string
      enum:
        - value: external
        - value: admin
        - value: workspace_admin
        - value: workspace_member
        - value: support_l1
        - value: support_l2
        - value: moderator
        - value: sales
        - value: voice_mixer
        - value: voice_admin
        - value: convai_admin
        - value: enterprise_viewer
        - value: quality_check_admin
        - value: workspace_migration_admin
        - value: human_reviewer
        - value: productions_admin
        - value: support
        - value: internal
    Body_Invite_user_v1_workspace_invites_add_post:
      type: object
      properties:
        email:
          type: string
        group_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        workspace_permission:
          oneOf:
            - $ref: >-
                #/components/schemas/BodyInviteUserV1WorkspaceInvitesAddPostWorkspacePermission
            - type: 'null'
      required:
        - email
    AddWorkspaceInviteResponseModel:
      type: object
      properties:
        status:
          type: string
      required:
        - status

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.workspace.invites.create({
        email: "john.doe@testmail.com",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.workspace.invites.create(
    email="john.doe@testmail.com"
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

	url := "https://api.elevenlabs.io/v1/workspace/invites/add"

	payload := strings.NewReader("{\n  \"email\": \"john.doe@testmail.com\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/workspace/invites/add")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"john.doe@testmail.com\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/invites/add")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"john.doe@testmail.com\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/invites/add', [
  'body' => '{
  "email": "john.doe@testmail.com"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/workspace/invites/add");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"email\": \"john.doe@testmail.com\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["email": "john.doe@testmail.com"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/invites/add")! as URL,
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


# Invite Multiple Users

POST https://api.elevenlabs.io/v1/workspace/invites/add-bulk
Content-Type: application/json

Sends email invitations to join your workspace to the provided emails. Requires all email addresses to be part of a verified domain. If the users don't have an account they will be prompted to create one. If the users accept these invites they will be added as users to your workspace and your subscription using one of your seats. This endpoint may only be called by workspace administrators.

Reference: https://elevenlabs.io/docs/api-reference/workspace/invites/create-batch


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Invite Multiple Users
  version: endpoint_workspace/invites.create_batch
paths:
  /v1/workspace/invites/add-bulk:
    post:
      operationId: create-batch
      summary: Invite Multiple Users
      description: >-
        Sends email invitations to join your workspace to the provided emails.
        Requires all email addresses to be part of a verified domain. If the
        users don't have an account they will be prompted to create one. If the
        users accept these invites they will be added as users to your workspace
        and your subscription using one of your seats. This endpoint may only be
        called by workspace administrators.
      tags:
        - - subpackage_workspace
          - subpackage_workspace/invites
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
                $ref: '#/components/schemas/AddWorkspaceInviteResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Invite_multiple_users_v1_workspace_invites_add_bulk_post
components:
  schemas:
    Body_Invite_multiple_users_v1_workspace_invites_add_bulk_post:
      type: object
      properties:
        emails:
          type: array
          items:
            type: string
        group_ids:
          type:
            - array
            - 'null'
          items:
            type: string
      required:
        - emails
    AddWorkspaceInviteResponseModel:
      type: object
      properties:
        status:
          type: string
      required:
        - status

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.workspace.invites.createBatch({
        emails: [
            "string",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.workspace.invites.create_batch(
    emails=[
        "string"
    ]
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

	url := "https://api.elevenlabs.io/v1/workspace/invites/add-bulk"

	payload := strings.NewReader("{\n  \"emails\": [\n    \"string\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/workspace/invites/add-bulk")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"emails\": [\n    \"string\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/invites/add-bulk")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"emails\": [\n    \"string\"\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/invites/add-bulk', [
  'body' => '{
  "emails": [
    "string"
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/workspace/invites/add-bulk");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"emails\": [\n    \"string\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["emails": ["string"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/invites/add-bulk")! as URL,
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


# Delete invite

DELETE https://api.elevenlabs.io/v1/workspace/invites
Content-Type: application/json

Invalidates an existing email invitation. The invitation will still show up in the inbox it has been delivered to, but activating it to join the workspace won't work. This endpoint may only be called by workspace administrators.

Reference: https://elevenlabs.io/docs/api-reference/workspace/invites/delete


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete invite
  version: endpoint_workspace/invites.delete
paths:
  /v1/workspace/invites:
    delete:
      operationId: delete
      summary: Delete invite
      description: >-
        Invalidates an existing email invitation. The invitation will still show
        up in the inbox it has been delivered to, but activating it to join the
        workspace won't work. This endpoint may only be called by workspace
        administrators.
      tags:
        - - subpackage_workspace
          - subpackage_workspace/invites
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
                $ref: '#/components/schemas/DeleteWorkspaceInviteResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Delete_existing_invitation_v1_workspace_invites_delete
components:
  schemas:
    Body_Delete_existing_invitation_v1_workspace_invites_delete:
      type: object
      properties:
        email:
          type: string
      required:
        - email
    DeleteWorkspaceInviteResponseModel:
      type: object
      properties:
        status:
          type: string
      required:
        - status

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.workspace.invites.delete({
        email: "john.doe@testmail.com",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.workspace.invites.delete(
    email="john.doe@testmail.com"
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

	url := "https://api.elevenlabs.io/v1/workspace/invites"

	payload := strings.NewReader("{\n  \"email\": \"john.doe@testmail.com\"\n}")

	req, _ := http.NewRequest("DELETE", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/workspace/invites")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"john.doe@testmail.com\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/workspace/invites")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"john.doe@testmail.com\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/workspace/invites', [
  'body' => '{
  "email": "john.doe@testmail.com"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/workspace/invites");
var request = new RestRequest(Method.DELETE);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"email\": \"john.doe@testmail.com\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["email": "john.doe@testmail.com"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/invites")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
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


# Update member

POST https://api.elevenlabs.io/v1/workspace/members
Content-Type: application/json

Updates attributes of a workspace member. Apart from the email identifier, all parameters will remain unchanged unless specified. This endpoint may only be called by workspace administrators.

Reference: https://elevenlabs.io/docs/api-reference/workspace/members/update


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update member
  version: endpoint_workspace/members.update
paths:
  /v1/workspace/members:
    post:
      operationId: update
      summary: Update member
      description: >-
        Updates attributes of a workspace member. Apart from the email
        identifier, all parameters will remain unchanged unless specified. This
        endpoint may only be called by workspace administrators.
      tags:
        - - subpackage_workspace
          - subpackage_workspace/members
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
                $ref: '#/components/schemas/UpdateWorkspaceMemberResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Update_member_v1_workspace_members_post
components:
  schemas:
    BodyUpdateMemberV1WorkspaceMembersPostWorkspaceRole:
      type: string
      enum:
        - value: workspace_admin
        - value: workspace_member
    Body_Update_member_v1_workspace_members_post:
      type: object
      properties:
        email:
          type: string
        is_locked:
          type:
            - boolean
            - 'null'
        workspace_role:
          oneOf:
            - $ref: >-
                #/components/schemas/BodyUpdateMemberV1WorkspaceMembersPostWorkspaceRole
            - type: 'null'
      required:
        - email
    UpdateWorkspaceMemberResponseModel:
      type: object
      properties:
        status:
          type: string
      required:
        - status

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.workspace.members.update({
        email: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.workspace.members.update(
    email="string"
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

	url := "https://api.elevenlabs.io/v1/workspace/members"

	payload := strings.NewReader("{\n  \"email\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/workspace/members")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/members")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"string\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/members', [
  'body' => '{
  "email": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/workspace/members");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"email\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["email": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/members")! as URL,
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


# Get Resource

GET https://api.elevenlabs.io/v1/workspace/resources/{resource_id}

Gets the metadata of a resource by ID.

Reference: https://elevenlabs.io/docs/api-reference/workspace/resources/get


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Resource
  version: endpoint_workspace/resources.get
paths:
  /v1/workspace/resources/{resource_id}:
    get:
      operationId: get
      summary: Get Resource
      description: Gets the metadata of a resource by ID.
      tags:
        - - subpackage_workspace
          - subpackage_workspace/resources
      parameters:
        - name: resource_id
          in: path
          description: The ID of the target resource.
          required: true
          schema:
            type: string
        - name: resource_type
          in: query
          description: Resource type of the target resource.
          required: true
          schema:
            $ref: '#/components/schemas/WorkspaceResourceType'
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
                $ref: '#/components/schemas/ResourceMetadataResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    WorkspaceResourceType:
      type: string
      enum:
        - value: voice
        - value: voice_collection
        - value: pronunciation_dictionary
        - value: dubbing
        - value: project
        - value: convai_agents
        - value: convai_knowledge_base_documents
        - value: convai_tools
        - value: convai_settings
        - value: convai_secrets
        - value: workspace_auth_connections
        - value: convai_phone_numbers
        - value: convai_mcp_servers
        - value: convai_api_integration_connections
        - value: convai_batch_calls
        - value: convai_agent_response_tests
        - value: convai_test_suite_invocations
        - value: convai_crawl_jobs
        - value: convai_crawl_tasks
        - value: convai_whatsapp_accounts
        - value: convai_agent_versions
        - value: convai_agent_branches
        - value: dashboard
        - value: dashboard_configuration
    ResourceMetadataResponseModelAnonymousAccessLevelOverride:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    ShareOptionResponseModelType:
      type: string
      enum:
        - value: user
        - value: group
        - value: key
    ShareOptionResponseModel:
      type: object
      properties:
        name:
          type: string
        id:
          type: string
        type:
          $ref: '#/components/schemas/ShareOptionResponseModelType'
      required:
        - name
        - id
        - type
    ResourceMetadataResponseModel:
      type: object
      properties:
        resource_id:
          type: string
        resource_type:
          $ref: '#/components/schemas/WorkspaceResourceType'
        creator_user_id:
          type:
            - string
            - 'null'
        anonymous_access_level_override:
          oneOf:
            - $ref: >-
                #/components/schemas/ResourceMetadataResponseModelAnonymousAccessLevelOverride
            - type: 'null'
        role_to_group_ids:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
        share_options:
          type: array
          items:
            $ref: '#/components/schemas/ShareOptionResponseModel'
      required:
        - resource_id
        - resource_type
        - creator_user_id
        - anonymous_access_level_override
        - role_to_group_ids
        - share_options

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.workspace.resources.get("resource_id", {
        resourceType: "voice",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.workspace.resources.get(
    resource_id="resource_id",
    resource_type="voice"
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

	url := "https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice"

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

url = URI("https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice")! as URL,
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


# Share Workspace Resource

POST https://api.elevenlabs.io/v1/workspace/resources/{resource_id}/share
Content-Type: application/json

Grants a role on a workspace resource to a user or a group. It overrides any existing role this user/service account/group/workspace api key has on the resource. To target a user or service account, pass only the user email. The user must be in your workspace. To target a group, pass only the group id. To target a workspace api key, pass the api key id. The resource will be shared with the service account associated with the api key. You must have admin access to the resource to share it.

Reference: https://elevenlabs.io/docs/api-reference/workspace/resources/share


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Share Workspace Resource
  version: endpoint_workspace/resources.share
paths:
  /v1/workspace/resources/{resource_id}/share:
    post:
      operationId: share
      summary: Share Workspace Resource
      description: >-
        Grants a role on a workspace resource to a user or a group. It overrides
        any existing role this user/service account/group/workspace api key has
        on the resource. To target a user or service account, pass only the user
        email. The user must be in your workspace. To target a group, pass only
        the group id. To target a workspace api key, pass the api key id. The
        resource will be shared with the service account associated with the api
        key. You must have admin access to the resource to share it.
      tags:
        - - subpackage_workspace
          - subpackage_workspace/resources
      parameters:
        - name: resource_id
          in: path
          description: The ID of the target resource.
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
                description: Any type
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Share_workspace_resource_v1_workspace_resources__resource_id__share_post
components:
  schemas:
    BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePostRole:
      type: string
      enum:
        - value: admin
        - value: editor
        - value: commenter
        - value: viewer
    WorkspaceResourceType:
      type: string
      enum:
        - value: voice
        - value: voice_collection
        - value: pronunciation_dictionary
        - value: dubbing
        - value: project
        - value: convai_agents
        - value: convai_knowledge_base_documents
        - value: convai_tools
        - value: convai_settings
        - value: convai_secrets
        - value: workspace_auth_connections
        - value: convai_phone_numbers
        - value: convai_mcp_servers
        - value: convai_api_integration_connections
        - value: convai_batch_calls
        - value: convai_agent_response_tests
        - value: convai_test_suite_invocations
        - value: convai_crawl_jobs
        - value: convai_crawl_tasks
        - value: convai_whatsapp_accounts
        - value: convai_agent_versions
        - value: convai_agent_branches
        - value: dashboard
        - value: dashboard_configuration
    Body_Share_workspace_resource_v1_workspace_resources__resource_id__share_post:
      type: object
      properties:
        role:
          $ref: >-
            #/components/schemas/BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePostRole
        resource_type:
          $ref: '#/components/schemas/WorkspaceResourceType'
        user_email:
          type:
            - string
            - 'null'
        group_id:
          type:
            - string
            - 'null'
        workspace_api_key_id:
          type:
            - string
            - 'null'
      required:
        - role
        - resource_type

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.workspace.resources.share("resource_id", {
        role: "admin",
        resourceType: "voice",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.workspace.resources.share(
    resource_id="resource_id",
    role="admin",
    resource_type="voice"
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

	url := "https://api.elevenlabs.io/v1/workspace/resources/resource_id/share"

	payload := strings.NewReader("{\n  \"role\": \"admin\",\n  \"resource_type\": \"voice\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/workspace/resources/resource_id/share")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"role\": \"admin\",\n  \"resource_type\": \"voice\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/resources/resource_id/share")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"role\": \"admin\",\n  \"resource_type\": \"voice\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/resources/resource_id/share', [
  'body' => '{
  "role": "admin",
  "resource_type": "voice"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/workspace/resources/resource_id/share");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"role\": \"admin\",\n  \"resource_type\": \"voice\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "role": "admin",
  "resource_type": "voice"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/resources/resource_id/share")! as URL,
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


# Unshare Workspace Resource

POST https://api.elevenlabs.io/v1/workspace/resources/{resource_id}/unshare
Content-Type: application/json

Removes any existing role on a workspace resource from a user, service account, group or workspace api key. To target a user or service account, pass only the user email. The user must be in your workspace. To target a group, pass only the group id. To target a workspace api key, pass the api key id. The resource will be unshared from the service account associated with the api key. You must have admin access to the resource to unshare it. You cannot remove permissions from the user who created the resource.

Reference: https://elevenlabs.io/docs/api-reference/workspace/resources/unshare


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Unshare Workspace Resource
  version: endpoint_workspace/resources.unshare
paths:
  /v1/workspace/resources/{resource_id}/unshare:
    post:
      operationId: unshare
      summary: Unshare Workspace Resource
      description: >-
        Removes any existing role on a workspace resource from a user, service
        account, group or workspace api key. To target a user or service
        account, pass only the user email. The user must be in your workspace.
        To target a group, pass only the group id. To target a workspace api
        key, pass the api key id. The resource will be unshared from the service
        account associated with the api key. You must have admin access to the
        resource to unshare it. You cannot remove permissions from the user who
        created the resource.
      tags:
        - - subpackage_workspace
          - subpackage_workspace/resources
      parameters:
        - name: resource_id
          in: path
          description: The ID of the target resource.
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
                description: Any type
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Unshare_workspace_resource_v1_workspace_resources__resource_id__unshare_post
components:
  schemas:
    WorkspaceResourceType:
      type: string
      enum:
        - value: voice
        - value: voice_collection
        - value: pronunciation_dictionary
        - value: dubbing
        - value: project
        - value: convai_agents
        - value: convai_knowledge_base_documents
        - value: convai_tools
        - value: convai_settings
        - value: convai_secrets
        - value: workspace_auth_connections
        - value: convai_phone_numbers
        - value: convai_mcp_servers
        - value: convai_api_integration_connections
        - value: convai_batch_calls
        - value: convai_agent_response_tests
        - value: convai_test_suite_invocations
        - value: convai_crawl_jobs
        - value: convai_crawl_tasks
        - value: convai_whatsapp_accounts
        - value: convai_agent_versions
        - value: convai_agent_branches
        - value: dashboard
        - value: dashboard_configuration
    Body_Unshare_workspace_resource_v1_workspace_resources__resource_id__unshare_post:
      type: object
      properties:
        resource_type:
          $ref: '#/components/schemas/WorkspaceResourceType'
        user_email:
          type:
            - string
            - 'null'
        group_id:
          type:
            - string
            - 'null'
        workspace_api_key_id:
          type:
            - string
            - 'null'
      required:
        - resource_type

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.workspace.resources.unshare("resource_id", {
        resourceType: "voice",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.workspace.resources.unshare(
    resource_id="resource_id",
    resource_type="voice"
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

	url := "https://api.elevenlabs.io/v1/workspace/resources/resource_id/unshare"

	payload := strings.NewReader("{\n  \"resource_type\": \"voice\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/workspace/resources/resource_id/unshare")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"resource_type\": \"voice\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/resources/resource_id/unshare")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"resource_type\": \"voice\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/resources/resource_id/unshare', [
  'body' => '{
  "resource_type": "voice"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/workspace/resources/resource_id/unshare");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"resource_type\": \"voice\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["resource_type": "voice"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/resources/resource_id/unshare")! as URL,
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


# List Workspace Webhooks

GET https://api.elevenlabs.io/v1/workspace/webhooks

List all webhooks for a workspace

Reference: https://elevenlabs.io/docs/api-reference/webhooks/list


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List Workspace Webhooks
  version: endpoint_webhooks.list
paths:
  /v1/workspace/webhooks:
    get:
      operationId: list
      summary: List Workspace Webhooks
      description: List all webhooks for a workspace
      tags:
        - - subpackage_webhooks
      parameters:
        - name: include_usages
          in: query
          description: >-
            Whether to include active usages of the webhook, only usable by
            admins
          required: false
          schema:
            type: boolean
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
                $ref: '#/components/schemas/WorkspaceWebhookListResponseModel'
        '422':
          description: Validation Error
          content: {}
components:
  schemas:
    WebhookAuthMethodType:
      type: string
      enum:
        - value: hmac
        - value: oauth2
        - value: mtls
    WebhookUsageType:
      type: string
      enum:
        - value: ConvAI Agent Settings
        - value: ConvAI Settings
        - value: Voice Library Removal Notices
        - value: Speech to Text
    WorkspaceWebhookUsageResponseModel:
      type: object
      properties:
        usage_type:
          $ref: '#/components/schemas/WebhookUsageType'
      required:
        - usage_type
    WorkspaceWebhookResponseModel:
      type: object
      properties:
        name:
          type: string
        webhook_id:
          type: string
        webhook_url:
          type: string
        is_disabled:
          type: boolean
        is_auto_disabled:
          type: boolean
        created_at_unix:
          type: integer
        auth_type:
          $ref: '#/components/schemas/WebhookAuthMethodType'
        usage:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/WorkspaceWebhookUsageResponseModel'
        most_recent_failure_error_code:
          type:
            - integer
            - 'null'
        most_recent_failure_timestamp:
          type:
            - integer
            - 'null'
      required:
        - name
        - webhook_id
        - webhook_url
        - is_disabled
        - is_auto_disabled
        - created_at_unix
        - auth_type
    WorkspaceWebhookListResponseModel:
      type: object
      properties:
        webhooks:
          type: array
          items:
            $ref: '#/components/schemas/WorkspaceWebhookResponseModel'
      required:
        - webhooks

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.webhooks.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.webhooks.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/workspace/webhooks"

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

url = URI("https://api.elevenlabs.io/v1/workspace/webhooks")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/workspace/webhooks")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/webhooks', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/workspace/webhooks");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/webhooks")! as URL,
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


# Create agent

POST https://api.elevenlabs.io/v1/convai/agents/create
Content-Type: application/json

Create an agent from a config object

Reference: https://elevenlabs.io/docs/api-reference/agents/create


## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create agent
  version: endpoint_conversationalAi/agents.create
paths:
  /v1/convai/agents/create:
    post:
      operationId: create
      summary: Create agent
      description: Create an agent from a config object
      tags:
        - - subpackage_conversationalAi
          - subpackage_conversationalAi/agents
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
                $ref: '#/components/schemas/CreateAgentResponseModel'
        '422':
          description: Validation Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Create_Agent_v1_convai_agents_create_post
components:
  schemas:
    ASRQuality:
      type: string
      enum:
        - value: high
    ASRProvider:
      type: string
      enum:
        - value: elevenlabs
    ASRInputFormat:
      type: string
      enum:
        - value: pcm_8000
        - value: pcm_16000
        - value: pcm_22050
        - value: pcm_24000
        - value: pcm_44100
        - value: pcm_48000
        - value: ulaw_8000
    ASRConversationalConfig:
      type: object
      properties:
        quality:
          $ref: '#/components/schemas/ASRQuality'
        provider:
          $ref: '#/components/schemas/ASRProvider'
        user_input_audio_format:
          $ref: '#/components/schemas/ASRInputFormat'
        keywords:
          type: array
          items:
            type: string
    SoftTimeoutConfig:
      type: object
      properties:
        timeout_seconds:
          type: number
          format: double
        message:
          type: string
    TurnEagerness:
      type: string
      enum:
        - value: patient
        - value: normal
        - value: eager
    TurnConfig:
      type: object
      properties:
        turn_timeout:
          type: number
          format: double
        initial_wait_time:
          type:
            - number
            - 'null'
          format: double
        silence_end_call_timeout:
          type: number
          format: double
        soft_timeout_config:
          $ref: '#/components/schemas/SoftTimeoutConfig'
        turn_eagerness:
          $ref: '#/components/schemas/TurnEagerness'
    TTSConversationalModel:
      type: string
      enum:
        - value: eleven_turbo_v2
        - value: eleven_turbo_v2_5
        - value: eleven_flash_v2
        - value: eleven_flash_v2_5
        - value: eleven_multilingual_v2
        - value: eleven_expressive
    TTSModelFamily:
      type: string
      enum:
        - value: turbo
        - value: flash
        - value: multilingual
        - value: expressive
    TTSOptimizeStreamingLatency:
      type: string
      enum:
        - value: '0'
        - value: '1'
        - value: '2'
        - value: '3'
        - value: '4'
    SupportedVoice:
      type: object
      properties:
        label:
          type: string
        voice_id:
          type: string
        description:
          type:
            - string
            - 'null'
        language:
          type:
            - string
            - 'null'
        model_family:
          oneOf:
            - $ref: '#/components/schemas/TTSModelFamily'
            - type: 'null'
        optimize_streaming_latency:
          oneOf:
            - $ref: '#/components/schemas/TTSOptimizeStreamingLatency'
            - type: 'null'
        stability:
          type:
            - number
            - 'null'
          format: double
        speed:
          type:
            - number
            - 'null'
          format: double
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
      required:
        - label
        - voice_id
    TTSOutputFormat:
      type: string
      enum:
        - value: pcm_8000
        - value: pcm_16000
        - value: pcm_22050
        - value: pcm_24000
        - value: pcm_44100
        - value: pcm_48000
        - value: ulaw_8000
    PydanticPronunciationDictionaryVersionLocator:
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
        - version_id
    TTSConversationalConfig-Input:
      type: object
      properties:
        model_id:
          $ref: '#/components/schemas/TTSConversationalModel'
        voice_id:
          type: string
        supported_voices:
          type: array
          items:
            $ref: '#/components/schemas/SupportedVoice'
        agent_output_audio_format:
          $ref: '#/components/schemas/TTSOutputFormat'
        optimize_streaming_latency:
          $ref: '#/components/schemas/TTSOptimizeStreamingLatency'
        stability:
          type: number
          format: double
        speed:
          type: number
          format: double
        similarity_boost:
          type: number
          format: double
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: '#/components/schemas/PydanticPronunciationDictionaryVersionLocator'
    ClientEvent:
      type: string
      enum:
        - value: conversation_initiation_metadata
        - value: asr_initiation_metadata
        - value: ping
        - value: audio
        - value: interruption
        - value: user_transcript
        - value: tentative_user_transcript
        - value: agent_response
        - value: agent_response_correction
        - value: client_tool_call
        - value: mcp_tool_call
        - value: mcp_connection_status
        - value: agent_tool_response
        - value: vad_score
        - value: agent_chat_response_part
        - value: internal_turn_probability
        - value: internal_tentative_agent_response
    ConversationConfig:
      type: object
      properties:
        text_only:
          type: boolean
        max_duration_seconds:
          type: integer
        client_events:
          type: array
          items:
            $ref: '#/components/schemas/ClientEvent'
    SoftTimeoutConfigOverride:
      type: object
      properties:
        message:
          type:
            - string
            - 'null'
    TurnConfigOverride:
      type: object
      properties:
        soft_timeout_config:
          oneOf:
            - $ref: '#/components/schemas/SoftTimeoutConfigOverride'
            - type: 'null'
    TTSConversationalConfigOverride:
      type: object
      properties:
        voice_id:
          type:
            - string
            - 'null'
        stability:
          type:
            - number
            - 'null'
          format: double
        speed:
          type:
            - number
            - 'null'
          format: double
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
    ConversationConfigOverride:
      type: object
      properties:
        text_only:
          type:
            - boolean
            - 'null'
    LLM:
      type: string
      enum:
        - value: gpt-4o-mini
        - value: gpt-4o
        - value: gpt-4
        - value: gpt-4-turbo
        - value: gpt-4.1
        - value: gpt-4.1-mini
        - value: gpt-4.1-nano
        - value: gpt-5
        - value: gpt-5-mini
        - value: gpt-5-nano
        - value: gpt-3.5-turbo
        - value: gemini-1.5-pro
        - value: gemini-1.5-flash
        - value: gemini-2.0-flash
        - value: gemini-2.0-flash-lite
        - value: gemini-2.5-flash-lite
        - value: gemini-2.5-flash
        - value: claude-sonnet-4-5
        - value: claude-sonnet-4
        - value: claude-haiku-4-5
        - value: claude-3-7-sonnet
        - value: claude-3-5-sonnet
        - value: claude-3-5-sonnet-v1
        - value: claude-3-haiku
        - value: grok-beta
        - value: custom-llm
        - value: qwen3-4b
        - value: qwen3-30b-a3b
        - value: gpt-oss-20b
        - value: gpt-oss-120b
        - value: glm-45-air-fp8
        - value: gemini-2.5-flash-preview-09-2025
        - value: gemini-2.5-flash-lite-preview-09-2025
        - value: gemini-2.5-flash-preview-05-20
        - value: gemini-2.5-flash-preview-04-17
        - value: gemini-2.5-flash-lite-preview-06-17
        - value: gemini-2.0-flash-lite-001
        - value: gemini-2.0-flash-001
        - value: gemini-1.5-flash-002
        - value: gemini-1.5-flash-001
        - value: gemini-1.5-pro-002
        - value: gemini-1.5-pro-001
        - value: claude-sonnet-4@20250514
        - value: claude-sonnet-4-5@20250929
        - value: claude-haiku-4-5@20251001
        - value: claude-3-7-sonnet@20250219
        - value: claude-3-5-sonnet@20240620
        - value: claude-3-5-sonnet-v2@20241022
        - value: claude-3-haiku@20240307
        - value: gpt-5-2025-08-07
        - value: gpt-5-mini-2025-08-07
        - value: gpt-5-nano-2025-08-07
        - value: gpt-4.1-2025-04-14
        - value: gpt-4.1-mini-2025-04-14
        - value: gpt-4.1-nano-2025-04-14
        - value: gpt-4o-mini-2024-07-18
        - value: gpt-4o-2024-11-20
        - value: gpt-4o-2024-08-06
        - value: gpt-4o-2024-05-13
        - value: gpt-4-0613
        - value: gpt-4-0314
        - value: gpt-4-turbo-2024-04-09
        - value: gpt-3.5-turbo-0125
        - value: gpt-3.5-turbo-1106
        - value: watt-tool-8b
        - value: watt-tool-70b
    PromptAgentAPIModelOverride:
      type: object
      properties:
        prompt:
          type:
            - string
            - 'null'
        llm:
          oneOf:
            - $ref: '#/components/schemas/LLM'
            - type: 'null'
        native_mcp_server_ids:
          type:
            - array
            - 'null'
          items:
            type: string
    AgentConfigOverride-Input:
      type: object
      properties:
        first_message:
          type:
            - string
            - 'null'
        language:
          type:
            - string
            - 'null'
        prompt:
          oneOf:
            - $ref: '#/components/schemas/PromptAgentAPIModelOverride'
            - type: 'null'
    ConversationConfigClientOverride-Input:
      type: object
      properties:
        turn:
          oneOf:
            - $ref: '#/components/schemas/TurnConfigOverride'
            - type: 'null'
        tts:
          oneOf:
            - $ref: '#/components/schemas/TTSConversationalConfigOverride'
            - type: 'null'
        conversation:
          oneOf:
            - $ref: '#/components/schemas/ConversationConfigOverride'
            - type: 'null'
        agent:
          oneOf:
            - $ref: '#/components/schemas/AgentConfigOverride-Input'
            - type: 'null'
    LanguagePresetTranslation:
      type: object
      properties:
        source_hash:
          type: string
        text:
          type: string
      required:
        - source_hash
        - text
    LanguagePreset-Input:
      type: object
      properties:
        overrides:
          $ref: '#/components/schemas/ConversationConfigClientOverride-Input'
        first_message_translation:
          oneOf:
            - $ref: '#/components/schemas/LanguagePresetTranslation'
            - type: 'null'
        soft_timeout_translation:
          oneOf:
            - $ref: '#/components/schemas/LanguagePresetTranslation'
            - type: 'null'
      required:
        - overrides
    VADConfig:
      type: object
      properties: {}
    DynamicVariablesConfigDynamicVariablePlaceholders:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: integer
        - type: boolean
    DynamicVariablesConfig:
      type: object
      properties:
        dynamic_variable_placeholders:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/DynamicVariablesConfigDynamicVariablePlaceholders
    LLMReasoningEffort:
      type: string
      enum:
        - value: minimal
        - value: low
        - value: medium
        - value: high
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
    EndCallToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: end_call
    LanguageDetectionToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: language_detection
    AgentTransfer:
      type: object
      properties:
        agent_id:
          type: string
        condition:
          type: string
        delay_ms:
          type: integer
        transfer_message:
          type:
            - string
            - 'null'
        enable_transferred_agent_first_message:
          type: boolean
      required:
        - agent_id
        - condition
    TransferToAgentToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: transfer_to_agent
        transfers:
          type: array
          items:
            $ref: '#/components/schemas/AgentTransfer'
      required:
        - transfers
    PhoneNumberTransferDestination:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: phone
        phone_number:
          type: string
      required:
        - phone_number
    SIPUriTransferDestination:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: sip_uri
        sip_uri:
          type: string
      required:
        - sip_uri
    PhoneNumberDynamicVariableTransferDestination:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: phone_dynamic_variable
        phone_number:
          type: string
      required:
        - phone_number
    SIPUriDynamicVariableTransferDestination:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: sip_uri_dynamic_variable
        sip_uri:
          type: string
      required:
        - sip_uri
    PhoneNumberTransferTransferDestination:
      oneOf:
        - $ref: '#/components/schemas/PhoneNumberTransferDestination'
        - $ref: '#/components/schemas/SIPUriTransferDestination'
        - $ref: '#/components/schemas/PhoneNumberDynamicVariableTransferDestination'
        - $ref: '#/components/schemas/SIPUriDynamicVariableTransferDestination'
    TransferTypeEnum:
      type: string
      enum:
        - value: conference
        - value: sip_refer
    PhoneNumberTransfer:
      type: object
      properties:
        transfer_destination:
          oneOf:
            - $ref: '#/components/schemas/PhoneNumberTransferTransferDestination'
            - type: 'null'
        phone_number:
          type:
            - string
            - 'null'
        condition:
          type: string
        transfer_type:
          $ref: '#/components/schemas/TransferTypeEnum'
      required:
        - condition
    TransferToNumberToolConfig-Input:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: transfer_to_number
        transfers:
          type: array
          items:
            $ref: '#/components/schemas/PhoneNumberTransfer'
        enable_client_message:
          type: boolean
      required:
        - transfers
    SkipTurnToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: skip_turn
    PlayDTMFToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: play_keypad_touch_tone
    VoicemailDetectionToolConfig:
      type: object
      properties:
        system_tool_type:
          type: string
          enum:
            - type: stringLiteral
              value: voicemail_detection
        voicemail_message:
          type:
            - string
            - 'null'
    SystemToolConfigInputParams:
      oneOf:
        - $ref: '#/components/schemas/EndCallToolConfig'
        - $ref: '#/components/schemas/LanguageDetectionToolConfig'
        - $ref: '#/components/schemas/TransferToAgentToolConfig'
        - $ref: '#/components/schemas/TransferToNumberToolConfig-Input'
        - $ref: '#/components/schemas/SkipTurnToolConfig'
        - $ref: '#/components/schemas/PlayDTMFToolConfig'
        - $ref: '#/components/schemas/VoicemailDetectionToolConfig'
    SystemToolConfig-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: system
        name:
          type: string
        description:
          type: string
        response_timeout_secs:
          type: integer
        disable_interruptions:
          type: boolean
        force_pre_tool_speech:
          type: boolean
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        params:
          $ref: '#/components/schemas/SystemToolConfigInputParams'
      required:
        - name
        - params
    BuiltInTools-Input:
      type: object
      properties:
        end_call:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        language_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        transfer_to_agent:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        transfer_to_number:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        skip_turn:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        play_keypad_touch_tone:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        voicemail_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
    KnowledgeBaseDocumentType:
      type: string
      enum:
        - value: file
        - value: url
        - value: text
    DocumentUsageModeEnum:
      type: string
      enum:
        - value: prompt
        - value: auto
    KnowledgeBaseLocator:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/KnowledgeBaseDocumentType'
        name:
          type: string
        id:
          type: string
        usage_mode:
          $ref: '#/components/schemas/DocumentUsageModeEnum'
      required:
        - type
        - name
        - id
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
    CustomLlmRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    CustomLLM:
      type: object
      properties:
        url:
          type: string
        model_id:
          type:
            - string
            - 'null'
        api_key:
          oneOf:
            - $ref: '#/components/schemas/ConvAISecretLocator'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/CustomLlmRequestHeaders'
        api_version:
          type:
            - string
            - 'null'
      required:
        - url
    EmbeddingModelEnum:
      type: string
      enum:
        - value: e5_mistral_7b_instruct
        - value: multilingual_e5_large_instruct
    RagConfig:
      type: object
      properties:
        enabled:
          type: boolean
        embedding_model:
          $ref: '#/components/schemas/EmbeddingModelEnum'
        max_vector_distance:
          type: number
          format: double
        max_documents_length:
          type: integer
        max_retrieved_rag_chunks_count:
          type: integer
    BackupLLMDefault:
      type: object
      properties:
        preference:
          type: string
          enum:
            - type: stringLiteral
              value: default
    BackupLLMDisabled:
      type: object
      properties:
        preference:
          type: string
          enum:
            - type: stringLiteral
              value: disabled
    BackupLLMOverride:
      type: object
      properties:
        preference:
          type: string
          enum:
            - type: stringLiteral
              value: override
        order:
          type: array
          items:
            $ref: '#/components/schemas/LLM'
      required:
        - order
    PromptAgentApiModelInputBackupLlmConfig:
      oneOf:
        - $ref: '#/components/schemas/BackupLLMDefault'
        - $ref: '#/components/schemas/BackupLLMDisabled'
        - $ref: '#/components/schemas/BackupLLMOverride'
    ToolExecutionMode:
      type: string
      enum:
        - value: immediate
        - value: post_tool_speech
        - value: async
    WebhookToolApiSchemaConfigInputMethod:
      type: string
      enum:
        - value: GET
        - value: POST
        - value: PUT
        - value: PATCH
        - value: DELETE
    LiteralJsonSchemaPropertyType:
      type: string
      enum:
        - value: boolean
        - value: string
        - value: integer
        - value: number
    LiteralJsonSchemaPropertyConstantValue:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
    LiteralJsonSchemaProperty:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/LiteralJsonSchemaPropertyType'
        description:
          type: string
        enum:
          type:
            - array
            - 'null'
          items:
            type: string
        is_system_provided:
          type: boolean
        dynamic_variable:
          type: string
        constant_value:
          $ref: '#/components/schemas/LiteralJsonSchemaPropertyConstantValue'
      required:
        - type
    QueryParamsJsonSchema:
      type: object
      properties:
        properties:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        required:
          type: array
          items:
            type: string
      required:
        - properties
    ArrayJsonSchemaPropertyInputItems:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
        - $ref: '#/components/schemas/ArrayJsonSchemaProperty-Input'
    ArrayJsonSchemaProperty-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: array
        description:
          type: string
        items:
          $ref: '#/components/schemas/ArrayJsonSchemaPropertyInputItems'
      required:
        - items
    ObjectJsonSchemaPropertyInput:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
        - $ref: '#/components/schemas/ArrayJsonSchemaProperty-Input'
    ObjectJsonSchemaProperty-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: object
        required:
          type: array
          items:
            type: string
        description:
          type: string
        properties:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ObjectJsonSchemaPropertyInput'
    WebhookToolApiSchemaConfigInputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    AuthConnectionLocator:
      type: object
      properties:
        auth_connection_id:
          type: string
      required:
        - auth_connection_id
    WebhookToolApiSchemaConfig-Input:
      type: object
      properties:
        url:
          type: string
        method:
          $ref: '#/components/schemas/WebhookToolApiSchemaConfigInputMethod'
        path_params_schema:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        query_params_schema:
          oneOf:
            - $ref: '#/components/schemas/QueryParamsJsonSchema'
            - type: 'null'
        request_body_schema:
          oneOf:
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
            - type: 'null'
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/WebhookToolApiSchemaConfigInputRequestHeaders'
        auth_connection:
          oneOf:
            - $ref: '#/components/schemas/AuthConnectionLocator'
            - type: 'null'
      required:
        - url
    WebhookToolConfig-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: webhook
        name:
          type: string
        description:
          type: string
        response_timeout_secs:
          type: integer
        disable_interruptions:
          type: boolean
        force_pre_tool_speech:
          type: boolean
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        dynamic_variables:
          $ref: '#/components/schemas/DynamicVariablesConfig'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        api_schema:
          $ref: '#/components/schemas/WebhookToolApiSchemaConfig-Input'
      required:
        - name
        - description
        - api_schema
    ClientToolConfig-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: client
        name:
          type: string
        description:
          type: string
        response_timeout_secs:
          type: integer
        disable_interruptions:
          type: boolean
        force_pre_tool_speech:
          type: boolean
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        parameters:
          oneOf:
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
            - type: 'null'
        expects_response:
          type: boolean
        dynamic_variables:
          $ref: '#/components/schemas/DynamicVariablesConfig'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
      required:
        - name
        - description
    LiteralOverrideConstantValue:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
    LiteralOverride:
      type: object
      properties:
        description:
          type:
            - string
            - 'null'
        dynamic_variable:
          type:
            - string
            - 'null'
        constant_value:
          oneOf:
            - $ref: '#/components/schemas/LiteralOverrideConstantValue'
            - type: 'null'
    QueryOverride:
      type: object
      properties:
        properties:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/LiteralOverride'
        required:
          type:
            - array
            - 'null'
          items:
            type: string
    ObjectOverrideInput:
      oneOf:
        - $ref: '#/components/schemas/LiteralOverride'
        - $ref: '#/components/schemas/ObjectOverride-Input'
    ObjectOverride-Input:
      type: object
      properties:
        description:
          type:
            - string
            - 'null'
        properties:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/ObjectOverrideInput'
        required:
          type:
            - array
            - 'null'
          items:
            type: string
    ApiIntegrationWebhookOverridesInputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
    ApiIntegrationWebhookOverrides-Input:
      type: object
      properties:
        path_params_schema:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/LiteralOverride'
        query_params_schema:
          oneOf:
            - $ref: '#/components/schemas/QueryOverride'
            - type: 'null'
        request_body_schema:
          oneOf:
            - $ref: '#/components/schemas/ObjectOverride-Input'
            - type: 'null'
        request_headers:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: >-
              #/components/schemas/ApiIntegrationWebhookOverridesInputRequestHeaders
    ApiIntegrationWebhookToolConfig-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: api_integration_webhook
        name:
          type: string
        description:
          type: string
        response_timeout_secs:
          type: integer
        disable_interruptions:
          type: boolean
        force_pre_tool_speech:
          type: boolean
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
        dynamic_variables:
          $ref: '#/components/schemas/DynamicVariablesConfig'
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
        tool_version:
          type: string
        api_integration_id:
          type: string
        api_integration_connection_id:
          type: string
        api_schema_overrides:
          oneOf:
            - $ref: '#/components/schemas/ApiIntegrationWebhookOverrides-Input'
            - type: 'null'
      required:
        - name
        - description
        - api_integration_id
        - api_integration_connection_id
    PromptAgentApiModelInputToolsItems:
      oneOf:
        - $ref: '#/components/schemas/WebhookToolConfig-Input'
        - $ref: '#/components/schemas/ClientToolConfig-Input'
        - $ref: '#/components/schemas/SystemToolConfig-Input'
        - $ref: '#/components/schemas/ApiIntegrationWebhookToolConfig-Input'
    PromptAgentAPIModel-Input:
      type: object
      properties:
        prompt:
          type: string
        llm:
          $ref: '#/components/schemas/LLM'
        reasoning_effort:
          oneOf:
            - $ref: '#/components/schemas/LLMReasoningEffort'
            - type: 'null'
        thinking_budget:
          type:
            - integer
            - 'null'
        temperature:
          type: number
          format: double
        max_tokens:
          type: integer
        tool_ids:
          type: array
          items:
            type: string
        built_in_tools:
          $ref: '#/components/schemas/BuiltInTools-Input'
        mcp_server_ids:
          type: array
          items:
            type: string
        native_mcp_server_ids:
          type: array
          items:
            type: string
        knowledge_base:
          type: array
          items:
            $ref: '#/components/schemas/KnowledgeBaseLocator'
        custom_llm:
          oneOf:
            - $ref: '#/components/schemas/CustomLLM'
            - type: 'null'
        ignore_default_personality:
          type:
            - boolean
            - 'null'
        rag:
          $ref: '#/components/schemas/RagConfig'
        timezone:
          type:
            - string
            - 'null'
        backup_llm_config:
          $ref: '#/components/schemas/PromptAgentApiModelInputBackupLlmConfig'
        tools:
          type: array
          items:
            $ref: '#/components/schemas/PromptAgentApiModelInputToolsItems'
    AgentConfigAPIModel-Input:
      type: object
      properties:
        first_message:
          type: string
        language:
          type: string
        dynamic_variables:
          $ref: '#/components/schemas/DynamicVariablesConfig'
        disable_first_message_interruptions:
          type: boolean
        prompt:
          $ref: '#/components/schemas/PromptAgentAPIModel-Input'
    ConversationalConfigAPIModel-Input:
      type: object
      properties:
        asr:
          $ref: '#/components/schemas/ASRConversationalConfig'
        turn:
          $ref: '#/components/schemas/TurnConfig'
        tts:
          $ref: '#/components/schemas/TTSConversationalConfig-Input'
        conversation:
          $ref: '#/components/schemas/ConversationConfig'
        language_presets:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LanguagePreset-Input'
        vad:
          $ref: '#/components/schemas/VADConfig'
        agent:
          $ref: '#/components/schemas/AgentConfigAPIModel-Input'
    PromptEvaluationCriteria:
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
              value: prompt
        conversation_goal_prompt:
          type: string
        use_knowledge_base:
          type: boolean
      required:
        - id
        - name
        - conversation_goal_prompt
    EvaluationSettings:
      type: object
      properties:
        criteria:
          type: array
          items:
            $ref: '#/components/schemas/PromptEvaluationCriteria'
    EmbedVariant:
      type: string
      enum:
        - value: tiny
        - value: compact
        - value: full
        - value: expandable
    WidgetPlacement:
      type: string
      enum:
        - value: top-left
        - value: top
        - value: top-right
        - value: bottom-left
        - value: bottom
        - value: bottom-right
    WidgetExpandable:
      type: string
      enum:
        - value: never
        - value: mobile
        - value: desktop
        - value: always
    OrbAvatar:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: orb
        color_1:
          type: string
        color_2:
          type: string
    URLAvatar:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: url
        custom_url:
          type: string
    ImageAvatar:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: image
        url:
          type: string
    WidgetConfigInputAvatar:
      oneOf:
        - $ref: '#/components/schemas/OrbAvatar'
        - $ref: '#/components/schemas/URLAvatar'
        - $ref: '#/components/schemas/ImageAvatar'
    WidgetFeedbackMode:
      type: string
      enum:
        - value: none
        - value: during
        - value: end
    WidgetEndFeedbackType:
      type: string
      enum:
        - value: rating
    WidgetEndFeedbackConfig:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/WidgetEndFeedbackType'
    WidgetTextContents:
      type: object
      properties:
        main_label:
          type:
            - string
            - 'null'
        start_call:
          type:
            - string
            - 'null'
        start_chat:
          type:
            - string
            - 'null'
        new_call:
          type:
            - string
            - 'null'
        end_call:
          type:
            - string
            - 'null'
        mute_microphone:
          type:
            - string
            - 'null'
        change_language:
          type:
            - string
            - 'null'
        collapse:
          type:
            - string
            - 'null'
        expand:
          type:
            - string
            - 'null'
        copied:
          type:
            - string
            - 'null'
        accept_terms:
          type:
            - string
            - 'null'
        dismiss_terms:
          type:
            - string
            - 'null'
        listening_status:
          type:
            - string
            - 'null'
        speaking_status:
          type:
            - string
            - 'null'
        connecting_status:
          type:
            - string
            - 'null'
        chatting_status:
          type:
            - string
            - 'null'
        input_label:
          type:
            - string
            - 'null'
        input_placeholder:
          type:
            - string
            - 'null'
        input_placeholder_text_only:
          type:
            - string
            - 'null'
        input_placeholder_new_conversation:
          type:
            - string
            - 'null'
        user_ended_conversation:
          type:
            - string
            - 'null'
        agent_ended_conversation:
          type:
            - string
            - 'null'
        conversation_id:
          type:
            - string
            - 'null'
        error_occurred:
          type:
            - string
            - 'null'
        copy_id:
          type:
            - string
            - 'null'
    WidgetStyles:
      type: object
      properties:
        base:
          type:
            - string
            - 'null'
        base_hover:
          type:
            - string
            - 'null'
        base_active:
          type:
            - string
            - 'null'
        base_border:
          type:
            - string
            - 'null'
        base_subtle:
          type:
            - string
            - 'null'
        base_primary:
          type:
            - string
            - 'null'
        base_error:
          type:
            - string
            - 'null'
        accent:
          type:
            - string
            - 'null'
        accent_hover:
          type:
            - string
            - 'null'
        accent_active:
          type:
            - string
            - 'null'
        accent_border:
          type:
            - string
            - 'null'
        accent_subtle:
          type:
            - string
            - 'null'
        accent_primary:
          type:
            - string
            - 'null'
        overlay_padding:
          type:
            - number
            - 'null'
          format: double
        button_radius:
          type:
            - number
            - 'null'
          format: double
        input_radius:
          type:
            - number
            - 'null'
          format: double
        bubble_radius:
          type:
            - number
            - 'null'
          format: double
        sheet_radius:
          type:
            - number
            - 'null'
          format: double
        compact_sheet_radius:
          type:
            - number
            - 'null'
          format: double
        dropdown_sheet_radius:
          type:
            - number
            - 'null'
          format: double
    WidgetLanguagePreset:
      type: object
      properties:
        text_contents:
          oneOf:
            - $ref: '#/components/schemas/WidgetTextContents'
            - type: 'null'
    WidgetConfig-Input:
      type: object
      properties:
        variant:
          $ref: '#/components/schemas/EmbedVariant'
        placement:
          $ref: '#/components/schemas/WidgetPlacement'
        expandable:
          $ref: '#/components/schemas/WidgetExpandable'
        avatar:
          $ref: '#/components/schemas/WidgetConfigInputAvatar'
        feedback_mode:
          $ref: '#/components/schemas/WidgetFeedbackMode'
        end_feedback:
          oneOf:
            - $ref: '#/components/schemas/WidgetEndFeedbackConfig'
            - type: 'null'
        bg_color:
          type: string
        text_color:
          type: string
        btn_color:
          type: string
        btn_text_color:
          type: string
        border_color:
          type: string
        focus_color:
          type: string
        border_radius:
          type:
            - integer
            - 'null'
        btn_radius:
          type:
            - integer
            - 'null'
        action_text:
          type:
            - string
            - 'null'
        start_call_text:
          type:
            - string
            - 'null'
        end_call_text:
          type:
            - string
            - 'null'
        expand_text:
          type:
            - string
            - 'null'
        listening_text:
          type:
            - string
            - 'null'
        speaking_text:
          type:
            - string
            - 'null'
        shareable_page_text:
          type:
            - string
            - 'null'
        shareable_page_show_terms:
          type: boolean
        terms_text:
          type:
            - string
            - 'null'
        terms_html:
          type:
            - string
            - 'null'
        terms_key:
          type:
            - string
            - 'null'
        show_avatar_when_collapsed:
          type:
            - boolean
            - 'null'
        disable_banner:
          type: boolean
        override_link:
          type:
            - string
            - 'null'
        mic_muting_enabled:
          type: boolean
        transcript_enabled:
          type: boolean
        text_input_enabled:
          type: boolean
        default_expanded:
          type: boolean
        always_expanded:
          type: boolean
        text_contents:
          $ref: '#/components/schemas/WidgetTextContents'
        styles:
          $ref: '#/components/schemas/WidgetStyles'
        language_selector:
          type: boolean
        supports_text_only:
          type: boolean
        custom_avatar_path:
          type:
            - string
            - 'null'
        language_presets:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/WidgetLanguagePreset'
    SoftTimeoutConfigOverrideConfig:
      type: object
      properties:
        message:
          type: boolean
    TurnConfigOverrideConfig:
      type: object
      properties:
        soft_timeout_config:
          $ref: '#/components/schemas/SoftTimeoutConfigOverrideConfig'
    TTSConversationalConfigOverrideConfig:
      type: object
      properties:
        voice_id:
          type: boolean
        stability:
          type: boolean
        speed:
          type: boolean
        similarity_boost:
          type: boolean
    ConversationConfigOverrideConfig:
      type: object
      properties:
        text_only:
          type: boolean
    PromptAgentAPIModelOverrideConfig:
      type: object
      properties:
        prompt:
          type: boolean
        llm:
          type: boolean
        native_mcp_server_ids:
          type: boolean
    AgentConfigOverrideConfig:
      type: object
      properties:
        first_message:
          type: boolean
        language:
          type: boolean
        prompt:
          $ref: '#/components/schemas/PromptAgentAPIModelOverrideConfig'
    ConversationConfigClientOverrideConfig-Input:
      type: object
      properties:
        turn:
          $ref: '#/components/schemas/TurnConfigOverrideConfig'
        tts:
          $ref: '#/components/schemas/TTSConversationalConfigOverrideConfig'
        conversation:
          $ref: '#/components/schemas/ConversationConfigOverrideConfig'
        agent:
          $ref: '#/components/schemas/AgentConfigOverrideConfig'
    ConversationInitiationClientDataConfig-Input:
      type: object
      properties:
        conversation_config_override:
          $ref: '#/components/schemas/ConversationConfigClientOverrideConfig-Input'
        custom_llm_extra_body:
          type: boolean
        enable_conversation_initiation_client_data_from_webhook:
          type: boolean
    ConversationInitiationClientDataWebhookRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
    ConversationInitiationClientDataWebhook:
      type: object
      properties:
        url:
          type: string
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/ConversationInitiationClientDataWebhookRequestHeaders
      required:
        - url
        - request_headers
    WebhookEventType:
      type: string
      enum:
        - value: transcript
        - value: audio
        - value: call_initiation_failure
    ConvAIWebhooks:
      type: object
      properties:
        post_call_webhook_id:
          type:
            - string
            - 'null'
        events:
          type: array
          items:
            $ref: '#/components/schemas/WebhookEventType'
        send_audio:
          type:
            - boolean
            - 'null'
    AgentWorkspaceOverrides-Input:
      type: object
      properties:
        conversation_initiation_client_data_webhook:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationClientDataWebhook'
            - type: 'null'
        webhooks:
          $ref: '#/components/schemas/ConvAIWebhooks'
    AttachedTestModel:
      type: object
      properties:
        test_id:
          type: string
        workflow_node_id:
          type:
            - string
            - 'null'
      required:
        - test_id
    AgentTestingSettings:
      type: object
      properties:
        attached_tests:
          type: array
          items:
            $ref: '#/components/schemas/AttachedTestModel'
    AllowlistItem:
      type: object
      properties:
        hostname:
          type: string
      required:
        - hostname
    AuthSettings:
      type: object
      properties:
        enable_auth:
          type: boolean
        allowlist:
          type: array
          items:
            $ref: '#/components/schemas/AllowlistItem'
        shareable_token:
          type:
            - string
            - 'null'
    AgentCallLimits:
      type: object
      properties:
        agent_concurrency_limit:
          type: integer
        daily_limit:
          type: integer
        bursting_enabled:
          type: boolean
    PrivacyConfig:
      type: object
      properties:
        record_voice:
          type: boolean
        retention_days:
          type: integer
        delete_transcript_and_pii:
          type: boolean
        delete_audio:
          type: boolean
        apply_to_existing_conversations:
          type: boolean
        zero_retention_mode:
          type: boolean
    AgentPlatformSettingsRequestModel:
      type: object
      properties:
        evaluation:
          $ref: '#/components/schemas/EvaluationSettings'
        widget:
          $ref: '#/components/schemas/WidgetConfig-Input'
        data_collection:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        overrides:
          $ref: '#/components/schemas/ConversationInitiationClientDataConfig-Input'
        workspace_overrides:
          $ref: '#/components/schemas/AgentWorkspaceOverrides-Input'
        testing:
          $ref: '#/components/schemas/AgentTestingSettings'
        archived:
          type: boolean
        auth:
          $ref: '#/components/schemas/AuthSettings'
        call_limits:
          $ref: '#/components/schemas/AgentCallLimits'
        privacy:
          $ref: '#/components/schemas/PrivacyConfig'
    WorkflowUnconditionalModel-Input:
      type: object
      properties:
        label:
          type:
            - string
            - 'null'
        type:
          type: string
          enum:
            - type: stringLiteral
              value: unconditional
    WorkflowLLMConditionModel-Input:
      type: object
      properties:
        label:
          type:
            - string
            - 'null'
        type:
          type: string
          enum:
            - type: stringLiteral
              value: llm
        condition:
          type: string
      required:
        - condition
    WorkflowResultConditionModel-Input:
      type: object
      properties:
        label:
          type:
            - string
            - 'null'
        type:
          type: string
          enum:
            - type: stringLiteral
              value: result
        successful:
          type: boolean
      required:
        - successful
    ASTStringNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: string_literal
        value:
          type: string
      required:
        - value
    ASTNumberNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: number_literal
        value:
          type: number
          format: double
      required:
        - value
    ASTBooleanNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: boolean_literal
        value:
          type: boolean
      required:
        - value
    ASTLLMNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: llm
        prompt:
          type: string
      required:
        - prompt
    ASTDynamicVariableNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: dynamic_variable
        name:
          type: string
      required:
        - name
    AstLessThanOrEqualsOperatorNodeInputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    AstLessThanOrEqualsOperatorNodeInputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTLessThanOrEqualsOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: lte_operator
        left:
          $ref: '#/components/schemas/AstLessThanOrEqualsOperatorNodeInputLeft'
        right:
          $ref: '#/components/schemas/AstLessThanOrEqualsOperatorNodeInputRight'
      required:
        - left
        - right
    AstGreaterThanOrEqualsOperatorNodeInputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    AstGreaterThanOrEqualsOperatorNodeInputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTGreaterThanOrEqualsOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: gte_operator
        left:
          $ref: '#/components/schemas/AstGreaterThanOrEqualsOperatorNodeInputLeft'
        right:
          $ref: '#/components/schemas/AstGreaterThanOrEqualsOperatorNodeInputRight'
      required:
        - left
        - right
    AstLessThanOperatorNodeInputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    AstLessThanOperatorNodeInputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTLessThanOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: lt_operator
        left:
          $ref: '#/components/schemas/AstLessThanOperatorNodeInputLeft'
        right:
          $ref: '#/components/schemas/AstLessThanOperatorNodeInputRight'
      required:
        - left
        - right
    AstGreaterThanOperatorNodeInputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    AstGreaterThanOperatorNodeInputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTGreaterThanOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: gt_operator
        left:
          $ref: '#/components/schemas/AstGreaterThanOperatorNodeInputLeft'
        right:
          $ref: '#/components/schemas/AstGreaterThanOperatorNodeInputRight'
      required:
        - left
        - right
    AstNotEqualsOperatorNodeInputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    AstNotEqualsOperatorNodeInputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTNotEqualsOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: neq_operator
        left:
          $ref: '#/components/schemas/AstNotEqualsOperatorNodeInputLeft'
        right:
          $ref: '#/components/schemas/AstNotEqualsOperatorNodeInputRight'
      required:
        - left
        - right
    AstEqualsOperatorNodeInputLeft:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    AstEqualsOperatorNodeInputRight:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTEqualsOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: eq_operator
        left:
          $ref: '#/components/schemas/AstEqualsOperatorNodeInputLeft'
        right:
          $ref: '#/components/schemas/AstEqualsOperatorNodeInputRight'
      required:
        - left
        - right
    AstAndOperatorNodeInputChildrenItems:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTAndOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: and_operator
        children:
          type: array
          items:
            $ref: '#/components/schemas/AstAndOperatorNodeInputChildrenItems'
      required:
        - children
    AstOrOperatorNodeInputChildrenItems:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    ASTOrOperatorNode-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: or_operator
        children:
          type: array
          items:
            $ref: '#/components/schemas/AstOrOperatorNodeInputChildrenItems'
      required:
        - children
    WorkflowExpressionConditionModelInputExpression:
      oneOf:
        - $ref: '#/components/schemas/ASTStringNode-Input'
        - $ref: '#/components/schemas/ASTNumberNode-Input'
        - $ref: '#/components/schemas/ASTBooleanNode-Input'
        - $ref: '#/components/schemas/ASTLLMNode-Input'
        - $ref: '#/components/schemas/ASTDynamicVariableNode-Input'
        - $ref: '#/components/schemas/ASTOrOperatorNode-Input'
        - $ref: '#/components/schemas/ASTAndOperatorNode-Input'
        - $ref: '#/components/schemas/ASTEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTNotEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOperatorNode-Input'
        - $ref: '#/components/schemas/ASTGreaterThanOrEqualsOperatorNode-Input'
        - $ref: '#/components/schemas/ASTLessThanOrEqualsOperatorNode-Input'
    WorkflowExpressionConditionModel-Input:
      type: object
      properties:
        label:
          type:
            - string
            - 'null'
        type:
          type: string
          enum:
            - type: stringLiteral
              value: expression
        expression:
          $ref: '#/components/schemas/WorkflowExpressionConditionModelInputExpression'
      required:
        - expression
    WorkflowEdgeModelInputForwardCondition:
      oneOf:
        - $ref: '#/components/schemas/WorkflowUnconditionalModel-Input'
        - $ref: '#/components/schemas/WorkflowLLMConditionModel-Input'
        - $ref: '#/components/schemas/WorkflowResultConditionModel-Input'
        - $ref: '#/components/schemas/WorkflowExpressionConditionModel-Input'
    WorkflowEdgeModelInputBackwardCondition:
      oneOf:
        - $ref: '#/components/schemas/WorkflowUnconditionalModel-Input'
        - $ref: '#/components/schemas/WorkflowLLMConditionModel-Input'
        - $ref: '#/components/schemas/WorkflowResultConditionModel-Input'
        - $ref: '#/components/schemas/WorkflowExpressionConditionModel-Input'
    WorkflowEdgeModel-Input:
      type: object
      properties:
        source:
          type: string
        target:
          type: string
        forward_condition:
          oneOf:
            - $ref: '#/components/schemas/WorkflowEdgeModelInputForwardCondition'
            - type: 'null'
        backward_condition:
          oneOf:
            - $ref: '#/components/schemas/WorkflowEdgeModelInputBackwardCondition'
            - type: 'null'
      required:
        - source
        - target
    Position-Input:
      type: object
      properties:
        x:
          type: number
          format: double
        'y':
          type: number
          format: double
    WorkflowStartNodeModel-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: start
        position:
          $ref: '#/components/schemas/Position-Input'
        edge_order:
          type: array
          items:
            type: string
    WorkflowEndNodeModel-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: end
        position:
          $ref: '#/components/schemas/Position-Input'
        edge_order:
          type: array
          items:
            type: string
    WorkflowPhoneNumberNodeModelInputTransferDestination:
      oneOf:
        - $ref: '#/components/schemas/PhoneNumberTransferDestination'
        - $ref: '#/components/schemas/SIPUriTransferDestination'
        - $ref: '#/components/schemas/PhoneNumberDynamicVariableTransferDestination'
        - $ref: '#/components/schemas/SIPUriDynamicVariableTransferDestination'
    WorkflowPhoneNumberNodeModel-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: phone_number
        position:
          $ref: '#/components/schemas/Position-Input'
        edge_order:
          type: array
          items:
            type: string
        transfer_destination:
          $ref: >-
            #/components/schemas/WorkflowPhoneNumberNodeModelInputTransferDestination
        transfer_type:
          $ref: '#/components/schemas/TransferTypeEnum'
      required:
        - transfer_destination
    ASRConversationalConfigWorkflowOverride:
      type: object
      properties:
        quality:
          oneOf:
            - $ref: '#/components/schemas/ASRQuality'
            - type: 'null'
        provider:
          oneOf:
            - $ref: '#/components/schemas/ASRProvider'
            - type: 'null'
        user_input_audio_format:
          oneOf:
            - $ref: '#/components/schemas/ASRInputFormat'
            - type: 'null'
        keywords:
          type:
            - array
            - 'null'
          items:
            type: string
    SoftTimeoutConfigWorkflowOverride:
      type: object
      properties:
        timeout_seconds:
          type:
            - number
            - 'null'
          format: double
        message:
          type:
            - string
            - 'null'
    TurnConfigWorkflowOverride:
      type: object
      properties:
        turn_timeout:
          type:
            - number
            - 'null'
          format: double
        initial_wait_time:
          type:
            - number
            - 'null'
          format: double
        silence_end_call_timeout:
          type:
            - number
            - 'null'
          format: double
        soft_timeout_config:
          oneOf:
            - $ref: '#/components/schemas/SoftTimeoutConfigWorkflowOverride'
            - type: 'null'
        turn_eagerness:
          oneOf:
            - $ref: '#/components/schemas/TurnEagerness'
            - type: 'null'
    TTSConversationalConfigWorkflowOverride-Input:
      type: object
      properties:
        model_id:
          oneOf:
            - $ref: '#/components/schemas/TTSConversationalModel'
            - type: 'null'
        voice_id:
          type:
            - string
            - 'null'
        supported_voices:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/SupportedVoice'
        agent_output_audio_format:
          oneOf:
            - $ref: '#/components/schemas/TTSOutputFormat'
            - type: 'null'
        optimize_streaming_latency:
          oneOf:
            - $ref: '#/components/schemas/TTSOptimizeStreamingLatency'
            - type: 'null'
        stability:
          type:
            - number
            - 'null'
          format: double
        speed:
          type:
            - number
            - 'null'
          format: double
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
        pronunciation_dictionary_locators:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/PydanticPronunciationDictionaryVersionLocator'
    ConversationConfigWorkflowOverride:
      type: object
      properties:
        text_only:
          type:
            - boolean
            - 'null'
        max_duration_seconds:
          type:
            - integer
            - 'null'
        client_events:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ClientEvent'
    VADConfigWorkflowOverride:
      type: object
      properties: {}
    DynamicVariablesConfigWorkflowOverrideDynamicVariablePlaceholders:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: integer
        - type: boolean
    DynamicVariablesConfigWorkflowOverride:
      type: object
      properties:
        dynamic_variable_placeholders:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: >-
              #/components/schemas/DynamicVariablesConfigWorkflowOverrideDynamicVariablePlaceholders
    BuiltInToolsWorkflowOverride-Input:
      type: object
      properties:
        end_call:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        language_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        transfer_to_agent:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        transfer_to_number:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        skip_turn:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        play_keypad_touch_tone:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
        voicemail_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
    RagConfigWorkflowOverride:
      type: object
      properties:
        enabled:
          type:
            - boolean
            - 'null'
        embedding_model:
          oneOf:
            - $ref: '#/components/schemas/EmbeddingModelEnum'
            - type: 'null'
        max_vector_distance:
          type:
            - number
            - 'null'
          format: double
        max_documents_length:
          type:
            - integer
            - 'null'
        max_retrieved_rag_chunks_count:
          type:
            - integer
            - 'null'
    PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig:
      oneOf:
        - $ref: '#/components/schemas/BackupLLMDefault'
        - $ref: '#/components/schemas/BackupLLMDisabled'
        - $ref: '#/components/schemas/BackupLLMOverride'
    PromptAgentApiModelWorkflowOverrideInputToolsItems:
      oneOf:
        - $ref: '#/components/schemas/WebhookToolConfig-Input'
        - $ref: '#/components/schemas/ClientToolConfig-Input'
        - $ref: '#/components/schemas/SystemToolConfig-Input'
        - $ref: '#/components/schemas/ApiIntegrationWebhookToolConfig-Input'
    PromptAgentAPIModelWorkflowOverride-Input:
      type: object
      properties:
        prompt:
          type:
            - string
            - 'null'
        llm:
          oneOf:
            - $ref: '#/components/schemas/LLM'
            - type: 'null'
        reasoning_effort:
          oneOf:
            - $ref: '#/components/schemas/LLMReasoningEffort'
            - type: 'null'
        thinking_budget:
          type:
            - integer
            - 'null'
        temperature:
          type:
            - number
            - 'null'
          format: double
        max_tokens:
          type:
            - integer
            - 'null'
        tool_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        built_in_tools:
          oneOf:
            - $ref: '#/components/schemas/BuiltInToolsWorkflowOverride-Input'
            - type: 'null'
        mcp_server_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        native_mcp_server_ids:
          type:
            - array
            - 'null'
          items:
            type: string
        knowledge_base:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/KnowledgeBaseLocator'
        custom_llm:
          oneOf:
            - $ref: '#/components/schemas/CustomLLM'
            - type: 'null'
        ignore_default_personality:
          type:
            - boolean
            - 'null'
        rag:
          oneOf:
            - $ref: '#/components/schemas/RagConfigWorkflowOverride'
            - type: 'null'
        timezone:
          type:
            - string
            - 'null'
        backup_llm_config:
          oneOf:
            - $ref: >-
                #/components/schemas/PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig
            - type: 'null'
        tools:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/PromptAgentApiModelWorkflowOverrideInputToolsItems
    AgentConfigAPIModelWorkflowOverride-Input:
      type: object
      properties:
        first_message:
          type:
            - string
            - 'null'
        language:
          type:
            - string
            - 'null'
        dynamic_variables:
          oneOf:
            - $ref: '#/components/schemas/DynamicVariablesConfigWorkflowOverride'
            - type: 'null'
        disable_first_message_interruptions:
          type:
            - boolean
            - 'null'
        prompt:
          oneOf:
            - $ref: '#/components/schemas/PromptAgentAPIModelWorkflowOverride-Input'
            - type: 'null'
    ConversationalConfigAPIModelWorkflowOverride-Input:
      type: object
      properties:
        asr:
          oneOf:
            - $ref: '#/components/schemas/ASRConversationalConfigWorkflowOverride'
            - type: 'null'
        turn:
          oneOf:
            - $ref: '#/components/schemas/TurnConfigWorkflowOverride'
            - type: 'null'
        tts:
          oneOf:
            - $ref: >-
                #/components/schemas/TTSConversationalConfigWorkflowOverride-Input
            - type: 'null'
        conversation:
          oneOf:
            - $ref: '#/components/schemas/ConversationConfigWorkflowOverride'
            - type: 'null'
        language_presets:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/LanguagePreset-Input'
        vad:
          oneOf:
            - $ref: '#/components/schemas/VADConfigWorkflowOverride'
            - type: 'null'
        agent:
          oneOf:
            - $ref: '#/components/schemas/AgentConfigAPIModelWorkflowOverride-Input'
            - type: 'null'
    WorkflowOverrideAgentNodeModel-Input:
      type: object
      properties:
        conversation_config:
          $ref: >-
            #/components/schemas/ConversationalConfigAPIModelWorkflowOverride-Input
        additional_prompt:
          type: string
        additional_knowledge_base:
          type: array
          items:
            $ref: '#/components/schemas/KnowledgeBaseLocator'
        additional_tool_ids:
          type: array
          items:
            type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: override_agent
        position:
          $ref: '#/components/schemas/Position-Input'
        edge_order:
          type: array
          items:
            type: string
        label:
          type: string
      required:
        - label
    WorkflowStandaloneAgentNodeModel-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: standalone_agent
        position:
          $ref: '#/components/schemas/Position-Input'
        edge_order:
          type: array
          items:
            type: string
        agent_id:
          type: string
        delay_ms:
          type: integer
        transfer_message:
          type:
            - string
            - 'null'
        enable_transferred_agent_first_message:
          type: boolean
      required:
        - agent_id
    WorkflowToolLocator:
      type: object
      properties:
        tool_id:
          type: string
      required:
        - tool_id
    WorkflowToolNodeModel-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: tool
        position:
          $ref: '#/components/schemas/Position-Input'
        edge_order:
          type: array
          items:
            type: string
        tools:
          type: array
          items:
            $ref: '#/components/schemas/WorkflowToolLocator'
    AgentWorkflowRequestModelNodes:
      oneOf:
        - $ref: '#/components/schemas/WorkflowStartNodeModel-Input'
        - $ref: '#/components/schemas/WorkflowEndNodeModel-Input'
        - $ref: '#/components/schemas/WorkflowPhoneNumberNodeModel-Input'
        - $ref: '#/components/schemas/WorkflowOverrideAgentNodeModel-Input'
        - $ref: '#/components/schemas/WorkflowStandaloneAgentNodeModel-Input'
        - $ref: '#/components/schemas/WorkflowToolNodeModel-Input'
    AgentWorkflowRequestModel:
      type: object
      properties:
        edges:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/WorkflowEdgeModel-Input'
        nodes:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/AgentWorkflowRequestModelNodes'
    Body_Create_Agent_v1_convai_agents_create_post:
      type: object
      properties:
        conversation_config:
          $ref: '#/components/schemas/ConversationalConfigAPIModel-Input'
        platform_settings:
          oneOf:
            - $ref: '#/components/schemas/AgentPlatformSettingsRequestModel'
            - type: 'null'
        workflow:
          $ref: '#/components/schemas/AgentWorkflowRequestModel'
        name:
          type:
            - string
            - 'null'
        tags:
          type:
            - array
            - 'null'
          items:
            type: string
      required:
        - conversation_config
    CreateAgentResponseModel:
      type: object
      properties:
        agent_id:
          type: string
      required:
        - agent_id

```


## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        environment: "https://api.elevenlabs.io",
    });
    await client.conversationalAi.agents.create({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    base_url="https://api.elevenlabs.io"
)

client.conversational_ai.agents.create()

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

	url := "https://api.elevenlabs.io/v1/convai/agents/create"

	payload := strings.NewReader("{}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/create")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/create")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/create', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/create");
var request = new RestRequest(Method.POST);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/create")! as URL,
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
**Navigation:** [← Previous](./41-delete-voice-sample.md) | [Index](./index.md) | [Next →](./43-get-agent.md)
