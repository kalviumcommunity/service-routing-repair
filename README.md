# service-routing-repair

CampusBoard containers start, but host API and dashboard requests fail. Repair listener and internal API address settings without changing ports or service responses.

## Prerequisites

Git, Docker Engine and POSIX shell (Linux/macOS or WSL with Docker integration). Compose v2 required for Compose commands; curl required for host HTTP checks. Docker must be running; internet access needed to download python:3.12-slim. Reserve documented host ports. Docker Desktop is subject to its license; Linux Docker Engine is sufficient. No cloud account, billing, registry login, real credentials, Kubernetes cluster or paid tools needed. Fork or clone this starter and run commands from repository root.

## Allowed edits

compose.yaml (BIND and API_URL only), routing-review.md. Preserve all other source, routes, ports, fixtures and checks. No failure suppression or fabricated output.

## Required behaviour and commands

API container port is 8080; dashboard container port is 9000. Published host ports must remain 18082 and 19082. Host API URL is http://localhost:18082/health; dashboard URL is http://localhost:19082/.

Task 1: diagnose API status/logs and an inside-container loopback request before editing. The API must accept traffic through its published port, not just its own loopback interface. Only its BIND setting may change. Recreate after changing runtime settings; rebuilding is not necessary for these setting changes.

Task 2: after Task 1, diagnose dashboard HTTP 502 and its logged connection error. From inside dashboard compare its configured address with the API service name and container port on the Compose network. Correct API_URL only. Do not use host networking, host.docker.internal, a fixed container IP or hardcoded response.

Task 3: demonstrate both host responses, both containers Up and actual published ports. Complete the three routing-review.md lines using observed local evidence, not cloud claims.
```sh
docker compose up -d --build
docker compose ps
docker compose logs --tail=10
docker compose port api 8080
docker compose port dashboard 9000
```
Use docker compose exec -T SERVICE python -c with urllib.request for inside-container requests. Wait for listener startup before HTTP checks. Cleanup: docker compose down.
