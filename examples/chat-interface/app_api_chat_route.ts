/**
 * Chat API Route - Server-side streaming
 *
 * This file should be placed at: app/api/chat/route.ts
 *
 * Handles POST requests for chat messages and streams responses.
 */

import { Anthropic } from '@anthropic-ai/sdk';

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

export async function POST(request: Request) {
  try {
    const { messages, systemPrompt, model, temperature, maxTokens } = await request.json();

    // Validate input
    if (!messages || !Array.isArray(messages)) {
      return new Response('Invalid messages format', { status: 400 });
    }

    if (messages.length === 0) {
      return new Response('No messages provided', { status: 400 });
    }

    // Create streaming response
    const stream = await anthropic.messages.stream({
      model: model || process.env.NEXT_PUBLIC_DEFAULT_MODEL || 'claude-3-5-sonnet-20241022',
      max_tokens: maxTokens || parseInt(process.env.NEXT_PUBLIC_MAX_TOKENS || '2000'),
      system: systemPrompt || 'You are a helpful AI assistant.',
      messages: messages,
      temperature: temperature !== undefined ? temperature : parseFloat(process.env.NEXT_PUBLIC_DEFAULT_TEMPERATURE || '0.7'),
    });

    // Convert stream to Response
    const response = new Response(
      stream.toReadableStream(),
      {
        headers: {
          'Content-Type': 'text/event-stream',
          'Cache-Control': 'no-cache',
          'Connection': 'keep-alive',
        },
      }
    );

    return response;
  } catch (error) {
    console.error('Chat API error:', error);

    if (error instanceof Anthropic.APIError) {
      return new Response(JSON.stringify({ error: error.message }), {
        status: error.status || 500,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    return new Response(
      JSON.stringify({ error: 'Internal server error' }),
      {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      }
    );
  }
}

export async function OPTIONS(request: Request) {
  return new Response(null, {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}
