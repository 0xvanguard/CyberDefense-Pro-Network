#!/bin/bash

# Reverse Engineering Lab Validation Script

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'
BOLD='\033[1m'

TOTAL_POINTS=0
MAX_POINTS=600

echo -e "${BOLD}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}║     🔧 Reverse Engineering Lab - Validation Script       ║${NC}"
echo -e "${BOLD}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Phase 1: Basic Analysis
echo -e "${BLUE}═══ Phase 1: Basic Analysis (150 XP) ═══${NC}"

echo -n "  [?] Checking binary identification... "
if [ -f /output/crackme01_type.txt ]; then
    echo -e "${GREEN}✓ Binaries identified${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 30))
else
    echo -e "${YELLOW}~ Identification pending${NC}"
fi

echo -n "  [?] Checking imports analysis... "
if [ -f /output/crackme01_imports.txt ]; then
    echo -e "${GREEN}✓ Imports analyzed${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 30))
else
    echo -e "${YELLOW}~ Imports pending${NC}"
fi

echo -n "  [?] Checking strings extraction... "
if [ -f /output/crackme01_strings.txt ]; then
    echo -e "${GREEN}✓ Strings extracted${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 40))
else
    echo -e "${YELLOW}~ Strings pending${NC}"
fi

echo -n "  [?] Checking sections analysis... "
if [ -f /output/crackme01_sections.txt ]; then
    echo -e "${GREEN}✓ Sections analyzed${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Sections pending${NC}"
fi

echo ""

# Phase 2: Disassembly
echo -e "${BLUE}═══ Phase 2: Disassembly (200 XP) ═══${NC}"

echo -n "  [?] Checking entry point analysis... "
if [ -f /output/crackme01_entry.txt ]; then
    echo -e "${GREEN}✓ Entry point analyzed${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 40))
else
    echo -e "${YELLOW}~ Entry point pending${NC}"
fi

echo -n "  [?] Checking validation logic... "
if [ -f /output/validation_logic.txt ]; then
    echo -e "${GREEN}✓ Validation logic found${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Validation pending${NC}"
fi

echo -n "  [?] Checking algorithm identification... "
if [ -f /output/algorithm_analysis.txt ]; then
    echo -e "${GREEN}✓ Algorithm identified${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 60))
else
    echo -e "${YELLOW}~ Algorithm pending${NC}"
fi

echo -n "  [?] Checking decompilation... "
if [ -f /output/crackme01_pseudocode.c ]; then
    echo -e "${GREEN}✓ Decompiled${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Decompilation pending${NC}"
fi

echo ""

# Phase 3: Anti-RE
echo -e "${BLUE}═══ Phase 3: Anti-RE Techniques (150 XP) ═══${NC}"

echo -n "  [?] Checking anti-debug detection... "
if [ -f /output/antidebug_analysis.txt ]; then
    echo -e "${GREEN}✓ Anti-debug detected${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Anti-debug pending${NC}"
fi

echo -n "  [?] Checking obfuscation analysis... "
if [ -f /output/obfuscation_analysis.txt ]; then
    echo -e "${GREEN}✓ Obfuscation analyzed${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Obfuscation pending${NC}"
fi

echo -n "  [?] Checking unpacking... "
if [ -f /output/unpacked_binary ]; then
    echo -e "${GREEN}✓ Unpacking completed${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Unpacking pending${NC}"
fi

echo ""

# Phase 4: Keygen
echo -e "${BLUE}═══ Phase 4: Keygen & Secrets (100 XP) ═══${NC}"

echo -n "  [?] Checking keygen... "
if [ -f /output/keygen.py ]; then
    echo -e "${GREEN}✓ Keygen created${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Keygen pending${NC}"
fi

echo -n "  [?] Checking secret extraction... "
if [ -f /output/extracted_secret.txt ]; then
    echo -e "${GREEN}✓ Secret extracted${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Secret pending${NC}"
fi

echo ""

# Summary
echo -e "${BOLD}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}║                    📊 RESULTS SUMMARY                    ║${NC}"
echo -e "${BOLD}╠════════════════════════════════════════════════════════════╣${NC}"
echo -e "${BOLD}║${NC}  Total Points: ${BOLD}${TOTAL_POINTS}/${MAX_POINTS}${NC}"
echo -e "${BOLD}║${NC}  Progress:     ${BOLD}$((TOTAL_POINTS * 100 / MAX_POINTS))%${NC}"
echo -e "${BOLD}║${NC}"

if [ $TOTAL_POINTS -eq $MAX_POINTS ]; then
    echo -e "${BOLD}║${NC}  ${GREEN}🏆 LAB COMPLETED! Reverse Engineering Master!${NC}"
elif [ $TOTAL_POINTS -gt 400 ]; then
    echo -e "${BOLD}║${NC}  ${YELLOW}⭐ Excellent analysis! Almost done!${NC}"
elif [ $TOTAL_POINTS -gt 200 ]; then
    echo -e "${BOLD}║${NC}  ${BLUE}📈 Good progress! Complete anti-RE analysis.${NC}"
else
    echo -e "${BOLD}║${NC}  ${RED}🎯 Begin Phase 1: Basic Analysis${NC}"
fi

echo -e "${BOLD}╚════════════════════════════════════════════════════════════╝${NC}"
