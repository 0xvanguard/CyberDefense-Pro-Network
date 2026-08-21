#!/bin/bash
# ================================================
# Script de Validación - Lab disk-forensics-01
# Análisis Forense de Disco
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
echo -e "${BLUE}║   VALIDACIÓN - Lab disk-forensics-01     ║${NC}"
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
# Ejercicio 1: Hash Verification
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 1: Verificar Integridad ━━━${NC}"

HASH_FILE=$(docker compose exec forensics cat /evidence/hashes.txt 2>/dev/null || true)
if [ -n "$HASH_FILE" ]; then
    check_result "Hash file existe" "PASS" 40
else
    check_result "Hash file existe" "FAIL" 40
fi

echo ""

# ============================================
# Ejercicio 3: File Recovery
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 3: Recuperar Archivos ━━━${NC}"

STRINGS_CHECK=$(docker compose exec forensics strings /evidence/disk.img 2>/dev/null | grep -c "password\|secret\|flag\|backdoor" || true)
if [ "$STRINGS_CHECK" -gt 0 ]; then
    check_result "Strings sensibles encontrados en imagen" "PASS" 50
else
    check_result "Strings sensibles encontrados en imagen" "FAIL" 50
fi

echo ""

# ============================================
# Ejercicio 5: Metadata Analysis
# ============================================
echo -e "${YELLOW}━━━ Ejercicio 5: Metadatos ━━━${NC}"

EXIF_CHECK=$(docker compose exec forensics file /evidence/disk.img 2>/dev/null || true)
if [ -n "$EXIF_CHECK" ]; then
    check_result "Tipo de imagen identificado" "PASS" 50
else
    check_result "Tipo de imagen identificado" "FAIL" 50
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
echo -e "${BLUE}Siguiente lab recomendado: ${GREEN}social-01${NC}"
echo ""
