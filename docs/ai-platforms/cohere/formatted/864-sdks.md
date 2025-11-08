---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## SDKs

The Cohere SDK is the primary way of accessing Cohere's models. We support SDKs in four different languages. To get started, please see the installation methods and code snippets below.

### Python

[https://github.com/cohere-ai/cohere-python](https://github.com/cohere-ai/cohere-python)
```bash
python -m pip install cohere --upgrade
```
```python
import cohere

co = cohere.ClientV2("<<apiKey>>")
response = co.chat(
    model="command-a-03-2025", 
    messages=[{"role": "user", "content": "hello world!"}]
)

print(response)
```

### Typescript

[https://github.com/cohere-ai/cohere-typescript](https://github.com/cohere-ai/cohere-typescript)
```bash
npm i -s cohere-ai
```
```typescript
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({
  token: '<<apiKey>>',
});

(async () => {
  const response = await cohere.chat({
    model: 'command-a-03-2025',
    messages: [
      {
        role: 'user',
        content: 'hello world!',
      },
    ],
  });

  console.log(response);
})();
```

### Java

[https://github.com/cohere-ai/cohere-java](https://github.com/cohere-ai/cohere-java)
```gradle
implementation 'com.cohere:cohere-java:1.x.x'
```
```java
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatRequest;
import com.cohere.api.types.*;
import java.util.List;

public class Default {
    public static void main(String[] args) {
        Cohere cohere = Cohere.builder().token("<<apiKey>>").clientName("snippet").build();

        ChatResponse response =
                cohere.v2()
                        .chat(
                                V2ChatRequest.builder()
                                    .model("command-a-03-2025")
                                    .messages(
                                        List.of(
                                            ChatMessageV2.user(
                                                UserMessage.builder()
                                                    .content(
                                                        UserMessageContent
                                                                .of("Hello world!"))
                                                    .build())))
                                    .build());

        System.out.println(response);
    }
}
```

### Go

[https://github.com/cohere-ai/cohere-go](https://github.com/cohere-ai/cohere-go)
```bash
go get github.com/cohere-ai/cohere-go/v2
```
```go
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
			Message: "Hello world!",
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
