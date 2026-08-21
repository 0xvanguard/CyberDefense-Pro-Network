#!/bin/bash
# ================================================
# Script de Validación - Lab vulnscan-01
# Análisis de Vulnerabilidades
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
echo -e "${BLUE}║   VALIDACIÓN - Lab vulnscan-01            ║${NC}"
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

if docker compose exec kali curl -s -o /dev/null -w "%{http_code}" http://10.0.3.10/ | grep -q "200"; then
    check_result "Apache server accessible" "PASS" 0
else
    check_result "Apache server accessible" "FAIL" 0
fi

if docker compose exec kali curl -s -o /dev/null -w "%{http_code}" http://10.0.3.20/ | grep -q "200"; then
    check_result "Nginx/Node server accessible" "PASS" 0
else
    check_result "Nginx/Node server accessible" "FAIL" 0
fi

echo ""

# ============================================
# Ejercicio 1: Nmap NSE (50 XP)
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 1: Nmap NSE ━━━${NC}"

NSE_RESULT=$(docker compose exec kali nmap -sV --script vuln 10.0.3.10 2>/dev/null || true)
if echo "$NSE_RESULT" | grep -qi "VULNERABLE\|vuln"; then
    check_result "Nmap NSE detectó vulnerabilidades" "PASS" 50
else
    check_result "Nmap NSE detectó vulnerabilidades" "FAIL" 50
fi

echo ""

# ============================================
# Ejercicio 2: Nuclei (60 XP)
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 2: Nuclei ━━━${NC}"

if docker compose exec kali which nuclei >/dev/null 2>&1; then
    NUCLEI_RESULT=$(docker compose exec kali nuclei -u http://10.0.3.10 -severity critical,high 2>/dev/null || true)
    if [ -n "$NUCLEI_RESULT" ]; then
        check_result "Nuclei encontró vulnerabilidades" "PASS" 60
    else
        check_result "Nuclei encontró vulnerabilidades" "FAIL" 60
    fi
else
    check_result "Nuclei instalado" "FAIL" 60
fi

echo ""

# ============================================
# Ejercicio 5: Validación (40 XP)
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 5: Validación ━━━${NC}"

PHPINFO=$(docker compose exec kali curl -s http://10.0.3.10/vuln/phpinfo.php 2>/dev/null || true)
if echo "$PHPINFO" | grep -qi "php"; then
    check_result "PHP Info expuesto" "PASS" 20
else
    check_result "PHP Info expuesto" "FAIL" 20
fi

STATUS=$(docker compose exec kali curl -s http://10.0.3.10/server-status 2>/dev/null || true)
if echo "$STATUS" | grep -qi "apache"; then
    check_result "Server Status expuesto" "PASS" 20
else
    check_result "Server Status expuesto" "FAIL" 20
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
echo -e "Puntuación parcial:     ${GREEN}$SCORE${NC}/300 XP"
echo ""
echo -e "${BLUE}Siguiente lab recomendado: ${GREEN}webapp-01${NC}"
echo ""
