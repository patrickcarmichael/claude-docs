---
title: "Crewai: Arguments"
description: "Arguments section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Arguments


* `github_repo` : The URL of the GitHub repository where the search will be conducted. This is a mandatory field and specifies the target repository for your search.
* `gh_token` : Your GitHub Personal Access Token (PAT) required for authentication. You can create one in your GitHub account settings under Developer Settings > Personal Access Tokens.
* `content_types` : Specifies the types of content to include in your search. You must provide a list of content types from the following options: `code` for searching within the code,
  `repo` for searching within the repository's general information, `pr` for searching within pull requests, and `issue` for searching within issues.
  This field is mandatory and allows tailoring the search to specific content types within the GitHub repository.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool for semantic searches within a specific GitHub repository, so the agent can search any repository if it learns about during its execution](./1093-initialize-the-tool-for-semantic-searches-within-a.md)

**Next:** [Custom model and embeddings →](./1095-custom-model-and-embeddings.md)
