**Navigation:** [← Previous](./10-chat-with-streaming.md) | [Index](./index.md) | [Next →](./12-delete-a-dataset.md)

---

# Embed API (v2)

POST https://api.cohere.com/v2/embed
Content-Type: application/json

This endpoint returns text embeddings. An embedding is a list of floating point numbers that captures semantic information about the text that it represents.

Embeddings can be used to create text classifiers as well as empower semantic search. To learn more about embeddings, see the embedding page.

If you want to learn more how to use the embedding model, have a look at the [Semantic Search Guide](https://docs.cohere.com/docs/semantic-search).

Reference: https://docs.cohere.com/reference/embed

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Embed API (v2)
  version: endpoint_v2.embed
paths:
  /v2/embed:
    post:
      operationId: embed
      summary: Embed API (v2)
      description: >-
        This endpoint returns text embeddings. An embedding is a list of
        floating point numbers that captures semantic information about the text
        that it represents.


        Embeddings can be used to create text classifiers as well as empower
        semantic search. To learn more about embeddings, see the embedding page.


        If you want to learn more how to use the embedding model, have a look at
        the [Semantic Search
        Guide](https://docs.cohere.com/docs/semantic-search).
      tags:
        - - subpackage_v2
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
                $ref: '#/components/schemas/EmbedByTypeResponse'
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
                texts:
                  type: array
                  items:
                    type: string
                images:
                  type: array
                  items:
                    type: string
                model:
                  type: string
                input_type:
                  $ref: '#/components/schemas/EmbedInputType'
                inputs:
                  type: array
                  items:
                    $ref: '#/components/schemas/EmbedInput'
                max_tokens:
                  type: integer
                output_dimension:
                  type: integer
                embedding_types:
                  type: array
                  items:
                    $ref: '#/components/schemas/EmbeddingType'
                truncate:
                  $ref: >-
                    #/components/schemas/V2EmbedPostRequestBodyContentApplicationJsonSchemaTruncate
                priority:
                  type: integer
              required:
                - model
                - input_type
components:
  schemas:
    EmbedInputType:
      type: string
      enum:
        - value: search_document
        - value: search_query
        - value: classification
        - value: clustering
        - value: image
    EmbedContentType:
      type: string
      enum:
        - value: text
        - value: image_url
    EmbedImageUrl:
      type: object
      properties:
        url:
          type: string
      required:
        - url
    EmbedImage:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/EmbedContentType'
        image_url:
          $ref: '#/components/schemas/EmbedImageUrl'
    EmbedText:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/EmbedContentType'
        text:
          type: string
    EmbedContent:
      oneOf:
        - $ref: '#/components/schemas/EmbedImage'
        - $ref: '#/components/schemas/EmbedText'
    EmbedInput:
      type: object
      properties:
        content:
          type: array
          items:
            $ref: '#/components/schemas/EmbedContent'
      required:
        - content
    EmbeddingType:
      type: string
      enum:
        - value: float
        - value: int8
        - value: uint8
        - value: binary
        - value: ubinary
        - value: base64
    V2EmbedPostRequestBodyContentApplicationJsonSchemaTruncate:
      type: string
      enum:
        - value: NONE
        - value: START
        - value: END
    EmbedByTypeResponseResponseType:
      type: string
      enum:
        - value: embeddings_floats
        - value: embeddings_by_type
    EmbedByTypeResponseEmbeddings:
      type: object
      properties:
        float:
          type: array
          items:
            type: array
            items:
              type: number
              format: double
        int8:
          type: array
          items:
            type: array
            items:
              type: integer
        uint8:
          type: array
          items:
            type: array
            items:
              type: integer
        binary:
          type: array
          items:
            type: array
            items:
              type: integer
        ubinary:
          type: array
          items:
            type: array
            items:
              type: integer
        base64:
          type: array
          items:
            type: string
    Image:
      type: object
      properties:
        width:
          type: integer
          format: int64
        height:
          type: integer
          format: int64
        format:
          type: string
        bit_depth:
          type: integer
          format: int64
      required:
        - width
        - height
        - format
        - bit_depth
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
    EmbedByTypeResponse:
      type: object
      properties:
        response_type:
          $ref: '#/components/schemas/EmbedByTypeResponseResponseType'
        id:
          type: string
        embeddings:
          $ref: '#/components/schemas/EmbedByTypeResponseEmbeddings'
        texts:
          type: array
          items:
            type: string
        images:
          type: array
          items:
            $ref: '#/components/schemas/Image'
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - id
        - embeddings

```

## SDK Code Examples

```go Texts
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	"github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.Embed(
		context.TODO(),
		&cohere.V2EmbedRequest{
			Texts:          []string{"hello", "goodbye"},
			Model:          "embed-v4.0",
			InputType:      cohere.EmbedInputTypeSearchDocument,
			EmbeddingTypes: []cohere.EmbeddingType{cohere.EmbeddingTypeFloat},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```typescript Texts
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const embed = await cohere.v2.embed({
    texts: ['hello', 'goodbye'],
    model: 'embed-v4.0',
    inputType: 'classification',
    embeddingTypes: ['float'],
  });
  console.log(embed);
})();

```

```python Texts
import cohere

co = cohere.ClientV2()

text_inputs = [
    {
        "content": [
            {"type": "text", "text": "hello"},
            {"type": "text", "text": "goodbye"}
        ]
    },
]

response = co.embed(
    inputs=text_inputs,
    model="embed-v4.0",
    input_type="classification",
    embedding_types=["float"],
)
print(response)

```

```python Texts (async)
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.embed(
        texts=["hello", "goodbye"],
        model="embed-v4.0",
        input_type="classification",
    )
    print(response)


asyncio.run(main())

```

```java Texts
package embedv2post; /* (C)2024 */

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2EmbedRequest;
import com.cohere.api.types.EmbedByTypeResponse;
import com.cohere.api.types.EmbedInputType;
import java.util.List;

public class EmbedPost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    EmbedByTypeResponse response =
        cohere
            .v2()
            .embed(
                V2EmbedRequest.builder()
                    .model("embed-v4.0")
                    .inputType(EmbedInputType.CLASSIFICATION)
                    .texts(List.of("hello", "goodbye"))
                    .build());

    System.out.println(response);
  }
}

```

```ruby Texts
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/embed")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model\": \"embed-v4.0\",\n  \"input_type\": \"classification\",\n  \"texts\": [\n    \"hello\",\n    \"goodbye\"\n  ],\n  \"embedding_types\": [\n    \"float\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Texts
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/embed', [
  'body' => '{
  "model": "embed-v4.0",
  "input_type": "classification",
  "texts": [
    "hello",
    "goodbye"
  ],
  "embedding_types": [
    "float"
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Texts
var client = new RestClient("https://api.cohere.com/v2/embed");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model\": \"embed-v4.0\",\n  \"input_type\": \"classification\",\n  \"texts\": [\n    \"hello\",\n    \"goodbye\"\n  ],\n  \"embedding_types\": [\n    \"float\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Texts
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "model": "embed-v4.0",
  "input_type": "classification",
  "texts": ["hello", "goodbye"],
  "embedding_types": ["float"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/embed")! as URL,
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

```go Images
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	"github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	// Fetch the image
	resp, err := http.Get("https://cohere.com/favicon-32x32.png")
	if err != nil {
		log.Println("Error fetching the image:", err)
		return
	}
	defer resp.Body.Close()

	// Read the image content
	buffer, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Println("Error reading the image content:", err)
		return
	}

	stringifiedBuffer := base64.StdEncoding.EncodeToString(buffer)
	contentType := resp.Header.Get("Content-Type")
	imageBase64 := fmt.Sprintf("data:%s;base64,%s", contentType, stringifiedBuffer)

	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	embed, err := co.V2.Embed(
		context.TODO(),
		&cohere.V2EmbedRequest{
			Images:         []string{imageBase64},
			Model:          "embed-v4.0",
			InputType:      cohere.EmbedInputTypeImage,
			EmbeddingTypes: []cohere.EmbeddingType{cohere.EmbeddingTypeFloat},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", embed)
}

```

```typescript Images
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const image = await fetch('https://cohere.com/favicon-32x32.png');
  const buffer = await image.arrayBuffer();
  const stringifiedBuffer = Buffer.from(buffer).toString('base64');
  const contentType = image.headers.get('content-type');
  const imageBase64 = `data:${contentType};base64,${stringifiedBuffer}`;

  const embed = await cohere.v2.embed({
    model: 'embed-v4.0',
    inputType: 'image',
    embeddingTypes: ['float'],
    images: [imageBase64],
  });
  console.log(embed);
})();

```

```python Images
import cohere
import requests
import base64

co = cohere.ClientV2()

image = requests.get("https://cohere.com/favicon-32x32.png")
stringified_buffer = base64.b64encode(image.content).decode("utf-8")
content_type = image.headers["Content-Type"]
image_base64 = f"data:{content_type};base64,{stringified_buffer}"

image_inputs = [
    {
        "content": [
            {
                "type": "image_url",
                "image_url": {"url": image_base64}
            }
        ]
    }
]

response = co.embed(
    model="embed-v4.0",
    input_type="image",
    embedding_types=["float"],
    inputs=image_inputs
)

print(response)

```

```java Images
package embedv2post; /* (C)2024 */

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2EmbedRequest;
import com.cohere.api.types.EmbedByTypeResponse;
import com.cohere.api.types.EmbedInputType;
import com.cohere.api.types.EmbeddingType;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;
import java.util.Base64;
import java.util.List;

public class EmbedImagePost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    try {
      URI uri = URI.create("https://cohere.com/favicon-32x32.png");
      URL url = uri.toURL();
      HttpURLConnection connection = (HttpURLConnection) url.openConnection();
      connection.connect();

      InputStream inputStream = connection.getInputStream();
      byte[] buffer = inputStream.readAllBytes();
      inputStream.close();

      String imageBase64 =
          String.format(
              "data:%s;base64,%s",
              connection.getHeaderField("Content-Type"),
              Base64.getEncoder().encodeToString(buffer));

      EmbedByTypeResponse response =
          cohere
              .v2()
              .embed(
                  V2EmbedRequest.builder()
                      .model("embed-v4.0")
                      .inputType(EmbedInputType.IMAGE)
                      .images(List.of(imageBase64))
                      .embeddingTypes(List.of(EmbeddingType.FLOAT))
                      .build());

      System.out.println(response);
    } catch (MalformedURLException e) {
      System.err.println("Invalid URL: " + e.getMessage());
    } catch (IOException e) {
      System.err.println("I/O error: " + e.getMessage());
    }
  }
}

```

```ruby Images
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/embed")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model\": \"embed-v4.0\",\n  \"input_type\": \"image\",\n  \"images\": [\n    \"data:image/jpeg;base64,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\"\n  ],\n  \"embedding_types\": [\n    \"float\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Images
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/embed', [
  'body' => '{
  "model": "embed-v4.0",
  "input_type": "image",
  "images": [
    "data:image/jpeg;base64,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"
  ],
  "embedding_types": [
    "float"
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Images
var client = new RestClient("https://api.cohere.com/v2/embed");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model\": \"embed-v4.0\",\n  \"input_type\": \"image\",\n  \"images\": [\n    \"data:image/jpeg;base64,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\"\n  ],\n  \"embedding_types\": [\n    \"float\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Images
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "model": "embed-v4.0",
  "input_type": "image",
  "images": ["data:image/jpeg;base64,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"],
  "embedding_types": ["float"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/embed")! as URL,
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

# Create an Embed Job

POST https://api.cohere.com/v1/embed-jobs
Content-Type: application/json

This API launches an async Embed job for a [Dataset](https://docs.cohere.com/docs/datasets) of type `embed-input`. The result of a completed embed job is new Dataset of type `embed-output`, which contains the original text entries and the corresponding embeddings.

Reference: https://docs.cohere.com/reference/create-embed-job

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create an Embed Job
  version: endpoint_embedJobs.create
paths:
  /v1/embed-jobs:
    post:
      operationId: create
      summary: Create an Embed Job
      description: >-
        This API launches an async Embed job for a
        [Dataset](https://docs.cohere.com/docs/datasets) of type `embed-input`.
        The result of a completed embed job is new Dataset of type
        `embed-output`, which contains the original text entries and the
        corresponding embeddings.
      tags:
        - - subpackage_embedJobs
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
                $ref: '#/components/schemas/CreateEmbedJobResponse'
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
              $ref: '#/components/schemas/CreateEmbedJobRequest'
components:
  schemas:
    EmbedInputType:
      type: string
      enum:
        - value: search_document
        - value: search_query
        - value: classification
        - value: clustering
        - value: image
    EmbeddingType:
      type: string
      enum:
        - value: float
        - value: int8
        - value: uint8
        - value: binary
        - value: ubinary
        - value: base64
    CreateEmbedJobRequestTruncate:
      type: string
      enum:
        - value: START
        - value: END
    CreateEmbedJobRequest:
      type: object
      properties:
        model:
          type: string
          format: string
        dataset_id:
          type: string
        input_type:
          $ref: '#/components/schemas/EmbedInputType'
        name:
          type: string
        embedding_types:
          type: array
          items:
            $ref: '#/components/schemas/EmbeddingType'
        truncate:
          $ref: '#/components/schemas/CreateEmbedJobRequestTruncate'
      required:
        - model
        - dataset_id
        - input_type
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
    CreateEmbedJobResponse:
      type: object
      properties:
        job_id:
          type: string
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - job_id

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

	resp, err := co.EmbedJobs.Create(
		context.TODO(),
		&cohere.CreateEmbedJobRequest{
			DatasetId: "dataset_id",
			Model:     "embed-english-v3.0",
			InputType: cohere.EmbedInputTypeSearchDocument,
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

# start an embed job
job = co.embed_jobs.create(
    dataset_id="my-dataset-id", input_type="search_document", model="embed-english-v3.0"
)

# poll the server until the job is complete
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

# List Embed Jobs

GET https://api.cohere.com/v1/embed-jobs

The list embed job endpoint allows users to view all embed jobs history for that specific user.

Reference: https://docs.cohere.com/reference/list-embed-jobs

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List Embed Jobs
  version: endpoint_embedJobs.list
paths:
  /v1/embed-jobs:
    get:
      operationId: list
      summary: List Embed Jobs
      description: >-
        The list embed job endpoint allows users to view all embed jobs history
        for that specific user.
      tags:
        - - subpackage_embedJobs
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
                $ref: '#/components/schemas/ListEmbedJobResponse'
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
    EmbedJobStatus:
      type: string
      enum:
        - value: processing
        - value: complete
        - value: cancelling
        - value: cancelled
        - value: failed
    EmbedJobTruncate:
      type: string
      enum:
        - value: START
        - value: END
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
    EmbedJob:
      type: object
      properties:
        job_id:
          type: string
        name:
          type: string
        status:
          $ref: '#/components/schemas/EmbedJobStatus'
        created_at:
          type: string
          format: date-time
        input_dataset_id:
          type: string
        output_dataset_id:
          type: string
        model:
          type: string
        truncate:
          $ref: '#/components/schemas/EmbedJobTruncate'
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - job_id
        - status
        - created_at
        - input_dataset_id
        - model
        - truncate
    ListEmbedJobResponse:
      type: object
      properties:
        embed_jobs:
          type: array
          items:
            $ref: '#/components/schemas/EmbedJob'

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

	resp, err := co.EmbedJobs.Get(context.TODO(), "embed_job_id")

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```python Sync
import cohere

co = cohere.Client()

# list embed jobs
response = co.embed_jobs.list()

print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.embed_jobs.list()

    print(response)


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.types.ListEmbedJobResponse;

public class EmbedJobsGet {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ListEmbedJobResponse response = cohere.embedJobs().list();

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const embedJobs = await cohere.embedJobs.list();

  console.log(embedJobs);
})();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/embed-jobs")

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

$response = $client->request('GET', 'https://api.cohere.com/v1/embed-jobs', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/embed-jobs");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/embed-jobs")! as URL,
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

# Fetch an Embed Job

GET https://api.cohere.com/v1/embed-jobs/{id}

This API retrieves the details about an embed job started by the same user.

Reference: https://docs.cohere.com/reference/get-embed-job

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Fetch an Embed Job
  version: endpoint_embedJobs.get
paths:
  /v1/embed-jobs/{id}:
    get:
      operationId: get
      summary: Fetch an Embed Job
      description: >-
        This API retrieves the details about an embed job started by the same
        user.
      tags:
        - - subpackage_embedJobs
      parameters:
        - name: id
          in: path
          description: The ID of the embed job to retrieve.
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
                $ref: '#/components/schemas/EmbedJob'
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
    EmbedJobStatus:
      type: string
      enum:
        - value: processing
        - value: complete
        - value: cancelling
        - value: cancelled
        - value: failed
    EmbedJobTruncate:
      type: string
      enum:
        - value: START
        - value: END
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
    EmbedJob:
      type: object
      properties:
        job_id:
          type: string
        name:
          type: string
        status:
          $ref: '#/components/schemas/EmbedJobStatus'
        created_at:
          type: string
          format: date-time
        input_dataset_id:
          type: string
        output_dataset_id:
          type: string
        model:
          type: string
        truncate:
          $ref: '#/components/schemas/EmbedJobTruncate'
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - job_id
        - status
        - created_at
        - input_dataset_id
        - model
        - truncate

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

	resp, err := co.EmbedJobs.List(context.TODO())

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```python Sync
import cohere

co = cohere.Client()

# get embed job
response = co.embed_jobs.get("job_id")

print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.embed_jobs.get("job_id")

    print(response)


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.types.ListEmbedJobResponse;

public class EmbedJobsGet {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ListEmbedJobResponse response = cohere.embedJobs().list();

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const embedJob = await cohere.embedJobs.get('job_id');

  console.log(embedJob);
})();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/embed-jobs/id")

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

$response = $client->request('GET', 'https://api.cohere.com/v1/embed-jobs/id', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/embed-jobs/id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/embed-jobs/id")! as URL,
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

# Cancel an Embed Job

POST https://api.cohere.com/v1/embed-jobs/{id}/cancel

This API allows users to cancel an active embed job. Once invoked, the embedding process will be terminated, and users will be charged for the embeddings processed up to the cancellation point. It's important to note that partial results will not be available to users after cancellation.

Reference: https://docs.cohere.com/reference/cancel-embed-job

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Cancel an Embed Job
  version: endpoint_embedJobs.cancel
paths:
  /v1/embed-jobs/{id}/cancel:
    post:
      operationId: cancel
      summary: Cancel an Embed Job
      description: >-
        This API allows users to cancel an active embed job. Once invoked, the
        embedding process will be terminated, and users will be charged for the
        embeddings processed up to the cancellation point. It's important to
        note that partial results will not be available to users after
        cancellation.
      tags:
        - - subpackage_embedJobs
      parameters:
        - name: id
          in: path
          description: The ID of the embed job to cancel.
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
                $ref: '#/components/schemas/embed-jobs_cancel_Response_200'
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
    embed-jobs_cancel_Response_200:
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

	err := co.EmbedJobs.Cancel(context.TODO(), "embed_job_id")

	if err != nil {
		log.Fatal(err)
	}

}

```

```python Sync
import cohere

co = cohere.Client()

# cancel an embed job
co.embed_jobs.cancel("job_id")

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    await co.embed_jobs.cancel("job_id")

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;

public class EmbedJobsCancel {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    cohere.embedJobs().cancel("job_id");
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const embedJob = await cohere.embedJobs.cancel('job_id');

  console.log(embedJob);
})();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/embed-jobs/id/cancel")

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

$response = $client->request('POST', 'https://api.cohere.com/v1/embed-jobs/id/cancel', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/embed-jobs/id/cancel");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/embed-jobs/id/cancel")! as URL,
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

# Create a Dataset

POST https://api.cohere.com/v1/datasets
Content-Type: multipart/form-data

Create a dataset by uploading a file. See ['Dataset Creation'](https://docs.cohere.com/docs/datasets#dataset-creation) for more information.

Reference: https://docs.cohere.com/reference/create-dataset

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create a Dataset
  version: endpoint_datasets.create
paths:
  /v1/datasets:
    post:
      operationId: create
      summary: Create a Dataset
      description: >-
        Create a dataset by uploading a file. See ['Dataset
        Creation'](https://docs.cohere.com/docs/datasets#dataset-creation) for
        more information.
      tags:
        - - subpackage_datasets
      parameters:
        - name: name
          in: query
          description: The name of the uploaded dataset.
          required: true
          schema:
            type: string
        - name: type
          in: query
          description: >-
            The dataset type, which is used to validate the data. The only valid
            type is `embed-input` used in conjunction with the Embed Jobs API.
          required: true
          schema:
            $ref: '#/components/schemas/DatasetType'
        - name: keep_original_file
          in: query
          description: Indicates if the original file should be stored.
          required: false
          schema:
            type: boolean
        - name: skip_malformed_input
          in: query
          description: >-
            Indicates whether rows with malformed input should be dropped
            (instead of failing the validation check). Dropped rows will be
            returned in the warnings field.
          required: false
          schema:
            type: boolean
        - name: keep_fields
          in: query
          description: >-
            List of names of fields that will be persisted in the Dataset. By
            default the Dataset will retain only the required fields indicated
            in the [schema for the corresponding Dataset
            type](https://docs.cohere.com/docs/datasets#dataset-types). For
            example, datasets of type `embed-input` will drop all fields other
            than the required `text` field. If any of the fields in
            `keep_fields` are missing from the uploaded file, Dataset validation
            will fail.
          required: false
          schema:
            type: array
            items:
              type: string
        - name: optional_fields
          in: query
          description: >-
            List of names of fields that will be persisted in the Dataset. By
            default the Dataset will retain only the required fields indicated
            in the [schema for the corresponding Dataset
            type](https://docs.cohere.com/docs/datasets#dataset-types). For
            example, Datasets of type `embed-input` will drop all fields other
            than the required `text` field. If any of the fields in
            `optional_fields` are missing from the uploaded file, Dataset
            validation will pass.
          required: false
          schema:
            type: array
            items:
              type: string
        - name: text_separator
          in: query
          description: >-
            Raw .txt uploads will be split into entries using the text_separator
            value.
          required: false
          schema:
            type: string
        - name: csv_delimiter
          in: query
          description: The delimiter used for .csv uploads.
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
                $ref: '#/components/schemas/datasets_create_Response_200'
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
          multipart/form-data:
            schema:
              type: object
              properties: {}
components:
  schemas:
    DatasetType:
      type: string
      enum:
        - value: embed-input
        - value: embed-result
        - value: cluster-result
        - value: cluster-outliers
        - value: reranker-finetune-input
        - value: single-label-classification-finetune-input
        - value: chat-finetune-input
        - value: multi-label-classification-finetune-input
        - value: batch-chat-input
        - value: batch-openai-chat-input
        - value: batch-embed-v2-input
        - value: batch-chat-v2-input
    datasets_create_Response_200:
      type: object
      properties:
        id:
          type: string

```

## SDK Code Examples

```go Cohere Go SDK
package main

import (
	"context"
	"io"
	"log"
	"os"
	"strings"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

type MyReader struct {
	io.Reader
	name string
}

func (m *MyReader) Name() string {
	return m.name
}

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Datasets.Create(
		context.TODO(),
		&cohere.DatasetsCreateRequest{
			Name:     "embed-dataset",
			Type:     cohere.DatasetTypeEmbedInput,
			Data:     &MyReader{Reader: strings.NewReader(`{"text": "The quick brown fox jumps over the lazy dog"}`), name: "test.jsonl"},
			EvalData: &MyReader{Reader: strings.NewReader(""), name: "a.jsonl"},
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

# upload a dataset
my_dataset = co.datasets.create(
    name="embed-dataset",
    data=open("./embed.jsonl", "rb"),
    type="embed-input",
)

# wait for validation to complete
response = co.wait(my_dataset)

print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    # upload a dataset
    response = await co.datasets.create(
        name="embed-dataset",
        data=open("./embed.jsonl", "rb"),
        type="embed-input",
    )

    # wait for validation to complete
    response = await co.wait(response)

    print(response)


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.datasets.requests.DatasetsCreateRequest;
import com.cohere.api.resources.datasets.types.DatasetsCreateResponse;
import com.cohere.api.types.DatasetType;
import java.util.Optional;

public class DatasetPost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    DatasetsCreateResponse response =
        cohere
            .datasets()
            .create(
                null,
                Optional.empty(),
                DatasetsCreateRequest.builder()
                    .name("embed-dataset")
                    .type(DatasetType.EMBED_INPUT)
                    .build());

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const fs = require('fs');

const cohere = new CohereClient({});

(async () => {
  const file = fs.createReadStream('embed_jobs_sample_data.jsonl'); // {"text": "The quick brown fox jumps over the lazy dog"}

  const dataset = await cohere.datasets.create({ name: 'my-dataset', type: 'embed-input' }, file);

  console.log(dataset);
})();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/datasets?name=name&type=embed-input")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"data\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"eval_data\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/datasets?name=name&type=embed-input', [
  'multipart' => [
    [
        'name' => 'data',
        'filename' => 'string',
        'contents' => null
    ],
    [
        'name' => 'eval_data',
        'filename' => '<file1>',
        'contents' => null
    ]
  ]
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/datasets?name=name&type=embed-input");
var request = new RestRequest(Method.POST);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"data\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"eval_data\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>",
  "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
]
let parameters = [
  [
    "name": "data",
    "fileName": "string"
  ],
  [
    "name": "eval_data",
    "fileName": "<file1>"
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/datasets?name=name&type=embed-input")! as URL,
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

# List Datasets

GET https://api.cohere.com/v1/datasets

List datasets that have been created.

Reference: https://docs.cohere.com/reference/list-datasets

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List Datasets
  version: endpoint_datasets.list
paths:
  /v1/datasets:
    get:
      operationId: list
      summary: List Datasets
      description: List datasets that have been created.
      tags:
        - - subpackage_datasets
      parameters:
        - name: datasetType
          in: query
          description: optional filter by dataset type
          required: false
          schema:
            type: string
        - name: before
          in: query
          description: optional filter before a date
          required: false
          schema:
            type: string
            format: date-time
        - name: after
          in: query
          description: optional filter after a date
          required: false
          schema:
            type: string
            format: date-time
        - name: limit
          in: query
          description: optional limit to number of results
          required: false
          schema:
            type: number
            format: double
        - name: offset
          in: query
          description: optional offset to start of results
          required: false
          schema:
            type: number
            format: double
        - name: validationStatus
          in: query
          description: optional filter by validation status
          required: false
          schema:
            $ref: '#/components/schemas/DatasetValidationStatus'
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
                $ref: '#/components/schemas/datasets_list_Response_200'
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
    DatasetValidationStatus:
      type: string
      enum:
        - value: unknown
        - value: queued
        - value: processing
        - value: failed
        - value: validated
        - value: skipped
    DatasetType:
      type: string
      enum:
        - value: embed-input
        - value: embed-result
        - value: cluster-result
        - value: cluster-outliers
        - value: reranker-finetune-input
        - value: single-label-classification-finetune-input
        - value: chat-finetune-input
        - value: multi-label-classification-finetune-input
        - value: batch-chat-input
        - value: batch-openai-chat-input
        - value: batch-embed-v2-input
        - value: batch-chat-v2-input
    DatasetPart:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        url:
          type: string
        index:
          type: integer
        size_bytes:
          type: integer
        num_rows:
          type: integer
        original_url:
          type: string
        samples:
          type: array
          items:
            type: string
      required:
        - id
        - name
    ParseInfo:
      type: object
      properties:
        separator:
          type: string
        delimiter:
          type: string
    RerankerDataMetrics:
      type: object
      properties:
        num_train_queries:
          type: integer
          format: int64
        num_train_relevant_passages:
          type: integer
          format: int64
        num_train_hard_negatives:
          type: integer
          format: int64
        num_eval_queries:
          type: integer
          format: int64
        num_eval_relevant_passages:
          type: integer
          format: int64
        num_eval_hard_negatives:
          type: integer
          format: int64
    ChatDataMetrics:
      type: object
      properties:
        num_train_turns:
          type: integer
          format: int64
        num_eval_turns:
          type: integer
          format: int64
        preamble:
          type: string
    LabelMetric:
      type: object
      properties:
        total_examples:
          type: integer
          format: int64
        label:
          type: string
        samples:
          type: array
          items:
            type: string
    ClassifyDataMetrics:
      type: object
      properties:
        label_metrics:
          type: array
          items:
            $ref: '#/components/schemas/LabelMetric'
    FinetuneDatasetMetrics:
      type: object
      properties:
        trainable_token_count:
          type: integer
          format: int64
        total_examples:
          type: integer
          format: int64
        train_examples:
          type: integer
          format: int64
        train_size_bytes:
          type: integer
          format: int64
        eval_examples:
          type: integer
          format: int64
        eval_size_bytes:
          type: integer
          format: int64
        reranker_data_metrics:
          $ref: '#/components/schemas/RerankerDataMetrics'
        chat_data_metrics:
          $ref: '#/components/schemas/ChatDataMetrics'
        classify_data_metrics:
          $ref: '#/components/schemas/ClassifyDataMetrics'
    Metrics:
      type: object
      properties:
        finetune_dataset_metrics:
          $ref: '#/components/schemas/FinetuneDatasetMetrics'
    Dataset:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        dataset_type:
          $ref: '#/components/schemas/DatasetType'
        validation_status:
          $ref: '#/components/schemas/DatasetValidationStatus'
        validation_error:
          type: string
        schema:
          type: string
        required_fields:
          type: array
          items:
            type: string
        preserve_fields:
          type: array
          items:
            type: string
        dataset_parts:
          type: array
          items:
            $ref: '#/components/schemas/DatasetPart'
        validation_warnings:
          type: array
          items:
            type: string
        parse_info:
          $ref: '#/components/schemas/ParseInfo'
        metrics:
          $ref: '#/components/schemas/Metrics'
      required:
        - id
        - name
        - created_at
        - updated_at
        - dataset_type
        - validation_status
    datasets_list_Response_200:
      type: object
      properties:
        datasets:
          type: array
          items:
            $ref: '#/components/schemas/Dataset'

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

	resp, err := co.Datasets.List(
		context.TODO(),
		&cohere.DatasetsListRequest{})

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```python Sync
import cohere

co = cohere.Client()

# get list of datasets
response = co.datasets.list()

print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.datasets.list()

    print(response)


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.datasets.types.DatasetsListResponse;

public class DatasetList {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    DatasetsListResponse response = cohere.datasets().list();

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const datasets = await cohere.datasets.list();

  console.log(datasets);
})();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/datasets")

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

$response = $client->request('GET', 'https://api.cohere.com/v1/datasets', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/datasets");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/datasets")! as URL,
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

# Get Dataset Usage

GET https://api.cohere.com/v1/datasets/usage

View the dataset storage usage for your Organization. Each Organization can have up to 10GB of storage across all their users.

Reference: https://docs.cohere.com/reference/get-dataset-usage

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get Dataset Usage
  version: endpoint_datasets.getUsage
paths:
  /v1/datasets/usage:
    get:
      operationId: get-usage
      summary: Get Dataset Usage
      description: >-
        View the dataset storage usage for your Organization. Each Organization
        can have up to 10GB of storage across all their users.
      tags:
        - - subpackage_datasets
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
                $ref: '#/components/schemas/datasets_getUsage_Response_200'
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
    datasets_getUsage_Response_200:
      type: object
      properties:
        organization_usage:
          type: integer
          format: int64

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

	resp, err := co.Datasets.GetUsage(context.TODO())

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```python Sync
import cohere

co = cohere.Client()

# get usage
response = co.datasets.get_usage()

print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.datasets.get_usage()

    print(response)


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.datasets.types.DatasetsGetUsageResponse;

public class DatasetUsageGet {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    DatasetsGetUsageResponse response = cohere.datasets().getUsage();

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const usage = await cohere.datasets.getUsage('id');

  console.log(usage);
})();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/datasets/usage")

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

$response = $client->request('GET', 'https://api.cohere.com/v1/datasets/usage', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/datasets/usage");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/datasets/usage")! as URL,
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

# Get a Dataset

GET https://api.cohere.com/v1/datasets/{id}

Retrieve a dataset by ID. See ['Datasets'](https://docs.cohere.com/docs/datasets) for more information.

Reference: https://docs.cohere.com/reference/get-dataset

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get a Dataset
  version: endpoint_datasets.get
paths:
  /v1/datasets/{id}:
    get:
      operationId: get
      summary: Get a Dataset
      description: >-
        Retrieve a dataset by ID. See
        ['Datasets'](https://docs.cohere.com/docs/datasets) for more
        information.
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
                $ref: '#/components/schemas/datasets_get_Response_200'
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
    DatasetType:
      type: string
      enum:
        - value: embed-input
        - value: embed-result
        - value: cluster-result
        - value: cluster-outliers
        - value: reranker-finetune-input
        - value: single-label-classification-finetune-input
        - value: chat-finetune-input
        - value: multi-label-classification-finetune-input
        - value: batch-chat-input
        - value: batch-openai-chat-input
        - value: batch-embed-v2-input
        - value: batch-chat-v2-input
    DatasetValidationStatus:
      type: string
      enum:
        - value: unknown
        - value: queued
        - value: processing
        - value: failed
        - value: validated
        - value: skipped
    DatasetPart:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        url:
          type: string
        index:
          type: integer
        size_bytes:
          type: integer
        num_rows:
          type: integer
        original_url:
          type: string
        samples:
          type: array
          items:
            type: string
      required:
        - id
        - name
    ParseInfo:
      type: object
      properties:
        separator:
          type: string
        delimiter:
          type: string
    RerankerDataMetrics:
      type: object
      properties:
        num_train_queries:
          type: integer
          format: int64
        num_train_relevant_passages:
          type: integer
          format: int64
        num_train_hard_negatives:
          type: integer
          format: int64
        num_eval_queries:
          type: integer
          format: int64
        num_eval_relevant_passages:
          type: integer
          format: int64
        num_eval_hard_negatives:
          type: integer
          format: int64
    ChatDataMetrics:
      type: object
      properties:
        num_train_turns:
          type: integer
          format: int64
        num_eval_turns:
          type: integer
          format: int64
        preamble:
          type: string
    LabelMetric:
      type: object
      properties:
        total_examples:
          type: integer
          format: int64
        label:
          type: string
        samples:
          type: array
          items:
            type: string
    ClassifyDataMetrics:
      type: object
      properties:
        label_metrics:
          type: array
          items:
            $ref: '#/components/schemas/LabelMetric'
    FinetuneDatasetMetrics:
      type: object
      properties:
        trainable_token_count:
          type: integer
          format: int64
        total_examples:
          type: integer
          format: int64
        train_examples:
          type: integer
          format: int64
        train_size_bytes:
          type: integer
          format: int64
        eval_examples:
          type: integer
          format: int64
        eval_size_bytes:
          type: integer
          format: int64
        reranker_data_metrics:
          $ref: '#/components/schemas/RerankerDataMetrics'
        chat_data_metrics:
          $ref: '#/components/schemas/ChatDataMetrics'
        classify_data_metrics:
          $ref: '#/components/schemas/ClassifyDataMetrics'
    Metrics:
      type: object
      properties:
        finetune_dataset_metrics:
          $ref: '#/components/schemas/FinetuneDatasetMetrics'
    Dataset:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        dataset_type:
          $ref: '#/components/schemas/DatasetType'
        validation_status:
          $ref: '#/components/schemas/DatasetValidationStatus'
        validation_error:
          type: string
        schema:
          type: string
        required_fields:
          type: array
          items:
            type: string
        preserve_fields:
          type: array
          items:
            type: string
        dataset_parts:
          type: array
          items:
            $ref: '#/components/schemas/DatasetPart'
        validation_warnings:
          type: array
          items:
            type: string
        parse_info:
          $ref: '#/components/schemas/ParseInfo'
        metrics:
          $ref: '#/components/schemas/Metrics'
      required:
        - id
        - name
        - created_at
        - updated_at
        - dataset_type
        - validation_status
    datasets_get_Response_200:
      type: object
      properties:
        dataset:
          $ref: '#/components/schemas/Dataset'
      required:
        - dataset

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

	resp, err := co.Datasets.Get(context.TODO(), "dataset_id")

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```python Sync
import cohere

co = cohere.Client()

# get dataset
response = co.datasets.get(id="<<datasetId>>")

print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.datasets.get(id="<<datasetId>>")

    print(response)


asyncio.run(main())

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.datasets.types.DatasetsGetResponse;

public class DatasetGet {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    DatasetsGetResponse response = cohere.datasets().get("dataset_id");

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const datasets = await cohere.datasets.get('<<datasetId>>');

  console.log(datasets);
})();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/datasets/id")

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

$response = $client->request('GET', 'https://api.cohere.com/v1/datasets/id', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://api.cohere.com/v1/datasets/id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/datasets/id")! as URL,
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

**Navigation:** [← Previous](./10-chat-with-streaming.md) | [Index](./index.md) | [Next →](./12-delete-a-dataset.md)
