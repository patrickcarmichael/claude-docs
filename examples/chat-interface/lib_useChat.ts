/**
 * useChat Hook - Custom React Hook for chat logic
 *
 * This file should be placed at: app/hooks/useChat.ts
 *
 * Manages:
 * - Message state and history
 * - Streaming responses
 * - Error handling
 * - Configuration (model, temperature, etc.)
 */

import { useState, useCallback } from 'react';

export interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: number;
}

export interface ChatConfig {
  model: string;
  temperature: number;
  maxTokens: number;
  systemPrompt: string;
}

export interface UseChatReturn {
  messages: Message[];
  isLoading: boolean;
  error: string | null;
  config: ChatConfig;
  sendMessage: (content: string) => Promise<void>;
  setConfig: (config: Partial<ChatConfig>) => void;
  clearMessages: () => void;
  deleteMessage: (id: string) => void;
}

export function useChat(initialConfig?: Partial<ChatConfig>): UseChatReturn {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const [config, setConfigState] = useState<ChatConfig>({
    model: process.env.NEXT_PUBLIC_DEFAULT_MODEL || 'claude-3-5-sonnet-20241022',
    temperature: parseFloat(process.env.NEXT_PUBLIC_DEFAULT_TEMPERATURE || '0.7'),
    maxTokens: parseInt(process.env.NEXT_PUBLIC_MAX_TOKENS || '2000'),
    systemPrompt: 'You are a helpful AI assistant.',
    ...initialConfig,
  });

  const setConfig = useCallback((newConfig: Partial<ChatConfig>) => {
    setConfigState((prev) => ({ ...prev, ...newConfig }));
  }, []);

  const sendMessage = useCallback(
    async (content: string) => {
      if (!content.trim()) return;

      // Add user message
      const userMessage: Message = {
        id: `user-${Date.now()}`,
        role: 'user',
        content,
        timestamp: Date.now(),
      };

      setMessages((prev) => [...prev, userMessage]);
      setIsLoading(true);
      setError(null);

      try {
        // Create request
        const response = await fetch('/api/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            messages: messages.map((m) => ({
              role: m.role,
              content: m.content,
            })),
            ...config,
          }),
        });

        if (!response.ok) {
          throw new Error(`API error: ${response.statusText}`);
        }

        // Handle streaming response
        let assistantMessage = '';
        const assistantId = `assistant-${Date.now()}`;

        const reader = response.body?.getReader();
        if (!reader) {
          throw new Error('Response body is not readable');
        }

        // Create placeholder message
        setMessages((prev) => [
          ...prev,
          {
            id: assistantId,
            role: 'assistant',
            content: '',
            timestamp: Date.now(),
          },
        ]);

        // Process stream
        const decoder = new TextDecoder();
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          const text = decoder.decode(value);
          assistantMessage += text;

          // Update message with streaming content
          setMessages((prev) =>
            prev.map((m) =>
              m.id === assistantId
                ? { ...m, content: assistantMessage }
                : m
            )
          );
        }
      } catch (err) {
        const errorMessage = err instanceof Error ? err.message : 'Unknown error';
        setError(errorMessage);
        console.error('Chat error:', err);
      } finally {
        setIsLoading(false);
      }
    },
    [messages, config]
  );

  const clearMessages = useCallback(() => {
    setMessages([]);
    setError(null);
  }, []);

  const deleteMessage = useCallback((id: string) => {
    setMessages((prev) => prev.filter((m) => m.id !== id));
  }, []);

  return {
    messages,
    isLoading,
    error,
    config,
    sendMessage,
    setConfig,
    clearMessages,
    deleteMessage,
  };
}
