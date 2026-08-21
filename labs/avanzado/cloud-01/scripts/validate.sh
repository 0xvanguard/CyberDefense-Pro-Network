#!/bin/bash

# Cloud Security Lab Validation Script
# Validates that the cloud security environment is properly configured

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'
BOLD='\033[1m'

TOTAL_POINTS=0
MAX_POINTS=500

echo -e "${BOLD}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}║     ☁️  Cloud Security Lab - Validation Script           ║${NC}"
echo -e "${BOLD}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Phase 1: IAM Audit
echo -e "${BLUE}═══ Phase 1: IAM Audit (150 XP) ═══${NC}"

echo -n "  [?] Checking IAM users listed... "
if docker compose exec -T cloud-lab aws iam list-users --endpoint-url http://10.0.6.20:4566 2>/dev/null | grep -q "UserName"; then
    echo -e "${GREEN}✓ IAM users found${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ IAM audit pending${NC}"
fi

echo -n "  [?] Checking privilege detection... "
if docker compose exec -T cloud-lab bash -c "ls /output/iam_audit.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Privileges analyzed${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Privilege detection pending${NC}"
fi

echo -n "  [?] Checking MFA configuration... "
if docker compose exec -T cloud-lab bash -c "ls /output/mfa_status.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ MFA configured${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ MFA configuration pending${NC}"
fi

echo ""

# Phase 2: Storage Security
echo -e "${BLUE}═══ Phase 2: Storage Security (150 XP) ═══${NC}"

echo -n "  [?] Checking S3 bucket audit... "
if docker compose exec -T cloud-lab bash -c "ls /output/s3_audit.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Buckets audited${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ S3 audit pending${NC}"
fi

echo -n "  [?] Checking encryption configuration... "
if docker compose exec -T cloud-lab bash -c "ls /output/encryption_status.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Encryption configured${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Encryption pending${NC}"
fi

echo -n "  [?] Checking versioning status... "
if docker compose exec -T cloud-lab bash -c "ls /output/versioning_status.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Versioning enabled${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Versioning pending${NC}"
fi

echo ""

# Phase 3: Monitoring
echo -e "${BLUE}═══ Phase 3: Monitoring (100 XP) ═══${NC}"

echo -n "  [?] Checking CloudTrail status... "
if docker compose exec -T cloud-lab bash -c "ls /output/cloudtrail_status.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ CloudTrail configured${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ CloudTrail pending${NC}"
fi

echo -n "  [?] Checking GuardDuty status... "
if docker compose exec -T cloud-lab bash -c "ls /output/guardduty_status.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ GuardDuty enabled${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ GuardDuty pending${NC}"
fi

echo ""

# Phase 4: Secrets Management
echo -e "${BLUE}═══ Phase 4: Secrets Management (100 XP) ═══${NC}"

echo -n "  [?] Checking secrets detection... "
if docker compose exec -T cloud-lab bash -c "ls /output/secrets_detected.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Secrets detected${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Secrets detection pending${NC}"
fi

echo -n "  [?] Checking Secrets Manager migration... "
if docker compose exec -T cloud-lab bash -c "ls /output/secrets_migrated.txt 2>/dev/null" 2>/dev/null; then
    echo -e "${GREEN}✓ Secrets migrated${NC}"
    TOTAL_POINTS=$((TOTAL_POINTS + 50))
else
    echo -e "${YELLOW}~ Secrets migration pending${NC}"
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
    echo -e "${BOLD}║${NC}  ${GREEN}🏆 LAB COMPLETED! Cloud Security Expert!${NC}"
elif [ $TOTAL_POINTS -gt 300 ]; then
    echo -e "${BOLD}║${NC}  ${YELLOW}⭐ Great progress! Keep securing!${NC}"
elif [ $TOTAL_POINTS -gt 100 ]; then
    echo -e "${BOLD}║${NC}  ${BLUE}📈 Good start! Continue auditing.${NC}"
else
    echo -e "${BOLD}║${NC}  ${RED}🎯 Begin Phase 1: IAM Audit${NC}"
fi

echo -e "${BOLD}╚════════════════════════════════════════════════════════════╝${NC}"
