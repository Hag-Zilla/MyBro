## Instructions personnalisées GitHub Copilot — Français

But
: Fournir des suggestions cohérentes avec les conventions du dépôt, accélérer la rédaction de code et aider les contributeurs sur Python, MLOps, déploiement et observabilité.

Contexte du dépôt
- Stack technique: Python, Docker, FastAPI, Kubernetes, Prometheus, Grafana, Loki.
- Public cible: data scientists, ingénieurs MLOps, développeurs backend.

Préférences générales
- Style de code: Respecter PEP 8, noms explicites, fonctions courtes (<= 50 lignes), type hints quand possible. Utiliser un formatteur automatique pour garantir la conformité (préférer `black` + `isort`).
- Docstrings: Toutes les fonctions et classes doivent inclure une docstring conforme à PEP 257; documenter paramètres, valeurs de retour et exceptions. Préférer le style Google ou NumPy.
- Tests: Préférer `pytest`; viser une couverture minimale acceptable (ex: 80% pour modules critiques).
- Logging: Utiliser le module `logging` avec niveaux adaptés; ne pas « print » en production.
- Sécurité: Ne jamais générer ni proposer d'insérer des secrets (clé API, mots de passe). Utiliser des variables d'environnement et des solutions de vault.

Outils recommandés
- Formatage automatique: `black` (configurable via `pyproject.toml`).
- Tri des imports: `isort`.
- Linting: `ruff` ou `flake8` pour détecter violations PEP8 et erreurs courantes.
- Hooks git: utiliser `pre-commit` pour exécuter `black`, `isort` et `ruff/flake8` avant chaque commit.

Exemples de commandes (local)
```bash
python -m pip install --user black isort ruff pre-commit
pre-commit install
black .
isort .
ruff check .
```

Docker et conteneurisation
- Fournir des Dockerfiles légers et reproductibles (multi-stage builds si besoin).
- Exposer uniquement les ports nécessaires; définir `USER` non-root quand possible.
- Inclure instructions pour builder et exécuter localement.

Kubernetes et déploiement
- Préférer des manifests Helm ou kustomize templates minimalistes.
- Toujours proposer requests/limits pour CPU et mémoire.
- Suggérer probes (`readiness`, `liveness`) et stratégies de déploiement (rolling updates).

FastAPI
- Utiliser Pydantic pour la validation des modèles d'entrée/sortie.
- Documenter les routes via OpenAPI (docstrings + types).
- Proposer des patterns pour tests d'API (client TestClient + fixtures).

Observabilité (Prometheus / Grafana / Loki)
- Proposer métriques applicatives pertinentes (latence, erreurs, compteurs).
- Ajouter instrumentation basique (Prometheus client) et exemples de dashboard Grafana.
- Suggérer format de logs structurés (JSON) compatible Loki.

Bonnes pratiques MLOps
- Séparer code de formation et code de service (inférence).
- Fournir exemples de CI pour training et déploiement (ex: GitHub Actions).
- Suggérer validation des modèles (tests unitaires + tests d'intégration de prédiction).

Restrictions et interdits
- Ne pas générer: secrets, clés d'API, mots de passe, ou instructions pour contourner la sécurité.
- Éviter suggestions qui hardcodent des chemins locaux non reproductibles.

Usage opérationnel
- Ce fichier doit rester à la racine `.github/copilot-instructions.md` pour être pris en compte.
- Pour proposer une modification: ouvrir une PR petite et explicite, inclure tests et instructions de validation.

---

**Comment demander à Copilot**

- Donnez un but clair: expliquer l'objectif recherché et les contraintes (compatibilité Python, dépendances, limites de performance).
- Fournissez des exemples d'entrée/sortie si possible (format des données, types attendus).
- Indiquez le niveau de détail souhaité: "code uniquement", "code + explication brève" ou "code + tests".
- Précisez les fichiers ou modules concernés, et si la modification doit être rétrocompatible.

**Format de réponse attendu**

- Fournir une implémentation concise et testable, avec docstrings conformes (PEP 257) et annotations de type.
- Ajouter un petit test `pytest` quand la fonctionnalité est non-triviale.
- Pour les changements d'infrastructure, fournir le manifest complet (`Dockerfile`, `helm` chart snippet) et une brève note d'utilisation.
- Pour les commandes et instructions, utiliser des blocs de code avec le bon langage (bash, Dockerfile, yaml).
- Ne jamais inclure de secrets ou de valeurs sensibles en clair.

**Exemples de prompts efficaces**

- "Écris une fonction `normalize_df(df: pd.DataFrame) -> pd.DataFrame` qui normalise les colonnes numériques. Inclut une docstring style NumPy et un test pytest minimal."
- "Génère un `Dockerfile` multistage pour une app FastAPI (module `app:app`) avec Uvicorn et expose le port 8000."
- "Propose un test d'intégration FastAPI utilisant `TestClient` pour l'endpoint `/predict`."
- "Ajoute instrumentation Prometheus pour compter les requêtes HTTP et mesurer la latence."
- "Donne un manifest Helm simple pour déployer un service FastAPI avec requests/limits et probes."

**Exclusions et bonnes pratiques**

- Ne pas modifier directement les workflows CI/CD ou les secrets; proposer des PRs et des instructions de validation.
- Éviter les chemins locaux non reproductibles et les dépendances non déclarées.
- Préférer les changements atomiques et testés; chaque PR doit inclure des tests ou une justification.

**Conventions PR / commit**

- Préférer des PRs petites et ciblées avec titre clair et description des changements.
- Messages de commit concis: `feat:`, `fix:`, `chore:` suivis d'une courte description.

