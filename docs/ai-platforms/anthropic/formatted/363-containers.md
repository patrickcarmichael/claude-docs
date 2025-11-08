---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Containers

The code execution tool runs in a secure, containerized environment designed specifically for code execution, with a higher focus on Python.

### Runtime environment

* **Python version**: 3.11.12
* **Operating system**: Linux-based container
* **Architecture**: x86\_64 (AMD64)

### Resource limits

* **Memory**: 5GiB RAM
* **Disk space**: 5GiB workspace storage
* **CPU**: 1 CPU

### Networking and security

* **Internet access**: Completely disabled for security
* **External connections**: No outbound network requests permitted
* **Sandbox isolation**: Full isolation from host system and other containers
* **File access**: Limited to workspace directory only
* **Workspace scoping**: Like [Files](/en/docs/build-with-claude/files), containers are scoped to the workspace of the API key
* **Expiration**: Containers expire 30 days after creation

### Pre-installed libraries

The sandboxed Python environment includes these commonly used libraries:

* **Data Science**: pandas, numpy, scipy, scikit-learn, statsmodels
* **Visualization**: matplotlib, seaborn
* **File Processing**: pyarrow, openpyxl, xlsxwriter, xlrd, pillow, python-pptx, python-docx, pypdf, pdfplumber, pypdfium2, pdf2image, pdfkit, tabula-py, reportlab\[pycairo], Img2pdf
* **Math & Computing**: sympy, mpmath
* **Utilities**: tqdm, python-dateutil, pytz, joblib, unzip, unrar, 7zip, bc, rg (ripgrep), fd, sqlite

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
