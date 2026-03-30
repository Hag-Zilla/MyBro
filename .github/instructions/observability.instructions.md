---
applyTo: "src/**/metrics/**/*.py,src/**/monitoring/**/*.py,src/**/*metrics*.py,src/**/*monitoring*.py"
---

## Purpose

Guide Copilot for observability code covering Prometheus metrics, structured logging (Loki), and Grafana dashboard hints.

## Guidelines

### Prometheus Metrics
- Define metrics at module level (not inside functions) to avoid re-registration errors.
- Use the correct metric type: `Counter` for counts, `Histogram` for latency/size, `Gauge` for live values.
- Always add a `labelnames` list; avoid high-cardinality labels (e.g., user IDs or raw URLs).
- Expose metrics on a dedicated `/metrics` endpoint; never mix it with business routes.

```python
from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status_code"],
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency",
    ["endpoint"],
    buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5],
)
```

### Structured Logging (Loki)
- Use JSON log format compatible with Loki label extraction.
- Include at minimum: `timestamp`, `level`, `service`, `message`, and context fields (`request_id`, `endpoint`).
- Use `logging` module with a JSON formatter; avoid `print` in production.

```python
import logging, json

class JsonFormatter(logging.Formatter):
    """Format log records as JSON for Loki ingestion."""
    def format(self, record: logging.LogRecord) -> str:
        return json.dumps({
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "service": "my-service",
            "message": record.getMessage(),
        })
```

### Grafana
- When generating dashboard JSON, include: title, time range, refresh interval, and at least one `rate()` panel.
- Prefer `rate(counter[5m])` over raw counter values in panels.
- Group panels by domain: latency / errors / throughput.

### Testing
- Add a test that verifies metric registration does not raise on import.
- Add a test that exercises the instrumented function and checks that the counter increments.
