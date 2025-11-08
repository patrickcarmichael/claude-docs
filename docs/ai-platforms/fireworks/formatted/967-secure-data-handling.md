---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Secure Data Handling

**Data Ownership & Control:** Customers maintain ownership of their data. Customer data stored as part of an active workflow can be permanently deleted with auditable confirmation, and secure wipe processes ensure deleted assets cannot be reconstructed.

**Encryption**: Data is encrypted in transit (TLS 1.2+) and at rest (AES-256).

**Bring Your Own Bucket:** Customers may integrate their own cloud storage to retain governance and apply their own compliance frameworks.

* Datasets: [GCS Bucket Integration](/fine-tuning/secure-fine-tuning#gcs-bucket-integration) (AWS S3 coming soon)
* Models: [External AWS S3 Bucket Integration](/models/uploading-custom-models#uploading-your-model)
* (Coming soon) Encryption Keys: Customers may choose to use their own encryption keys and policies for end-to-end control.

**Access Logging:** All customer data access is logged, monitored, and protected against tampering. See [Audit & Access Logs](https://docs.fireworks.ai/guides/security_compliance/audit_logs).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
