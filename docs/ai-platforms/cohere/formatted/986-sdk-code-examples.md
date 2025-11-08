---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## SDK Code Examples

```python
from cohere import Client

client = Client(
    client_name="YOUR_CLIENT_NAME",
    token="YOUR_TOKEN",
)
client.models.get(
    model="command-a-03-2025",
)
```
```typescript
import { CohereClient } from "cohere-ai";

const client = new CohereClient({ token: "YOUR_TOKEN", clientName: "YOUR_CLIENT_NAME" });
await client.models.get("command-a-03-2025");
```
```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cohere.com/v1/models/command-a-03-2025"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("X-Client-Name", "my-cool-project")
	req.Header.Add("Authorization", "Bearer <token>")

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

url = URI("https://api.cohere.com/v1/models/command-a-03-2025")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```
```java
HttpResponse<String> response = Unirest.get("https://api.cohere.com/v1/models/command-a-03-2025")
  .header("X-Client-Name", "my-cool-project")
  .header("Authorization", "Bearer <token>")
  .asString();
```
```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.cohere.com/v1/models/command-a-03-2025', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```
```csharp
var client = new RestClient("https://api.cohere.com/v1/models/command-a-03-2025");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/models/command-a-03-2025")! as URL,
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
