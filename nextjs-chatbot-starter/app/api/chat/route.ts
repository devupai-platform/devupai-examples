import OpenAI from "openai";
import { NextRequest } from "next/server";

/**
 * DEVUP AI — Next.js Streaming Chat API Route
 *
 * Compatible with the Vercel AI SDK useChat() hook.
 * Streams tokens in real-time using Server-Sent Events.
 */

const client = new OpenAI({
  apiKey: process.env.DEVUPAI_API_KEY,
  baseURL: "https://api.devupai.com/v1",
});

export const runtime = "edge";

export async function POST(req: NextRequest) {
  try {
    const { messages, model = "meta-llama/Llama-3.3-70B-Instruct-Turbo" } =
      await req.json();

    // Validate input
    if (!Array.isArray(messages) || messages.length === 0) {
      return new Response(
        JSON.stringify({ error: "messages array is required" }),
        { status: 400, headers: { "Content-Type": "application/json" } }
      );
    }

    // Create streaming completion
    const stream = await client.chat.completions.create({
      model,
      messages: [
        {
          role: "system",
          content:
            "You are a helpful AI assistant powered by DEVUP AI — Algeria's AI infrastructure platform. Answer clearly and concisely.",
        },
        ...messages,
      ],
      max_tokens: 2048,
      temperature: 0.7,
      stream: true,
    });

    // Stream response as SSE
    const encoder = new TextEncoder();

    const readable = new ReadableStream({
      async start(controller) {
        try {
          for await (const chunk of stream) {
            const content = chunk.choices[0]?.delta?.content ?? "";
            if (content) {
              // Vercel AI SDK data stream format
              controller.enqueue(
                encoder.encode(`0:${JSON.stringify(content)}\n`)
              );
            }

            // Send finish reason
            if (chunk.choices[0]?.finish_reason === "stop") {
              controller.enqueue(encoder.encode(`d:{"finishReason":"stop"}\n`));
            }
          }
        } catch (err) {
          controller.error(err);
        } finally {
          controller.close();
        }
      },
    });

    return new Response(readable, {
      headers: {
        "Content-Type": "text/plain; charset=utf-8",
        "X-Vercel-AI-Data-Stream": "v1",
        "Cache-Control": "no-cache",
        Connection: "keep-alive",
      },
    });
  } catch (error) {
    console.error("[DEVUP AI] Chat error:", error);
    return new Response(
      JSON.stringify({ error: "Failed to process chat request" }),
      { status: 500, headers: { "Content-Type": "application/json" } }
    );
  }
}
