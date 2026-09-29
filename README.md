# Research Paper RAG Assistant

A monorepo scaffold for building a research assistant that will retrieve evidence from a user’s research paper collection. This phase establishes the application shell and local development services.

## Architecture

- **backend/**: Python 3.12 and FastAPI, with configuration loaded from environment variables. Versioned API routes use `/api/v1`.
- **frontend/**: React, TypeScript, and Vite.
- **PostgreSQL**: relational database for future application metadata.
- **ChromaDB**: vector database service for future semantic retrieval.
- **infrastructure/**: local service notes; the Compose definition is at the repository root.
- **docs/**: architecture notes.
- **tests/**: backend API tests.

The planned retrieval approach includes BM25 and BGE embeddings. These are not implemented yet. PDF processing, ingestion, retrieval, LLM integration, and authentication are also out of scope for this scaffold.

## Local development

Requirements: Docker Compose, Python 3.12, and Node.js/npm.

1. Copy `.env.example` to `.env` if `.env` does not already exist. Set a private local `POSTGRES_PASSWORD`; `.env` is ignored by Git.
2. Start the services with `docker compose up --build`. PostgreSQL listens on `localhost:5432`, ChromaDB on `localhost:8001`, FastAPI on `localhost:8000`, and Vite on `localhost:5173`.
3. Open the API docs at <http://localhost:8000/docs> and the frontend at <http://localhost:5173>. The health endpoint is <http://localhost:8000/api/v1/health>.

To start only the data services, use `docker compose up -d db chroma`. Data is persisted in named Compose volumes. See [infrastructure/README.md](infrastructure/README.md) for service details.

### Backend tests

```sh
python -m venv .venv
# Activate .venv, then:
python -m pip install -r backend/requirements-dev.txt
python -m pytest
```

### Frontend build

```sh
cd frontend
npm install
npm run build
```

## Configuration

Root `.env.example` documents Compose settings. `backend/.env.example` documents API settings, and `frontend/.env.example` documents the Vite API URL. Copy an example only when creating a local `.env`; never commit secrets. Compose supplies service URLs within its network, while local processes use localhost URLs.

## Current implementation status

Implemented: monorepo layout, basic FastAPI app and versioned health route, minimal React app, environment-based settings, PostgreSQL and ChromaDB Compose services, and a health endpoint test.

Not implemented: paper upload or parsing, chunking, BM25, BGE embedding generation, indexing, retrieval, answer generation, authentication, or production deployment configuration.

