<p align="center">
  <strong style="font-size: 2em;">🔷 RAYS DeckForge</strong>
</p>

<p align="center">
  <em>Local-first AI presentation generation engine — part of the RAYS ecosystem</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-Apache%202.0-blue?style=flat" alt="Apache2.0" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=flat" alt="Platform" />
  <img src="https://img.shields.io/badge/Default_LLM-Ollama-green?style=flat" alt="Ollama" />
</p>

---

# RAYS DeckForge

**RAYS DeckForge** is a local-first, self-hosted AI presentation generation engine. It generates professional presentations from prompts or uploaded documents, with full PPTX and PDF export capabilities.

### ✨ Key Principles

- **Local-first** — No cloud dependencies, no forced subscriptions
- **Ollama-native** — Default to local LLM inference, zero API keys required
- **Self-hosted** — Full control over your data and models
- **Enterprise-ready** — Deploy internally for your team
- **Extensible** — Custom templates, themes, and providers

---

## 🎛 Features

- **AI Slide Generation** — Generate complete presentations from prompts or documents
- **Custom Templates & Themes** — Create unlimited designs with HTML/Tailwind CSS
- **AI Template Generation** — Create templates from existing PowerPoint documents
- **Multi-Provider Support** — Ollama (default), OpenAI, Gemini, Anthropic, Azure, custom endpoints
- **Export** — PowerPoint (PPTX) and PDF with professional formatting
- **Built-In MCP Server** — Generate presentations over Model Context Protocol
- **Presentation Memory** — Local Mem0-based context system
- **Image Generation** — DALL-E 3, Gemini Flash, Pexels, Pixabay, ComfyUI, Open WebUI
- **Rich Media** — Icons, charts, and custom graphics
- **Electron Desktop App** — Native desktop application (Windows, macOS, Linux)
- **API Service** — RESTful API for programmatic presentation generation

---

## ⚡ Quick Start

### Prerequisites

- **Python 3.11** + [uv](https://docs.astral.sh/uv/)
- **Node.js** (LTS) + npm
- **Ollama** (recommended) — [ollama.com](https://ollama.com)

### 1. Install Dependencies

```bash
# Backend
cd servers/fastapi && uv sync

# Frontend
cd servers/nextjs && npm install
```

### 2. Configure (Optional)

The default `.env` is pre-configured for Ollama with `llama3.1:latest`. Ensure Ollama is running:

```bash
ollama pull llama3.1:latest
ollama serve
```

### 3. Start Development Servers

```bash
chmod +x start-dev.sh
./start-dev.sh
```

Or start manually:

```bash
# Terminal 1: Backend
cd servers/fastapi
uv run uvicorn server:app --host 0.0.0.0 --port 8000 --reload

# Terminal 2: Frontend
cd servers/nextjs
NEXT_PUBLIC_FAST_API=http://localhost:8000 npm run dev
```

Open **http://localhost:3000** in your browser.

---

## 🖥 Desktop App (Electron)

Run RAYS DeckForge as a native desktop application:

```bash
cd electron
npm run setup:env   # First time only
npm run dev         # Start development
```

Build distributable:
```bash
npm run build:all
npm run dist
```

---

## ⚙️ Configuration

All configuration is via environment variables in `.env`:

### LLM Provider

| Variable | Description | Default |
|----------|-------------|---------|
| `LLM` | Provider: `ollama`, `openai`, `google`, `vertex`, `azure`, `anthropic`, `custom` | `ollama` |
| `OLLAMA_URL` | Ollama HTTP API URL | `http://localhost:11434` |
| `OLLAMA_MODEL` | Ollama model name | `llama3.1:latest` |
| `OPENAI_API_KEY` | OpenAI API key (if `LLM=openai`) | — |
| `GOOGLE_API_KEY` | Google API key (if `LLM=google`) | — |
| `ANTHROPIC_API_KEY` | Anthropic API key (if `LLM=anthropic`) | — |
| `CUSTOM_LLM_URL` | OpenAI-compatible endpoint (if `LLM=custom`) | — |

### Image Generation

| Variable | Description |
|----------|-------------|
| `IMAGE_PROVIDER` | `pexels`, `pixabay`, `gemini_flash`, `dall-e-3`, `gpt-image-1.5`, `comfyui`, `open_webui` |
| `DISABLE_IMAGE_GENERATION` | Set to `true` to skip image generation |

### System

| Variable | Description | Default |
|----------|-------------|---------|
| `DISABLE_AUTH` | Disable login requirement | `true` |
| `DATABASE_URL` | SQLAlchemy database URL | SQLite (auto) |
| `DISABLE_ANONYMOUS_TRACKING` | Disable all telemetry | `true` |

---

## 🔌 API

Generate presentations programmatically:

```bash
curl -X POST http://localhost:8000/api/v1/ppt/presentation/generate \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Introduction to Machine Learning",
    "n_slides": 5,
    "language": "English",
    "template": "general",
    "export_as": "pptx"
  }'
```

**Response:**
```json
{
  "presentation_id": "d3000f96-...",
  "path": "/app_data/d3000f96-.../Introduction_to_Machine_Learning.pptx",
  "edit_path": "/presentation?id=d3000f96-..."
}
```

Full API docs available at **http://localhost:8000/docs** when the backend is running.

---

## 🏗 Architecture

```
RAYS_DECK/
├── servers/
│   ├── fastapi/          # Python backend (presentation engine, LLM orchestration)
│   └── nextjs/           # React frontend (dashboard, editor, templates)
├── electron/             # Desktop app shell
├── presentation-export/  # PPTX/PDF export runtime
├── scripts/              # Utility scripts
└── start-dev.sh          # Local development launcher
```

### Stack

- **Backend:** FastAPI + SQLModel + Alembic
- **Frontend:** Next.js 14 + Redux Toolkit + Tailwind CSS
- **Desktop:** Electron + Puppeteer
- **LLM:** Multi-provider (Ollama, OpenAI, Google, Anthropic, Azure, Custom)
- **Memory:** Mem0 OSS (local Qdrant + SQLite)
- **Export:** Puppeteer-based HTML→PPTX/PDF pipeline

---

## 📄 License

Apache 2.0 — See [LICENSE](./LICENSE)

---

<p align="center">
  <strong>RAYS DeckForge</strong> — Part of the RAYS Ecosystem
</p>
