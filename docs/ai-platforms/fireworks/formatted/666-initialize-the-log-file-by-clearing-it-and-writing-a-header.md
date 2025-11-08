---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Initialize the log file by clearing it and writing a header

with open(MANUAL_LOG_FILE, 'w', encoding='utf-8') as f:
    f.write(f"--- Evaluation Log ---\n")
    f.write(f"Log started at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

def write_to_log(message: str):
    """Appends a timestamped message to the manual log file."""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
    try:
        with open(MANUAL_LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{timestamp} - {message}\n")
    except Exception as e:
        # If logging fails, print an error to the console

        print(f"CRITICAL: Failed to write to log file '{MANUAL_LOG_FILE}'. Error: {e}")

print(f"Manual logging configured. Log file is '{MANUAL_LOG_FILE}'.")


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
