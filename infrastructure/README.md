# Local infrastructure

The root `compose.yaml` defines the local PostgreSQL and ChromaDB services alongside the API and frontend. Start only the data services with:

```sh
docker compose up -d db chroma
```

PostgreSQL is available on `localhost:5432`; ChromaDB is available on `localhost:8001` (container port `8000`). Compose stores both databases in named volumes. Do not place research PDFs, secrets, or vector indexes in source control.
