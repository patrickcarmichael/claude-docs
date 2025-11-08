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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
