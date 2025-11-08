---
title: "Langgraph: How to handle large numbers of tools"
description: "How to handle large numbers of tools section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# How to handle large numbers of tools


<div class="admonition tip">
    <p class="admonition-title">Prerequisites</p>
    <p>
        This guide assumes familiarity with the following:
        <ul>
            <li>
                <a href="https://python.langchain.com/docs/concepts/#tools">
                    Tools
                </a>
            </li>
            <li>
                <a href="https://python.langchain.com/docs/concepts/#chat-models/">
                    Chat Models
                </a>
            </li>
            <li>
                <a href="https://python.langchain.com/docs/concepts/#embedding-models">
                    Embedding Models
                </a>
            </li>
            <li>
                <a href="https://python.langchain.com/docs/concepts/#vector-stores">
                    Vectorstores
                </a>
            </li>   
            <li>
                <a href="https://python.langchain.com/docs/concepts/#documents">
                    Document
                </a>
            </li>
        </ul>
    </p>
</div> 

The subset of available tools to call is generally at the discretion of the model (although many providers also enable the user to [specify or constrain the choice of tool](https://python.langchain.com/docs/how_to/tool_choice/)). As the number of available tools grows, you may want to limit the scope of the LLM's selection, to decrease token consumption and to help manage sources of error in LLM reasoning.

Here we will demonstrate how to dynamically adjust the tools available to a model. Bottom line up front: like [RAG](https://python.langchain.com/docs/concepts/#retrieval) and similar methods, we prefix the model invocation by retrieving over available tools. Although we demonstrate one implementation that searches over tool descriptions, the details of the tool selection can be customized as needed.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← filename: fibonacci_range.py](./187-filename-fibonacci_rangepy.md)

**Next:** [Setup →](./189-setup.md)
