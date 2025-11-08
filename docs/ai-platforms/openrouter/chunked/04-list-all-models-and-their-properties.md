**Navigation:** [← Previous](./03-tool-calling.md) | [Index](./index.md) | [Next →](./05-create-a-completion.md)

---

# List all models and their properties

GET https://openrouter.ai/api/v1/models

Reference: https://openrouter.ai/docs/api-reference/models/get-models

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List all models and their properties
  version: endpoint_models.getModels
paths:
  /models:
    get:
      operationId: get-models
      summary: List all models and their properties
      tags:
        - - subpackage_models
      parameters:
        - name: category
          in: query
          required: false
          schema:
            type: string
        - name: supported_parameters
          in: query
          required: false
          schema:
            type: string
        - name: use_rss
          in: query
          required: false
          schema:
            type: string
        - name: use_rss_chat_links
          in: query
          required: false
          schema:
            type: string
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns a list of models or RSS feed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelsListResponse'
        '400':
          description: Bad Request - Invalid request parameters
          content: {}
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    BigNumberUnion:
      oneOf:
        - type: number
          format: double
        - type: string
        - type: number
          format: double
    PublicPricing:
      type: object
      properties:
        prompt:
          $ref: '#/components/schemas/BigNumberUnion'
        completion:
          $ref: '#/components/schemas/BigNumberUnion'
        request:
          $ref: '#/components/schemas/BigNumberUnion'
        image:
          $ref: '#/components/schemas/BigNumberUnion'
        image_output:
          $ref: '#/components/schemas/BigNumberUnion'
        audio:
          $ref: '#/components/schemas/BigNumberUnion'
        input_audio_cache:
          $ref: '#/components/schemas/BigNumberUnion'
        web_search:
          $ref: '#/components/schemas/BigNumberUnion'
        internal_reasoning:
          $ref: '#/components/schemas/BigNumberUnion'
        input_cache_read:
          $ref: '#/components/schemas/BigNumberUnion'
        input_cache_write:
          $ref: '#/components/schemas/BigNumberUnion'
        discount:
          type: number
          format: double
      required:
        - prompt
        - completion
    ModelGroup:
      type: string
      enum:
        - value: Router
        - value: Media
        - value: Other
        - value: GPT
        - value: Claude
        - value: Gemini
        - value: Grok
        - value: Cohere
        - value: Nova
        - value: Qwen
        - value: Yi
        - value: DeepSeek
        - value: Mistral
        - value: Llama2
        - value: Llama3
        - value: Llama4
        - value: PaLM
        - value: RWKV
        - value: Qwen3
    ModelArchitectureInstructType:
      type: string
      enum:
        - value: none
        - value: airoboros
        - value: alpaca
        - value: alpaca-modif
        - value: chatml
        - value: claude
        - value: code-llama
        - value: gemma
        - value: llama2
        - value: llama3
        - value: mistral
        - value: nemotron
        - value: neural
        - value: openchat
        - value: phi3
        - value: rwkv
        - value: vicuna
        - value: zephyr
        - value: deepseek-r1
        - value: deepseek-v3.1
        - value: qwq
        - value: qwen3
    InputModality:
      type: string
      enum:
        - value: text
        - value: image
        - value: file
        - value: audio
        - value: video
    OutputModality:
      type: string
      enum:
        - value: text
        - value: image
        - value: embeddings
    ModelArchitecture:
      type: object
      properties:
        tokenizer:
          $ref: '#/components/schemas/ModelGroup'
        instruct_type:
          oneOf:
            - $ref: '#/components/schemas/ModelArchitectureInstructType'
            - type: 'null'
        modality:
          type:
            - string
            - 'null'
        input_modalities:
          type: array
          items:
            $ref: '#/components/schemas/InputModality'
        output_modalities:
          type: array
          items:
            $ref: '#/components/schemas/OutputModality'
      required:
        - modality
        - input_modalities
        - output_modalities
    TopProviderInfo:
      type: object
      properties:
        context_length:
          type:
            - number
            - 'null'
          format: double
        max_completion_tokens:
          type:
            - number
            - 'null'
          format: double
        is_moderated:
          type: boolean
      required:
        - is_moderated
    PerRequestLimits:
      type: object
      properties:
        prompt_tokens:
          type: number
          format: double
        completion_tokens:
          type: number
          format: double
      required:
        - prompt_tokens
        - completion_tokens
    Parameter:
      type: string
      enum:
        - value: temperature
        - value: top_p
        - value: top_k
        - value: min_p
        - value: top_a
        - value: frequency_penalty
        - value: presence_penalty
        - value: repetition_penalty
        - value: max_tokens
        - value: logit_bias
        - value: logprobs
        - value: top_logprobs
        - value: seed
        - value: response_format
        - value: structured_outputs
        - value: stop
        - value: tools
        - value: tool_choice
        - value: parallel_tool_calls
        - value: include_reasoning
        - value: reasoning
        - value: web_search_options
        - value: verbosity
    DefaultParameters:
      type: object
      properties:
        temperature:
          type:
            - number
            - 'null'
          format: double
        top_p:
          type:
            - number
            - 'null'
          format: double
        frequency_penalty:
          type:
            - number
            - 'null'
          format: double
    Model:
      type: object
      properties:
        id:
          type: string
        canonical_slug:
          type: string
        hugging_face_id:
          type:
            - string
            - 'null'
        name:
          type: string
        created:
          type: number
          format: double
        description:
          type: string
        pricing:
          $ref: '#/components/schemas/PublicPricing'
        context_length:
          type:
            - number
            - 'null'
          format: double
        architecture:
          $ref: '#/components/schemas/ModelArchitecture'
        top_provider:
          $ref: '#/components/schemas/TopProviderInfo'
        per_request_limits:
          $ref: '#/components/schemas/PerRequestLimits'
        supported_parameters:
          type: array
          items:
            $ref: '#/components/schemas/Parameter'
        default_parameters:
          $ref: '#/components/schemas/DefaultParameters'
      required:
        - id
        - canonical_slug
        - name
        - created
        - pricing
        - context_length
        - architecture
        - top_provider
        - per_request_limits
        - supported_parameters
        - default_parameters
    ModelsListResponseData:
      type: array
      items:
        $ref: '#/components/schemas/Model'
    ModelsListResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/ModelsListResponseData'
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/models"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/models';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

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
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/models"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://openrouter.ai/api/v1/models")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/models")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/models', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/models");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/models")! as URL,
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

# List all embeddings models

GET https://openrouter.ai/api/v1/models/embeddings

Returns a list of all available embeddings models and their properties

Reference: https://openrouter.ai/docs/api-reference/models/list-models-embeddings

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List all embeddings models
  version: endpoint_models.listModelsEmbeddings
paths:
  /models/embeddings:
    get:
      operationId: list-models-embeddings
      summary: List all embeddings models
      description: Returns a list of all available embeddings models and their properties
      tags:
        - - subpackage_models
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns a list of embeddings models
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelsListResponse'
        '400':
          description: Bad Request - Invalid request parameters
          content: {}
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    BigNumberUnion:
      oneOf:
        - type: number
          format: double
        - type: string
        - type: number
          format: double
    PublicPricing:
      type: object
      properties:
        prompt:
          $ref: '#/components/schemas/BigNumberUnion'
        completion:
          $ref: '#/components/schemas/BigNumberUnion'
        request:
          $ref: '#/components/schemas/BigNumberUnion'
        image:
          $ref: '#/components/schemas/BigNumberUnion'
        image_output:
          $ref: '#/components/schemas/BigNumberUnion'
        audio:
          $ref: '#/components/schemas/BigNumberUnion'
        input_audio_cache:
          $ref: '#/components/schemas/BigNumberUnion'
        web_search:
          $ref: '#/components/schemas/BigNumberUnion'
        internal_reasoning:
          $ref: '#/components/schemas/BigNumberUnion'
        input_cache_read:
          $ref: '#/components/schemas/BigNumberUnion'
        input_cache_write:
          $ref: '#/components/schemas/BigNumberUnion'
        discount:
          type: number
          format: double
      required:
        - prompt
        - completion
    ModelGroup:
      type: string
      enum:
        - value: Router
        - value: Media
        - value: Other
        - value: GPT
        - value: Claude
        - value: Gemini
        - value: Grok
        - value: Cohere
        - value: Nova
        - value: Qwen
        - value: Yi
        - value: DeepSeek
        - value: Mistral
        - value: Llama2
        - value: Llama3
        - value: Llama4
        - value: PaLM
        - value: RWKV
        - value: Qwen3
    ModelArchitectureInstructType:
      type: string
      enum:
        - value: none
        - value: airoboros
        - value: alpaca
        - value: alpaca-modif
        - value: chatml
        - value: claude
        - value: code-llama
        - value: gemma
        - value: llama2
        - value: llama3
        - value: mistral
        - value: nemotron
        - value: neural
        - value: openchat
        - value: phi3
        - value: rwkv
        - value: vicuna
        - value: zephyr
        - value: deepseek-r1
        - value: deepseek-v3.1
        - value: qwq
        - value: qwen3
    InputModality:
      type: string
      enum:
        - value: text
        - value: image
        - value: file
        - value: audio
        - value: video
    OutputModality:
      type: string
      enum:
        - value: text
        - value: image
        - value: embeddings
    ModelArchitecture:
      type: object
      properties:
        tokenizer:
          $ref: '#/components/schemas/ModelGroup'
        instruct_type:
          oneOf:
            - $ref: '#/components/schemas/ModelArchitectureInstructType'
            - type: 'null'
        modality:
          type:
            - string
            - 'null'
        input_modalities:
          type: array
          items:
            $ref: '#/components/schemas/InputModality'
        output_modalities:
          type: array
          items:
            $ref: '#/components/schemas/OutputModality'
      required:
        - modality
        - input_modalities
        - output_modalities
    TopProviderInfo:
      type: object
      properties:
        context_length:
          type:
            - number
            - 'null'
          format: double
        max_completion_tokens:
          type:
            - number
            - 'null'
          format: double
        is_moderated:
          type: boolean
      required:
        - is_moderated
    PerRequestLimits:
      type: object
      properties:
        prompt_tokens:
          type: number
          format: double
        completion_tokens:
          type: number
          format: double
      required:
        - prompt_tokens
        - completion_tokens
    Parameter:
      type: string
      enum:
        - value: temperature
        - value: top_p
        - value: top_k
        - value: min_p
        - value: top_a
        - value: frequency_penalty
        - value: presence_penalty
        - value: repetition_penalty
        - value: max_tokens
        - value: logit_bias
        - value: logprobs
        - value: top_logprobs
        - value: seed
        - value: response_format
        - value: structured_outputs
        - value: stop
        - value: tools
        - value: tool_choice
        - value: parallel_tool_calls
        - value: include_reasoning
        - value: reasoning
        - value: web_search_options
        - value: verbosity
    DefaultParameters:
      type: object
      properties:
        temperature:
          type:
            - number
            - 'null'
          format: double
        top_p:
          type:
            - number
            - 'null'
          format: double
        frequency_penalty:
          type:
            - number
            - 'null'
          format: double
    Model:
      type: object
      properties:
        id:
          type: string
        canonical_slug:
          type: string
        hugging_face_id:
          type:
            - string
            - 'null'
        name:
          type: string
        created:
          type: number
          format: double
        description:
          type: string
        pricing:
          $ref: '#/components/schemas/PublicPricing'
        context_length:
          type:
            - number
            - 'null'
          format: double
        architecture:
          $ref: '#/components/schemas/ModelArchitecture'
        top_provider:
          $ref: '#/components/schemas/TopProviderInfo'
        per_request_limits:
          $ref: '#/components/schemas/PerRequestLimits'
        supported_parameters:
          type: array
          items:
            $ref: '#/components/schemas/Parameter'
        default_parameters:
          $ref: '#/components/schemas/DefaultParameters'
      required:
        - id
        - canonical_slug
        - name
        - created
        - pricing
        - context_length
        - architecture
        - top_provider
        - per_request_limits
        - supported_parameters
        - default_parameters
    ModelsListResponseData:
      type: array
      items:
        $ref: '#/components/schemas/Model'
    ModelsListResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/ModelsListResponseData'
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/models/embeddings"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/models/embeddings';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

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
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/models/embeddings"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://openrouter.ai/api/v1/models/embeddings")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/models/embeddings")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/models/embeddings', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/models/embeddings");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/models/embeddings")! as URL,
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

# List models filtered by user provider preferences

GET https://openrouter.ai/api/v1/models/user

Reference: https://openrouter.ai/docs/api-reference/models/list-models-user

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List models filtered by user provider preferences
  version: endpoint_models.listModelsUser
paths:
  /models/user:
    get:
      operationId: list-models-user
      summary: List models filtered by user provider preferences
      tags:
        - - subpackage_models
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns a list of models filtered by user provider preferences
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelsListResponse'
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    BigNumberUnion:
      oneOf:
        - type: number
          format: double
        - type: string
        - type: number
          format: double
    PublicPricing:
      type: object
      properties:
        prompt:
          $ref: '#/components/schemas/BigNumberUnion'
        completion:
          $ref: '#/components/schemas/BigNumberUnion'
        request:
          $ref: '#/components/schemas/BigNumberUnion'
        image:
          $ref: '#/components/schemas/BigNumberUnion'
        image_output:
          $ref: '#/components/schemas/BigNumberUnion'
        audio:
          $ref: '#/components/schemas/BigNumberUnion'
        input_audio_cache:
          $ref: '#/components/schemas/BigNumberUnion'
        web_search:
          $ref: '#/components/schemas/BigNumberUnion'
        internal_reasoning:
          $ref: '#/components/schemas/BigNumberUnion'
        input_cache_read:
          $ref: '#/components/schemas/BigNumberUnion'
        input_cache_write:
          $ref: '#/components/schemas/BigNumberUnion'
        discount:
          type: number
          format: double
      required:
        - prompt
        - completion
    ModelGroup:
      type: string
      enum:
        - value: Router
        - value: Media
        - value: Other
        - value: GPT
        - value: Claude
        - value: Gemini
        - value: Grok
        - value: Cohere
        - value: Nova
        - value: Qwen
        - value: Yi
        - value: DeepSeek
        - value: Mistral
        - value: Llama2
        - value: Llama3
        - value: Llama4
        - value: PaLM
        - value: RWKV
        - value: Qwen3
    ModelArchitectureInstructType:
      type: string
      enum:
        - value: none
        - value: airoboros
        - value: alpaca
        - value: alpaca-modif
        - value: chatml
        - value: claude
        - value: code-llama
        - value: gemma
        - value: llama2
        - value: llama3
        - value: mistral
        - value: nemotron
        - value: neural
        - value: openchat
        - value: phi3
        - value: rwkv
        - value: vicuna
        - value: zephyr
        - value: deepseek-r1
        - value: deepseek-v3.1
        - value: qwq
        - value: qwen3
    InputModality:
      type: string
      enum:
        - value: text
        - value: image
        - value: file
        - value: audio
        - value: video
    OutputModality:
      type: string
      enum:
        - value: text
        - value: image
        - value: embeddings
    ModelArchitecture:
      type: object
      properties:
        tokenizer:
          $ref: '#/components/schemas/ModelGroup'
        instruct_type:
          oneOf:
            - $ref: '#/components/schemas/ModelArchitectureInstructType'
            - type: 'null'
        modality:
          type:
            - string
            - 'null'
        input_modalities:
          type: array
          items:
            $ref: '#/components/schemas/InputModality'
        output_modalities:
          type: array
          items:
            $ref: '#/components/schemas/OutputModality'
      required:
        - modality
        - input_modalities
        - output_modalities
    TopProviderInfo:
      type: object
      properties:
        context_length:
          type:
            - number
            - 'null'
          format: double
        max_completion_tokens:
          type:
            - number
            - 'null'
          format: double
        is_moderated:
          type: boolean
      required:
        - is_moderated
    PerRequestLimits:
      type: object
      properties:
        prompt_tokens:
          type: number
          format: double
        completion_tokens:
          type: number
          format: double
      required:
        - prompt_tokens
        - completion_tokens
    Parameter:
      type: string
      enum:
        - value: temperature
        - value: top_p
        - value: top_k
        - value: min_p
        - value: top_a
        - value: frequency_penalty
        - value: presence_penalty
        - value: repetition_penalty
        - value: max_tokens
        - value: logit_bias
        - value: logprobs
        - value: top_logprobs
        - value: seed
        - value: response_format
        - value: structured_outputs
        - value: stop
        - value: tools
        - value: tool_choice
        - value: parallel_tool_calls
        - value: include_reasoning
        - value: reasoning
        - value: web_search_options
        - value: verbosity
    DefaultParameters:
      type: object
      properties:
        temperature:
          type:
            - number
            - 'null'
          format: double
        top_p:
          type:
            - number
            - 'null'
          format: double
        frequency_penalty:
          type:
            - number
            - 'null'
          format: double
    Model:
      type: object
      properties:
        id:
          type: string
        canonical_slug:
          type: string
        hugging_face_id:
          type:
            - string
            - 'null'
        name:
          type: string
        created:
          type: number
          format: double
        description:
          type: string
        pricing:
          $ref: '#/components/schemas/PublicPricing'
        context_length:
          type:
            - number
            - 'null'
          format: double
        architecture:
          $ref: '#/components/schemas/ModelArchitecture'
        top_provider:
          $ref: '#/components/schemas/TopProviderInfo'
        per_request_limits:
          $ref: '#/components/schemas/PerRequestLimits'
        supported_parameters:
          type: array
          items:
            $ref: '#/components/schemas/Parameter'
        default_parameters:
          $ref: '#/components/schemas/DefaultParameters'
      required:
        - id
        - canonical_slug
        - name
        - created
        - pricing
        - context_length
        - architecture
        - top_provider
        - per_request_limits
        - supported_parameters
        - default_parameters
    ModelsListResponseData:
      type: array
      items:
        $ref: '#/components/schemas/Model'
    ModelsListResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/ModelsListResponseData'
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/models/user"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/models/user';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

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
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/models/user"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://openrouter.ai/api/v1/models/user")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/models/user")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/models/user', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/models/user");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/models/user")! as URL,
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

# List all endpoints for a model

GET https://openrouter.ai/api/v1/models/{author}/{slug}/endpoints

Reference: https://openrouter.ai/docs/api-reference/endpoints/list-endpoints

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List all endpoints for a model
  version: endpoint_endpoints.listEndpoints
paths:
  /models/{author}/{slug}/endpoints:
    get:
      operationId: list-endpoints
      summary: List all endpoints for a model
      tags:
        - - subpackage_endpoints
      parameters:
        - name: author
          in: path
          required: true
          schema:
            type: string
        - name: slug
          in: path
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns a list of endpoints
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Endpoints_listEndpoints_Response_200'
        '404':
          description: Not Found - Model does not exist
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    ModelGroup:
      type: string
      enum:
        - value: Router
        - value: Media
        - value: Other
        - value: GPT
        - value: Claude
        - value: Gemini
        - value: Grok
        - value: Cohere
        - value: Nova
        - value: Qwen
        - value: Yi
        - value: DeepSeek
        - value: Mistral
        - value: Llama2
        - value: Llama3
        - value: Llama4
        - value: PaLM
        - value: RWKV
        - value: Qwen3
    ModelArchitectureInstructType:
      type: string
      enum:
        - value: none
        - value: airoboros
        - value: alpaca
        - value: alpaca-modif
        - value: chatml
        - value: claude
        - value: code-llama
        - value: gemma
        - value: llama2
        - value: llama3
        - value: mistral
        - value: nemotron
        - value: neural
        - value: openchat
        - value: phi3
        - value: rwkv
        - value: vicuna
        - value: zephyr
        - value: deepseek-r1
        - value: deepseek-v3.1
        - value: qwq
        - value: qwen3
    InputModality:
      type: string
      enum:
        - value: text
        - value: image
        - value: file
        - value: audio
        - value: video
    OutputModality:
      type: string
      enum:
        - value: text
        - value: image
        - value: embeddings
    ListEndpointsResponseArchitectureTokenizer:
      type: object
      properties: {}
    InstructType:
      type: string
      enum:
        - value: none
        - value: airoboros
        - value: alpaca
        - value: alpaca-modif
        - value: chatml
        - value: claude
        - value: code-llama
        - value: gemma
        - value: llama2
        - value: llama3
        - value: mistral
        - value: nemotron
        - value: neural
        - value: openchat
        - value: phi3
        - value: rwkv
        - value: vicuna
        - value: zephyr
        - value: deepseek-r1
        - value: deepseek-v3.1
        - value: qwq
        - value: qwen3
    ListEndpointsResponseArchitecture:
      type: object
      properties:
        tokenizer:
          $ref: '#/components/schemas/ListEndpointsResponseArchitectureTokenizer'
        instruct_type:
          $ref: '#/components/schemas/InstructType'
        modality:
          type:
            - string
            - 'null'
        input_modalities:
          type: array
          items:
            $ref: '#/components/schemas/InputModality'
        output_modalities:
          type: array
          items:
            $ref: '#/components/schemas/OutputModality'
      required:
        - modality
        - input_modalities
        - output_modalities
        - tokenizer
        - instruct_type
    BigNumberUnion:
      oneOf:
        - type: number
          format: double
        - type: string
        - type: number
          format: double
    PublicEndpointPricing:
      type: object
      properties:
        prompt:
          $ref: '#/components/schemas/BigNumberUnion'
        completion:
          $ref: '#/components/schemas/BigNumberUnion'
        request:
          $ref: '#/components/schemas/BigNumberUnion'
        image:
          $ref: '#/components/schemas/BigNumberUnion'
        image_output:
          $ref: '#/components/schemas/BigNumberUnion'
        audio:
          $ref: '#/components/schemas/BigNumberUnion'
        input_audio_cache:
          $ref: '#/components/schemas/BigNumberUnion'
        web_search:
          $ref: '#/components/schemas/BigNumberUnion'
        internal_reasoning:
          $ref: '#/components/schemas/BigNumberUnion'
        input_cache_read:
          $ref: '#/components/schemas/BigNumberUnion'
        input_cache_write:
          $ref: '#/components/schemas/BigNumberUnion'
        discount:
          type: number
          format: double
      required:
        - prompt
        - completion
    ProviderName:
      type: string
      enum:
        - value: AnyScale
        - value: Cent-ML
        - value: HuggingFace
        - value: Hyperbolic 2
        - value: Lepton
        - value: Lynn 2
        - value: Lynn
        - value: Mancer
        - value: Modal
        - value: OctoAI
        - value: Recursal
        - value: Reflection
        - value: Replicate
        - value: SambaNova 2
        - value: SF Compute
        - value: Together 2
        - value: 01.AI
        - value: AI21
        - value: AionLabs
        - value: Alibaba
        - value: Amazon Bedrock
        - value: Anthropic
        - value: AtlasCloud
        - value: Atoma
        - value: Avian
        - value: Azure
        - value: BaseTen
        - value: Cerebras
        - value: Chutes
        - value: Cirrascale
        - value: Clarifai
        - value: Cloudflare
        - value: Cohere
        - value: CrofAI
        - value: Crusoe
        - value: DeepInfra
        - value: DeepSeek
        - value: Enfer
        - value: Featherless
        - value: Fireworks
        - value: Friendli
        - value: GMICloud
        - value: Google
        - value: Google AI Studio
        - value: Groq
        - value: Hyperbolic
        - value: Inception
        - value: InferenceNet
        - value: Infermatic
        - value: Inflection
        - value: InoCloud
        - value: Kluster
        - value: Lambda
        - value: Liquid
        - value: Mancer 2
        - value: Meta
        - value: Minimax
        - value: ModelRun
        - value: Mistral
        - value: Modular
        - value: Moonshot AI
        - value: Morph
        - value: NCompass
        - value: Nebius
        - value: NextBit
        - value: Nineteen
        - value: Novita
        - value: Nvidia
        - value: OpenAI
        - value: OpenInference
        - value: Parasail
        - value: Perplexity
        - value: Phala
        - value: Relace
        - value: SambaNova
        - value: SiliconFlow
        - value: Stealth
        - value: Switchpoint
        - value: Targon
        - value: Together
        - value: Ubicloud
        - value: Venice
        - value: WandB
        - value: xAI
        - value: Z.AI
        - value: FakeProvider
    PublicEndpointQuantization:
      type: object
      properties: {}
    Parameter:
      type: string
      enum:
        - value: temperature
        - value: top_p
        - value: top_k
        - value: min_p
        - value: top_a
        - value: frequency_penalty
        - value: presence_penalty
        - value: repetition_penalty
        - value: max_tokens
        - value: logit_bias
        - value: logprobs
        - value: top_logprobs
        - value: seed
        - value: response_format
        - value: structured_outputs
        - value: stop
        - value: tools
        - value: tool_choice
        - value: parallel_tool_calls
        - value: include_reasoning
        - value: reasoning
        - value: web_search_options
        - value: verbosity
    EndpointStatus:
      type: string
      enum:
        - value: '0'
        - value: '-1'
        - value: '-2'
        - value: '-3'
        - value: '-5'
        - value: '-10'
    PublicEndpoint:
      type: object
      properties:
        name:
          type: string
        model_name:
          type: string
        context_length:
          type: number
          format: double
        pricing:
          $ref: '#/components/schemas/PublicEndpointPricing'
        provider_name:
          $ref: '#/components/schemas/ProviderName'
        tag:
          type: string
        quantization:
          $ref: '#/components/schemas/PublicEndpointQuantization'
        max_completion_tokens:
          type:
            - number
            - 'null'
          format: double
        max_prompt_tokens:
          type:
            - number
            - 'null'
          format: double
        supported_parameters:
          type: array
          items:
            $ref: '#/components/schemas/Parameter'
        status:
          $ref: '#/components/schemas/EndpointStatus'
        uptime_last_30m:
          type:
            - number
            - 'null'
          format: double
        supports_implicit_caching:
          type: boolean
      required:
        - name
        - model_name
        - context_length
        - pricing
        - provider_name
        - tag
        - quantization
        - max_completion_tokens
        - max_prompt_tokens
        - supported_parameters
        - uptime_last_30m
        - supports_implicit_caching
    ListEndpointsResponse:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        created:
          type: number
          format: double
        description:
          type: string
        architecture:
          $ref: '#/components/schemas/ListEndpointsResponseArchitecture'
        endpoints:
          type: array
          items:
            $ref: '#/components/schemas/PublicEndpoint'
      required:
        - id
        - name
        - created
        - description
        - architecture
        - endpoints
    Endpoints_listEndpoints_Response_200:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/ListEndpointsResponse'
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/models/author/slug/endpoints"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/models/author/slug/endpoints';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

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
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/models/author/slug/endpoints"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://openrouter.ai/api/v1/models/author/slug/endpoints")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/models/author/slug/endpoints")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/models/author/slug/endpoints', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/models/author/slug/endpoints");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/models/author/slug/endpoints")! as URL,
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

# Preview the impact of ZDR on the available endpoints

GET https://openrouter.ai/api/v1/endpoints/zdr

Reference: https://openrouter.ai/docs/api-reference/endpoints/list-endpoints-zdr

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Preview the impact of ZDR on the available endpoints
  version: endpoint_endpoints.listEndpointsZdr
paths:
  /endpoints/zdr:
    get:
      operationId: list-endpoints-zdr
      summary: Preview the impact of ZDR on the available endpoints
      tags:
        - - subpackage_endpoints
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns a list of endpoints
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Endpoints_listEndpointsZdr_Response_200'
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    BigNumberUnion:
      oneOf:
        - type: number
          format: double
        - type: string
        - type: number
          format: double
    PublicEndpointPricing:
      type: object
      properties:
        prompt:
          $ref: '#/components/schemas/BigNumberUnion'
        completion:
          $ref: '#/components/schemas/BigNumberUnion'
        request:
          $ref: '#/components/schemas/BigNumberUnion'
        image:
          $ref: '#/components/schemas/BigNumberUnion'
        image_output:
          $ref: '#/components/schemas/BigNumberUnion'
        audio:
          $ref: '#/components/schemas/BigNumberUnion'
        input_audio_cache:
          $ref: '#/components/schemas/BigNumberUnion'
        web_search:
          $ref: '#/components/schemas/BigNumberUnion'
        internal_reasoning:
          $ref: '#/components/schemas/BigNumberUnion'
        input_cache_read:
          $ref: '#/components/schemas/BigNumberUnion'
        input_cache_write:
          $ref: '#/components/schemas/BigNumberUnion'
        discount:
          type: number
          format: double
      required:
        - prompt
        - completion
    ProviderName:
      type: string
      enum:
        - value: AnyScale
        - value: Cent-ML
        - value: HuggingFace
        - value: Hyperbolic 2
        - value: Lepton
        - value: Lynn 2
        - value: Lynn
        - value: Mancer
        - value: Modal
        - value: OctoAI
        - value: Recursal
        - value: Reflection
        - value: Replicate
        - value: SambaNova 2
        - value: SF Compute
        - value: Together 2
        - value: 01.AI
        - value: AI21
        - value: AionLabs
        - value: Alibaba
        - value: Amazon Bedrock
        - value: Anthropic
        - value: AtlasCloud
        - value: Atoma
        - value: Avian
        - value: Azure
        - value: BaseTen
        - value: Cerebras
        - value: Chutes
        - value: Cirrascale
        - value: Clarifai
        - value: Cloudflare
        - value: Cohere
        - value: CrofAI
        - value: Crusoe
        - value: DeepInfra
        - value: DeepSeek
        - value: Enfer
        - value: Featherless
        - value: Fireworks
        - value: Friendli
        - value: GMICloud
        - value: Google
        - value: Google AI Studio
        - value: Groq
        - value: Hyperbolic
        - value: Inception
        - value: InferenceNet
        - value: Infermatic
        - value: Inflection
        - value: InoCloud
        - value: Kluster
        - value: Lambda
        - value: Liquid
        - value: Mancer 2
        - value: Meta
        - value: Minimax
        - value: ModelRun
        - value: Mistral
        - value: Modular
        - value: Moonshot AI
        - value: Morph
        - value: NCompass
        - value: Nebius
        - value: NextBit
        - value: Nineteen
        - value: Novita
        - value: Nvidia
        - value: OpenAI
        - value: OpenInference
        - value: Parasail
        - value: Perplexity
        - value: Phala
        - value: Relace
        - value: SambaNova
        - value: SiliconFlow
        - value: Stealth
        - value: Switchpoint
        - value: Targon
        - value: Together
        - value: Ubicloud
        - value: Venice
        - value: WandB
        - value: xAI
        - value: Z.AI
        - value: FakeProvider
    PublicEndpointQuantization:
      type: object
      properties: {}
    Parameter:
      type: string
      enum:
        - value: temperature
        - value: top_p
        - value: top_k
        - value: min_p
        - value: top_a
        - value: frequency_penalty
        - value: presence_penalty
        - value: repetition_penalty
        - value: max_tokens
        - value: logit_bias
        - value: logprobs
        - value: top_logprobs
        - value: seed
        - value: response_format
        - value: structured_outputs
        - value: stop
        - value: tools
        - value: tool_choice
        - value: parallel_tool_calls
        - value: include_reasoning
        - value: reasoning
        - value: web_search_options
        - value: verbosity
    EndpointStatus:
      type: string
      enum:
        - value: '0'
        - value: '-1'
        - value: '-2'
        - value: '-3'
        - value: '-5'
        - value: '-10'
    PublicEndpoint:
      type: object
      properties:
        name:
          type: string
        model_name:
          type: string
        context_length:
          type: number
          format: double
        pricing:
          $ref: '#/components/schemas/PublicEndpointPricing'
        provider_name:
          $ref: '#/components/schemas/ProviderName'
        tag:
          type: string
        quantization:
          $ref: '#/components/schemas/PublicEndpointQuantization'
        max_completion_tokens:
          type:
            - number
            - 'null'
          format: double
        max_prompt_tokens:
          type:
            - number
            - 'null'
          format: double
        supported_parameters:
          type: array
          items:
            $ref: '#/components/schemas/Parameter'
        status:
          $ref: '#/components/schemas/EndpointStatus'
        uptime_last_30m:
          type:
            - number
            - 'null'
          format: double
        supports_implicit_caching:
          type: boolean
      required:
        - name
        - model_name
        - context_length
        - pricing
        - provider_name
        - tag
        - quantization
        - max_completion_tokens
        - max_prompt_tokens
        - supported_parameters
        - uptime_last_30m
        - supports_implicit_caching
    Endpoints_listEndpointsZdr_Response_200:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/PublicEndpoint'
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/endpoints/zdr"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/endpoints/zdr';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

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
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/endpoints/zdr"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://openrouter.ai/api/v1/endpoints/zdr")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/endpoints/zdr")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/endpoints/zdr', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/endpoints/zdr");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/endpoints/zdr")! as URL,
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

# Get a model's supported parameters and data about which are most popular

GET https://openrouter.ai/api/v1/parameters/{author}/{slug}

Reference: https://openrouter.ai/docs/api-reference/parameters/get-parameters

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get a model's supported parameters and data about which are most popular
  version: endpoint_parameters.getParameters
paths:
  /parameters/{author}/{slug}:
    get:
      operationId: get-parameters
      summary: Get a model's supported parameters and data about which are most popular
      tags:
        - - subpackage_parameters
      parameters:
        - name: author
          in: path
          required: true
          schema:
            type: string
        - name: slug
          in: path
          required: true
          schema:
            type: string
        - name: provider
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/ParametersAuthorSlugGetParametersProvider'
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns the parameters for the specified model
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Parameters_getParameters_Response_200'
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '404':
          description: Not Found - Model or provider does not exist
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    ParametersAuthorSlugGetParametersProvider:
      type: string
      enum:
        - value: AI21
        - value: AionLabs
        - value: Alibaba
        - value: Amazon Bedrock
        - value: Anthropic
        - value: AtlasCloud
        - value: Atoma
        - value: Avian
        - value: Azure
        - value: BaseTen
        - value: Cerebras
        - value: Chutes
        - value: Cirrascale
        - value: Clarifai
        - value: Cloudflare
        - value: Cohere
        - value: CrofAI
        - value: Crusoe
        - value: DeepInfra
        - value: DeepSeek
        - value: Enfer
        - value: Featherless
        - value: Fireworks
        - value: Friendli
        - value: GMICloud
        - value: Google
        - value: Google AI Studio
        - value: Groq
        - value: Hyperbolic
        - value: Inception
        - value: InferenceNet
        - value: Infermatic
        - value: Inflection
        - value: Kluster
        - value: Lambda
        - value: Liquid
        - value: Mancer 2
        - value: Meta
        - value: Minimax
        - value: ModelRun
        - value: Mistral
        - value: Modular
        - value: Moonshot AI
        - value: Morph
        - value: NCompass
        - value: Nebius
        - value: NextBit
        - value: Nineteen
        - value: Novita
        - value: Nvidia
        - value: OpenAI
        - value: OpenInference
        - value: Parasail
        - value: Perplexity
        - value: Phala
        - value: Relace
        - value: SambaNova
        - value: SiliconFlow
        - value: Stealth
        - value: Switchpoint
        - value: Targon
        - value: Together
        - value: Ubicloud
        - value: Venice
        - value: WandB
        - value: xAI
        - value: Z.AI
        - value: FakeProvider
    ParametersAuthorSlugGetResponsesContentApplicationJsonSchemaDataSupportedParametersItems:
      type: string
      enum:
        - value: temperature
        - value: top_p
        - value: top_k
        - value: min_p
        - value: top_a
        - value: frequency_penalty
        - value: presence_penalty
        - value: repetition_penalty
        - value: max_tokens
        - value: logit_bias
        - value: logprobs
        - value: top_logprobs
        - value: seed
        - value: response_format
        - value: structured_outputs
        - value: stop
        - value: tools
        - value: tool_choice
        - value: parallel_tool_calls
        - value: include_reasoning
        - value: reasoning
        - value: web_search_options
        - value: verbosity
    ParametersAuthorSlugGetResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        model:
          type: string
        supported_parameters:
          type: array
          items:
            $ref: >-
              #/components/schemas/ParametersAuthorSlugGetResponsesContentApplicationJsonSchemaDataSupportedParametersItems
      required:
        - model
        - supported_parameters
    Parameters_getParameters_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/ParametersAuthorSlugGetResponsesContentApplicationJsonSchemaData
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/parameters/author/slug"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/parameters/author/slug';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

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
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/parameters/author/slug"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://openrouter.ai/api/v1/parameters/author/slug")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/parameters/author/slug")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/parameters/author/slug', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/parameters/author/slug");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/parameters/author/slug")! as URL,
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

# List all providers

GET https://openrouter.ai/api/v1/providers

Reference: https://openrouter.ai/docs/api-reference/providers/list-providers

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List all providers
  version: endpoint_providers.listProviders
paths:
  /providers:
    get:
      operationId: list-providers
      summary: List all providers
      tags:
        - - subpackage_providers
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns a list of providers
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Providers_listProviders_Response_200'
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    ProvidersGetResponsesContentApplicationJsonSchemaDataItems:
      type: object
      properties:
        name:
          type: string
        slug:
          type: string
        privacy_policy_url:
          type:
            - string
            - 'null'
        terms_of_service_url:
          type:
            - string
            - 'null'
        status_page_url:
          type:
            - string
            - 'null'
      required:
        - name
        - slug
        - privacy_policy_url
    Providers_listProviders_Response_200:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: >-
              #/components/schemas/ProvidersGetResponsesContentApplicationJsonSchemaDataItems
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/providers"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/providers';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

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
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/providers"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://openrouter.ai/api/v1/providers")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/providers")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/providers', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/providers");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/providers")! as URL,
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

# List API keys

GET https://openrouter.ai/api/v1/keys

Reference: https://openrouter.ai/docs/api-reference/api-keys/list

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: List API keys
  version: endpoint_apiKeys.list
paths:
  /keys:
    get:
      operationId: list
      summary: List API keys
      tags:
        - - subpackage_apiKeys
      parameters:
        - name: include_disabled
          in: query
          description: Whether to include disabled API keys in the response
          required: false
          schema:
            type: string
        - name: offset
          in: query
          description: Number of API keys to skip for pagination
          required: false
          schema:
            type: string
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: List of API keys
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/API Keys_list_Response_200'
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    KeysGetResponsesContentApplicationJsonSchemaDataItems:
      type: object
      properties:
        hash:
          type: string
        name:
          type: string
        label:
          type: string
        disabled:
          type: boolean
        limit:
          type:
            - number
            - 'null'
          format: double
        limit_remaining:
          type:
            - number
            - 'null'
          format: double
        limit_reset:
          type:
            - string
            - 'null'
        include_byok_in_limit:
          type: boolean
        usage:
          type: number
          format: double
        usage_daily:
          type: number
          format: double
        usage_weekly:
          type: number
          format: double
        usage_monthly:
          type: number
          format: double
        byok_usage:
          type: number
          format: double
        byok_usage_daily:
          type: number
          format: double
        byok_usage_weekly:
          type: number
          format: double
        byok_usage_monthly:
          type: number
          format: double
        created_at:
          type: string
        updated_at:
          type:
            - string
            - 'null'
      required:
        - hash
        - name
        - label
        - disabled
        - limit
        - limit_remaining
        - limit_reset
        - include_byok_in_limit
        - usage
        - usage_daily
        - usage_weekly
        - usage_monthly
        - byok_usage
        - byok_usage_daily
        - byok_usage_weekly
        - byok_usage_monthly
        - created_at
        - updated_at
    API Keys_list_Response_200:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: >-
              #/components/schemas/KeysGetResponsesContentApplicationJsonSchemaDataItems
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/keys"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/keys';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

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
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/keys"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://openrouter.ai/api/v1/keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/keys")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/keys', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/keys");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/keys")! as URL,
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

# Create a new API key

POST https://openrouter.ai/api/v1/keys
Content-Type: application/json

Reference: https://openrouter.ai/docs/api-reference/api-keys/create-keys

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create a new API key
  version: endpoint_apiKeys.createKeys
paths:
  /keys:
    post:
      operationId: create-keys
      summary: Create a new API key
      tags:
        - - subpackage_apiKeys
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '201':
          description: API key created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/API Keys_createKeys_Response_201'
        '400':
          description: Bad Request - Invalid request parameters
          content: {}
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                limit:
                  type:
                    - number
                    - 'null'
                  format: double
                limit_reset:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/KeysPostRequestBodyContentApplicationJsonSchemaLimitReset
                    - type: 'null'
                include_byok_in_limit:
                  type: boolean
              required:
                - name
components:
  schemas:
    KeysPostRequestBodyContentApplicationJsonSchemaLimitReset:
      type: string
      enum:
        - value: daily
        - value: weekly
        - value: monthly
    KeysPostResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        hash:
          type: string
        name:
          type: string
        label:
          type: string
        disabled:
          type: boolean
        limit:
          type:
            - number
            - 'null'
          format: double
        limit_remaining:
          type:
            - number
            - 'null'
          format: double
        limit_reset:
          type:
            - string
            - 'null'
        include_byok_in_limit:
          type: boolean
        usage:
          type: number
          format: double
        usage_daily:
          type: number
          format: double
        usage_weekly:
          type: number
          format: double
        usage_monthly:
          type: number
          format: double
        byok_usage:
          type: number
          format: double
        byok_usage_daily:
          type: number
          format: double
        byok_usage_weekly:
          type: number
          format: double
        byok_usage_monthly:
          type: number
          format: double
        created_at:
          type: string
        updated_at:
          type:
            - string
            - 'null'
      required:
        - hash
        - name
        - label
        - disabled
        - limit
        - limit_remaining
        - limit_reset
        - include_byok_in_limit
        - usage
        - usage_daily
        - usage_weekly
        - usage_monthly
        - byok_usage
        - byok_usage_daily
        - byok_usage_weekly
        - byok_usage_monthly
        - created_at
        - updated_at
    API Keys_createKeys_Response_201:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/KeysPostResponsesContentApplicationJsonSchemaData
        key:
          type: string
      required:
        - data
        - key

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/keys"

payload = {
    "name": "My New API Key",
    "limit": 50,
    "limit_reset": "monthly",
    "include_byok_in_limit": True
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/keys';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"name":"My New API Key","limit":50,"limit_reset":"monthly","include_byok_in_limit":true}'
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

	url := "https://openrouter.ai/api/v1/keys"

	payload := strings.NewReader("{\n  \"name\": \"My New API Key\",\n  \"limit\": 50,\n  \"limit_reset\": \"monthly\",\n  \"include_byok_in_limit\": true\n}")

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

url = URI("https://openrouter.ai/api/v1/keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"My New API Key\",\n  \"limit\": 50,\n  \"limit_reset\": \"monthly\",\n  \"include_byok_in_limit\": true\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/keys")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"My New API Key\",\n  \"limit\": 50,\n  \"limit_reset\": \"monthly\",\n  \"include_byok_in_limit\": true\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/keys', [
  'body' => '{
  "name": "My New API Key",
  "limit": 50,
  "limit_reset": "monthly",
  "include_byok_in_limit": true
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/keys");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"My New API Key\",\n  \"limit\": 50,\n  \"limit_reset\": \"monthly\",\n  \"include_byok_in_limit\": true\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "name": "My New API Key",
  "limit": 50,
  "limit_reset": "monthly",
  "include_byok_in_limit": true
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/keys")! as URL,
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

# Get a single API key

GET https://openrouter.ai/api/v1/keys/{hash}

Reference: https://openrouter.ai/docs/api-reference/api-keys/get-key

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get a single API key
  version: endpoint_apiKeys.getKey
paths:
  /keys/{hash}:
    get:
      operationId: get-key
      summary: Get a single API key
      tags:
        - - subpackage_apiKeys
      parameters:
        - name: hash
          in: path
          description: The hash identifier of the API key to retrieve
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: API key details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/API Keys_getKey_Response_200'
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '404':
          description: Not Found - API key does not exist
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    KeysHashGetResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        hash:
          type: string
        name:
          type: string
        label:
          type: string
        disabled:
          type: boolean
        limit:
          type:
            - number
            - 'null'
          format: double
        limit_remaining:
          type:
            - number
            - 'null'
          format: double
        limit_reset:
          type:
            - string
            - 'null'
        include_byok_in_limit:
          type: boolean
        usage:
          type: number
          format: double
        usage_daily:
          type: number
          format: double
        usage_weekly:
          type: number
          format: double
        usage_monthly:
          type: number
          format: double
        byok_usage:
          type: number
          format: double
        byok_usage_daily:
          type: number
          format: double
        byok_usage_weekly:
          type: number
          format: double
        byok_usage_monthly:
          type: number
          format: double
        created_at:
          type: string
        updated_at:
          type:
            - string
            - 'null'
      required:
        - hash
        - name
        - label
        - disabled
        - limit
        - limit_remaining
        - limit_reset
        - include_byok_in_limit
        - usage
        - usage_daily
        - usage_weekly
        - usage_monthly
        - byok_usage
        - byok_usage_daily
        - byok_usage_weekly
        - byok_usage_monthly
        - created_at
        - updated_at
    API Keys_getKey_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/KeysHashGetResponsesContentApplicationJsonSchemaData
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/keys/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"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/keys/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';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

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
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/keys/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"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://openrouter.ai/api/v1/keys/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")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/keys/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")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/keys/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', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/keys/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");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/keys/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")! as URL,
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

# Delete an API key

DELETE https://openrouter.ai/api/v1/keys/{hash}

Reference: https://openrouter.ai/docs/api-reference/api-keys/delete-keys

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Delete an API key
  version: endpoint_apiKeys.deleteKeys
paths:
  /keys/{hash}:
    delete:
      operationId: delete-keys
      summary: Delete an API key
      tags:
        - - subpackage_apiKeys
      parameters:
        - name: hash
          in: path
          description: The hash identifier of the API key to delete
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: API key deleted successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/API Keys_deleteKeys_Response_200'
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '404':
          description: Not Found - API key does not exist
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    API Keys_deleteKeys_Response_200:
      type: object
      properties:
        deleted:
          type: string
          enum:
            - type: booleanLiteral
              value: true
      required:
        - deleted

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/keys/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"

headers = {"Authorization": "Bearer <token>"}

response = requests.delete(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/keys/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';
const options = {method: 'DELETE', headers: {Authorization: 'Bearer <token>'}};

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
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/keys/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"

	req, _ := http.NewRequest("DELETE", url, nil)

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

url = URI("https://openrouter.ai/api/v1/keys/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")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.delete("https://openrouter.ai/api/v1/keys/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")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://openrouter.ai/api/v1/keys/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', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/keys/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");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/keys/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")! as URL,
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

# Update an API key

PATCH https://openrouter.ai/api/v1/keys/{hash}
Content-Type: application/json

Reference: https://openrouter.ai/docs/api-reference/api-keys/update-keys

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Update an API key
  version: endpoint_apiKeys.updateKeys
paths:
  /keys/{hash}:
    patch:
      operationId: update-keys
      summary: Update an API key
      tags:
        - - subpackage_apiKeys
      parameters:
        - name: hash
          in: path
          description: The hash identifier of the API key to update
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: API key updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/API Keys_updateKeys_Response_200'
        '400':
          description: Bad Request - Invalid request parameters
          content: {}
        '401':
          description: Unauthorized - Missing or invalid authentication
          content: {}
        '404':
          description: Not Found - API key does not exist
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                disabled:
                  type: boolean
                limit:
                  type:
                    - number
                    - 'null'
                  format: double
                limit_reset:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/KeysHashPatchRequestBodyContentApplicationJsonSchemaLimitReset
                    - type: 'null'
                include_byok_in_limit:
                  type: boolean
components:
  schemas:
    KeysHashPatchRequestBodyContentApplicationJsonSchemaLimitReset:
      type: string
      enum:
        - value: daily
        - value: weekly
        - value: monthly
    KeysHashPatchResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        hash:
          type: string
        name:
          type: string
        label:
          type: string
        disabled:
          type: boolean
        limit:
          type:
            - number
            - 'null'
          format: double
        limit_remaining:
          type:
            - number
            - 'null'
          format: double
        limit_reset:
          type:
            - string
            - 'null'
        include_byok_in_limit:
          type: boolean
        usage:
          type: number
          format: double
        usage_daily:
          type: number
          format: double
        usage_weekly:
          type: number
          format: double
        usage_monthly:
          type: number
          format: double
        byok_usage:
          type: number
          format: double
        byok_usage_daily:
          type: number
          format: double
        byok_usage_weekly:
          type: number
          format: double
        byok_usage_monthly:
          type: number
          format: double
        created_at:
          type: string
        updated_at:
          type:
            - string
            - 'null'
      required:
        - hash
        - name
        - label
        - disabled
        - limit
        - limit_remaining
        - limit_reset
        - include_byok_in_limit
        - usage
        - usage_daily
        - usage_weekly
        - usage_monthly
        - byok_usage
        - byok_usage_daily
        - byok_usage_weekly
        - byok_usage_monthly
        - created_at
        - updated_at
    API Keys_updateKeys_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/KeysHashPatchResponsesContentApplicationJsonSchemaData
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/keys/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"

payload = {
    "name": "Updated API Key Name",
    "disabled": False,
    "limit": 75,
    "limit_reset": "daily",
    "include_byok_in_limit": True
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/keys/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';
const options = {
  method: 'PATCH',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"name":"Updated API Key Name","disabled":false,"limit":75,"limit_reset":"daily","include_byok_in_limit":true}'
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

	url := "https://openrouter.ai/api/v1/keys/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"

	payload := strings.NewReader("{\n  \"name\": \"Updated API Key Name\",\n  \"disabled\": false,\n  \"limit\": 75,\n  \"limit_reset\": \"daily\",\n  \"include_byok_in_limit\": true\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://openrouter.ai/api/v1/keys/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")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Updated API Key Name\",\n  \"disabled\": false,\n  \"limit\": 75,\n  \"limit_reset\": \"daily\",\n  \"include_byok_in_limit\": true\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.patch("https://openrouter.ai/api/v1/keys/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")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Updated API Key Name\",\n  \"disabled\": false,\n  \"limit\": 75,\n  \"limit_reset\": \"daily\",\n  \"include_byok_in_limit\": true\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://openrouter.ai/api/v1/keys/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', [
  'body' => '{
  "name": "Updated API Key Name",
  "disabled": false,
  "limit": 75,
  "limit_reset": "daily",
  "include_byok_in_limit": true
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/keys/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");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Updated API Key Name\",\n  \"disabled\": false,\n  \"limit\": 75,\n  \"limit_reset\": \"daily\",\n  \"include_byok_in_limit\": true\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "name": "Updated API Key Name",
  "disabled": false,
  "limit": 75,
  "limit_reset": "daily",
  "include_byok_in_limit": true
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/keys/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")! as URL,
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

# Get current API key

GET https://openrouter.ai/api/v1/key

Get information on the API key associated with the current authentication session

Reference: https://openrouter.ai/docs/api-reference/api-keys/get-current-key

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get current API key
  version: endpoint_apiKeys.getCurrentKey
paths:
  /key:
    get:
      operationId: get-current-key
      summary: Get current API key
      description: >-
        Get information on the API key associated with the current
        authentication session
      tags:
        - - subpackage_apiKeys
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: API key details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/API Keys_getCurrentKey_Response_200'
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    KeyGetResponsesContentApplicationJsonSchemaDataRateLimit:
      type: object
      properties:
        requests:
          type: number
          format: double
        interval:
          type: string
        note:
          type: string
      required:
        - requests
        - interval
        - note
    KeyGetResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        label:
          type: string
        limit:
          type:
            - number
            - 'null'
          format: double
        usage:
          type: number
          format: double
        usage_daily:
          type: number
          format: double
        usage_weekly:
          type: number
          format: double
        usage_monthly:
          type: number
          format: double
        byok_usage:
          type: number
          format: double
        byok_usage_daily:
          type: number
          format: double
        byok_usage_weekly:
          type: number
          format: double
        byok_usage_monthly:
          type: number
          format: double
        is_free_tier:
          type: boolean
        is_provisioning_key:
          type: boolean
        limit_remaining:
          type:
            - number
            - 'null'
          format: double
        limit_reset:
          type:
            - string
            - 'null'
        include_byok_in_limit:
          type: boolean
        rate_limit:
          $ref: >-
            #/components/schemas/KeyGetResponsesContentApplicationJsonSchemaDataRateLimit
      required:
        - label
        - limit
        - usage
        - usage_daily
        - usage_weekly
        - usage_monthly
        - byok_usage
        - byok_usage_daily
        - byok_usage_weekly
        - byok_usage_monthly
        - is_free_tier
        - is_provisioning_key
        - limit_remaining
        - limit_reset
        - include_byok_in_limit
        - rate_limit
    API Keys_getCurrentKey_Response_200:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/KeyGetResponsesContentApplicationJsonSchemaData'
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/key"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/key';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

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
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/key"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://openrouter.ai/api/v1/key")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/key")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/key', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/key");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/key")! as URL,
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

# Exchange authorization code for API key

POST https://openrouter.ai/api/v1/auth/keys
Content-Type: application/json

Exchange an authorization code from the PKCE flow for a user-controlled API key

Reference: https://openrouter.ai/docs/api-reference/o-auth/exchange-auth-code-for-api-key

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Exchange authorization code for API key
  version: endpoint_oAuth.exchangeAuthCodeForAPIKey
paths:
  /auth/keys:
    post:
      operationId: exchange-auth-code-for-api-key
      summary: Exchange authorization code for API key
      description: >-
        Exchange an authorization code from the PKCE flow for a user-controlled
        API key
      tags:
        - - subpackage_oAuth
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successfully exchanged code for an API key
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/OAuth_exchangeAuthCodeForAPIKey_Response_200
        '400':
          description: Bad Request - Invalid request parameters or malformed input
          content: {}
        '403':
          description: Forbidden - Authentication successful but insufficient permissions
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                code:
                  type: string
                code_verifier:
                  type: string
                code_challenge_method:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/AuthKeysPostRequestBodyContentApplicationJsonSchemaCodeChallengeMethod
                    - type: 'null'
              required:
                - code
components:
  schemas:
    AuthKeysPostRequestBodyContentApplicationJsonSchemaCodeChallengeMethod:
      type: string
      enum:
        - value: S256
        - value: plain
    OAuth_exchangeAuthCodeForAPIKey_Response_200:
      type: object
      properties:
        key:
          type: string
        user_id:
          type:
            - string
            - 'null'
      required:
        - key
        - user_id

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/auth/keys"

payload = {
    "code": "auth_code_abc123def456",
    "code_verifier": "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk",
    "code_challenge_method": "S256"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/auth/keys';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"code":"auth_code_abc123def456","code_verifier":"dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk","code_challenge_method":"S256"}'
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

	url := "https://openrouter.ai/api/v1/auth/keys"

	payload := strings.NewReader("{\n  \"code\": \"auth_code_abc123def456\",\n  \"code_verifier\": \"dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk\",\n  \"code_challenge_method\": \"S256\"\n}")

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

url = URI("https://openrouter.ai/api/v1/auth/keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"code\": \"auth_code_abc123def456\",\n  \"code_verifier\": \"dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk\",\n  \"code_challenge_method\": \"S256\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/auth/keys")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"code\": \"auth_code_abc123def456\",\n  \"code_verifier\": \"dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk\",\n  \"code_challenge_method\": \"S256\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/auth/keys', [
  'body' => '{
  "code": "auth_code_abc123def456",
  "code_verifier": "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk",
  "code_challenge_method": "S256"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/auth/keys");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"code\": \"auth_code_abc123def456\",\n  \"code_verifier\": \"dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk\",\n  \"code_challenge_method\": \"S256\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "code": "auth_code_abc123def456",
  "code_verifier": "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk",
  "code_challenge_method": "S256"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/auth/keys")! as URL,
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

# Create authorization code

POST https://openrouter.ai/api/v1/auth/keys/code
Content-Type: application/json

Create an authorization code for the PKCE flow to generate a user-controlled API key

Reference: https://openrouter.ai/docs/api-reference/o-auth/create-auth-keys-code

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create authorization code
  version: endpoint_oAuth.createAuthKeysCode
paths:
  /auth/keys/code:
    post:
      operationId: create-auth-keys-code
      summary: Create authorization code
      description: >-
        Create an authorization code for the PKCE flow to generate a
        user-controlled API key
      tags:
        - - subpackage_oAuth
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successfully created authorization code
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OAuth_createAuthKeysCode_Response_200'
        '400':
          description: Bad Request - Invalid request parameters or malformed input
          content: {}
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                callback_url:
                  type: string
                  format: uri
                code_challenge:
                  type: string
                code_challenge_method:
                  $ref: >-
                    #/components/schemas/AuthKeysCodePostRequestBodyContentApplicationJsonSchemaCodeChallengeMethod
                limit:
                  type: number
                  format: double
              required:
                - callback_url
components:
  schemas:
    AuthKeysCodePostRequestBodyContentApplicationJsonSchemaCodeChallengeMethod:
      type: string
      enum:
        - value: S256
        - value: plain
    AuthKeysCodePostResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
        app_id:
          type: number
          format: double
        created_at:
          type: string
      required:
        - id
        - app_id
        - created_at
    OAuth_createAuthKeysCode_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/AuthKeysCodePostResponsesContentApplicationJsonSchemaData
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/auth/keys/code"

payload = {
    "callback_url": "https://myapp.com/auth/callback",
    "code_challenge": "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM",
    "code_challenge_method": "S256",
    "limit": 100
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/auth/keys/code';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"callback_url":"https://myapp.com/auth/callback","code_challenge":"E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM","code_challenge_method":"S256","limit":100}'
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

	url := "https://openrouter.ai/api/v1/auth/keys/code"

	payload := strings.NewReader("{\n  \"callback_url\": \"https://myapp.com/auth/callback\",\n  \"code_challenge\": \"E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM\",\n  \"code_challenge_method\": \"S256\",\n  \"limit\": 100\n}")

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

url = URI("https://openrouter.ai/api/v1/auth/keys/code")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"callback_url\": \"https://myapp.com/auth/callback\",\n  \"code_challenge\": \"E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM\",\n  \"code_challenge_method\": \"S256\",\n  \"limit\": 100\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/auth/keys/code")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"callback_url\": \"https://myapp.com/auth/callback\",\n  \"code_challenge\": \"E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM\",\n  \"code_challenge_method\": \"S256\",\n  \"limit\": 100\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/auth/keys/code', [
  'body' => '{
  "callback_url": "https://myapp.com/auth/callback",
  "code_challenge": "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM",
  "code_challenge_method": "S256",
  "limit": 100
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/auth/keys/code");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"callback_url\": \"https://myapp.com/auth/callback\",\n  \"code_challenge\": \"E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM\",\n  \"code_challenge_method\": \"S256\",\n  \"limit\": 100\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "callback_url": "https://myapp.com/auth/callback",
  "code_challenge": "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM",
  "code_challenge_method": "S256",
  "limit": 100
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/auth/keys/code")! as URL,
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

# Create a chat completion

POST https://openrouter.ai/api/v1/chat/completions
Content-Type: application/json

Sends a request for a model response for the given chat conversation. Supports both streaming and non-streaming modes.

Reference: https://openrouter.ai/docs/api-reference/chat/send-chat-completion-request

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create a chat completion
  version: endpoint_chat.sendChatCompletionRequest
paths:
  /chat/completions:
    post:
      operationId: send-chat-completion-request
      summary: Create a chat completion
      description: >-
        Sends a request for a model response for the given chat conversation.
        Supports both streaming and non-streaming modes.
      tags:
        - - subpackage_chat
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful chat completion response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatResponse'
        '400':
          description: Bad request - invalid parameters
          content: {}
        '401':
          description: Unauthorized - invalid API key
          content: {}
        '429':
          description: Too many requests - rate limit exceeded
          content: {}
        '500':
          description: Internal server error
          content: {}
      requestBody:
        description: Chat completion request parameters
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChatGenerationParams'
components:
  schemas:
    ChatMessageContentItemText:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: text
        text:
          type: string
      required:
        - type
        - text
    SystemMessageContent1:
      type: array
      items:
        $ref: '#/components/schemas/ChatMessageContentItemText'
    SystemMessageContent:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/SystemMessageContent1'
    SystemMessage:
      type: object
      properties:
        role:
          type: string
          enum:
            - type: stringLiteral
              value: system
        content:
          $ref: '#/components/schemas/SystemMessageContent'
        name:
          type: string
      required:
        - role
        - content
    ChatMessageContentItemImageImageUrlDetail:
      type: string
      enum:
        - value: auto
        - value: low
        - value: high
    ChatMessageContentItemImageImageUrl:
      type: object
      properties:
        url:
          type: string
        detail:
          $ref: '#/components/schemas/ChatMessageContentItemImageImageUrlDetail'
      required:
        - url
    ChatMessageContentItemImage:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: image_url
        image_url:
          $ref: '#/components/schemas/ChatMessageContentItemImageImageUrl'
      required:
        - type
        - image_url
    ChatMessageContentItemAudioInputAudioFormat:
      type: string
      enum:
        - value: wav
        - value: mp3
        - value: flac
        - value: m4a
        - value: ogg
        - value: pcm16
        - value: pcm24
    ChatMessageContentItemAudioInputAudio:
      type: object
      properties:
        data:
          type: string
        format:
          $ref: '#/components/schemas/ChatMessageContentItemAudioInputAudioFormat'
      required:
        - data
        - format
    ChatMessageContentItemAudio:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: input_audio
        input_audio:
          $ref: '#/components/schemas/ChatMessageContentItemAudioInputAudio'
      required:
        - type
        - input_audio
    ChatMessageContentItemVideoVideoUrl:
      type: object
      properties:
        url:
          type: string
      required:
        - url
    ChatMessageContentItemVideo:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: input_video
        video_url:
          $ref: '#/components/schemas/ChatMessageContentItemVideoVideoUrl'
      required:
        - type
        - video_url
    ChatMessageContentItem:
      oneOf:
        - $ref: '#/components/schemas/ChatMessageContentItemText'
        - $ref: '#/components/schemas/ChatMessageContentItemImage'
        - $ref: '#/components/schemas/ChatMessageContentItemAudio'
        - $ref: '#/components/schemas/ChatMessageContentItemVideo'
    UserMessageContent1:
      type: array
      items:
        $ref: '#/components/schemas/ChatMessageContentItem'
    UserMessageContent:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/UserMessageContent1'
    UserMessage:
      type: object
      properties:
        role:
          type: string
          enum:
            - type: stringLiteral
              value: user
        content:
          $ref: '#/components/schemas/UserMessageContent'
        name:
          type: string
      required:
        - role
        - content
    MessageOneOf2Content1:
      type: array
      items:
        $ref: '#/components/schemas/ChatMessageContentItemText'
    MessageOneOf2Content:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/MessageOneOf2Content1'
    Message2:
      type: object
      properties:
        role:
          type: string
          enum:
            - type: stringLiteral
              value: developer
        content:
          $ref: '#/components/schemas/MessageOneOf2Content'
        name:
          type: string
      required:
        - role
        - content
    AssistantMessageContent1:
      type: array
      items:
        $ref: '#/components/schemas/ChatMessageContentItem'
    AssistantMessageContent:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/AssistantMessageContent1'
    ChatMessageToolCallFunction:
      type: object
      properties:
        name:
          type: string
        arguments:
          type: string
      required:
        - name
        - arguments
    ChatMessageToolCall:
      type: object
      properties:
        id:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: function
        function:
          $ref: '#/components/schemas/ChatMessageToolCallFunction'
      required:
        - id
        - type
        - function
    AssistantMessage:
      type: object
      properties:
        role:
          type: string
          enum:
            - type: stringLiteral
              value: assistant
        content:
          oneOf:
            - $ref: '#/components/schemas/AssistantMessageContent'
            - type: 'null'
        name:
          type: string
        tool_calls:
          type: array
          items:
            $ref: '#/components/schemas/ChatMessageToolCall'
        refusal:
          type:
            - string
            - 'null'
        reasoning:
          type:
            - string
            - 'null'
      required:
        - role
    ToolResponseMessageContent1:
      type: array
      items:
        $ref: '#/components/schemas/ChatMessageContentItem'
    ToolResponseMessageContent:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ToolResponseMessageContent1'
    ToolResponseMessage:
      type: object
      properties:
        role:
          type: string
          enum:
            - type: stringLiteral
              value: tool
        content:
          $ref: '#/components/schemas/ToolResponseMessageContent'
        tool_call_id:
          type: string
      required:
        - role
        - content
        - tool_call_id
    Message:
      oneOf:
        - $ref: '#/components/schemas/SystemMessage'
        - $ref: '#/components/schemas/UserMessage'
        - $ref: '#/components/schemas/Message2'
        - $ref: '#/components/schemas/AssistantMessage'
        - $ref: '#/components/schemas/ToolResponseMessage'
    ModelName:
      type: string
    ChatGenerationParamsReasoningEffort:
      type: string
      enum:
        - value: minimal
        - value: low
        - value: medium
        - value: high
    ReasoningSummaryVerbosity:
      type: string
      enum:
        - value: auto
        - value: concise
        - value: detailed
    ChatGenerationParamsReasoning:
      type: object
      properties:
        effort:
          oneOf:
            - $ref: '#/components/schemas/ChatGenerationParamsReasoningEffort'
            - type: 'null'
        summary:
          oneOf:
            - $ref: '#/components/schemas/ReasoningSummaryVerbosity'
            - type: 'null'
    ChatGenerationParamsResponseFormat0:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: text
      required:
        - type
    ChatGenerationParamsResponseFormat1:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: json_object
      required:
        - type
    JSONSchemaConfig:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        schema:
          type: object
          additionalProperties:
            description: Any type
        strict:
          type:
            - boolean
            - 'null'
      required:
        - name
    ResponseFormatJSONSchema:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: json_schema
        json_schema:
          $ref: '#/components/schemas/JSONSchemaConfig'
      required:
        - type
        - json_schema
    ResponseFormatTextGrammar:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: grammar
        grammar:
          type: string
      required:
        - type
        - grammar
    ChatGenerationParamsResponseFormat4:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: python
      required:
        - type
    ChatGenerationParamsResponseFormat:
      oneOf:
        - $ref: '#/components/schemas/ChatGenerationParamsResponseFormat0'
        - $ref: '#/components/schemas/ChatGenerationParamsResponseFormat1'
        - $ref: '#/components/schemas/ResponseFormatJSONSchema'
        - $ref: '#/components/schemas/ResponseFormatTextGrammar'
        - $ref: '#/components/schemas/ChatGenerationParamsResponseFormat4'
    ChatGenerationParamsStop:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
    ChatStreamOptions:
      type: object
      properties:
        include_usage:
          type: boolean
    NamedToolChoiceFunction:
      type: object
      properties:
        name:
          type: string
      required:
        - name
    NamedToolChoice:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: function
        function:
          $ref: '#/components/schemas/NamedToolChoiceFunction'
      required:
        - type
        - function
    ToolChoiceOption:
      oneOf:
        - type: string
          enum:
            - type: stringLiteral
              value: none
        - type: string
          enum:
            - type: stringLiteral
              value: auto
        - type: string
          enum:
            - type: stringLiteral
              value: required
        - $ref: '#/components/schemas/NamedToolChoice'
    ToolDefinitionJsonFunction:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        parameters:
          type: object
          additionalProperties:
            description: Any type
        strict:
          type:
            - boolean
            - 'null'
      required:
        - name
    ToolDefinitionJson:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: function
        function:
          $ref: '#/components/schemas/ToolDefinitionJsonFunction'
      required:
        - type
        - function
    ChatGenerationParams:
      type: object
      properties:
        messages:
          type: array
          items:
            $ref: '#/components/schemas/Message'
        model:
          $ref: '#/components/schemas/ModelName'
        models:
          type: array
          items:
            $ref: '#/components/schemas/ModelName'
        frequency_penalty:
          type:
            - number
            - 'null'
          format: double
        logit_bias:
          type:
            - object
            - 'null'
          additionalProperties:
            type: number
            format: double
        logprobs:
          type:
            - boolean
            - 'null'
        top_logprobs:
          type:
            - number
            - 'null'
          format: double
        max_completion_tokens:
          type:
            - number
            - 'null'
          format: double
        max_tokens:
          type:
            - number
            - 'null'
          format: double
        metadata:
          type: object
          additionalProperties:
            type: string
        presence_penalty:
          type:
            - number
            - 'null'
          format: double
        reasoning:
          $ref: '#/components/schemas/ChatGenerationParamsReasoning'
        response_format:
          $ref: '#/components/schemas/ChatGenerationParamsResponseFormat'
        seed:
          type:
            - integer
            - 'null'
        stop:
          oneOf:
            - $ref: '#/components/schemas/ChatGenerationParamsStop'
            - type: 'null'
        stream:
          type: boolean
        stream_options:
          oneOf:
            - $ref: '#/components/schemas/ChatStreamOptions'
            - type: 'null'
        temperature:
          type:
            - number
            - 'null'
          format: double
        tool_choice:
          $ref: '#/components/schemas/ToolChoiceOption'
        tools:
          type: array
          items:
            $ref: '#/components/schemas/ToolDefinitionJson'
        top_p:
          type:
            - number
            - 'null'
          format: double
        user:
          type: string
      required:
        - messages
    ChatCompletionFinishReason:
      type: string
      enum:
        - value: tool_calls
        - value: stop
        - value: length
        - value: content_filter
        - value: error
    __schema0:
      oneOf:
        - $ref: '#/components/schemas/ChatCompletionFinishReason'
        - type: 'null'
    ChatMessageTokenLogprobTopLogprobsItems:
      type: object
      properties:
        token:
          type: string
        logprob:
          type: number
          format: double
        bytes:
          type:
            - array
            - 'null'
          items:
            type: number
            format: double
      required:
        - token
        - logprob
        - bytes
    ChatMessageTokenLogprob:
      type: object
      properties:
        token:
          type: string
        logprob:
          type: number
          format: double
        bytes:
          type:
            - array
            - 'null'
          items:
            type: number
            format: double
        top_logprobs:
          type: array
          items:
            $ref: '#/components/schemas/ChatMessageTokenLogprobTopLogprobsItems'
      required:
        - token
        - logprob
        - bytes
        - top_logprobs
    ChatMessageTokenLogprobs:
      type: object
      properties:
        content:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ChatMessageTokenLogprob'
        refusal:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ChatMessageTokenLogprob'
      required:
        - content
        - refusal
    ChatResponseChoice:
      type: object
      properties:
        finish_reason:
          $ref: '#/components/schemas/__schema0'
        index:
          type: number
          format: double
        message:
          $ref: '#/components/schemas/AssistantMessage'
        logprobs:
          oneOf:
            - $ref: '#/components/schemas/ChatMessageTokenLogprobs'
            - type: 'null'
      required:
        - finish_reason
        - index
        - message
    ChatGenerationTokenUsageCompletionTokensDetails:
      type: object
      properties:
        reasoning_tokens:
          type:
            - number
            - 'null'
          format: double
        audio_tokens:
          type:
            - number
            - 'null'
          format: double
        accepted_prediction_tokens:
          type:
            - number
            - 'null'
          format: double
        rejected_prediction_tokens:
          type:
            - number
            - 'null'
          format: double
    ChatGenerationTokenUsagePromptTokensDetails:
      type: object
      properties:
        cached_tokens:
          type: number
          format: double
        audio_tokens:
          type: number
          format: double
        video_tokens:
          type: number
          format: double
    ChatGenerationTokenUsage:
      type: object
      properties:
        completion_tokens:
          type: number
          format: double
        prompt_tokens:
          type: number
          format: double
        total_tokens:
          type: number
          format: double
        completion_tokens_details:
          oneOf:
            - $ref: >-
                #/components/schemas/ChatGenerationTokenUsageCompletionTokensDetails
            - type: 'null'
        prompt_tokens_details:
          oneOf:
            - $ref: '#/components/schemas/ChatGenerationTokenUsagePromptTokensDetails'
            - type: 'null'
      required:
        - completion_tokens
        - prompt_tokens
        - total_tokens
    ChatResponse:
      type: object
      properties:
        id:
          type: string
        choices:
          type: array
          items:
            $ref: '#/components/schemas/ChatResponseChoice'
        created:
          type: number
          format: double
        model:
          type: string
        object:
          type: string
          enum:
            - type: stringLiteral
              value: chat.completion
        system_fingerprint:
          type:
            - string
            - 'null'
        usage:
          $ref: '#/components/schemas/ChatGenerationTokenUsage'
      required:
        - id
        - choices
        - created
        - model
        - object

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/chat/completions"

payload = { "messages": [
        {
            "role": "string",
            "content": "string"
        }
    ] }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/chat/completions';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"messages":[{"role":"string","content":"string"}]}'
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

	url := "https://openrouter.ai/api/v1/chat/completions"

	payload := strings.NewReader("{\n  \"messages\": [\n    {\n      \"role\": \"string\",\n      \"content\": \"string\"\n    }\n  ]\n}")

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

url = URI("https://openrouter.ai/api/v1/chat/completions")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"messages\": [\n    {\n      \"role\": \"string\",\n      \"content\": \"string\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/chat/completions")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"messages\": [\n    {\n      \"role\": \"string\",\n      \"content\": \"string\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/chat/completions', [
  'body' => '{
  "messages": [
    {
      "role": "string",
      "content": "string"
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/chat/completions");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"messages\": [\n    {\n      \"role\": \"string\",\n      \"content\": \"string\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["messages": [
    [
      "role": "string",
      "content": "string"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/chat/completions")! as URL,
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

**Navigation:** [← Previous](./03-tool-calling.md) | [Index](./index.md) | [Next →](./05-create-a-completion.md)
