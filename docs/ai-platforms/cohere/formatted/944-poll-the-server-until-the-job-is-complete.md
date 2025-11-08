---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## poll the server until the job is complete

response = co.wait(job)

print(response)
```
```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    # start an embed job

    job = await co.embed_jobs.create(
        dataset_id="my-dataset-id",
        input_type="search_document",
        model="embed-english-v3.0",
    )

    # poll the server until the job is complete

    response = await co.wait(job)

    print(response)


asyncio.run(main())
```
```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.embedjobs.requests.CreateEmbedJobRequest;
import com.cohere.api.types.CreateEmbedJobResponse;
import com.cohere.api.types.EmbedInputType;

public class EmbedJobsPost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    CreateEmbedJobResponse response =
        cohere
            .embedJobs()
            .create(
                CreateEmbedJobRequest.builder()
                    .model("embed-v4.0")
                    .datasetId("ds.id")
                    .inputType(EmbedInputType.SEARCH_DOCUMENT)
                    .build());

    System.out.println(response);
  }
}
```
```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const embedJob = await cohere.embedJobs.create({
    datasetId: 'my-dataset',
    inputType: 'search_document',
    model: 'embed-v4.0',
  });

  console.log(embedJob);
})();
```
```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/embed-jobs")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model\": \"string\",\n  \"dataset_id\": \"string\",\n  \"input_type\": \"search_document\"\n}"

response = http.request(request)
puts response.read_body
```
```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/embed-jobs', [
  'body' => '{
  "model": "string",
  "dataset_id": "string",
  "input_type": "search_document"
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
var client = new RestClient("https://api.cohere.com/v1/embed-jobs");
var request = new RestRequest(Method.POST);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model\": \"string\",\n  \"dataset_id\": \"string\",\n  \"input_type\": \"search_document\"\n}", ParameterType.RequestBody);
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
  "model": "string",
  "dataset_id": "string",
  "input_type": "search_document"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/embed-jobs")! as URL,
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
