---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 5. Upload the dataset

The CSV data is uploaded programmatically, not via AI-generated code. The code interpreter by E2B runs inside the E2B sandbox. Read more about the file upload [here](https://e2b.dev/docs/sandbox/api/upload).
```py
def upload_dataset(code_interpreter):
    print("Uploading dataset to Code Interpreter sandbox...")
    dataset_path = "./data.csv"

    if not os.path.exists(dataset_path):
        raise FileNotFoundError("Dataset file not found")

    try:
        with open(dataset_path, "rb") as f:
            remote_path = code_interpreter.upload_file(f)

        if not remote_path:
            raise ValueError("Failed to upload dataset")

        print("Uploaded at", remote_path)
        return remote_path
    except Exception as error:
        print("Error during file upload:", error)
        raise error
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
