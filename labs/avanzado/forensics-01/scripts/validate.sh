#!/bin/bash

# Forensics Lab Validation Script
# Validates that the forensics analysis is properly completed

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'
BOLD='\033[1m'

TOTAL_POINTS=0
MAX_POINTS=500

echo -e "${BOLD}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}║     🔍 Digital Forensics Lab - Validation Script         ║${NC}"
echo -e "${BOLD}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Phase 1: Acquisition
echo -e "${BLUE}═══ Phase 1: Acquisition & Preservation (100 XP) ═══${NC}"

echo -n "  [?] Checking hash verification... "
if docker compose exec -T forensics bash -c "ls /output/hash_verified.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Hashes verified${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 25))
else
    echo -e "${YELLOW}~ Hash verification pending${NC}"
fi

echo -n "  [?] Checking image identification... "
if docker compose exec -T forensics bash -c "ls /output/image_info.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Image identified${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 25))
else
    echo -e "${YELLOW}~ Image identification pending${NC}"
fi

echo -n "  [?] Checking filesystem mount... "
if docker compose exec -T forensics bash -c "ls /mnt/evidence 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Filesystem mounted${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 25))
else
    echo -e "${YELLOW}~ Filesystem mount pending${NC}"
fi

echo -n "  [?] Checking chain of custody... "
if docker compose exec -T forensics bash -c "ls /evidence/custody_chain.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Chain of custody created${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 25))
else
    echo -e "${YELLOW}~ Chain of custody pending${NC}"
fi

echo ""

# Phase 2: Disk Analysis
echo -e "${BLUE}═══ Phase 2: Disk Analysis (200 XP) ═══${NC}"

echo -n "  [?] Checking file recovery... "
if docker compose exec -T forensics bash -c "ls /output/recovered/ 2>/dev/null | head -1" 2>/dev/null; then
    echo -e "${GREEN}✓ Files recovered${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ File recovery pending${NC}"
fi

echo -n "  [?] Checking log analysis... "
if docker compose exec -T forensics bash -c "ls /output/log_analysis.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Logs analyzed${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Log analysis pending${NC}"
fi

echo -n "  [?] Checking hidden files... "
if docker compose exec -T forensics bash -c "ls /output/hidden_files.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Hidden files found${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Hidden file search pending${NC}"
fi

echo -n "  [?] Checking metadata extraction... "
if docker compose exec -T forensics bash -c "ls /output/metadata.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Metadata extracted${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Metadata extraction pending${NC}"
fi

echo ""

# Phase 3: Memory Analysis
echo -e "${BLUE}═══ Phase 3: Memory Analysis (150 XP) ═══${NC}"

echo -n "  [?] Checking OS identification... "
if docker compose exec -T forensics bash -c "ls /output/os_info.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ OS identified${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ OS identification pending${NC}"
fi

echo -n "  [?] Checking process analysis... "
if docker compose exec -T forensics bash -c "ls /output/process_list.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Processes analyzed${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Process analysis pending${NC}"
fi

echo -n "  [?] Checking file extraction... "
if docker compose exec -T forensics bash -c "ls /output/extracted/ 2>/dev/null | head -1" 2>/dev/null; then
    echo -e "${GREEN}✓ Files extracted${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ File extraction pending${NC}"
fi

echo ""

# Phase 4: Report
echo -e "${BLUE}═══ Phase 4: Timeline & Report (50 XP) ═══${NC}"

echo -n "  [?] Checking timeline... "
if docker compose exec -T forensics bash -c "ls /output/timeline.csv 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Timeline created${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 25))
else
    echo -e "${YELLOW}~ Timeline pending${NC}"
fi

echo -n "  [?] Checking forensic report... "
if docker compose exec -T forensics bash -c "ls /output/forensic_report.md 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Report generated${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 25))
else
    echo -e "${YELLOW}~ Report pending${NC}"
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
    echo -e "${BOLD}║${NC}  ${GREEN}🏆 LAB COMPLETED! Digital Forensics Expert!${NC}"
elif [ $TOTAL_POINTS -gt 300 ]; then
    echo -e "${BOLD}║${NC}  ${YELLOW}⭐ Great analysis! Complete the report.${NC}"
elif [ $TOTAL_POINTS -gt 100 ]; then
    echo -e "${BOLD}║${NC}  ${BLUE}📈 Good progress! Continue analysis.${NC}"
else
    echo -e "${BOLD}║${NC}  ${RED}🎯 Begin Phase 1: Acquisition${NC}"
fi

echo -e "${BOLD}╚════════════════════════════════════════════════════════════╝${NC}"
