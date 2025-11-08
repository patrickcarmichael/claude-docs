---
title: "Crewai: Store knowledge in project directory"
description: "Store knowledge in project directory section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Store knowledge in project directory

project_root = Path(__file__).parent
knowledge_dir = project_root / "knowledge_storage"

os.environ["CREWAI_STORAGE_DIR"] = str(knowledge_dir)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Use with knowledge sources](./164-use-with-knowledge-sources.md)

**Next:** [Now all knowledge will be stored in your project directory →](./166-now-all-knowledge-will-be-stored-in-your-project-d.md)
