# ThreatSim ⚔️

> Generate realistic attack scenarios for security training and red team exercises.

## Overview

ThreatSim creates synthetic but realistic attack scenarios based on MITRE ATT&CK, helping teams practice incident response and detection.

## Quick Start

```bash
pip install threatsim
threatsim generate --framework mitre --scenario "ransomware"
threatsim play --scenario scenarios/apt29.json
```

## Features

- **MITRE ATT&CK Integration** — Maps to real techniques
- **Scenario Generator** — Create custom attack narratives
- **Difficulty Scaling** — Beginner to expert scenarios
- **Detection Validation** — Test if your SIEM catches the attacks
- **Export** — JSON, YAML, Sigma rules

## License

MIT
