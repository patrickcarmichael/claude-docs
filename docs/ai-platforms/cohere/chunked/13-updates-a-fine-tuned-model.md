**Navigation:** [← Previous](./12-delete-a-dataset.md) | [Index](./index.md) | [Next →](./14-step-4-conversation-with-memory-using-ai-messages-.md)

---

# Updates a fine-tuned model.

PATCH https://api.cohere.com/v1/finetuning/finetuned-models/{id}
Content-Type: application/json

Updates the fine-tuned model with the given ID. The model will be updated with the new settings and name provided in the request body.

Reference: https://docs.cohere.com/reference/updatefinetunedmodel

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Updates a fine-tuned model.
  version: endpoint_finetuning.UpdateFinetunedModel
paths:
  /v1/finetuning/finetuned-models/{id}:
    patch:
      operationId: update-finetuned-model
      summary: Updates a fine-tuned model.
      description: >-
        Updates the fine-tuned model with the given ID. The model will be
        updated with the new settings and name provided in the request body.
      tags:
        - - subpackage_finetuning
      parameters:
        - name: id
          in: path
          description: FinetunedModel ID.
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateFinetunedModelResponse'
        '400':
          description: Bad Request
          content: {}
        '401':
          description: Unauthorized
          content: {}
        '403':
          description: Forbidden
          content: {}
        '404':
          description: Not Found
          content: {}
        '500':
          description: Internal Server Error
          content: {}
        '503':
          description: Status Service Unavailable
          content: {}
      requestBody:
        description: >-
          Information about the fine-tuned model. Must contain name and
          settings.
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                creator_id:
                  type: string
                organization_id:
                  type: string
                settings:
                  $ref: '#/components/schemas/Settings'
                status:
                  $ref: '#/components/schemas/Status'
                created_at:
                  type: string
                  format: date-time
                updated_at:
                  type: string
                  format: date-time
                completed_at:
                  type: string
                  format: date-time
                last_used:
                  type: string
                  format: date-time
              required:
                - name
                - settings
components:
  schemas:
    BaseType:
      type: string
      enum:
        - value: BASE_TYPE_UNSPECIFIED
        - value: BASE_TYPE_GENERATIVE
        - value: BASE_TYPE_CLASSIFICATION
        - value: BASE_TYPE_RERANK
        - value: BASE_TYPE_CHAT
    Strategy:
      type: string
      enum:
        - value: STRATEGY_UNSPECIFIED
        - value: STRATEGY_VANILLA
        - value: STRATEGY_TFEW
    BaseModel:
      type: object
      properties:
        name:
          type: string
        version:
          type: string
        base_type:
          $ref: '#/components/schemas/BaseType'
        strategy:
          $ref: '#/components/schemas/Strategy'
      required:
        - base_type
    LoraTargetModules:
      type: string
      enum:
        - value: LORA_TARGET_MODULES_UNSPECIFIED
        - value: LORA_TARGET_MODULES_QV
        - value: LORA_TARGET_MODULES_QKVO
        - value: LORA_TARGET_MODULES_QKVO_FFN
    Hyperparameters:
      type: object
      properties:
        early_stopping_patience:
          type: integer
        early_stopping_threshold:
          type: number
          format: double
        train_batch_size:
          type: integer
        train_epochs:
          type: integer
        learning_rate:
          type: number
          format: double
        lora_alpha:
          type: integer
        lora_rank:
          type: integer
        lora_target_modules:
          $ref: '#/components/schemas/LoraTargetModules'
    WandbConfig:
      type: object
      properties:
        project:
          type: string
        api_key:
          type: string
        entity:
          type: string
      required:
        - project
        - api_key
    Settings:
      type: object
      properties:
        base_model:
          $ref: '#/components/schemas/BaseModel'
        dataset_id:
          type: string
        hyperparameters:
          $ref: '#/components/schemas/Hyperparameters'
        multi_label:
          type: boolean
        wandb:
          $ref: '#/components/schemas/WandbConfig'
      required:
        - base_model
        - dataset_id
    Status:
      type: string
      enum:
        - value: STATUS_UNSPECIFIED
        - value: STATUS_FINETUNING
        - value: STATUS_DEPLOYING_API
        - value: STATUS_READY
        - value: STATUS_FAILED
        - value: STATUS_DELETED
        - value: STATUS_TEMPORARILY_OFFLINE
        - value: STATUS_PAUSED
        - value: STATUS_QUEUED
    FinetunedModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        creator_id:
          type: string
        organization_id:
          type: string
        settings:
          $ref: '#/components/schemas/Settings'
        status:
          $ref: '#/components/schemas/Status'
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        completed_at:
          type: string
          format: date-time
        last_used:
          type: string
          format: date-time
      required:
        - name
        - settings
    UpdateFinetunedModelResponse:
      type: object
      properties:
        finetuned_model:
          $ref: '#/components/schemas/FinetunedModel'

```

## SDK Code Examples

```java Cohere java SDK
/* (C)2024 */
package finetuning;

import com.cohere.api.Cohere;
import com.cohere.api.resources.finetuning.finetuning.types.BaseModel;
import com.cohere.api.resources.finetuning.finetuning.types.BaseType;
import com.cohere.api.resources.finetuning.finetuning.types.Settings;
import com.cohere.api.resources.finetuning.finetuning.types.UpdateFinetunedModelResponse;
import com.cohere.api.resources.finetuning.requests.FinetuningUpdateFinetunedModelRequest;

public class UpdateFinetunedModel {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    UpdateFinetunedModelResponse response =
        cohere
            .finetuning()
            .updateFinetunedModel(
                "test-id",
                FinetuningUpdateFinetunedModelRequest.builder()
                    .name("new name")
                    .settings(
                        Settings.builder()
                            .baseModel(
                                BaseModel.builder().baseType(BaseType.BASE_TYPE_CHAT).build())
                            .datasetId("my-dataset-id")
                            .build())
                    .build());

    System.out.println(response);
  }
}

```

```go Cohere Go SDK
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	"github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Finetuning.UpdateFinetunedModel(
		context.TODO(),
		"test-id",
		&cohere.FinetuningUpdateFinetunedModelRequest{
			Name: "new-name",
		},
	)
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp.FinetunedModel)
}

```

```typescript Cohere TypeScript SDK
const { CohereClient } = require('cohere-ai');

const cohere = new CohereClient({
  token: '<<apiKey>>',
});

(async () => {
  const finetunedModel = await cohere.finetuning.updateFinetunedModel('test-id', {
    name: 'new name',
  });

  console.log(finetunedModel);
})();

```

```python Sync
from cohere.finetuning import (
    BaseModel,
    Settings,
)
import cohere

co = cohere.Client()
finetuned_model = co.finetuning.update_finetuned_model(
    id="test-id",
    name="new name",
    settings=Settings(
        base_model=BaseModel(
            base_type="BASE_TYPE_CHAT",
        ),
        dataset_id="my-dataset-id",
    ),
)

print(finetuned_model)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.finetuning.update_finetuned_model(id="test-id", name="new name")
    print(response)


asyncio.run(main())

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/finetuning/finetuned-models/id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"string\",\n  \"settings\": {\n    \"base_model\": {\n      \"base_type\": \"BASE_TYPE_UNSPECIFIED\"\n    },\n    \"dataset_id\": \"string\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.cohere.com/v1/finetuning/finetuned-models/id', [
  'body' => '{
  "name": "string",
  "settings": {
    "base_model": {
      "base_type": "BASE_TYPE_UNSPECIFIED"
    },
    "dataset_id": "string"
  }
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/finetuning/finetuned-models/id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"string\",\n  \"settings\": {\n    \"base_model\": {\n      \"base_type\": \"BASE_TYPE_UNSPECIFIED\"\n    },\n    \"dataset_id\": \"string\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "name": "string",
  "settings": [
    "base_model": ["base_type": "BASE_TYPE_UNSPECIFIED"],
    "dataset_id": "string"
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/finetuning/finetuned-models/id")! as URL,
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

# Returns a fine-tuned model by ID.

GET https://api.cohere.com/v1/finetuning/finetuned-models/{id}

Retrieve a fine-tuned model by its ID.

Reference: https://docs.cohere.com/reference/getfinetunedmodel

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Returns a fine-tuned model by ID.
  version: endpoint_finetuning.GetFinetunedModel
paths:
  /v1/finetuning/finetuned-models/{id}:
    get:
      operationId: get-finetuned-model
      summary: Returns a fine-tuned model by ID.
      description: Retrieve a fine-tuned model by its ID.
      tags:
        - - subpackage_finetuning
      parameters:
        - name: id
          in: path
          description: The fine-tuned model ID.
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetFinetunedModelResponse'
        '400':
          description: Bad Request
          content: {}
        '401':
          description: Unauthorized
          content: {}
        '403':
          description: Forbidden
          content: {}
        '404':
          description: Not Found
          content: {}
        '500':
          description: Internal Server Error
          content: {}
        '503':
          description: Status Service Unavailable
          content: {}
components:
  schemas:
    BaseType:
      type: string
      enum:
        - value: BASE_TYPE_UNSPECIFIED
        - value: BASE_TYPE_GENERATIVE
        - value: BASE_TYPE_CLASSIFICATION
        - value: BASE_TYPE_RERANK
        - value: BASE_TYPE_CHAT
    Strategy:
      type: string
      enum:
        - value: STRATEGY_UNSPECIFIED
        - value: STRATEGY_VANILLA
        - value: STRATEGY_TFEW
    BaseModel:
      type: object
      properties:
        name:
          type: string
        version:
          type: string
        base_type:
          $ref: '#/components/schemas/BaseType'
        strategy:
          $ref: '#/components/schemas/Strategy'
      required:
        - base_type
    LoraTargetModules:
      type: string
      enum:
        - value: LORA_TARGET_MODULES_UNSPECIFIED
        - value: LORA_TARGET_MODULES_QV
        - value: LORA_TARGET_MODULES_QKVO
        - value: LORA_TARGET_MODULES_QKVO_FFN
    Hyperparameters:
      type: object
      properties:
        early_stopping_patience:
          type: integer
        early_stopping_threshold:
          type: number
          format: double
        train_batch_size:
          type: integer
        train_epochs:
          type: integer
        learning_rate:
          type: number
          format: double
        lora_alpha:
          type: integer
        lora_rank:
          type: integer
        lora_target_modules:
          $ref: '#/components/schemas/LoraTargetModules'
    WandbConfig:
      type: object
      properties:
        project:
          type: string
        api_key:
          type: string
        entity:
          type: string
      required:
        - project
        - api_key
    Settings:
      type: object
      properties:
        base_model:
          $ref: '#/components/schemas/BaseModel'
        dataset_id:
          type: string
        hyperparameters:
          $ref: '#/components/schemas/Hyperparameters'
        multi_label:
          type: boolean
        wandb:
          $ref: '#/components/schemas/WandbConfig'
      required:
        - base_model
        - dataset_id
    Status:
      type: string
      enum:
        - value: STATUS_UNSPECIFIED
        - value: STATUS_FINETUNING
        - value: STATUS_DEPLOYING_API
        - value: STATUS_READY
        - value: STATUS_FAILED
        - value: STATUS_DELETED
        - value: STATUS_TEMPORARILY_OFFLINE
        - value: STATUS_PAUSED
        - value: STATUS_QUEUED
    FinetunedModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        creator_id:
          type: string
        organization_id:
          type: string
        settings:
          $ref: '#/components/schemas/Settings'
        status:
          $ref: '#/components/schemas/Status'
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        completed_at:
          type: string
          format: date-time
        last_used:
          type: string
          format: date-time
      required:
        - name
        - settings
    GetFinetunedModelResponse:
      type: object
      properties:
        finetuned_model:
          $ref: '#/components/schemas/FinetunedModel'

```

## SDK Code Examples

```java Cohere java SDK
/* (C)2024 */
package finetuning;

import com.cohere.api.Cohere;
import com.cohere.api.resources.finetuning.finetuning.types.GetFinetunedModelResponse;

public class GetFinetunedModel {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    GetFinetunedModelResponse response = cohere.finetuning().getFinetunedModel("test-id");

    System.out.println(response);
  }
}

```

```go Cohere Go SDK
package main

import (
	"context"
	"log"
	"os"

	"github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Finetuning.GetFinetunedModel(context.TODO(), "test-id")
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp.FinetunedModel)
}

```

```typescript Cohere TypeScript SDK
const { CohereClient } = require('cohere-ai');

const cohere = new CohereClient({
  token: '<<apiKey>>',
});

(async () => {
  const finetunedModel = await cohere.finetuning.getFinetunedModel('test-id');

  console.log(finetunedModel);
})();

```

```python Sync
import cohere

co = cohere.Client()
response = co.finetuning.get_finetuned_model("test-id")
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.finetuning.get_finetuned_model("test-id")
    print(response)


asyncio.run(main())

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/finetuning/finetuned-models/id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.cohere.com/v1/finetuning/finetuned-models/id', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/finetuning/finetuned-models/id");
var request = new RestRequest(Method.GET);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/finetuning/finetuned-models/id")! as URL,
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

# Deletes a fine-tuned model.

DELETE https://api.cohere.com/v1/finetuning/finetuned-models/{id}

Deletes a fine-tuned model. The model will be removed from the system and will no longer be available for use.
This operation is irreversible.

Reference: https://docs.cohere.com/reference/deletefinetunedmodel

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Deletes a fine-tuned model.
  version: endpoint_finetuning.DeleteFinetunedModel
paths:
  /v1/finetuning/finetuned-models/{id}:
    delete:
      operationId: delete-finetuned-model
      summary: Deletes a fine-tuned model.
      description: >-
        Deletes a fine-tuned model. The model will be removed from the system
        and will no longer be available for use.

        This operation is irreversible.
      tags:
        - - subpackage_finetuning
      parameters:
        - name: id
          in: path
          description: The fine-tuned model ID.
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteFinetunedModelResponse'
        '400':
          description: Bad Request
          content: {}
        '401':
          description: Unauthorized
          content: {}
        '403':
          description: Forbidden
          content: {}
        '404':
          description: Not Found
          content: {}
        '500':
          description: Internal Server Error
          content: {}
        '503':
          description: Status Service Unavailable
          content: {}
components:
  schemas:
    DeleteFinetunedModelResponse:
      type: object
      properties: {}

```

## SDK Code Examples

```java Cohere java SDK
/* (C)2024 */
package finetuning;

import com.cohere.api.Cohere;

public class DeleteFinetunedModel {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    cohere.finetuning().deleteFinetunedModel("test-id");
  }
}

```

```go Cohere Go SDK
package main

import (
	"context"
	"log"
	"os"

	"github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	_, err := co.Finetuning.DeleteFinetunedModel(context.TODO(), "test-id")
	if err != nil {
		log.Fatal(err)
	}
}

```

```typescript Cohere TypeScript SDK
const { CohereClient } = require('cohere-ai');

const cohere = new CohereClient({
  token: '<<apiKey>>',
});

(async () => {
  await cohere.finetuning.deleteFinetunedModel('test-id');
})();

```

```python Sync
import cohere

co = cohere.Client()
co.finetuning.delete_finetuned_model("test-id")

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    await co.finetuning.delete_finetuned_model("test-id")


asyncio.run(main())

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/finetuning/finetuned-models/id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.cohere.com/v1/finetuning/finetuned-models/id', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/finetuning/finetuned-models/id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/finetuning/finetuned-models/id")! as URL,
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

# Fetch history of statuses for a fine-tuned model.

GET https://api.cohere.com/v1/finetuning/finetuned-models/{finetuned_model_id}/events

Returns a list of events that occurred during the life-cycle of the fine-tuned model.
The events are ordered by creation time, with the most recent event first.
The list can be paginated using `page_size` and `page_token` parameters.

Reference: https://docs.cohere.com/reference/listevents

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Fetch history of statuses for a fine-tuned model.
  version: endpoint_finetuning.ListEvents
paths:
  /v1/finetuning/finetuned-models/{finetuned_model_id}/events:
    get:
      operationId: list-events
      summary: Fetch history of statuses for a fine-tuned model.
      description: >-
        Returns a list of events that occurred during the life-cycle of the
        fine-tuned model.

        The events are ordered by creation time, with the most recent event
        first.

        The list can be paginated using `page_size` and `page_token` parameters.
      tags:
        - - subpackage_finetuning
      parameters:
        - name: finetuned_model_id
          in: path
          description: The parent fine-tuned model ID.
          required: true
          schema:
            type: string
        - name: page_size
          in: query
          description: >-
            Maximum number of results to be returned by the server. If 0,
            defaults to

            50.
          required: false
          schema:
            type: integer
        - name: page_token
          in: query
          description: Request a specific page of the list results.
          required: false
          schema:
            type: string
        - name: order_by
          in: query
          description: >-
            Comma separated list of fields. For example: "created_at,name". The
            default

            sorting order is ascending. To specify descending order for a field,
            append

            " desc" to the field name. For example: "created_at desc,name".


            Supported sorting fields:
              - created_at (default)
          required: false
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListEventsResponse'
        '400':
          description: Bad Request
          content: {}
        '401':
          description: Unauthorized
          content: {}
        '403':
          description: Forbidden
          content: {}
        '404':
          description: Not Found
          content: {}
        '500':
          description: Internal Server Error
          content: {}
        '503':
          description: Status Service Unavailable
          content: {}
components:
  schemas:
    Status:
      type: string
      enum:
        - value: STATUS_UNSPECIFIED
        - value: STATUS_FINETUNING
        - value: STATUS_DEPLOYING_API
        - value: STATUS_READY
        - value: STATUS_FAILED
        - value: STATUS_DELETED
        - value: STATUS_TEMPORARILY_OFFLINE
        - value: STATUS_PAUSED
        - value: STATUS_QUEUED
    Event:
      type: object
      properties:
        user_id:
          type: string
        status:
          $ref: '#/components/schemas/Status'
        created_at:
          type: string
          format: date-time
    ListEventsResponse:
      type: object
      properties:
        events:
          type: array
          items:
            $ref: '#/components/schemas/Event'
        next_page_token:
          type: string
        total_size:
          type: integer

```

## SDK Code Examples

```java Cohere java SDK
/* (C)2024 */
package finetuning;

import com.cohere.api.Cohere;
import com.cohere.api.resources.finetuning.finetuning.types.ListEventsResponse;

public class ListEvents {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ListEventsResponse response = cohere.finetuning().listEvents("test-id");

    System.out.println(response);
  }
}

```

```go Cohere Go SDK
package main

import (
	"context"
	"log"
	"os"

	"github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Finetuning.ListEvents(
		context.TODO(),
		"test-finetuned-model-id",
		nil,
	)
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp.Events)
}

```

```typescript Cohere TypeScript SDK
const { CohereClient } = require('cohere-ai');

const cohere = new CohereClient({
  token: '<<apiKey>>',
});

(async () => {
  const events = await cohere.finetuning.listEvents('test-finetuned-model-id');

  console.log(events);
})();

```

```python Sync
import cohere

co = cohere.Client()
response = co.finetuning.list_events(finetuned_model_id="test-id")
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.finetuning.list_events(finetuned_model_id="test-id")
    print(response)


asyncio.run(main())

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/events")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/events', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/events");
var request = new RestRequest(Method.GET);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/events")! as URL,
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

# Retrieve training metrics for fine-tuned models.

GET https://api.cohere.com/v1/finetuning/finetuned-models/{finetuned_model_id}/training-step-metrics

Returns a list of metrics measured during the training of a fine-tuned model.
The metrics are ordered by step number, with the most recent step first.
The list can be paginated using `page_size` and `page_token` parameters.

Reference: https://docs.cohere.com/reference/listtrainingstepmetrics

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Retrieve training metrics for fine-tuned models.
  version: endpoint_finetuning.ListTrainingStepMetrics
paths:
  /v1/finetuning/finetuned-models/{finetuned_model_id}/training-step-metrics:
    get:
      operationId: list-training-step-metrics
      summary: Retrieve training metrics for fine-tuned models.
      description: >-
        Returns a list of metrics measured during the training of a fine-tuned
        model.

        The metrics are ordered by step number, with the most recent step first.

        The list can be paginated using `page_size` and `page_token` parameters.
      tags:
        - - subpackage_finetuning
      parameters:
        - name: finetuned_model_id
          in: path
          description: The parent fine-tuned model ID.
          required: true
          schema:
            type: string
        - name: page_size
          in: query
          description: >-
            Maximum number of results to be returned by the server. If 0,
            defaults to

            50.
          required: false
          schema:
            type: integer
        - name: page_token
          in: query
          description: Request a specific page of the list results.
          required: false
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListTrainingStepMetricsResponse'
        '400':
          description: Bad Request
          content: {}
        '401':
          description: Unauthorized
          content: {}
        '403':
          description: Forbidden
          content: {}
        '404':
          description: Not Found
          content: {}
        '500':
          description: Internal Server Error
          content: {}
        '503':
          description: Status Service Unavailable
          content: {}
components:
  schemas:
    TrainingStepMetrics:
      type: object
      properties:
        created_at:
          type: string
          format: date-time
        step_number:
          type: integer
        metrics:
          type: object
          additionalProperties:
            type: number
            format: double
    ListTrainingStepMetricsResponse:
      type: object
      properties:
        step_metrics:
          type: array
          items:
            $ref: '#/components/schemas/TrainingStepMetrics'
        next_page_token:
          type: string

```

## SDK Code Examples

```java Cohere java SDK
/* (C)2024 */
package finetuning;

import com.cohere.api.Cohere;
import com.cohere.api.resources.finetuning.finetuning.types.ListTrainingStepMetricsResponse;

public class ListTrainingStepMetrics {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ListTrainingStepMetricsResponse response =
        cohere.finetuning().listTrainingStepMetrics("test-id");

    System.out.println(response);
  }
}

```

```go Cohere Go SDK
package main

import (
	"context"
	"log"
	"os"

	"github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Finetuning.ListTrainingStepMetrics(
		context.TODO(),
		"test-finetuned-model-id",
		nil,
	)
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp.StepMetrics)
}

```

```typescript Cohere TypeScript SDK
const { CohereClient } = require('cohere-ai');

const cohere = new CohereClient({
  token: '<<apiKey>>',
});

(async () => {
  const trainingStepMetrics = await cohere.finetuning.listTrainingStepMetrics(
    'test-finetuned-model-id'
  );

  console.log(trainingStepMetrics);
})();

```

```python Sync
import cohere

co = cohere.Client()
train_step_metrics = co.finetuning.list_training_step_metrics(
    finetuned_model_id="test-id"
)
print(train_step_metrics)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.finetuning.list_train_step_metrics(finetuned_model_id="test-id")
    print(response)


asyncio.run(main())

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/training-step-metrics")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/training-step-metrics', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/training-step-metrics");
var request = new RestRequest(Method.GET);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/training-step-metrics")! as URL,
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

# Release Notes



# Announcing Major Command Deprecations

> This announcement covers a series of major deprecations, including of classic Command models, several parameters, and entire endpoints.

As part of our ongoing commitment to delivering advanced AI solutions, we are deprecating the following models, features, and API endpoints:

Deprecated Models:

* `command-r-03-2024`  (and the alias `command-r`)
* `command-r-plus-04-2024`  (and the alias `command-r-plus`)
* `command-light`
* `command`
* `summarize` (Refer to [the migration guide](https://docs.cohere.com/docs/summarizing-text#migration-from-summarize-to-chat-endpoint) for alternatives).

For command model replacements, we recommend you use `command-r-08-2024`, `command-r-plus-08-2024`, or `command-a-03-2025` (which is the strongest-performing model across domains) instead.

Retired Fine-Tuning Capabilities:
All fine-tuning options via dashboard and API for models including `command-light`, `command`, `command-r`, `classify`, and `rerank` are being retired. Previously fine-tuned models will no longer be accessible.

Deprecated Features and API Endpoints:

* `/v1/connectors` (Managed connectors for RAG)
* `/v1/chat` parameters: `connectors`, `search_queries_only`
* `/v1/generate` (Legacy generative endpoint)
* `/v1/summarize` (Legacy summarization endpoint)
* `/v1/classify`
* Slack App integration
* Coral Web UI (chat.cohere.com and coral.cohere.com)

For questions, reach out to [support@cohere.com](mailto:support@cohere.com)


# Announcing Cohere's Command A Translate Model

> This announcement covers the release of Command A Translate, Cohere's most powerful translation model.

We're excited to announce the release of **Command A Translate**, Cohere's first machine translation model. It achieves state-of-the-art performance at producing accurate, fluent translations across 23 languages.

## Key Features

* **23 supported languages**: English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Chinese, Arabic, Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian
* **111 billion parameters** for superior translation quality
* **16K token context length** (8K input + 8K output) for handling longer texts
* **Optimized for deployment** on 1-2 GPUs (A100s/H100s)
* **Secure deployment options** for sensitive data translation

## Getting Started

The model is available immediately through Cohere's Chat API endpoint. You can start translating text with simple prompts or integrate it programmatically into your applications.

```python
from cohere import ClientV2

co = ClientV2(api_key="<YOUR API KEY>")

response = co.chat(
    model="command-a-translate-08-2025",
    messages=[
        {
            "role": "user",
            "content": "Translate this text to Spanish: Hello, how are you?",
        }
    ],
)
```

## Availability

Command A Translate (`command-a-translate-08-2025`) is now available for all Cohere users through our standard API endpoints. For enterprise customers, [private deployment](https://docs.cohere.com/docs/private-deployment-overview) options are available to ensure maximum security and control over your translation workflows.

For more detailed information about Command A Translate, including technical specifications and implementation examples, visit our [model documentation](/docs/command-a-translate).


# Announcing Cohere's Command A Reasoning Model

> This announcement covers the release of Command A Reasoning, Cohere's first model able to engage in thinking and reasoning.

We’re excited to announce the release of **Command A Reasoning**, a hybrid reasoning model designed to excel at complex agentic tasks, in English and 22 other languages. With 111 billion parameters and a 256K context length, this model brings advanced reasoning capabilities to your applications through the familiar Command API interface.

**Key Features**

* **Tool Use**: Provides the strongest tool use performance out of the Command family of models.
* **Agentic Applications**: Demonstrates proactive problem-solving, autonomously using tools and resources to complete highly complex tasks.
* **Multilingual**: With 23 languages supported, the model solves reasoning and agentic problems in the language your business operates in.

**Technical Specifications**

* **Model Name**: `command-a-reasoning-08-2025`
* **Context Length**: 256K tokens
* **Maximum Output**: 32K tokens
* **API Endpoint**: Chat API

### Getting Started

Integrating Command A Reasoning is straightforward using the Chat API. Here’s a non-streaming example:

<CodeBlocks>
  ```python PYTHON 
  from cohere import ClientV2

  co = ClientV2("<YOUR_API_KEY>")

  prompt = """
  Alice has 3 brothers and she also has 2 sisters. How many sisters does Alice's brother have?
  """

  response = co.chat(
      model="command-a-reasoning-08-2025",
      messages=[
          {
              "role": "user",
              "content": prompt,
          }
      ],
  )

  for content in response.message.content:
  	if content.type == "thinking":
  		print("Thinking:", content.thinking)

  	if content.type == "text":
  		print("Response:", content.text)
  ```

  ```python PYTHON (Streaming) 
  from cohere import ClientV2

  co = ClientV2(api_key="<YOUR_API_KEY>")        

  prompt = """
  Alice has 3 brothers and she also has 2 sisters. How many sisters does Alice's brother have?
  """

  response = co.chat_stream(
      model="command-a-reasoning-08-2025",
      messages=[
          {
              "role": "user",
              "content": prompt,
          }
      ],
  )
  for event in response:
      if event.type == "content-delta":
          if event.delta.message.content.thinking:
              print(event.delta.message.content.thinking, end="")
          if event.delta.message.content.text:
              print(event.delta.message.content.text, end="")
  ```
</CodeBlocks>

**Customization Options**

You can enable and disable thinking capabilities using the `thinking` parameter, and steer the model's output with a flexible user-controlled thinking budget; for more details on token budgets, advanced configurations, and best practices, refer to our dedicated [Reasoning documentation](/docs/reasoning).


# Announcing Cohere's Command A Vision Model

> This announcement covers the release of Command A Vision, Cohere's first model able to understand and interpret image inputs.

We're excited to announce the release of **Command A Vision**, Cohere's first commercial model capable of understanding and interpreting visual data alongside text. This addition to our Command family brings enterprise-grade vision capabilities to your applications with the same familiar Command API interface.

## Key Features

### Multimodal Capabilities

* **Text + Image Processing**: Combine text prompts with image inputs
* **Enterprise-Focused Use Cases**: Optimized for business applications like document analysis, chart interpretation, and OCR
* **Multiple Languages**: Officially supports English, Portuguese, Italian, French, German, and Spanish

### Technical Specifications

* **Model Name**: `command-a-vision-07-2025`
* **Context Length**: 128K tokens
* **Maximum Output**: 8K tokens
* **Image Support**: Up to 20 images per request (or 20MB total)
* **API Endpoint**: Chat API

## What You Can Do

Command A Vision excels in enterprise use cases including:

* **📊 Chart & Graph Analysis**: Extract insights from complex visualizations
* **📋 Table Understanding**: Parse and interpret data tables within images
* **📄 Document OCR**: Optical character recognition with natural language processing
* **🌐 Image Processing for Multiple Languages**: Handle text in images across multiple languages
* **🔍 Scene Analysis**: Identify and describe objects within images

## 💻 Getting Started

The API structure is identical to our existing Command models, making integration straightforward:

```python
import cohere

co = cohere.Client("your-api-key")

response = co.chat(
    model="command-a-vision-07-2025",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Analyze this chart and extract the key data points",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "your-image-url"},
                },
            ],
        }
    ],
)
```

There's much more to be said about working with images, various limitations, and best practices, which you can find in our dedicated [Command A Vision](https://docs.cohere.com/docs/command-a-vision) and [Image Inputs](https://docs.cohere.com/docs/image-inputs) documents.


# Announcing Cutting-Edge Cohere Models on OCI

> This announcement covers the release of Command A, Rerank v3.5, and Embed v3.0 multimodal on Oracle Cloud Infrastructure's platform.

We are thrilled to announce that the Oracle Cloud Infrastructure (OCI) Generative AI service now supports Cohere Command A, Rerank v3.5, Embed v3.0 multimodal. This marks a major advancement in providing OCI's customers with enterprise-ready AI solutions.

Command A 03-2025 is the most performant Command model to date, delivering 150% of the throughput of its predecessor on only two GPUs.

Embed v3.0 is a cutting-edge AI search model enhanced with multimodal capabilities, allowing it to generate embeddings from both text and images.

Rerank 3.5, Cohere's newest AI search foundation model, is engineered to improve the precision of enterprise search and retrieval-augmented generation (RAG) systems across a wide range of data formats (such as lengthy documents, emails, tables, JSON, and code) and in over 100 languages.

Check out [Oracle's announcement](https://blogs.oracle.com/ai-and-datascience/post/cohere-command-a-rerank-oci-gen-ai) and [documentation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/pretrained-models.htm) for more details.


# Announcing Embed Multimodal v4

> Release of Embed Multimodal v4, a performant search model, with Matryoshka embeddings and a 128k context length.

We’re thrilled to announce the release of [Embed 4](https://docs.cohere.com/docs/cohere-embed), the most recent entrant into the Embed family of enterprise-focused [large language models](https://docs.cohere.com/docs/the-cohere-platform#large-language-models-llms) (LLMs).

Embed v4 is Cohere’s most performant search model to date, and supports the following new features:

1. Matryoshka Embeddings in the following dimensions: '\[256, 512, 1024, 1536]'
2. Unified Embeddings produced from mixed modality input (i.e. a single payload of image(s) and text(s))
3. Context length of 128k

Embed v4 achieves state of the art in the following areas:

1. Text-to-text retrieval
2. Text-to-image retrieval
3. Text-to-mixed modality retrieval (from e.g. PDFs)

Embed v4 is available today on the [Cohere Platform](https://docs.cohere.com/docs/the-cohere-platform), [AWS Sagemaker](https://docs.cohere.com/docs/amazon-sagemaker-setup-guide#embeddings), and [Azure AI Foundry](https://docs.cohere.com/docs/cohere-on-microsoft-azure#embeddings). For more information, check out our dedicated blog post [here](https://cohere.com/blog/embed-4).


# Announcing Command A

> Release of Command A, a performant model suited for tool use, RAG, agents, and multilingual uses, with 111 billion parameters and a 256k context length.

We're thrilled to announce the release of Command A, the most recent entrant into the Command family of enterprise-focused [large language models](https://docs.cohere.com/docs/the-cohere-platform#large-language-models-llms) (LLMs).

[Command A](https://docs.cohere.com/docs/command-a) is Cohere's most performant model to date, excelling at real world enterprise tasks including tool use, retrieval augmented generation (RAG), agents, and multilingual use cases. With 111B parameters and a context length of 256K, Command A boasts a considerable increase in inference-time efficiency -- 150% higher throughput compared to its predecessor Command R+ 08-2024 -- and only requires two GPUs (A100s / H100s) to run.

Command A is available today on the [Cohere Platform](https://docs.cohere.com/docs/the-cohere-platform), [HuggingFace](https://huggingface.co/CohereForAI/c4ai-command-a-03-2025), or through the SDK with `command-a-03-2025`. For more information, check out our [dedicated blog post](https://cohere.com/blog/command-a/).


# Our Groundbreaking Multimodal Model, Aya Vision, is Here!

> Release announcement for the new multimodal Aya Vision model 

Today, Cohere Labs, Cohere’s research arm, is proud to announce [Aya Vision](https://cohere.com/blog/aya-vision), a state-of-the-art multimodal large language model excelling across multiple languages and modalities. Aya Vision outperforms the leading open-weight models in critical benchmarks for language, text, and image capabilities.

built as a foundation for multilingual and multimodal communication, this groundbreaking AI model supports tasks such as image captioning, visual question answering, text generation, and translations from both texts and images into coherent text.

Find more information about Aya Vision [here](/docs/aya-multimodal).


# Cohere Releases Arabic-Optimized Command Model!

> Release announcement for the Command R7B Arabic model

Cohere is thrilled to announce the release of Command R7B Arabic (`c4ai-command-r7b-12-2024`). This is an open weights release of an advanced, 8-billion parameter custom model optimized for the Arabic language (MSA dialect), in addition to English. As with Cohere's other command models, this one comes with context length of 128,000 tokens; it excels at a number of critical enterprise tasks -- instruction following, length control, [retrieval-augmented generation (RAG)](https://docs.cohere.com/docs/retrieval-augmented-generation-rag), minimizing code-switching -- and it demonstrates excellent general purpose knowledge and understanding of the Arabic language and culture.

## Try Command R7B Arabic

If you want to try Command R7B Arabic, it's very easy: you can use it through the [Cohere playground](https://dashboard.cohere.com/playground/chat) or in our dedicated [Hugging Face Space](https://huggingface.co/spaces/CohereForAI/c4ai-command-r-plus).

Alternatively, you can use the model in your own code. To do that, first install the `transformers` library from its source repository:

```bash
pip install 'git+https://github.com/huggingface/transformers.git'
```

Then, use this Python snippet to run a simple text-generation task with the model:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "CohereForAI/c4ai-command-r7b-12-2024"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Format message with the c4ai-command-r7b-12-2024 chat template
messages = [{"role": "user", "content": "مرحبا، كيف حالك؟"}]
input_ids = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt",
)

gen_tokens = model.generate(
    input_ids,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.3,
)

gen_text = tokenizer.decode(gen_tokens[0])
print(gen_text)
```

## Chat Capabilities

Command R7B Arabic can be operated in two modes, "conversational" and "instruct" mode:

* *Conversational mode* conditions the model on interactive behaviour, meaning it is expected to reply in a conversational fashion, provide introductory statements and follow-up questions, and use Markdown as well as LaTeX where appropriate. This mode is optimized for interactive experiences, such as chatbots, where the model engages in dialogue.
* *Instruct mode* conditions the model to provide concise yet comprehensive responses, and to not use Markdown or LaTeX by default. This mode is designed for non-interactive, task-focused use cases such as extracting information, summarizing text, translation, and categorization.

<aside>
  Note: Command R7B Arabic is delivered without a system preamble by default, though we encourage you to experiment with the conversational and instruct mode preambles. More information can be [found in our docs](https://docs.cohere.com/docs/command-r7b-hf).
</aside>

## Multilingual RAG Capabilities

Command R7B Arabic has been trained specifically for Arabic and English tasks, such as the *generation* step of Retrieval Augmented Generation (RAG).

Command R7B Arabic's RAG functionality is supported through chat templates in Transformers. Using our RAG chat template, the model takes a conversation (with an optional user-supplied system preamble) and a list of document snippets as input. The resulting output contains a response with in-line citations. Here's what that looks like:

```python
# Define conversation input
conversation = [
    {
        "role": "user",
        "content": "اقترح طبقًا يمزج نكهات من عدة دول عربية",
    }
]

# Define documents for retrieval-based generation
documents = [
    {
        "heading": "المطبخ العربي: أطباقنا التقليدية",
        "body": "يشتهر المطبخ العربي بأطباقه الغنية والنكهات الفريدة. في هذا المقال، سنستكشف ...",
    },
    {
        "heading": "وصفة اليوم: مقلوبة",
        "body": "المقلوبة هي طبق فلسطيني تقليدي، يُحضر من الأرز واللحم أو الدجاج والخضروات. في وصفتنا اليوم ...",
    },
]

# Get the RAG prompt
input_prompt = tokenizer.apply_chat_template(
    conversation=conversation,
    documents=documents,
    tokenize=False,
    add_generation_prompt=True,
    return_tensors="pt",
)
# Tokenize the prompt
input_ids = tokenizer.encode_plus(input_prompt, return_tensors="pt")
```

You can then generate text from this input as normal.

## Notes on Usage

We recommend document snippets be short chunks (around 100-400 words per chunk) instead of long documents. They should also be formatted as key-value pairs, where the keys are short descriptive strings and the values are either text or semi-structured.

You may find that simply including relevant documents directly in a user message works as well as or better than using the `documents` parameter to render the special RAG template (though the template is a strong default for those wanting [citations](https://docs.cohere.com/docs/retrieval-augmented-generation-rag#citation-modes)). We encourage users to experiment with both approaches, and to evaluate which mode works best for their specific use case.


# Cohere via OpenAI SDK Using Compatibility API

> With the Compatibility API, you can use Cohere models via the OpenAI SDK without major refactoring.

Today, we are releasing our Compatibility API, enabling developers to seamlessly use Cohere's models via OpenAI's SDK.

This API enables you to switch your existing OpenAI-based applications to use Cohere's models without major refactoring.

It includes comprehensive support for chat completions, such as function calling and structured outputs, as well as support for text embeddings generation.

Check out [our documentation](https://docs.cohere.com/docs/compatibility-api) on how to get started with the Compatibility API, with examples in Python, TypeScript, and cURL.


# Cohere's Rerank v3.5 Model is on Azure AI Foundry!

> Release announcement for the ability to work with Cohere Rerank v3.5 models in the Azure's AI Foundry.

In December 2024, Cohere released [Rerank v3.5 model](https://docs.cohere.com/changelog/rerank-v3.5). It demonstrates SOTA performance on multilingual retrieval, reasoning, and tasks in domains as varied as finance, eCommerce, hospitality, project management, and email/messaging retrieval.

This model has been available through the Cohere API, but today we’re pleased to announce that it can also be utilized through Microsoft Azure's AI Foundry!

You can find more information about using Cohere’s embedding models on AI Foundry [here](https://docs.cohere.com/docs/cohere-on-microsoft-azure).


# Cohere's Rerank v3.5 Model is on Azure AI Foundry!

> Release announcement for the ability to work with Cohere Rerank v3.5 models in the Azure's AI Foundry.

In December 2024, Cohere released [Rerank v3.5 model](https://docs.cohere.com/changelog/rerank-v3.5). It demonstrates SOTA performance on multilingual retrieval, reasoning, and tasks in domains as varied as finance, eCommerce, hospitality, project management, and email/messaging retrieval.

This model has been available through the Cohere API, but today we’re pleased to announce that it can also be utilized through Microsoft Azure's AI Foundry!

You can find more information about using Cohere’s embedding models on AI Foundry [here](https://docs.cohere.com/docs/cohere-on-microsoft-azure).


# Deprecation of Classify via default Embed Models

> Usage of Classify endpoint via the default Embed models is now deprecated. Usage of Classify endpoint via a fine-tuned Embed model is not affected.

Effective January 31st, 2025, we are deprecating the use of default Embed models with the Classify endpoint.

This deprecation does not affect usage of the Classify endpoint with fine-tuned Embed models. Fine-tuned models continue to be fully supported and are recommended for achieving optimal classification performance.

For guidance on implementing Classify with fine-tuned models, please refer to our [Classify fine-tuning documentation](https://docs.cohere.com/docs/classify-fine-tuning).


# Cohere's Multimodal Embedding Models are on Bedrock!

> Release announcement for the ability to work with multimodal image models on the Amazon Bedrock platform.

In October, Cohere updated our embeddings models to be able to [process images](https://docs.cohere.com/v1/docs/embeddings#image-embeddings) in addition to text.

These enhanced models have been available through the Cohere API, but today we’re pleased to announce that they can also be utilized through the powerful Amazon Bedrock cloud computing platform!

You can find more information about using Cohere’s embedding models on Bedrock [here](https://docs.cohere.com/v1/docs/amazon-bedrock).


# Aya Expanse is Available on WhatsApp!

> Release announcement for the ability to chat with Aya Expanse on WhatsApp

[Aya](https://cohere.com/research/aya) Expanse is a multilingual large language model that is designed to expand the number of languages covered by generative AI. It is optimized to perform well in 23 languages, including Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Russian, Spanish, and more.

Now, you can talk to Aya Expanse directly in the popular messaging service WhatsApp! All of Aya's functionality is avaible through the app, and you can find more details [here](https://docs.cohere.com/docs/aya#aya-expanse-integration-with-whatsapp).


# Announcing Command R7b

> Release announcment for Command R 7B - our fastest, lightest, and last Command R model.

We're thrilled to announce the release of Command R7B, the smallest, fastest, and final model in our R family of enterprise-focused [large language models](https://docs.cohere.com/docs/the-cohere-platform#large-language-models-llms) (LLMs). With a context window of 128K, Command R7B offers state-of-the-art performance across a variety of real-world tasks, and is designed for use cases in which speed, cost, and compute are important. Specifically, Command R7B is excellent for [retrieval-augmented generation](https://docs.cohere.com/docs/retrieval-augmented-generation-rag), [tool use](https://docs.cohere.com/docs/tool-use), and [agentic applications](https://docs.cohere.com/docs/multi-step-tool-use) where complex reasoning, multiple actions, and information-seeking are important for success.

Command R7B is available today on the [Cohere Platform](https://docs.cohere.com/docs/the-cohere-platform) as well as accessible on HuggingFace, or you can access it in the SDK with `command-r7b-12-2024`. For more information, check out our [dedicated blog post](https://cohere.com/blog/command-r7b).


# Announcing Rerank-v3.5

> Release announcment for Rerank 3.5 - our new state of the art model for ranking.

We're pleased to announce the release of [Rerank 3.5](/docs/rerank) our newest and most performant foundational model for ranking. Rerank 3.5 has a context length of 4096, SOTA performance on Multilingual Retrieval tasks and Reasoning Capabilities. In addition, Rerank 3.5 has SOTA performance on BEIR and domains such as Finance, E-commerce, Hospitality, Project Management, and Email/Messaging Retrieval tasks.

In the rest of these release notes, we’ll provide more details about changes to the api.

## Technical Details

### API Changes:

Along with the model, we are releasing V2 of the Rerank API. It includes the following major changes:

* `model` is now a required parameter
* `max_chunks_per_doc` has been replaced by `max_tokens_per_doc`; `max_tokens_per_doc` will determine the maximum amount of tokens a document can have before truncation. The default value for `max_tokens_per_doc` is 4096.
* support for passing a list of objects for the `documents` parameter has been removed - if your documents contain structured data, for best performance we recommend formatting them as [YAML strings](/docs/rerank-overview#example-with-structured-data).

Example request

```Text cURL
POST https://api.cohere.ai/v2/rerank
{
    "model": "rerank-v3.5",
    "query": "What is the capital of the United States?",
    "top_n": 3,
    "documents": ["Carson City is the capital city of the American state of Nevada.",
                  "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
                  "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
                  "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
                  "Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states."]
}
```


# Structured Outputs support for tool use

> Structured Outputs now supports both JSON and tool use scenarios.

Today, we're pleased to announce that we have added Structured Outputs support for tool use in the Chat API.

In addition to supporting Structured Outputs with JSON generation via the `response_format` parameter, Structured Outputs will be available with Tools as well via the `strict_tools` parameter.

Setting `strict_tools` to `true` ensures that tool calls will follow the  provided tool schema exactly. This means the tool calls are guaranteed to adhere to the tool names, parameter names, parameter data types, and required parameters, without the risk of hallucinations.

See the [Structured Outputs documentation](https://docs.cohere.com/v2/docs/structured-outputs#structured-outputs-tools) to learn more.


# Embed v3.0 Models are now Multimodal

> Launch of multimodal embeddings for our Embed models, plus some code to help get started.

Today we’re announcing updates to our embed-v3.0 family of models. These models now have the ability to process images into embeddings. There is no change to existing text capabilities which means there is no need to re-embed texts you have already processed with our `embed-v3.0` models.

In the rest of these release notes, we’ll provide more details about technical enhancements, new features, and new pricing.

## Technical Details

### API Changes:

The Embed API has two major changes:

* Introduced a new `input_type` called `image`
* Introduced a new parameter called `images`

Example request on how to process

```Text cURL
POST https://api.cohere.ai/v1/embed
{
    "model": "embed-multilingual-v3.0",
    "input_type": "image",
    "embedding_types": ["float"],
    "images": [enc_img]
}
```

### Restrictions:

* The API only accepts images in the base format of the following: `png`, `jpeg`,`Webp`, and `gif`
* Image embeddings currently does not support batching so the max images sent per request is 1
* The maximum image sizez is `5mb`
* The `images` parameter only accepts a base64 encoded image formatted as a Data Url


# Fine-Tuning Now Available for Command R 08-2024

> Launch of fine-tuning for Command R 08-2024 and other new fine-tuning features.

Today, we're pleased to announce that fine-tuning is now available for [Command R 08-2024](/docs/command-r#command-r-august-2024-release)!

We're also introducing other chat fine-tuning features:

* Support for **16384 context lengths (up from 8192)** for fine-tuning training and MultiLoRA.
* Integration with Weights & Biases for tracking fine-tuning experiments in real time.

See the [Chat fine-tuning documentation](/docs/chat-fine-tuning) to learn more about creating a fine-tuned model.


# New Embed, Rerank, Chat, and Classify APIs

> Introducing improvements to our Chat, Classify, Embed, and Rerank APIs in a major version upgrade, making it easier and faster to build with Cohere.

We're excited to introduce improvements to our Chat, Classify, Embed, and Rerank APIs in a major version upgrade, making it easier and faster to build with Cohere. We are also releasing new versions of our Python, TypeScript, Java, and Go SDKs which feature `cohere.ClientV2` for access to the new API.

## New at a glance

* V2 Chat, Classify, Embed, and Rerank: `model` is a required parameter
* V2 Embed: `embedding_types` is a required parameter
* V2 Chat: Message and chat history are [combined](/v2/docs/migrating-v1-to-v2#messages-and-preamble) in a single `messages` array
* V2 Chat: [Tools](/v2/docs/parameter-types-in-tool-use) are defined in JSON schema
* V2 Chat: Introduces `tool_call_ids` to [match tool calls with tool results](/v2/docs/migrating-v1-to-v2#tool-call-id)
* V2 Chat: `documents` [supports a list of strings or a list of objects](/v2/docs/migrating-v1-to-v2#documents) with document metadata
* V2 Chat streaming: Uses [server-sent events](/v2/docs/migrating-v1-to-v2#streaming)

## Other updates

We are simplifying the Chat API by removing support for the following parameters available in V1:

* `search_queries_only`, which generates only a search query given a user’s message input. `search_queries_only` is not supported in the V2 Chat API today, but will be supported at a later date.
* `connectors`, which enables users to register a data source with Cohere for RAG queries. To use the Chat V2 API with web search, see our [migration guide](/v2/docs/migrating-v1-to-v2#) for instructios to implement a web search tool.
* `conversation_id`, used to manage chat history on behalf of the developer. This will not be supported in the V2 Chat API.
* `prompt_truncation`, used to automatically rerank and remove documents if the query did not fit in the model’s context limit. This will not be supported in the V2 Chat API.
* `force_single_step`, which forced the model to finish tool calling in one set of turns. This will not be supported in the V2 Chat API.
* `preamble`, used for giving the model task, context, and style instructions. Use a system turn at the beginning of your `messages` array in V2.
* `citation_quality`, for users to select between `fast` citations, `accurate` citations (slightly higher latency than fast), or citations `off`. In V2 Chat, we are introducing a top level `citation_options` parameter for all citation settings. `citation_quality` will be replaced by a `mode` parameter within `citation_options`.

See our Chat API [migration guide](/v2/docs/migrating-v1-to-v2) for detailed instructions to update your implementation.

These APIs are in Beta and are subject to updates. We welcome feedback in our [Discord](https://discord.com/invite/co-mmunity) channel.


# Refreshed Command R and R+ models now on Azure

> Introducing our improved Command models are available on the Azure cloud computing platform.

You'll recall that we [released refreshed models](https://docs.cohere.com/changelog/command-gets-refreshed) of Command R and Command R+ in August.

Today, we're pleased to announce that these models are available on the Azure cloud computing platform!

You can find more information about using Cohere's Command models on Azure [here](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-command?tabs=cohere-command-r-plus\&pivots=programming-language-python).


# Command models get an August refresh

> We're excited to announce updates to our Command R and R+ models, offering improved performance, new features, and more.

Today we’re announcing updates to our flagship generative AI model series: Command R and Command R+. These models demonstrate improved performance on a variety of tasks.

The latest model versions are designated with timestamps, as follows:

* The updated Command R is `command-r-08-2024` on the API.
* The updated Command R+ is `command-r-plus-08-2024` on the API.

In the rest of these release notes, we’ll provide more details about technical enhancements, new features, and new pricing.

## Technical Details

`command-r-08-2024` shows improved performance for multilingual retrieval-augmented generation (RAG) and tool use. More broadly, `command-r-08-2024` is better at math, code and reasoning and is competitive with the previous version of the larger Command R+ model.

`command-r-08-2024` delivers around 50% higher throughput and 20% lower latencies as compared to the previous Command R version, while cutting the hardware footprint required to serve the model by half. Similarly, `command-r-plus-08-2024` delivers roughly 50% higher throughput and 25% lower latencies as compared to the previous Command R+ version, while keeping the hardware footprint the same.

Both models include the following feature improvements:

* For tool use, `command-r-08-2024` and `command-r-plus-08-2024` have demonstrated improved decision-making around which tool to use in which context, and whether or not to use a tool.
* Improved instruction following in the preamble.
* Improved multilingual RAG searches in the language of the user with improved responses.
* Better structured data analysis for structured data manipulation.
* Better structured data creation from unstructured natural language instructions.
* Improved robustness to non-semantic prompt changes like white space or new lines.
* The models will decline unanswerable questions.
* The models have improved citation quality and users can now turn off citations for RAG workflows.
* For `command-r-08-2024` there are meaningful improvements on length and formatting control.

## New Feature: Safety Modes

The primary new feature available in both `command-r-08-2024` and `command-r-plus-08-2024` is Safety Modes (in beta). For our enterprise customers building with our models, what is considered safe depends on their use case and the context the model is deployed in. To support diverse enterprise applications, we have developed safety modes, acknowledging that safety and appropriateness are context-dependent, and that predictability and control are critical in building confidence in Cohere models.

Safety guardrails have traditionally been reactive and binary, and we’ve observed that users often have difficulty defining what safe usage means to them for their use case. Safety Modes introduce a nuanced approach that is context sensitive.

(Note: Command R/R+ have built-in protections against core harms, such as content that endangers child safety. These types of harm are always blocked and cannot be adjusted.)

Safety modes are activated through a `safety_mode` parameter, which can (currently) be in one of two modes:

* `"STRICT"`: Encourages avoidance of all sensitive topics. Strict content guardrails provide an extra safe experience by prohibiting inappropriate responses or recommendations. Ideal for general and enterprise use.
* `"CONTEXTUAL"`: (enabled by default): For wide-ranging interactions with fewer constraints on output while maintaining core protections. The model responds as instructed while still rejecting harmful or illegal suggestions. Well-suited for entertainment, creative, educational use.

You can also opt out of the safety modes beta by setting `safety_mode="NONE"`. For more information, check out our dedicated guide to [Safety Modes](https://docs.cohere.com/docs/safety-modes).

## Pricing

Here’s a breakdown the pricing structure for the new models:

* For `command-r-plus-08-2024`, input tokens are priced at \$2.50/M and output tokens at \$10.00/M.
* For `command-r-08-2024`, input tokens are priced at \$0.15/M and output tokens at \$0.60/M.


# Force JSON object response format

> Generate outputs in JSON objects with the new 'response_format' parameter, now available with the 'command-nightly' model.

Users can now force `command-nightly`to generate outputs in JSON objects by setting the `response_format` parameter in the Chat API. Users can also specify a JSON schema for the output.

This feature is available across all of Cohere's SDKs (Python, Typescript, Java, Go).

Example request for forcing JSON response format:

```Text cURL
POST https://api.cohere.ai/v1/chat
{
    "message": "Generate a JSON that represents a person, with name and age",
    "model": "command-nightly",
    "response_format": {
        "type": "json_object"
    }
}
```

<br />

Example request for forcing JSON response format in user defined schema:

```Text cURL
POST https://api.cohere.ai/v1/chat
{
    "message": "Generate a JSON that represents a person, with name and age",
    "model": "command-nightly",
    "response_format": {
        "type": "json_object",
        "schema": {
            "type": "object",
            "required": ["name", "age"],
            "properties": {
                "name": { "type": "string" },
                "age": { "type": "integer" }
            }
        }
    }
}

```

Currently only compatible with \`command-nightly model.


# Release Notes for June 10th 2024

> Get started with multi-step tool use, explore new docs, and learn about billing changes in Cohere's Chat API.

## Multi-step tool use now default in Chat API

Tool use is a technique which allows developers to connect Cohere's Command family of models to external tools like search engines, APIs, functions, databases, etc. It comes in two variants, single-step and [multi-step](/docs/multi-step-tool-use), both of which are available through Cohere's Chat API.

As of today, tool use will now be multi-step by default. Here are some resources to help you get started:

* Check out our [multi-step tool use guide](/docs/multi-step-tool-use).
* Experiment with multi-step tool use with [this notebook](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/Tool_Use.ipynb).

## We've published additional docs!

Cohere's models and functionality are always improving, and we've recently dropped the following guides to help you make full use of our offering:

* [Predictable outputs](/docs/predictable-outputs) - Information about the `seed` parameter has been added, giving you more control over the predictability of the text generated by Cohere models.
* [Using Cohere SDKs with private cloud models](/docs/cohere-works-everywhere) - To maximize convenience in building on and switching between Cohere-supported environments, our SDKs have been developed to allow seamless support of whichever cloud backend you choose. This guide walks you through when you can use Python, Typescript, Go, and Java on Amazon Bedrock, Amazon SageMaker, Azure, and OCI, what features and parameters are supported, etc.

## Changes to Billing

Going forward, Cohere is implementing the following two billing policies:

* When a user accrues \$150 of outstanding debts, a warning email will be sent alerting them of upcoming charges.
* When a self-serve customer (i.e. a non-contracted organization with a credit card on file) accumulates \$250 in outstanding debts, a charge will be forced via Stripe.


# Advanced Retrieval Launch release

> Rerank 3 offers improved performance and inference speed for long and short documents with a context length of 4096.

We're pleased to announce the release of [Rerank 3](/docs/rerank) our newest and most performant foundational model for ranking. Rerank 3 boast a context length of 4096, SOTA performance on Code Retrieval, Long Document, and Semi-Structured Data. In addition to quality improvements, we've improved inference speed by a factor of 2x for short documents (doc length \< 512 tokens) and 3x for long documents (doc length \~4096 tokens).


# Cohere Python SDK v5.2.0 release

> Stay up to date with our Python SDK update, including local tokenizer defaults and new required fields.

We've released an additional update for our Python SDK! Here are the highlights.

* The tokenize and detokenize functions in the Python SDK now default to using a *local* tokenizer.
* When using the local tokenizer, the response will not include `token_strings`, but users can revert to using the hosted tokenizer by specifying `offline=False`.
* Also, `model` will now be a required field.
* For more information, see the guide for [tokens and tokenizers](/docs/tokens-and-tokenizers).

<br />


# Command R: Retrieval-Augmented Generation at Scale

> Command R: Retrieval Augmented Generation at scale.

Today, we are introducing Command R, a new LLM aimed at large-scale production workloads. Command R targets the emerging “scalable” category of models that balance high efficiency with strong accuracy, enabling companies to move beyond proof of concept, and into production.

Command R is a generative model optimized for long context tasks such as retrieval-augmented generation (RAG) and using external APIs and tools. It is designed to work in concert with our industry-leading Embed and Rerank models to provide best-in-class integration for RAG applications and excel at enterprise use cases. As a model built for companies to implement at scale, Command R boasts:

* Strong accuracy on RAG and Tool Use
* Low latency, and high throughput
* Longer 128k context and lower pricing
* Strong capabilities across 10 key languages
* Model weights available on HuggingFace for research and evaluation

For more information, check out the [official blog post](https://cohere.com/blog/command-r/) or the [Command R documentation](/docs/command-r).


# Fine-tuning has been added to the Python SDK

> Stay up-to-date with Cohere's Python SDK by checking out the new `fine_tuning` feature and its functions.

In place of `custom_models`, `fine_tuning` has been added to the Python SDK. See this Python [github repository](https://github.com/cohere-ai/cohere-python/tree/main/src/cohere/finetuning) for the full list of supported functions!


# Cohere Python SDK v5.0.0 release

> Stay up-to-date with our latest Python SDK release and learn about deprecated functions and migration instructions.

With the release of our latest Python SDK, there are a number of functions that are no longer supported, including `create_custom_models`.

For more granular instructions on upgrading to the new SDK, and what that will mean for your Cohere integrations, see the comprehensive [migration guide](https://github.com/cohere-ai/cohere-python/blob/main/4.0.0-5.0.0-migration-guide.md).


# Release Notes January 22, 2024

> Discover new AI capabilities with Cohere's latest features, including improved fine-tuning, Embed Jobs API, and multi-language SDK support.

## Apply Cohere's AI with Connectors!

One of the most exciting applications of generative AI is known as ["retrieval augmented generation"](/docs/retrieval-augmented-generation-rag) (RAG). This refers to the practice of *grounding* the outputs of a large language model (LLM) by offering it resources -- like your internal technical documentation, chat logs, etc. -- from which to draw as it formulates its replies.

Cohere has made it much easier to utilize RAG in bespoke applications via [Connectors](/docs/overview-rag-connectors). As the name implies, Connectors allow you to *connect* Cohere's generative AI platform up to whatever resources you'd like it to ground on, facilitating the creation of a wide variety of applications -- customer service chatbots, internal tutors, or whatever else you want to build.

Our docs cover how to [create and deploy connectors](/v1/docs/creating-and-deploying-a-connector), [how to manage your connectors ](/docs/managing-your-connector), [how to handle authentication](/docs/connector-authentication), and [more](/docs/connector-faqs)!

## Expanded Fine-tuning Functionality

Cohere's ready-to-use LLMs, such as Command, are very good at producing responses to natural language prompts. However, there are many cases in which getting the best model performance requires performing an additional round of training on custom user data. This is process known as fine-tuning, and we've dramatically revamped our [fine-tuning documentation](/docs/fine-tuning).

The new docs are organized according to the major endpoints, and we support fine-tuning for [Generate](/docs/generate-fine-tuning), [Classify](/docs/classify-fine-tuning), [Rerank](/docs/rerank-fine-tuning), and [Chat](/docs/chat-fine-tuning).

But wait, there's more: many developers work with generative AI through popular cloud-compute platforms like Amazon Web Services (AWS), and we support [fine-tuning on AWS Bedrock](/docs/fine-tuning-cohere-models-on-amazon-bedrock). We also support fine-tuning with Sagemaker, and the relevant documentation will be published in the coming weeks.

## A new Embed Jobs API Endpoint Has Been Released

The [Embed Jobs API](/docs/embed-jobs-api) was designed for users who want to leverage the power of retrieval over large corpuses of information. Encoding a large volume of documents with an API can be tedious and difficult, but the Embed Jobs API makes it a breeze to handle encoding workflows involving 100,000 documents, or more!

The API works in conjunction with `co.embed()`. For more information, [consult the docs](/docs/embed-jobs-api).

## Our SDK now Supports More Languages

Throughout our documentation you'll find code-snippets for performing common tasks with Python. Recently, we made the decision to expand these code snippets to include Typescript and Go, and are working to include several other popular languages as well.


# Release Notes September 29th 2023

> Experience the future of generative AI with co.chat() and explore the power of retrieval-augmented generation for grounded and timely outputs.

**We're Releasing co.chat() and the Chat + RAG Playground**

We're pleased to announce that we've released our `co.chat()` beta! Of particular importance is the fact that the `co.chat()` API is able to utilize [retrieval augmented generation](/docs/retrieval-augmented-generation-rag) (RAG), meaning developers can provide sources of context that inform and ground the model's output.

This represents a leap forward in the accuracy, verifiability, and timeliness of our generative AI offering. For our public beta, developers can connect `co.chat()` to web search or plain text documents.

Access to the `co.chat()` public beta is available through an API key included with a Cohere account.

**Our Command Model has Been Updated**

We've updated both the `command` and `command-light` models. Expect improved question answering, generation quality, rewriting and conversational capabilities.

**New Rate Limits**

For all trial keys and all endpoints, there is now a rate limit of 5000 calls per month.


# Release Notes August 8th 2023 (Changelog)

> Unlock improved reasoning and conversation with Command R+, now featuring Okta OIDC support and an enhanced finetuning SDK.

**Command Model Updated**
The Command model has been updated. Expect improvements in reasoning and conversational capabilities.

**Finetuning SDK**
Programmatic finetuning via the Cohere SDK has been released. Full support for the existing finetuning capabilites along with added capabilities such as configuring hyperparameters. [Learn more here.](/docs/fine-tuning-with-the-python-sdk)

**Okta OIDC Support**
We've introduced support for Okta SSO leveraging the OIDC protocol. If you are interested in support for your account, please reach out to [support@cohere.com](mailto:support@cohere.com) directly.


# Release Notes June 28th 2023 (Changelog)

> The latest Command model update brings enhanced code, conversation, and reasoning, along with new API features and usage/billing improvements.

**Command Model Updated**\
The Command model has been updated. Expect improved code and conversational capabilities, as well as reasoning skills on various tasks.

**Co.rerank()**\
`co.rerank()`, a new API that sorts a list of text inputs by semantic relevance to a query. [Learn more here.](/reference/rerank-1)

**Streaming Now Part of Generate API**\
Token streaming is now supported via the Co.generate() api. [Learn more here](/reference/generate).

**Usage and Billing Table Improvements**\
The usage and billing table in the Cohere dashboard now has filtering and sorting capabilities. [See here.](https://dashboard.cohere.com/welcome/login?redirect_uri=%2Fbilling)


# New Maximum Number of Input Documents for Rerank

> Stay up to date with our latest changes to co.rerank, now with an improved maximum document limit.

We have updated how the maximum number of documents is calculated for co.rerank. The endpoint will error if `len(documents) * max_chunks_per_doc >10,000` where `max_chunks_per_doc` is set to 10 as default.


# Cohere Model Names Are Changing!

> We've updated our model names for simplicity and consistency, and old names will work for now.

We are updating the names of our models to bring consistency and simplicity to our product offerings. As of today, you will be able to call Cohere’s models via our API and SDK with the new model names, and all of our documentation has been updated to reflect the new naming convention.

These changes are backwards compatible, so you can also continue to call our models with the **Previous Names** found in the table below until further notice.

| Model Type | Previous Name          | New Name                 | Endpoint    |
| ---------- | ---------------------- | ------------------------ | ----------- |
| Generative | command-xlarge         | command                  | co.generate |
| Generative | command-medium         | command-light            | co.generate |
| Generative | command-xlarge-nightly | command-nightly          | co.generate |
| Generative | command-medium-nightly | command-light-nightly    | co.generate |
| Generative | xlarge                 | base                     | co.generate |
| Generative | medium                 | base-light               | co.generate |
| Embeddings | large                  | embed-english-v2.0       | co.embed    |
| Embeddings | small                  | embed-english-light-v2.0 | co.embed    |
| Embeddings | multilingual-22-12     | embed-multilingual-v2.0  | co.embed    |

See the latest information about our models here: [/docs/models](/docs/models)

If you experience any issues in accessing our models, please reach out to [support@cohere.com](mailto:support@cohere.com).


# Multilingual Support for Co.classify

> The co.classify endpoint now supports multilingual capabilities with the new multilingual-22-12 model.

The co.classify endpoint now supports the use of Cohere's multilingual embedding model. The `multilingual-22-12 model` is now a valid model input in the co.classify call.


# Command Model Nightly Available!

> Get improved performance with our new nightly versions of Command models, now available in medium and x-large sizes.

Nightly versions of our Common models are now available. This means that every week, you can expect the performance of command-nightly to improve as we continually retrain them.

Command-nightly will be available in two sizes - `medium` and `xlarge`. The `xlarge` model demonstrates better performance, and medium is a great option for developers who require fast response, like those building chatbots. You can find more information [here](/docs/command-beta).

If you were previously using the `command-xlarge-20221108` model, you will now be redirected to the `command-xlarge-nightly` model. Please note that access to the `command-xlarge-20221108` model will be discontinued after January 30, 2023. The `command-xlarge-nightly` model has shown enhancements in all generative tasks, and we anticipate you will notice an improvement.


# Command R+ is a scalable LLM for business

> Explore Command R+, Cohere's powerful language model, excelling in multi-step tool use and complex conversational AI tasks.

We're pleased to announce the release of [Command R+](/docs/command-r-plus), our newest and most performant large language model. Command R+ is optimized for conversational interaction and long-context tasks, and it is the recommended model for use cases requiring high performance and accuracy.

Command R+ has been trained on a massive corpus of diverse texts in multiple languages, and can perform a wide array of text-generation tasks. You'll find it especially strong for complex RAG functionality, as well as workflows that lean on multi-step tool use to build agents.

### Multi-step Tool Use

Speaking of [multi-step tool use](/docs/multi-step-tool-use), this functionality is now available for Command R+ models.

Multi-step tool use allows the model to call any number of tools in any sequence of steps, using the results from one tool call in a subsequent step until it has found a solution to a user's problem. This process allows the model to reason, perform dynamic actions, and quickly adapt on the basis of information coming from external sources.


# Multilingual Text Model + Language Detection

> Cohere's multilingual model now supports semantic search across 100 languages with a single index.

**\[NOTE: `co.detect_language()` is deprecated.]**

Cohere's multilingual text understanding model is now available! The `multilingual-22-12` model can be used to semantically search within a single language, as well as across languages. Compared to keyword search, where you often need separate tokenizers and indices to handle different languages, the deployment of the multilingual model for search is trivial: no language-specific handling is needed — everything can be done by a single model within a single index.

In addition to our new model, you can now detect the language of a data source using `co.detect_language()` endpoint.

For more information, see our [multilingual docs](/docs/multilingual-language-models).


# Model Sizing Update + Improvements

> We're updating our generative AI models to offer improved Medium and X-Large options.

Effective December 2, 2022, we will be consolidating our generative models and only serving our Medium (focused on speed) and X-Large (focused on quality). We will also be discontinuing support for our Medium embedding model.

This means that as of this date, our Small and Large generative models and Medium embedding model will be deprecated.

If you are currently using a Small or Large generative model, then we recommend that you proactively change to a Medium or X-Large model before December 2, 2022. Additionally, if you are currently using a Medium embed model, we recommend that you change to a Small embed model.

Calls to Generate large-20220926 and xlarge-20220609 will route to the new and improved X-Large model (xlarge-20221108). Calls to Generate small-20220926 will route to the new and improved Medium model (medium-20221108).

If you have any questions or concerns about this change, please don’t hesitate to contact us at: [team@cohere.com](mailto:team@cohere.com).


# Current Model Upgrades + New Command Beta Model

> Introducing new and improved Medium and XLarge models, plus a Command model for precise responses to commands.

**New & Improved Medium & Extremely Large**

The new and improved `medium` and `x-large` outperform our existing generation models on most downstream tasks, including summarization, paraphrasing, classification, and extraction, as measured by our internal task-based benchmarks.\
At this time, all baseline calls to `x-large` and `medium` will still route to previous versions of the models (namely, xlarge-20220609 and  medium-20220926). To access the new and improved versions, you’ll need to specify the release date in the Playground or your API call: `xlarge-20221108` and `medium-20221108`.

Older versions of the models (xlarge-20220609 & medium-20220926) will be deprecated on December 2, 2022.

**NEW Command Model (Beta)**

We’re also introducing a Beta of our new Command model, a generative model that’s conditioned to respond well to single-statement commands. Learn more about how to prompt `command-xlarge-20221108`. You can expect to see `command-xlarge-20221108` evolve dramatically in performance over the coming weeks.


# New Look For Cohere Documentation!

> Explore our updated docs with interactive tutorials, improved info architecture, and a UI refresh for a streamlined experience.

We've updated our docs to better suit our new developer journey! You'll have a sleeker, more streamlined documentation experience.

## New Features

* Interactive quickstart tutorials!
* Improved information architecture!
* UI refresh!

Try out the new experience, and let us know what you think.


# Co.classify uses Representational model embeddings

> Improve few-shot classification with Co.classify and embeddings from our Representational model.

The Co.classify endpoint now serves few-shot classification tasks using embeddings from our Representational model for the small, medium, and large default models.


# New Logit Bias experimental parameter

> Take control of your generative models with the new logit_bias parameter to guide token generation.

Our Generative models have now the option to use the new logit\_bias parameter to prevent the model from generating unwanted tokens or to incentivize it to include desired tokens. Logit bias is supported in all our default Generative models.


# Pricing Update and New Dashboard UI

> Unlock new features, including production keys, flat-rate pricing, improved UI, and enhanced team collaboration and model insights.

* Free, rate limited Trial Keys for experimentation, testing, and playground usage
* Production keys with no rate limit for serving Cohere in production applications
* Flat rate [pricing ](https://cohere.ai/pricing)for Generate and Embed endpoints
* Reduced pricing for Classify endpoint
* New UI for dashboard including sign up and onboarding - everything except playground
* New use-case specific Quickstart Guides to learn about using Cohere API
* Replacing "Finetune" nomenclature with "Custom Model"
* Inviting team members is now more intuitive. Teams enable users to share custom models with each other
* Generative custom models now show accuracy and loss metrics alongside logs
* Embed and Classify custom models now show logs alongside accuracy, loss, precision, f1, recall
* Custom model details now show number of each label in dataset


# Introducing Moderate Tool (Beta)!

> Access cutting-edge natural language processing tools without the need for costly supercomputing power.

Use Moderate (Beta) to classify harmful text across the following categories: `profane`, `hate speech`, `violence`, `self-harm`, `sexual`, `sexual (non-consenual)`, `harassment`, `spam`, `information hazard (e.g., pii)`. Moderate returns an array containing each category and its associated confidence score. Over the coming weeks, expect performance to improve significantly as we optimize the underlying model.


# The `model` Parameter Becomes Optional.

> Our APIs are now model-agnostic with default endpoint settings, offering greater flexibility and control for users.

Our APIs no longer require a model to be specified. Each endpoint comes with great defaults. For more control, a model can still be specified by adding a model param in the request.


# New & Improved Generation and Representation Models

> Enhance your text generation and representation with improved models, now offering better context support and optimal performance.

We've retrained our `small`, `medium`, and `large` generation and representation models. Updated representation models now support contexts up to 4096 tokens (previously 1024 tokens). We recommend keeping text lengths below 512 tokens for optimal performance; for any text longer than 512 tokens, the text is spliced and the resulting embeddings of each component are then averaged and returned.


# New and Improved Extremely Large Model!

> We're thrilled to introduce our enhanced `xlarge` model, now with superior generation quality and speed.

Our new and improved `xlarge` has better generation quality and a 4x faster prediction speed. This model now supports a maximum token length of 2048 tokens and frequency and presence penalties.


# Updated Small, Medium, and Large Generation Models

> The latest updates improve model stability and fix a bug for more effective generation presence and frequency penalties.

Updated `small`, `medium`, and `large` models are more stable and resilient against abnormal inputs due to a FP16 quantization fix. We also fixed a bug in generation presence & frequency penalty, which will result in more effective penalties.


# Introducing Classification Endpoint

> Classify text with Cohere's new classification endpoint, powered by generation models, offering few-shot learning.

Classification is now available via our classification endpoint. This endpoint is currently powered by our generation models (`small` and `medium`) and supports few-shot classification. We will be deprecating support for Choose Best by May 18th. To learn more about classification at Cohere check out the docs [here](/classify-reference).


# Finetuning Available + Policy Updates

> Fine-tune models with your own data and leverage updated policies for powerful NLP solutions.

**Finetuning is Generally Available**

You no longer need to wait for Full Access approval to build your own custom finetuned generation or representation model. Upload your dataset and start seeing even better performance for your specific task.

**Policy Updates**

The Cohere team continues to be focused on improving our products and features to enable our customers to build powerful NLP solutions. To help reflect some of the changes in our product development and research process, we have updated our [Terms of Use](https://cohere.ai/terms-of-use), [Privacy Policy](https://cohere.ai/privacy), and click-through [SaaS Agreement](https://cohere.ai/saas-agreement). Please carefully read and review these updates. By continuing to use Cohere’s services, you acknowledge that you have read, understood, and consent to all of the changes. If you have any questions or concerns about these updates, please contact us at [support@cohere.ai](mailto:support@cohere.ai).


# New & Improved Generation Models

> Try our new small, medium, and large generation models with improved performance from our high-quality dataset.

We’ve shipped updated `small`, `medium`, and `large` generation models. You’ll find significant improvements in performance that come from our newly assembled high quality dataset.


# Extremely Large (Beta) Release

> Take your NLP tasks further with our new top-tier model, Extremely Large (Beta), now available.

Our biggest and most performant generation model is now available. `Extremely Large (Beta)` outperforms our previous `large` model on a variety of downstream tasks including sentiment analysis, named entity recognition (NER) and common sense reasoning, as measured by our internal benchmarks. You can access `Extremely Large (Beta)` as `xlarge-20220301`. While in Beta, note that this model will have a maximum token length of 1024 tokens and maximum `num_generations` of 1.


# Larger Cohere Representation Models

> New Representation Model sizes and an increased token limit offer improved performance and flexibility.

Representation Models are now available in the sizes of `medium-20220217` and `large-20220217` as well as an updated version of `small-20220217`. Our previous `small` model will be available as `small-20211115`. In addition, the maximum tokens length per text has increased from 512 to 1024. We recommend keeping text lengths below 128 tokens for optimal performance; for any text longer than 128 tokens, the text is spliced and the resulting embeddings of each component are then averaged and returned.


# Cookbooks

> Explore a range of AI guides and get started with Cohere's generative platform, ready-made and best-practice optimized.

export const marco = {
  name: "Marco Del Tredici",
  imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/f103c96-Marco.jpg",
};

export const shaan = {
  name: "Shaan Desai",
  imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/d17fc44-Shaan.jpg",
};

export const jason = {
  name: "Jason Jung",
  imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/0803e3d-Jason_Jung.jpg",
};

export const ania = {
  name: "Ania Bialas",
  imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/c5dc5a3-Ania.jpg",
};

export const aal = {
  name: "Aal Patankar",
  imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/d48e622-Aal.jpg",
};

export const alex = {
  name: "Alex Barbet",
  imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/bf2c763-Alex.jpg",
};

export const giannis = {
  name: "Giannis Chatziveroglou",
  imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/73153cb-giannis.jpeg",
};

export const komal = {
  name: "Komal Teru",
  imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/7026fcc-komal-headshot.jpg"
}

export const youran = {
  name: "Youran Qi",
  imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/929cb1c-youran-headshot.jpg"
}

export const mike = {
  name: "Mike Mao",
  imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/d514b09-mike-headshot.jpg"
}

export const agentCards = [
  {
    title: "Calendar Agent with Native Multi Step Tool",
    description:
      "A minimal working example of how to use our chat API to call tools.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/5523913-Community_Demo_1.png",
    tags: ["agents"],
    href: "/page/calendar-agent",
  },
  {
    title: "Basic Tool Use",
    description:
      "Connect large language models to external tools, like search engines, APIs, and databases, to access and utilise a wider range of data.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/bad278b-Community_Demo_2.png",
    tags: ["agents"],
    href: "/page/basic-tool-use",
  },
  {
    title: "Multi-Step Tool Use",
    description:
      "Multi-step tool use allows developers to connect Cohere's models to external tools like search engines, APIs, and databases.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/8b24122-Community_Demo_3.png",
    tags: ["agents", "oss"],
    href: "/page/basic-multi-step",
  },
  {
    title: "A Data Analyst Agent Built with Cohere and Langchain",
    description:
      "Build a data analyst agent with Python and Cohere's Command R+ mode and Langchain.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/86191a6-Community_Demo_5.png",
    tags: ["agents", "oss"],
    href: "/page/data-analyst-agent",
  },
  {
    title: "Short-Term Memory Handling for Agents",
    description:
      "A walkthrough of how to use Langchain cohere_react_agent to effectively manage short-term chat history that contains tool calls with Langchain.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/d86be24-Community_Demo_6.png",
    tags: ["agents"],
    href: "/page/agent-short-term-memory",
    authors: [marco],
  },
  {
    title: "Agent API Calls",
    description:
      "A walkthrough of how to use Langchain cohere_react_agent to make API calls to external services that require regex.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/083d9e2-Community_Demo_7.png",
    tags: ["agents"],
    href: "/page/agent-api-calls",
    authors: [marco],
  },
  {
    title: "Financial CSV Agent with Langchain",
    description:
      "The notebook demonstrates how to setup a Langchain Cohere ReAct Agent to answer questions over the income statement and balance sheet from Apple's SEC10K 2020 form.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/13cb578-Community_Demo_8.png",
    tags: ["agents", "oss"],
    href: "/page/csv-agent",
    authors: [shaan],
  },
  {
    title: "Agentic RAG for PDFs with mixed data",
    description:
      "A walkthrough of how to use Langchain cohere_react_agent to run RAG as an agent tool to handle PDFs with mixed table and text data.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/142e385-Community_Demo_9.png",
    tags: ["agents"],
    href: "/page/agentic-rag-mixed-data",
    authors: [shaan],
  },
  {
    title: "SQL Agent",
    description:
      "In this notebook we explore how to setup a Cohere ReAct Agent to answer questions over SQL Databases using Langchain's SQLDBToolkit.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/5523913-Community_Demo_1.png",
    tags: ["agents"],
    href: "/page/sql-agent",
    authors: [shaan],
  },
  {
    title: "SQL Agent with Cohere and LangChain (i-5O Case Study)",
    description:
      "Build a SQL agent with Cohere and LangChain in the manufacturing industry.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/bad278b-Community_Demo_2.png",
    tags: ["agents"],
    href: "/page/sql-agent-cohere-langchain",
  },
  {
    title: "Financial CSV Agent with Native Multi-Step Cohere API",
    description:
      "This notebook demonstrates how to setup a Cohere Native API sequence of tool calls to answer questions over the income statement and balance sheet from Apple's SEC10K 2020 form.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/bad278b-Community_Demo_2.png",
    tags: ["agents"],
    href: "/page/csv-agent-native-api",
    authors: [jason],
  },
  {
    title: "PDF Extractor with Native Multi Step Tool Use",
    description: "How we can leverage agents to extract information from PDFs?",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/28ee583-Community_Demo_4.png",
    tags: ["agents"],
    href: "/page/pdf-extractor",
    authors: [jason],
  },
  {
    title: "Agentic Multi-Stage RAG with Cohere Tools API",
    description: "How to use Agents to improve RAG performance.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/86191a6-Community_Demo_5.png",
    tags: ["agents"],
    href: "/page/agentic-multi-stage-rag",
    authors: [jason],
  },
];

export const ossCards = [
  {
    title: "Multi-Step Tool Use",
    description:
      "Multi-step tool use allows developers to connect Cohere's models to external tools like search engines, APIs, and databases.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/8b24122-Community_Demo_3.png",
    tags: ["agents", "oss"],
    href: "/page/basic-multi-step",
  },
  {
    title: "A Data Analyst Agent Built with Cohere and Langchain",
    description:
      "Build a data analyst agent with Python and Cohere's Command R+ mode and Langchain.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/86191a6-Community_Demo_5.png",
    tags: ["agents", "oss"],
    href: "/page/data-analyst-agent",
  },
  {
    title: "Financial CSV Agent with Langchain",
    description:
      "The notebook demonstrates how to setup a Langchain Cohere ReAct Agent to answer questions over the income statement and balance sheet from Apple's SEC10K 2020 form.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/13cb578-Community_Demo_8.png",
    tags: ["agents", "oss"],
    href: "/page/csv-agent",
    authors: [shaan],
  },
  {
    title: "Multilingual Search with Cohere and Langchain",
    description: "Multilingual search with Cohere and Langchain.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/d86be24-Community_Demo_6.png",
    tags: ["search", "oss"],
    href: "/page/multilingual-search",
  },
  {
    title: "Creating a QA Bot From Technical Documentation",
    description:
      "Create a chatbot that answers user questions based on technical documentation using Cohere embeddings and LlamaIndex.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/28ee583-Community_Demo_4.png",
    tags: ["oss", "search", "rag"],
    href: "/page/creating-a-qa-bot",
  },
  {
    title: "Migrating away from deprecated create_csv_agent in langchain-cohere",
    description:
      "This page contains a tutorial on how to build a CSV agent without the deprecated `create_csv_agent` abstraction in langchain-cohere v0.3.5 and beyond.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/13cb578-Community_Demo_8.png",
    tags: ["agents", "oss", "csv"],
    href: "/page/migrate-csv-agent",
  },
];

export const searchCards = [
  {
    title: "Wikipedia Semantic Search with Cohere Embedding Archives",
    description:
      "Find relevant Wikipedia passages with semantic search and Cohere embeddings.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/083d9e2-Community_Demo_7.png",
    tags: ["search"],
    href: "/page/wikipedia-semantic-search",
  },
  {
    title:
      "Semantic Search with Cohere Embed Jobs and Pinecone serverless Solution",
    description:
      "Learn how to use Cohere's Embed Jobs and Pinecone's serverless solution to perform semantic search.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/13cb578-Community_Demo_8.png",
    tags: ["cloud", "search"],
    href: "/page/embed-jobs-serverless-pinecone",
  },
  {
    title: "End-to-end RAG using Elasticsearch and Cohere",
    description:
      "Learn how to use Cohere and Elastic for semantic search and retrieval-augmented generation.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/5523913-Community_Demo_1.png",
    tags: ["search", "rag", "cloud"],
    href: "/page/elasticsearch-and-cohere",
  },
  {
    title: "Semantic Search with Cohere Embed Jobs",
    description:
      "Learn how to use Cohere Embed Jobs to create semantic search functionality.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/bad278b-Community_Demo_2.png",
    tags: ["search"],
    href: "/page/embed-jobs",
  },
  {
    title: "Basic Semantic Search",
    description:
      "Learn how to build a simple semantic search engine using sentence embeddings.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/bad278b-Community_Demo_2.png",
    tags: ["search"],
    href: "/page/basic-semantic-search",
  },
  {
    title: "Multilingual Search with Cohere and Langchain",
    description: "Multilingual search with Cohere and Langchain.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/d86be24-Community_Demo_6.png",
    tags: ["search", "oss"],
    href: "/page/multilingual-search",
  },
  {
    title: "Wikipedia Semantic Search with Cohere + Weaviate",
    description:
      "Search 10 million Wikipedia vectors with Cohere's multilingual model and Weaviate's public dataset.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/5523913-Community_Demo_1.png",
    tags: ["search"],
    href: "/page/wikipedia-search-with-weaviate",
  },
  {
    title: "Creating a QA Bot From Technical Documentation",
    description:
      "Create a chatbot that answers user questions based on technical documentation using Cohere embeddings and LlamaIndex.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/28ee583-Community_Demo_4.png",
    tags: ["oss", "search", "rag"],
    href: "/page/creating-a-qa-bot",
  },
  {
    title: "Demo of Rerank",
    description:
      "Improve search results with Cohere's Relevance Endpoint, which reranks documents for better accuracy.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/d86be24-Community_Demo_6.png",
    tags: ["search"],
    href: "/page/rerank-demo",
  },
  {
    title: "RAG with MongoDB and Cohere",
    description:
      "Build a chatbot that provides actionable insights on technology company market reports.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/bad278b-Community_Demo_2.png",
    tags: ["search"],
    href: "/page/rag-cohere-mongodb",
  },
  {
    title: "Retrieval Evaluation with LLM-as-a-Judge via Pydantic AI",
    description:
      "Evaluate retrieval systems using LLMs as judges via Pydantic AI.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/28ee583-Community_Demo_4.png",
    tags: ["search"],
    href: "/page/retrieval-eval-pydantic-ai",
  },
];

export const cloudCards = [
  {
    title:
      "Semantic Search with Cohere Embed Jobs and Pinecone serverless Solution",
    description:
      "Learn how to use Cohere's Embed Jobs and Pinecone's serverless solution to perform semantic search.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/13cb578-Community_Demo_8.png",
    tags: ["cloud", "search"],
    href: "/page/embed-jobs-serverless-pinecone",
  },
  {
    title: "End-to-end RAG using Elasticsearch and Cohere",
    description:
      "Learn how to use Cohere and Elastic for semantic search and retrieval-augmented generation.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/5523913-Community_Demo_1.png",
    tags: ["search", "rag", "cloud"],
    href: "/page/elasticsearch-and-cohere",
  },
];

export const ragCards = [
  {
    title: "Basic RAG",
    description:
      "RAG boosts the accuracy of language models by combining them with a retrieval system.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/142e385-Community_Demo_9.png",
    tags: ["rag"],
    href: "/page/basic-rag",
  },
  {
    title: "End-to-end RAG using Elasticsearch and Cohere",
    description:
      "Learn how to use Cohere and Elastic for semantic search and retrieval-augmented generation.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/5523913-Community_Demo_1.png",
    tags: ["search", "rag", "cloud"],
    href: "/page/elasticsearch-and-cohere",
  },
  {
    title: "Chunking Strategies",
    description: "Explore chunking strategies for RAG systems.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/28ee583-Community_Demo_4.png",
    tags: ["rag"],
    href: "/page/chunking-strategies",
    authors: [ania],
  },
  {
    title: "Migrating Monolithic Prompts to Command-R with RAG",
    description:
      "Command-R simplifies prompt migration to RAG, reducing hallucination and improving conciseness and grounding.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/5523913-Community_Demo_1.png",
    tags: ["rag"],
    href: "/page/migrating-prompts",
  },
  {
    title: "RAG With Chat Embed and Rerank via Pinecone",
    description:
      "This notebook shows how to build a RAG-powered chatbot with Cohere's Chat endpoint.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/8b24122-Community_Demo_3.png",
    tags: ["rag"],
    href: "/page/rag-with-chat-embed",
  },
  {
    title: "Creating a QA Bot From Technical Documentation",
    description:
      "Create a chatbot that answers user questions based on technical documentation using Cohere embeddings and LlamaIndex.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/28ee583-Community_Demo_4.png",
    tags: ["oss", "search", "rag"],
    href: "/page/creating-a-qa-bot",
  },
  {
    title: "Deep Dive Into RAG Evaluation",
    description: "Learn how to evaluate RAG models.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/8b24122-Community_Demo_3.png",
    tags: ["rag"],
    href: "/page/rag-evaluation-deep-dive",
    authors: [marco, aal],
  },
];

export const summarizationCards = [
  {
    title: "Analysis of Form 10-K/10-Q Using Cohere and RAG",
    description:
      "Jumpstart financial analysis of 10-Ks or 10-Qs with Cohere's Command model and LlamaIndex tooling.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/083d9e2-Community_Demo_7.png",
    tags: ["summarization"],
    href: "/page/analysis-of-financial-forms",
    authors: [alex],
  },
  {
    title: "Long Form General Strategies",
    description:
      "Techniques to address lengthy documents exceeding the context window of LLMs.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/28ee583-Community_Demo_4.png",
    tags: ["summarization"],
    href: "/page/long-form-general-strategies",
    authors: [ania],
  },
  {
    title: "Summarization Evals",
    description:
      "This cookbook demonstrates an approach to evaluating summarization tasks using LLM evaluation.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/86191a6-Community_Demo_5.png",
    tags: ["summarization"],
    href: "/page/summarization-evals",
  },
  {
    title: "Grounded Summarization Using Command R",
    description:
      "Learn how to summarise long documents with citations, reducing cost and improving latency.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/bad278b-Community_Demo_2.png",
    tags: ["summarization"],
    href: "/page/grounded-summarization",
  },
];

export const finetuningCards = [
  {
    title: "Finetuning on Cohere's Platform",
    description:
      "An example of finetuning using Cohere's platform and a financial dataset.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/86191a6-Community_Demo_5.png",
    tags: ["finetuning", "wandb"],
    href: "/page/convfinqa-finetuning-wandb",
    authors: [komal],
  },
  {
    title: "Deploy your finetuned model on AWS Marketplace",
    description:
      "Learn how to deploy your finetuned model on AWS Marketplace.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/5523913-Community_Demo_1.png",
    tags: ["finetuning", "sagemaker"],
    href: "/page/deploy-finetuned-model-aws-marketplace",
    authors: [youran],
  },
  {
    title: "Finetuning on AWS Sagemaker",
    description:
      "Learn how to finetune one of Cohere's models on AWS Sagemaker.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/bad278b-Community_Demo_2.png",
    tags: ["finetuning", "sagemaker"],
    href: "/page/finetune-on-sagemaker",
    authors: [mike],
  }
]

export const otherCards = [
  {
    title: "Fueling Generative Content with Keyword Research",
    description:
      "Enhance content creation with keyword-based topic clusters, generating blog ideas with Cohere's Chat model.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/8b24122-Community_Demo_3.png",
    tags: [],
    href: "/page/fueling-generative-content",
  },
  {
    title: "Text Classification Using Embeddings",
    description:
      "Build a text classifier with Cohere embeddings. This notebook shows you how to train a sentiment analysis model with a small dataset.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/86191a6-Community_Demo_5.png",
    tags: [],
    href: "/page/text-classification-using-embeddings",
  },
  {
    title: "Article Recommender with Text Embedding Classification Extraction",
    description:
      "Improve news article recommendations with embeddings, text classification, and keyword extraction.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/142e385-Community_Demo_9.png",
    tags: [],
    href: "/page/article-recommender-with-text-embeddings",
  },
  {
    title: "Advanced Document Parsing For Enterprises",
    description: "Learn how to parse PDFs into text with a real-world example.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/083d9e2-Community_Demo_7.png",
    tags: [],
    href: "/page/document-parsing-for-enterprises",
    authors: [
      giannis,
      {
        name: "Justin Lee",
        imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/3678fac-Justin.jpg",
      },
    ],
  },
  {
    title: "Pondr, Fostering Connection through Good Conversation",
    description:
      "Learn how to create Pondr, a game that fosters connections and meaningful conversations with friends and strangers.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/86191a6-Community_Demo_5.png",
    tags: [],
    href: "/page/pondr",
  },
  {
    title: "Hello World! Meet Language AI",
    description:
      "General quickstart with basic instructions on how to get started with generative AI.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/083d9e2-Community_Demo_7.png",
    tags: [],
    href: "/page/hello-world-meet-ai",
  },
  {
    title: "Topic Modeling AI Papers",
    description: "Learn how to build a topic modeling pipeline in Python.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/5523913-Community_Demo_1.png",
    tags: [],
    href: "/page/topic-modeling-ai-papers",
  },
  {
    title: "Analyzing Hacker News with Six Language Understanding Methods",
    description: "Learn how to analyze textual data using Cohere's tools.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/28ee583-Community_Demo_4.png",
    tags: [],
    href: "/page/analyzing-hacker-news",
  },
  {
    title: "Introduction to Aya Vision: A state-of-the-art open-weights vision model",
    description: "Explore the capabilities of Aya Vision, which can take text and image inputs to generates text responses.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/28ee583-Community_Demo_4.png",
    tags: [],
    href: "/page/aya-vision-intro",
  },
  {
    title: "Document Translation with Command A Translate",
    description: "Learn how to use Command A Translate for automated translation across 23 languages with industry-leading performance.",
    imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/28ee583-Community_Demo_4.png",
    tags: [],
    href: "/page/command-a-translate",
  },
];

export const sections = [
  {
    id: "agents",
    title: "Agents",
    description:
      "Learn how to build powerful agents that use tools to connect to external services, like search engines, APIs, and databases. Agents can be used to automate tasks, answer questions, and more.",
    cards: agentCards,
  },
  {
    id: "oss",
    title: "Open Source Software Integrations",
    description:
      "Cohere integrates natively with a variety of popular Open Source Software tools like LangChain and LlamaIndex. These guides will help you get started with these integrations.",
    cards: ossCards,
  },
  {
    id: "search",
    title: "Search and Embeddings",
    description:
      "Learn how to embed and search text with Cohere. These guides will help you build semantic search engines, search Wikipedia, and more.",
    cards: searchCards,
  },
  {
    id: "cloud",
    title: "Cloud",
    description:
      "Learn how to use Cohere's cloud-based services in your preferred environment. Cohere is integrated with most major cloud providers. These guides will help you get started wherever your code lives.",
    cards: cloudCards,
  },
  {
    id: "rag",
    title: "RAG",
    description:
      "Learn how to use Cohere's foundation model for Retrieval-Augmented Generation (RAG). RAG can be used to improve the accuracy of language models by combining them with a retrieval system. This allows the model to generate completions that are grounded in provided sources of truth.",
    cards: ragCards,
  },
  {
    id: "summarization",
    title: "Summarization",
    description:
      "Learn how to summarize long documents, meeting summaries, and technical reports. Summarization is a key feature of Cohere's Command model, which can be used to generate summaries of long documents with citations.",
    cards: summarizationCards,
  },
  {
    id: "finetuning",
    title: "Finetuning",
    description:
      "Learn how to finetune Cohere's models using custom data. Finetuning allows you to adapt Cohere's models to your specific use case, improving performance and accuracy.",
    cards: finetuningCards,
  },
  {
    id: "other",
    title: "Other",
    description:
      "Here are a variety of other fun and useful guides to help you get started with Cohere. From text classification to document parsing, there's something for everyone!",
    cards: otherCards,
  },
];

export const AllCardsContainer = () => (
  <div className="all-cards-container">
    {sections.map(({ id, title, description, cards }) => (
      <div key={id}>
        <SecondaryTitleContainer
          id={id}
          title={title}
          description={description}
        />
        <div className="divider" />
        <CardsContainer cards={cards} />
      </div>
    ))}
  </div>
);

export const UseCasesContainer = () => (
  <div className="all-cards-container !py-0">
    <div className="page-secondary-title-container">
      <div className="toc-title">
        <h3 className="h2-title mb-3">Use Cases</h3>
        <p className="p-base mb-6">
          Click on one of the section headers below to jump to guides for that
          use case category.
        </p>
        <div className="toc-list">
          {sections.map(({ id, title }) => (
            <div key={id} className="toc-item">
              <a
                href={`#${id}`}
                className="group inline-block cursor-pointer font-medium"
                target="_self"
              >
                {title}
              </a>
            </div>
          ))}
        </div>
      </div>
    </div>
  </div>
);

<div>
  <div>
    <h1>
      Cookbooks
    </h1>

    <p>
      Explore what you can build on Cohere's generative AI platform. These
      ready-made guides will get you started with best-practices that get the
      most out of Cohere's models. Everything is set up and ready for you to
      start testing!
    </p>
  </div>
</div>

<div>
  <UseCasesContainer />

  <AllCardsContainer />
</div>


# Building an LLM Agent with the Cohere API

> This page how to use Cohere's API to build an LLM-based agent.

<AuthorsContainer
  authors={[
    {
      name: "Marco Del Tredici",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/f103c96-Marco.jpg",
    },
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/agents_with_deterministic_functions.ipynb" />

## Motivation

Agents can play a crucial role in different enterprise scenarios. One such example is creating a request to fetch results from an existing enterprise API with specific requirements. For example, given a user query:

`Retrieve id 7410e652-639d-402e-984e-8fd7025f0aac 8bb21b93-2ddf-4a63-af63-ddb6b1be49a1, ref GLPNT0005GUJOGGE GLSBR000BGASOBRE, nmg 0000234GLCHL0200ARTINDIUS'`

The expected API request is:

`[{"uuid":["7410e652-639d-402e-984e-8fd7025f0aac","8bb21b93-2ddf-4a63-af63-ddb6b1be49a1"],"page":0,"size":10}, {"objref":["GLPNT0005GUJOGGE","GLSBR000BGASOBRE"],"page":0,"size":10},{"nmgs":["0000234GLCHL0200ARTINDIUS"],"page":0,"size":10}]`

This kind of task poses a major challenge, namely, the model must be very precise at identifying the codes in the query, based on their alphanumeric patterns, and matching these codes with the right parameter - for example, the code `GLSBR000BGASOBRE` needs to map to
`objref`. The task is even more challenging when multiple APIs are available, and the model has to deal with a plethora of parameters.

## Solution

In this notebook, we propose a simple but effective solution to the challenge defined above: We create a [Langchain ReAct Agent](https://github.com/langchain-ai/langchain-cohere/blob/main/libs/cohere/langchain_cohere/cohere_agent.py) that has access to a deterministic tool that extracts the alphanumeric patterns in the query, and returns a dictionary in which the keys are the parameters, and the values the extracted patterns. The output of the tool is then used to generate the final request.

Using such a tool is just one of the possibilities that the Agent has to generate the query. As we will see below, when a more semantic understanding of the query is required, we can ignore the tool and leverage the linguistic capabilities of the LLM powering the Agent to generate the final output.

With this approach, we bring together the best of two worlds: the ability of LLMs to use tools and generate outputs and the reliability and efficiency of deterministic functions.

# Step 1: Setup \[#sec\_step1]

```python PYTHON
# Uncomment if you need to install the following packages
# !pip install cohere
# !pip install python-dotenv
# !pip install pandas
```

```python PYTHON
import os
import json
import re
import getpass
from langchain.agents import AgentExecutor
from langchain_cohere.chat_models import ChatCohere
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import tool
```

```python PYTHON
# load the cohere api key
os.environ["COHERE_API_KEY"] = getpass.getpass()
```

# Step 2: Define the Tool and the Agent \[#sec\_step2]

Here we create a tool which implements the deterministic function to extract alphanumeric strings
from the user's query and match them to the right parameter.

```python PYTHON
@tool
def regex_extractor(user_query: str) -> dict:
    """Function which, given the query from the user, returns a dictionary parameter:value."""
    uuid = re.findall("\s([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})", user_query)
    nmgs = re.findall("(0000[A-Z0-9]{21})", user_query)
    objref = re.findall("\s([A-Z]{5,9}\d{3,4}[A-Z]{3,8})", user_query)
    urn = re.findall("urn:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",user_query,)
    d = {"uuid": uuid,
         "nmgs": nmgs,
         "objref": objref,
         "urn": urn}
    d_filtered = {k: v for k, v in d.items() if v != []}
    return d_filtered

class extract_code_v1productssearch(BaseModel):
    user_query: str = Field(
        description="This is the full input query as received from the user. Do not truncate or modify the query in any way."
    )
regex_extractor.name = "regex_extractor"
regex_extractor.args_schema = extract_code_v1productssearch
tools=[regex_extractor]
```

```python PYTHON
# Let's define the system instruction (preamble) for the Agent.
# The system instruction includes info about:
# - the tool the Agent has access to
# - the cases in which the Agent has to produce an output without using the tool
# - some examples to clarify the task
preamble = """You are an assistant that given a user's query about, generates a request an API.
You can use the tool named "regex_extractor".
Pass to the "regex_extractor" tool the entire text of the the input query.
The tool returns a dictionary, in which keys are the name of the codes, and values a list of extracted codes.
Create a JSON for each of the key-value pairs in the dictionary.

Return a list of JSONs. Make sure each JSON is properly defined. Do not return any other explanation or comment.
You MUST generate a perfect JSON object: make sure that each string in the lists is included between quotes.

If the request mentions one of the tags listed below, or a related word, create a dictionary in which the key is "taxonomies" and the value the list of capitalized tags.
Tags list: cars, trucks, clothes, sport


Find a list of examples here:
User question | parameter for the tool | what you should understand
Look products GLCMS004AGTCAMIS; 0000234GLCMS0100ANORAKCAA, GLCHL000CGUCHALE | Look products GLCMS004AGTCAMIS; 0000234GLCMS0100ANORAKCAA, GLCHL000CGUCHALE | [{"objref":["GLCMS004AGTCAMIS","GLCHL000CGUCHALE"]},{"nmgs":["0000234GLCMS0100ANORAKCAA"]}]
Retrieve id 7410e652-639d-402e-984e-8fd7025f0aac 8bb21b93-2ddf-4a63-af63-ddb6b1be49a1, ref GLPNT0005GUJOGGE GLSBR000BGASOBRE, nmg 0000234GLCHL0200ARTINDIUS | Retrieve id 7410e652-639d-402e-984e-8fd7025f0aac 8bb21b93-2ddf-4a63-af63-ddb6b1be49a1, ref GLPNT0005GUJOGGE GLSBR000BGASOBRE, nmg 0000234GLCHL0200ARTINDIUS | [{"uuid":["7410e652-639d-402e-984e-8fd7025f0aac","8bb21b93-2ddf-4a63-af63-ddb6b1be49a1"]}, {"objref":["GLPNT0005GUJOGGE","GLSBR000BGASOBRE"]},{"nmgs":["0000234GLCHL0200ARTINDIUS"]}]
Look for items of cars and trucks | Look for items of pants and t-shirts | [{'taxonomies': ['CARS', 'TRUCKS']}]
Search products sport | Search products dress and jumpsuit | [{'taxonomies': ['SPORT']}]
"""
```

```python PYTHON
# Define the prompt
prompt = ChatPromptTemplate.from_template("{input}")
# Define the agent
llm = ChatCohere(model="command-a-03-2025", temperature=0)
# instantiate agent and agent executor
agent = create_cohere_react_agent(
   llm=llm,
   tools=tools,
   prompt=prompt,
)
agent_executor = AgentExecutor(agent=agent,
                               tools=tools,
                               verbose=True,
                               return_intermediate_steps=True
                    )
```

```python PYTHON
# finally, let's write a function to convert the Agents output to a json
def convert_to_json(string: str) -> json:
    return json.loads(
                string.replace("\xa0", " ")
                .replace("json", "")
                .replace("`", "")
                .replace("`", "")
            )
```

# Step 3: Run the Agent \[#sec\_step3]

Let's now test the Agent we just defined!

```python PYTHON
query_1 = "Look for urn:75f2b737-06dd-4399-9206-a6c11b65138e, GLCMS004AGTCAMIS; 0000234GLCMS0100ANORAKCAA, GLCHL000CGUCHALE"
response_1 = agent_executor.invoke(
            {
                "input": query_1,
                "preamble": preamble,
            }
        )
```

````txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will use the regex_extractor tool to extract the codes from the user query.
{'tool_name': 'regex_extractor', 'parameters': {'user_query': 'Look for urn:75f2b737-06dd-4399-9206-a6c11b65138e, GLCMS004AGTCAMIS; 0000234GLCMS0100ANORAKCAA, GLCHL000CGUCHALE'}}
[0m[36;1m[1;3m{'nmgs': ['0000234GLCMS0100ANORAKCAA'], 'objref': ['GLCMS004AGTCAMIS', 'GLCHL000CGUCHALE'], 'urn': ['urn:75f2b737-06dd-4399-9206-a6c11b65138e']}[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: ```json JSON
[
    {
        "urn": ["urn:75f2b737-06dd-4399-9206-a6c11b65138e"],
        "objref": ["GLCMS004AGTCAMIS", "GLCHL000CGUCHALE"],
        "nmgs": ["0000234GLCMS0100ANORAKCAA"]
    }
]
```
Grounded answer: ```json JSON
  [
    {
        "urn": [<co: 0>"urn:75f2b737-06dd-4399-9206-a6c11b65138e</co: 0>"],
        "objref": [<co: 0>"GLCMS004AGTCAMIS</co: 0>", <co: 0>"GLCHL000CGUCHALE</co: 0>"],
        "nmgs": [<co: 0>"0000234GLCMS0100ANORAKCAA</co: 0>"]
    }
]
```[0m

[1m> Finished chain.[0m
````

In the reasoning chain above, we can see that the Agent uses the tool we provided it to extract the strings in the query.
The output of the tool is then used to generate the request.

```python PYTHON
# let's have a look at the final output
convert_to_json(response_1['output'])
```

```python title="Output"
[{'urn': ['urn:75f2b737-06dd-4399-9206-a6c11b65138e'],
  'objref': ['GLCMS004AGTCAMIS', 'GLCHL000CGUCHALE'],
  'nmgs': ['0000234GLCMS0100ANORAKCAA']}]
```

As mentioned above, the Agent can use the tool when specific alphanumeric patterns have to be extracted from the query; however, it can also generate the output based on its semantic understanding of the query. For example:

```python PYTHON
query_2 = "I need tennis products"

response_2 = agent_executor.invoke(
    {
        "input": query_2,
        "preamble": preamble,
    }
)
```

````txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will use the regex_extractor tool to extract the relevant information from the user request.
{'tool_name': 'regex_extractor', 'parameters': {'user_query': 'I need tennis products'}}
[0m[36;1m[1;3m{}[0m[32;1m[1;3mRelevant Documents: None
Cited Documents: None
Answer: ```json JSON
[
    {
        "taxonomies": [
            "SPORT"
        ]
    }
]
```
Grounded answer: ```json JSON
  [
  {
  "taxonomies": [
  "SPORT"
  ]
  }
]
```[0m

[1m> Finished chain.[0m
````

The Agent runs the tool to check if any target string was in the query, then it generated the request body based on its understanding.

```python PYTHON
convert_to_json(response_2['output'])
```

```python title="Output"
[{'taxonomies': ['SPORT']}]
```

Finally, the two paths to generation - deterministic and semantic - can be applied in parallel by the Agent, as shown below:

```python PYTHON
query_3 = "Look for GLBRL0000GACHALE, nmg 0000234GLCZD0000GUREDTOAA and car products"

response_3 = agent_executor.invoke(
    {
        "input": query_3,
        "preamble": preamble,
    }
)
```

````txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will use the regex_extractor tool to extract the codes from the user query. Then, I will create a JSON for each of the key-value pairs in the dictionary.
{'tool_name': 'regex_extractor', 'parameters': {'user_query': 'Look for GLBRL0000GACHALE, nmg 0000234GLCZD0000GUREDTOAA and car products'}}
[0m[36;1m[1;3m{'nmgs': ['0000234GLCZD0000GUREDTOAA'], 'objref': ['GLBRL0000GACHALE']}[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: ```json JSON
[
    {
        "objref": ["GLBRL0000GACHALE"],
        "nmgs": ["0000234GLCZD0000GUREDTOAA"]
    },
    {
        "taxonomies": ["CARS"]
    }
]
```
Grounded answer: ```json JSON
  [
    {
        "objref": [<co: 0>"GLBRL0000GACHALE</co: 0>"],
        "nmgs": [<co: 0>"0000234GLCZD0000GUREDTOAA</co: 0>"]
    },
    {
        "taxonomies": ["CARS"]
    }
]
```[0m

[1m> Finished chain.[0m
````

```python PYTHON
convert_to_json(response_3['output'])
```

```python title="Output"
[{'objref': ['GLBRL0000GACHALE'], 'nmgs': ['0000234GLCZD0000GUREDTOAA']},
  {'taxonomies': ['CARS']}]
```

# Conclusions \[#sec\_conclusion]

In this notebook we showed how Agents can be used to solve a real-world use case, in which the goal is to create API requests based on the user's query. We did it by providing the Agent with a deterministic tool to extract relevant alphanumeric strings in the query, and matching them to the right parameter name. In parallel, the Agent can leverage the semantic understanding of the query provided by the LLM powering it.


# Short-Term Memory Handling for Agents

> This page describes how to manage short-term memory in an agent built with Cohere models.

<AuthorsContainer
  authors={[
    {
      name: "Marco Del Tredici",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/f103c96-Marco.jpg",
    },
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/agent_memory_walkthrough.ipynb" />

## Motivation

Users frequently engage in long conversations with LLMs with the expectation that the LLM fully recalls what was said in the previous turns.

The way we make LLMs aware of previous information is by simply providing them the full conversation history, i.e., the concatenation of previous input queries and generations.

As Agents become more and more used, we face the issue to make Agents fully aware of the info from previous turns.
The current approach is to pass the Agent the generations of the previous turns (see [https://python.langchain.com/docs/how\_to/migrate\_agent/](https://python.langchain.com/docs/how_to/migrate_agent/)). However, as we show below, while this is a good approach for LLMs it is not for Agents. Given the same input, LLMs *only* produce the final generation; conversely, Agents *first* produce a reasoning chain (intermediate steps), *then* produce the final outcome. Hence, if we only retain the final generation we lose some crucial info: the reasoning chain.

A straightforward solution to this issue would be to append to the conversation history from both the reasoning chain and the generations. This is problematic due to the fact that reasoning chains can be very long, especially when the model makes mistakes and corrects itself. Using the full reasoning chains would (i) introduce a lot of noise; (ii) quickly fill the whole input window of the model.

## Objective

In this notebook we introduce a simple approach to address the issue described above. We propose to use *augmented memory objects*, which we define as compact and interpretable pieces of information based on the reasoning chain and the generation.

Below, we show that, with augmented memory objects, the Agent is more aware of the information that emerged in the conversation, and, in turn, this makes the Agent behaviour more robust and effective.

# Step 1: Setup the Prompt and the Agent \[#sec\_step1]

```python PYTHON
# Uncomment if you need to install the following packages
# !pip install cohere
# !pip install python-dotenv
# !pip install pandas
```

```python PYTHON
import os
import pandas as pd
import getpass
from langchain_core.prompts import ChatPromptTemplate
from langchain_experimental.utilities import PythonREPL
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.agents import Tool
from langchain_cohere.chat_models import ChatCohere
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain.agents import AgentExecutor
from langchain_core.messages.ai import AIMessage
from langchain_core.messages.system import SystemMessage
from langchain_core.messages.human import HumanMessage
```

```python PYTHON
# load the cohere api key
os.environ["COHERE_API_KEY"] = getpass.getpass()
```

```python PYTHON
# Load the data
revenue_table = pd.read_csv('revenue_table.csv')
```

```python PYTHON
# Define the prompt
prompt = ChatPromptTemplate.from_template("{input}")
```

```python PYTHON
# Define the tools
python_repl = PythonREPL()
python_tool = Tool(
    name="python_repl",
    description="Executes python code and returns the result. The code runs in a static sandbox without interactive mode, so print output or save output to a file.",
    func=python_repl.run,
)
python_tool.name = "python_interpreter"

class ToolInput(BaseModel):
    code: str = Field(description="Python code to execute.")
python_tool.args_schema = ToolInput

tools=[python_tool]
```

```python PYTHON
# Define the agent
llm = ChatCohere(model="command-r", temperature=0)

# instantiate agent and agent executor
agent = create_cohere_react_agent(
   llm=llm,
   tools=tools,
   prompt=prompt,
)
agent_executor = AgentExecutor(agent=agent,
                               tools=tools,
                               verbose=True,
                               return_intermediate_steps=True
                    )
```

# Step 2: Conversation without memory \[#sec\_step2]

```python PYTHON
# let's start the conversation with a question about the csv we have loaded
q1 = "read revenue_table.csv and show me the column names"
a1=agent_executor.invoke({
   "input": q1,
})
```

```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will use python to read the CSV file and extract the column names.
{'tool_name': 'python_interpreter', 'parameters': {'code': "import pandas as pd\n\ndf = pd.read_csv('revenue_table.csv')\n\nprint(df.columns)"}}
[0m[36;1m[1;3mIndex(['Unnamed: 0', 'time', 'revenue', 'loss'], dtype='object')
[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The column names in the CSV file are:
- Unnamed: 0
- time
- revenue
- loss
Grounded answer: The column names in the CSV file are:
- <co: 0="">Unnamed: 0</co:>
- <co: 0="">time</co:>
- <co: 0="">revenue</co:>
- <co: 0="">loss</co:>[0m

[1m> Finished chain.[0m
```

```python PYTHON
# nice! now let's ask a follow-up question
q2 = "plot revenue numbers"
a2_no_mem = agent_executor.invoke({
   "input": q2,
})
```

````txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3mPlan: I will ask the user for clarification on what data they would like to visualise.
Action: ```json JSON
[
    {
        "tool_name": "directly_answer",
        "parameters": {}
    }
]
```

Relevant Documents: None
Cited Documents: None
Answer: Hello, could you please clarify what data you would like to see plotted?
Grounded answer: Hello, could you please clarify what data you would like to see plotted?[0m

[1m> Finished chain.[0m

````

Without memory, the model cannot answer follow up questions because it misses the necessary previous context

# Step 3: Conversation with Memory using AI Messages \[#sec\_step3]

Here we will populate the chat history only with the generations from the model. This is the current approach used, e.g., here: [https://python.langchain.com/v0.1/docs/modules/agents/how\_to/custom\_agent/](https://python.langchain.com/v0.1/docs/modules/agents/how_to/custom_agent/)

```python PYTHON
# let's answer the followup question above with the new setup
a2_mem_ai = agent_executor.invoke({
   "input": q2,
   "chat_history": [AIMessage(content=a1['output'])] # we add here the generation of the model at turn 1
})
```

```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will copy and paste the code from the previous conversation and add code to plot the revenue numbers.
{'tool_name': 'python_interpreter', 'parameters': {'code': "import pandas as pd\nimport matplotlib.pyplot as plt\n\ndata = pd.read_csv('data/sample.csv')\n\n# Plot revenue numbers\nplt.plot(data['revenue'])\n\nplt.savefig('revenue_plot.png')"}}
[0m[36;1m[1;3mFileNotFoundError(2, 'No such file or directory')[0m[32;1m[1;3m
The code is throwing an error because the file doesn't exist in the specified location. I will amend the file path and re-run the code.
{'tool_name': 'python_interpreter', 'parameters': {'code': "import pandas as pd\nimport matplotlib.pyplot as plt\n\ndata = pd.read_csv('sample.csv')\n\n# Plot revenue numbers\nplt.plot(data['revenue'])\n\nplt.savefig('revenue_plot.png')"}}
[0m[36;1m[1;3mFileNotFoundError(2, 'No such file or directory')[0m[32;1m[1;3m
The file path is still incorrect. I will amend it and re-run the code.
{'tool_name': 'python_interpreter', 'parameters': {'code': "import pandas as pd\nimport matplotlib.pyplot as plt\n\ndata = pd.read_csv('../data/sample.csv')\n\n# Plot revenue numbers\nplt.plot(data['revenue'])\n\nplt.savefig('revenue_plot.png')"}}
[0m[36;1m[1;3mFileNotFoundError(2, 'No such file or directory')[0m[32;1m[1;3mReflection: The file path is still incorrect. I will ask the user to provide the correct file path.
Relevant Documents: 0,1,2
Cited Documents: 0,1,2
Answer: The file path provided is incorrect. Please provide the correct file path so that I can plot the revenue numbers. I have tried '../data/sample.csv' but this also doesn't work.
Grounded answer: The file path provided is <co: 0,1,2="">incorrect</co:>. Please provide the correct file path so that I can plot the revenue numbers. I have tried '../data/sample.csv' but this also doesn't work.[0m

[1m> Finished chain.[0m
```

Also in this case, the model cannot manage the follow up question. The reason is that the AI message only tells part of the necessary context: we need more info from previous turns.


---

**Navigation:** [← Previous](./12-delete-a-dataset.md) | [Index](./index.md) | [Next →](./14-step-4-conversation-with-memory-using-ai-messages-.md)
