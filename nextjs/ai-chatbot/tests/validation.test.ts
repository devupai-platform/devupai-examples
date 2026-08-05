import { describe, it, expect } from 'vitest';
import { validateRequest } from '../lib/validation';
import { CONFIG } from '../lib/config';

describe('validateRequest', () => {
  it('should accept a valid request', () => {
    const result = validateRequest({
      messages: [{ role: 'user', content: 'Hello' }],
      model: CONFIG.DEFAULT_MODEL,
    });
    expect(result.error).toBeUndefined();
    expect(result.status).toBeUndefined();
  });

  it('should reject non-object body', () => {
    const result = validateRequest(null);
    expect(result.error).toBe('Invalid JSON body');
    expect(result.status).toBe(400);
  });

  it('should reject missing messages array', () => {
    const result = validateRequest({});
    expect(result.error).toBe('Messages must be an array');
    expect(result.status).toBe(400);
  });

  it('should reject empty messages array', () => {
    const result = validateRequest({ messages: [] });
    expect(result.error).toBe('Messages array cannot be empty');
    expect(result.status).toBe(422);
  });

  it('should reject exceeding max message count', () => {
    const messages = Array(CONFIG.MAX_MESSAGE_COUNT + 1).fill({ role: 'user', content: 'test' });
    const result = validateRequest({ messages });
    expect(result.error).toBe('Message count exceeds limit');
    expect(result.status).toBe(422);
  });

  it('should reject unsupported roles', () => {
    const result = validateRequest({ messages: [{ role: 'admin', content: 'test' }] });
    expect(result.error).toBe('Unsupported role: admin');
    expect(result.status).toBe(422);
  });

  it('should reject overly large single message content', () => {
    const result = validateRequest({
      messages: [{ role: 'user', content: 'A'.repeat(CONFIG.MAX_MESSAGE_LENGTH + 1) }]
    });
    expect(result.error).toBe('Individual message exceeds length limit');
    expect(result.status).toBe(422);
  });

  it('should reject total payload exceeding limit', () => {
    const content = 'A'.repeat(CONFIG.MAX_MESSAGE_LENGTH);
    const messages = Array(Math.ceil(CONFIG.MAX_PAYLOAD_SIZE / CONFIG.MAX_MESSAGE_LENGTH) + 1).fill({ role: 'user', content });
    const result = validateRequest({ messages });
    expect(result.error).toBe('Total payload too large');
    expect(result.status).toBe(413);
  });

  it('should reject unsupported models', () => {
    const result = validateRequest({
      messages: [{ role: 'user', content: 'test' }],
      model: 'unknown-model-123'
    });
    expect(result.error).toBe('Unsupported model identifier');
    expect(result.status).toBe(422);
  });
});
