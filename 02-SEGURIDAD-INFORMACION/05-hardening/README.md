# 🔒 Módulo 05 — Hardening de Sistemas y Redes

> **Objetivo principal:** Aprender a endurecer (hardening) sistemas operativos, servicios y redes para reducir la superficie de ataque y cumplir con marcos de referencia como CIS Benchmarks, DISA STIGs y NIST 800-123.

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio-blue?style=flat-square)]()
[![Enfoque](https://img.shields.io/badge/Enfoque-Blue%20Team%20%7C%20DevSecOps-green?style=flat-square)]()
[![Frameworks](https://img.shields.io/badge/Frameworks-CIS%20%7C%20DISA%20STIG%20%7C%20NIST-orange?style=flat-square)]()
[![Lab](https://img.shields.io/badge/Lab-Docker%20%7C%20VM-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|---|---|
| 🏷️ **Nivel** | Intermedio |
| ⏱️ **Duración estimada** | 3–4 semanas |
| 🎯 **Resultado esperado** | Ser capaz de endurecer servidores Linux/Windows y configuraciones de red siguiendo estándares CIS |
| 🧪 **Práctica verificable** | Scripts de hardening, auditorías con Lynis/OpenSCAP, before/after reports |
| 🗂️ **Portafolio** | Scripts de hardening documentados + reportes de auditoría |
| 🔗 **Requiere** | Fundamentos de Linux/Windows, redes básicas |
| 🔗 **Conduce a** | DevSecOps, Compliance, Security Engineering |

---

## 🎯 Qué aprenderás

- [ ] Aplicar CIS Benchmarks a servidores Ubuntu/Windows
- [ ] Configurar firewalls (iptables/nftables, Windows Firewall)
- [ ] Endurecer servicios comunes (SSH, Apache, Nginx, IIS)
- [ ] Implementar hardening de red (segmentación, ACLs, VLANs)
- [ ] Auditar configuraciones con herramientas automatizadas
- [ ] Documentar el proceso de hardening para compliance

---

## 🗂️ Estructura del módulo

```
05-hardening/
├── README.md                    ← Este archivo
├── linux/
│   ├── README.md               ← Hardening Linux general
│   ├── hardening_ubuntu.sh     ← Script de hardening Ubuntu
│   ├── ssh-hardening.md        ← Hardening SSH
│   └── audit-lynis.md          ← Auditoría con Lynis
├── windows/
│   ├── README.md               ← Hardening Windows Server
│   ├── gpo-hardening.md        ← Group Policy Objects
│   └── openscap.md             ← Auditoría con OpenSCAP
├── redes/
│   ├── README.md               ← Hardening de red
│   ├── firewall-iptables.md    ← iptables/nftables
│   ├── segmentation.md         ← Segmentación de red
│   └── acl-switches.md         ← ACLs en switches
└── portafolio/
    └── template-hardening.md   ← Plantilla de reporte
```

---

## 📚 Contenido del módulo

### FASE 1 — Hardening Linux (Semana 1)

#### 1.1 Principios de Hardening
El hardening es el proceso de reducir la superficie de ataque de un sistema eliminando servicios innecesarios, aplicando parches, configurando controles de acceso y siguiendo estándares de la industria.

**Pilares del hardening:**
- **Mínimo privilegio:** Solo lo necesario para funcionar
- **Defensa en profundidad:** Múltiples capas de controles
- **Seguridad por defecto:** Todo bloqueado excepto lo explícitamente permitido
- **Auditoría continua:** Monitoreo y verificación periódica

#### 1.2 CIS Benchmarks
Los CIS Benchmarks son guías de configuración segura desarrolladas por el Center for Internet Security. Cada benchmark incluye:
- Configuraciones recomendadas con nivel (Level 1 / Level 2)
- Justificación de cada configuración
- Impacto en funcionalidad
- Métodos de verificación

**Recursos:**
- [CIS Ubuntu Linux Benchmark](https://www.cisecurity.org/cis-benchmarks/cis-ubuntu-linux)
- [CIS Microsoft Windows Benchmark](https://www.cisecurity.org/cis-benchmarks/cis-microsoft-windows)
- [CIS Docker Benchmark](https://www.cisecurity.org/cis-benchmarks/cis-docker)

---

### FASE 2 — Hardening Windows (Semana 2)

#### 2.1 Group Policy Objects (GPO)
Las GPOs son el mecanismo central de hardening en entornos Windows/Active Directory:

| Configuración | GPO Setting | Impacto |
|---|---|---|
| Contraseñas complejas | Password Policy | Previene fuerza bruta |
| Bloqueo de cuenta | Account Lockout | Previene brute force |
| Auditoría de eventos | Advanced Audit Policy | Visibilidad de actividad |
| Firewalls | Windows Firewall GPO | Control de tráfico |
| Software Restriction | AppLocker/WDAC | Previene malware |

#### 2.2 Windows Defender Exploit Guard
- **ASLR:** Address Space Layout Randomization
- **DEP:** Data Execution Prevention
- **CFG:** Control Flow Guard
- **Exploit Protection:** Protecciones por proceso

---

### FASE 3 — Hardening de Red (Semana 3)

#### 3.1 Segmentación de Red
```
Internet → DMZ (Web Servers)
         → VLAN 10 (Servidores de Aplicación)
         → VLAN 20 (Base de Datos)
         → VLAN 30 (Admin/Management)
         → VLAN 40 (Usuarios)
```

**Reglas de segmentación:**
- DMZ solo puede comunicarse con Internet y VLAN 10
- VLAN 20 (DB) solo acepta conexiones desde VLAN 10
- VLAN 30 (Admin) requiere VPN + MFA
- VLAN 40 (Usuarios) tiene acceso limitado a VLAN 10

#### 3.2 Firewall Configuration
```bash
# iptables — Política por defecto: denegar todo
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Permitir solo lo necesario
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -s 10.0.30.0/24 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```

---

### FASE 4 — Auditoría y Verificación (Semana 4)

#### 4.1 Lynis (Linux)
```bash
# Instalar y ejecutar auditoría
sudo apt install lynis
sudo lynis audit system

# Resultado esperado: Hardening index > 70
[+] Hardening index : 78 [#############       ]
```

#### 4.2 OpenSCAP (Multiplataforma)
```bash
# Evaluar contra CIS Benchmark
oscap xccdf eval --profile cis --results results.xml \
  /usr/share/xml/scap/ssg/content/ssg-ubuntu2204-ds.xml
```

---

## 🧪 Laboratorios

| Lab | Descripción | Nivel |
|-----|-------------|-------|
| `lab-01` | Hardening SSH + firewall en Ubuntu | Básico |
| `lab-02` | GPO hardening en Windows Server | Intermedio |
| `lab-03` | Segmentación de red con VLANs | Intermedio |
| `lab-04` | Auditoría completa con Lynis + OpenSCAP | Avanzado |

---

## 📊 Métricas de éxito

| Métrica | Objetivo |
|---------|----------|
| Hardening index (Lynis) | > 75 |
| CIS Benchmark compliance | > 80% Level 1 |
| Servicios innecesarios | 0 expuestos |
| Firewall policy | DROP por defecto |
| Documentación | Script + reporte por cada OS |

---

## 🔗 Referencias

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [DISA STIGs](https://public.cyber.mil/stigs/)
- [NIST 800-123 Guide to General Server Security](https://csrc.nist.gov/publications/detail/sp/800-123/final)
- [NIST 800-111 Guide to Storage Encryption](https://csrc.nist.gov/publications/detail/sp/800-111/final)
- [Lynis - Security Auditing Tool](https://cisofy.com/lynis/)
- [OpenSCAP](https://www.open-scap.org/)

---

*Última actualización: Agosto 2026*
*CyberDefense-Pro-Network — Aprende haciendo. Demuestra con evidencia.*
