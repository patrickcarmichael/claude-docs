# Production Deployment Best Practices

> Deploy AI applications to production safely and efficiently using modern hosting platforms with security, monitoring, and scaling strategies

## Overview

This guide covers production deployment of AI applications built with Claude, focusing on:

- Security hardening and secret management
- Monitoring, logging, and observability
- Performance optimization and scaling
- Cost management and resource allocation
- Disaster recovery and reliability

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│              Client Applications                         │
│         (Web, Mobile, CLI, API Consumers)               │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│           Edge/CDN Layer (Cloudflare/Vercel)            │
│        (Caching, DDoS Protection, Rate Limiting)       │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│          Application Layer (Vercel/AWS/GCP)            │
│    ┌──────────────┬──────────────┬──────────────┐      │
│    │ Next.js/API  │ Background   │ Scheduled    │      │
│    │ Servers      │ Jobs         │ Tasks        │      │
│    └──────────────┴──────────────┴──────────────┘      │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│          Data Layer (Databases & Services)             │
│    ┌──────────────┬──────────────┬──────────────┐      │
│    │ Vector DB    │ Primary DB   │ Cache        │      │
│    │ (Pinecone)   │ (PostgreSQL) │ (Redis)      │      │
│    └──────────────┴──────────────┴──────────────┘      │
└─────────────────────────────────────────────────────────┘
```

## Part 1: Vercel Deployment

### Step 1: Prepare Your Application

#### 1.1 Project Structure

```
my-app/
├── app/
│   ├── api/
│   │   ├── chat/
│   │   ├── documents/
│   │   └── health/
│   ├── components/
│   ├── layout.tsx
│   └── page.tsx
├── lib/
│   ├── langchain.ts
│   ├── rag-chain.ts
│   └── monitoring.ts
├── public/
├── .env.local
├── .env.production
├── vercel.json
├── tsconfig.json
├── package.json
└── next.config.js
```

#### 1.2 Environment Configuration

Create `vercel.json`:

```json
{
  "version": 2,
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "env": {
    "ANTHROPIC_API_KEY": "@anthropic_api_key",
    "PINECONE_API_KEY": "@pinecone_api_key",
    "PINECONE_INDEX_NAME": "@pinecone_index_name",
    "DATABASE_URL": "@database_url"
  },
  "functions": {
    "app/api/**/*.ts": {
      "maxDuration": 300,
      "memory": 1024
    }
  },
  "regions": ["us-east-1", "eu-west-1"],
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        },
        {
          "key": "X-XSS-Protection",
          "value": "1; mode=block"
        }
      ]
    }
  ]
}
```

#### 1.3 Next.js Configuration

Update `next.config.js`:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Enable SWR for incremental static regeneration
  swrDraft: true,

  // Optimize images
  images: {
    formats: ['image/avif', 'image/webp'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
  },

  // Enable compression
  compress: true,

  // Configure headers
  headers: async () => {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'Strict-Transport-Security',
            value: 'max-age=31536000; includeSubDomains',
          },
          {
            key: 'X-DNS-Prefetch-Control',
            value: 'on',
          },
        ],
      },
    ];
  },

  // Rewrite API routes for security
  rewrites: async () => {
    return {
      beforeFiles: [
        {
          source: '/api/v1/:path*',
          destination: '/api/:path*',
        },
      ],
    };
  },
};

export default nextConfig;
```

### Step 2: Security Hardening

#### 2.1 API Route Security

Create `app/lib/security.ts`:

```typescript
import { NextRequest } from "next/server";

export class SecurityManager {
  // Rate limiting
  private rateLimitMap = new Map<string, number[]>();
  private readonly MAX_REQUESTS = 100;
  private readonly WINDOW_MS = 15 * 60 * 1000; // 15 minutes

  public checkRateLimit(identifier: string): boolean {
    const now = Date.now();
    const requests = this.rateLimitMap.get(identifier) || [];

    // Remove old requests outside window
    const validRequests = requests.filter(
      (timestamp) => now - timestamp < this.WINDOW_MS
    );

    if (validRequests.length >= this.MAX_REQUESTS) {
      return false;
    }

    validRequests.push(now);
    this.rateLimitMap.set(identifier, validRequests);
    return true;
  }

  // Input validation
  public validateInput(input: unknown, maxLength: number = 10000): boolean {
    if (typeof input !== "string") return false;
    if (input.length === 0 || input.length > maxLength) return false;
    return true;
  }

  // CORS validation
  public validateOrigin(request: NextRequest): boolean {
    const origin = request.headers.get("origin");
    const allowedOrigins = (
      process.env.ALLOWED_ORIGINS || "http://localhost:3000"
    ).split(",");

    return allowedOrigins.includes(origin || "");
  }

  // Authentication
  public validateApiKey(apiKey: string): boolean {
    const validKeys = process.env.VALID_API_KEYS?.split(",") || [];
    return validKeys.includes(apiKey);
  }

  // Sanitize output
  public sanitizeOutput(data: string): string {
    return data
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#x27;")
      .replace(/\//g, "&#x2F;");
  }
}

export const securityManager = new SecurityManager();
```

#### 2.2 Protected API Route

Create `app/api/chat/route.ts`:

```typescript
import { NextRequest, NextResponse } from "next/server";
import { securityManager } from "@/app/lib/security";
import { createRAGChain } from "@/app/lib/rag-chain";
import { logRequest } from "@/app/lib/monitoring";

export async function POST(request: NextRequest) {
  try {
    // Validate origin
    if (!securityManager.validateOrigin(request)) {
      return NextResponse.json(
        { error: "Origin not allowed" },
        { status: 403 }
      );
    }

    // Get client identifier for rate limiting
    const clientIp =
      request.headers.get("x-forwarded-for") ||
      request.headers.get("x-real-ip") ||
      "unknown";

    // Check rate limit
    if (!securityManager.checkRateLimit(clientIp)) {
      return NextResponse.json(
        { error: "Rate limit exceeded" },
        { status: 429 }
      );
    }

    // Parse and validate input
    const { message } = await request.json();

    if (!securityManager.validateInput(message)) {
      return NextResponse.json(
        { error: "Invalid input" },
        { status: 400 }
      );
    }

    // Log request
    await logRequest({
      endpoint: "/api/chat",
      clientIp,
      messageLength: message.length,
      timestamp: new Date(),
    });

    // Process request
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
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}
```

### Step 3: Deploy to Vercel

#### 3.1 Install and Configure

```bash
# Install Vercel CLI
npm i -g vercel

# Link project to Vercel
vercel link

# Add environment variables
vercel env add ANTHROPIC_API_KEY
vercel env add PINECONE_API_KEY
vercel env add PINECONE_INDEX_NAME
vercel env add DATABASE_URL
```

#### 3.2 Deploy

```bash
# Deploy to production
vercel --prod

# View deployment
vercel inspect

# Check logs
vercel logs
```

## Part 2: Cloudflare Deployment

### Step 1: Cloudflare Workers Setup

Create `wrangler.toml`:

```toml
name = "ai-app"
type = "javascript"
account_id = "your-account-id"
workers_dev = true
route = "api.example.com/*"
zone_id = "your-zone-id"

[env.production]
route = "api.example.com/*"
vars = { ENVIRONMENT = "production" }

[[env.production.secrets]]
name = "ANTHROPIC_API_KEY"

[build]
command = "npm run build"
cwd = "./workers"

[build.upload]
format = "modules"
main = "./dist/index.js"
```

### Step 2: Cloudflare Workers Script

Create `workers/src/index.ts`:

```typescript
interface Env {
  ANTHROPIC_API_KEY: string;
  PINECONE_API_KEY: string;
  RATE_LIMIT_BUCKET: DurableObject;
}

async function handleRequest(request: Request, env: Env): Promise<Response> {
  // CORS headers
  if (request.method === "OPTIONS") {
    return new Response(null, {
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
      },
    });
  }

  // Route to appropriate handler
  const url = new URL(request.url);

  if (url.pathname === "/api/chat" && request.method === "POST") {
    return handleChat(request, env);
  }

  if (url.pathname === "/api/health" && request.method === "GET") {
    return handleHealth();
  }

  return new Response(JSON.stringify({ error: "Not found" }), {
    status: 404,
    headers: { "Content-Type": "application/json" },
  });
}

async function handleChat(request: Request, env: Env): Promise<Response> {
  try {
    const { message } = await request.json();

    // Validate input
    if (!message || typeof message !== "string") {
      return new Response(JSON.stringify({ error: "Invalid input" }), {
        status: 400,
        headers: { "Content-Type": "application/json" },
      });
    }

    // Call Claude API
    const response = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "x-api-key": env.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
      },
      body: JSON.stringify({
        model: "claude-3-sonnet-20240229",
        max_tokens: 1024,
        messages: [
          {
            role: "user",
            content: message,
          },
        ],
      }),
    });

    const data = await response.json();

    return new Response(JSON.stringify(data), {
      headers: { "Content-Type": "application/json" },
    });
  } catch (error) {
    console.error("Error:", error);
    return new Response(JSON.stringify({ error: "Internal error" }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }
}

function handleHealth(): Response {
  return new Response(JSON.stringify({ status: "healthy" }), {
    headers: { "Content-Type": "application/json" },
  });
}

export default {
  fetch: handleRequest,
};
```

### Step 3: Deploy to Cloudflare

```bash
# Install Wrangler
npm install -g wrangler

# Authenticate
wrangler login

# Deploy
wrangler deploy

# View logs
wrangler tail
```

## Part 3: Monitoring & Observability

### Step 1: Structured Logging

Create `app/lib/monitoring.ts`:

```typescript
import { Anthropic } from "@anthropic-sdk";

interface LogEntry {
  timestamp: Date;
  level: "info" | "warn" | "error";
  message: string;
  metadata?: Record<string, any>;
  endpoint?: string;
  duration?: number;
  statusCode?: number;
}

class MonitoringService {
  private logs: LogEntry[] = [];

  public log(entry: LogEntry) {
    this.logs.push(entry);

    // Send to external service in production
    if (process.env.NODE_ENV === "production") {
      this.sendToExternalService(entry);
    }

    // Console log in development
    if (process.env.NODE_ENV === "development") {
      console.log(
        `[${entry.level.toUpperCase()}] ${entry.timestamp.toISOString()} - ${entry.message}`,
        entry.metadata || ""
      );
    }
  }

  private async sendToExternalService(entry: LogEntry) {
    // Send to DataDog, New Relic, etc.
    try {
      await fetch(process.env.LOG_ENDPOINT || "", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(entry),
      });
    } catch (error) {
      console.error("Failed to send log:", error);
    }
  }

  public metrics() {
    return {
      totalLogs: this.logs.length,
      errors: this.logs.filter((l) => l.level === "error").length,
      warnings: this.logs.filter((l) => l.level === "warn").length,
      averageResponseTime:
        this.logs
          .filter((l) => l.duration)
          .reduce((sum, l) => sum + (l.duration || 0), 0) / this.logs.length,
    };
  }
}

export const monitoring = new MonitoringService();

// Logging helper
export async function logRequest(data: any) {
  monitoring.log({
    timestamp: new Date(),
    level: "info",
    message: "API Request",
    metadata: data,
    endpoint: data.endpoint,
  });
}

// Error logging helper
export async function logError(error: Error, context: any) {
  monitoring.log({
    timestamp: new Date(),
    level: "error",
    message: error.message,
    metadata: {
      stack: error.stack,
      context,
    },
  });
}
```

### Step 2: Performance Monitoring

Create `app/lib/performance.ts`:

```typescript
export class PerformanceMonitor {
  private timers = new Map<string, number>();

  start(label: string) {
    this.timers.set(label, performance.now());
  }

  end(label: string): number {
    const startTime = this.timers.get(label);
    if (!startTime) {
      console.warn(`No start time found for ${label}`);
      return 0;
    }

    const duration = performance.now() - startTime;
    this.timers.delete(label);

    return duration;
  }

  // Measure async operations
  async measure<T>(label: string, fn: () => Promise<T>): Promise<T> {
    this.start(label);
    try {
      return await fn();
    } finally {
      const duration = this.end(label);
      console.log(`${label}: ${duration.toFixed(2)}ms`);
    }
  }
}

export const performanceMonitor = new PerformanceMonitor();
```

### Step 3: Health Check Endpoint

Create `app/api/health/route.ts`:

```typescript
import { NextResponse } from "next/server";

export async function GET() {
  const health = {
    status: "healthy",
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    memory: process.memoryUsage(),
    checks: {
      database: await checkDatabase(),
      anthropic: await checkAnthropic(),
      pinecone: await checkPinecone(),
    },
  };

  const allHealthy = Object.values(health.checks).every((c) => c.status === "ok");

  return NextResponse.json(health, {
    status: allHealthy ? 200 : 503,
  });
}

async function checkDatabase() {
  try {
    // Add database health check
    return { status: "ok", latency: 10 };
  } catch (error) {
    return { status: "error", error: String(error) };
  }
}

async function checkAnthropic() {
  try {
    // Verify API key is valid
    const response = await fetch("https://api.anthropic.com/v1/models", {
      headers: {
        "x-api-key": process.env.ANTHROPIC_API_KEY || "",
      },
    });

    return { status: response.ok ? "ok" : "error" };
  } catch (error) {
    return { status: "error", error: String(error) };
  }
}

async function checkPinecone() {
  try {
    // Verify Pinecone connection
    return { status: "ok" };
  } catch (error) {
    return { status: "error", error: String(error) };
  }
}
```

## Part 4: Cost Optimization

### Step 1: Token Usage Tracking

Create `app/lib/cost-tracking.ts`:

```typescript
interface TokenUsage {
  model: string;
  inputTokens: number;
  outputTokens: number;
  cost: number;
}

export class CostTracker {
  // Pricing per 1M tokens (as of 2024)
  private pricing = {
    "claude-3-opus": { input: 15, output: 75 },
    "claude-3-sonnet": { input: 3, output: 15 },
    "claude-3-haiku": { input: 0.25, output: 1.25 },
  };

  calculateCost(
    model: string,
    inputTokens: number,
    outputTokens: number
  ): number {
    const modelPricing =
      this.pricing[model as keyof typeof this.pricing] || null;

    if (!modelPricing) {
      console.warn(`Unknown model: ${model}`);
      return 0;
    }

    const inputCost = (inputTokens / 1000000) * modelPricing.input;
    const outputCost = (outputTokens / 1000000) * modelPricing.output;

    return inputCost + outputCost;
  }

  trackUsage(usage: TokenUsage) {
    // Log to cost tracking system
    console.log(`Token usage: ${JSON.stringify(usage)}`);

    // Send to external service
    if (process.env.COST_TRACKING_ENDPOINT) {
      fetch(process.env.COST_TRACKING_ENDPOINT, {
        method: "POST",
        body: JSON.stringify(usage),
      }).catch((error) => console.error("Cost tracking error:", error));
    }
  }
}

export const costTracker = new CostTracker();
```

### Step 2: Caching Strategy

Create `app/lib/caching.ts`:

```typescript
import Redis from "ioredis";

export class CacheManager {
  private redis: Redis;

  constructor() {
    this.redis = new Redis(process.env.REDIS_URL || "redis://localhost");
  }

  async get<T>(key: string): Promise<T | null> {
    const data = await this.redis.get(key);
    return data ? JSON.parse(data) : null;
  }

  async set<T>(key: string, value: T, ttl: number = 3600) {
    await this.redis.setex(key, ttl, JSON.stringify(value));
  }

  async invalidate(pattern: string) {
    const keys = await this.redis.keys(pattern);
    if (keys.length > 0) {
      await this.redis.del(...keys);
    }
  }

  async getCachedResponse<T>(
    key: string,
    fn: () => Promise<T>,
    ttl: number = 3600
  ): Promise<T> {
    // Try to get from cache
    const cached = await this.get<T>(key);
    if (cached) {
      return cached;
    }

    // Execute function and cache result
    const result = await fn();
    await this.set(key, result, ttl);

    return result;
  }
}

export const cacheManager = new CacheManager();
```

## Part 5: Scaling Strategies

### Step 1: Load Testing

Create `load-test.js`:

```javascript
import http from "k6/http";
import { check, sleep } from "k6";

export let options = {
  stages: [
    { duration: "2m", target: 100 },
    { duration: "5m", target: 100 },
    { duration: "2m", target: 200 },
    { duration: "5m", target: 200 },
    { duration: "2m", target: 0 },
  ],
};

export default function () {
  let res = http.post("https://api.example.com/api/chat", JSON.stringify({
    message: "What is the capital of France?",
  }), {
    headers: { "Content-Type": "application/json" },
  });

  check(res, {
    "status is 200": (r) => r.status === 200,
    "response time < 5s": (r) => r.timings.duration < 5000,
  });

  sleep(1);
}
```

Run load test:

```bash
k6 run load-test.js
```

### Step 2: Auto-Scaling Configuration

For Vercel (automatic), ensure `vercel.json` specifies:

```json
{
  "functions": {
    "app/api/**/*.ts": {
      "maxDuration": 300,
      "memory": 1024
    }
  },
  "regions": ["us-east-1", "eu-west-1", "ap-southeast-1"]
}
```

## Part 6: Disaster Recovery

### Step 1: Backup Strategy

Create `scripts/backup.ts`:

```typescript
import fs from "fs";
import path from "path";

async function backupVectorDatabase() {
  // Export Pinecone vectors
  const vectors = await pineconeIndex.query({
    topK: 10000,
  });

  const backup = {
    timestamp: new Date().toISOString(),
    vectors,
    metadata: {
      count: vectors.length,
      version: "1.0",
    },
  };

  fs.writeFileSync(
    path.join("backups", `vectors-${Date.now()}.json`),
    JSON.stringify(backup, null, 2)
  );

  console.log("Backup completed");
}

// Schedule daily backups
setInterval(backupVectorDatabase, 24 * 60 * 60 * 1000);
```

### Step 2: Error Recovery

Create `app/lib/recovery.ts`:

```typescript
export class RecoveryManager {
  private maxRetries = 3;
  private retryDelay = 1000;

  async retryWithExponentialBackoff<T>(
    fn: () => Promise<T>,
    context: string
  ): Promise<T> {
    for (let attempt = 1; attempt <= this.maxRetries; attempt++) {
      try {
        return await fn();
      } catch (error) {
        if (attempt === this.maxRetries) {
          throw error;
        }

        const delay = this.retryDelay * Math.pow(2, attempt - 1);
        console.log(
          `${context} failed (attempt ${attempt}/${this.maxRetries}). Retrying in ${delay}ms...`
        );

        await new Promise((resolve) => setTimeout(resolve, delay));
      }
    }

    throw new Error("Should not reach here");
  }
}

export const recoveryManager = new RecoveryManager();
```

## Monitoring Dashboard Setup

### Using DataDog

```bash
npm install @anthropic-sdk/monitoring-datadog
```

Create `monitoring/datadog-setup.ts`:

```typescript
import { StatsD } from "node-dogstatsd";

const statsd = new StatsD({
  host: "127.0.0.1",
  port: 8125,
  tags: ["service:ai-app", "env:production"],
});

export function recordMetric(metric: string, value: number) {
  statsd.gauge(metric, value);
}

export function recordAPICall(endpoint: string, duration: number) {
  recordMetric(`api.${endpoint}.duration`, duration);
}
```

## Checklist for Production

- [ ] Environment variables configured securely
- [ ] Rate limiting implemented
- [ ] CORS policy defined
- [ ] API key validation in place
- [ ] Error handling and logging
- [ ] Health check endpoint
- [ ] Monitoring and alerting
- [ ] Backup strategy
- [ ] Disaster recovery plan
- [ ] Load testing completed
- [ ] Security audit done
- [ ] Documentation updated
- [ ] Team trained on operations

## Related Resources

- [Vercel Documentation](../../web-frameworks/vercel/)
- [Cloudflare Workers](../../infrastructure/cloudflare/)
- [Next.js Deployment](../../web-frameworks/nextjs/)
- [RAG Application Guide](./rag-app-complete.md)
- [Multi-Agent Workflows](./multi-agent-workflow.md)

## Troubleshooting

### Issue: High API Costs
- Implement caching layer
- Use appropriate model sizes (Haiku for simple tasks)
- Optimize prompt engineering
- Monitor token usage

### Issue: Slow Response Times
- Add CDN caching (Cloudflare)
- Optimize database queries
- Use async processing for long tasks
- Implement request batching

### Issue: Rate Limiting
- Implement queue system (Bull, RabbitMQ)
- Use background jobs for batch processing
- Add API key throttling per user

## Next Steps

1. Choose deployment platform (Vercel/Cloudflare)
2. Set up monitoring and logging
3. Implement security measures
4. Configure auto-scaling
5. Create disaster recovery plan
6. Monitor costs and optimize
7. Set up alerting for production issues
