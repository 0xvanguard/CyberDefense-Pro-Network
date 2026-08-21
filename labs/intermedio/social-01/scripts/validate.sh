#!/bin/bash
# ================================================
# Script de Validación - Lab social-01
# Ingeniería Social — Campañas de Phishing
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
echo -e "${BLUE}║   VALIDACIÓN - Lab social-01              ║${NC}"
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
# Ejercicio 2: Landing Page
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 2: Landing Page ━━━${NC}"

LANDING=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/ 2>/dev/null || true)
if [ "$LANDING" = "200" ]; then
    check_result "Landing page accesible (HTTP 200)" "PASS" 50
else
    check_result "Landing page accesible (HTTP 200)" "FAIL" 50
fi

echo ""

# ============================================
# Ejercicio 3: Credential Harvester
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 3: Credential Harvester ━━━${NC}"

# Submit test credential
curl -s -X POST http://localhost:8081/harvest -d "email=test@test.com&password=test123" >/dev/null 2>&1

HARVESTER=$(curl -s http://localhost:8081/credentials 2>/dev/null || true)
if echo "$HARVESTER" | grep -q "test@test.com"; then
    check_result "Harvester captura credenciales" "PASS" 50
else
    check_result "Harvester captura credenciales" "FAIL" 50
fi

echo ""

# ============================================
# Ejercicio 4: Campaign Simulation
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 4: Campaña Simulada ━━━${NC}"

# Submit multiple credentials
curl -s -X POST http://localhost:8081/harvest -d "email=alice@corp.local&password=Password1" >/dev/null 2>&1
curl -s -X POST http://localhost:8081/harvest -d "email=bob@corp.local&password=Summer2024" >/dev/null 2>&1

METRICS=$(curl -s http://localhost:8081/metrics 2>/dev/null || true)
if echo "$METRICS" | grep -q '"total_captured"'; then
    check_result "Métricas de campaña disponibles" "PASS" 60
else
    check_result "Métricas de campaña disponibles" "FAIL" 60
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
echo -e "${GREEN}🎉 ¡Has completado todos los labs de módulos 05-08!${NC}"
echo ""
