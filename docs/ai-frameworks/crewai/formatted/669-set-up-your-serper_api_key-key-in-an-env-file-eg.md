---
title: "Crewai: Set up your SERPER_API_KEY key in an .env file, eg:"
description: "Set up your SERPER_API_KEY key in an .env file, eg: section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Set up your SERPER_API_KEY key in an .env file, eg:

# SERPER_API_KEY=<your api key>
load_dotenv()

search = GoogleSerperAPIWrapper()

class SearchTool(BaseTool):
    name: str = "Search"
    description: str = "Useful for search-based queries. Use this to find current information about markets, companies, and trends."
    search: GoogleSerperAPIWrapper = Field(default_factory=GoogleSerperAPIWrapper)

    def _run(self, query: str) -> str:
        """Execute the search query and return results"""
        try:
            return self.search.run(query)
        except Exception as e:
            return f"Error performing search: {str(e)}"

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← `LangChainTool`](./668-langchaintool.md)

**Next:** [Create Agents →](./670-create-agents.md)
