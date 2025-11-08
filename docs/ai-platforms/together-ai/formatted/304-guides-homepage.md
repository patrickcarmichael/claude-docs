---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Guides Homepage

Source: https://docs.together.ai/docs/guides

Quickstarts and step-by-step guides for building with Together AI.

export const GridGuides = ({children}) => {
  return <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 md:gap-4 xl:gap-6">
      {children}
    </div>;
};

export const GuideCard = ({title, description, href, badges = [], className = ""}) => {
  const getTagColor = tag => {
    const tagColors = {
      python: {
        bg: "#dbeafe",
        text: "#1e40af"
      },
      typescript: {
        bg: "#dcfce7",
        text: "#166534"
      },
      chat: {
        bg: "#e0f2fe",
        text: "#0c4a6e"
      },
      audio: {
        bg: "#fef3c7",
        text: "#92400e"
      },
      vision: {
        bg: "#f3e8ff",
        text: "#6b21a8"
      },
      agents: {
        bg: "#e0e7ff",
        text: "#3730a3"
      },
      rerank: {
        bg: "#cffafe",
        text: "#0e7490"
      },
      "bing-api": {
        bg: "#dbeafe",
        text: "#1e40af"
      },
      embeddings: {
        bg: "#e0e7ff",
        text: "#3730a3"
      },
      rag: {
        bg: "#ecfdf5",
        text: "#166534"
      },
      huggingface: {
        bg: "#fef3c7",
        text: "#92400e"
      },
      "vercel-ai-sdk": {
        bg: "#f9fafb",
        text: "#111827"
      },
      mastra: {
        bg: "#ecfdf5",
        text: "#166534"
      },
      workflows: {
        bg: "#f1f5f9",
        text: "#334155"
      },
      sequential: {
        bg: "#ccfbf1",
        text: "#0f766e"
      },
      parallel: {
        bg: "#f3e8ff",
        text: "#7c3aed"
      },
      async: {
        bg: "#fce7f3",
        text: "#be185d"
      },
      routing: {
        bg: "#fed7aa",
        text: "#9a3412"
      },
      json: {
        bg: "#f9fafb",
        text: "#374151"
      },
      optimization: {
        bg: "#d1fae5",
        text: "#065f46"
      },
      ensemble: {
        bg: "#fce7f3",
        text: "#be185d"
      },
      cli: {
        bg: "#cffafe",
        text: "#0e7490"
      },
      terminal: {
        bg: "#d1fae5",
        text: "#065f46"
      },
      frameworks: {
        bg: "#cffafe",
        text: "#0e7490"
      },
      langgraph: {
        bg: "#f3e8ff",
        text: "#6b21a8"
      },
      crewai: {
        bg: "#fef2f2",
        text: "#991b1b"
      },
      training: {
        bg: "#fed7aa",
        text: "#9a3412"
      },
      "instant-clusters": {
        bg: "#f3e8ff",
        text: "#7c3aed"
      }
    };
    const tagName = tag.toLowerCase().replace(/ /g, "-");
    if (tagColors[tagName]) {
      return {
        bg: tagColors[tagName].bg,
        text: tagColors[tagName].text
      };
    }
    return {
      bg: "#f9fafb",
      text: "#374151"
    };
  };
  const CardContent = <div className={`flex flex-col justify-start items-start w-full overflow-hidden gap-2.5 px-5 py-4 rounded-2xl bg-white dark:bg-transparent dark:hover:bg-[#0B0C0E] border border-[#d9e1ec] dark:border-gray-700 hover:bg-gray-50 transition-all ${className}`}>
      <div className="flex flex-col justify-start items-start self-stretch flex-grow-0 flex-shrink-0 gap-2">
        {badges.length > 0 && <div className="flex justify-start items-start flex-grow-0 flex-shrink-0 gap-2.5 flex-wrap">
            {badges.map((badge, index) => {
    const colors = getTagColor(badge);
    return <div key={index} className={`flex justify-center items-center flex-grow-0 flex-shrink-0 relative overflow-hidden gap-2.5 px-2 py-1 rounded-[100px] dark:invert`} style={{
      backgroundColor: colors.bg
    }}>
                  <p className="flex-grow-0 flex-shrink-0 text-xs text-center capitalize" style={{
      color: colors.text
    }}>
                    {badge}
                  </p>
                </div>;
  })}
          </div>}
        <div className="flex flex-col justify-start items-start self-stretch flex-grow-0 flex-shrink-0 relative gap-1.5">
          <p className="self-stretch flex-grow-0 flex-shrink-0 text-base text-left text-black dark:text-white font-normal">
            {title}
          </p>
          <p className="flex-grow-0 flex-shrink-0 text-sm font-light text-left text-neutral-600 dark:text-gray-400">
            {description}
          </p>
        </div>
      </div>
    </div>;
  if (href) {
    return <a href={href} className="flex underline-none outline-none border-none">
        {CardContent}
      </a>;
  }
  return CardContent;
};

export const SubHeading = ({heading, description}) => {
  return <div className="flex flex-col md:flex-row gap-6 items-center mb-3 mt-10">
      <p className="text-lg font-medium text-left text-neutral-900 dark:text-white">
        {heading}
      </p>
      <p className="text-base text-left text-neutral-600 dark:text-gray-400">{description}</p>
    </div>;
};

<SubHeading heading={"Agents"} description={"Design agent loops, tools, and planners"} />

<GridGuides>
  <GuideCard title="Agent Workflows" description="Orchestrating together multiple language model calls to solve complex tasks." href="/docs/workflows" badges={["workflows", "python"]} />

  <GuideCard title="Sequential Agent Workflow" description="Tasks execute one after another when later steps depend on earlier ones." href="/docs/sequential-agent-workflow" badges={["sequential", "python"]} />

  <GuideCard title="Parallel Workflows" description="Multiple tasks execute simultaneously for improved performance." href="/docs/parallel-workflows" badges={["async", "parallel", "python"]} />

  <GuideCard title="Conditional Workflows" description="The workflow branches based on evaluation results." href="/docs/conditional-workflows" badges={["routing", "json", "python"]} />

  <GuideCard title="Iterative Workflow" description="A task repeats until a condition is met for optimization." href="/docs/iterative-workflow" badges={["optimization", "json", "python"]} />

  <GuideCard title="Agent Integrations" description="Using OSS agent frameworks with Together AI" href="/docs/integrations-2" badges={["frameworks", "langgraph", "crewai"]} />
</GridGuides>

<SubHeading heading={"Apps"} description={"Full-stack patterns you can copy"} />

<GridGuides>
  <GuideCard title="How to Build Coding Agents" description="How to build your own simple code editing agent from scratch in 400 lines of code!" href="/docs/how-to-build-coding-agents" badges={["chat", "python"]} />

  <GuideCard title="How to Build a Lovable Clone with Kimi K2" description="Learn how to build a full-stack Next.js app that can generate React apps with a single prompt." href="/docs/how-to-build-a-lovable-clone-with-kimi-k2" badges={["chat", "typescript"]} />

  <GuideCard title="How to Build Real-time Audio Transcription App" description="Build real-time audio transcription using Together AI models." href="/docs/how-to-build-real-time-audio-transcription-app" badges={["audio", "typescript"]} />

  <GuideCard title="Data Analyst Agent" description="Build an AI agent that can analyze data and provide insights." href="/docs/data-analyst-agent" badges={["agents", "python"]} />

  <GuideCard title="Open NotebookLM PDF to Podcast" description="Convert PDF documents into podcast episodes using AI." href="/docs/open-notebooklm-pdf-to-podcast" badges={["chat", "typescript"]} />

  <GuideCard title="AI Tutor" description="Build an intelligent tutoring system with Together AI." href="/docs/ai-tutor" badges={["agents", "python"]} />
</GridGuides>

<SubHeading heading={"Search & RAG"} description={"Build intelligent search and retrieval systems"} />

<GridGuides>
  <GuideCard title="How to Improve Search With Rerankers" description="Learn how you can improve semantic search quality with reranker models!" href="/docs/how-to-improve-search-with-rerankers" badges={["rerank", "python"]} />

  <GuideCard title="AI Search Engine" description="Build a simplified Perplexity-style search using Together models." href="/docs/ai-search-engine" badges={["bing-api", "typescript"]} />

  <GuideCard title="Building a RAG Workflow" description="Combine retrieval and generation to build grounded RAG apps." href="/docs/building-a-rag-workflow" badges={["embeddings", "rag", "python"]} />

  <GuideCard title="How to Implement Contextual RAG from Anthropic" description="Implement advanced RAG techniques with contextual understanding." href="/docs/how-to-implement-contextual-rag-from-anthropic" badges={["rag", "rerank", "python"]} />

  <GuideCard title="Quickstart Retrieval Augmented Generation RAG" description="Get started with RAG using Together AI's powerful models." href="/docs/quickstart-retrieval-augmented-generation-rag" badges={["rag", "embeddings", "python"]} />
</GridGuides>

<SubHeading heading={"General Guides"} description={"Essential guides and tutorials"} />

<GridGuides>
  <GuideCard title="How to run nanochat on Instant Clusters⚡️" description="Learn how to train Andrej Karpathy's end-to-end ChatGPT clone on Together's on-demand GPU clusters" href="/docs/nanochat-on-instant-clusters" badges={["training", "instant clusters", "python"]} />

  <GuideCard title="Quickstart Using Hugging Face Inference" description="Use Together AI with Hugging Face models and workflows." href="/docs/quickstart-using-hugging-face-inference" badges={["huggingface", "python"]} />

  <GuideCard title="Using Together with Vercel's AI SDK" description="Build powerful apps with Vercel's AI SDK and Together AI." href="/docs/using-together-with-vercels-ai-sdk" badges={["vercel-ai-sdk", "typescript"]} />

  <GuideCard title="Using Together with Mastra" description="Integrate Together AI models with the Mastra framework for building AI-powered features." href="/docs/using-together-with-mastra" badges={["mastra-ai", "typescript"]} />

  <GuideCard title="Logprobs" description="Understanding and using log probabilities in language models." href="/docs/logprobs" badges={["chat"]} />

  <GuideCard title="Next.js Chat Quickstart" description="Spin up a production-ready chatbot using Together + Next.js." href="/docs/nextjs-chat-quickstart" badges={["chat", "typescript"]} />

  <GuideCard title="Quickstart How to Do OCR" description="Build optical character recognition applications with AI." href="/docs/quickstart-how-to-do-ocr" badges={["vision", "typescript"]} />

  <GuideCard title="How to Use Cline" description="Get started with Cline for AI-powered development." href="/docs/how-to-use-cline" badges={["CLI", "Terminal"]} />

  <GuideCard title="Videos" description="Generate high-quality videos from text and image prompts." href="/docs/videos-overview" badges={["video", "python", "typescript"]} />

  <GuideCard title="Mixture of Agents" description="Combine multiple agents for enhanced problem-solving capabilities." href="/docs/mixture-of-agents" badges={["async", "ensemble", "python"]} />
</GridGuides>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
