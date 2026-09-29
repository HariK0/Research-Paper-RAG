# Architecture

The repository is a monorepo with separate `backend/` and `frontend/` applications. The FastAPI service exposes versioned HTTP endpoints under `/api/v1`. PostgreSQL is the relational data store, while ChromaDB is the planned vector database. The root Docker Compose configuration provides the local development services and named persistent volumes.

BM25 lexical retrieval and BGE embeddings are planned components. Retrieval, ingestion, PDF processing, embedding generation, and model calls are not implemented in this scaffold.
