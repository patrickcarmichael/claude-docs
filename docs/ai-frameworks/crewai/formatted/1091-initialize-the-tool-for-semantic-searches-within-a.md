---
title: "Crewai: Initialize the tool for semantic searches within a specific GitHub repository"
description: "Initialize the tool for semantic searches within a specific GitHub repository section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize the tool for semantic searches within a specific GitHub repository

tool = GithubSearchTool(
	github_repo='https://github.com/example/repo',
	gh_token='your_github_personal_access_token',
	content_types=['code', 'issue'] # Options: code, repo, pr, issue
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example](./1090-example.md)

**Next:** [OR →](./1092-or.md)
