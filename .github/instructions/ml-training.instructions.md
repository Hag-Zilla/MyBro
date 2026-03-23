---
applyTo: "src/ml/training/**/*.py,src/ml/**/*train*.py"
---

## Instructions pour code de training MLOps

### Validation et datos
- **Cross-validation obligatoire**: utiliser `sklearn.model_selection.cross_validate` ou `KFold`, `StratifiedKFold` selon contexte.
- **Train/Val/Test split minimal**: 70%/15%/15 au minimum; documenter if "applyTo": `src/ml/**` then justifier autre ratio.
- **Data validation**: vérifier shape, null values, outliers avant training. Utiliser le module `logging` pour tracer.
- **Reproducibilité**: fixer tous les random seeds (`np.random.seed()`, `random.seed()`, `torch.manual_seed()` si ML framework).

### Hyperparamètres et suivi
- **Hyperparamètres documentés**: inclure dans docstring de fonction, format dict ou config object, pas magic numbers.
- **MLflow ou équivalent**: logger métriques (`accuracy`, `f1`, `loss`), params, model artifact pour chaque run.
- **Early stopping et callbacks**: implémenter monitoring validation loss, patience > 3 epochs.

### Tests et validation modèle
- Ajouter test `pytest` pour en:
  - Vérifier output shape et type du modèle (ex: `assert y_pred.shape == (n_samples,)`)
  - Vérifier no NaN/Inf après training
  - Sanity check: modèle doit surpasser baseline (ex: 60% acc min sur dataset simple)
- **Data drift monitoring**: comparer distribution train vs validation via `scipy.stats` ou Kolmogorov-Smirnov.
- **Model card / README**: documenter version modèle, params, performance metrics, limitations.

### Logging et observabilité
- Utiliser `logging` avec niveaux INFO (progression), WARNING (data issues), ERROR (failures).
- Inclure timestamps, parametrization, metrics en structuré (pas print).

