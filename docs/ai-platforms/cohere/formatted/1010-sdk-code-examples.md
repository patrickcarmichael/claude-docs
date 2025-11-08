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

	resp, err := co.Connectors.OAuthAuthorize(
		context.TODO(),
		"connector_id",
		&cohere.ConnectorsOAuthAuthorizeRequest{
			AfterTokenRedirect: cohere.String("https://test.com"),
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}
```
```python Sync
import cohere

co = cohere.Client()
response = co.connectors.o_auth_authorize(
    connector_id="test-id", after_token_redirect="https://test.com"
)
print(response)
```
```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.connectors.o_auth_authorize(
        connector_id="test-id", after_token_redirect="https://test.com"
    )
    print(response)


asyncio.run(main())
```
```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.connectors.requests.ConnectorsOAuthAuthorizeRequest;
import com.cohere.api.types.OAuthAuthorizeResponse;

public class ConnectorsIdOauthAuthorizePost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    OAuthAuthorizeResponse response =
        cohere
            .connectors()
            .oAuthAuthorize(
                "test-id",
                ConnectorsOAuthAuthorizeRequest.builder()
                    .afterTokenRedirect("https://connector-example.com/search")
                    .build());

    System.out.println(response);
  }
}
```
```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const connector = await cohere.connectors.oAuthAuthorize('connector-id', {
    redirect_uri: 'https://example.com/oauth/callback',
  });

  console.log(connector);
})();
```
```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/connectors/id/oauth/authorize")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```
```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/connectors/id/oauth/authorize', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```
```csharp
var client = new RestClient("https://api.cohere.com/v1/connectors/id/oauth/authorize");
var request = new RestRequest(Method.POST);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/connectors/id/oauth/authorize")! as URL,
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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
