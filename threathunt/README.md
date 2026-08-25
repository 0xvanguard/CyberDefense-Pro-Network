# ThreatHunt

**Automated threat hunting with AI** — proactively search for hidden threats using behavioral analysis and anomaly detection.

## Features

- **Behavioral Analysis**: Detect anomalies in user/system behavior
- **MITRE ATT&CK Mapping**: Map findings to known TTPs
- **Log Correlation**: Correlate events across multiple sources
- **IoC Matching**: Check against threat intelligence feeds
- **AI-Powered**: ML models for pattern recognition

## Quick Start

```python
from threathunt import ThreatHunter

hunter = ThreatHunter(data_sources=["syslog", "dns", "netflow"])

# Run hunt
findings = hunter.hunt(timeframe="24h")

# Get MITRE mappings
for finding in findings:
    print(f"{finding.technique} — {finding.confidence}")

# Export
hunter.export(findings, format="stix")
```

## Hunt Queries

| Hunt | MITRE ID | Description |
|------|----------|-------------|
| lateral-movement | T1021 | Detect SMB/SSH lateral movement |
| persistence | T1053 | Detect scheduled task creation |
| exfiltration | T1048 | Detect unusual data transfers |
| credential-access | T1003 | Detect credential dumping |
| defense-evasion | T1027 | Detect obfuscated payloads |

## Author

[@0xvanguard](https://github.com/0xvanguard) — Security Researcher

## License

MIT
