#!/bin/bash

# Network Forensics Lab Validation Script

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'
BOLD='\033[1m'

TOTAL_POINTS=0
MAX_POINTS=500

echo -e "${BOLD}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}║     🌐 Network Forensics Lab - Validation Script         ║${NC}"
echo -e "${BOLD}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Phase 1: Basic Analysis
echo -e "${BLUE}═══ Phase 1: Basic Analysis (150 XP) ═══${NC}"

echo -n "  [?] Checking statistics... "
if [ -f /output/packet_stats.txt ]; then
    echo -e "${GREEN}✓ Statistics generated${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 30))
else
    echo -e "${YELLOW}~ Statistics pending${NC}"
fi

echo -n "  [?] Checking filtering... "
if [ -f /output/filtered_analysis.txt ]; then
    echo -e "${GREEN}✓ Filtering completed${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 30))
else
    echo -e "${YELLOW}~ Filtering pending${NC}"
fi

echo -n "  [?] Checking DNS analysis... "
if [ -f /output/dns_analysis.txt ]; then
    echo -e "${GREEN}✓ DNS analyzed${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 45))
else
    echo -e "${YELLOW}~ DNS pending${NC}"
fi

echo -n "  [?] Checking HTTP analysis... "
if [ -f /output/http_analysis.txt ]; then
    echo -e "${GREEN}✓ HTTP analyzed${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 45))
else
    echo -e "${YELLOW}~ HTTP pending${NC}"
fi

echo ""

# Phase 2: Threat Analysis
echo -e "${BLUE}═══ Phase 2: Threat Analysis (200 XP) ═══${NC}"

echo -n "  [?] Checking C2 detection... "
if [ -f /output/c2_detection.txt ]; then
    echo -e "${GREEN}✓ C2 detected${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ C2 pending${NC}"
fi

echo -n "  [?] Checking exfiltration... "
if [ -f /output/exfiltration_analysis.txt ]; then
    echo -e "${GREEN}✓ Exfiltration identified${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Exfiltration pending${NC}"
fi

echo -n "  [?] Checking lateral movement... "
if [ -f /output/lateral_movement.txt ]; then
    echo -e "${GREEN}✓ Lateral movement found${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Lateral movement pending${NC}"
fi

echo -n "  [?] Checking TLS analysis... "
if [ -f /output/tls_analysis.txt ]; then
    echo -e "${GREEN}✓ TLS analyzed${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ TLS pending${NC}"
fi

echo ""

# Phase 3: Evidence Extraction
echo -e "${BLUE}═══ Phase 3: Evidence Extraction (100 XP) ═══${NC}"

echo -n "  [?] Checking file extraction... "
if [ -d /output/extracted_files ] && [ "$(ls -A /output/extracted_files 2>/dev/null)" ]; then
    echo -e "${GREEN}✓ Files extracted${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 40))
else
    echo -e "${YELLOW}~ File extraction pending${NC}"
fi

echo -n "  [?] Checking session reconstruction... "
if [ -f /output/session_reconstruction.txt ]; then
    echo -e "${GREEN}✓ Sessions reconstructed${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 30))
else
    echo -e "${YELLOW}~ Session pending${NC}"
fi

echo -n "  [?] Checking timeline... "
if [ -f /output/timeline_report.md ]; then
    echo -e "${GREEN}✓ Timeline created${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 30))
else
    echo -e "${YELLOW}~ Timeline pending${NC}"
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
    echo -e "${BOLD}║${NC}  ${GREEN}🏆 LAB COMPLETED! Network Forensics Expert!${NC}"
elif [ $TOTAL_POINTS -gt 300 ]; then
    echo -e "${BOLD}║${NC}  ${YELLOW}⭐ Excellent analysis! Almost done!${NC}"
elif [ $TOTAL_POINTS -gt 150 ]; then
    echo -e "${BOLD}║${NC}  ${BLUE}📈 Good progress! Complete threat analysis.${NC}"
else
    echo -e "${BOLD}║${NC}  ${RED}🎯 Begin Phase 1: Basic Analysis${NC}"
fi

echo -e "${BOLD}╚════════════════════════════════════════════════════════════╝${NC}"
