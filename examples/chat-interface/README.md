# AI Chat Interface with Next.js and Streaming

A modern web application for conversational AI using:
- **Next.js**: React framework with server-side capabilities
- **Anthropic Claude**: Advanced language model
- **Streaming API**: Real-time response streaming
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Modern styling

## Overview

This is a production-ready chat interface that demonstrates:
- Server-side API routes with Anthropic SDK
- Real-time streaming responses
- Conversation history management
- Custom system prompts
- Error handling and recovery

### Features

- Real-time message streaming
- Conversation memory and history
- Multiple conversation threads
- Custom system prompts per conversation
- Model selection (Claude 3.5 Sonnet, Opus, etc.)
- Temperature and token controls
- Responsive design (mobile, tablet, desktop)
- Dark/light mode support
- Message persistence (localStorage/database)
- File upload support (with RAG integration)

## Architecture

```
Client (Next.js UI)
    ↓ (HTTP/WebSocket)
API Route (/api/chat)
    ↓ (Streaming)
Anthropic Claude API
    ↓ (Stream response)
UI (Real-time display)
```

## Tech Stack

- **Frontend**: Next.js 14, React 18, TypeScript
- **Styling**: Tailwind CSS
- **API Integration**: Anthropic SDK
- **Streaming**: ReadableStream API
- **State Management**: React hooks, SWR/React Query optional
- **Database**: Optional (Supabase, MongoDB, etc.)

## Requirements

### System Requirements
- Node.js 18+ or Bun
- npm, yarn, pnpm, or bun
- Anthropic API key

### Dependencies

```json
{
  "next": "^14.0.0",
  "react": "^18.0.0",
  "react-dom": "^18.0.0",
  "anthropic": "^0.9.0",
  "tailwindcss": "^3.0.0",
  "typescript": "^5.0.0"
}
```

## Installation

### 1. Setup Project

```bash
cd examples/chat-interface
npm install
```

Or with other package managers:
```bash
yarn install  # Yarn
pnpm install # pnpm
bun install  # Bun
```

### 2. Environment Variables

Create a `.env.local` file:

```env
ANTHROPIC_API_KEY=sk-ant-...

# Optional: Default settings
NEXT_PUBLIC_DEFAULT_MODEL=claude-3-5-sonnet-20241022
NEXT_PUBLIC_DEFAULT_TEMPERATURE=0.7
NEXT_PUBLIC_API_BASE_URL=http://localhost:3000
```

### 3. Run Development Server

```bash
npm run dev
# Open http://localhost:3000
```

### 4. Build for Production

```bash
npm run build
npm start
```

## File Structure

```
chat-interface/
├── README.md                      # This file
├── package.json                   # Dependencies
├── next.config.js                 # Next.js configuration
├── tsconfig.json                  # TypeScript configuration
├── .env.local.example            # Environment template
│
├── app/
│   ├── layout.tsx                # Root layout
│   ├── page.tsx                  # Home page / Chat UI
│   ├── api/
│   │   └── chat/
│   │       └── route.ts          # Chat API endpoint (streaming)
│   └── api/
│       └── models/
│           └── route.ts          # Available models endpoint
│
├── components/
│   ├── ChatContainer.tsx         # Main chat component
│   ├── MessageList.tsx           # Message display
│   ├── MessageInput.tsx          # Input field
│   ├── ModelSelector.tsx         # Model selection dropdown
│   ├── SettingsPanel.tsx         # Temperature, tokens, etc.
│   └── Header.tsx                # Top navigation
│
├── hooks/
│   └── useChat.ts                # Custom hook for chat logic
│
├── lib/
│   ├── anthropic.ts              # Anthropic SDK initialization
│   ├── types.ts                  # TypeScript type definitions
│   └── utils.ts                  # Utility functions
│
├── styles/
│   └── globals.css               # Global styles
│
└── public/
    └── (static assets)
```

## Key Components

### 1. API Route (`app/api/chat/route.ts`)

Server-side streaming endpoint:

```typescript
export async function POST(request: Request) {
  const { messages, systemPrompt } = await request.json();

  const stream = await anthropic.messages.stream({
    model: "claude-3-5-sonnet-20241022",
    max_tokens: 1024,
    system: systemPrompt,
    messages: messages,
  });

  return new StreamingTextResponse(stream);
}
```

### 2. Chat Component (`components/ChatContainer.tsx`)

Main chat UI with streaming:

```typescript
export function ChatContainer() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");

  const handleSendMessage = async (text: string) => {
    const newMessage = { role: "user", content: text };
    setMessages(prev => [...prev, newMessage]);

    const stream = await fetch("/api/chat", {
      method: "POST",
      body: JSON.stringify({
        messages: [...messages, newMessage],
      }),
    });

    // Handle streaming response
    const reader = stream.body?.getReader();
    // Process chunks and update UI
  };

  return (
    <div>
      <MessageList messages={messages} />
      <MessageInput onSend={handleSendMessage} />
    </div>
  );
}
```

### 3. Custom Hook (`hooks/useChat.ts`)

Encapsulates chat logic:

```typescript
export function useChat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const sendMessage = async (content: string) => {
    // Handle sending and streaming
  };

  return { messages, isLoading, error, sendMessage };
}
```

## Usage

### Basic Chat

```bash
npm run dev
# Open http://localhost:3000
# Type messages and see real-time responses
```

### Custom Prompts

Edit the system prompt in Settings to customize behavior:
- "You are a helpful assistant"
- "You are a coding expert"
- "You are a creative writer"

### With Database

Integrate with a database to persist conversations:

```typescript
// In app/api/chat/route.ts
const conversation = await db.conversations.create({
  userId: user.id,
  messages: messages,
});
```

## Features & Customization

### Multiple Models

```typescript
const models = [
  "claude-3-5-sonnet-20241022",
  "claude-3-opus-20240229",
  "claude-3-haiku-20240307",
];
```

### Temperature Control

```typescript
const temperature = 0.7; // 0 = deterministic, 1 = creative
```

### System Prompt Customization

```typescript
const systemPrompt = `You are a helpful AI assistant.
When answering:
1. Be clear and concise
2. Provide examples
3. Ask clarifying questions if needed`;
```

### Message Persistence

```typescript
// Save to localStorage
localStorage.setItem("messages", JSON.stringify(messages));

// Or with backend
await fetch("/api/messages", {
  method: "POST",
  body: JSON.stringify({ messages }),
});
```

### File Upload Integration

```typescript
const handleFileUpload = async (file: File) => {
  // Upload to backend/storage
  // Process with RAG if needed
  // Return as context for chat
};
```

## Performance Optimization

### 1. Message Virtualization

For long conversation histories:

```typescript
import { FixedSizeList } from "react-window";

<FixedSizeList
  height={600}
  itemCount={messages.length}
  itemSize={80}
>
  {MessageRow}
</FixedSizeList>
```

### 2. Streaming Optimization

Debounce rapid updates:

```typescript
const debouncedUpdate = useMemo(
  () => debounce((text: string) => setResponse(text), 100),
  []
);
```

### 3. Code Splitting

Lazy load heavy components:

```typescript
const SettingsPanel = lazy(() => import("./SettingsPanel"));
```

## Security

### 1. API Key Protection

Never expose API keys in client code:

```typescript
// ✅ Good: Server-side only
const apiKey = process.env.ANTHROPIC_API_KEY;

// ❌ Bad: Client-side exposure
const apiKey = process.env.NEXT_PUBLIC_API_KEY;
```

### 2. Rate Limiting

Implement rate limiting on API routes:

```typescript
import { Ratelimit } from "@upstash/ratelimit";

const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(10, "1 h"),
});

const { success } = await ratelimit.limit("user-id");
```

### 3. Input Validation

Validate all inputs:

```typescript
const schema = z.object({
  messages: z.array(z.object({
    role: z.enum(["user", "assistant"]),
    content: z.string().max(10000),
  })),
});

const validated = schema.parse(request.body);
```

## Deployment

### Vercel (Recommended)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

### Docker

```dockerfile
FROM node:18
WORKDIR /app
COPY . .
RUN npm install && npm run build
CMD ["npm", "start"]
```

```bash
docker build -t chat-app .
docker run -p 3000:3000 chat-app
```

### Environment Variables in Production

Set in your deployment platform:
- `ANTHROPIC_API_KEY`
- `NEXT_PUBLIC_DEFAULT_MODEL`
- Other configuration

## Advanced Features

### 1. Conversation Threading

Multiple conversations with separate histories:

```typescript
const [conversations, setConversations] = useState<Conversation[]>([]);
const [selectedConversation, setSelectedConversation] = useState<string>();
```

### 2. RAG Integration

Use with RAG backend:

```typescript
const response = await fetch("/api/chat/rag", {
  method: "POST",
  body: JSON.stringify({
    messages,
    documents: relevantDocs,
  }),
});
```

### 3. Voice I/O (Optional)

Add voice input/output:

```typescript
import { useSpeechRecognition } from "react-speech-recognition";

const handleVoiceInput = () => {
  // Record and transcribe audio
  sendMessage(transcribedText);
};
```

## Troubleshooting

### "API Key not found"
```bash
# Check .env.local
cat .env.local

# Should contain: ANTHROPIC_API_KEY=sk-ant-...
```

### Streaming stops unexpectedly
Check network tab for errors. May need error boundary:

```typescript
<ErrorBoundary fallback={<ErrorMessage />}>
  <ChatContainer />
</ErrorBoundary>
```

### Performance issues with long conversations
Implement message pagination or archiving:

```typescript
const [visibleMessages, setVisibleMessages] = useState(messages.slice(-50));
```

## Next Steps

1. **Add Database**: Store conversations persistently
2. **User Authentication**: Add NextAuth for user sessions
3. **RAG Integration**: Connect to RAG backend for contextual responses
4. **Analytics**: Track usage, response quality, costs
5. **Customizations**: Create domain-specific chat experiences
6. **Mobile App**: Wrap in React Native or Flutter

## Related Examples

- [RAG Application](../rag-app/) - Backend for knowledge-based chat
- [Multi-Agent System](../multi-agent/) - Complex reasoning workflows
- [Claude Code Automation](../claude-code-automation/) - Automate deployment

## Resources

- Next.js Documentation: https://nextjs.org/docs
- Anthropic API Reference: https://docs.anthropic.com/
- Streaming Guide: https://docs.anthropic.com/guides/streaming
- Vercel Deployment: https://vercel.com/docs

---

*A complete, production-ready chat interface demonstrating streaming, real-time interactions, and modern web development practices.*
