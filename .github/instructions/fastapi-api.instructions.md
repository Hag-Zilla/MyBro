---
applyTo: "src/api/**/*.py,src/routes/**/*.py,app/api/**/*.py"
---

## Purpose

Guide Copilot output for FastAPI modules with pragmatic, production-oriented defaults.

## Scope

Applies to FastAPI API code in `src/api/`, `src/routes/`, and `app/`.

## Guidelines

### Pydantic and Validation

- Prefer Pydantic v2 `BaseModel` for request and response payloads.
- Use explicit type hints for model fields and endpoint signatures.
- Prefer `Field()` constraints for OpenAPI clarity and input quality.
- Add `example` or `examples` where it improves API discoverability.

### Endpoints and Routing

- Prefer one domain per `APIRouter()` instead of a monolithic main module.
- Set explicit `status_code` when behavior is known.
- Add concise docstrings for route handlers, especially for non-trivial logic.
- Use `HTTPException` and shared exception handlers for consistent API errors.

### Testing

- Prefer `pytest` with `TestClient` for endpoint validation.
- Cover happy path, invalid input, and at least one edge case.
- Use fixtures for reusable client setup and dependency overrides.

### Observability

- Prefer structured logging for request lifecycle events.
- Add request count and latency metrics with Prometheus instrumentation when relevant.
- Include endpoint context in exception logs.

### Security and Performance

- Configure CORS explicitly and avoid permissive defaults in production.
- Prefer dependency-injected auth (`Depends`) for protected endpoints.
- Use `async def` for I/O-bound handlers.
- Consider rate limiting and caching for public or high-traffic endpoints.

## Examples

```python
from fastapi import APIRouter, status

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", status_code=status.HTTP_200_OK)
async def health() -> dict[str, str]:
    """Return service health status."""
    return {"status": "ok"}
```
