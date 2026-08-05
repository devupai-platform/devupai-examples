'use client';

import { useChat } from '@ai-sdk/react';
import React, { useState, useRef, useEffect, useMemo } from 'react';
import ReactMarkdown from 'react-markdown';
import { CONFIG } from '@/lib/config';
import { DefaultChatTransport } from 'ai';

export default function Chat() {
  const [model, setModel] = useState(CONFIG.DEFAULT_MODEL);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const [input, setInput] = useState('');

  const transport = useMemo(() => new DefaultChatTransport({
    api: '/api/chat',
    body: { model },
  }), [model]);

  const {
    messages,
    status,
    sendMessage,
    stop,
    error,
    setMessages,
  } = useChat({
    transport,
  });

  const isLoading = status === 'streaming' || status === 'submitted';

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setInput(e.target.value);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;
    sendMessage({ text: input });
    setInput('');
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleClear = () => {
    setMessages([]);
  };

  const handleCopy = (text: string) => {
    navigator.clipboard.writeText(text);
  };

  const onSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;
    handleSubmit(e);
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      onSubmit(e as unknown as React.FormEvent);
    }
  };

  return (
    <main className="container">
      <header className="header">
        <h1>DEVUP AI Chatbot</h1>
        <select
          className="model-select"
          value={model}
          onChange={(e) => setModel(e.target.value)}
          disabled={isLoading}
          aria-label="Select Model"
        >
          {CONFIG.ALLOWED_MODELS.map((m) => (
            <option key={m} value={m}>
              {m}
            </option>
          ))}
        </select>
      </header>

      <div className="messages">
        {messages.length === 0 ? (
          <div className="empty-state">
            <h2>Welcome to the DEVUP AI Next.js Starter</h2>
            <p>Start typing a message below to test the streaming API.</p>
          </div>
        ) : (
          messages.map((m) => {
            // eslint-disable-next-line @typescript-eslint/no-explicit-any
            const content = (m as any).content || (m.parts?.filter((p: { type: string; text?: string }) => p.type === 'text').map((p: { type: string; text?: string }) => p.text).join('')) || '';
            return (
            <div key={m.id} className="message">
              <div className="message-role">
                {m.role === 'user' ? 'You' : 'Assistant'}
                {m.role === 'assistant' && (
                  <button
                    type="button"
                    className="button-outline sr-only focus:not-sr-only"
                    onClick={() => handleCopy(content)}
                    style={{ marginLeft: '0.5rem', padding: '0.25rem 0.5rem', fontSize: '0.75rem' }}
                  >
                    Copy
                  </button>
                )}
              </div>
              <div className="message-content">
                <ReactMarkdown>{content}</ReactMarkdown>
              </div>
            </div>
            );
          })
        )}
        {error && (
          <div className="error-state">
            <strong>Error:</strong> {error.message || 'An unexpected error occurred.'}
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {isLoading && (
        <div className="controls">
          <button type="button" className="button button-outline" onClick={stop}>
            Stop generating
          </button>
        </div>
      )}

      {messages.length > 0 && !isLoading && (
        <div className="controls">
          <button type="button" className="button button-outline" onClick={handleClear}>
            Clear conversation
          </button>
        </div>
      )}

      <div className="input-area">
        <form onSubmit={onSubmit} className="input-form">
          <textarea
            className="textarea"
            value={input}
            onChange={handleInputChange}
            onKeyDown={handleKeyDown}
            placeholder="Type a message..."
            disabled={isLoading}
            aria-label="Message input"
            rows={1}
          />
          <button
            type="submit"
            className="button"
            disabled={isLoading || !input.trim()}
          >
            Send
          </button>
        </form>
      </div>
    </main>
  );
}
