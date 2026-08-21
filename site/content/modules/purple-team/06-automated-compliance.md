---
title: "Módulo 06 — Automated Compliance Testing"
---

# 📋 Módulo 06 — Automated Compliance Testing

> **Objetivo Principal:** Automatizar la validación de controles de seguridad contra frameworks de cumplimiento (CIS, NIST, ISO 27001).

[![Nivel](https://img.shields.io/badge/Nivel-Intermedio--Avanzado-orange?style=flat-square)]()
[![Duración](https://img.shields.io/badge/Duración-1.5%20meses-blue?style=flat-square)]()

---

## 📋 Resumen del módulo

| Atributo | Detalle |
|----------|---------|
| **Pre-requisitos** | Módulos 01-05 completados |
| **Herramientas** | OpenSCAP, InSpec, Prowler, ScoutSuite |
| **Entregable** | Reporte de compliance automatizado |
| **Nivel** | Intermedio-Avanzado |

---

## 1. 🧠 Teoría: Compliance Automation

### ¿Por qué automatizar compliance?

| Enfoque Manual | Enfoque Automatizado |
|---------------|---------------------|
| Lento (semanas) | Rápido (minutos) |
| Propenso a errores | Consistente |
| Punto en el tiempo | Continuo |
| Caro | Escalable |

### Frameworks de cumplimiento

| Framework | Alcance | Herramientas |
|-----------|---------|--------------|
| **CIS Benchmark** | Hardening de sistemas | OpenSCAP, Ansible |
| **NIST CSF** | Seguridad general | Various |
| **ISO 27001** | Gestión de seguridad | Audit tools |
| **PCI DSS** | Tarjetas de pago | Custom scripts |
| **HIPAA** | Datos de salud | Compliance tools |

---

## 2. 🛠️ Herramientas

### OpenSCAP

```bash
# Instalar OpenSCAP
sudo apt install libopenscap8 scap-security-guide

# Listar perfiles disponibles
oscap info /usr/share/xml/scap/ssg/content/ssg-ubuntu2204-ds.xml

# Escanear sistema
sudo oscap xccdf eval \
  --profile cis \
  --results results.xml \
  --report report.html \
  /usr/share/xml/scap/ssg/content/ssg-ubuntu2204-ds.xml

# Ver reporte
firefox report.html
```

### InSpec (Chef)

```ruby
# Ejemplo de perfil InSpec
control 'sshd-01' do
  impact 1.0
  title 'SSH Protocol 2'
  desc 'SSH debe usar Protocol 2'
  
  describe sshd_config do
    its('Protocol') { should eq '2' }
  end
end

control 'sshd-02' do
  impact 1.0
  title 'SSH Root Login'
  desc 'SSH no debe permitir root login'
  
  describe sshd_config do
    its('PermitRootLogin') { should eq 'no' }
  end
end
```

### Prowler (AWS/Azure/GCP)

```bash
# Instalar Prowler
pip install prowler

# Ejecutar evaluación completa
prowler aws

# Evaluar contra framework específico
prowler aws --framework cis

# Generar reporte
prowler aws --output-format html
```

---

## 3. 🔬 Práctica Guiada: Evaluar Compliance

### Escenario: Evaluar servidor Linux contra CIS Benchmark

#### Paso 1: Ejecutar escaneo

```bash
# Con OpenSCAP
sudo oscap xccdf eval \
  --profile cis_level1_server \
  --results /tmp/results.xml \
  --report /tmp/report.html \
  /usr/share/xml/scap/ssg/content/ssg-ubuntu2204-ds.xml
```

#### Paso 2: Analizar resultados

```bash
# Extraer fallos
oscap info /tmp/results.xml | grep -A5 "fail"

# Generar CSV de resultados
oscap xccdf generate csv /tmp/results.xml > /tmp/results.csv
```

#### Paso 3: Remediación con Ansible

```yaml
# playbook.yml - Auto-remediación
- hosts: all
  become: yes
  tasks:
    - name: Configurar SSH según CIS
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '{{ item.regexp }}'
        line: '{{ item.line }}'
      loop:
        - { regexp: '^#?PermitRootLogin', line: 'PermitRootLogin no' }
        - { regexp: '^#?Protocol', line: 'Protocol 2' }
        - { regexp: '^#?MaxAuthTries', line: 'MaxAuthTries 3' }
```

---

## 4. 📊 Reporte de Compliance

### Ejemplo de reporte

```markdown
## Reporte de Compliance - Servidor WEB-01

### Resumen
- **Total controles:** 150
- **Cumplidos:** 120 (80%)
- **No cumplidos:** 25 (17%)
- **No aplicables:** 5 (3%)

### Hallazgos Críticos
1. SSH permite root login (CIS 5.2.10)
2. Passwords no expiran (CIS 5.4.1.1)
3. Firewall deshabilitado (CIS 3.5)

### Recomendaciones
1. Implementar hardening SSH
2. Configurar políticas de contraseña
3. Habilitar UFW
```

---

## 5. 🎯 Mini-Entregable

**Tarea:** Evaluar un sistema contra CIS Benchmark y crear:

1. **Escaneo** con OpenSCAP o InSpec
2. **Reporte** de hallazgos
3. **Playbook** de Ansible para remediación
4. **Verificación** post-remediación

---

## 6. 🔗 Recursos Adicionales

- [OpenSCAP](https://www.open-scap.org/)
- [InSpec](https://docs.chef.io/inspec/)
- [Prowler](https://github.com/prowler-cloud/prowler)

---

> **Siguiente paso:** Continúa con el [Módulo 07 — Threat Intelligence Driven Purple Team](../purple-team/07-threat-intelligence) para aprender a usar inteligencia de amenazas en ejercicios purple team.
