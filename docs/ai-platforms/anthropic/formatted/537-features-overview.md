---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Features overview

Source: https://docs.claude.com/en/docs/build-with-claude/overview

Explore Claude's advanced features and capabilities.

export const PlatformAvailability = ({claudeApi = false, claudeApiBeta = false, bedrock = false, bedrockBeta = false, vertexAi = false, vertexAiBeta = false}) => {
  const platforms = [];
  if (claudeApi || claudeApiBeta) {
    platforms.push(claudeApiBeta ? 'Claude API (Beta)' : 'Claude API');
  }
  if (bedrock || bedrockBeta) {
    platforms.push(bedrockBeta ? 'Amazon Bedrock (Beta)' : 'Amazon Bedrock');
  }
  if (vertexAi || vertexAiBeta) {
    platforms.push(vertexAiBeta ? "Google Cloud's Vertex AI (Beta)" : "Google Cloud's Vertex AI");
  }
  return <>
      {platforms.map((platform, index) => <span key={index}>
          {platform}
          {index < platforms.length - 1 && <><br /><br /></>}
        </span>)}
    </>;
};

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
