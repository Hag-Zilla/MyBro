# Docker & Kubernetes Best Practices

Generate Docker and Kubernetes manifests following these practices:

## Docker

1. **Multi-stage builds** to minimize image size:

   ```dockerfile
   FROM python:3.11 as builder
   # Install dependencies
   FROM python:3.11
   # Copy from builder
   ```

2. **Security**:
   - Use non-root user: `USER appuser`
   - Minimal base image (python:3.11-slim)
   - Pin package versions in requirements.txt

3. **Health checks**:

   ```dockerfile
   HEALTHCHECK --interval=30s CMD python /app/health_check.py
   ```

## Kubernetes

1. **Resource requests/limits**:

   ```yaml
   resources:
     requests:
       cpu: 100m
       memory: 256Mi
     limits:
       cpu: 500m
       memory: 512Mi
   ```

2. **Probes** (readiness + liveness):

   ```yaml
   livenessProbe:
     httpGet:
       path: /health
       port: 8000
     initialDelaySeconds: 10
   readinessProbe:
     httpGet:
       path: /ready
       port: 8000
     initialDelaySeconds: 5
   ```

3. **Rolling updates**:

   ```yaml
   strategy:
     type: RollingUpdate
     rollingUpdate:
       maxSurge: 1
       maxUnavailable: 0
   ```

4. **Environment & ConfigMap**:

   ```yaml
   envFrom:
     - configMapRef:
         name: app-config
   ```

Reference standards: #file:../copilot-instructions.md
