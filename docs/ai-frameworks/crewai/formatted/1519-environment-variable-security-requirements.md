---
title: "Crewai: ⚠️ Environment Variable Security Requirements"
description: "⚠️ Environment Variable Security Requirements section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## ⚠️ Environment Variable Security Requirements


<Warning>
  **Important**: CrewAI AMP has security restrictions on environment variable names that can cause deployment failures if not followed.
</Warning>

### Blocked Environment Variable Patterns

For security reasons, the following environment variable naming patterns are **automatically filtered** and will cause deployment issues:

**Blocked Patterns:**

* Variables ending with `_TOKEN` (e.g., `MY_API_TOKEN`)
* Variables ending with `_PASSWORD` (e.g., `DB_PASSWORD`)
* Variables ending with `_SECRET` (e.g., `API_SECRET`)
* Variables ending with `_KEY` in certain contexts

**Specific Blocked Variables:**

* `GITHUB_USER`, `GITHUB_TOKEN`
* `AWS_REGION`, `AWS_DEFAULT_REGION`
* Various internal CrewAI system variables

### Allowed Exceptions

Some variables are explicitly allowed despite matching blocked patterns:

* `AZURE_AD_TOKEN`
* `AZURE_OPENAI_AD_TOKEN`
* `ENTERPRISE_ACTION_TOKEN`
* `CREWAI_ENTEPRISE_TOOLS_TOKEN`

### How to Fix Naming Issues

If your deployment fails due to environment variable restrictions:

```bash  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Option 2: Deploy Directly via Web Interface](./1518-option-2-deploy-directly-via-web-interface.md)

**Next:** [❌ These will cause deployment failures →](./1520-these-will-cause-deployment-failures.md)
