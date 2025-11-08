---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Snippets

#### Cohere Platform

<CodeBlocks>
```typescript TS 
  const { CohereClient } = require('cohere-ai');

  const cohere = new CohereClient({
    token: 'Your API key',
  });

  (async () => {
    const response = await cohere.chat({
      chatHistory: [
        { role: 'USER', message: 'Who discovered gravity?' },
        {
          role: 'CHATBOT',
          message: 'The man who is widely credited with discovering gravity is Sir Isaac Newton',
        },
      ],
      message: 'What year was he born?',
      // perform web search before answering the question. You can also use your own custom connector.
      connectors: [{ id: 'web-search' }],
    });

    console.log(response);
  })();
```
```python PYTHON
  import cohere

  co = cohere.Client("Your API key")

  response = co.chat(
      chat_history=[
          {"role": "USER", "message": "Who discovered gravity?"},
          {
              "role": "CHATBOT",
              "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton",
          },
      ],
      message="What year was he born?",
      # perform web search before answering the question. You can also use your own custom connector.

      connectors=[{"id": "web-search"}],
  )

  print(response)
```
```go GO
  package main

  import (
  	"context"
  	"log"

  	cohere "github.com/cohere-ai/cohere-go/v2"
  	client "github.com/cohere-ai/cohere-go/v2/client"
  )

  func main() {
  	co := client.NewClient(client.WithToken("Your API key"))

  	resp, err := co.Chat(
  		context.TODO(),
  		&cohere.ChatRequest{
  			ChatHistory: []*cohere.ChatMessage{
  				{
  					Role:    cohere.ChatMessageRoleUser,
  					Message: "Who discovered gravity?",
  				},
  				{
  					Role:    cohere.ChatMessageRoleChatbot,
  					Message: "The man who is widely credited with discovering gravity is Sir Isaac Newton",
  				}},
  			Message: "What year was he born?",
  			Connectors: []*cohere.ChatConnector{
  				{Id: "web-search"},
  			},
  		},
  	)

  	if err != nil {
  		log.Fatal(err)
  	}

  	log.Printf("%+v", resp)
  }
```
```java JAVA
  import com.cohere.api.Cohere;
  import com.cohere.api.requests.ChatRequest;
  import com.cohere.api.types.ChatMessage;
  import com.cohere.api.types.Message;
  import com.cohere.api.types.NonStreamedChatResponse;

  import java.util.List;


  public class ChatPost {
      public static void main(String[] args) {
          Cohere cohere = Cohere.builder().token("Your API key").clientName("snippet").build();

          NonStreamedChatResponse response = cohere.chat(
                  ChatRequest.builder()
                          .message("What year was he born?")
                          .chatHistory(
                                  List.of(Message.user(ChatMessage.builder().message("Who discovered gravity?").build()),
                                          Message.chatbot(ChatMessage.builder().message("The man who is widely credited with discovering gravity is Sir Isaac Newton").build()))).build());

          System.out.println(response);
      }
  }
```
</CodeBlocks>

#### Private Deployment

<CodeBlocks>
```typescript TS 
  const { CohereClient } = require('cohere-ai');

  const cohere = new CohereClientV2({
    token: '',
    environment: '<YOUR_DEPLOYMENT_URL>'
  });

  (async () => {
    const response = await cohere.chat({
      chatHistory: [
        { role: 'USER', message: 'Who discovered gravity?' },
        {
          role: 'CHATBOT',
          message: 'The man who is widely credited with discovering gravity is Sir Isaac Newton',
        },
      ],
      message: 'What year was he born?',
      // perform web search before answering the question. You can also use your own custom connector.
      connectors: [{ id: 'web-search' }],
    });

    console.log(response);
  })();
```
```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="", base_url="<YOUR_DEPLOYMENT_URL>")

  response = co.chat(
      chat_history=[
          {"role": "USER", "message": "Who discovered gravity?"},
          {
              "role": "CHATBOT",
              "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton",
          },
      ],
      message="What year was he born?",
      # perform web search before answering the question. You can also use your own custom connector.

      connectors=[{"id": "web-search"}],
  )

  print(response)
```
```go GO
  package main

  import (
  	"context"
  	"log"

  	cohere "github.com/cohere-ai/cohere-go/v2"
  	client "github.com/cohere-ai/cohere-go/v2/client"
  )

  func main() {
    co := client.NewClient(
  			  client.WithBaseURL("<YOUR_DEPLOYMENT_URL>"),
  		)

  	resp, err := co.V2.Chat(
  		context.TODO(),
  		&cohere.ChatRequest{
  			ChatHistory: []*cohere.ChatMessage{
  				{
  					Role:    cohere.ChatMessageRoleUser,
  					Message: "Who discovered gravity?",
  				},
  				{
  					Role:    cohere.ChatMessageRoleChatbot,
  					Message: "The man who is widely credited with discovering gravity is Sir Isaac Newton",
  				}},
  			Message: "What year was he born?",
  			Connectors: []*cohere.ChatConnector{
  				{Id: "web-search"},
  			},
  		},
  	)

  	if err != nil {
  		log.Fatal(err)
  	}

  	log.Printf("%+v", resp)
  }
```
```java JAVA
  import com.cohere.api.Cohere;
  import com.cohere.api.requests.ChatRequest;
  import com.cohere.api.types.ChatMessage;
  import com.cohere.api.types.Message;
  import com.cohere.api.types.NonStreamedChatResponse;

  import java.util.List;


  public class ChatPost {
      public static void main(String[] args) {
          Cohere cohere = Cohere.builder().token("Your API key").clientName("snippet").build();
          Cohere cohere = Cohere.builder().environment(Environment.custom("<YOUR_DEPLOYMENT_URL>")).clientName("snippet").build();

          NonStreamedChatResponse response = cohere.v2.chat(
                  ChatRequest.builder()
                          .message("What year was he born?")
                          .chatHistory(
                                  List.of(Message.user(ChatMessage.builder().message("Who discovered gravity?").build()),
                                          Message.chatbot(ChatMessage.builder().message("The man who is widely credited with discovering gravity is Sir Isaac Newton").build()))).build());

          System.out.println(response);
      }
  }
```
</CodeBlocks>

#### Bedrock

<Warning title="Rerank API Compatibility">
  Rerank v3.5 on Bedrock is only supported with Rerank API v2, via `BedrockClientV2()`
</Warning>

<CodeBlocks>
```typescript TS 
  const { BedrockClient } = require('cohere-ai');

  const cohere = new BedrockClient({
    awsRegion: "us-east-1",
    awsAccessKey: "...",
    awsSecretKey: "...",
    awsSessionToken: "...",
  });

  (async () => {
    const response = await cohere.chat({
      model: "cohere.command-r-plus-v1:0",
      chatHistory: [
        { role: 'USER', message: 'Who discovered gravity?' },
        {
          role: 'CHATBOT',
          message: 'The man who is widely credited with discovering gravity is Sir Isaac Newton',
        },
      ],
      message: 'What year was he born?',
    });

    console.log(response);
  })();
```
```python PYTHON
  import cohere

  co = cohere.BedrockClient(
      aws_region="us-east-1",
      aws_access_key="...",
      aws_secret_key="...",
      aws_session_token="...",
  )

  response = co.chat(
      model="cohere.command-r-plus-v1:0",
      chat_history=[
          {"role": "USER", "message": "Who discovered gravity?"},
          {
              "role": "CHATBOT",
              "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton",
          },
      ],
      message="What year was he born?",
  )

  print(response)
```
```go GO
  package main

  import (
  	"context"
  	"log"

  	cohere "github.com/cohere-ai/cohere-go/v2"
  	client "github.com/cohere-ai/cohere-go/v2/client"
    "github.com/cohere-ai/cohere-go/v2/core"
  )

  func main() {
  	co := client.NewBedrockClient([]core.RequestOption{}, []client.AwsRequestOption{
  		client.WithAwsRegion("us-east-1"),
  		client.WithAwsAccessKey(""),
  		client.WithAwsSecretKey(""),
  		client.WithAwsSessionToken(""),
  	})

  	resp, err := co.Chat(
  		context.TODO(),
  		&cohere.ChatRequest{
  			ChatHistory: []*cohere.ChatMessage{
  				{
  					Role:    cohere.ChatMessageRoleUser,
  					Message: "Who discovered gravity?",
  				},
  				{
  					Role:    cohere.ChatMessageRoleChatbot,
  					Message: "The man who is widely credited with discovering gravity is Sir Isaac Newton",
  				}},
  			Message: "What year was he born?",
  		},
  	)

  	if err != nil {
  		log.Fatal(err)
  	}

  	log.Printf("%+v", resp)
  }
```
```java JAVA
  //Coming Soon
```
</CodeBlocks>

#### Sagemaker

<CodeBlocks>
```typescript TS 
  const { SagemakerClient } = require('cohere-ai');

  const cohere = new SagemakerClient({
    awsRegion: "us-east-1",
    awsAccessKey: "...",
    awsSecretKey: "...",
    awsSessionToken: "...",
  });

  (async () => {
    const response = await cohere.chat({
      model: "my-endpoint-name",
      chatHistory: [
        { role: 'USER', message: 'Who discovered gravity?' },
        {
          role: 'CHATBOT',
          message: 'The man who is widely credited with discovering gravity is Sir Isaac Newton',
        },
      ],
      message: 'What year was he born?',
    });

    console.log(response);
  })();
```
```python PYTHON
  import cohere

  co = cohere.SagemakerClient(
      aws_region="us-east-1",
      aws_access_key="...",
      aws_secret_key="...",
      aws_session_token="...",
  )

  response = co.chat(
      model="my-endpoint-name",
      chat_history=[
          {"role": "USER", "message": "Who discovered gravity?"},
          {
              "role": "CHATBOT",
              "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton",
          },
      ],
      message="What year was he born?",
  )

  print(response)
```
```go GO
  package main

  import (
  	"context"
  	"log"

  	cohere "github.com/cohere-ai/cohere-go/v2"
  	client "github.com/cohere-ai/cohere-go/v2/client"
    "github.com/cohere-ai/cohere-go/v2/core"
  )

  func main() {
  	co := client.NewSagemakerClient([]core.RequestOption{}, []client.AwsRequestOption{
  		client.WithAwsRegion("us-east-1"),
  		client.WithAwsAccessKey(""),
  		client.WithAwsSecretKey(""),
  		client.WithAwsSessionToken(""),
  	})

  	resp, err := co.Chat(
  		context.TODO(),
  		&cohere.ChatRequest{
        Model: cohere.String("my-endpoint-name"),
  			ChatHistory: []*cohere.ChatMessage{
  				{
  					Role:    cohere.ChatMessageRoleUser,
  					Message: "Who discovered gravity?",
  				},
  				{
  					Role:    cohere.ChatMessageRoleChatbot,
  					Message: "The man who is widely credited with discovering gravity is Sir Isaac Newton",
  				}},
  			Message: "What year was he born?",
  		},
  	)

  	if err != nil {
  		log.Fatal(err)
  	}

  	log.Printf("%+v", resp)
  }
```
```java JAVA
  //Coming Soon
```
</CodeBlocks>

#### Azure

<CodeBlocks>
```typescript TS 
  const { CohereClient } = require('cohere-ai');

  const cohere = new CohereClient({
    token: "<azure token>",
    environment: "https://Cohere-command-r-plus-phulf-serverless.eastus2.inference.ai.azure.com/v1",
  });

  (async () => {
    const response = await cohere.chat({
      chatHistory: [
        { role: 'USER', message: 'Who discovered gravity?' },
        {
          role: 'CHATBOT',
          message: 'The man who is widely credited with discovering gravity is Sir Isaac Newton',
        },
      ],
      message: 'What year was he born?',
    });

    console.log(response);
  })();
```
```python PYTHON
  import cohere

  co = cohere.Client(
      api_key="<azure token>",
      base_url="https://Cohere-command-r-plus-phulf-serverless.eastus2.inference.ai.azure.com/v1",
  )

  response = co.chat(
      chat_history=[
          {"role": "USER", "message": "Who discovered gravity?"},
          {
              "role": "CHATBOT",
              "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton",
          },
      ],
      message="What year was he born?",
  )

  print(response)
```
```go GO
  package main

  import (
  	"context"
  	"log"

  	cohere "github.com/cohere-ai/cohere-go/v2"
  	client "github.com/cohere-ai/cohere-go/v2/client"
  )

  func main() {
  	client := client.NewClient(
  		client.WithToken("<azure token>"),
  		client.WithBaseURL("https://Cohere-command-r-plus-phulf-serverless.eastus2.inference.ai.azure.com/v1"),
  	)

  	resp, err := co.Chat(
  		context.TODO(),
  		&cohere.ChatRequest{
  			ChatHistory: []*cohere.ChatMessage{
  				{
  					Role:    cohere.ChatMessageRoleUser,
  					Message: "Who discovered gravity?",
  				},
  				{
  					Role:    cohere.ChatMessageRoleChatbot,
  					Message: "The man who is widely credited with discovering gravity is Sir Isaac Newton",
  				}},
  			Message: "What year was he born?",
  		},
  	)

  	if err != nil {
  		log.Fatal(err)
  	}

  	log.Printf("%+v", resp)
  }
```
```java JAVA
  import com.cohere.api.Cohere;
  import com.cohere.api.requests.ChatRequest;
  import com.cohere.api.types.ChatMessage;
  import com.cohere.api.types.Message;
  import com.cohere.api.types.NonStreamedChatResponse;

  import java.util.List;


  public class ChatPost {
      public static void main(String[] args) {
          Cohere cohere = Cohere.builder().environment(Environment.custom("https://Cohere-command-r-plus-phulf-serverless.eastus2.inference.ai.azure.com/v1")).token("<azure token>").clientName("snippet").build();

          NonStreamedChatResponse response = cohere.chat(
                  ChatRequest.builder()
                          .message("What year was he born?")
                          .chatHistory(
                                  List.of(Message.user(ChatMessage.builder().message("Who discovered gravity?").build()),
                                          Message.chatbot(ChatMessage.builder().message("The man who is widely credited with discovering gravity is Sir Isaac Newton").build()))).build());

          System.out.println(response);
      }
  }
```
</CodeBlocks>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
