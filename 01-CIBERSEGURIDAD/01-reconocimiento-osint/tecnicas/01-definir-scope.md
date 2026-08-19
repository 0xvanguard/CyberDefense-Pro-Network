# Técnica 01 — Cómo definir un buen scope en un pentest

> **Objetivo:** ayudarte a escribir y entender scopes claros, realistas y legales para ejercicios de reconocimiento y pentesting.

Un buen scope protege al cliente, al equipo técnico y a ti mismo. Es la diferencia entre un ejercicio profesional y "jugar a hackear".

---

## 1. ¿Qué es el scope?

En un pentest, el **scope** (alcance) es el acuerdo explícito sobre **qué está dentro** y **qué está fuera** de la evaluación.

Responde a preguntas como:

- ¿Qué dominios, subdominios y aplicaciones se pueden evaluar?
- ¿Qué rangos de IP están autorizados?
- ¿Qué tipo de pruebas están permitidas (solo recon, explotación limitada, post-explotación, etc.)?
- ¿Qué está prohibido (por ejemplo, DoS, fuerza bruta, phishing a clientes reales)?

Sin un scope claro, cualquier acción técnica puede ser ambigua o incluso ilegal.

---

## 2. Componentes básicos de un scope profesional

Un scope típico en un contrato o SOW (Statement of Work) suele incluir al menos:

1. **Objetivo del ejercicio**  
   - Ejemplo: "Evaluar la exposición externa de la infraestructura web de NovaPay Labs".

2. **Activos dentro de alcance**  
   - Dominios (y subdominios, si aplica).  
   - Rangos de IP.  
   - Aplicaciones específicas (por ejemplo, "portal de merchants", "API pública v1").

3. **Tipos de pruebas permitidas**  
   - Solo reconocimiento pasivo.  
   - Reconocimiento + explotación controlada.  
   - Inclusión o exclusión de ingeniería social, phishing, etc.

4. **Restricciones y prohibiciones**  
   - Nada de DoS ni pruebas de alta carga.  
   - Nada de fuerza bruta masiva de credenciales.  
   - Nada de acceso a datos de producción sensibles (o reglas muy específicas de manejo de datos).

5. **Ventanas de tiempo o condiciones especiales**  
   - Horarios en los que se pueden hacer pruebas.  
   - Reglas sobre interrupción del test si se detecta impacto.

En los labs de la plataforma usamos versiones simplificadas de esto, pero la lógica es la misma.

---

## 3. Ejemplo de scope (versión resumida)

Para el Lab 01 de NovaPay Labs, un scope resumido podría verse así:

> **Objetivo:** Mapear la superficie de ataque de NovaPay Labs en el entorno de laboratorio, sin explotación de vulnerabilidades.
>
> **Dentro de alcance:**  
> - Dominio simulado: `novapay-labs.local`.  
> - Rango de red del lab: `10.20.30.0/24`.  
> - Actividades: reconocimiento pasivo y activo controlado (host discovery, enumeración de puertos/servicios) dentro del rango autorizado.
>
> **Fuera de alcance:**  
> - Cualquier IP fuera de `10.20.30.0/24`.  
> - Ataques de denegación de servicio, fuerza bruta, explotación de vulnerabilidades.  
> - Acceso a datos de producción reales.

Esto ya sería suficiente como clause de alcance en un documento interno o en un anexo técnico.

---

## 4. Checklist rápida para definir scope

Usa esta lista cuando redactes o revises un scope:

- [ ] ¿Está claro el **objetivo** del ejercicio? (qué se quiere lograr)
- [ ] ¿Están listados los **dominios** incluidos? (y subdominios, si aplica)
- [ ] ¿Están definidos los **rangos de IP** autorizados?
- [ ] ¿Se indica qué **tipos de pruebas** están permitidas? (recon, explotación, post-explotación)
- [ ] ¿Se documenta explícitamente qué está **fuera de alcance**?
- [ ] ¿Hay reglas sobre **acciones prohibidas** (DoS, fuerza bruta, ingeniería social real)?
- [ ] ¿Se mencionan condiciones especiales de tiempo/impacto, si son relevantes?

Si alguna casilla se queda en blanco, el scope está incompleto.

---

## 5. Cómo aplicar esto en tus informes y labs

En tus informes para la plataforma (por ejemplo, `informe-recon-novapay-labs.md`):

- Siempre incluye una sección de **Scope y limitaciones**.  
- Copia o adapta el scope que se da en el lab, pero escríbelo con tus propias palabras para practicar.  
- Si en un futuro lab hay alguna ambigüedad, **anótala** como nota: en la vida real, sería algo que discutirías con el cliente.

Practicar scopes claros ahora hará que cuando llegues a módulos de pentesting, Red Team o consultoría, ya tengas el hábito de trabajar de forma profesional y defensible.

---

**[⬅ Volver al README del módulo](../README.md)**