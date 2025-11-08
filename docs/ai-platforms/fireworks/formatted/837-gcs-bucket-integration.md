---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## GCS Bucket Integration

Use external Google Cloud Storage (GCS) buckets for fine-tuning while keeping your data private. Fireworks creates proxy datasets that reference your external buckets—data is only accessed during fine-tuning within a secure, isolated cluster.

>   **ℹ️ Info**
>
> Your data never leaves your GCS bucket except during fine-tuning, ensuring maximum privacy and security.

### Required Permissions

You need to grant access to three service accounts:

#### Fireworks Control Plane

* **Account**: `fireworks-control-plane@fw-ai-cp-prod.iam.gserviceaccount.com`
* **Required role**: Custom role with `storage.buckets.getIamPolicy` permission
```bash Setup command theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:fireworks-control-plane@fw-ai-cp-prod.iam.gserviceaccount.com \
    --role=projects/<YOUR_PROJECT>/roles/<YOUR_CUSTOM_ROLE>
```

This service account will be used to retrieve the IAM Policy set on the bucket, so that we are able to perform bucket ownership verifications and access verifications during dataset creation.

#### Inference Service Account

* **Account**: `inference@fw-ai-cp-prod.iam.gserviceaccount.com`
* **Required role**: Storage Object Viewer or Storage Object Admin
```bash Storage Object Viewer theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:inference@fw-ai-cp-prod.iam.gserviceaccount.com \
    --role=roles/storage.objectViewer
```
```bash Storage Object Admin theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:inference@fw-ai-cp-prod.iam.gserviceaccount.com \
    --role=roles/storage.objectAdmin
```

This service account will be used to access the files in the bucket.

#### Your Company's Fireworks Service Account

* **Account**: Your company's Fireworks account registration email
* **Required role**: Storage Object Viewer or Storage Object Admin
```bash Storage Object Viewer theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:<YOUR_COMPANY_FW_ACCOUNT_EMAIL> \
    --role=roles/storage.objectViewer
```
```bash Storage Object Admin theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:<YOUR_COMPANY_FW_ACCOUNT_EMAIL> \
    --role=roles/storage.objectAdmin
```

This is used to validate that your account actually has access to the bucket that you are trying to reference the dataset from. The email associated with your account (not the email of the user, but the account itself, you can get it with `firectl get account`) must have at least read access to the bucket listed under the bucket access IAM policy.

### Usage Example

<Steps>
  <Step title="Create a Proxy Dataset">
    Create a dataset that references your external GCS bucket:
```bash
    firectl create dataset {DATASET_NAME} --external-url gs://bucket-name/object-name
```
    <Tip>
      Ensure your gsutil path points directly to the JSONL file. If the file is in a folder, make sure the folder contains only the intended file.
    </Tip>
  </Step>

  <Step title="Start Fine-tuning">
    Use the proxy dataset to create a fine-tuning job:
```bash
    firectl create sftj \
      --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
      --base-model "accounts/fireworks/models/{MODEL}" \
      --output-model {TRAINED_MODEL_NAME}
```typescript
    <Check>
      For additional options, run: `firectl create sftj -h`
    </Check>
  </Step>
</Steps>

### Key Benefits

<CardGroup cols={3}>
  <Card title="Data Privacy" icon="shield">
    Your data never leaves your GCS bucket except during fine-tuning
  </Card>

  <Card title="Security" icon="lock">
    Access is limited to isolated fine-tuning clusters
  </Card>

  <Card title="Simplicity" icon="circle">
    Reference external data without copying or moving files
  </Card>
</CardGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
