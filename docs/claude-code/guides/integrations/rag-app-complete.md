# Complete RAG Stack Setup Guide

> Build a production-ready Retrieval-Augmented Generation (RAG) application using LangChain, Pinecone, Anthropic Claude, and Next.js

## Overview

This guide walks you through building a complete RAG application that combines:
- **LangChain** for orchestrating LLM workflows
- **Pinecone** for vector storage and semantic search
- **Anthropic Claude** for intelligent generation
- **Next.js** for the web interface

The resulting application can answer questions based on your custom knowledge base with citations and context awareness.

## Prerequisites

Before starting, ensure you have:
- Node.js 18+ and npm/yarn
- Python 3.10+ (for backend services)
- API keys for:
  - [Anthropic Claude](https://docs.anthropic.com/en/docs/getting-started-with-the-api)
  - [Pinecone vector database](https://docs.pinecone.io/guides/getting-started/quickstart)
- Basic knowledge of [LangChain fundamentals](../../features/mcp.md#langchain-integration)

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Next.js Frontend                      │
│          (React UI + API Routes)                         │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│              LangChain Orchestration                     │
│    ┌──────────────────┬───────────────────┐             │
│    │ Document Loader  │ Text Splitter     │             │
│    │ & Embeddings     │                   │             │
│    └──────────┬───────┴────────────┬──────┘             │
│               │                    │                     │
│    ┌──────────▼──────────┐  ┌──────▼────────┐          │
│    │ Pinecone Vector DB  │  │ Claude LLM    │          │
│    │ (Semantic Search)   │  │ (Generation)  │          │
│    └─────────────────────┘  └───────────────┘          │
└─────────────────────────────────────────────────────────┘
```

## Step 1: Environment Setup

### 1.1 Create Project Structure

```bash
# Create main project directory
mkdir rag-app && cd rag-app

# Create subdirectories
mkdir -p app/api/chat app/components app/lib
mkdir -p scripts data
mkdir -p public
```

### 1.2 Initialize Next.js Project

```bash
# Create Next.js app
npx create-next-app@latest . --typescript --tailwind --eslint

# Install required dependencies
npm install \
  langchain \
  @langchain/community \
  @langchain/anthropic \
  @pinecone-database/pinecone \
  axios \
  dotenv
```

### 1.3 Set Up Environment Variables

Create `.env.local`:

```bash
# Anthropic API
ANTHROPIC_API_KEY=sk-ant-...

# Pinecone Configuration
PINECONE_API_KEY=pc-...
PINECONE_ENVIRONMENT=us-east-1-aws
PINECONE_INDEX_NAME=rag-documents

# Optional: For document processing
NEXT_PUBLIC_API_BASE=http://localhost:3000
```

## Step 2: Configure Vector Database

### 2.1 Initialize Pinecone Index

```python
# scripts/setup_pinecone.py
from pinecone import Pinecone, ServerlessSpec

# Initialize Pinecone
pc = Pinecone(api_key="your-api-key")

# Create index if not exists
index_name = "rag-documents"
dimension = 1536  # OpenAI/Anthropic embedding dimension

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

print(f"Index '{index_name}' is ready")
```

Run setup:

```bash
pip install pinecone-client
python scripts/setup_pinecone.py
```

### 2.2 Prepare Sample Documents

Create `data/sample_documents.json`:

```json
{
  "documents": [
    {
      "id": "doc-001",
      "title": "Claude API Overview",
      "content": "Claude is Anthropic's advanced AI assistant. The Claude API provides access to various model versions including Claude 3 Opus, Sonnet, and Haiku. You can use Claude for text analysis, content generation, and reasoning tasks.",
      "metadata": {
        "source": "anthropic-docs",
        "category": "ai-models"
      }
    },
    {
      "id": "doc-002",
      "title": "Building RAG Systems",
      "content": "RAG (Retrieval-Augmented Generation) systems combine document retrieval with language models. They work by: 1) Converting documents to embeddings, 2) Storing embeddings in a vector database, 3) Retrieving relevant documents based on user queries, 4) Using an LLM to generate answers based on retrieved context.",
      "metadata": {
        "source": "technical-guide",
        "category": "ai-systems"
      }
    }
  ]
}
```

## Step 3: Create LangChain Integration

### 3.1 Document Loader and Embedding Pipeline

Create `app/lib/langchain.ts`:

```typescript
import { Pinecone } from "@pinecone-database/pinecone";
import { PineconeStore } from "@langchain/pinecone";
import { OpenAIEmbeddings } from "@langchain/openai";
import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";
import { Document } from "langchain/document";

// Initialize Pinecone
const pinecone = new Pinecone({
  apiKey: process.env.PINECONE_API_KEY,
});

// Get index
export const pineconeIndex = pinecone.Index(
  process.env.PINECONE_INDEX_NAME || "rag-documents"
);

// Initialize embeddings (using OpenAI for this example)
// Alternative: Use Anthropic embeddings or other providers
export const embeddings = new OpenAIEmbeddings({
  apiKey: process.env.OPENAI_API_KEY,
  modelName: "text-embedding-3-small",
});

// Initialize vector store
export async function initializeVectorStore() {
  return await PineconeStore.fromExistingIndex(embeddings, {
    pineconeIndex,
  });
}

// Split documents into chunks
export const textSplitter = new RecursiveCharacterTextSplitter({
  chunkSize: 1000,
  chunkOverlap: 200,
});

// Add documents to vector store
export async function addDocumentsToVectorStore(
  documents: Array<{ id: string; title: string; content: string; metadata?: Record<string, any> }>
) {
  const vectorStore = await initializeVectorStore();

  // Convert to LangChain Document format
  const docs = documents.map(
    (doc) =>
      new Document({
        pageContent: doc.content,
        metadata: {
          ...doc.metadata,
          source: doc.title,
          id: doc.id,
        },
      })
  );

  // Split documents
  const splits = await textSplitter.splitDocuments(docs);

  // Add to Pinecone
  await PineconeStore.fromDocuments(splits, embeddings, {
    pineconeIndex,
  });

  return splits.length;
}

// Search for similar documents
export async function searchDocuments(query: string, topK: number = 3) {
  const vectorStore = await initializeVectorStore();
  const results = await vectorStore.similaritySearch(query, topK);

  return results.map((doc) => ({
    content: doc.pageContent,
    metadata: doc.metadata,
    similarity: doc.metadata.similarity || 0,
  }));
}
```

### 3.2 Create RAG Chain with Claude

Create `app/lib/rag-chain.ts`:

```typescript
import { ChatAnthropic } from "@langchain/anthropic";
import {
  RunnablePassthrough,
  RunnableParallel,
  RunnableLambda,
} from "@langchain/core/runnables";
import {
  ChatPromptTemplate,
  SystemMessagePromptTemplate,
  HumanMessagePromptTemplate,
} from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";
import { initializeVectorStore } from "./langchain";

// Initialize Claude
const model = new ChatAnthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
  modelName: "claude-3-sonnet-20240229",
  temperature: 0.7,
});

// Format documents for context
function formatDocs(docs: any[]) {
  return docs
    .map(
      (doc, index) =>
        `Document ${index + 1}:\n${doc.pageContent}\nSource: ${doc.metadata.source}`
    )
    .join("\n\n---\n\n");
}

// Create RAG chain
export async function createRAGChain() {
  const vectorStore = await initializeVectorStore();
  const retriever = vectorStore.asRetriever({ k: 3 });

  // System prompt for RAG
  const systemPrompt = `You are a helpful assistant that answers questions based on provided documents.

Guidelines:
- Answer questions based primarily on the provided document context
- If the answer is not in the documents, say "I don't have that information in my knowledge base"
- Always cite which document(s) you're referencing
- Be concise and clear in your explanations
- If multiple documents are relevant, synthesize information from all of them`;

  const promptTemplate = ChatPromptTemplate.fromMessages([
    SystemMessagePromptTemplate.fromTemplate(systemPrompt),
    HumanMessagePromptTemplate.fromTemplate(
      `Context from documents:\n{context}\n\nQuestion: {question}`
    ),
  ]);

  // Create chain with retrieval
  const ragChain = RunnablePassthrough.assign({
    context: new RunnableLambda({
      func: async (input: { question: string }) => {
        const docs = await retriever.invoke(input.question);
        return formatDocs(docs);
      },
    }),
  })
    .pipe(promptTemplate)
    .pipe(model)
    .pipe(new StringOutputParser());

  return ragChain;
}

// Stream response helper
export async function streamRAGResponse(question: string) {
  const chain = await createRAGChain();

  // For streaming, use the chain with streaming enabled
  const stream = await chain.stream({ question });
  return stream;
}
```

## Step 4: Build Next.js API Routes

### 4.1 Chat Endpoint

Create `app/api/chat/route.ts`:

```typescript
import { NextRequest, NextResponse } from "next/server";
import { createRAGChain } from "@/app/lib/rag-chain";

export async function POST(request: NextRequest) {
  try {
    const { message } = await request.json();

    if (!message) {
      return NextResponse.json(
        { error: "Message is required" },
        { status: 400 }
      );
    }

    const ragChain = await createRAGChain();
    const response = await ragChain.invoke({ question: message });

    return NextResponse.json({
      success: true,
      answer: response,
      timestamp: new Date().toISOString(),
    });
  } catch (error) {
    console.error("Chat error:", error);
    return NextResponse.json(
      { error: "Failed to process message" },
      { status: 500 }
    );
  }
}
```

### 4.2 Document Upload Endpoint

Create `app/api/documents/upload/route.ts`:

```typescript
import { NextRequest, NextResponse } from "next/server";
import { addDocumentsToVectorStore } from "@/app/lib/langchain";

export async function POST(request: NextRequest) {
  try {
    const documents = await request.json();

    // Validate documents format
    if (!Array.isArray(documents)) {
      return NextResponse.json(
        { error: "Documents must be an array" },
        { status: 400 }
      );
    }

    // Add documents to vector store
    const count = await addDocumentsToVectorStore(documents);

    return NextResponse.json({
      success: true,
      message: `Added ${count} document chunks to knowledge base`,
      chunksAdded: count,
    });
  } catch (error) {
    console.error("Upload error:", error);
    return NextResponse.json(
      { error: "Failed to upload documents" },
      { status: 500 }
    );
  }
}
```

### 4.3 Search Endpoint

Create `app/api/search/route.ts`:

```typescript
import { NextRequest, NextResponse } from "next/server";
import { searchDocuments } from "@/app/lib/langchain";

export async function GET(request: NextRequest) {
  try {
    const query = request.nextUrl.searchParams.get("q");
    const topK = parseInt(request.nextUrl.searchParams.get("topK") || "5");

    if (!query) {
      return NextResponse.json(
        { error: "Query parameter 'q' is required" },
        { status: 400 }
      );
    }

    const results = await searchDocuments(query, topK);

    return NextResponse.json({
      success: true,
      query,
      results,
      count: results.length,
    });
  } catch (error) {
    console.error("Search error:", error);
    return NextResponse.json(
      { error: "Failed to search documents" },
      { status: 500 }
    );
  }
}
```

## Step 5: Build Frontend Components

### 5.1 Chat Interface Component

Create `app/components/ChatInterface.tsx`:

```typescript
"use client";

import { useState, useRef, useEffect } from "react";
import type { ReactNode } from "react";

interface Message {
  id: string;
  role: "user" | "assistant";
  content: string;
  timestamp: Date;
}

export default function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!input.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      role: "user",
      content: input,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });

      if (!response.ok) {
        throw new Error("Failed to get response");
      }

      const data = await response.json();

      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: "assistant",
        content: data.answer,
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (err) {
      setError(err instanceof Error ? err.message : "An error occurred");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-full bg-gradient-to-b from-slate-900 to-slate-800 rounded-lg">
      {/* Header */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 p-4 text-white">
        <h1 className="text-2xl font-bold">RAG Assistant</h1>
        <p className="text-sm opacity-90">Ask questions about your documents</p>
      </div>

      {/* Messages Container */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.length === 0 && (
          <div className="text-center text-gray-400 mt-8">
            <p className="text-lg mb-2">Welcome to RAG Assistant</p>
            <p className="text-sm">
              Start by asking a question about your knowledge base
            </p>
          </div>
        )}

        {messages.map((message) => (
          <div
            key={message.id}
            className={`flex ${
              message.role === "user" ? "justify-end" : "justify-start"
            }`}
          >
            <div
              className={`max-w-xs lg:max-w-md xl:max-w-lg px-4 py-2 rounded-lg ${
                message.role === "user"
                  ? "bg-blue-600 text-white rounded-br-none"
                  : "bg-gray-700 text-gray-100 rounded-bl-none"
              }`}
            >
              <p className="text-sm">{message.content}</p>
              <p className="text-xs opacity-70 mt-1">
                {message.timestamp.toLocaleTimeString()}
              </p>
            </div>
          </div>
        ))}

        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-gray-700 text-gray-100 px-4 py-2 rounded-lg rounded-bl-none">
              <div className="flex space-x-2">
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-100"></div>
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-200"></div>
              </div>
            </div>
          </div>
        )}

        {error && (
          <div className="bg-red-900 text-red-100 px-4 py-2 rounded-lg text-sm">
            Error: {error}
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Input Form */}
      <div className="border-t border-gray-600 p-4 bg-slate-800">
        <form onSubmit={handleSendMessage} className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask a question..."
            disabled={isLoading}
            className="flex-1 bg-gray-700 text-white rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50"
          />
          <button
            type="submit"
            disabled={isLoading || !input.trim()}
            className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 text-white px-6 py-2 rounded-lg font-medium transition"
          >
            {isLoading ? "Thinking..." : "Send"}
          </button>
        </form>
      </div>
    </div>
  );
}
```

### 5.2 Document Upload Component

Create `app/components/DocumentUpload.tsx`:

```typescript
"use client";

import { useState } from "react";

interface DocumentData {
  id: string;
  title: string;
  content: string;
  metadata?: Record<string, any>;
}

export default function DocumentUpload() {
  const [isLoading, setIsLoading] = useState(false);
  const [message, setMessage] = useState<{
    type: "success" | "error" | null;
    text: string;
  }>({ type: null, text: "" });

  const handleUploadJSON = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setIsLoading(true);
    try {
      const content = await file.text();
      const data = JSON.parse(content);

      // Validate document format
      const documents = data.documents || data;
      if (!Array.isArray(documents)) {
        throw new Error("Invalid format: expected array of documents");
      }

      const response = await fetch("/api/documents/upload", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(documents),
      });

      const result = await response.json();

      if (response.ok) {
        setMessage({
          type: "success",
          text: result.message || "Documents uploaded successfully",
        });
      } else {
        throw new Error(result.error || "Upload failed");
      }
    } catch (err) {
      setMessage({
        type: "error",
        text: err instanceof Error ? err.message : "Upload failed",
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-lg shadow p-6 max-w-md">
      <h2 className="text-xl font-bold mb-4">Upload Documents</h2>

      <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center cursor-pointer hover:border-blue-500 transition">
        <input
          type="file"
          accept=".json"
          onChange={handleUploadJSON}
          disabled={isLoading}
          className="hidden"
          id="fileInput"
        />
        <label htmlFor="fileInput" className="cursor-pointer">
          <p className="text-lg font-medium text-gray-700">
            Drop JSON file here
          </p>
          <p className="text-sm text-gray-500">or click to browse</p>
        </label>
      </div>

      {message.type && (
        <div
          className={`mt-4 p-3 rounded-lg text-sm ${
            message.type === "success"
              ? "bg-green-100 text-green-800"
              : "bg-red-100 text-red-800"
          }`}
        >
          {message.text}
        </div>
      )}
    </div>
  );
}
```

## Step 6: Main Page

Create `app/page.tsx`:

```typescript
import ChatInterface from "./components/ChatInterface";
import DocumentUpload from "./components/DocumentUpload";

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-950 p-4">
      <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-4 gap-4">
        {/* Chat Interface */}
        <div className="lg:col-span-3 h-screen max-h-screen">
          <ChatInterface />
        </div>

        {/* Sidebar */}
        <div className="lg:col-span-1">
          <DocumentUpload />
        </div>
      </div>
    </div>
  );
}
```

## Step 7: Deployment & Production

### 7.1 Environment Configuration

For production deployment (see [Production Deployment Guide](./production-deployment.md)):

```bash
# Generate .env.production.local
ANTHROPIC_API_KEY=sk-ant-... (production key)
PINECONE_API_KEY=pc-... (production key)
PINECONE_INDEX_NAME=rag-documents-prod
```

### 7.2 Build and Test

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Visit http://localhost:3000

# Build for production
npm run build

# Test production build
npm start
```

### 7.3 Deploy to Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Set environment variables in Vercel dashboard
```

## Step 8: Optimization Tips

### 8.1 Caching Strategy

Add caching for frequently accessed documents:

```typescript
// app/lib/cache.ts
import NodeCache from "node-cache";

const cache = new NodeCache({ stdTTL: 3600 });

export function getCachedSearch(query: string) {
  return cache.get(`search:${query}`);
}

export function setCachedSearch(query: string, results: any) {
  cache.set(`search:${query}`, results);
}
```

### 8.2 Rate Limiting

Implement rate limiting for API endpoints:

```typescript
// app/lib/rateLimit.ts
import { Ratelimit } from "@upstash/ratelimit";
import { Redis } from "@upstash/redis";

const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(10, "1 h"),
});

export async function checkRateLimit(identifier: string) {
  const { success } = await ratelimit.limit(identifier);
  return success;
}
```

### 8.3 Monitoring

Integrate with monitoring services:

```typescript
// Add to your API routes
import { captureException } from "@sentry/nextjs";

try {
  // API logic
} catch (error) {
  captureException(error);
}
```

## Testing

### Unit Tests

```typescript
// __tests__/rag-chain.test.ts
import { createRAGChain } from "@/app/lib/rag-chain";

describe("RAG Chain", () => {
  it("should create RAG chain successfully", async () => {
    const chain = await createRAGChain();
    expect(chain).toBeDefined();
  });
});
```

## Related Resources

- [LangChain Documentation](../../ai-frameworks/langchain/)
- [Pinecone Vector Database](../../infrastructure/pinecone/)
- [Anthropic Claude API](../../ai-platforms/anthropic/)
- [Next.js Framework](../../web-frameworks/nextjs/)
- [Production Deployment Guide](./production-deployment.md)
- [Multi-Agent Workflows](./multi-agent-workflow.md)

## Troubleshooting

### Issue: Pinecone Connection Failed
- Verify API key is correct in `.env.local`
- Check Pinecone index name matches configuration
- Ensure index is created before adding documents

### Issue: Slow Retrieval
- Increase `chunkOverlap` in text splitter
- Adjust embedding model for better semantic understanding
- Consider implementing caching for frequently accessed queries

### Issue: Poor RAG Response Quality
- Verify documents are well-formatted and contain relevant information
- Adjust system prompt to provide better context
- Increase `topK` parameter in similarity search
- Fine-tune chunk size based on your documents

## Next Steps

1. Load your own documents into the knowledge base
2. Customize the system prompt for your use case
3. Implement monitoring and analytics
4. Deploy to production using [Production Deployment Guide](./production-deployment.md)
5. Build multi-agent workflows for complex tasks using [Multi-Agent Guide](./multi-agent-workflow.md)
