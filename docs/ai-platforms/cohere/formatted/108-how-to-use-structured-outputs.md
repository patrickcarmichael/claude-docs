---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to Use Structured Outputs

There are two ways to use Structured Outputs:

* **Structured Outputs (JSON)**. This is primarily used in text generation use cases.
* **Structured Outputs (Tools)**. Structured Outputs (Tools). This is primarily used in [tool use (or function calling)](https://docs.cohere.com/docs/tool-use) and [agents](https://docs.cohere.com/docs/multi-step-tool-use) use cases.

<Note title="API Compatibility">
  Structured Outputs with Tools are only supported in [Chat API V2](https://docs.cohere.com/reference/chat#request.body.strict_tools) via the `strict_tools` parameter. This parameter is not supported in Chat API V1.
</Note>

### Structured Outputs (JSON)

Here, you can call the Chat API to generate Structured Outputs in JSON format. JSON is a lightweight format that is easy for humans to read and write and is also easy for machines to parse.

This is particularly useful in text generation use cases, for example, when you want to extract specific information from the responses, perform data analysis, or integrate the responses into your applications seamlessly.

There are two ways of specifying the JSON output:

* JSON mode
* JSON Schema mode

#### JSON mode

In JSON mode, when making an API request, you can specify the `response_format` parameter to indicate that you want the response in a JSON object format.

<CodeBlocks>
```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="YOUR API KEY")

  res = co.chat(
      model="command-a-03-2025",
      messages=[
          {
              "role": "user",
              "content": "Generate a JSON describing a person, with the fields 'name' and 'age'",
          }
      ],
      response_format={"type": "json_object"},
  )

  print(res.message.content[0].text)
```
```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-03-2025",
      "messages": [
        {
          "role": "user",
          "content": "Generate a JSON describing a person, with the fields '\''name'\'' and '\''age'\''"
        }
      ],
      "response_format": {
        "type": "json_object"
      }
    }'
```
</CodeBlocks>

By setting the `response_format` type to `"json_object"` in the Chat API, the output of the model is guaranteed to be a valid JSON object.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
