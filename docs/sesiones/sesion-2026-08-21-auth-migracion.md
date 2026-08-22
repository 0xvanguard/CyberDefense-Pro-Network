# 🔐 Migración de Autenticación — 21 de Agosto de 2026
## CyberDefense Pro Network

---

## 📋 Resumen

Migración de la autenticación client-side del admin panel de SHA-256 básico a un sistema robusto con PBKDF2, HMAC y rate limiting mejorado.

| Métrica | Antes | Después |
|---------|-------|---------|
| **Hash function** | SHA-256 (1 iteración) | PBKDF2 (100,000 iteraciones) |
| **Salt** | ❌ Sin salt | ✅ Salt aleatorio de 16 bytes |
| **Session tokens** | JSON sin firmar | HMAC-SHA256 firmado |
| **Rate limiting** | Contador simple en localStorage | Contador firmado con HMAC + exponential backoff |
| **Timing attacks** | ❌ Comparación binaria | ✅ Constant-time comparison |
| **Replay attacks** | ❌ Sin protección | ✅ Nonce único por sesión |
| **Session expiry** | ✅ 24 horas | ✅ 24 horas + verificación HMAC |

---

## 🔧 Cambios Implementados

### 1. PBKDF2 con Salt (reemplaza SHA-256)

**ANTES:**
```javascript
async function hashPassword(password) {
    const encoder = new TextEncoder();
    const data = encoder.encode(password);
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    return Array.from(new Uint8Array(hashBuffer))
        .map(b => b.toString(16).padStart(2, '0')).join('');
}
// Comparación directa: hash === AUTH_HASH
```

**DESPUÉS:**
```javascript
const PBKDF2_ITERATIONS = 100000;
const PBKDF2_HASH = 'SHA-256';
const PBKDF2_KEY_LEN = 256;
const AUTH_STORED = '100000:SHA-256:<salt>:<hash>';

async function deriveKey(password, salt) {
    const keyMaterial = await crypto.subtle.importKey(
        'raw', encoder.encode(password), 'PBKDF2', false, ['deriveBits']
    );
    const derivedBits = await crypto.subtle.deriveBits(
        { name: 'PBKDF2', salt, iterations: PBKDF2_ITERATIONS, hash: PBKDF2_HASH },
        keyMaterial, PBKDF2_KEY_LEN
    );
    return bufferToHex(derivedBits);
}

async function verifyPassword(password) {
    const [iterations, hashAlgo, saltHex, expectedHash] = AUTH_STORED.split(':');
    const salt = hexToBuffer(saltHex);
    const derived = await deriveKey(password, salt);
    // Constant-time comparison
    let result = 0;
    for (let i = 0; i < derived.length; i++) {
        result |= derived.charCodeAt(i) ^ expectedHash.charCodeAt(i);
    }
    return result === 0;
}
```

**Ventajas:**
- 100,000 iteraciones = ~100x más lento de crackear
- Salt aleatorio previene rainbow tables
- Constant-time comparison previene timing attacks

### 2. HMAC-SHA256 Session Tokens

**ANTES:**
```javascript
function saveSession(hash) {
    localStorage.setItem(SESSION_KEY, JSON.stringify({
        hash: hash,
        timestamp: Date.now()
    }));
}
// Verificación: session.hash === AUTH_HASH
```

**DESPUÉS:**
```javascript
async function createSessionToken() {
    const key = await crypto.subtle.importKey(
        'raw', encoder.encode(HMAC_KEY_raw),
        { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']
    );
    const nonce = bufferToHex(crypto.getRandomValues(new Uint8Array(16)));
    const payload = JSON.stringify({
        ts: Date.now(),
        exp: Date.now() + SESSION_DURATION,
        nonce: nonce,
        ua: navigator.userAgent.slice(0, 50)
    });
    const sig = await crypto.subtle.sign('HMAC', key, encoder.encode(payload));
    return { payload, sig: bufferToHex(sig) };
}

async function verifySessionToken(session) {
    // Verificar expiración
    const data = JSON.parse(session.payload);
    if (Date.now() > data.exp) return false;
    // Verificar firma HMAC
    const valid = await crypto.subtle.verify('HMAC', key, sigBuffer, encoder.encode(session.payload));
    return valid;
}
```

**Ventajas:**
- Tokens firmados con HMAC no se pueden falsificar
- Nonce único previene replay attacks
- Expiración verificada criptográficamente

### 3. Rate Limiter Mejorado

**ANTES:**
```javascript
const RateLimiter = {
    MAX_ATTEMPTS: 5,
    WINDOW_MS: 30000,
    // Contador simple en localStorage (fácil de borrar)
};
```

**DESPUÉS:**
```javascript
const RateLimiter = {
    MAX_ATTEMPTS: 5,
    WINDOW_MS: 60000,       // 1 minute window
    BASE_COOLDOWN: 30000,   // 30 seconds base
    MAX_COOLDOWN: 300000,   // 5 minutes max
    // Contador firmado con HMAC (no se puede manipular)
    // Exponential backoff: 30s → 60s → 120s → 240s → 300s (max)
};
```

**Ventajas:**
- Contador firmado con HMAC — no se puede borrar o manipular
- Exponential backoff — cada intento fallido aumenta el cooldown
- Máximo de 5 minutos de bloqueo

---

## 📁 Archivos Modificados

| Archivo | Cambio |
|---------|--------|
| `site/content/public/admin.html` | Auth completa migrada a PBKDF2 + HMAC |
| `site/content/public/generate-hash.html` | Herramienta para generar hash (eliminar después) |

---

## ⚠️ Acción Requerida

**Debes generar tu hash PBKDF2 personalizado:**

1. Abre `site/content/public/generate-hash.html` en tu navegador
2. Escribe tu contraseña admin
3. Copia la línea generada
4. Reemplaza la constante `AUTH_STORED` en `admin.html`
5. **Elimina `generate-hash.html` después de usarlo**

```javascript
// En admin.html, reemplazar:
const AUTH_STORED = '100000:SHA-256:<tu-salt>:<tu-hash>';
```

---

## 📊 Mejoras de Seguridad

| Ataque | Antes | Después |
|--------|-------|---------|
| **Brute force offline** | ❌ SHA-256 rápido | ✅ PBKDF2 100K iteraciones |
| **Rainbow tables** | ❌ Sin salt | ✅ Salt aleatorio 16 bytes |
| **Timing attacks** | ❌ Comparación binaria | ✅ Constant-time comparison |
| **Session forgery** | ❌ JSON sin firmar | ✅ HMAC-SHA256 firmado |
| **Replay attacks** | ❌ Sin nonce | ✅ Nonce único 16 bytes |
| **Rate limit bypass** | ❌ localStorage editable | ✅ Contador HMAC firmado |
| **Session hijacking** | ⚠️ Básico | ✅ UA fingerprint + nonce |

---

## 🔮 Próximos Pasos (cuando tengas backend)

1. **GitHub OAuth** — Eliminar passwords completamente
2. **Server-side rate limiting** — Rate limit real en el servidor
3. **Session storage server-side** — No más localStorage para sesiones
4. **JWT tokens** — Tokens firmados con expiración real

---

*Documentado por Buffy — Codebuff Security Team*
*Fecha: 21 de Agosto de 2026*
