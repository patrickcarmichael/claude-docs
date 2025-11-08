---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 3: Clone nanochat and Set Up Environment

Let's clone the nanochat repository and set up the required dependencies.
```bash
  # Clone the repository

  git clone https://github.com/karpathy/nanochat.git
  cd nanochat

  # Add ~/.local/bin to your PATH

  export PATH="$HOME/.local/bin:$PATH"

  # Source the Cargo environment

  source "$HOME/.cargo/env"
```

**Install System Dependencies**

nanochat requires Python 3.10 and development headers:
```bash
  # Update package manager and install Python dependencies

  sudo apt-get update
  sudo apt-get install -y python3.10-dev

  # Verify Python installation

  python3 -c "import sysconfig; print(sysconfig.get_path('include'))"
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
