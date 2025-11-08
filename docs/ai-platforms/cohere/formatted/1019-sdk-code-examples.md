---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
