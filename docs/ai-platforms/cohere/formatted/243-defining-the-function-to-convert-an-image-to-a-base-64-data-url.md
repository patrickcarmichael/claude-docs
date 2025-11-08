---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Defining the function to convert an image to a base 64 Data URL

def image_to_base64_data_url(image_path):
    _, file_extension = os.path.splitext(image_path)
    file_type = file_extension[1:]

    with open(image_path, "rb") as f:
        enc_img = base64.b64encode(f.read()).decode("utf-8")
        enc_img = f"data:image/{file_type};base64,{enc_img}"
    return enc_img


image_path = "<YOUR IMAGE PATH>"
base64_url = image_to_base64_data_url(image_path)
```

#### 2. Call the Embed Endpoint

<CodeBlocks>
```python PYTHON
  # Import the necessary packages

  import cohere

  co = cohere.ClientV2(api_key="<YOUR API KEY>")

  # format the input_object

  image_input = {
      "content": [
          {"type": "image_url", "image_url": {"url": base64_url}}
      ]
  }

  co.embed(
      model="embed-v4.0",
      inputs=[image_input],
      input_type="search_document",
      embedding_types=["float"],
  )
```
```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/embed \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "embed-v4.0",
      "inputs": [
        {
          "content": [
            {
              "type": "image_url",
              "image_url": {
                "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD..."
              }
            }
          ]
        }
      ],
      "input_type": "search_document",
      "embedding_types": ["float"]
    }'
```
</CodeBlocks>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
