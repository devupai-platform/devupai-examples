import { describe, it, expect, vi } from 'vitest';
import { streamText } from 'ai';

vi.mock('devupai/ai', () => ({
  createDevupAI: () => {
    const provider = (modelId: string) => ({
      specificationVersion: 'v3',
      provider: 'devupai',
      modelId,
      defaultObjectGenerationMode: 'json',
      doStream: async () => ({
        stream: new ReadableStream({
          start(controller) {
            controller.enqueue({ type: 'text-delta', textDelta: 'Hello from devup', delta: 'Hello from devup' });
            controller.enqueue({
              type: 'finish',
              finishReason: 'stop',
              usage: {
                promptTokens: 10,
                completionTokens: 20,
                inputTokens: { total: 10, noCache: 0, cacheRead: 0, cacheWrite: 0 },
                outputTokens: { total: 20 }
              }
            });
            controller.close();
          },
        }),
        rawCall: { rawPrompt: null, rawSettings: {} },
      }),
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } as any);
    return provider;
  }
}));

import { createDevupAI } from 'devupai/ai';

describe('Provider Contract', () => {
  it('createDevupAI returns a model accepted by streamText and processes streamed response without network request', async () => {
    const devup = createDevupAI({ apiKey: 'test-key' });
    const model = devup('devup-model-v1');

    const result = await streamText({
      model,
      messages: [{ role: 'user', content: 'Say hello' }],
    });

    let fullText = '';
    for await (const chunk of result.textStream) {
      fullText += chunk;
    }

    expect(fullText).toBe('Hello from devup');
  });
});
