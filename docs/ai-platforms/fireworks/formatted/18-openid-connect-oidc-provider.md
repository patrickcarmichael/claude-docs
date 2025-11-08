---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## OpenID Connect (OIDC) provider

<Steps>
  <Step title="Create OIDC client application">
    Create an OIDC client application in your identity provider, e.g. Okta.
  </Step>

  <Step title="Configure client">
    Ensure the client is configured for "code authorization" of the "web" type (i.e. with a client\_secret).
  </Step>

  <Step title="Set redirect URL">
    Set the client's "allowed redirect URL" to the URL provided by Fireworks. It looks like:
```http
    https://fireworks-<your-company-name>.auth.us-west-2.amazoncognito.com/oauth2/idpresponse
```
  </Step>

  <Step title="Note down client details">
    Note down the `issuer`, `client_id`, and `client_secret` for the newly created client. You will need to provide this to your Fireworks.ai representative to complete your account set up.
  </Step>
</Steps>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
