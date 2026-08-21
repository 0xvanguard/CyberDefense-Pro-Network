#!/bin/bash
# ================================================
# Script de Validación - Lab net-01
# Fundamentos de Redes y Modelo OSI
# ================================================

set -e

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Contadores
SCORE=0
TOTAL=6
EXERCISES_PASSED=0

echo -e "${BLUE}╔══════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   VALIDACIÓN - Lab net-01: Redes         ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════╝${NC}"
echo ""

# Función para mostrar resultado
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
# Ejercicio 1: Modelo OSI (25 XP)
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 1: Modelo OSI ━━━${NC}"

# Verificar que el estudiante puede identificar capas
# Esto se valida manualmente en el README
echo -e "${BLUE}Nota: Ejercicio 1 se valida manualmente${NC}"
echo ""

# ============================================
# Ejercicio 2: TCP Handshake (25 XP)
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 2: TCP Handshake ━━━${NC}"

# Verificar que puede capturar tráfico
if docker compose exec kali tcpdump -c 10 -i eth0 tcp port 80 2>/dev/null | grep -q "SYN"; then
    check_result "Captura de tráfico TCP" "PASS" 10
else
    check_result "Captura de tráfico TCP" "FAIL" 10
fi

echo ""

# ============================================
# Ejercicio 3: Escaneo de Puertos (50 XP)
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 3: Escaneo de Puertos ━━━${NC}"

# Verificar que nmap está instalado
if docker compose exec kali which nmap >/dev/null 2>&1; then
    check_result "Nmap instalado" "PASS" 5
else
    check_result "Nmap instalado" "FAIL" 5
fi

# Ejecutar escaneo y verificar resultados
SCAN_OUTPUT=$(docker compose exec kali nmap -sn 10.10.10.0/24 2>/dev/null)

# Contar hosts activos (deberían ser 4: router, web, db, ftp)
ACTIVE_HOSTS=$(echo "$SCAN_OUTPUT" | grep -c "Nmap scan report for")
if [ "$ACTIVE_HOSTS" -ge 4 ]; then
    check_result "Hosts activos identificados (≥4)" "PASS" 10
else
    check_result "Hosts activos identificados (≥4)" "FAIL" 10
fi

# Escaneo detallado
DETAILED_SCAN=$(docker compose exec kali nmap -sV 10.10.10.10 2>/dev/null)

# Verificar puerto 80 abierto
if echo "$DETAILED_SCAN" | grep -q "80/tcp.*open"; then
    check_result "Puerto 80 abierto en Web Server" "PASS" 10
else
    check_result "Puerto 80 abierto en Web Server" "FAIL" 10
fi

# Verificar Apache
if echo "$DETAILED_SCAN" | grep -qi "apache"; then
    check_result "Apache detectado" "PASS" 10
else
    check_result "Apache detectado" "FAIL" 10
fi

# Verificar FTP
FTP_SCAN=$(docker compose exec kali nmap -sV 10.10.10.30 2>/dev/null)
if echo "$FTP_SCAN" | grep -q "21/tcp.*open"; then
    check_result "FTP Service detectado" "PASS" 15
else
    check_result "FTP Service detectado" "FAIL" 15
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
echo -e "Puntuación total:      ${GREEN}$SCORE${NC}/100 XP"
echo ""

# Calcular porcentaje
PERCENTAGE=$((SCORE * 100 / 100))

if [ "$SCORE" -ge 90 ]; then
    echo -e "${GREEN}🏆 ¡EXCELENTE! Has dominado los fundamentos de redes.${NC}"
    echo -e "${GREEN}   +200 XP bonus por puntuación ≥90%${NC}"
elif [ "$SCORE" -ge 70 ]; then
    echo -e "${YELLOW}✓ ¡BUEN TRABAJO! Tienes una base sólida.${NC}"
elif [ "$SCORE" -ge 50 ]; then
    echo -e "${YELLOW}⚠ Necesitas practicar más algunos conceptos.${NC}"
else
    echo -e "${RED}✗ Revisa el material y vuelve a intentarlo.${NC}"
fi

echo ""
echo -e "${BLUE}Siguiente lab recomendado: ${GREEN}linux-01${NC}"
echo ""
