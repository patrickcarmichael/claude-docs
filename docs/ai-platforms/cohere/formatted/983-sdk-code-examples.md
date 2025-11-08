---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## SDK Code Examples

```go Cohere Go SDK
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Detokenize(
		context.TODO(),
		&cohere.DetokenizeRequest{
			Tokens: []int{10002, 1706, 1722, 5169, 4328},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}
```
```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const detokenize = await cohere.detokenize({
    tokens: [10002, 2261, 2012, 8, 2792, 43],
    model: 'command',
  });

  console.log(detokenize);
})();
```
```python Sync
import cohere

co = cohere.Client()

response = co.detokenize(
    tokens=[8466, 5169, 2594, 8, 2792, 43], model="command-a-03-2025"  # optional

)
print(response)
```
```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.detokenize(
        tokens=[8466, 5169, 2594, 8, 2792, 43],
        model="command-a-03-2025",  # optional

    )
    print(response)


asyncio.run(main())
```
```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.requests.DetokenizeRequest;
import com.cohere.api.types.DetokenizeResponse;
import java.util.List;

public class DetokenizePost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    DetokenizeResponse response =
        cohere.detokenize(
            DetokenizeRequest.builder()
                .model("command-a-03-2025")
                .tokens(List.of(8466, 5169, 2594, 8, 2792, 43))
                .build());

    System.out.println(response);
  }
}
```
```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/detokenize")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tokens\": [\n    10002,\n    2261,\n    2012,\n    8,\n    2792,\n    43\n  ],\n  \"model\": \"command\"\n}"

response = http.request(request)
puts response.read_body
```
```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/detokenize', [
  'body' => '{
  "tokens": [
    10002,
    2261,
    2012,
    8,
    2792,
    43
  ],
  "model": "command"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```
```csharp
var client = new RestClient("https://api.cohere.com/v1/detokenize");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"tokens\": [\n    10002,\n    2261,\n    2012,\n    8,\n    2792,\n    43\n  ],\n  \"model\": \"command\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```
```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "tokens": [10002, 2261, 2012, 8, 2792, 43],
  "model": "command"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/detokenize")! as URL,
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

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
