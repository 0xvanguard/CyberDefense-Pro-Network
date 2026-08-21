#!/bin/bash
# ================================================
# Script de Validación - Lab persist-01
# Técnicas de Persistencia
# ================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SCORE=0
TOTAL=4
EXERCISES_PASSED=0

echo -e "${BLUE}╔══════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   VALIDACIÓN - Lab persist-01             ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════╝${NC}"
echo ""

check_result() {
    local test_name="$1"
    local result="$2"
    local points="$3"

    if [ "$result" = "PASS" ]; then
        echo -e "${GREEN}✓${NC} $test_name ${GREEN}+${points} XP${NC}"
        SCORE=$((SCORE + points))
        EXERCISES_PASSED=$((EXERCISES_PASSED + 1))
    else
        echo -e "${RED}✗${NC} $test_name ${RED}(0 XP)${NC}"
    fi
}

# ============================================
# Verificar servicios
# ============================================
echo -e "${YELLOW}━━━ Verificando servicios ━━━${NC}"

if docker compose exec persist-linux whoami >/dev/null 2>&1; then
    check_result "Linux container accessible" "PASS" 0
else
    check_result "Linux container accessible" "FAIL" 0
fi

echo ""

# ============================================
# Ejercicio 1: SSH Key Persistence
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 1: SSH Key Persistence ━━━${NC}"

SSH_CHECK=$(docker compose exec persist-linux ls -la /home/lowuser/.ssh/ 2>/dev/null || true)
if echo "$SSH_CHECK" | grep -q "authorized_keys"; then
    check_result "SSH authorized_keys existe" "PASS" 40
else
    check_result "SSH authorized_keys existe" "FAIL" 40
fi

echo ""

# ============================================
# Ejercicio 2: Cron Job Persistence
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 2: Cron Job Persistence ━━━${NC}"

CRON_CHECK=$(docker compose exec persist-linux crontab -l 2>/dev/null || true)
if [ -n "$CRON_CHECK" ]; then
    check_result "Cron job de persistencia creado" "PASS" 45
else
    # Check system crontab
    CRON_SYS=$(docker compose exec persist-linux cat /etc/crontab 2>/dev/null || true)
    if echo "$CRON_SYS" | grep -v "^#" | grep -q "[0-9]"; then
        check_result "Cron job de persistencia creado" "PASS" 45
    else
        check_result "Cron job de persistencia creado" "FAIL" 45
    fi
fi

echo ""

# ============================================
# Ejercicio 3: Systemd Service
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 3: Systemd Service ━━━${NC}"

SYSTEMD_CHECK=$(docker compose exec persist-linux ls /etc/systemd/system/ 2>/dev/null || true)
if echo "$SYSTEMD_CHECK" | grep -q ".service"; then
    check_result "Servicio systemd creado" "PASS" 45
else
    check_result "Servicio systemd creado" "FAIL" 45
fi

echo ""

# ============================================
# Ejercicio 4: Bashrc Injection
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 4: Bashrc Injection ━━━${NC}"

BASHRC_CHECK=$(docker compose exec persist-linux cat /home/lowuser/.bashrc 2>/dev/null || true)
if [ $(echo "$BASHRC_CHECK" | wc -l) -gt 20 ]; then
    check_result "Bashrc modificado (líneas adicionales)" "PASS" 45
else
    check_result "Bashrc modificado (líneas adicionales)" "FAIL" 45
fi

echo ""

# ============================================
# Resultados Finales
# ============================================
echo -e "${BLUE}╔══════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║           RESULTADOS FINALES             ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════╝${NC}"
echo ""
echo -e "Verificaciones pasadas: ${GREEN}$EXERCISES_PASSED${NC}/$TOTAL"
echo -e "Puntuación parcial:     ${GREEN}$SCORE${NC}/350 XP"
echo ""
echo -e "${BLUE}Siguiente lab recomendado: ${GREEN}lateral-01${NC}"
echo ""
