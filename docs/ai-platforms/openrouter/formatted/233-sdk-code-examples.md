---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/responses"

payload = {
    "input": [
        {
            "type": "message",
            "role": "user",
            "content": "Hello, how are you?"
        }
    ],
    "tools": [
        {
            "type": "function",
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": { "location": { "type": "string" } }
            }
        }
    ],
    "model": "anthropic/claude-4.5-sonnet-20250929",
    "temperature": 0.7,
    "top_p": 0.9
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```
```javascript
const url = 'https://openrouter.ai/api/v1/responses';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"input":[{"type":"message","role":"user","content":"Hello, how are you?"}],"tools":[{"type":"function","name":"get_current_weather","description":"Get the current weather in a given location","parameters":{"type":"object","properties":{"location":{"type":"string"}}}}],"model":"anthropic/claude-4.5-sonnet-20250929","temperature":0.7,"top_p":0.9}'
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

	url := "https://openrouter.ai/api/v1/responses"

	payload := strings.NewReader("{\n  \"input\": [\n    {\n      \"type\": \"message\",\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"name\": \"get_current_weather\",\n      \"description\": \"Get the current weather in a given location\",\n      \"parameters\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"temperature\": 0.7,\n  \"top_p\": 0.9\n}")

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

url = URI("https://openrouter.ai/api/v1/responses")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"input\": [\n    {\n      \"type\": \"message\",\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"name\": \"get_current_weather\",\n      \"description\": \"Get the current weather in a given location\",\n      \"parameters\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"temperature\": 0.7,\n  \"top_p\": 0.9\n}"

response = http.request(request)
puts response.read_body
```
```java
HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/responses")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"input\": [\n    {\n      \"type\": \"message\",\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"name\": \"get_current_weather\",\n      \"description\": \"Get the current weather in a given location\",\n      \"parameters\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"temperature\": 0.7,\n  \"top_p\": 0.9\n}")
  .asString();
```
```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/responses', [
  'body' => '{
  "input": [
    {
      "type": "message",
      "role": "user",
      "content": "Hello, how are you?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string"
          }
        }
      }
    }
  ],
  "model": "anthropic/claude-4.5-sonnet-20250929",
  "temperature": 0.7,
  "top_p": 0.9
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```
```csharp
var client = new RestClient("https://openrouter.ai/api/v1/responses");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"input\": [\n    {\n      \"type\": \"message\",\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"name\": \"get_current_weather\",\n      \"description\": \"Get the current weather in a given location\",\n      \"parameters\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"temperature\": 0.7,\n  \"top_p\": 0.9\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```
```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "input": [
    [
      "type": "message",
      "role": "user",
      "content": "Hello, how are you?"
    ]
  ],
  "tools": [
    [
      "type": "function",
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": [
        "type": "object",
        "properties": ["location": ["type": "string"]]
      ]
    ]
  ],
  "model": "anthropic/claude-4.5-sonnet-20250929",
  "temperature": 0.7,
  "top_p": 0.9
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/responses")! as URL,
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
