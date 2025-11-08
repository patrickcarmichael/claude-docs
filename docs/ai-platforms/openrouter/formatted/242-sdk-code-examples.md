---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/credits/coinbase"

payload = {
    "amount": 100,
    "sender": "0x1234567890123456789012345678901234567890",
    "chain_id": 1
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```
```javascript
const url = 'https://openrouter.ai/api/v1/credits/coinbase';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"amount":100,"sender":"0x1234567890123456789012345678901234567890","chain_id":1}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
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

	url := "https://openrouter.ai/api/v1/credits/coinbase"

	payload := strings.NewReader("{\n  \"amount\": 100,\n  \"sender\": \"0x1234567890123456789012345678901234567890\",\n  \"chain_id\": 1\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
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

url = URI("https://openrouter.ai/api/v1/credits/coinbase")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"amount\": 100,\n  \"sender\": \"0x1234567890123456789012345678901234567890\",\n  \"chain_id\": 1\n}"

response = http.request(request)
puts response.read_body
```
```java
HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/credits/coinbase")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"amount\": 100,\n  \"sender\": \"0x1234567890123456789012345678901234567890\",\n  \"chain_id\": 1\n}")
  .asString();
```
```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/credits/coinbase', [
  'body' => '{
  "amount": 100,
  "sender": "0x1234567890123456789012345678901234567890",
  "chain_id": 1
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```
```csharp
var client = new RestClient("https://openrouter.ai/api/v1/credits/coinbase");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"amount\": 100,\n  \"sender\": \"0x1234567890123456789012345678901234567890\",\n  \"chain_id\": 1\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```
```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "amount": 100,
  "sender": "0x1234567890123456789012345678901234567890",
  "chain_id": 1
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/credits/coinbase")! as URL,
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
