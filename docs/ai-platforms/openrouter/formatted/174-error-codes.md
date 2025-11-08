---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Error Codes

* **{HTTPStatus.S400_Bad_Request}**: Bad Request (invalid or missing params, CORS)
* **{HTTPStatus.S401_Unauthorized}**: Invalid credentials (OAuth session expired, disabled/invalid API key)
* **{HTTPStatus.S402_Payment_Required}**: Your account or API key has insufficient credits. Add more credits and retry the request.
* **{HTTPStatus.S403_Forbidden}**: Your chosen model requires moderation and your input was flagged
* **{HTTPStatus.S408_Request_Timeout}**: Your request timed out
* **{HTTPStatus.S429_Too_Many_Requests}**: You are being rate limited
* **{HTTPStatus.S502_Bad_Gateway}**: Your chosen model is down or we received an invalid response from it
* **{HTTPStatus.S503_Service_Unavailable}**: There is no available model provider that meets your routing requirements

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
