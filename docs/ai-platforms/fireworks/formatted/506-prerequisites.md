---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Prerequisites

1. **Google Cloud Platform (GCP) Account**: Active GCP account with billing enabled.
2. **`gcloud` CLI**: [Google Cloud CLI](https://cloud.google.com/sdk/docs/install) installed and authenticated (`gcloud auth login`, `gcloud auth application-default login`).
3. **APIs Enabled**: Ensure the following APIs are enabled in your GCP project:
   * Cloud Build API
   * Artifact Registry API
   * Cloud Run Admin API
   * Secret Manager API
4. **Permissions**: The authenticated user/service account for `gcloud` needs sufficient permissions (e.g., roles like "Cloud Build Editor", "Artifact Registry Administrator", "Cloud Run Admin", "Secret Manager Admin").
5. **`reward-kit` installed**: Ensure `reward-kit` is installed in your Python environment (e.g., `pip install reward-kit`).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
