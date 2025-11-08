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
import com.cohere.api.resources.finetuning.finetuning.types.ListFinetunedModelsResponse;

public class ListFinetunedModels {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ListFinetunedModelsResponse response = cohere.finetuning().listFinetunedModels();

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

	resp, err := co.Finetuning.ListFinetunedModels(context.TODO(), nil)
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp.FinetunedModels)
}
```
```typescript Cohere TypeScript SDK
const { CohereClient } = require('cohere-ai');

const cohere = new CohereClient({
  token: '<<apiKey>>',
});

(async () => {
  const finetunedModels = await cohere.finetuning.listFinetunedModels();

  console.log(finetunedModels);
})();
```
```python Sync
import cohere

co = cohere.Client()
response = co.finetuning.list_finetuned_models()
print(response)
```
```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.finetuning.list_finetuned_models()
    print(response)


asyncio.run(main())
```
```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/finetuning/finetuned-models")

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

$response = $client->request('GET', 'https://api.cohere.com/v1/finetuning/finetuned-models', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```
```csharp
var client = new RestClient("https://api.cohere.com/v1/finetuning/finetuned-models");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/finetuning/finetuned-models")! as URL,
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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
