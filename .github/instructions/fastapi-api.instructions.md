---
applyTo: "src/api/**/*.py,src/routes/**/*.py,app/**/*.py"
---

## Instructions pour code FastAPI

### Modèles Pydantic et validation
- **Pydantic v2**: utiliser `BaseModel` pour tous les request/response bodies.
- **Validation type hints**: int, str, float, list[str], Optional[X], etc. Copilot doit générer validation automatique.
- **Field constraints**: documenter via `Field(..., description="...", min_length=1, max_length=100)` pour OpenAPI.
- **Exemples**: inclure `example` ou `examples` dans `Field()` pour Swagger docs.

### Endpoints et routes
- **Docstrings obligatoires**: chaque route Route handler doit inclure docstring Google-style avec description, paramètres, réponses.
- **Status codes**: définir explicitement `status_code` dans `@app.post(..., status_code=201)` etc.
- **Séparation routes**: grouper dans `APIRouter()` par domaine (ex: `/auth`, `/models`, `/inference`),pas tout dans main.
- **Error handling**: utiliser `HTTPException(status_code=400, detail="...")` + custom exception handlers pour uniformité.

### Tests
- **TestClient pytest**: 
  ```python
  from fastapi.testclient import TestClient
  client = TestClient(app)
  def test_endpoint_success():
      response = client.get("/health")
      assert response.status_code == 200
  ```
- **Couvrir**: happy path, invalid input, edge cases, error cases.
- **Fixtures**: utiliser `@pytest.fixture` pour client, mock services, databases.

### Observabilité et monitoring
- **Middleware logging**: ajouter pour tracer request/response (temps, statut, utilisateur).
- **Prometheus metrics**: instrumenter avec `prometheus_client` pour compter requests, mesurer latence.
- **Errors et exceptions**: logger avec contexte (user_id, endpoint), pas juste le message.

### Sécurité
- **CORS**: configurer explicitement `add_middleware(CORSMiddleware, allow_origins=[...])` avec whitelist.
- **Auth**: utiliser `Depends()` avec OAuth2PasswordBearer ou JWT, valider token systématiquement.
- **Input sanitization**: ne pas faire confiance aux user inputs, valider + nettoyer.
- **No secrets in code**: credentials via env vars ou Vault, pas hardcodés.

### Performance
- **Rate limiting**: ajouter `slowapi` ou custom middleware si endpoint expose publique.
- **Async**: utiliser `async def` pour I/O-bound handlers (DB, API calls).
- **Caching**: implémenter `@lru_cache` ou Redis pour données stables.

