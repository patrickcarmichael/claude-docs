---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Modules

### reward\_function Module

The `reward_function` module contains the core functionality for creating and using reward functions.
```python
from reward_kit.reward_function import RewardFunction, reward_function
```

### evaluation Module

The `evaluation` module provides the `Evaluator` class for managing evaluation configurations and functions for creating and previewing evaluations.
```python
from reward_kit.evaluation import Evaluator, preview_evaluation, create_evaluation
```
Key components:

* **`Evaluator` class**: Manages metric loading, sample loading, and evaluator creation on the platform.
* **`preview_evaluation`**: Previews an evaluation with sample data before deployment.
* **`create_evaluation`**: Creates and deploys an evaluator to the platform.

### config Module

The `config` module handles loading and managing configurations for the Reward Kit, typically from a `rewardkit.yaml` file.
```python
from reward_kit.config import load_config, get_config, RewardKitConfig
```
Key functions and classes:

* **`load_config()` / `get_config()`**: Load the global Reward Kit configuration.
* **`RewardKitConfig`**: Pydantic model for the main configuration structure.
* Other models like `GCPCloudRunConfig`, `AWSLambdaConfig`.

### models Module

The `models` module contains data models used throughout the Reward Kit.
```python
from reward_kit.models import EvaluateResult, MetricResult, Message
```

### rewards Module

The `rewards` module contains specialized reward functions for specific use cases.
```python
from reward_kit.rewards.function_calling import match_function_call
```

### server Module

The `server` module provides the `RewardServer` class and `serve` function to host reward functions as a FastAPI application.
```python
from reward_kit.server import RewardServer, serve
```
Key components:

* **`RewardServer` class**: A class to encapsulate a reward function and run it as a server.
* **`serve()` function**: A utility to quickly serve a given reward function.

### auth Module

The `auth` module provides utility functions to retrieve authentication credentials, primarily for Fireworks AI.
```python
from reward_kit.auth import get_fireworks_api_key, get_fireworks_account_id
```
Key functions:

* **`get_fireworks_api_key()`**: Retrieves the Fireworks API key.
* **`get_fireworks_account_id()`**: Retrieves the Fireworks account ID.

### gcp\_tools Module

The `gcp_tools` module offers utilities for working with Google Cloud Platform, such as building and pushing Docker images to Artifact Registry and deploying to Cloud Run.
```python
from reward_kit.gcp_tools import build_and_push_docker_image, deploy_to_cloud_run
```

### packaging Module

The `packaging` module assists in preparing reward functions for deployment, for example, by generating Dockerfile content.
```python
from reward_kit.packaging import generate_dockerfile_content
```

### platform\_api Module

The `platform_api` module provides functions for direct interaction with the Fireworks AI platform API, such as managing secrets.
```python
from reward_kit.platform_api import create_or_update_fireworks_secret
```

### rl\_processing Module

The `rl_processing` module contains tools for processing data for Reinforcement Learning workflows, such as the `RLDataAligner`.
```python
from reward_kit.rl_processing import RLDataAligner
```typescript

### mcp Module (`reward_kit.mcp`)

This sub-package contains components related to the Model Context Protocol (MCP).

* **`reward_kit.mcp.clients`**: Provides clients for interacting with MCP-compliant servers.

### mcp\_agent Module (`reward_kit.mcp_agent`)

This sub-package provides a framework for building and running agents that interact with MCP servers. It includes orchestration logic, various backend implementations, and a collection of pre-built MCP servers for common tasks (e.g., filesystem, git).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
