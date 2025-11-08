---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Available Metrics

### Common Labels

All metrics include the following common labels:

* `base_model`: The base model identifier (e.g., "accounts/fireworks/models/deepseek-v3")
* `deployment`: Full deployment path (e.g., "accounts/account-name/deployments/deployment-id")
* `deployment_account`: The account name
* `deployment_id`: The deployment identifier

### Rate Metrics (per second)

These metrics show activity rates calculated using 1-minute windows:

#### Request Rate

* `request_counter_total:sum_by_deployment`: Request rate per deployment

#### Error Rate

* `requests_error_total:sum_by_deployment`: Error rate per deployment, broken down by HTTP status code (includes additional `http_code` label)

#### Token Processing Rates

* `tokens_cached_prompt_total:sum_by_deployment`: Rate of cached prompt tokens per deployment
* `tokens_prompt_total:sum_by_deployment`: Rate of total prompt tokens processed per deployment

### Latency Histogram Metrics

These metrics provide latency distribution data with histogram buckets, calculated using 1-minute windows:

#### Generation Latency

* `latency_generation_per_token_ms_bucket:sum_by_deployment`: Per-token generation time distribution
* `latency_generation_queue_ms_bucket:sum_by_deployment`: Time spent waiting in generation queue

#### Request Latency

* `latency_overall_ms_bucket:sum_by_deployment`: End-to-end request latency distribution
* `latency_to_first_token_ms_bucket:sum_by_deployment`: Time to first token distribution

#### Prefill Latency

* `latency_prefill_ms_bucket:sum_by_deployment`: Prefill processing time distribution
* `latency_prefill_queue_ms_bucket:sum_by_deployment`: Time spent waiting in prefill queue

### Token Distribution Metrics

These histogram metrics show token count distributions per request, calculated using 1-minute windows:

* `tokens_generated_per_request_bucket:sum_by_deployment`: Distribution of generated tokens per request
* `tokens_prompt_per_request_bucket:sum_by_deployment`: Distribution of prompt tokens per request

### Resource Utilization Metrics

These gauge metrics show average resource usage:

* `generator_kv_blocks_fraction:avg_by_deployment`: Average fraction of KV cache blocks in use
* `generator_kv_slots_fraction:avg_by_deployment`: Average fraction of KV cache slots in use
* `generator_model_forward_time:avg_by_deployment`: Average time spent in model forward pass
* `requests_coordinator_concurrent_count:avg_by_deployment`: Average number of concurrent requests
* `prefiller_prompt_cache_ttl:avg_by_deployment`: Average prompt cache time-to-live


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
