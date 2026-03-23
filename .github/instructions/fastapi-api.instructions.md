---
applyTo: "src/api/**/*.py,src/routes/**/*.py,app/**/*.py"
---

## Instructions for FastAPI Code

### Pydantic Models and Validation
- **Pydantic v2**: use `BaseModel` for all request/response bodies.
- **Type hint validation**: int, str, float, list[str], Optional[X], etc. Copilot must generate automatic validation.
- **Field constraints**: document via `Field(..., description="...", min_length=1, max_length=100)` for OpenAPI.
- **Examples**: include `example` or `examples` in `Field()` for Swagger docs.

### Endpoints and Routes
- **Mandatory docstrings**: each route handler must include Google-style docstring with description, parameters, responses.
- **Status codes**: explicitly define `status_code` in `@app.post(..., status_code=201)` etc.
- **Route separation**: group in `APIRouter()` by domain (e.g., `/auth`, `/models`, `/inference`), not everything in main.
- **Error handling**: use `HTTPException(status_code=400, detail="...")` + custom exception handlers for uniformity.

### Testing
- **TestClient pytest**: 
  ```python
  from fastapi.testclient import TestClient
  client = TestClient(app)
  def test_endpoint_success():
      response = client.get("/health")
      assert response.status_code == 200
  ```
- **Coverage**: happy path, invalid input, edge cases, error cases.
- **Fixtures**: use `@pytest.fixture` for client, mock services, databases.

### Observability and Monitoring
- **Middleware logging**: add to trace request/response (time, status, user).
- **Prometheus metrics**: instrument with `prometheus_client` to count requests, measure latency.
- **Errors and exceptions**: log with context (user_id, endpoint), not just the message.

### Security
- **CORS**: explicitly configure `add_middleware(CORSMiddleware, allow_origins=[...])` with whitelist.
- **Auth**: use `Depends()` with OAuth2PasswordBearer or JWT, validate token systematically.
- **Input sanitization**: do not trust user inputs, validate + clean.
- **No secrets in code**: credentials via env vars or Vault, not hardcoded.

### Performance
- **Rate limiting**: add `slowapi` or custom middleware if endpoint is public.
- **Async**: use `async def` for I/O-bound handlers (DB, API calls).
- **Caching**: implement `@lru_cache` or Redis for stable data.

