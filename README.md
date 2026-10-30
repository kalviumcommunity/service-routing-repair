# service-routing-repair

Intentionally broken DevOps Foundation Module 4 starter. No solved implementation or completed review answers are supplied. Diagnose and repair only the assessment tasks.

## Preparation

Fork or clone https://github.com/kalviumcommunity/service-routing-repair before assessment. Fork ownership is not graded. Use free local Docker Engine/Compose, Git and POSIX shell (Linux/macOS or prepared WSL). Docker Desktop subject to its license; Linux Docker Engine is sufficient. Pull python:3.12-slim before assessment. Reserve exercise ports only. Preparation/download delays excluded. No cloud account, billing, registry login, real credentials, paid tools or Kubernetes needed.

## Allowed edits

compose.yaml (BIND and API_URL only), routing-review.md. Preserve all other source, routes, ports, fixtures and checks. No failure suppression or fabricated output. Existing run.sh tolerates absence of its old exercise container only; that cleanup is not an application-validation bypass.

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

## Evidence and submission

Follow assessment's three tasks. One PDF, three labelled task sections, at least one real terminal screenshot per task, requested findings and cause/fix/result captions. Include complete corrected diff of permitted files once. Show original failures and final checks only as requested by each task. Grade only those tasks and evidence (6 + 7 + 7 = 20). Repository/fork URLs, fork ownership, branch names and submission commit hashes are not required or graded. Technical image IDs remain required where tasks ask for them. Standalone instructor evidence is valid under the same technical criteria. Written findings are manually assessed; local evidence does not prove Cloud Run deployment. No PR, video or ZIP. Cleanup only exercise containers; never expose real credentials.
