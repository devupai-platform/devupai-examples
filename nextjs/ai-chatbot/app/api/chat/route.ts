import { streamText, convertToModelMessages } from 'ai';
import { createDevupAI } from 'devupai/ai';
import { validateRequest } from '@/lib/validation';
import { CONFIG } from '@/lib/config';

export async function POST(req: Request) {
  try {
    const apiKey = process.env.DEVUP_API_KEY;
    if (!apiKey) {
      return new Response(JSON.stringify({ error: 'Server configuration error: Missing API Key' }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    let body;
    try {
      body = await req.json();
    } catch {
      return new Response(JSON.stringify({ error: 'Malformed JSON' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const { error, status } = validateRequest(body);
    if (error) {
      return new Response(JSON.stringify({ error }), {
        status,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const devupai = createDevupAI({ apiKey });
    const model = body.model || CONFIG.DEFAULT_MODEL;

    const result = streamText({
      model: devupai(model),
      messages: await convertToModelMessages(body.messages),
    });

    return result.toUIMessageStreamResponse();
  } catch (err: unknown) {
    console.error('API Chat Route Error:', err);
    return new Response(JSON.stringify({ error: 'Upstream provider failure' }), {
      status: 502,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}
