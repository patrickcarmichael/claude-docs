---
title: "Crewai: Initialize the tool for semantic searches within a specific GitHub repository, so the agent can search any repository if it learns about during its execution"
description: "Initialize the tool for semantic searches within a specific GitHub repository, so the agent can search any repository if it learns about during its execution section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize the tool for semantic searches within a specific GitHub repository, so the agent can search any repository if it learns about during its execution

tool = GithubSearchTool(
	gh_token='your_github_personal_access_token',
	content_types=['code', 'issue'] # Options: code, repo, pr, issue
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← OR](./1092-or.md)

**Next:** [Arguments →](./1094-arguments.md)
