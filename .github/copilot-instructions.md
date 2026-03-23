## Instructions personnalisées GitHub Copilot — Français

But
: Fournir des suggestions cohérentes avec les conventions du dépôt, accélérer la rédaction de code et aider les contributeurs sur Python, MLOps, déploiement et observabilité.

Contexte du dépôt
- Stack technique: Python, Docker, FastAPI, Kubernetes, Prometheus, Grafana, Loki.
- Public cible: data scientists, ingénieurs MLOps, développeurs backend.

Préférences générales
- Style de code: Respecter PEP 8, noms explicites, fonctions courtes (<= 50 lignes), type hints quand possible.
- Tests: Préférer `pytest`; viser une couverture minimale acceptable (ex: 80% pour modules critiques).
- Logging: Utiliser le module `logging` avec niveaux adaptés; ne pas « print » en production.
- Sécurité: Ne jamais générer ni proposer d'insérer des secrets (clé API, mots de passe). Utiliser des variables d'environnement et des solutions de vault.
Préférences générales
Préférences générales
- Style de code: Respecter PEP 8, noms explicites, fonctions courtes (<= 50 lignes), type hints quand possible. Utiliser un formatteur automatique pour garantir la conformité (préférer `black` + `isort`).
- Tests: Préférer `pytest`; viser une couverture minimale acceptable (ex: 80% pour modules critiques).
- Logging: Utiliser le module `logging` avec niveaux adaptés; ne pas « print » en production.
- Sécurité: Ne jamais générer ni proposer d'insérer des secrets (clé API, mots de passe). Utiliser des variables d'environnement et des solutions de vault.
- Docstrings: Toutes les fonctions et classes doivent inclure une docstring conforme à PEP 257; documenter paramètres, valeurs de retour et exceptions. Préférer le style Google ou NumPy pour la structure des docstrings.

Outils recommandés
- Formatage automatique: `black` (configurable via `pyproject.toml`).
- Tri des imports: `isort`.
- Linting: `ruff` ou `flake8` pour détecter violations PEP8 et erreurs courantes.
- Hooks git: utiliser `pre-commit` pour exécuter `black`, `isort` et `ruff/flake8` avant chaque commit.

Exemples de commandes (local)
```bash
python -m pip install --user black isort ruff pre-commit
black .
isort .
ruff check .
pre-commit run --all-files
```
- Style de code: Respecter PEP 8, noms explicites, fonctions courtes (<= 50 lignes), type hints quand possible.
- Tests: Préférer `pytest`; viser une couverture minimale acceptable (ex: 80% pour modules critiques).
- Logging: Utiliser le module `logging` avec niveaux adaptés; ne pas « print » en production.
- Sécurité: Ne jamais générer ni proposer d'insérer des secrets (clé API, mots de passe). Utiliser des variables d'environnement et des solutions de vault.
- Docstrings: Toutes les fonctions et classes doivent inclure une docstring conforme à PEP 257; documenter paramètres, valeurs de retour et exceptions. Préférer le style Google ou NumPy pour la structure des docstrings.

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

Exemples de requêtes utiles pour Copilot
- "Propose une fonction Python pour normaliser un DataFrame pandas selon PEP8 et avec type hints."
- "Écris un Dockerfile minimal pour une app FastAPI servant `app:app` sur Uvicorn." 
- "Donne un manifest Helm simple pour déployer un service FastAPI avec requests/limits et probes." 
- "Ajoute instrumentation Prometheus pour compter les requêtes HTTP et mesurer la latence."

Restrictions et interdits
- Ne pas générer: secrets, clés d'API, mots de passe, ou instructions pour contourner la sécurité.
- Éviter suggestions qui hardcodent des chemins locaux non reproductibles.

Usage opérationnel
- Ce fichier doit rester à la racine `.github/copilot-instructions.md` pour être pris en compte.
- Pour proposer une modification: ouvrir une PR petite et explicite, inclure tests et instructions de validation.

Contact / Références
- Pour les conventions de style, voir le README du projet.
- Si incertitude sur le pattern, privilégier une solution testable et documentée.

---
Ajoutez ou adaptez les sections ci‑dessous selon vos besoins spécifiques du dépôt.

Commit suggéré
```bash
git add .github/copilot-instructions.md
git commit -m "Ajout: instructions Copilot (FR) orientées Python / MLOps"
git push
```

