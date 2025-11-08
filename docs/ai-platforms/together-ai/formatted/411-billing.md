---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Billing

#### Compute Billing

Instant Clusters offer two compute billing options: **reserved** and **on-demand**.

* **Reservations** – Credits are charged upfront or deducted for the full
  reserved duration once the cluster is provisioned. Any usage beyond the reserved
  capacity is billed at on-demand rates.
* **On-Demand** – Pay only for the time your cluster is running, with no upfront
  commitment.

See our [pricing page](https://www.together.ai/instant-gpu-clusters) for current rates.

#### Storage Billing

Storage is billed on a **pay-as-you-go** basis, as detailed on our [pricing
page](https://www.together.ai/instant-gpu-clusters). You can freely increase or
decrease your storage volume size, with all usage billed at the same rate.

#### Viewing Usage and Invoices

You can view your current usage anytime on the [Billing page in
Settings](https://api.together.ai/settings/billing). Each invoice includes a
detailed breakdown of reservation, burst, and on-demand usage for compute and
storage

#### Cluster and Storage Lifecycles

Clusters and storage volumes follow different lifecycle policies:

* **Compute Clusters** – Clusters are automatically decommissioned when their
  reservation period ends. To extend a reservation, please contact your account
  team.
* **Storage Volumes** – Storage volumes are persistent and remain available as
  long as your billing account is in good standing. They are not automatically
  deleted.

#### Running Out of Credits

When your credits are exhausted, resources behave differently depending on their
type:

* **Reserved Compute** – Existing reservations remain active until their
  scheduled end date. Any additional on-demand capacity used to scale beyond the
  reservation is decommissioned.
* **Fully On-Demand Compute** – Clusters are first paused and then
  decommissioned if credits are not restored.
* **Storage Volumes** – Access is revoked first, and the data is later
  decommissioned.

You will receive alerts before these actions take place. For questions or
assistance, please contact your billing team.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
