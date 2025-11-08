---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Memory not persisting between sessions?**

* Check `CREWAI_STORAGE_DIR` environment variable
* Ensure write permissions to storage directory
* Verify memory is enabled with `memory=True`

**Mem0 authentication errors?**

* Verify `MEM0_API_KEY` environment variable is set
* Check API key permissions on Mem0 dashboard
* Ensure `mem0ai` package is installed

**High memory usage with large datasets?**

* Consider using External Memory with custom storage
* Implement pagination in custom storage search methods
* Use smaller embedding models for reduced memory footprint

### Performance Tips

* Use `memory=True` for most use cases (simplest and fastest)
* Only use User Memory if you need user-specific persistence
* Consider External Memory for high-scale or specialized requirements
* Choose smaller embedding models for faster processing
* Set appropriate search limits to control memory retrieval size

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Use secure storage paths](./248-use-secure-storage-paths.md)

**Next:** [Benefits of Using CrewAI's Memory System →](./250-benefits-of-using-crewais-memory-system.md)
