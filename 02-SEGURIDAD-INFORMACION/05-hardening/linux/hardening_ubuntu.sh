#!/usr/bin/env bash
# =============================================================================
# hardening_ubuntu.sh — Hardening básico de Ubuntu Server (basado en CIS)
#
# Uso: ejecutar como ROOT en un sistema de PRUEBAS:
#     sudo bash hardening_ubuntu.sh
#     sudo bash hardening_ubuntu.sh --apply
#
# Por defecto muestra las acciones en modo "demo" (--dry-run) sin aplicar cambios.
# Solo aplica cuando se pasa --apply. Es responsabilidad del operador probarlo
# en un entorno controlado antes de producción.
# =============================================================================

set -uo pipefail

APPLY=false
[ "${1:-}" = "--apply" ] && APPLY=true

info()  { echo -e "[\e[34m*\e[0m] $*"; }
ok()    { echo -e "[\e[32m+\e[0m] $*"; }
warn()  { echo -e "[\e[33m!\e[0m] $*"; }

run() {
    if $APPLY; then
        "$@" || warn "Fallo: $*"
    else
        echo "    (demo) $*"
    fi
}

if [[ $EUID -ne 0 ]] && $APPLY; then
    warn "Modo aplicar requiere root: sudo bash $0 --apply"
    exit 1
fi

echo "=================================================="
echo " Hardening Ubuntu — modo $([ $APPLY = true ] && echo APLICAR || echo DEMO)"
echo "=================================================="

# --- 1. Actualizaciones de seguridad -----------------------------------------
info "1/8 Actualizaciones de seguridad"
run apt-get update -y
run apt-get upgrade -y
run apt-get install -y unattended-upgrades
run dpkg-reconfigure -f noninteractive unattended-upgrades

# --- 2. SSH seguro ------------------------------------------------------------
info "2/8 Configuración SSH segura"
SSHD=/etc/ssh/sshd_config
if [ -f "$SSHD" ]; then
    run sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' "$SSHD"
    run sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication no/' "$SSHD"
    run sed -i 's/^#\?X11Forwarding.*/X11Forwarding no/' "$SSHD"
    run sed -i 's/^#\?MaxAuthTries.*/MaxAuthTries 4/' "$SSHD"
    run systemctl restart sshd
fi

# --- 3. UFW firewall ----------------------------------------------------------
info "3/8 Firewall UFW"
run ufw default deny incoming
run ufw default allow outgoing
run ufw allow 22/tcp comment 'SSH'
run ufw allow 80/tcp comment 'HTTP' || true
run ufw allow 443/tcp comment 'HTTPS' || true
run ufw --force enable

# --- 4. Permisos de archivos críticos ----------------------------------------
info "4/8 Permisos de archivos críticos"
run chmod 600 /etc/shadow
run chmod 644 /etc/passwd
run chmod 600 /etc/ssh/ssh_host_*_key

# --- 5. Kernel hardening (sysctl) --------------------------------------------
info "5/8 Parámetros de red del kernel"
SYSCTL=/etc/sysctl.d/99-hardening.conf
if $APPLY; then
    cat > "$SYSCTL" <<'EOF'
net.ipv4.ip_forward = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.secure_redirects = 0
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.all.rp_filter = 1
net.ipv4.tcp_syncookies = 1
kernel.randomize_va_space = 2
fs.suid_dumpable = 0
EOF
    sysctl --system >/dev/null
    ok "sysctl aplicado"
else
    echo "    (demo) escribir $SYSCTL"
fi

# --- 6. Fail2ban --------------------------------------------------------------
info "6/8 Fail2ban (protección de fuerza bruta)"
run apt-get install -y fail2ban
if $APPLY; then
    cat > /etc/fail2ban/jail.local <<'EOF'
[DEFAULT]
bantime = 10m
maxretry = 5
[sshd]
enabled = true
EOF
    systemctl enable --now fail2ban
    ok "fail2ban activo"
else
    echo "    (demo) configurar fail2ban"
fi

# --- 7. Paquetes innecesarios ------------------------------------------------
info "7/8 Eliminación de paquetes innecesarios"
run apt-get purge -y telnetd rsh-server rsh-redone-server || true

# --- 8. Servicios deshabilitados ---------------------------------------------
info "8/8 Servicios innecesarios"
for svc in avahi-daemon cups rpcbind; do
    run systemctl disable "$svc" 2>/dev/null || true
    run systemctl stop "$svc" 2>/dev/null || true
done

echo "=================================================="
if $APPLY; then
    ok "Hardening aplicado. REINICIA el sistema para verificar."
else
    warn "Modo demo: ninguna acción fue aplicada. Usa --apply para ejecutar."
fi
