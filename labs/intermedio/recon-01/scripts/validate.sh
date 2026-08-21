#!/bin/bash
# ================================================
# Script de Validación - Lab recon-01
# Reconocimiento y OSINT
# ================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SCORE=0
TOTAL=6
EXERCISES_PASSED=0

echo -e "${BLUE}╔══════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   VALIDACIÓN - Lab recon-01: Reconocimiento${NC}"
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
# Ejercicio 2: DNS Enumeration (40 XP)
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 2: DNS Enumeration ━━━${NC}"

DNS_RESULT=$(docker compose exec kali dig corpnet.local A +short 2>/dev/null || true)
if echo "$DNS_RESULT" | grep -q "10.0.1"; then
    check_result "DNS A record encontrado" "PASS" 20
else
    check_result "DNS A record encontrado" "FAIL" 20
fi

MX_RESULT=$(docker compose exec kali dig corpnet.local MX +short 2>/dev/null || true)
if [ -n "$MX_RESULT" ]; then
    check_result "DNS MX record encontrado" "PASS" 20
else
    check_result "DNS MX record encontrado" "FAIL" 20
fi

echo ""

# ============================================
# Ejercicio 3: Host Discovery (50 XP)
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 3: Host Discovery ━━━${NC}"

HOST_SCAN=$(docker compose exec kali nmap -sn 10.0.1.0/24 2>/dev/null || true)
ACTIVE_HOSTS=$(echo "$HOST_SCAN" | grep -c "Nmap scan report for" || true)
if [ "$ACTIVE_HOSTS" -ge 4 ]; then
    check_result "Hosts activos ≥4 ($ACTIVE_HOSTS encontrados)" "PASS" 50
else
    check_result "Hosts activos ≥4 ($ACTIVE_HOSTS encontrados)" "FAIL" 50
fi

echo ""

# ============================================
# Ejercicio 4: Port Scan (60 XP)
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 4: Port Scan ━━━${NC}"

WEB_SCAN=$(docker compose exec kali nmap -sV 10.0.1.10 2>/dev/null || true)
if echo "$WEB_SCAN" | grep -q "80/tcp.*open"; then
    check_result "Puerto 80 abierto en webserver" "PASS" 15
else
    check_result "Puerto 80 abierto en webserver" "FAIL" 15
fi

FTP_SCAN=$(docker compose exec kali nmap -sV 10.0.1.30 2>/dev/null || true)
if echo "$FTP_SCAN" | grep -q "21/tcp.*open"; then
    check_result "Puerto 21 abierto en FTP" "PASS" 15
else
    check_result "Puerto 21 abierto en FTP" "FAIL" 15
fi

MYSQL_SCAN=$(docker compose exec kali nmap -sV 10.0.1.40 2>/dev/null || true)
if echo "$MYSQL_SCAN" | grep -q "3306/tcp.*open"; then
    check_result "Puerto 3306 abierto en MySQL" "PASS" 15
else
    check_result "Puerto 3306 abierto en MySQL" "FAIL" 15
fi

if echo "$WEB_SCAN" | grep -qi "apache"; then
    check_result "Apache detectado" "PASS" 15
else
    check_result "Apache detectado" "FAIL" 15
fi

echo ""

# ============================================
# Ejercicio 5: Enumeration (40 XP)
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 5: Enumeration ━━━${NC}"

HTTP_ENUM=$(docker compose exec kali curl -s http://10.0.1.10/ 2>/dev/null || true)
if echo "$HTTP_ENUM" | grep -qi "corpent"; then
    check_result "Contenido web encontrado" "PASS" 40
else
    check_result "Contenido web encontrado" "FAIL" 40
fi

echo ""

# ============================================
# Resultados Finales
# ============================================
echo -e "${BLUE}╔══════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║           RESULTADOS FINALES             ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════╝${NC}"
echo ""
echo -e "Ejercicios completados: ${GREEN}$EXERCISES_PASSED${NC}/$TOTAL"
echo -e "Puntuación total:      ${GREEN}$SCORE${NC}/250 XP"
echo ""

if [ "$SCORE" -ge 225 ]; then
    echo -e "${GREEN}🏆 ¡EXCELENTE! Has dominado el reconocimiento.${NC}"
elif [ "$SCORE" -ge 150 ]; then
    echo -e "${YELLOW}✓ ¡BUEN TRABAJO! Tienes una base sólida.${NC}"
elif [ "$SCORE" -ge 75 ]; then
    echo -e "${YELLOW}⚠ Necesitas practicar más algunos conceptos.${NC}"
else
    echo -e "${RED}✗ Revisa el material y vuelve a intentarlo.${NC}"
fi

echo ""
echo -e "${BLUE}Siguiente lab recomendado: ${GREEN}pentest-01${NC}"
echo ""
