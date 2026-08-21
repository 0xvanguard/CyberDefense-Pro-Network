#!/bin/bash

# AD Lab Validation Script
# Validates that the Active Directory environment is properly configured

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'
BOLD='\033[1m'

TOTAL_POINTS=0
MAX_POINTS=500

echo -e "${BOLD}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}║     🏢 Active Directory Lab - Validation Script          ║${NC}"
echo -e "${BOLD}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Phase 1: Reconnaissance
echo -e "${BLUE}═══ Phase 1: Reconnaissance (100 XP) ═══${NC}"

echo -n "  [?] Checking if DC is responding... "
if docker compose exec -T kali bash -c "nmap -sn 10.0.1.10 -q | grep -q 'Host is up'" 2>/dev/null; then
    echo -e "${GREEN}✓ DC is reachable${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 25))
else
    echo -e "${RED}✗ DC not responding${NC}"
fi

echo -n "  [?] Checking SMB enumeration... "
if docker compose exec -T kali bash -c "smbclient -L //10.0.1.10 -U '' -N 2>/dev/null | grep -q 'Disk'" 2>/dev/null; then
    echo -e "${GREEN}✓ SMB shares found${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 25))
else
    echo -e "${YELLOW}~ SMB enumeration pending${NC}"
fi

echo -n "  [?] Checking user enumeration... "
if docker compose exec -T kali bash -c "enum4linux -a 10.0.1.10 2>/dev/null | grep -q 'User:'" 2>/dev/null; then
    echo -e "${GREEN}✓ Users enumerated${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 25))
else
    echo -e "${YELLOW}~ User enumeration pending${NC}"
fi

echo -n "  [?] Checking host discovery... "
if docker compose exec -T kali bash -c "nmap -sn 10.0.0.0/24 2>/dev/null | grep -q 'Host is up'" 2>/dev/null; then
    echo -e "${GREEN}✓ Hosts discovered${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 25))
else
    echo -e "${YELLOW}~ Host discovery pending${NC}"
fi

echo ""

# Phase 2: Credential Harvesting
echo -e "${BLUE}═══ Phase 2: Credential Harvesting (150 XP) ═══${NC}"

echo -n "  [?] Checking AS-REP Roasting... "
if docker compose exec -T kali bash -c "ls /output/asrep.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ AS-REP hash captured${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ AS-REP pending${NC}"
fi

echo -n "  [?] Checking Kerberoasting... "
if docker compose exec -T kali bash -c "ls /output/kerberoast.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Kerberoast hash captured${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Kerberoast pending${NC}"
fi

echo -n "  [?] Checking Password Spraying... "
if docker compose exec -T kali bash -c "ls /output/spray_results.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Credentials found${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Password spray pending${NC}"
fi

echo ""

# Phase 3: Lateral Movement
echo -e "${BLUE}═══ Phase 3: Lateral Movement (150 XP) ═══${NC}"

echo -n "  [?] Checking Pass-the-Hash... "
if docker compose exec -T kali bash -c "ls /output/pth_shell.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Pass-the-Hash successful${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Pass-the-Hash pending${NC}"
fi

echo -n "  [?] Checking Golden Ticket... "
if docker compose exec -T kali bash -c "ls /output/golden_ticket.kirbi 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Golden Ticket created${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Golden Ticket pending${NC}"
fi

echo -n "  [?] Checking DCSync... "
if docker compose exec -T kali bash -c "ls /output/dcsync_hashes.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ DCSync successful${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ DCSync pending${NC}"
fi

echo ""

# Phase 4: Domain Compromise
echo -e "${BLUE}═══ Phase 4: Domain Compromise (100 XP) ═══${NC}"

echo -n "  [?] Checking Domain Admin access... "
if docker compose exec -T kali bash -c "ls /output/domain_admin.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Domain Admin obtained${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Domain Admin pending${NC}"
fi

echo -n "  [?] Checking Flag capture... "
if docker compose exec -T kali bash -c "cat /output/flag.txt 2>/dev/null" 2>/dev/null | grep -q "FLAG{"; then
    echo -e "${GREEN}✓ Flag captured!${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Flag pending${NC}"
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
    echo -e "${BOLD}║${NC}  ${GREEN}🏆 LAB COMPLETED! You are an AD Master!${NC}"
elif [ $TOTAL_POINTS -gt 300 ]; then
    echo -e "${BOLD}║${NC}  ${YELLOW}⭐ Great progress! Keep going!${NC}"
elif [ $TOTAL_POINTS -gt 100 ]; then
    echo -e "${BOLD}║${NC}  ${BLUE}📈 Good start! Complete remaining phases.${NC}"
else
    echo -e "${BOLD}║${NC}  ${RED}🎯 Begin Phase 1: Reconnaissance${NC}"
fi

echo -e "${BOLD}╚════════════════════════════════════════════════════════════╝${NC}"
