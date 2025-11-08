---
title: "Crewai: Store in project directory"
description: "Store in project directory section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Store in project directory

project_root = Path(__file__).parent
storage_dir = project_root / "crewai_storage"

os.environ["CREWAI_STORAGE_DIR"] = str(storage_dir)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Configure custom storage location](./215-configure-custom-storage-location.md)

**Next:** [Now all storage will be in your project directory →](./217-now-all-storage-will-be-in-your-project-directory.md)
