# 🎣 Playbook — Respuesta a Phishing (compromiso de credenciales)

> **Severidad inicial:** S2 (alto) si hay credenciales comprometidas; S3 si solo fue clic.
> **Marco:** NIST SP 800-61 · **Objetivo:** contener, identificar alcance y erradicar un ataque de phishing.

---

## 📋 Resumen del escenario

Un usuario reporta (o el SIEM detecta) un correo de phishing. El flujo típico de ataque:

```
Correo malicioso → usuario hace clic → landing falsa → introduce credenciales
        ↓                                          ↓
  descarga malware                          credenciales robadas → login no autorizado
```

---

## Fase 0 — Preparation (qué tener listo ANTES)

- [ ] Plantilla de reporte de usuario (botón "Reportar phishing" en el cliente de correo).
- [ ] Sandbox para URLs/adjuntos (Any.Run, Hybrid Analysis, VirusTotal).
- [ ] Acceso al SIEM/EDR y al panel del correo (Microsoft 365 / Google Workspace).
- [ ] Procedimiento de reset de contraseñas y revocación de sesiones.
- [ ] Lista de dueños por sistema/tenant.

---

## Fase 1 — Detection & Triage

### 1.1 Confirmar el correo

Inspecciona las **cabeceras** (no confíes en el "From" visible):

```bash
# Extraer cabeceras completas (en un .eml)
cat correo.eml | head -50
```

Revisa:

| Campo | Qué buscar |
|---|---|
| `From` / `Return-Path` | Dominio que no coincide (typosquatting) |
| `Received` | Origen real del correo (SPF/DKIM fallaron?) |
| `Authentication-Results` | `spf=fail`, `dkim=fail`, `dmarc=fail` |
| Enlaces | URL de phishing (dominio recién registrado, acortada) |
| Adjuntos | `.html`, `.exe`, `.iso`, `.docm` (macros) |

### 1.2 Verificar en la sandbox

```text
1. Extraer URLs y adjuntos SIN abrirlos en producción.
2. Subir a VirusTotal / Any.Run / Hybrid Analysis.
3. Anotar: hashes (sha256), IPs, dominios, verdict.
```

### 1.3 Responder la pregunta clave: **¿el usuario introdujo credenciales?**

- Si **solo hizo clic** → S3, monitorizar.
- Si **introdujo credenciales** → S2, aplicar fase 2 inmediatamente.

---

## Fase 2 — Containment (contención)

Acciones **inmediatas** (en este orden):

### 2.1 Revocar sesiones y resetear credenciales

```text
1. Forzar reset de password del usuario afectado.
2. Revocar todas las sesiones activas (MFA re-registro si aplica).
3. Revocar tokens/OAuth de la cuenta.
```

Microsoft 365 (ejemplo PowerShell):

```powershell
# Revocar sesiones de un usuario
Revoke-AzureADUserAllRefreshToken -ObjectId "usuario@corp.com"
```

### 2.2 Bloquear IOCs

```text
1. Bloquear el dominio/URL del remitente en el filtro de correo.
2. Bloquear IPs/hashes en EDR/firewall.
3. Purgar el correo de TODOS los buzones (no solo el reportado).
```

### 2.3 Buscar el blast radius (¿a quién más llegó?)

```text
Query en el SIEM/correo: 
  - ¿El mismo remitente envió a otros usuarios?
  - ¿Otros usuarios hicieron clic en la misma URL?
  - ¿Hay logins anómalos posteriores desde IPs externas?
```

---

## Fase 3 — Eradication (erradicación)

### 3.1 Eliminar persistencia

```text
1. Escanear el equipo del usuario con EDR (full scan).
2. Si hay malware: aislar el host y analizar (ver forense).
3. Buscar reglas de reenvío de correo creadas por el atacante.
4. Revisar MFA: ¿el atacante registró un dispositivo/factor nuevo?
```

### 3.2 Buscar reglas de reenvío maliciosas (Microsoft 365)

```powershell
# Reglas de inbox recién creadas (posible auto-reexpedición)
Get-InboxRule -Mailbox usuario@corp.com | Where-Object {$_.ForwardTo -or $_.RedirectTo}
```

---

## Fase 4 — Recovery (recuperación)

```text
1. Restaurar acceso al usuario (credenciales nuevas + MFA).
2. Confirmar que el buzón está limpio (sin reglas/reenvíos).
3. Reintegrar el host tras verificar que está limpio.
4. Monitoreo reforzado durante 30 días (cuenta y host).
```

---

## Fase 5 — Post-Incident (lecciones aprendidas)

Documentar (formato blameless):

1. ¿Cómo entró el correo? (SPF/DKIM/DMARC, filtro)
2. ¿Por qué el usuario cayó? (urgencia, suplantación de jefe, etc.)
3. ¿Qué detección falló o tardó? (¿no había alerta de login anómalo?)
4. **Acciones correctivas** con dueño y fecha:
   - [ ] Configurar/endurecer SPF, DKIM y DMARC (p=reject).
   - [ ] Regla de detección: login exitoso desde IP no habitual (T1078).
   - [ ] Capacitación anti-phishing al equipo.
   - [ ] Simulacros de phishing periódicos (GoPhish).

---

## 🧪 Cómo practicar este playbook

1. Monta un simulacro con **GoPhish** contra un tenant de prueba propio.
2. Genera la landing y captura el "clic + credenciales".
3. Ejecuta este playbook de punta a punta sobre el incidente simulado.
4. Documenta la timeline y el post-mortem (ver [`TEMPLATE-ficha-evento-soc.md`](../../../03-blue-team-defensa/portafolio/TEMPLATE-ficha-evento-soc.md)).

---

## Referencias

- [NIST SP 800-61 Rev. 2](https://csrc.nist.gov/pubs/sp/800/61/r2/final)
- [CISA Phishing Guidance](https://www.cisa.gov/stopransomware/avoids-phishing)
- [GoPhish (simulacros)](https://getgophish.com/)

---

**[← Metodología IR](../incident-response/README.md)** · **[← Volver al módulo SOC](../README.md)**
