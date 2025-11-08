---
title: "Crewai: Implementation Details"
description: "Implementation Details section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Implementation Details


The `YoutubeChannelSearchTool` is implemented as a subclass of `RagTool`, which provides the base functionality for Retrieval-Augmented Generation:

```python Code theme={null}
class YoutubeChannelSearchTool(RagTool):
    name: str = "Search a Youtube Channels content"
    description: str = "A tool that can be used to semantic search a query from a Youtube Channels content."
    args_schema: Type[BaseModel] = YoutubeChannelSearchToolSchema

    def __init__(self, youtube_channel_handle: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        if youtube_channel_handle is not None:
            kwargs["data_type"] = DataType.YOUTUBE_CHANNEL
            self.add(youtube_channel_handle)
            self.description = f"A tool that can be used to semantic search a query the {youtube_channel_handle} Youtube Channels content."
            self.args_schema = FixedYoutubeChannelSearchToolSchema
            self._generate_description()

    def add(
        self,
        youtube_channel_handle: str,
        **kwargs: Any,
    ) -> None:
        if not youtube_channel_handle.startswith("@"):
            youtube_channel_handle = f"@{youtube_channel_handle}"
        super().add(youtube_channel_handle, **kwargs)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1208-run-the-task.md)

**Next:** [Conclusion →](./1210-conclusion.md)
