import { CONFIG } from './config';

export function validateRequest(body: unknown): { error?: string; status?: number } {
  if (!body || typeof body !== 'object') {
    return { error: 'Invalid JSON body', status: 400 };
  }

  const { messages, model } = body as Record<string, unknown>;

  if (!Array.isArray(messages)) {
    return { error: 'Messages must be an array', status: 400 };
  }

  if (messages.length === 0) {
    return { error: 'Messages array cannot be empty', status: 422 };
  }

  if (messages.length > CONFIG.MAX_MESSAGE_COUNT) {
    return { error: 'Message count exceeds limit', status: 422 };
  }

  let totalSize = 0;
  for (const item of messages) {
    if (!item || typeof item !== 'object') {
      return { error: 'Invalid message structure', status: 400 };
    }
    const msg = item as Record<string, unknown>;

    if (typeof msg.role !== 'string' || !CONFIG.ALLOWED_ROLES.includes(msg.role)) {
      return { error: `Unsupported role: ${msg.role}`, status: 422 };
    }

    const content = msg.content || '';
    if (typeof content !== 'string') {
      return { error: 'Message content must be a string', status: 400 };
    }

    if (content.length > CONFIG.MAX_MESSAGE_LENGTH) {
      return { error: 'Individual message exceeds length limit', status: 422 };
    }

    if (content.trim().length === 0) {
      return { error: 'Message content cannot be empty', status: 422 };
    }

    totalSize += content.length;
  }

  if (totalSize > CONFIG.MAX_PAYLOAD_SIZE) {
    return { error: 'Total payload too large', status: 413 };
  }

  if (model && (typeof model !== 'string' || !CONFIG.ALLOWED_MODELS.includes(model))) {
    return { error: 'Unsupported model identifier', status: 422 };
  }

  return {};
}
