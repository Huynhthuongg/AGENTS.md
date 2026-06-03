<div align="center">

# 🤖 Universal Project Compiler Agent

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-darkred?style=for-the-badge)](LICENSE)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Termux Ready](https://img.shields.io/badge/Termux-Ready-2d2d2d?style=for-the-badge&logo=android)](https://termux.dev)
[![Status: Active](https://img.shields.io/badge/Status-Active-green?style=for-the-badge&logo=github)](https://github.com/Huynhthuongg/AGENTS.md)
[![Code Quality](https://img.shields.io/badge/Code%20Quality-A-brightgreen?style=for-the-badge)](.)

---

### 📱 Android-first • 🚀 Termux-ready • 🔧 No Docker • ✨ AI-powered

**Transform documents, specs, repositories, OCR text, Markdown, or natural language into complete, runnable, production-ready software projects in seconds.**

[📖 Documentation](#-quick-start) • [🚀 Get Started](#-quick-start) • [🔗 API](#-api-examples) • [💬 Issues](https://github.com/Huynhthuongg/AGENTS.md/issues)

</div>

---

## ✨ Features

<table>
<tr>
<td>

### 🎯 **Core Features**
- 🏗️ Python CLI (`upca`) for local workflows
- ⚡ FastAPI service with planning & compilation endpoints
- 🧠 AI-powered planning engine (Critical/High/Medium/Low tasks)
- 🛡️ Safe compiler with security validation
- 🔐 Secret redaction & path traversal protection
- 📱 Termux-optimized (runs on low-memory Android)

</td>
<td>

### 🔒 **Security & Quality**
- ✅ HTTP security headers
- 🚫 Secret pattern detection
- 🔍 Safe slug generation
- 📝 Full test coverage
- 🧹 Ruff linting & Codespell
- 📚 Complete documentation

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Git
- 200MB disk space (Termux-friendly)

### Installation & Run

```bash
# Clone and setup
git clone https://github.com/Huynhthuongg/AGENTS.md.git
cd AGENTS.md
./scripts/setup.sh
./scripts/start.sh
```

Open **http://127.0.0.1:8000** in your browser or use the CLI:

```bash
# Plan a project
upca plan --text "# CRM Dashboard\nNeed auth, API, admin dashboard, dark mode"

# Compile & generate
upca compile --text "# CRM Dashboard\nNeed auth, API, admin dashboard" --output-dir generated
```

### 📱 Termux Setup

```bash
pkg update && pkg install python git
cd ~
git clone https://github.com/Huynhthuongg/AGENTS.md.git
cd AGENTS.md
./scripts/setup.sh
./scripts/start.sh
```

---

## 🔌 API Examples

### Health Check
```bash
curl -s http://127.0.0.1:8000/health
```

### Plan Endpoint
```bash
curl -s -X POST http://127.0.0.1:8000/plan \
  -H 'Content-Type: application/json' \
  -d '{
    "requirements": "# Portal\nNeed API, dashboard, auth and mobile responsive UI"
  }'
```

### Compile Endpoint
```bash
curl -s -X POST http://127.0.0.1:8000/compile \
  -H 'Content-Type: application/json' \
  -d '{
    "requirements": "# E-commerce Store\nPython FastAPI backend, React frontend, PostgreSQL",
    "output_dir": "generated"
  }'
```

---

## 📁 Project Structure

```
AGENTS.md/
├── app/universal_compiler_agent/    # Main application package
│   ├── cli.py                        # CLI interface
│   ├── server.py                     # FastAPI server
│   ├── planner.py                    # Planning engine
│   └── compiler.py                   # Code generation
├── config/                           # Configuration examples
├── docs/                             # Architecture & specs
├── scripts/                          # Setup & helpers
│   ├── setup.sh                      # Initial setup
│   ├── start.sh                      # Start server
│   ├── check.sh                      # Run tests & linters
│   └── backup.sh                     # Backup script
├── tests/                            # Unit tests
├── .github/workflows/                # CI/CD pipelines
├── pyproject.toml                    # Project configuration
└── LICENSE                           # AGPL-3.0
```

---

## 🛠️ Development

### Setup Development Environment

```bash
# Install dev dependencies
python -m pip install -e '.[dev]'

# Run quality checks
./scripts/check.sh
```

The `check.sh` script runs:
- 🔍 Ruff (linter)
- ✏️ Codespell (spell checker)
- ✅ Pytest (test suite)

---

## 📊 Current Release

| Property | Details |
|----------|---------|
| **Version** | 0.1.1 |
| **Release Date** | 2026-06-02 |
| **Python** | 3.10+ |
| **License** | AGPL-3.0-only |
| **Status** | ✅ Active Development |

### Release Highlights v0.1.1
- 🏃 CLI dry-run previews
- 📂 Safe output directory validation
- 🎛️ Dashboard route alignment
- 🧪 Hardened test workflows

---

## 🔐 Security Model

We take security seriously:

- 🚫 **No hardcoded secrets** in generated output
- 🔍 **Pattern detection** redacts API keys, tokens, passwords
- 🛡️ **Path validation** prevents directory traversal attacks
- 🔒 **HTTP headers** follow security best practices
- ✅ **AGPL-3.0** ensures transparency

---

## 📦 Dependencies

### Core
- **FastAPI** (0.115+) - Web framework
- **Uvicorn** (0.30+) - ASGI server
- **Pydantic** (2.8+) - Data validation

### Development
- **Pytest** (8.0+) - Testing
- **Ruff** (0.6+) - Code linting
- **Httpx** (0.28+) - HTTP client
- **Codespell** (2.3+) - Spell checking

---

## 🌟 Sponsors & Contributors

<div align="center">

### ✨ **Thank You to Our Sponsors!** ✨

<div style="animation: pulse 2s infinite; display: inline-block;">

[![Sponsor Badge](https://img.shields.io/badge/❤️_Sponsor_This_Project-ea4aaa?style=for-the-badge&logo=github-sponsors&logoColor=white)](https://github.com/sponsors/Huynhthuongg)

</div>

**Become a sponsor and help us develop faster! Your support helps maintain and improve this project.**

### 🏆 Featured Sponsors

<table>
<tr>
<td align="center" width="50%">
  <a href="https://github.com/sponsors/Huynhthuongg">
    <img src="https://avatars.githubusercontent.com/u/252359928?v=4" width="100px;" alt="Your Logo Here" style="border-radius: 50%; border: 3px solid #ffd700; animation: glow 1.5s ease-in-out infinite;"/>
    <br/>
    <b>Your Company Here</b>
    <br/>
    <sub>🌟 Platinum Sponsor</sub>
  </a>
</td>
<td align="center" width="50%">
  <a href="https://github.com/sponsors/Huynhthuongg">
    <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=sponsor" width="100px;" alt="Sponsor 2" style="border-radius: 50%; border: 3px solid #c0c0c0;"/>
    <br/>
    <b>Support Us</b>
    <br/>
    <sub>🥈 Gold Sponsor</sub>
  </a>
</td>
</tr>
</table>

### 👥 Contributors

<div align="center">

Thanks to all our contributors! Your contributions make this project better every day.

[![Contributors](https://contrib.rocks/image?repo=Huynhthuongg/AGENTS.md)](https://github.com/Huynhthuongg/AGENTS.md/graphs/contributors)

</div>

</div>

---

## 📖 Documentation

- 📄 [**Product Specification**](docs/SPECIFICATION.md)
- 🏗️ [**Architecture Overview**](docs/ARCHITECTURE.md)
- 📝 [**API Documentation**](docs/API.md)
- 🔄 [**Changelog**](docs/CHANGELOG.md)

---

## 🐛 Issues & Feedback

Found a bug? Have a feature request? We'd love to hear from you!

- 🐛 [Report a Bug](https://github.com/Huynhthuongg/AGENTS.md/issues/new?template=bug_report.md)
- ✨ [Request a Feature](https://github.com/Huynhthuongg/AGENTS.md/issues/new?template=feature_request.md)
- 💬 [Start a Discussion](https://github.com/Huynhthuongg/AGENTS.md/discussions/new)

---

## 📄 License

This project is licensed under the **GNU Affero General Public License v3.0** (AGPL-3.0).

This means:
- ✅ You can use, modify, and distribute this software
- ✅ You must share your modifications if you use it
- ✅ You must include the original license

See [LICENSE](LICENSE) for full details.

---

<div align="center">

### 🚀 Ready to Get Started?

[📖 Read the Docs](docs/SPECIFICATION.md) • [💻 Clone the Repo](https://github.com/Huynhthuongg/AGENTS.md) • [⭐ Star on GitHub](https://github.com/Huynhthuongg/AGENTS.md)

**Made with ❤️ by [Huynhthuongg](https://github.com/Huynhthuongg)**

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" alt="colored line" width="100%">

![Python](https://img.shields.io/badge/Made%20with-Python-3776ab?style=flat-square&logo=python)
![Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red?style=flat-square)
![Open Source](https://img.shields.io/badge/Open%20Source-💚-brightgreen?style=flat-square)

</div>
