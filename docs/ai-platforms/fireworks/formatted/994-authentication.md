---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Authentication

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/authentication

Authentication for access to your account

### Signing in

Users using Google SSO can run:
```
firectl signin
```
If you are using [custom SSO](/accounts/sso), also specify the account ID:
```
firectl signin my-enterprise-account
```

### Authenticate with API Key

To authenticate with an API key, append `--api-key` to any firectl command.
```
firectl --api-key API_KEY <command>
```
To persist the API key for all subsequent commands, run:
```
firectl set-api-key API_KEY
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
