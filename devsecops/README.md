<div align="center">

# ⚙️ DevSecOps

### Security Pipeline Automation Platform

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Tools](https://img.shields.io/badge/tools-10+-purple)

**Automate security in your CI/CD pipeline** with SAST, SCA, DAST, and more.

[DevSecOps](https://github.com/0xvanguard/devsecops) • [Try It Live](#quick-start) • [Tools](#security-tools)

</div>

---

## ⚙️ What is DevSecOps?

DevSecOps is a **security pipeline automation platform** that integrates security testing into your CI/CD pipeline with SAST, SCA, DAST, and container scanning.

### Why DevSecOps?

| Without DevSecOps | With DevSecOps |
|-------------------|----------------|
| Security as afterthought | **Security by design** |
| Manual security testing | **Automated scanning** |
| Late discovery | **Early detection** |
| No compliance | **Built-in compliance** |

## 🛠️ Security Tools

| Tool | Type | Description |
|------|------|-------------|
| **SAST** | Static Analysis | Source code vulnerabilities |
| **SCA** | Software Composition | Dependency vulnerabilities |
| **DAST** | Dynamic Analysis | Runtime vulnerabilities |
| **Container** | Image Scanning | Container vulnerabilities |
| **Secrets** | Secret Detection | Hardcoded secrets |
| **IaC** | Infrastructure | Terraform/CloudFormation |

## 🚀 Quick Start

```bash
# Install
pip install devsecops

# Scan project
devsecops scan --project ./my-app --tools sast,sca
```

## 💻 Programmatic Usage

```python
from devsecops import SecurityPipeline

pipeline = SecurityPipeline()

# Run SAST scan
sast_results = pipeline.sast("./src")
print(f"SAST: {sast_results.vulnerabilities} vulnerabilities")

# Run SCA scan
sca_results = pipeline.sca("./requirements.txt")
print(f"SCA: {sca_results.vulnerabilities} vulnerabilities")

# Run DAST scan
dast_results = pipeline.dast("http://localhost:8080")
print(f"DAST: {dast_results.vulnerabilities} vulnerabilities")

# Generate report
pipeline.generate_report("security_report.pdf")
```

## 📊 Pipeline Integration

```python
from devsecops import CICDIntegration

# GitHub Actions
github = CICDIntegration("github")
github.add_step("sast", tools=["semgrep", "bandit"])
github.add_step("sca", tools=["safety", "snyk"])
github.add_step("dast", tools=["OWASP-ZAP"])
github.export(".github/workflows/security.yml")

# GitLab CI
gitlab = CICDIntegration("gitlab")
gitlab.add_step("security_scan")
gitlab.export(".gitlab-ci.yml")
```

## 📁 Project Structure

```
devsecops/
├── src/
│   ├── __init__.py
│   └── pipeline.py            # Core pipeline engine
├── data/
│   └── tools.json             # Tool configurations
├── examples/
│   └── quick_scan.py          # Getting started
└── README.md
```

## 📄 License

MIT License — Automate security.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/devsecops) • [🐛 Report Bug](https://github.com/0xvanguard/devsecops/issues)

</div>
