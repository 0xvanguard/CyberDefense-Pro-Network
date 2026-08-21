#!/bin/bash
# ================================================
# Script de Validación - Lab lateral-01
# Movimiento Lateral
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
echo -e "${BLUE}║   VALIDACIÓN - Lab lateral-01             ║${NC}"
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

for host in "10.0.6.10" "10.0.6.20" "10.0.6.30"; do
    if docker compose exec kali nmap -p 22 -Pn $host 2>/dev/null | grep -q "22/tcp.*open"; then
        check_result "Host $host SSH accessible" "PASS" 0
    else
        check_result "Host $host SSH accessible" "FAIL" 0
    fi
done

echo ""

# ============================================
# Ejercicio 4: SSH Credential Reuse
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 4: Movimiento Lateral ━━━${NC}"

SSH_CHECK=$(docker compose exec kali ssh -o StrictHostKeyChecking=no -o PasswordAuthentication=yes lowuser@10.0.6.10 "echo OK" 2>/dev/null || true)
if echo "$SSH_CHECK" | grep -q "OK"; then
    check_result "SSH a Jump Box funciona" "PASS" 30
else
    check_result "SSH a Jump Box funciona" "FAIL" 30
fi

# Check if db flag can be read
DB_FLAG=$(docker compose exec kali ssh -o StrictHostKeyChecking=no dbuser@10.0.6.30 "cat /home/dbuser/flag.txt" 2>/dev/null || true)
if echo "$DB_FLAG" | grep -q "FLAG"; then
    check_result "Flag de DB Server obtenida" "PASS" 30
else
    check_result "Flag de DB Server obtenida" "FAIL" 30
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
echo -e "${BLUE}Siguiente lab recomendado: ${GREEN}disk-forensics-01${NC}"
echo ""
