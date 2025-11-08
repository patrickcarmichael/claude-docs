---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Replace this with the key for the endpoint

api_key = "your-auth-key"
if not api_key:
    raise Exception("API Key is missing")

headers = {
    "Content-Type": "application/json",
    "Authorization": (api_key),
}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))
    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure

    print(error.info())
    print(error.read().decode("utf8", "ignore"))
```
You can find more code snippets, including examples of how to stream responses, in this [notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/cohere/webrequests.ipynb).

Though this section is called "Text Generation", it's worth pointing out that these models are capable of much more. Specifically, you can use Azure-hosted Cohere models for both retrieval augmented generation and [multi-step tool use](/docs/multi-step-tool-use). Check the linked pages for much more information.

Finally, we released refreshed versions of Command R and Command R+ in August 2024, both of which are now available on Azure. Check [these Microsoft docs](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-command?tabs=cohere-command-r-08-2024\&pivots=programming-language-python#:~:text=the%20model%20catalog.-,Cohere%20Command%20chat%20models,-The%20Cohere%20Command) for more information (select the Cohere Command R 08-2024 or Cohere Command R+ 08-2024 tabs).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
