#!/bin/bash
echo "=== Advanced Lab Validation ==="
echo ""
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}Checking lab environment...${NC}"
if docker compose ps | grep -q "Up"; then
    echo -e "${GREEN}✓ Containers are running${NC}"
else
    echo -e "${RED}✗ Containers not running. Run: docker compose up -d${NC}"
fi

echo ""
echo "=== Validation Complete ==="
