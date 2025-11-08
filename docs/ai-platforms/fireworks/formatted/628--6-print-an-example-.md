---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 6. Print an Example ---

if train_data:
    print("\n--- Example RFT training entry ---")
    print(json.dumps(train_data[0], indent=2))
```

### 9. 🛰️ Deploy an MCP Server for the Synthetic Data

Now, we'll start a remote server that speaks the Model Context Protocol (MCP). This server will wrap our synthetic DuckDB database, providing a standardized way for any external tool—in our case, the Fireworks RFT evaluator—to interact with it.

#### What is MCP?

The Model Context Protocol is an open standard that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals, MCP provides a standardized way to connect AI models to various data sources and tools.

Key benefits:

* **Flexibility**: Works with any data source or tool
* **Standardization**: One protocol for all integrations instead of custom APIs for each tool; MCP servers for many applications are readily available

> Real World 🌍: This pattern is directly applicable. You would run a similar MCP server to provide a secure, read-only interface to a production database replica or a data warehouse, allowing the fine-tuning process to happen without granting direct database credentials to the training environment.

9. a) Create a server script in this project's root directory (`run_mcp_server.py`). This Python script starts our database server. It is configured to be read-only.
```python
    import os, contextlib, uvicorn
    from starlette.applications import Starlette
    from starlette.routing import Mount
    from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
    from mcp_server_motherduck import build_application

    DB = "data/synthetic_openflights.db"          # ← path from previous steps

    PORT = int(os.environ.get("PORT", 8080))        # Cloud Run injects $PORT

    # 1️⃣ Build the core SQL-aware MCP server (read-only for safety).

    server, _ = build_application(db_path=DB, read_only=True)

    # 2️⃣ Wrap it so HTTP clients can talk to it (ASGI handler).

    sess = StreamableHTTPSessionManager(app=server, event_store=None, stateless=True)

    async def handler(scope, receive, send):
        await sess.handle_request(scope, receive, send)

    @contextlib.asynccontextmanager
    async def lifespan(app):
        async with sess.run():
            yield                                        # keep sessions alive

    # 3️⃣ Starlette turns that handler into a full ASGI app Uvicorn can serve.

    app = Starlette(routes=[Mount("/mcp", app=handler)], lifespan=lifespan)

    if __name__ == "__main__":
        print(f"🔥 MCP endpoint → http://0.0.0.0:{PORT}/mcp")
        uvicorn.run(app, host="0.0.0.0", port=PORT)
```

### 10. ☁️ Set Up Google Cloud CLI & .gcloudignore

We'll first set up the Google Cloud CLI and authenticate. Google Cloud Run provides an easy way to deploy containerized applications without managing infrastructure.

>   **Real World 🌍**\
> You would follow along here in the same way. Cloud Run is ideal for MCP servers because it auto-scales based on demand (down to zero when not in use, thus charging only for actual usage).

10. a) **Install** the SDK (macOS/Linux):
```bash
    curl -sSL https://sdk.cloud.google.com | bash
    exec -l $SHELL  # reload shell so 'gcloud' is available

```

11. b) **Log in** (creates local access token):
```bash
    gcloud auth login
```

12. c) **Set your active project desired gcloud project**:
```bash
    gcloud config set project < YOUR_PROJECT_ID >  # set up project in gcloud console before running this if not already done

```

### 11. 📦 Containerize & Deploy the MCP Server

We’ll build a Docker image and push it straight to Cloud Run.\
Remember to replace **`YOUR_PROJECT_ID`** with the project you actually want to bill.

>   **Real World 🌍**\
> You would follow along in the same way here.

11. a) Create `mcp_requirements.txt` containing the following:
```bash
mcp
mcp-server-motherduck
duckdb
uvicorn
starlette
```

11. b) Create a `Dockerfile` (no extension) containing the following
```bash
base
FROM python:3.11-slim
WORKDIR /app

COPY mcp_requirements.txt .
RUN pip install --no-cache-dir -r mcp_requirements.txt

COPY run_mcp_server.py .
COPY data/synthetic_openflights.db ./data/

EXPOSE 8080

CMD ["python", "run_mcp_server.py"]
```

11. c) Create a .gcloudignore file in your root dir (to only deploy files needed for MCP server) containing:
```bash

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
