# Sesión: 23 Agosto 2026 - Privacidad y AI Safety

## 📋 Resumen de la sesión

### Temas tratados:

#### 1. **Modelo Buffy/Codebuff**
- Modelo ejecutándose: **Mimo 2.5** (mimo/mimo-v2.5)
- Plataforma: **Freebuff** (acceso gratuito a IA para código)
- No se entrenan con datos de usuarios individuales

#### 2. **Privacidad en GitHub Codespaces**
- **Retención de codespaces**: Configurada a **0 días** (eliminación inmediata)
- **Telemetría VS Code**: Desactivada
  - `telemetry.telemetryLevel`: "off"
  - `telemetry.feedback.enabled`: false
  - `telemetry.editStats.enabled`: false
- **GitHub Copilot Training**: Desactivado en GitHub Settings
- **Editor Preference**: VS Code Web o Desktop

#### 3. **Configuración de VS Code Desktop**
```json
{
  "telemetry.telemetryLevel": "off",
  "telemetry.feedback.enabled": false,
  "telemetry.editStats.enabled": false,
  "update.enableWindowsBackgroundUpdates": false,
  "extensions.autoUpdate": false,
  "search.followSymlinks": false
}
```

#### 4. **Seguridad de Modelos AI**
- DeepSeek R1: Modelo chino open source, menos guardrails
- Llama 3.1 405B: Modelo de Meta, open source, puede ser fine-tuned
- Ambos tienen preocupaciones de seguridad conocidas

#### 5. **Jailbreaking - Contexto**
- Se discutió jailbreaking desde perspectiva **educativa/defensiva**
- Se enfatizó importancia de enfoque **ético y responsable**
- No se proporcionaron técnicas específicas para uso malicioso

#### 6. **Proyecto GovLLM-Sentinel**
- **Nombre**: GovLLM-Sentinel
- **Repo**: https://github.com/0xvanguard/GovLLM-Sentinel
- **Descripción**: Framework de evaluación y hardening de LLMs para sector público
- **Contratos**: Firmados físicamente (en empresa, no se suben)
- **Dashboard**: Solo lectura para gobierno y comunidad
- **Estado**: ✅ Estructura completa subida a GitHub (29 archivos)

### Pendientes para próxima sesión:

#### GovLLM-Sentinel - Próximos pasos:
- [ ] Ejecutar primera evaluación real de un modelo
- [ ] Personalizar config/contrato-referencia.json con datos reales
- [ ] Conectar dashboard con datos de evaluación reales
- [ ] Implementar tests reales (no simulados)
- [ ] Deploy del dashboard en servidor gubernamental

#### Configuración pendiente:
- [ ] Verificar .copilotignore en repositorio
- [ ] Configurar Remote Tunnels para máximo control
- [ ] Revisar políticas de privacidad de Freebuff

---

## 📁 Archivos relevantes

- Configuración VS Code: `~/.config/Code/User/settings.json`
- Configuración GitHub: https://github.com/settings/copilot
- Codespaces retention: https://github.com/settings/codespaces

---

## 🔗 Recursos

- [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)
- [Codespaces Retention Policy](https://docs.github.com/en/enterprise-cloud@latest/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces)
- [VS Code Telemetry](https://code.visualstudio.com/docs/configure/telemetry)
- [HarmBench Research](https://arxiv.org/abs/2402.04249)

---

*Última actualización: 23 Agosto 2026*
