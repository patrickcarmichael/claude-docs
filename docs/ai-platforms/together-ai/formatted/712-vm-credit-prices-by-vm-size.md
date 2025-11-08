---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## VM credit prices by VM size

Below is a summary of how many VM credits are used per hour of runtime in each of our available VM sizes. Note that, by default, we recommend using the Nano VM size, as it should provide enough resources for most simple workflows (Pico is mostly suitable for very simple code execution jobs) .

| VM size | Credits / hour | Cost / hour | CPU      | RAM    |
| :------ | :------------- | :---------- | :------- | :----- |
| Pico    | 5 credits      | \$0.0743    | 2 cores  | 1 GB   |
| Nano    | 10 credits     | \$0.1486    | 2 cores  | 4 GB   |
| Micro   | 20 credits     | \$0.2972    | 4 cores  | 8 GB   |
| Small   | 40 credits     | \$0.5944    | 8 cores  | 16 GB  |
| Medium  | 80 credits     | \$1.1888    | 16 cores | 32 GB  |
| Large   | 160 credits    | \$2.3776    | 32 cores | 64 GB  |
| XLarge  | 320 credits    | \$4.7552    | 64 cores | 128 GB |

<br />

### Concurrent VMs

To pick the most suitable plan for your use case, consider how many concurrent VMs you require and pick the corresponding plan:

* Build (free) plan: 10 concurrent VMs
* Scale plan: 250 concurrent VMs
* Enterprise plan: custom concurrent VMs

In case you expect a a high volume of VM runtime, our Enterprise plan also provides special discounts on VM credits.

<Tip>
  ### For enterprise

  Please [contact Sales](https://www.together.ai/contact-sales)
</Tip>

### Estimating your bill

To estimate your bill, you must consider:

* The base price of your CodeSandbox plan.
* The number of included VM credits on that plan.
* How many VM credits you expect to require.

As an example, let's say you are planning to run 80 concurrent VMs on average, each running 3 hours per day, every day, on the Nano VM size. Here's the breakdown:

* You will need a Scale plan (which allows up to 100 concurrent VMs).
* You will use a total of 72,000 VM credits per month (80 VMs x 3 hours/day x 30 days x 10 credits/hour).
* Your Scale plan includes 1100 free VM credits each month, so you will purchase 70,900 VM credits (72,000 - 1100).

Based on this, your expected bill for that month is:

* Base price of Scale plan: \$170
* Total price of VM credits: $1053.57 (70,900 VM credits * $0.01486/credit)
* Total bill: \$1223.57

<br />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
