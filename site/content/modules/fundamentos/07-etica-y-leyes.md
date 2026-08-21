---
title: "07 — Ética y leyes: lo que todo profesional debe saber"
---

# 07 — Ética y leyes: lo que todo profesional debe saber

> 🎯 **Objetivo:** que entiendas la línea entre investigación legítima y delito, y por qué la ética no es opcional.

## 1. La regla de oro del hacking ético

> **Si no tienes permiso por escrito, no lo hagas.**

No importa que la vulnerabilidad sea obvia. No importa que la empresa sea negligente. No importa que tu intención sea ayudar. **Sin autorización, es delito** en casi todas las jurisdicciones.

## 2. Por qué existe el hacking ético

Porque las empresas necesitan a gente que piense como el atacante para encontrar huecos **antes** de que los exploten. Pero necesitan garantías legales: si el "hacker bueno" hace algo sin permiso y causa daño real, ¿quién responde?

Por eso existe:
- **Contrato / scope** — autorizar exactamente qué puedes probar.
- **Reglas de engagement** — qué métodos están permitidos, cuáles no (¿DoS? ¿ingeniería social? ¿datos reales?).
- **Disclosure coordinado** — aviso al fabricante antes de publicar.
- **NDA** — no divulgar lo que veas.

## 3. Divulgación responsable (Coordinated Disclosure)

El ciclo correcto cuando encuentras algo:

1. **Reportas** al fabricante (o a través de un bug bounty) con detalle técnico suficiente para reproducir.
2. **Esperas** un plazo razonable (típico: 90 días) a que parchear.
3. **Si parchean**, publicas los detalles reconociendo al fabricante.
4. **Si no parchean** y el riesgo es alto, publiques con aviso y un plazo mayor.

**NO:**
- ❌ Vender un 0-day en mercados negros (sí, existen, pero no es profesional).
- ❌ Exigir rescate ("te digo el bug si me pagas").
- ❌ Amenazar con publicarlo.
- ❌ Probar el bug en sistemas reales sin autorización.

## 4. Lo que SÍ puedes hacer sin pedir permiso

- Auditar tu propio equipo o tu propio código.
- Hacer cosas en **laboratorios aislados** (HackTheBox, TryHackMe, Docker labs propios).
- Analizar código **open source** que ya está publicado.
- Leer CVE/Changelog público y estudiarlos.
- Participar en **CTFs** (Capture The Flag) expresamente diseñados para practicar.

## 5. Marco legal según país (resumen general)

> ⚠️ No soy abogado. Esto es solo un resumen cultural — verifica siempre la ley local.

### España 🇪🇸
- **Código Penal** art. 197 (acceso no autorizado a datos), 264 (daño informático), 264 bis (sabotaje).
- Ley de Protección de Datos (LOPD-GDD) y RGPD europeo.
- Es delito incluso acceder sin causar daño visible.

### México 🇲🇽
- **Código Penal Federal** art. 211 bis 1-4 (delitos informáticos).
- Ley Federal de Protección de Datos Personales.

### Argentina 🇦🇷
- **Código Penal** art. 153-157 (delitos信息技术).
- Ley 25.326 de Protección de Datos.

### Colombia 🇨🇴
- Ley 1273 de 2009 (delitos informáticos).

### Chile 🇨🇱
- Ley 19.223 (delitosinformáticos).

### EE.UU. 🇺🇸
- **CFAA** (Computer Fraud and Abuse Act) — muy agresivo, multas fuertes.
- **DMCA** — tiene excepciones de seguridad research eludiendo DRM.
- Algunos estados tienen leyes adicionales.

> 📂 Documentos marco y compliance en [`02-SEGURIDAD-INFORMACION/06-compliance-normativas/`](../02-SEGURIDAD-INFORMACION/06-compliance-normativas/).

## 6. El "qué NO hacer" en tu trabajo

- 🔒 No uses accesos obtenidos en pruebas para beneficio propio.
- 🔒 No reveles vulnerabilidades públicamente sin avisar al fabricante primero.
- 🔒 No pruebes DoS en producción sin autorización explícita (puede tumbar negocio real).
- 🔒 No hagas pruebas de ingeniería social si no están en el scope escrito.
- 🔒 No borres logs (a menos que sea parte autorizada de un test).
- 🔒 No mientas sobre lo que hiciste — la trazabilidad es tu mejor defensa.

## 7. El "qué SÍ hacer" en tu trabajo

- ✍️ **Documenta TODO.** Tu trabajo sin evidencia no vale.
- 🤝 **Comunica hallazgo crítico** al CISO y al equipo afectado rápido.
- 🧪 **Prueba en sandbox primero** todo lo que pueda romper.
- 📜 **Mantén contrato firmado** y guárdalo años.
- 🗑️ **Borra datos sensibles** que recopiles en pruebas una vez terminado.
- 👥 **Respeta a otros equipos** — un pentester arrogante no dura.

## 8. Privacidad: GDPR / RGPD / LOPD

Si manejas datos personales, aplica todo esto:

- **Minimización**: recopila lo mínimo necesario.
- **Propósito claro**: define para qué los usas antes de pedirlos.
- **Consentimiento informado**: explica qué harás y obtén permiso.
- **Retención limitada**: borra cuando ya no los necesites.
- **Transparencia**: ten un registro de actividades de tratamiento.
- **Notificación de brecha**: si hay fuga, notifica a la autoridad en 72h (en la UE).

## 9. Cuando algo sale mal — qué hacer

Si en una prueba autorizada rompes algo:
1. **Para inmediatamente** y documenta lo que pasó.
2. **Avisa al cliente** sin maquillar.
3. **Trabaja con el equipo técnico** para resolver.
4. **Documenta la lección aprendida** en un postmortem.
5. **Mejora tu proceso** para que no vuelva a pasar.

> La honestidad en este momento define tu carrera más que cualquier certificación.

## 10. Recursos recomendados

- **EC-Council Code of Ethics**
- **(ISC)² Code of Ethics**
- **SANS Institute** — su ética es referencia
- **OWASP Code of Ethics**
- **[Chaos Computer Club manifesto](https://www.ccc.de/en/club/manifesto)** si te interesa la postura europea

## ✏️ Ejercicios / reflexiones

1. **Lee el contrato** del último servicio que aceptaste sin leer (probablemente sea un banco o una app). Fíjate qué dice sobre tus datos.
2. **Pregúntate:** si encontraras mañana una vulnerabilidad crítica en el banco donde tienes tu cuenta, ¿qué harías? Escribe el procedimiento en 5 pasos.
3. **Estudia un caso:** busca "vulnerabilidad reportada" en las noticias. Mira cómo reaccionó la empresa. ¿Fue coordinada?
4. **Anota:** redacta tu propio "código de ética personal" en 5 frases. Te servirá para el CV y para guiar tus decisiones.

## 📌 Dónde profundizar

| Tema | Carpeta |
|---|---|
| GRC / Compliance | [`02-SEGURIDAD-INFORMACION/`](../02-SEGURIDAD-INFORMACION/) |
| CISO role | [`02-SEGURIDAD-INFORMACION/ciso/`](../02-SEGURIDAD-INFORMACION/ciso/) |
| Privacy / DPO | [`02-SEGURIDAD-INFORMACION/data-protection-officer/`](../02-SEGURIDAD-INFORMACION/data-protection-officer/) |
| Auditor | [`02-SEGURIDAD-INFORMACION/auditor-seguridad/`](../02-SEGURIDAD-INFORMACION/auditor-seguridad/) |

> ⏭️ **Siguiente:** [`08-herramientas-esenciales.md`](./08-herramientas-esenciales.md) — las herramientas más comunes que verás en tu día a día.
