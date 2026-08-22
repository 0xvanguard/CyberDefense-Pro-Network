# ⚠️ AUTH_STORED Pendiente de Actualizar — 22 de Agosto de 2026

---

## Estado

| Campo | Valor |
|-------|-------|
| **Prioridad** | CRÍTICA |
| **Estado** | ⏳ Pendiente |
| **Archivo** | `site/content/public/admin.html` |
| **Línea** | ~555 |

---

## Instrucciones

1. Abrir `site/content/public/generate-hash.html` en navegador
2. Generar hash con tu contraseña
3. Copiar la línea: `100000:SHA-256:salt:hash`
4. Reemplazar en admin.html:
```javascript
const AUTH_STORED = '100000:SHA-256:TU-SALT:TU-HASH';
```
5. Eliminar generate-hash.html y generate-hash-cli.js

---

*Documento guardado por Buffy — pendiente de completar*
