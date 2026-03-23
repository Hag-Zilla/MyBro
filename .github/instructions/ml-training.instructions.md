---
applyTo: "src/ml/training/**/*.py,src/ml/**/*train*.py"
---

## Instructions for MLOps Training Code

### Validation and Data
- **Cross-validation mandatory**: use `sklearn.model_selection.cross_validate` or `KFold`, `StratifiedKFold` depending on context.
- **Minimal Train/Val/Test split**: 70%/15%/15 minimum; document if `applyTo` is `src/ml/**` then justify other ratio.
- **Data validation**: check shape, null values, outliers before training. Use the `logging` module to trace.
- **Reproducibility**: fix all random seeds (`np.random.seed()`, `random.seed()`, `torch.manual_seed()` if using ML framework).

### Hyperparameters and Tracking
- **Documented hyperparameters**: include in function docstring, dict or config object format, no magic numbers.
- **MLflow or equivalent**: log metrics (`accuracy`, `f1`, `loss`), params, model artifact for each run.
- **Early stopping and callbacks**: implement validation loss monitoring, patience > 3 epochs.

### Model Tests and Validation
- Add `pytest` test to:
  - Verify model output shape and type (e.g., `assert y_pred.shape == (n_samples,)`)
  - Verify no NaN/Inf after training
  - Sanity check: model must surpass baseline (e.g., min 60% acc on simple dataset)
- **Data drift monitoring**: compare train vs validation distribution via `scipy.stats` or Kolmogorov-Smirnov.
- **Model card / README**: document model version, params, performance metrics, limitations.

### Logging and Observability
- Use `logging` with INFO (progress), WARNING (data issues), ERROR (failures) levels.
- Include timestamps, parametrization, metrics in structured format (no print).

