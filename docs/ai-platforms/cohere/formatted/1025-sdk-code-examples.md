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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
