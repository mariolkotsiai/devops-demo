# DevOps Demo — Full-Stack Project

A complete DevOps demonstration combining a Java Spring Boot REST API, Docker containerization, Python automation, monitoring with Prometheus/Grafana, and a CI/CD pipeline with GitHub Actions.

This project brings together the skills demonstrated individually in my other repositories into a single, deployable system.

## Architecture
┌─────────────────┐     ┌──────────────┐     ┌─────────────┐

│  Spring Boot API │────▶│  Prometheus  │────▶│   Grafana   │

│   (Java/Docker)  │     │  (metrics)   │     │ (dashboard) │

└─────────────────┘     └──────────────┘     └─────────────┘

│

▼

┌─────────────────┐

│  Python Health   │

│   Check Script   │

└─────────────────┘

## Components

- **app/** — Java Spring Boot Library API, containerized with Docker
- **scripts/** — Python health check script for monitoring API uptime
- **monitoring/** — Prometheus configuration for metrics scraping
- **docker-compose.yml** — Orchestrates all services together
- **.github/workflows/** — CI/CD pipeline (build, test, Docker image creation)

## Tech Stack

![Java](https://img.shields.io/badge/Java-21-orange?logo=java)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-3.5.14-green?logo=springboot)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-Dashboards-F46800?logo=grafana)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?logo=githubactions)

## Quick Start

```bash
git clone https://github.com/mariolkotsiai/devops-demo.git
cd devops-demo
docker-compose up --build
```

Once running:

| Service | URL |
|---|---|
| Library API | http://localhost:8080/api/books |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 (admin/admin) |

## Running the Health Check Script

```bash
python scripts/health_check.py
```

Generates a JSON report at `scripts/health_report.json` showing the status and response time of each API endpoint.

## CI/CD Pipeline

On every push to `main`, GitHub Actions automatically:
1. Builds the Java application with Maven
2. Runs all unit tests
3. Validates the Python health check script
4. Builds the Docker image
5. Verifies the image was created successfully

## Project Structure
devops-demo/

├── app/                      # Spring Boot application

│   ├── src/

│   ├── pom.xml

│   └── Dockerfile

├── scripts/

│   └── health_check.py       # API health monitoring

├── monitoring/

│   └── prometheus.yml        # Metrics scraping config

├── .github/workflows/

│   └── ci.yml                # CI/CD pipeline

└── docker-compose.yml        # Service orchestration

## Related Projects

This project combines work from:
- [python-fastapi-employee-manager](https://github.com/mariolkotsiai/python-fastapi-employee-manager) — Python API patterns
- [java-springboot-library](https://github.com/mariolkotsiai/java-springboot-library) — The Spring Boot API used here
- [java-algorithms](https://github.com/mariolkotsiai/java-algorithms) — Core Java fundamentals

## License

MIT License