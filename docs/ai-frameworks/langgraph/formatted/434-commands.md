---
title: "Langgraph: Commands"
description: "Commands section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Commands


LangGraph CLI provides the following core functionality:

| Command                                                        | Description                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`langgraph build`](../cloud/reference/cli.md#build)           | Builds a Docker image for the [LangGraph API server](./langgraph_server.md) that can be directly deployed.                                                                                                                                                                             |
| [`langgraph dev`](../cloud/reference/cli.md#dev)               | Starts a lightweight development server that requires no Docker installation. This server is ideal for rapid development and testing.                                                                                                                                                  |
| [`langgraph dockerfile`](../cloud/reference/cli.md#dockerfile) | Generates a [Dockerfile](https://docs.docker.com/reference/dockerfile/) that can be used to build images for and deploy instances of the [LangGraph API server](./langgraph_server.md). This is useful if you want to further customize the dockerfile or deploy in a more custom way. |
| [`langgraph up`](../cloud/reference/cli.md#up)                 | Starts an instance of the [LangGraph API server](./langgraph_server.md) locally in a docker container. This requires the docker server to be running locally. It also requires a LangSmith API key for local development or a license key for production use.                          |

For more information, see the [LangGraph CLI Reference](../cloud/reference/cli.md).

---

concepts/persistence.md

---

---

search:
  boost: 2

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Installation](./433-installation.md)

**Next:** [Persistence →](./435-persistence.md)
