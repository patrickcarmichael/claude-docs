---
title: "List GitHub Repositories"
source: "https://docs.cursor.com/en/background-agent/api/list-repositories"
language: "en"
language_name: "English"
---

# List GitHub Repositories
Source: https://docs.cursor.com/en/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
Retrieve a list of GitHub repositories accessible to the authenticated user.

<Warning>
  **This endpoint has very strict rate limits.**

  Limit requests to **1 / user / minute**, and **30 / user / hour.**

  This request can take tens of seconds to respond for users with access to many repositories.

  Make sure to handle this information not being available gracefully.
</Warning>

---

← Previous: [List Models](./list-models.md) | [Index](./index.md) | Next: [Overview](./overview.md) →