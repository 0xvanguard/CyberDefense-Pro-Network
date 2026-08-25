"""
Commands: audit — scan repos for security issues.
"""

import os
import re
import subprocess
from pathlib import Path

from src.repos import REPOS, CATEGORIES
from utils.display import (
    C, print_header, print_subheader, print_success, print_error,
    print_warning, print_info, print_table, print_progress,
)


# Security patterns to scan for
SECURITY_PATTERNS = {
    "hardcoded_secret": {
        "pattern": r"""(?:api[_-]?key|secret[_-]?key|password|token|credential)\s*[=:]\s*['"][^'"]{8,}['"]""",
        "severity": "HIGH",
        "description": "Potential hardcoded secret",
        "fix": "Move to environment variable or secrets manager",
    },
    "insecure_http": {
        "pattern": r"""http://(?!localhost|127\.0\.0\.1|0\.0\.0\.0)""",
        "severity": "MEDIUM",
        "description": "Insecure HTTP URL (should use HTTPS)",
        "fix": "Use HTTPS for external URLs",
    },
    "eval_usage": {
        "pattern": r"""\beval\s*\(""",
        "severity": "HIGH",
        "description": "eval() usage — potential code injection",
        "fix": "Use JSON.parse() or safer alternatives",
    },
    "innerHTML": {
        "pattern": r"""\.innerHTML\s*=""",
        "severity": "MEDIUM",
        "description": "innerHTML assignment — potential XSS",
        "fix": "Use textContent or sanitize input",
    },
    "debug_mode": {
        "pattern": r"""(?:DEBUG|debug)\s*[=:]\s*(?:True|true|1)""",
        "severity": "LOW",
        "description": "Debug mode enabled",
        "fix": "Disable debug mode in production",
    },
    "weak_crypto": {
        "pattern": r"""\b(?:md5|sha1)\b(?!.*(?:hashlib|crypto))""",
        "severity": "MEDIUM",
        "description": "Weak cryptographic algorithm",
        "fix": "Use SHA-256 or stronger",
    },
    "sql_injection": {
        "pattern": r"""(?:execute|cursor\.execute)\s*\(\s*['"](%s|{|\+)""",
        "severity": "HIGH",
        "description": "Potential SQL injection",
        "fix": "Use parameterized queries",
    },
    "unsafe_deserialization": {
        "pattern": r"""pickle\.loads?\s*\(""",
        "severity": "HIGH",
        "description": "Unsafe deserialization with pickle",
        "fix": "Use JSON or msgpack instead of pickle",
    },
    "open_redirect": {
        "pattern": r"""(?:redirect|location)\s*[=:]\s*(?:request\.(?:args|form|GET))""",
        "severity": "MEDIUM",
        "description": "Potential open redirect",
        "fix": "Validate and whitelist redirect URLs",
    },
    "cors_wildcard": {
        "pattern": r"""(?:Access-Control-Allow-Origin|cors)\s*[=:]\s*['"]\*['"]""",
        "severity": "MEDIUM",
        "description": "CORS wildcard — allows any origin",
        "fix": "Restrict to specific allowed origins",
    },
}


def scan_file(filepath: str) -> list:
    """Scan a single file for security issues."""
    findings = []
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except (OSError, IOError):
        return findings

    for line_num, line in enumerate(lines, 1):
        for rule_id, rule in SECURITY_PATTERNS.items():
            if re.search(rule["pattern"], line, re.IGNORECASE):
                findings.append({
                    "file": filepath,
                    "line": line_num,
                    "rule": rule_id,
                    "severity": rule["severity"],
                    "description": rule["description"],
                    "fix": rule["fix"],
                    "code": line.strip()[:80],
                })

    return findings


def scan_directory(dirpath: str) -> list:
    """Recursively scan a directory."""
    findings = []
    skip_dirs = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build"}

    for root, dirs, files in os.walk(dirpath):
        dirs[:] = [d for d in dirs if d not in skip_dirs]

        for fname in files:
            ext = Path(fname).suffix.lower()
            if ext in (".py", ".js", ".ts", ".html", ".css", ".json",
                       ".yml", ".yaml", ".sh", ".md"):
                fpath = os.path.join(root, fname)
                findings.extend(scan_file(fpath))

    return findings


def cmd_audit(args):
    """Run security audit on all repos."""
    target = args.get("target", "all")
    severity_filter = args.get("severity", "").upper()

    print_header("🔍 Security Audit")

    targets = []
    if target == "all":
        targets = list(REPOS.keys())
    elif target in REPOS:
        targets = [target]
    elif target in CATEGORIES:
        targets = CATEGORIES[target]["repos"]
    else:
        print_error(f"Unknown target: {target}")
        print_info("Use: all, <category>, or <repo-name>")
        return

    all_findings = []
    total_files_scanned = 0

    for i, repo_name in enumerate(targets):
        repo_path = os.path.join(os.getcwd(), repo_name)
        if not os.path.isdir(repo_path):
            print_warning(f"Skipping {repo_name} (not found locally)")
            continue

        print_progress(i + 1, len(targets), f"Scanning {repo_name}...")

        findings = scan_directory(repo_path)
        for f in findings:
            f["repo"] = repo_name
        all_findings.extend(findings)

        # Count files scanned
        for root, dirs, files in os.walk(repo_path):
            dirs[:] = [d for d in dirs if d not in {".git", "node_modules", "__pycache__"}]
            total_files_scanned += len(files)

    # Filter by severity if specified
    if severity_filter:
        all_findings = [f for f in all_findings if f["severity"] == severity_filter]

    # Print results
    print_header("📋 Audit Results")
    print(f"  {C.DIM}Scanned: {total_files_scanned} files across {len(targets)} repos{C.RESET}\n")

    if not all_findings:
        print_success("No security issues found! 🎉")
        return

    # Group by severity
    by_severity = {"HIGH": [], "MEDIUM": [], "LOW": []}
    for f in all_findings:
        by_severity.setdefault(f["severity"], []).append(f)

    # Print summary
    high = len(by_severity.get("HIGH", []))
    med = len(by_severity.get("MEDIUM", []))
    low = len(by_severity.get("LOW", []))

    print(f"  {C.RED}🔴 HIGH:   {high}{C.RESET}")
    print(f"  {C.YELLOW}🟡 MEDIUM: {med}{C.RESET}")
    print(f"  {C.DIM}⚪ LOW:    {low}{C.RESET}\n")

    # Print detailed findings
    for severity in ["HIGH", "MEDIUM", "LOW"]:
        items = by_severity.get(severity, [])
        if not items:
            continue

        color = {"HIGH": C.RED, "MEDIUM": C.YELLOW, "LOW": C.DIM}[severity]
        print_subheader(f"{color}{severity} Findings{C.RESET}")

        for f in items:
            print(f"  {color}[{severity}]{C.RESET} {f['repo']}/{f['file']}:{f['line']}")
            print(f"    {C.DIM}{f['description']}{C.RESET}")
            print(f"    {C.CYAN}>{C.RESET} {f['code']}")
            print(f"    {C.GREEN}Fix:{C.RESET} {f['fix']}")
            print()

    # Print summary
    print_subheader("Summary")
    print(f"  Total findings: {C.BOLD}{len(all_findings)}{C.RESET}")
    print(f"  Files scanned:  {C.BOLD}{total_files_scanned}{C.RESET}")
    print(f"  Repos scanned:  {C.BOLD}{len(targets)}{C.RESET}")
