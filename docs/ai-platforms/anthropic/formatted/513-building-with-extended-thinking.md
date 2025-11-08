---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Building with extended thinking

Source: https://docs.claude.com/en/docs/build-with-claude/extended-thinking


export const TryInConsoleButton = ({userPrompt, systemPrompt, maxTokens, thinkingBudgetTokens, buttonVariant = "primary", children}) => {
  const url = new URL("https://console.anthropic.com/workbench/new");
  if (userPrompt) {
    url.searchParams.set("user", userPrompt);
  }
  if (systemPrompt) {
    url.searchParams.set("system", systemPrompt);
  }
  if (maxTokens) {
    url.searchParams.set("max_tokens", maxTokens);
  }
  if (thinkingBudgetTokens) {
    url.searchParams.set("thinking.budget_tokens", thinkingBudgetTokens);
  }
  return <div style={{
    width: "100%",
    position: "relative",
    top: "-77px",
    textAlign: "right"
  }}>
      <a href={url.href} className={`btn size-xs ${buttonVariant}`} style={{
    position: "relative",
    right: "20px",
    zIndex: "10"
  }}>
        {children || "Try in Console"}{" "}
        <Icon icon="arrow-up-right" color="currentColor" size={14} />
      </a>
    </div>;
};

Extended thinking gives Claude enhanced reasoning capabilities for complex tasks, while providing varying levels of transparency into its step-by-step thought process before it delivers its final answer.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
