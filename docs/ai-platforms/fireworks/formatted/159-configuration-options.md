---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Configuration options

| Flag                     | Type      | Default       | Description                                            |
| ------------------------ | --------- | ------------- | ------------------------------------------------------ |
| `--min-replica-count`    | Integer   | 0             | Minimum number of replicas. Set to 0 for scale-to-zero |
| `--max-replica-count`    | Integer   | 1             | Maximum number of replicas                             |
| `--scale-up-window`      | Duration  | 30s           | Wait time before scaling up                            |
| `--scale-down-window`    | Duration  | 10m           | Wait time before scaling down                          |
| `--scale-to-zero-window` | Duration  | 1h            | Idle time before scaling to zero (min: 5m)             |
| `--load-targets`         | Key-value | `default=0.8` | Scaling thresholds. See options below                  |

**Load target options** (use as `--load-targets <key>=<value>[,<key>=<value>...]`):

* `default=<Fraction>` - General load target from 0 to 1
* `tokens_generated_per_second=<Integer>` - Desired tokens per second per replica
* `requests_per_second=<Number>` - Desired requests per second per replica
* `concurrent_requests=<Number>` - Desired concurrent requests per replica

When multiple targets are specified, the maximum replica count across all is used.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
