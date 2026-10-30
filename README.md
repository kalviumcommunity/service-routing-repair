# service-routing-repair

Intentionally broken DevOps Foundation Module 4 starter. Only documented faults and incomplete review lines require repair. Read assessment before editing.

## Preparation

Fork https://github.com/kalviumcommunity/service-routing-repair, clone YOUR fork and create fix/module4 branch. Free local Docker Engine/Compose, Git, terminal and PDF export only. Docker Desktop subject to its license; free Docker Engine on Linux is sufficient. No cloud account, billing, registry login, tokens, paid tools or Kubernetes cluster. Pull python:3.12-slim  before assessment. Host ports 18081-18084 and 19082 must be free. POSIX shell (Linux/macOS or prepared WSL); preparation and image downloads outside timer.

## Allowed edits

compose.yaml (BIND and API_URL only), routing-review.md. Keep routes, ports, application behaviour, fixtures and baseline unchanged except explicitly permitted temporary cache comment. Capture original failure before each repair. No bypasses or fabricated evidence.

## Required behaviour and commands

API listens on 8080, dashboard on 9000; host ports remain 18082/19082. Task 1 changes BIND to 0.0.0.0, then docker compose up -d recreates API without rebuild. Diagnose inside API loopback request versus host failure. Task 2 changes API_URL hostname and port to http://api:8080; recreate dashboard. Before fix compare localhost:9999 and api:8080 requests from dashboard. Do not use host networking, host.docker.internal or hardcoded dashboard response. Task 3 writes three path/evidence lines and verifies host /health plus dashboard response containing actual API health JSON. No app code changes. Run docker compose up -d --build, docker compose ps/logs/port/exec as taught. Cleanup docker compose down.

## Evidence and submission

One PDF, three labelled task sections. Grade only task work and requested screenshot/written evidence. Repository/fork URLs, branch names and submission commit hashes are not required or graded. Show initial failures, actual diagnosis commands, complete corrected diff, successful checks and requested written lines. At least one real screenshot per task. No PR/video/ZIP. Written answers human-graded; static configuration alone is not runtime proof. Keep .env untracked. Wait for startup log/health state, not arbitrary immediate curl. Do not remove unrelated containers. Cleanup exercise containers only.
