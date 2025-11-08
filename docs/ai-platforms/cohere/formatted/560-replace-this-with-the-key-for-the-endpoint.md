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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
