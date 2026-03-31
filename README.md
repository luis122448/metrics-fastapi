# Metrics FastAPI

REST API for managing project metrics, built with FastAPI and SQLite.

## Stack

- **Python 3.11** + **FastAPI**
- **SQLAlchemy** (ORM)
- **SQLite** (embedded database)
- **Uvicorn** (ASGI server)
- **Docker** + **GitLab CI/CD**

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/api/ready` | Health check (readiness/liveness) |
| GET | `/app/projects` | List all projects |
| GET | `/app/metrics` | List all metrics |
| GET | `/docs` | Swagger documentation |

## Local Setup

```bash
# Bootstrap environment
./dev-install.sh

# Start development server
./dev-init.sh
```

The server starts on `http://localhost:8083`.

## Database

Initialize the SQLite database:

```bash
python scripts/init_db.py
```

## Docker

### Local deploy (with local registry)

```bash
./dev-deploy.sh
```

### Production build

```bash
./build-release.sh <version> <environment> <architecture> <docker_registry> <docker_project>
```

## CI/CD

GitLab pipeline with three stages:

1. **build** - Docker image build and push to Harbor registry
2. **deploy** - Kubernetes rollout restart
3. **notify** - Deployment confirmation

| Branch | Environment | Deploy |
|---|---|---|
| `main` | Production | Automatic |
| `develop` | Development | Manual |

## Environment Variables

Copy `.env.example` to `.env` and fill in the values:

```bash
cp .env.example .env
```
