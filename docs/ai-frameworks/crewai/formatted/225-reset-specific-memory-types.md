---
title: "Crewai: Reset specific memory types"
description: "Reset specific memory types section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Reset specific memory types

crew.reset_memories(command_type='short')     # Short-term memory
crew.reset_memories(command_type='long')      # Long-term memory
crew.reset_memories(command_type='entity')    # Entity memory
crew.reset_memories(command_type='knowledge') # Knowledge storage
```

### Production Best Practices

1. **Set `CREWAI_STORAGE_DIR`** to a known location in production for better control
2. **Choose explicit embedding providers** to match your LLM setup
3. **Monitor storage directory size** for large-scale deployments
4. **Include storage directories** in your backup strategy
5. **Set appropriate file permissions** (0o755 for directories, 0o644 for files)
6. **Use project-relative paths** for containerized deployments

### Common Storage Issues

**"ChromaDB permission denied" errors:**

```bash  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Reset all memory storage](./224-reset-all-memory-storage.md)

**Next:** [Fix permissions →](./226-fix-permissions.md)
