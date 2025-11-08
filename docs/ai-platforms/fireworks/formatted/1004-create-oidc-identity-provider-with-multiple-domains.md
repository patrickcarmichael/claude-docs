---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create OIDC identity provider with multiple domains

firectl create identity-provider --display-name="Example OIDC" \
  --oidc-issuer="https://accounts.google.com" \
  --oidc-client-id="client123" \
  --oidc-client-secret="secret456" \
  --tenant-domains="example.com,example.co.uk"
```

### Flags

```
      --display-name string         The display name of the identity provider (required)
  -h, --help                        help for identity-provider
      --oidc-client-id string       The OIDC client ID for OIDC providers
      --oidc-client-secret string   The OIDC client secret for OIDC providers
      --oidc-issuer string          The OIDC issuer URL for OIDC providers
      --saml-metadata-url string    The SAML metadata URL for SAML providers
      --tenant-domains string       Comma-separated list of allowed domains for the organization (e.g., 'example.com,example.co.uk'). If not provided, domain will be derived from account email.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
