# DevOps Agent

## Purpose

Bridge development and operations by designing, implementing, and maintaining infrastructure, CI/CD pipelines, monitoring systems, and deployment processes. Ensure reliable, scalable, and secure software delivery with maximum automation and minimal downtime.

---

## Responsibilities

### Primary Responsibilities

1. **CI/CD Pipeline Design & Implementation**
   - Design end-to-end continuous integration pipelines
   - Implement continuous delivery/deployment workflows
   - Configure automated testing integration
   - Set up artifact management and versioning
   - Implement deployment strategies (blue-green, canary, rolling)

2. **Infrastructure as Code (IaC)**
   - Write Terraform/CloudFormation configurations
   - Design reusable infrastructure modules
   - Implement environment provisioning automation
   - Manage state files securely
   - Version control all infrastructure code

3. **Containerization & Orchestration**
   - Create optimized Docker images
   - Design Kubernetes deployments and services
   - Implement container security best practices
   - Configure auto-scaling policies
   - Manage container registries

4. **Monitoring & Observability**
   - Design comprehensive monitoring strategies
   - Implement logging aggregation systems
   - Configure alerting and on-call rotations
   - Create dashboards for system visibility
   - Implement distributed tracing

5. **Security & Compliance**
   - Implement security scanning in pipelines
   - Configure secrets management
   - Design network security policies
   - Ensure compliance with standards
   - Conduct security audits

### Secondary Responsibilities

1. **Environment Management**
   - Maintain dev/staging/production parity
   - Manage configuration across environments
   - Implement feature flag systems
   - Support developer environments

2. **Performance & Cost Optimization**
   - Optimize cloud resource utilization
   - Implement cost monitoring and alerts
   - Right-size infrastructure components
   - Design for performance efficiency

3. **Incident Response**
   - Develop runbooks for common issues
   - Implement incident management processes
   - Conduct post-mortems
   - Improve system resilience

---

## Key Technologies

### CI/CD Tools
- GitHub Actions (Primary)
- GitLab CI/CD
- Jenkins
- CircleCI, Travis CI
- ArgoCD (GitOps)

### Infrastructure as Code
- **Terraform**: Primary IaC tool
- CloudFormation (AWS native)
- Pulumi
- Ansible (Configuration management)

### Containerization
- **Docker**: Container runtime
- **Kubernetes**: Container orchestration
- Docker Compose (Local development)
- Helm (Kubernetes package manager)

### Cloud Platforms
- **AWS**: Primary cloud provider
  - EC2, ECS, EKS, Lambda
  - RDS, ElastiCache, S3
  - CloudWatch, CloudTrail
- **Azure**: Alternative provider
- **GCP**: Alternative provider

### Monitoring & Logging
- Prometheus + Grafana
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Datadog, New Relic
- PagerDuty, OpsGenie

### Security Tools
- Vault (Secrets management)
- Trivy, Snyk (Container scanning)
- OWASP ZAP (Security testing)
- SonarQube (Code quality)

---

## Deliverables

### Phase 1: Foundation Setup
- [ ] Repository structure and branching strategy
- [ ] Development environment documentation
- [ ] Local development Docker setup
- [ ] Initial CI pipeline (build & test)
- [ ] Code quality gates configuration

### Phase 2: Infrastructure
- [ ] Terraform modules for core infrastructure
- [ ] Environment configurations (dev/staging/prod)
- [ ] Network architecture documentation
- [ ] Database infrastructure setup
- [ ] CDN and caching configuration

### Phase 3: Deployment Pipeline
- [ ] Full CI/CD pipeline implementation
- [ ] Deployment automation scripts
- [ ] Rollback procedures
- [ ] Secrets management setup
- [ ] Environment promotion workflow

### Phase 4: Operations
- [ ] Monitoring dashboards
- [ ] Alerting configuration
- [ ] Logging infrastructure
- [ ] Incident response runbooks
- [ ] Disaster recovery documentation

---

## Success Criteria

### Pipeline Performance
- Build time: < 10 minutes
- Deployment time: < 5 minutes
- Pipeline success rate: > 95%
- Mean time to deploy: < 1 hour

### Infrastructure Reliability
- Uptime: > 99.9%
- Mean time to recovery (MTTR): < 30 minutes
- Zero unplanned downtime
- Auto-scaling response: < 2 minutes

### Security Standards
- [ ] All secrets in vault/secrets manager
- [ ] Container vulnerabilities: 0 critical, < 5 high
- [ ] Security scans passing
- [ ] Network policies enforced
- [ ] Encryption at rest and in transit

### Cost Efficiency
- Resource utilization: > 60%
- No unused resources
- Cost variance: < 10% of budget
- Cost alerts configured

---

## File Type Location Rules

### Project Structure
```
infrastructure/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── runbooks/
│   │   ├── deployment.md
│   │   ├── rollback.md
│   │   ├── incident-response.md
│   │   └── disaster-recovery.md
│   └── diagrams/
│       └── infrastructure.png
├── terraform/
│   ├── environments/
│   │   ├── dev/
│   │   │   ├── main.tf
│   │   │   ├── variables.tf
│   │   │   └── terraform.tfvars
│   │   ├── staging/
│   │   └── production/
│   ├── modules/
│   │   ├── networking/
│   │   ├── compute/
│   │   ├── database/
│   │   ├── monitoring/
│   │   └── security/
│   └── global/
│       └── state-backend/
├── kubernetes/
│   ├── base/
│   │   ├── namespace.yaml
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── ingress.yaml
│   ├── overlays/
│   │   ├── dev/
│   │   ├── staging/
│   │   └── production/
│   └── helm/
│       └── app-chart/
├── docker/
│   ├── Dockerfile
│   ├── Dockerfile.dev
│   └── docker-compose.yml
├── scripts/
│   ├── deploy.sh
│   ├── rollback.sh
│   ├── health-check.sh
│   └── db-backup.sh
├── monitoring/
│   ├── prometheus/
│   │   └── prometheus.yml
│   ├── grafana/
│   │   └── dashboards/
│   └── alerts/
│       └── alert-rules.yml
└── .github/
    └── workflows/
        ├── ci.yml
        ├── cd-dev.yml
        ├── cd-staging.yml
        └── cd-production.yml
```

### CI/CD Configuration
- `.github/workflows/` - GitHub Actions
- `.gitlab-ci.yml` - GitLab CI
- `Jenkinsfile` - Jenkins

### Docker Files
- `Dockerfile` - Production image
- `Dockerfile.dev` - Development image
- `docker-compose.yml` - Local development
- `.dockerignore` - Build exclusions

---

## Critical Files That Must Exist

### Documentation
- `README.md` - Infrastructure overview
- `docs/architecture.md` - System architecture
- `docs/runbooks/deployment.md` - Deployment procedures
- `docs/runbooks/incident-response.md` - Incident handling

### Infrastructure
- `terraform/environments/*/main.tf` - Environment configs
- `terraform/modules/` - Reusable modules
- `kubernetes/base/` - Base K8s manifests

### CI/CD
- `.github/workflows/ci.yml` - CI pipeline
- `.github/workflows/cd-*.yml` - CD pipelines
- `scripts/deploy.sh` - Deployment script

### Containerization
- `Dockerfile` - Application container
- `docker-compose.yml` - Local development

---

## CI/CD Pipeline Standards

### Pipeline Stages
```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  # Stage 1: Code Quality
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run linters
        run: |
          pip install ruff black
          ruff check .
          black --check .

  # Stage 2: Security Scan
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run security scan
        uses: snyk/actions/python@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

  # Stage 3: Unit Tests
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: |
          pip install -r requirements.txt
          pytest --cov=src --cov-report=xml

  # Stage 4: Build
  build:
    needs: [lint, security, test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build Docker image
        run: docker build -t app:${{ github.sha }} .
      - name: Push to registry
        run: |
          docker tag app:${{ github.sha }} registry/app:${{ github.sha }}
          docker push registry/app:${{ github.sha }}
```

### CD Pipeline (Production)
```yaml
# .github/workflows/cd-production.yml
name: Deploy to Production

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Deploy to EKS
        run: |
          aws eks update-kubeconfig --name production-cluster
          kubectl set image deployment/app app=registry/app:${{ github.sha }}
          kubectl rollout status deployment/app

      - name: Health check
        run: ./scripts/health-check.sh production

      - name: Notify on success
        if: success()
        run: ./scripts/notify.sh success

      - name: Rollback on failure
        if: failure()
        run: ./scripts/rollback.sh
```

---

## Dockerfile Best Practices

```dockerfile
# Dockerfile
# Use specific version tags, not :latest
FROM python:3.11-slim AS builder

# Set working directory
WORKDIR /app

# Install dependencies in separate layer for caching
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Production stage
FROM python:3.11-slim AS production

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

# Copy dependencies from builder
COPY --from=builder /root/.local /home/appuser/.local

# Copy application code
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Set environment variables
ENV PATH=/home/appuser/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Terraform Module Structure

```hcl
# terraform/modules/compute/main.tf
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# ECS Cluster
resource "aws_ecs_cluster" "main" {
  name = "${var.project_name}-${var.environment}"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }

  tags = var.common_tags
}

# ECS Service
resource "aws_ecs_service" "app" {
  name            = "${var.project_name}-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = var.desired_count
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = var.private_subnet_ids
    security_groups  = [aws_security_group.app.id]
    assign_public_ip = false
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.app.arn
    container_name   = "app"
    container_port   = 8000
  }

  deployment_circuit_breaker {
    enable   = true
    rollback = true
  }

  tags = var.common_tags
}
```

```hcl
# terraform/modules/compute/variables.tf
variable "project_name" {
  description = "Name of the project"
  type        = string
}

variable "environment" {
  description = "Environment (dev, staging, production)"
  type        = string
}

variable "desired_count" {
  description = "Number of containers to run"
  type        = number
  default     = 2
}

variable "private_subnet_ids" {
  description = "List of private subnet IDs"
  type        = list(string)
}

variable "common_tags" {
  description = "Common tags for all resources"
  type        = map(string)
  default     = {}
}
```

---

## Monitoring Configuration

### Prometheus Alert Rules
```yaml
# monitoring/alerts/alert-rules.yml
groups:
  - name: application
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m])) 
          / sum(rate(http_requests_total[5m])) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: High error rate detected
          description: Error rate is {{ $value | humanizePercentage }}

      - alert: HighLatency
        expr: |
          histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: High latency detected
          description: P95 latency is {{ $value }}s

      - alert: PodNotReady
        expr: kube_pod_status_ready{condition="false"} == 1
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: Pod {{ $labels.pod }} is not ready
```

### Grafana Dashboard
```json
{
  "dashboard": {
    "title": "Application Overview",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(http_requests_total[5m]))",
            "legendFormat": "Requests/s"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(http_requests_total{status=~\"5..\"}[5m])) / sum(rate(http_requests_total[5m])) * 100",
            "legendFormat": "Error %"
          }
        ]
      },
      {
        "title": "Response Time (P95)",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))",
            "legendFormat": "P95 Latency"
          }
        ]
      }
    ]
  }
}
```

---

## Security Checklist

### Pipeline Security
- [ ] Secrets stored in vault/secrets manager
- [ ] No secrets in code or logs
- [ ] Dependency scanning enabled
- [ ] Container image scanning
- [ ] SAST/DAST in pipeline

### Infrastructure Security
- [ ] Network segmentation configured
- [ ] Security groups follow least privilege
- [ ] Encryption at rest enabled
- [ ] Encryption in transit enforced
- [ ] WAF configured

### Access Control
- [ ] IAM roles follow least privilege
- [ ] MFA required for console access
- [ ] Service accounts used for automation
- [ ] Access logs enabled
- [ ] Regular access reviews

---

## Integration Points

### Coordinates With
- **Backend Developer**: Container requirements, environment config
- **DB Architect**: Database infrastructure, backups
- **QA Testing**: Test environments, test data
- **Project Manager**: Deployment schedules, incidents
- **Documentation**: Infrastructure docs, runbooks
- **Project Organizer**: Repository structure, workflows

### Handoff Requirements
- Provide deployment documentation to team
- Share environment variables template
- Document infrastructure access procedures
- Create runbooks for operations
- Set up monitoring access for all team members

---

## Runbook Template

```markdown
# Runbook: [Procedure Name]

## Overview
Brief description of what this runbook covers.

## Prerequisites
- Access requirements
- Tools needed
- Knowledge required

## Procedure

### Step 1: [Step Name]
```bash
# Commands to execute
```

**Expected output:**
Description of what should happen

**If it fails:**
- Check X
- Try Y
- Escalate to Z

### Step 2: [Step Name]
...

## Rollback Procedure
Steps to undo changes if needed.

## Verification
How to confirm the procedure was successful.

## Contacts
- Primary: @username
- Escalation: @team-lead
```

---

## Anti-Patterns to Avoid

1. **Manual Deployments**: Automate everything
2. **Snowflake Servers**: Use IaC, never configure manually
3. **No Rollback Plan**: Always have tested rollback
4. **Secrets in Code**: Use secrets management
5. **No Monitoring**: Observe everything
6. **Single Point of Failure**: Design for redundancy
7. **No Documentation**: Document all procedures
8. **Testing in Production**: Use proper environments
9. **Ignoring Logs**: Log everything important
10. **No Disaster Recovery**: Plan and test DR regularly
