<p align="center">
  <a href="https://devupai.com">
    <img src="https://devupai.com/image/devu.png" alt="DEVUP AI" width="160" />
  </a>
</p>

<h1 align="center">DEVUP AI — Official Examples</h1>

<p align="center">
  <strong>Production-oriented starter kits and reference implementations for building with DEVUP AI.</strong>
</p>

<p align="center">
  <a href="https://devupai.com">Platform</a> ·
  <a href="https://docs.devupai.com">Documentation</a> ·
  <a href="https://devupai.com/models">Models</a> ·
  <a href="https://devupai.com/dashboard">Dashboard</a> ·
  <a href="https://status.devupai.com">Status</a> ·
  <a href="https://www.npmjs.com/package/devupai">npm</a>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/devupai">
    <img
      src="https://img.shields.io/npm/v/devupai.svg?style=flat-square&label=DEVUP%20AI%20SDK"
      alt="DEVUP AI SDK"
    />
  </a>
  <a href="https://github.com/devupai-platform/devupai-examples/actions/workflows/ci.yml">
    <img
      src="https://github.com/devupai-platform/devupai-examples/actions/workflows/ci.yml/badge.svg?branch=main"
      alt="GitHub Actions CI"
    />
  </a>
  <img
    src="https://img.shields.io/badge/Next.js-16.3.0-black?style=flat-square"
    alt="Next.js 16.3.0"
  />
  <img
    src="https://img.shields.io/badge/TypeScript-Strict-3178C6?style=flat-square"
    alt="TypeScript Strict"
  />
</p>

---

## About the Repository

This repository contains official runnable examples and starter kits for the DEVUP AI platform.

These examples are designed to provide a production-grade foundation for developers to learn from and extend into their own applications.

---

## Available Examples

| Example | Stack | Status |
|---------|-------|--------|
| [Next.js AI Chatbot](./nextjs/ai-chatbot) | Next.js `16.3.0`, React `19.2.8`, `devupai@3.0.0`, AI SDK `6.0.242` | **Available** |

---

## Featured Starter

### Next.js AI Chatbot

The Next.js AI Chatbot is our primary reference implementation for conversational AI applications.

**Highlights:**

- Official provider integration through `createDevupAI` from `devupai/ai`
- Native AI SDK streaming through `streamText`
- Real-time **streaming** responses
- Strict **server-side API-key handling**
- Configurable **model allowlist**
- Server-side **validation** for payload and messages
- Clean **Markdown rendering**
- Comprehensive **Vitest tests**

[Explore the Next.js AI Chatbot →](./nextjs/ai-chatbot)

---

## Requirements

- Node.js 20.9.0 or newer
- npm 10 or newer
- A DEVUP AI API key

---

## Quick Start

To run the Next.js AI Chatbot example locally:

```bash
git clone https://github.com/devupai-platform/devupai-examples.git
cd devupai-examples
npm ci
```

Then navigate to the starter directory:

```bash
cd nextjs/ai-chatbot
```

Create your environment variables file:

**Windows PowerShell:**
```powershell
Copy-Item .env.example .env.local
```

**macOS/Linux:**
```bash
cp .env.example .env.local
```

Open `.env.local` and add your API key:

```env
DEVUP_API_KEY=sk-devup-your-api-key
```

Run the development server:

```bash
npm run dev
```

Open your browser to:
[http://localhost:3000](http://localhost:3000)

---

## Repository Structure

```text
devupai-examples/
├── .github/
│   └── workflows/
│       └── ci.yml
├── nextjs/
│   └── ai-chatbot/
├── CONTRIBUTING.md
├── SECURITY.md
├── package.json
├── package-lock.json
└── README.md
```

---

## Repository Principles

All supported examples in this repository adhere to strict validation and security criteria:

- **Runnable from a clean clone**
- **Secure server-side secret handling**
- **No live API calls during CI tests**
- **Complete per-example documentation**
- **Controlled dependency versions**
- **Meaningful automated tests**

Please report any security issues or vulnerabilities privately. [Review our Security Policy →](./SECURITY.md)

---

## Roadmap

The following examples are planned and are not yet available.

### API and SDK Examples
- Node.js SDK quickstart
- Node.js streaming
- Embeddings and RAG
- Image generation
- Audio transcription
- Video generation
- Native inference

### Python and Agent Examples
- Python OpenAI-compatible quickstart
- Python streaming
- AutoGen multi-agent workflow
- Agent tool calling

### Compute Examples
- GPU PyTorch training
- GPU inference server
- CPU FastAPI service
- Persistent Network Volume workflow
- JupyterLab GPU workflow

---

## Contributing

We welcome contributions to the DEVUP AI examples repository.

[Read the Contributing Guidelines →](./CONTRIBUTING.md)

---

## Resources

| Resource | Link |
|----------|------|
| Platform | [https://devupai.com](https://devupai.com) |
| Documentation | [https://docs.devupai.com](https://docs.devupai.com) |
| Model Catalog | [https://devupai.com/models](https://devupai.com/models) |
| Dashboard | [https://devupai.com/dashboard](https://devupai.com/dashboard) |
| API Keys | [https://devupai.com/dashboard/api-keys](https://devupai.com/dashboard/api-keys) |
| Node.js SDK | [https://www.npmjs.com/package/devupai](https://www.npmjs.com/package/devupai) |
| GitHub Organization | [https://github.com/devupai-platform](https://github.com/devupai-platform) |
| Status | [https://status.devupai.com](https://status.devupai.com) |
| Support | [support@devupai.com](mailto:support@devupai.com) |

---

<p align="center">
  Built in Algeria. Connected to the global AI ecosystem.
</p>

<p align="center">
  <a href="https://devupai.com">Platform</a> ·
  <a href="https://docs.devupai.com">Documentation</a> ·
  <a href="https://devupai.com/models">Models</a> ·
  <a href="https://devupai.com/dashboard">Dashboard</a> ·
  <a href="https://status.devupai.com">Status</a>
</p>
