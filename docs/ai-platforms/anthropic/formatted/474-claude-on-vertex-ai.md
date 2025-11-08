---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Claude on Vertex AI

Source: https://docs.claude.com/en/docs/build-with-claude/claude-on-vertex-ai

Anthropic's Claude models are now generally available through [Vertex AI](https://cloud.google.com/vertex-ai).

export const ModelId = ({children, style = {}}) => {
  const copiedNotice = 'Copied!';
  const handleClick = e => {
    const element = e.currentTarget;
    const textSpan = element.querySelector('.model-id-text');
    const copiedSpan = element.querySelector('.model-id-copied');
    navigator.clipboard.writeText(children).then(() => {
      textSpan.style.opacity = '0';
      copiedSpan.style.opacity = '1';
      element.style.backgroundColor = '#d4edda';
      element.style.borderColor = '#c3e6cb';
      setTimeout(() => {
        textSpan.style.opacity = '1';
        copiedSpan.style.opacity = '0';
        element.style.backgroundColor = '#f5f5f5';
        element.style.borderColor = 'transparent';
      }, 2000);
    }).catch(error => {
      console.error('Failed to copy:', error);
    });
  };
  const handleMouseEnter = e => {
    const element = e.currentTarget;
    const copiedSpan = element.querySelector('.model-id-copied');
    const tooltip = element.querySelector('.copy-tooltip');
    if (tooltip && copiedSpan.style.opacity !== '1') {
      tooltip.style.opacity = '1';
    }
    element.style.backgroundColor = '#e8e8e8';
    element.style.borderColor = '#d0d0d0';
  };
  const handleMouseLeave = e => {
    const element = e.currentTarget;
    const copiedSpan = element.querySelector('.model-id-copied');
    const tooltip = element.querySelector('.copy-tooltip');
    if (tooltip) {
      tooltip.style.opacity = '0';
    }
    if (copiedSpan.style.opacity !== '1') {
      element.style.backgroundColor = '#f5f5f5';
      element.style.borderColor = 'transparent';
    }
  };
  const defaultStyle = {
    cursor: 'pointer',
    position: 'relative',
    transition: 'all 0.2s ease',
    display: 'inline-block',
    userSelect: 'none',
    backgroundColor: '#f5f5f5',
    padding: '2px 4px',
    borderRadius: '4px',
    fontFamily: 'Monaco, Consolas, "Courier New", monospace',
    fontSize: '0.75em',
    border: '1px solid transparent',
    ...style
  };
  return <span onClick={handleClick} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave} style={defaultStyle}>
      <span className="model-id-text" style={{
    transition: 'opacity 0.1s ease'
  }}>
        {children}
      </span>
      <span className="model-id-copied" style={{
    position: 'absolute',
    top: '2px',
    left: '4px',
    right: '4px',
    opacity: '0',
    transition: 'opacity 0.1s ease',
    color: '#155724'
  }}>
        {copiedNotice}
      </span>
    </span>;
};

The Vertex API for accessing Claude is nearly-identical to the [Messages API](/en/api/messages) and supports all of the same options, with two key differences:

* In Vertex, `model` is not passed in the request body. Instead, it is specified in the Google Cloud endpoint URL.
* In Vertex, `anthropic_version` is passed in the request body (rather than as a header), and must be set to the value `vertex-2023-10-16`.

Vertex is also supported by Anthropic's official [client SDKs](/en/api/client-sdks). This guide will walk you through the process of making a request to Claude on Vertex AI in either Python or TypeScript.

Note that this guide assumes you have already have a GCP project that is able to use Vertex AI. See [using the Claude 3 models from Anthropic](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude) for more information on the setup required, as well as a full walkthrough.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
