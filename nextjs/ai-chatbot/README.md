<p align="center">
  <a href="https://devupai.com">
    <img src="https://devupai.com/image/devu.png" alt="DEVUP AI" width="160" />
  </a>
</p>

<h1 align="center">DEVUP AI Next.js Chatbot</h1>

<p align="center">
  <strong>A production-grade AI chatbot starter built with Next.js, Vercel AI SDK, and DEVUP AI.</strong>
</p>

<p align="center">
  Streaming responses · Server-side security · Model allowlist · Responsive UI
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Next.js-16.3.0-black?style=flat-square" alt="Next.js 16.3.0" />
  <img src="https://img.shields.io/badge/React-19.2.8-149ECA?style=flat-square" alt="React 19.2.8" />
  <img src="https://img.shields.io/badge/DEVUP_AI_SDK-3.0.0-7C3AED?style=flat-square" alt="DEVUP AI SDK 3.0.0" />
  <img src="https://img.shields.io/badge/TypeScript-Strict-3178C6?style=flat-square" alt="TypeScript Strict" />
</p>

---

## Overview

This starter demonstrates how to build a secure, streaming AI chat application using:

- **Next.js App Router**
- **DEVUP AI SDK V3**
- **Vercel AI SDK**
- **React and TypeScript**
- **Server-side API-key handling**

It is designed as a clean foundation for AI assistants, internal copilots, support bots, and other conversational AI applications.

---

## Features

| Capability               | Description                                                                   |
| ------------------------ | ----------------------------------------------------------------------------- |
| **Streaming responses**  | Assistant output is streamed progressively using `streamText`.                |
| **DEVUP AI integration** | Uses `createDevupAI` from the official `devupai/ai` provider.                 |
| **Model allowlist**      | The server accepts only explicitly approved model identifiers.                |
| **Request validation**   | Validates JSON, roles, message count, message length, and total payload size. |
| **Secure API keys**      | `DEVUP_API_KEY` is read only inside the server route.                         |
| **Responsive interface** | Optimized for desktop and mobile screens.                                     |
| **Markdown rendering**   | Supports formatted text and readable code blocks.                             |
| **Generation controls**  | Includes send, stop, clear conversation, and copy response actions.           |
| **Safe error handling**  | Returns controlled errors without exposing secrets or internal stack traces.  |
| **Dark and light modes** | Automatically supports the user’s preferred appearance.                       |

---

## Architecture

```text
Browser
  │
  │ useChat()
  ▼
Next.js API Route
  │
  ├── Request validation
  ├── Model allowlist
  ├── Server-side API key
  └── DEVUP AI provider
          │
          ▼
   DEVUP AI Inference API
```

The API key never reaches the browser.

---

## Technology Stack

```text
Next.js                 16.3.0
React                   19.2.8
DEVUP AI SDK            3.0.0
Vercel AI SDK           6.0.242
@ai-sdk/react           3.0.244
TypeScript              Strict mode
Testing                 Vitest
```

Default model:

```text
deepseek-ai/DeepSeek-V4-Pro
```

---

## Requirements

- Node.js `20.9.0` or newer
- npm `10` or newer
- A DEVUP AI account
- A DEVUP AI API key

Create an API key from the [DEVUP AI Dashboard](https://devupai.com/dashboard/api-keys).

---

## Quick Start

### 1. Install dependencies

From the repository root:

```bash
npm install
```

Or directly from the starter directory:

```bash
cd nextjs/ai-chatbot
npm install
```

### 2. Create the environment file

Windows PowerShell:

```powershell
Copy-Item .env.example .env.local
```

macOS or Linux:

```bash
cp .env.example .env.local
```

### 3. Configure your API key

Open `.env.local`:

```env
DEVUP_API_KEY=sk-devup-your-api-key
```

Replace the placeholder with your real DEVUP AI API key.

### 4. Start development

```bash
npm run dev
```

Open:

```text
http://localhost:3000
```

---

## Available Commands

```bash
npm run dev
```

Starts the local development server.

```bash
npm run lint
```

Runs ESLint.

```bash
npm run typecheck
```

Validates TypeScript without generating files.

```bash
npm run test
```

Runs the Vitest test suite.

```bash
npm run build
```

Creates a production Next.js build.

From the repository root:

```bash
npm run check
```

Runs the complete validation pipeline:

```text
lint → typecheck → test → build
```

---

## Security Model

The starter enforces several server-side protections:

- API keys are never exposed through `NEXT_PUBLIC_*`.
- The API key is evaluated inside the request handler.
- Missing server configuration returns a controlled error.
- Arbitrary model identifiers are rejected.
- Message roles are validated.
- Oversized requests are rejected.
- Provider failures return sanitized responses.
- Environment files are excluded from Git.

Never commit:

```text
.env
.env.local
```

Only `.env.example` should remain in source control.

---

## Request Limits

The default validation policy includes:

| Limit                  |                         Value |
| ---------------------- | ----------------------------: |
| Maximum messages       |                            50 |
| Maximum message length |              4,000 characters |
| Maximum total payload  |            150,000 characters |
| Allowed roles          | `system`, `user`, `assistant` |

These limits can be adjusted in:

```text
lib/config.ts
```

Validation logic is located in:

```text
lib/validation.ts
```

---

## Model Configuration

The default model and allowlist are managed in:

```text
lib/config.ts
```

Do not accept unrestricted model identifiers directly from the browser.

Add models only after confirming that they support the chat and streaming capabilities required by this starter.

Browse the current catalog at:

[devupai.com/models](https://devupai.com/models)

---

## Project Structure

```text
nextjs/ai-chatbot/
├── app/
│   ├── api/
│   │   └── chat/
│   │       └── route.ts
│   ├── globals.css
│   ├── layout.tsx
│   └── page.tsx
├── lib/
│   ├── config.ts
│   └── validation.ts
├── tests/
│   ├── integration.test.tsx
│   ├── provider.test.ts
│   ├── route.test.ts
│   └── validation.test.ts
├── .env.example
├── next.config.ts
├── package.json
├── tsconfig.json
└── vitest.config.ts
```

---

## Production Build

Validate the application before deployment:

```bash
npm run check
```

Create the production build:

```bash
npm run build
```

Start it locally:

```bash
npm run start
```

Configure `DEVUP_API_KEY` as a server-side environment variable in the selected hosting environment.

---

## Troubleshooting

### Missing API key

Confirm that `.env.local` contains:

```env
DEVUP_API_KEY=sk-devup-your-api-key
```

Restart the development server after changing environment variables.

### Unsupported model

The selected model must exist in the server-controlled allowlist inside:

```text
lib/config.ts
```

### Build or dependency issue

Run a clean installation from the repository root:

```bash
npm ci
npm run check
```

### Service availability

Check the live platform status:

[status.devupai.com](https://status.devupai.com)

---

## Resources

- [DEVUP AI Platform](https://devupai.com)
- [Documentation](https://docs.devupai.com)
- [Model Catalog](https://devupai.com/models)
- [Dashboard](https://devupai.com/dashboard)
- [API Keys](https://devupai.com/dashboard/api-keys)
- [Node.js SDK](https://www.npmjs.com/package/devupai)
- [System Status](https://status.devupai.com)
- [Support](mailto:support@devupai.com)

---

<p align="center">
  <strong>Built with DEVUP AI — AI infrastructure for modern applications.</strong>
</p>
