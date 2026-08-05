<p align="center">
  <a href="https://devupai.com">
    <img
      src="https://devupai.com/image/devu.png"
      alt="DEVUP AI"
      width="130"
    />
  </a>
</p>

<h1 align="center">Contributing to DEVUP AI Examples</h1>

<p align="center">
  <strong>Help us build reliable, secure, and runnable examples for the DEVUP AI ecosystem.</strong>
</p>

<p align="center">
  Clean code · No secrets · Automated tests · Reproducible builds
</p>

---

## Welcome

Contributions to **DEVUP AI Examples** are welcome.

This repository contains practical starter projects and integration examples for:

- DEVUP AI APIs
- Official SDKs
- Next.js and Node.js applications
- AI agents and automation workflows
- Cloud GPU and CPU infrastructure

Every contribution should be easy to understand, independently runnable, secure by default, and validated through automated checks.

---

## Before You Start

Before creating a new example:

1. Review the existing repository structure.
2. Check that a similar example does not already exist.
3. Use `npm` as the package manager for JavaScript and TypeScript projects.
4. Never include real API keys, credentials, tokens, or private data.
5. Keep each example focused on one clear use case.

For large changes, open an issue first to describe the proposed example and its purpose.

---

## Repository Structure

Place new examples in the appropriate directory:

```text
devupai-examples/
├── nextjs/
│   └── <example-name>/
├── node/
│   └── <example-name>/
├── python/
│   └── <example-name>/
└── compute/
    └── <example-name>/
```

Use lowercase, descriptive, hyphenated folder names:

```text
ai-chatbot
streaming-chat
embeddings-rag
audio-transcription
gpu-pytorch-training
```

Avoid vague names such as:

```text
test
demo
example-1
new-project
```

---

## Required Files

Every example must include the files necessary to run and understand it.

### JavaScript and TypeScript examples

```text
<example-name>/
├── README.md
├── package.json
├── source files
├── tests/
├── .env.example
└── required configuration files
```

### Python examples

```text
<example-name>/
├── README.md
├── pyproject.toml or requirements.txt
├── source files
├── tests/
└── .env.example
```

Add a `Dockerfile` only when containerization is relevant to the example.

Do not commit generated files such as:

```text
node_modules/
.next/
dist/
coverage/
.env
.env.local
*.log
*.tgz
*.zip
```

---

## README Requirements

Each example must include its own `README.md` with the following sections:

- Overview
- What the example demonstrates
- Features
- Architecture
- Requirements
- Installation
- Environment configuration
- Local development
- Validation commands
- Project structure
- Security notes
- Expected behavior
- Known limitations
- Troubleshooting
- DEVUP AI resources

The instructions must be complete enough for a developer to clone the repository and run the example without reconstructing missing steps.

---

## Environment Variables

Use environment variables for all credentials and sensitive configuration.

The approved API-key variable is:

```env
DEVUP_API_KEY=sk-devup-your-api-key
```

Use this exact placeholder in `.env.example`.

Never commit:

```env
DEVUP_API_KEY=sk-devup-real-secret
```

Never expose API keys through:

```text
NEXT_PUBLIC_*
client-side JavaScript
browser bundles
logs
screenshots
test fixtures
API responses
```

API keys must remain server-side.

---

## Security Requirements

Every contribution must follow these rules:

- Validate all untrusted input.
- Use a server-controlled model allowlist when models are selected by the client.
- Set reasonable payload and message limits.
- Return sanitized error responses.
- Do not expose stack traces or internal filesystem paths.
- Mock external network requests in tests.
- Do not call the live DEVUP AI API in CI.
- Do not include customer data in examples.
- Do not store prompts or responses unless the example explicitly requires persistence and documents it clearly.

Security issues should be reported privately to:

```text
support@devupai.com
```

Do not disclose vulnerabilities through a public issue.

---

## Testing Requirements

Every example must include meaningful automated tests.

For JavaScript and TypeScript examples, use:

```text
Vitest
```

Tests should cover, where applicable:

- Request validation
- Invalid input
- Missing environment variables
- Model allowlist enforcement
- Payload limits
- Safe error handling
- Streaming behavior
- Provider integration boundaries

All external API calls must be mocked.

Tests must be deterministic and must not depend on:

- A real DEVUP AI API key
- Live network access
- External service availability
- Local machine state

Do not add empty tests or meaningless snapshots only to increase the test count.

---

## Validation Commands

Before opening a pull request, run the full validation pipeline from the repository root:

```bash
npm ci
npm run check
```

The `check` command runs:

```text
lint → typecheck → test → build
```

All steps must pass before submission.

You may also run them separately:

```bash
npm run lint
npm run typecheck
npm run test
npm run build
```

---

## Code Quality

Contributions should be:

- Clear
- Focused
- Typed where applicable
- Easy to run
- Easy to review
- Free of dead code
- Free of unnecessary dependencies
- Compatible with the repository tooling

Prefer simple, explicit implementations over unnecessary abstraction.

Avoid:

- Unused dependencies
- Duplicate configuration
- Hard-coded secrets
- Deprecated APIs
- Stale model identifiers
- Manually constructed streaming protocols
- Unsupported production claims

---

## Dependency Policy

Use pinned or controlled dependency versions.

Before adding a dependency:

1. Confirm that it is actively maintained.
2. Confirm compatibility with the existing stack.
3. Check its peer dependencies.
4. Avoid duplicate packages that provide the same function.
5. Keep the dependency surface as small as possible.

Do not use these commands to hide compatibility problems:

```bash
npm install --legacy-peer-deps
npm install --force
npm audit fix --force
```

Dependency conflicts must be resolved through compatible package selection.

---

## Pull Request Checklist

Before submitting a pull request, confirm:

- [ ] The example has a clear purpose.
- [ ] The project installs from a clean environment.
- [ ] The example includes a complete README.
- [ ] `.env.example` contains placeholders only.
- [ ] No secrets or credentials are committed.
- [ ] External requests are mocked in tests.
- [ ] Tests pass.
- [ ] Lint passes.
- [ ] TypeScript checks pass.
- [ ] Production build passes.
- [ ] No generated files are committed.
- [ ] No deprecated or stale DEVUP AI values remain.
- [ ] `npm run check` succeeds from the repository root.

---

## Pull Request Expectations

Keep pull requests focused on one feature or example.

A pull request should include:

- A clear title
- A concise description
- The problem or use case addressed
- The new files or behavior introduced
- Validation results
- Screenshots only when they add meaningful value
- Any known limitations

Avoid mixing unrelated refactors with a new example.

---

## Commit Messages

Use clear, descriptive commit messages.

Examples:

```text
feat: add Node.js streaming example
feat: add GPU PyTorch training starter
fix: correct chatbot request validation
docs: improve embeddings example setup
test: add provider streaming coverage
```

---

## Review Criteria

A contribution may be rejected when it:

- Contains secrets
- Does not run from a clean installation
- Calls live APIs during tests
- Uses deprecated dependencies
- Includes incomplete files
- Lacks documentation
- Introduces unsupported claims
- Breaks existing examples
- Fails repository validation

---

## Resources

- [DEVUP AI Platform](https://devupai.com)
- [Documentation](https://docs.devupai.com)
- [Model Catalog](https://devupai.com/models)
- [Dashboard](https://devupai.com/dashboard)
- [Node.js SDK](https://www.npmjs.com/package/devupai)
- [System Status](https://status.devupai.com)
- [Security Policy](./SECURITY.md)

---

<p align="center">
  <strong>Thank you for helping improve the DEVUP AI developer ecosystem.</strong>
</p>
