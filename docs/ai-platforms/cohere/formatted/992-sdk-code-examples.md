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
	model := "<YOUR-FINE-TUNED-MODEL-ID>"

	resp, err := co.Classify(
		context.TODO(),
		&cohere.ClassifyRequest{
			Model: &model,
			Examples: []*cohere.ClassifyExample{
				{
					Text:  cohere.String("orange"),
					Label: cohere.String("fruit"),
				},
				{
					Text:  cohere.String("pear"),
					Label: cohere.String("fruit"),
				},
				{
					Text:  cohere.String("lettuce"),
					Label: cohere.String("vegetable"),
				},
				{
					Text:  cohere.String("cauliflower"),
					Label: cohere.String("vegetable"),
				},
			},
			Inputs: []string{"peach"},
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
  const classify = await cohere.classify({
    model: '<YOUR-FINE-TUNED-MODEL-ID>',
    examples: [
      { text: "Dermatologists don't like her!", label: 'Spam' },
      { text: "'Hello, open to this?'", label: 'Spam' },
      { text: 'I need help please wire me $1000 right now', label: 'Spam' },
      { text: 'Nice to know you ;)', label: 'Spam' },
      { text: 'Please help me?', label: 'Spam' },
      { text: 'Your parcel will be delivered today', label: 'Not spam' },
      { text: 'Review changes to our Terms and Conditions', label: 'Not spam' },
      { text: 'Weekly sync notes', label: 'Not spam' },
      { text: "'Re: Follow up from today's meeting'", label: 'Not spam' },
      { text: 'Pre-read for tomorrow', label: 'Not spam' },
    ],
    inputs: ['Confirm your email address', 'hey i need u to send some $'],
  });

  console.log(classify);
})();
```
```python Sync
import cohere
from cohere import ClassifyExample

co = cohere.Client()
examples = [
    ClassifyExample(text="Dermatologists don't like her!", label="Spam"),
    ClassifyExample(text="'Hello, open to this?'", label="Spam"),
    ClassifyExample(text="I need help please wire me $1000 right now", label="Spam"),
    ClassifyExample(text="Nice to know you ;)", label="Spam"),
    ClassifyExample(text="Please help me?", label="Spam"),
    ClassifyExample(text="Your parcel will be delivered today", label="Not spam"),
    ClassifyExample(
        text="Review changes to our Terms and Conditions", label="Not spam"
    ),
    ClassifyExample(text="Weekly sync notes", label="Not spam"),
    ClassifyExample(text="'Re: Follow up from today's meeting'", label="Not spam"),
    ClassifyExample(text="Pre-read for tomorrow", label="Not spam"),
]
inputs = [
    "Confirm your email address",
    "hey i need u to send some $",
]
response = co.classify(
    model="<YOUR-FINE-TUNED-MODEL-ID>",
    inputs=inputs,
    examples=examples,
)
print(response)
```
```python Async
import cohere
import asyncio
from cohere import ClassifyExample

co = cohere.AsyncClient()
examples = [
    ClassifyExample(text="Dermatologists don't like her!", label="Spam"),
    ClassifyExample(text="'Hello, open to this?'", label="Spam"),
    ClassifyExample(text="I need help please wire me $1000 right now", label="Spam"),
    ClassifyExample(text="Nice to know you ;)", label="Spam"),
    ClassifyExample(text="Please help me?", label="Spam"),
    ClassifyExample(text="Your parcel will be delivered today", label="Not spam"),
    ClassifyExample(
        text="Review changes to our Terms and Conditions", label="Not spam"
    ),
    ClassifyExample(text="Weekly sync notes", label="Not spam"),
    ClassifyExample(text="'Re: Follow up from today's meeting'", label="Not spam"),
    ClassifyExample(text="Pre-read for tomorrow", label="Not spam"),
]
inputs = [
    "Confirm your email address",
    "hey i need u to send some $",
]


async def main():
    response = await co.classify(
        model="<YOUR-FINE-TUNED-MODEL-ID>",
        inputs=inputs,
        examples=examples,
    )
    print(response)


asyncio.run(main())
```
```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.requests.ClassifyRequest;
import com.cohere.api.types.ClassifyExample;
import com.cohere.api.types.ClassifyResponse;
import java.util.List;

public class ClassifyPost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ClassifyResponse response =
        cohere.classify(
            ClassifyRequest.builder()
                .addAllInputs(List.of("Confirm your email address", "hey i need u to send some $"))
                .examples(
                    List.of(
                        ClassifyExample.builder()
                            .text("Dermatologists don't like her!")
                            .label("Spam")
                            .build(),
                        ClassifyExample.builder()
                            .text("'Hello, open to this?'")
                            .label("Spam")
                            .build(),
                        ClassifyExample.builder()
                            .text("I need help please wire me $1000" + " right now")
                            .label("Spam")
                            .build(),
                        ClassifyExample.builder().text("Nice to know you ;)").label("Spam").build(),
                        ClassifyExample.builder().text("Please help me?").label("Spam").build(),
                        ClassifyExample.builder()
                            .text("Your parcel will be delivered today")
                            .label("Not spam")
                            .build(),
                        ClassifyExample.builder()
                            .text("Review changes to our Terms and" + " Conditions")
                            .label("Not spam")
                            .build(),
                        ClassifyExample.builder()
                            .text("Weekly sync notes")
                            .label("Not spam")
                            .build(),
                        ClassifyExample.builder()
                            .text("'Re: Follow up from today's" + " meeting'")
                            .label("Not spam")
                            .build(),
                        ClassifyExample.builder()
                            .text("Pre-read for tomorrow")
                            .label("Not spam")
                            .build()))
                .build());

    System.out.println(response);
  }
}
```
```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/classify")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"inputs\": [\n    \"Confirm your email address\",\n    \"hey i need u to send some $\"\n  ],\n  \"examples\": [\n    {\n      \"text\": \"Dermatologists don't like her!\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"'Hello, open to this?'\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"I need help please wire me $1000 right now\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"Nice to know you ;)\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"Please help me?\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"Your parcel will be delivered today\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"Review changes to our Terms and Conditions\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"Weekly sync notes\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"'Re: Follow up from today's meeting'\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"Pre-read for tomorrow\",\n      \"label\": \"Not spam\"\n    }\n  ],\n  \"model\": \"YOUR-FINE-TUNED-MODEL-ID\"\n}"

response = http.request(request)
puts response.read_body
```
```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/classify', [
  'body' => '{
  "inputs": [
    "Confirm your email address",
    "hey i need u to send some $"
  ],
  "examples": [
    {
      "text": "Dermatologists don\'t like her!",
      "label": "Spam"
    },
    {
      "text": "\'Hello, open to this?\'",
      "label": "Spam"
    },
    {
      "text": "I need help please wire me $1000 right now",
      "label": "Spam"
    },
    {
      "text": "Nice to know you ;)",
      "label": "Spam"
    },
    {
      "text": "Please help me?",
      "label": "Spam"
    },
    {
      "text": "Your parcel will be delivered today",
      "label": "Not spam"
    },
    {
      "text": "Review changes to our Terms and Conditions",
      "label": "Not spam"
    },
    {
      "text": "Weekly sync notes",
      "label": "Not spam"
    },
    {
      "text": "\'Re: Follow up from today\'s meeting\'",
      "label": "Not spam"
    },
    {
      "text": "Pre-read for tomorrow",
      "label": "Not spam"
    }
  ],
  "model": "YOUR-FINE-TUNED-MODEL-ID"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```
```csharp
var client = new RestClient("https://api.cohere.com/v1/classify");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"inputs\": [\n    \"Confirm your email address\",\n    \"hey i need u to send some $\"\n  ],\n  \"examples\": [\n    {\n      \"text\": \"Dermatologists don't like her!\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"'Hello, open to this?'\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"I need help please wire me $1000 right now\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"Nice to know you ;)\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"Please help me?\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"Your parcel will be delivered today\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"Review changes to our Terms and Conditions\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"Weekly sync notes\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"'Re: Follow up from today's meeting'\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"Pre-read for tomorrow\",\n      \"label\": \"Not spam\"\n    }\n  ],\n  \"model\": \"YOUR-FINE-TUNED-MODEL-ID\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```
```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "inputs": ["Confirm your email address", "hey i need u to send some $"],
  "examples": [
    [
      "text": "Dermatologists don't like her!",
      "label": "Spam"
    ],
    [
      "text": "'Hello, open to this?'",
      "label": "Spam"
    ],
    [
      "text": "I need help please wire me $1000 right now",
      "label": "Spam"
    ],
    [
      "text": "Nice to know you ;)",
      "label": "Spam"
    ],
    [
      "text": "Please help me?",
      "label": "Spam"
    ],
    [
      "text": "Your parcel will be delivered today",
      "label": "Not spam"
    ],
    [
      "text": "Review changes to our Terms and Conditions",
      "label": "Not spam"
    ],
    [
      "text": "Weekly sync notes",
      "label": "Not spam"
    ],
    [
      "text": "'Re: Follow up from today's meeting'",
      "label": "Not spam"
    ],
    [
      "text": "Pre-read for tomorrow",
      "label": "Not spam"
    ]
  ],
  "model": "YOUR-FINE-TUNED-MODEL-ID"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/classify")! as URL,
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
