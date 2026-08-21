#!/bin/bash
# ================================================
# Script de Enumeración - Lab Privesc Linux
# Ejecutar como usuario lowuser
# ================================================

echo "=========================================="
echo "  ENUMERACIÓN DE SISTEMA - PRIVESC LAB"
echo "=========================================="
echo ""

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}[1] Información del Sistema${NC}"
echo "-------------------------------------------"
echo "Usuario actual: $(whoami)"
echo "ID: $(id)"
echo "Grupos: $(groups)"
echo "Hostname: $(hostname)"
echo "Kernel: $(uname -a)"
echo "OS: $(cat /etc/os-release | head -5)"
echo ""

echo -e "${YELLOW}[2] Archivos SUID/SGID${NC}"
echo "-------------------------------------------"
find / -perm -4000 -type f 2>/dev/null | head -20
echo ""
find / -perm -2000 -type f 2>/dev/null | head -20
echo ""

echo -e "${YELLOW}[3] Permisos Sudo${NC}"
echo "-------------------------------------------"
sudo -l 2>/dev/null || echo "No se pudo ejecutar sudo -l"
echo ""

echo -e "${YELLOW}[4] Capabilities${NC}"
echo "-------------------------------------------"
getcap -r / 2>/dev/null | head -20
echo ""

echo -e "${YELLOW}[5] Cron Jobs${NC}"
echo "-------------------------------------------"
echo "=== /etc/crontab ==="
cat /etc/crontab 2>/dev/null
echo ""
echo "=== Cron dirs ==="
for dir in /etc/cron.d /etc/cron.daily /etc/cron.hourly /etc/cron.weekly /etc/cron.monthly; do
    if [ -d "$dir" ]; then
        echo "Contenido de $dir:"
        ls -la $dir 2>/dev/null
    fi
done
echo ""

echo -e "${YELLOW}[6] Procesos en Ejecución${NC}"
echo "-------------------------------------------"
ps aux | grep -v "^root.*\[" | head -20
echo ""

echo -e "${YELLOW}[7] Archivos de Configación Sensibles${NC}"
echo "-------------------------------------------"
ls -la /etc/passwd /etc/shadow /etc/group 2>/dev/null
echo ""

echo -e "${YELLOW}[8] Puertos en Escucha${NC}"
echo "-------------------------------------------"
netstat -tlnp 2>/dev/null || ss -tlnp 2>/dev/null
echo ""

echo -e "${YELLOW}[9] Historial de Comandos${NC}"
echo "-------------------------------------------"
cat /home/lowuser/.bash_history 2>/dev/null | tail -20
echo ""

echo -e "${YELLOW}[10] Archivos Escribibles${NC}"
echo "-------------------------------------------"
find / -writable -type f 2>/dev/null | grep -v proc | head -20
echo ""

echo "=========================================="
echo "  ENUMERACIÓN COMPLETADA"
echo "=========================================="
