import { describe, it, expect, vi, beforeEach } from 'vitest';
import { POST } from '../app/api/chat/route';

vi.mock('ai', async (importOriginal) => {
  const actual = await importOriginal();
  return {
    ...actual as object,
    streamText: vi.fn(() => ({
      toUIMessageStreamResponse: vi.fn(() => new Response('mock-stream-response', { status: 200 }))
    }))
  };
});

vi.mock('devupai/ai', () => ({
  createDevupAI: vi.fn(() => vi.fn(() => 'mock-model'))
}));

describe('Chat API Route', () => {
  const originalEnv = process.env;

  beforeEach(() => {
    process.env = { ...originalEnv };
  });

  it('should return 500 if API key is missing', async () => {
    delete process.env.DEVUP_API_KEY;
    const req = new Request('http://localhost/api/chat', { method: 'POST', body: JSON.stringify({ messages: [{ role: 'user', content: 'test' }] }) });
    const res = await POST(req);
    expect(res.status).toBe(500);
    const body = await res.json();
    expect(body.error).toContain('Missing API Key');
  });

  it('should return 400 on malformed JSON', async () => {
    process.env.DEVUP_API_KEY = 'test-key';
    const req = new Request('http://localhost/api/chat', { method: 'POST', body: '{ malformed json' });
    const res = await POST(req);
    expect(res.status).toBe(400);
  });

  it('should call streamText and return 200 on valid request', async () => {
    process.env.DEVUP_API_KEY = 'test-key';
    const req = new Request('http://localhost/api/chat', {
      method: 'POST',
      body: JSON.stringify({ messages: [{ role: 'user', content: 'test', parts: [{ type: 'text', text: 'test' }] }] })
    });
    const res = await POST(req);
    expect(res.status).toBe(200);
  });
});
