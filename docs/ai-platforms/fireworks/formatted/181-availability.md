---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Availability

Current region availability:

| **Region**           | **Quota availability** | **Hardware availability**              |
| -------------------- | ---------------------- | -------------------------------------- |
| `US_IOWA_1`          | Available by default   | `NVIDIA_H100_80GB`                     |
| `US_TEXAS_2`         | Available by default   | `NVIDIA_H100_80GB`                     |
| `REGION_UNSPECIFIED` | Available by default   | `ANY OF THE ABOVE/BELOW`               |
| `US_ARIZONA_1`       | Must be requested      | `NVIDIA_H100_80GB`                     |
| `US_CALIFORNIA_1`    | Must be requested      | `NVIDIA_H200_141GB`                    |
| `US_GEORGIA_2`       | Must be requested      | `NVIDIA_B200_180GB`                    |
| `US_ILLINOIS_1`      | Must be requested      | `NVIDIA_H100_80GB`                     |
| `US_ILLINOIS_2`      | Must be requested      | `NVIDIA_A100_80GB`                     |
| `US_UTAH_1`          | Must be requested      | `NVIDIA_B200_180GB`                    |
| `US_VIRGINIA_1`      | Must be requested      | `NVIDIA_H100_80GB` `NVIDIA_H200_141GB` |
| `US_WASHINGTON_1`    | Must be requested      | `NVIDIA_H100_80GB`                     |
| `US_WASHINGTON_2`    | Must be requested      | `NVIDIA_H100_80GB`                     |
| `US_WASHINGTON_3`    | Must be requested      | `NVIDIA_B200_180GB`                    |
| `EU_FRANKFURT_1`     | Must be requested      | `NVIDIA_H100_80GB`                     |
| `EU_ICELAND_1`       | Must be requested      | `NVIDIA_H200_141GB`                    |
| `EU_ICELAND_2`       | Must be requested      | `NVIDIA_H200_141GB`                    |
| `AP_TOKYO_1`         | Must be requested      | `NVIDIA_H100_80GB`                     |
| `AP_TOKYO_2`         | Must be requested      | `NVIDIA_H200_141GB`                    |

<Tip>
  If you hit a quota limit when requesting a specific region, try launching the deployment without specifying a region. This taps into your global account quota, which is more flexible.
  Deployments may still be placed in `Must be requested` regions when region is not specified, but region-level quota must be enabled to explicitly specify that region when creating
  a deployment.
</Tip>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
