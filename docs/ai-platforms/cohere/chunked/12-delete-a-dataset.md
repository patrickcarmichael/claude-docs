**Navigation:** [← Previous](./11-embed-api-v2.md) | [Index](./index.md) | [Next →](./13-updates-a-fine-tuned-model.md)

---

# Delete a Dataset

DELETE https://api.cohere.com/v1/datasets/{id}

Delete a dataset by ID. Datasets are automatically deleted after 30 days, but they can also be deleted manually.

Reference: https://docs.cohere.com/reference/delete-dataset

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete a Dataset
  version: endpoint_datasets.delete
paths:
  /v1/datasets/{id}:
    delete:
      operationId: delete
      summary: Delete a Dataset
      description: >-
        Delete a dataset by ID. Datasets are automatically deleted after 30
        days, but they can also be deleted manually.
      tags:
        - - subpackage_datasets
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/datasets_delete_Response_200'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
components:
  schemas:
    datasets_delete_Response_200:
      type: object
      properties: {}

```

## SDK Code Examples

```go Cohere Go SDK
package main

import (
	"context"
	"log"
	"os"

	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	_, err := co.Datasets.Delete(context.TODO(), "dataset_id")

	if err != nil {
		log.Fatal(err)
	}

}

```

```python Sync
import cohere

co = cohere.Client()

# delete dataset
co.datasets.delete("id")

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    await co.delete_dataset("id")


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;

public class DatasetDelete {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    cohere.datasets().delete("id");
  }
}

```

```typescript
import { CohereClient } from "cohere-ai";

const client = new CohereClient({ token: "YOUR_TOKEN", clientName: "YOUR_CLIENT_NAME" });
await client.datasets.delete("id");

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/datasets/id")

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

$response = $client->request('DELETE', 'https://api.cohere.com/v1/datasets/id', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/datasets/id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/datasets/id")! as URL,
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

# Tokenize

POST https://api.cohere.com/v1/tokenize
Content-Type: application/json

This endpoint splits input text into smaller units called tokens using byte-pair encoding (BPE). To learn more about tokenization and byte pair encoding, see the tokens page.

Reference: https://docs.cohere.com/reference/tokenize

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Tokenize
  version: endpoint_.tokenize
paths:
  /v1/tokenize:
    post:
      operationId: tokenize
      summary: Tokenize
      description: >-
        This endpoint splits input text into smaller units called tokens using
        byte-pair encoding (BPE). To learn more about tokenization and byte pair
        encoding, see the tokens page.
      tags:
        - []
      parameters:
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/tokenize_Response_200'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
      requestBody:
        description: ''
        content:
          application/json:
            schema:
              type: object
              properties:
                text:
                  type: string
                model:
                  type: string
              required:
                - text
                - model
components:
  schemas:
    ApiMetaApiVersion:
      type: object
      properties:
        version:
          type: string
        is_deprecated:
          type: boolean
        is_experimental:
          type: boolean
      required:
        - version
    ApiMetaBilledUnits:
      type: object
      properties:
        images:
          type: number
          format: double
        input_tokens:
          type: number
          format: double
        output_tokens:
          type: number
          format: double
        search_units:
          type: number
          format: double
        classifications:
          type: number
          format: double
    ApiMetaTokens:
      type: object
      properties:
        input_tokens:
          type: number
          format: double
        output_tokens:
          type: number
          format: double
    ApiMeta:
      type: object
      properties:
        api_version:
          $ref: '#/components/schemas/ApiMetaApiVersion'
        billed_units:
          $ref: '#/components/schemas/ApiMetaBilledUnits'
        tokens:
          $ref: '#/components/schemas/ApiMetaTokens'
        cached_tokens:
          type: number
          format: double
        warnings:
          type: array
          items:
            type: string
    tokenize_Response_200:
      type: object
      properties:
        tokens:
          type: array
          items:
            type: integer
        token_strings:
          type: array
          items:
            type: string
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - tokens
        - token_strings

```

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

	resp, err := co.Tokenize(
		context.TODO(),
		&cohere.TokenizeRequest{
			Text:  "cohere <3",
			Model: "base",
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
  const tokenize = await cohere.tokenize({
    text: 'tokenize me! :D',
    model: 'command', // optional
  });

  console.log(tokenize);
})();

```

```typescript Cohere Node.js SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const tokenize = await cohere.tokenize({
    text: 'tokenize me! :D',
    model: 'command', // optional
  });

  console.log(tokenize);
})();

```

```python Sync
import cohere

co = cohere.Client()

response = co.tokenize(
    text="tokenize me! :D", model="command-a-03-2025"
)  # optional
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.tokenize(text="tokenize me! :D", model="command-a-03-2025")
    print(response)


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.requests.TokenizeRequest;
import com.cohere.api.types.TokenizeResponse;

public class TokenizePost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    TokenizeResponse response =
        cohere.tokenize(
            TokenizeRequest.builder().text("tokenize me").model("command-a-03-2025").build());

    System.out.println(response);
  }
}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/tokenize")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"tokenize me! :D\",\n  \"model\": \"command\"\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/tokenize', [
  'body' => '{
  "text": "tokenize me! :D",
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
var client = new RestClient("https://api.cohere.com/v1/tokenize");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"tokenize me! :D\",\n  \"model\": \"command\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "text": "tokenize me! :D",
  "model": "command"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/tokenize")! as URL,
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

# Detokenize

POST https://api.cohere.com/v1/detokenize
Content-Type: application/json

This endpoint takes tokens using byte-pair encoding and returns their text representation. To learn more about tokenization and byte pair encoding, see the tokens page.

Reference: https://docs.cohere.com/reference/detokenize

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Detokenize
  version: endpoint_.detokenize
paths:
  /v1/detokenize:
    post:
      operationId: detokenize
      summary: Detokenize
      description: >-
        This endpoint takes tokens using byte-pair encoding and returns their
        text representation. To learn more about tokenization and byte pair
        encoding, see the tokens page.
      tags:
        - []
      parameters:
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/detokenize_Response_200'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
      requestBody:
        description: ''
        content:
          application/json:
            schema:
              type: object
              properties:
                tokens:
                  type: array
                  items:
                    type: integer
                model:
                  type: string
              required:
                - tokens
                - model
components:
  schemas:
    ApiMetaApiVersion:
      type: object
      properties:
        version:
          type: string
        is_deprecated:
          type: boolean
        is_experimental:
          type: boolean
      required:
        - version
    ApiMetaBilledUnits:
      type: object
      properties:
        images:
          type: number
          format: double
        input_tokens:
          type: number
          format: double
        output_tokens:
          type: number
          format: double
        search_units:
          type: number
          format: double
        classifications:
          type: number
          format: double
    ApiMetaTokens:
      type: object
      properties:
        input_tokens:
          type: number
          format: double
        output_tokens:
          type: number
          format: double
    ApiMeta:
      type: object
      properties:
        api_version:
          $ref: '#/components/schemas/ApiMetaApiVersion'
        billed_units:
          $ref: '#/components/schemas/ApiMetaBilledUnits'
        tokens:
          $ref: '#/components/schemas/ApiMetaTokens'
        cached_tokens:
          type: number
          format: double
        warnings:
          type: array
          items:
            type: string
    detokenize_Response_200:
      type: object
      properties:
        text:
          type: string
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - text

```

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

# Get a Model

GET https://api.cohere.com/v1/models/{model}

Returns the details of a model, provided its name.

Reference: https://docs.cohere.com/reference/get-model

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get a Model
  version: endpoint_models.get
paths:
  /v1/models/{model}:
    get:
      operationId: get
      summary: Get a Model
      description: Returns the details of a model, provided its name.
      tags:
        - - subpackage_models
      parameters:
        - name: model
          in: path
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetModelResponse'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
components:
  schemas:
    CompatibleEndpoint:
      type: string
      enum:
        - value: chat
        - value: embed
        - value: classify
        - value: summarize
        - value: rerank
        - value: rate
        - value: generate
    GetModelResponse:
      type: object
      properties:
        name:
          type: string
        is_deprecated:
          type: boolean
        endpoints:
          type: array
          items:
            $ref: '#/components/schemas/CompatibleEndpoint'
        finetuned:
          type: boolean
        context_length:
          type: number
          format: double
        tokenizer_url:
          type: string
        default_endpoints:
          type: array
          items:
            $ref: '#/components/schemas/CompatibleEndpoint'
        features:
          type: array
          items:
            type: string

```

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

# List Models

GET https://api.cohere.com/v1/models

Returns a list of models available for use.

Reference: https://docs.cohere.com/reference/list-models

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List Models
  version: endpoint_models.list
paths:
  /v1/models:
    get:
      operationId: list
      summary: List Models
      description: Returns a list of models available for use.
      tags:
        - - subpackage_models
      parameters:
        - name: page_size
          in: query
          description: |-
            Maximum number of models to include in a page
            Defaults to `20`, min value of `1`, max value of `1000`.
          required: false
          schema:
            type: number
            format: double
        - name: page_token
          in: query
          description: >-
            Page token provided in the `next_page_token` field of a previous
            response.
          required: false
          schema:
            type: string
        - name: endpoint
          in: query
          description: >-
            When provided, filters the list of models to only those that are
            compatible with the specified endpoint.
          required: false
          schema:
            $ref: '#/components/schemas/CompatibleEndpoint'
        - name: default_only
          in: query
          description: >-
            When provided, filters the list of models to only the default model
            to the endpoint. This parameter is only valid when `endpoint` is
            provided.
          required: false
          schema:
            type: boolean
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListModelsResponse'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
components:
  schemas:
    CompatibleEndpoint:
      type: string
      enum:
        - value: chat
        - value: embed
        - value: classify
        - value: summarize
        - value: rerank
        - value: rate
        - value: generate
    GetModelResponse:
      type: object
      properties:
        name:
          type: string
        is_deprecated:
          type: boolean
        endpoints:
          type: array
          items:
            $ref: '#/components/schemas/CompatibleEndpoint'
        finetuned:
          type: boolean
        context_length:
          type: number
          format: double
        tokenizer_url:
          type: string
        default_endpoints:
          type: array
          items:
            $ref: '#/components/schemas/CompatibleEndpoint'
        features:
          type: array
          items:
            type: string
    ListModelsResponse:
      type: object
      properties:
        models:
          type: array
          items:
            $ref: '#/components/schemas/GetModelResponse'
        next_page_token:
          type: string
      required:
        - models

```

## SDK Code Examples

```python Sync
import cohere

co = cohere.Client()
response = co.models.list()
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.models.list()
    print(response)


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.types.ListModelsResponse;

public class ModelsListGet {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ListModelsResponse response = cohere.models().list();

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const models = await cohere.models.list();

  console.log(models);
})();

```

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

	resp, err := co.Models.List(context.TODO(), &cohere.ModelsListRequest{})

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/models")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.cohere.com/v1/models', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/models");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/models")! as URL,
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

# Classify

POST https://api.cohere.com/v1/classify
Content-Type: application/json

This endpoint makes a prediction about which label fits the specified text inputs best. To make a prediction, Classify uses the provided `examples` of text + label pairs as a reference.
Note: [Fine-tuned models](https://docs.cohere.com/docs/classify-fine-tuning) trained on classification examples don't require the `examples` parameter to be passed in explicitly.

Reference: https://docs.cohere.com/reference/classify

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Classify
  version: endpoint_.classify
paths:
  /v1/classify:
    post:
      operationId: classify
      summary: Classify
      description: >-
        This endpoint makes a prediction about which label fits the specified
        text inputs best. To make a prediction, Classify uses the provided
        `examples` of text + label pairs as a reference.

        Note: [Fine-tuned
        models](https://docs.cohere.com/docs/classify-fine-tuning) trained on
        classification examples don't require the `examples` parameter to be
        passed in explicitly.
      tags:
        - []
      parameters:
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/classify_Response_200'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
      requestBody:
        description: ''
        content:
          application/json:
            schema:
              type: object
              properties:
                inputs:
                  type: array
                  items:
                    type: string
                examples:
                  type: array
                  items:
                    $ref: '#/components/schemas/ClassifyExample'
                model:
                  type: string
                preset:
                  type: string
                truncate:
                  $ref: >-
                    #/components/schemas/V1ClassifyPostRequestBodyContentApplicationJsonSchemaTruncate
              required:
                - inputs
components:
  schemas:
    ClassifyExample:
      type: object
      properties:
        text:
          type: string
        label:
          type: string
    V1ClassifyPostRequestBodyContentApplicationJsonSchemaTruncate:
      type: string
      enum:
        - value: NONE
        - value: START
        - value: END
    V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItemsLabels:
      type: object
      properties:
        confidence:
          type: number
          format: double
    V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItemsClassificationType:
      type: string
      enum:
        - value: single-label
        - value: multi-label
    V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItems:
      type: object
      properties:
        id:
          type: string
        input:
          type: string
        prediction:
          type: string
        predictions:
          type: array
          items:
            type: string
        confidence:
          type: number
          format: double
        confidences:
          type: array
          items:
            type: number
            format: double
        labels:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItemsLabels
        classification_type:
          $ref: >-
            #/components/schemas/V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItemsClassificationType
      required:
        - id
        - predictions
        - confidences
        - labels
        - classification_type
    ApiMetaApiVersion:
      type: object
      properties:
        version:
          type: string
        is_deprecated:
          type: boolean
        is_experimental:
          type: boolean
      required:
        - version
    ApiMetaBilledUnits:
      type: object
      properties:
        images:
          type: number
          format: double
        input_tokens:
          type: number
          format: double
        output_tokens:
          type: number
          format: double
        search_units:
          type: number
          format: double
        classifications:
          type: number
          format: double
    ApiMetaTokens:
      type: object
      properties:
        input_tokens:
          type: number
          format: double
        output_tokens:
          type: number
          format: double
    ApiMeta:
      type: object
      properties:
        api_version:
          $ref: '#/components/schemas/ApiMetaApiVersion'
        billed_units:
          $ref: '#/components/schemas/ApiMetaBilledUnits'
        tokens:
          $ref: '#/components/schemas/ApiMetaTokens'
        cached_tokens:
          type: number
          format: double
        warnings:
          type: array
          items:
            type: string
    classify_Response_200:
      type: object
      properties:
        id:
          type: string
        classifications:
          type: array
          items:
            $ref: >-
              #/components/schemas/V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItems
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - id
        - classifications

```

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

# List Connectors

GET https://api.cohere.com/v1/connectors

Returns a list of connectors ordered by descending creation date (newer first). See ['Managing your Connector'](https://docs.cohere.com/docs/managing-your-connector) for more information.

Reference: https://docs.cohere.com/reference/list-connectors

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List Connectors
  version: endpoint_connectors.list
paths:
  /v1/connectors:
    get:
      operationId: list
      summary: List Connectors
      description: >-
        Returns a list of connectors ordered by descending creation date (newer
        first). See ['Managing your
        Connector'](https://docs.cohere.com/docs/managing-your-connector) for
        more information.
      tags:
        - - subpackage_connectors
      parameters:
        - name: limit
          in: query
          description: Maximum number of connectors to return [0, 100].
          required: false
          schema:
            type: number
            format: double
        - name: offset
          in: query
          description: Number of connectors to skip before returning results [0, inf].
          required: false
          schema:
            type: number
            format: double
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListConnectorsResponse'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
components:
  schemas:
    ConnectorOAuth:
      type: object
      properties:
        client_id:
          type: string
        client_secret:
          type: string
        authorize_url:
          type: string
        token_url:
          type: string
        scope:
          type: string
      required:
        - authorize_url
        - token_url
    ConnectorAuthStatus:
      type: string
      enum:
        - value: valid
        - value: expired
    Connector:
      type: object
      properties:
        id:
          type: string
        organization_id:
          type: string
        name:
          type: string
        description:
          type: string
        url:
          type: string
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        excludes:
          type: array
          items:
            type: string
        auth_type:
          type: string
          format: enum
        oauth:
          $ref: '#/components/schemas/ConnectorOAuth'
        auth_status:
          $ref: '#/components/schemas/ConnectorAuthStatus'
        active:
          type: boolean
        continue_on_failure:
          type: boolean
      required:
        - id
        - name
        - created_at
        - updated_at
    ListConnectorsResponse:
      type: object
      properties:
        connectors:
          type: array
          items:
            $ref: '#/components/schemas/Connector'
        total_count:
          type: number
          format: double
      required:
        - connectors

```

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

	resp, err := co.Connectors.List(
		context.TODO(),
		&cohere.ConnectorsListRequest{})

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```python Sync
import cohere

co = cohere.Client()
response = co.connectors.list()
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.connectors.list()
    print(response)


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.types.ListConnectorsResponse;

public class ConnectorsList {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ListConnectorsResponse list = cohere.connectors().list();

    System.out.println(list);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const connectors = await cohere.connectors.list();

  console.log(connectors);
})();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/connectors")

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

$response = $client->request('GET', 'https://api.cohere.com/v1/connectors', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/connectors");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/connectors")! as URL,
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

# Create a Connector

POST https://api.cohere.com/v1/connectors
Content-Type: application/json

Creates a new connector. The connector is tested during registration and will cancel registration when the test is unsuccessful. See ['Creating and Deploying a Connector'](https://docs.cohere.com/v1/docs/creating-and-deploying-a-connector) for more information.

Reference: https://docs.cohere.com/reference/create-connector

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create a Connector
  version: endpoint_connectors.create
paths:
  /v1/connectors:
    post:
      operationId: create
      summary: Create a Connector
      description: >-
        Creates a new connector. The connector is tested during registration and
        will cancel registration when the test is unsuccessful. See ['Creating
        and Deploying a
        Connector'](https://docs.cohere.com/v1/docs/creating-and-deploying-a-connector)
        for more information.
      tags:
        - - subpackage_connectors
      parameters:
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateConnectorResponse'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateConnectorRequest'
components:
  schemas:
    CreateConnectorOAuth:
      type: object
      properties:
        client_id:
          type: string
        client_secret:
          type: string
        authorize_url:
          type: string
        token_url:
          type: string
        scope:
          type: string
    AuthTokenType:
      type: string
      enum:
        - value: bearer
        - value: basic
        - value: noscheme
    CreateConnectorServiceAuth:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/AuthTokenType'
        token:
          type: string
      required:
        - type
        - token
    CreateConnectorRequest:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        url:
          type: string
        excludes:
          type: array
          items:
            type: string
        oauth:
          $ref: '#/components/schemas/CreateConnectorOAuth'
        active:
          type: boolean
        continue_on_failure:
          type: boolean
        service_auth:
          $ref: '#/components/schemas/CreateConnectorServiceAuth'
      required:
        - name
        - url
    ConnectorOAuth:
      type: object
      properties:
        client_id:
          type: string
        client_secret:
          type: string
        authorize_url:
          type: string
        token_url:
          type: string
        scope:
          type: string
      required:
        - authorize_url
        - token_url
    ConnectorAuthStatus:
      type: string
      enum:
        - value: valid
        - value: expired
    Connector:
      type: object
      properties:
        id:
          type: string
        organization_id:
          type: string
        name:
          type: string
        description:
          type: string
        url:
          type: string
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        excludes:
          type: array
          items:
            type: string
        auth_type:
          type: string
          format: enum
        oauth:
          $ref: '#/components/schemas/ConnectorOAuth'
        auth_status:
          $ref: '#/components/schemas/ConnectorAuthStatus'
        active:
          type: boolean
        continue_on_failure:
          type: boolean
      required:
        - id
        - name
        - created_at
        - updated_at
    CreateConnectorResponse:
      type: object
      properties:
        connector:
          $ref: '#/components/schemas/Connector'
      required:
        - connector

```

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

	resp, err := co.Connectors.Create(
		context.TODO(),
		&cohere.CreateConnectorRequest{
			Name: "Example connector",
			Url:  "https://you-connector-url",
			ServiceAuth: &cohere.CreateConnectorServiceAuth{
				Token: "dummy-connector-token",
				Type:  "bearer",
			},
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
response = co.connectors.create(
    name="Example connector",
    url="https://connector-example.com/search",
)
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.connectors.create(
        name="Example connector",
        url="https://connector-example.com/search",
    )
    print(response)


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.connectors.requests.CreateConnectorRequest;
import com.cohere.api.types.CreateConnectorResponse;

public class ConnectorCreate {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    CreateConnectorResponse response =
        cohere
            .connectors()
            .create(
                CreateConnectorRequest.builder()
                    .name("Example connector")
                    .url("https://connector-example.com/search")
                    .build());

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const connector = await cohere.connectors.create({
    name: 'test-connector',
    url: 'https://example.com/search',
    description: 'A test connector',
  });

  console.log(connector);
})();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/connectors")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"string\",\n  \"url\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/connectors', [
  'body' => '{
  "name": "string",
  "url": "string"
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
var client = new RestClient("https://api.cohere.com/v1/connectors");
var request = new RestRequest(Method.POST);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"string\",\n  \"url\": \"string\"\n}", ParameterType.RequestBody);
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
  "url": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/connectors")! as URL,
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

# Get a Connector

GET https://api.cohere.com/v1/connectors/{id}

Retrieve a connector by ID. See ['Connectors'](https://docs.cohere.com/docs/connectors) for more information.

Reference: https://docs.cohere.com/reference/get-connector

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get a Connector
  version: endpoint_connectors.get
paths:
  /v1/connectors/{id}:
    get:
      operationId: get
      summary: Get a Connector
      description: >-
        Retrieve a connector by ID. See
        ['Connectors'](https://docs.cohere.com/docs/connectors) for more
        information.
      tags:
        - - subpackage_connectors
      parameters:
        - name: id
          in: path
          description: The ID of the connector to retrieve.
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetConnectorResponse'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
components:
  schemas:
    ConnectorOAuth:
      type: object
      properties:
        client_id:
          type: string
        client_secret:
          type: string
        authorize_url:
          type: string
        token_url:
          type: string
        scope:
          type: string
      required:
        - authorize_url
        - token_url
    ConnectorAuthStatus:
      type: string
      enum:
        - value: valid
        - value: expired
    Connector:
      type: object
      properties:
        id:
          type: string
        organization_id:
          type: string
        name:
          type: string
        description:
          type: string
        url:
          type: string
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        excludes:
          type: array
          items:
            type: string
        auth_type:
          type: string
          format: enum
        oauth:
          $ref: '#/components/schemas/ConnectorOAuth'
        auth_status:
          $ref: '#/components/schemas/ConnectorAuthStatus'
        active:
          type: boolean
        continue_on_failure:
          type: boolean
      required:
        - id
        - name
        - created_at
        - updated_at
    GetConnectorResponse:
      type: object
      properties:
        connector:
          $ref: '#/components/schemas/Connector'
      required:
        - connector

```

## SDK Code Examples

```go Cohere Go SDK
package main

import (
	"context"
	"log"
	"os"

	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Connectors.Get(context.TODO(), "connector_id")

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```python Sync
import cohere

co = cohere.Client()
response = co.connectors.get("test-id")
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.connectors.get("test-id")
    print(response)


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.types.GetConnectorResponse;

public class ConnectorGet {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    GetConnectorResponse response = cohere.connectors().get("test-id");

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const connector = await cohere.connectors.get('connector-id');

  console.log(connector);
})();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/connectors/id")

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

$response = $client->request('GET', 'https://api.cohere.com/v1/connectors/id', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/connectors/id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/connectors/id")! as URL,
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

# Update a Connector

PATCH https://api.cohere.com/v1/connectors/{id}
Content-Type: application/json

Update a connector by ID. Omitted fields will not be updated. See ['Managing your Connector'](https://docs.cohere.com/docs/managing-your-connector) for more information.

Reference: https://docs.cohere.com/reference/update-connector

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update a Connector
  version: endpoint_connectors.update
paths:
  /v1/connectors/{id}:
    patch:
      operationId: update
      summary: Update a Connector
      description: >-
        Update a connector by ID. Omitted fields will not be updated. See
        ['Managing your
        Connector'](https://docs.cohere.com/docs/managing-your-connector) for
        more information.
      tags:
        - - subpackage_connectors
      parameters:
        - name: id
          in: path
          description: The ID of the connector to update.
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateConnectorResponse'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateConnectorRequest'
components:
  schemas:
    CreateConnectorOAuth:
      type: object
      properties:
        client_id:
          type: string
        client_secret:
          type: string
        authorize_url:
          type: string
        token_url:
          type: string
        scope:
          type: string
    AuthTokenType:
      type: string
      enum:
        - value: bearer
        - value: basic
        - value: noscheme
    CreateConnectorServiceAuth:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/AuthTokenType'
        token:
          type: string
      required:
        - type
        - token
    UpdateConnectorRequest:
      type: object
      properties:
        name:
          type: string
        url:
          type: string
        excludes:
          type: array
          items:
            type: string
        oauth:
          $ref: '#/components/schemas/CreateConnectorOAuth'
        active:
          type: boolean
        continue_on_failure:
          type: boolean
        service_auth:
          $ref: '#/components/schemas/CreateConnectorServiceAuth'
    ConnectorOAuth:
      type: object
      properties:
        client_id:
          type: string
        client_secret:
          type: string
        authorize_url:
          type: string
        token_url:
          type: string
        scope:
          type: string
      required:
        - authorize_url
        - token_url
    ConnectorAuthStatus:
      type: string
      enum:
        - value: valid
        - value: expired
    Connector:
      type: object
      properties:
        id:
          type: string
        organization_id:
          type: string
        name:
          type: string
        description:
          type: string
        url:
          type: string
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        excludes:
          type: array
          items:
            type: string
        auth_type:
          type: string
          format: enum
        oauth:
          $ref: '#/components/schemas/ConnectorOAuth'
        auth_status:
          $ref: '#/components/schemas/ConnectorAuthStatus'
        active:
          type: boolean
        continue_on_failure:
          type: boolean
      required:
        - id
        - name
        - created_at
        - updated_at
    UpdateConnectorResponse:
      type: object
      properties:
        connector:
          $ref: '#/components/schemas/Connector'
      required:
        - connector

```

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

	resp, err := co.Connectors.Update(
		context.TODO(),
		"connector_id",
		&cohere.UpdateConnectorRequest{
			Name: cohere.String("Example connector renamed"),
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
response = co.connectors.update(
    connector_id="test-id", name="new name", url="https://example.com/search"
)
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.connectors.update(
        connector_id="test-id", name="new name", url="https://example.com/search"
    )
    print(response)


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.connectors.requests.UpdateConnectorRequest;

public class ConnectorPatch {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    cohere
        .connectors()
        .update(
            "test-id",
            UpdateConnectorRequest.builder()
                .name("new name")
                .url("https://connector-example.com/search")
                .build());
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const connector = await cohere.connectors.update(connector.id, {
    name: 'test-connector-renamed',
    description: 'A test connector renamed',
  });

  console.log(connector);
})();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/connectors/id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.cohere.com/v1/connectors/id', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/connectors/id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/connectors/id")! as URL,
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

# Delete a Connector

DELETE https://api.cohere.com/v1/connectors/{id}

Delete a connector by ID. See ['Connectors'](https://docs.cohere.com/docs/connectors) for more information.

Reference: https://docs.cohere.com/reference/delete-connector

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete a Connector
  version: endpoint_connectors.delete
paths:
  /v1/connectors/{id}:
    delete:
      operationId: delete
      summary: Delete a Connector
      description: >-
        Delete a connector by ID. See
        ['Connectors'](https://docs.cohere.com/docs/connectors) for more
        information.
      tags:
        - - subpackage_connectors
      parameters:
        - name: id
          in: path
          description: The ID of the connector to delete.
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteConnectorResponse'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
components:
  schemas:
    DeleteConnectorResponse:
      type: object
      properties: {}

```

## SDK Code Examples

```go Cohere Go SDK
package main

import (
	"context"
	"log"
	"os"

	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Connectors.Delete(context.TODO(), "connector_id")

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
  await cohere.connectors.delete('connector-id');
})();

```

```python Sync
import cohere

co = cohere.Client()
co.connectors.delete("test-id")

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    await co.connectors.delete("test-id")


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;

public class ConnectorDelete {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    cohere.connectors().delete("test-id");
  }
}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/connectors/id")

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

$response = $client->request('DELETE', 'https://api.cohere.com/v1/connectors/id', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/connectors/id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/connectors/id")! as URL,
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

# Authorize with oAuth

POST https://api.cohere.com/v1/connectors/{id}/oauth/authorize

Authorize the connector with the given ID for the connector oauth app.  See ['Connector Authentication'](https://docs.cohere.com/docs/connector-authentication) for more information.

Reference: https://docs.cohere.com/reference/oauthauthorize-connector

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Authorize with oAuth
  version: endpoint_connectors.oAuthAuthorize
paths:
  /v1/connectors/{id}/oauth/authorize:
    post:
      operationId: o-auth-authorize
      summary: Authorize with oAuth
      description: >-
        Authorize the connector with the given ID for the connector oauth app. 
        See ['Connector
        Authentication'](https://docs.cohere.com/docs/connector-authentication)
        for more information.
      tags:
        - - subpackage_connectors
      parameters:
        - name: id
          in: path
          description: The ID of the connector to authorize.
          required: true
          schema:
            type: string
        - name: after_token_redirect
          in: query
          description: The URL to redirect to after the connector has been authorized.
          required: false
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OAuthAuthorizeResponse'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content: {}
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content: {}
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content: {}
        '429':
          description: Too many requests
          content: {}
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content: {}
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content: {}
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content: {}
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content: {}
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content: {}
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content: {}
components:
  schemas:
    OAuthAuthorizeResponse:
      type: object
      properties:
        redirect_url:
          type: string

```

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

# Lists fine-tuned models.

GET https://api.cohere.com/v1/finetuning/finetuned-models

Returns a list of fine-tuned models that the user has access to.

Reference: https://docs.cohere.com/reference/listfinetunedmodels

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Lists fine-tuned models.
  version: endpoint_finetuning.ListFinetunedModels
paths:
  /v1/finetuning/finetuned-models:
    get:
      operationId: list-finetuned-models
      summary: Lists fine-tuned models.
      description: Returns a list of fine-tuned models that the user has access to.
      tags:
        - - subpackage_finetuning
      parameters:
        - name: page_size
          in: query
          description: >-
            Maximum number of results to be returned by the server. If 0,
            defaults to

            50.
          required: false
          schema:
            type: integer
        - name: page_token
          in: query
          description: Request a specific page of the list results.
          required: false
          schema:
            type: string
        - name: order_by
          in: query
          description: >-
            Comma separated list of fields. For example: "created_at,name". The
            default

            sorting order is ascending. To specify descending order for a field,
            append

            " desc" to the field name. For example: "created_at desc,name".


            Supported sorting fields:
              - created_at (default)
          required: false
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListFinetunedModelsResponse'
        '400':
          description: Bad Request
          content: {}
        '401':
          description: Unauthorized
          content: {}
        '403':
          description: Forbidden
          content: {}
        '404':
          description: Not Found
          content: {}
        '500':
          description: Internal Server Error
          content: {}
        '503':
          description: Status Service Unavailable
          content: {}
components:
  schemas:
    BaseType:
      type: string
      enum:
        - value: BASE_TYPE_UNSPECIFIED
        - value: BASE_TYPE_GENERATIVE
        - value: BASE_TYPE_CLASSIFICATION
        - value: BASE_TYPE_RERANK
        - value: BASE_TYPE_CHAT
    Strategy:
      type: string
      enum:
        - value: STRATEGY_UNSPECIFIED
        - value: STRATEGY_VANILLA
        - value: STRATEGY_TFEW
    BaseModel:
      type: object
      properties:
        name:
          type: string
        version:
          type: string
        base_type:
          $ref: '#/components/schemas/BaseType'
        strategy:
          $ref: '#/components/schemas/Strategy'
      required:
        - base_type
    LoraTargetModules:
      type: string
      enum:
        - value: LORA_TARGET_MODULES_UNSPECIFIED
        - value: LORA_TARGET_MODULES_QV
        - value: LORA_TARGET_MODULES_QKVO
        - value: LORA_TARGET_MODULES_QKVO_FFN
    Hyperparameters:
      type: object
      properties:
        early_stopping_patience:
          type: integer
        early_stopping_threshold:
          type: number
          format: double
        train_batch_size:
          type: integer
        train_epochs:
          type: integer
        learning_rate:
          type: number
          format: double
        lora_alpha:
          type: integer
        lora_rank:
          type: integer
        lora_target_modules:
          $ref: '#/components/schemas/LoraTargetModules'
    WandbConfig:
      type: object
      properties:
        project:
          type: string
        api_key:
          type: string
        entity:
          type: string
      required:
        - project
        - api_key
    Settings:
      type: object
      properties:
        base_model:
          $ref: '#/components/schemas/BaseModel'
        dataset_id:
          type: string
        hyperparameters:
          $ref: '#/components/schemas/Hyperparameters'
        multi_label:
          type: boolean
        wandb:
          $ref: '#/components/schemas/WandbConfig'
      required:
        - base_model
        - dataset_id
    Status:
      type: string
      enum:
        - value: STATUS_UNSPECIFIED
        - value: STATUS_FINETUNING
        - value: STATUS_DEPLOYING_API
        - value: STATUS_READY
        - value: STATUS_FAILED
        - value: STATUS_DELETED
        - value: STATUS_TEMPORARILY_OFFLINE
        - value: STATUS_PAUSED
        - value: STATUS_QUEUED
    FinetunedModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        creator_id:
          type: string
        organization_id:
          type: string
        settings:
          $ref: '#/components/schemas/Settings'
        status:
          $ref: '#/components/schemas/Status'
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        completed_at:
          type: string
          format: date-time
        last_used:
          type: string
          format: date-time
      required:
        - name
        - settings
    ListFinetunedModelsResponse:
      type: object
      properties:
        finetuned_models:
          type: array
          items:
            $ref: '#/components/schemas/FinetunedModel'
        next_page_token:
          type: string
        total_size:
          type: integer

```

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

# Trains and deploys a fine-tuned model.

POST https://api.cohere.com/v1/finetuning/finetuned-models
Content-Type: application/json

Creates a new fine-tuned model. The model will be trained on the dataset specified in the request body. The training process may take some time, and the model will be available once the training is complete.

Reference: https://docs.cohere.com/reference/createfinetunedmodel

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Trains and deploys a fine-tuned model.
  version: endpoint_finetuning.CreateFinetunedModel
paths:
  /v1/finetuning/finetuned-models:
    post:
      operationId: create-finetuned-model
      summary: Trains and deploys a fine-tuned model.
      description: >-
        Creates a new fine-tuned model. The model will be trained on the dataset
        specified in the request body. The training process may take some time,
        and the model will be available once the training is complete.
      tags:
        - - subpackage_finetuning
      parameters:
        - name: Authorization
          in: header
          description: >-
            Bearer authentication of the form `Bearer <token>`, where token is
            your auth token.
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateFinetunedModelResponse'
        '400':
          description: Bad Request
          content: {}
        '401':
          description: Unauthorized
          content: {}
        '403':
          description: Forbidden
          content: {}
        '404':
          description: Not Found
          content: {}
        '500':
          description: Internal Server Error
          content: {}
        '503':
          description: Status Service Unavailable
          content: {}
      requestBody:
        description: >-
          Information about the fine-tuned model. Must contain name and
          settings.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FinetunedModel'
components:
  schemas:
    BaseType:
      type: string
      enum:
        - value: BASE_TYPE_UNSPECIFIED
        - value: BASE_TYPE_GENERATIVE
        - value: BASE_TYPE_CLASSIFICATION
        - value: BASE_TYPE_RERANK
        - value: BASE_TYPE_CHAT
    Strategy:
      type: string
      enum:
        - value: STRATEGY_UNSPECIFIED
        - value: STRATEGY_VANILLA
        - value: STRATEGY_TFEW
    BaseModel:
      type: object
      properties:
        name:
          type: string
        version:
          type: string
        base_type:
          $ref: '#/components/schemas/BaseType'
        strategy:
          $ref: '#/components/schemas/Strategy'
      required:
        - base_type
    LoraTargetModules:
      type: string
      enum:
        - value: LORA_TARGET_MODULES_UNSPECIFIED
        - value: LORA_TARGET_MODULES_QV
        - value: LORA_TARGET_MODULES_QKVO
        - value: LORA_TARGET_MODULES_QKVO_FFN
    Hyperparameters:
      type: object
      properties:
        early_stopping_patience:
          type: integer
        early_stopping_threshold:
          type: number
          format: double
        train_batch_size:
          type: integer
        train_epochs:
          type: integer
        learning_rate:
          type: number
          format: double
        lora_alpha:
          type: integer
        lora_rank:
          type: integer
        lora_target_modules:
          $ref: '#/components/schemas/LoraTargetModules'
    WandbConfig:
      type: object
      properties:
        project:
          type: string
        api_key:
          type: string
        entity:
          type: string
      required:
        - project
        - api_key
    Settings:
      type: object
      properties:
        base_model:
          $ref: '#/components/schemas/BaseModel'
        dataset_id:
          type: string
        hyperparameters:
          $ref: '#/components/schemas/Hyperparameters'
        multi_label:
          type: boolean
        wandb:
          $ref: '#/components/schemas/WandbConfig'
      required:
        - base_model
        - dataset_id
    Status:
      type: string
      enum:
        - value: STATUS_UNSPECIFIED
        - value: STATUS_FINETUNING
        - value: STATUS_DEPLOYING_API
        - value: STATUS_READY
        - value: STATUS_FAILED
        - value: STATUS_DELETED
        - value: STATUS_TEMPORARILY_OFFLINE
        - value: STATUS_PAUSED
        - value: STATUS_QUEUED
    FinetunedModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        creator_id:
          type: string
        organization_id:
          type: string
        settings:
          $ref: '#/components/schemas/Settings'
        status:
          $ref: '#/components/schemas/Status'
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        completed_at:
          type: string
          format: date-time
        last_used:
          type: string
          format: date-time
      required:
        - name
        - settings
    CreateFinetunedModelResponse:
      type: object
      properties:
        finetuned_model:
          $ref: '#/components/schemas/FinetunedModel'

```

## SDK Code Examples

```java Cohere java SDK
/* (C)2024 */
package finetuning;

import com.cohere.api.Cohere;
import com.cohere.api.resources.finetuning.finetuning.types.*;

public class CreateFinetunedModel {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    CreateFinetunedModelResponse response =
        cohere
            .finetuning()
            .createFinetunedModel(
                FinetunedModel.builder()
                    .name("test-finetuned-model")
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

	"github.com/cohere-ai/cohere-go/v2/client"
	"github.com/cohere-ai/cohere-go/v2/finetuning"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Finetuning.CreateFinetunedModel(
		context.TODO(),
		&finetuning.FinetunedModel{
			Name: "test-finetuned-model",
			Settings: &finetuning.Settings{
				DatasetId: "my-dataset-id",
				BaseModel: &finetuning.BaseModel{
					BaseType: finetuning.BaseTypeBaseTypeChat,
				},
			},
		},
	)
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp.FinetunedModel)
}

```

```typescript Cohere TypeScript SDK
const { Cohere, CohereClient } = require('cohere-ai');

const cohere = new CohereClient({
  token: '<<apiKey>>',
});

(async () => {
  const finetunedModel = await cohere.finetuning.createFinetunedModel({
    name: 'test-finetuned-model',
    settings: {
      base_model: {
        base_type: Cohere.Finetuning.BaseType.BaseTypeChat,
      },
      dataset_id: 'test-dataset-id',
    },
  });

  console.log(finetunedModel);
})();

```

```python Sync
from cohere.finetuning import (
    BaseModel,
    FinetunedModel,
    Hyperparameters,
    Settings,
    WandbConfig,
)
import cohere

co = cohere.Client()
hp = Hyperparameters(
    early_stopping_patience=10,
    early_stopping_threshold=0.001,
    train_batch_size=16,
    train_epochs=1,
    learning_rate=0.01,
)
wnb_config = WandbConfig(
    project="test-project",
    api_key="<<wandbApiKey>>",
    entity="test-entity",
)
finetuned_model = co.finetuning.create_finetuned_model(
    request=FinetunedModel(
        name="test-finetuned-model",
        settings=Settings(
            base_model=BaseModel(
                base_type="BASE_TYPE_CHAT",
            ),
            dataset_id="my-dataset-id",
            hyperparameters=hp,
            wandb=wnb_config,
        ),
    )
)
print(finetuned_model)

```

```python Async
from cohere.finetuning import (
    BaseModel,
    FinetunedModel,
    Settings,
)
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.finetuning.create_finetuned_model(
        request=FinetunedModel(
            name="test-finetuned-model",
            settings=Settings(
                base_model=BaseModel(
                    base_type="BASE_TYPE_CHAT",
                ),
                dataset_id="my-dataset-id",
            ),
        )
    )
    print(response)


asyncio.run(main())

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/finetuning/finetuned-models")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
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

$response = $client->request('POST', 'https://api.cohere.com/v1/finetuning/finetuned-models', [
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
var client = new RestClient("https://api.cohere.com/v1/finetuning/finetuned-models");
var request = new RestRequest(Method.POST);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/finetuning/finetuned-models")! as URL,
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

**Navigation:** [← Previous](./11-embed-api-v2.md) | [Index](./index.md) | [Next →](./13-updates-a-fine-tuned-model.md)
