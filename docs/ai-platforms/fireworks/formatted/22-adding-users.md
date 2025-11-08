---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Adding users

To add a new user to your Fireworks account, run the following command. If the email for the new user is already associated with a Fireworks account, they will have the option to freely switch between your account and their existing account(s). You can also add users in the Fireworks web UI at [https://app.fireworks.ai/account/users](https://app.fireworks.ai/account/users).
```bash
firectl create user --email="alice@example.com"
```

To create another admin user, pass the `--role=admin` flag:
```bash
firectl create user --email="alice@example.com" --role=admin
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
