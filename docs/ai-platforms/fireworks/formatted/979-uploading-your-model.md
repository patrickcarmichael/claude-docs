---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Uploading your model

<Tabs>
  <Tab title="Local files (CLI)">
    Upload from your local machine:
```bash
    firectl create model <MODEL_ID> /path/to/files/
```
  </Tab>

  <Tab title="S3 bucket (CLI)">
    For larger models, upload directly from an Amazon S3 bucket for faster transfer:
```bash
    firectl create model <MODEL_ID> s3://<BUCKET_NAME>/<PATH_TO_MODEL>/ \
      --aws-access-key-id <ACCESS_KEY_ID> \
      --aws-secret-access-key <SECRET_ACCESS_KEY>
```
    See the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id-credentials-access-keys-update.html) for how to generate an access key ID and secret access key pair.

    >   **📝 Note**
>
> Ensure the IAM user has read access to the S3 bucket containing the model.
  </Tab>

  <Tab title="REST API">
    For programmatic uploads (automation, CI/CD pipelines), use the Fireworks REST API with a 4-step process: create model → get upload URLs → upload files → validate.

    See the [REST API upload guide](/models/uploading-custom-models-api) for a complete Python example.
  </Tab>
</Tabs>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
