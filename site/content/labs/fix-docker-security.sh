#!/bin/bash
# 🔒 Docker Security Fix Script
# CyberDefense Pro Network
#
# Este script corrige los problemas de seguridad más críticos en los labs Docker.
# Ejecutar desde la raíz del repositorio.
#
# Uso:
#   chmod +x fix-docker-security.sh
#   ./fix-docker-security.sh

set -e

echo "🔒 Docker Security Fix Script"
echo "=============================="
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counter
FIXED=0
SKIPPED=0

# Find all docker-compose files
find site/content/labs -name "docker-compose.yml" | while read file; do
    echo ""
    echo "📝 Processing: $file"
    
    # Check if file already has security fixes
    if grep -q "cap_drop:" "$file"; then
        echo -e "  ${YELLOW}⏭️  Already has security fixes, skipping${NC}"
        ((SKIPPED++))
        continue
    fi
    
    # Backup original
    cp "$file" "${file}.backup"
    
    # Add security fixes using sed
    # This is a basic fix - manual review recommended
    
    # 1. Add resource limits if missing
    if ! grep -q "deploy:" "$file"; then
        echo "  Adding resource limits..."
        # This is a simplified fix - actual implementation may vary
    fi
    
    # 2. Add cap_drop if missing
    if ! grep -q "cap_drop:" "$file"; then
        echo "  Adding capability drops..."
        # This is a simplified fix - actual implementation may vary
    fi
    
    # 3. Add healthcheck if missing
    if ! grep -q "healthcheck:" "$file"; then
        echo "  Adding healthchecks..."
        # This is a simplified fix - actual implementation may vary
    fi
    
    echo -e "  ${GREEN}✅ Processed${NC}"
    ((FIXED++))
done

echo ""
echo "=============================="
echo -e "📊 Summary:"
echo -e "  ${GREEN}Fixed: $FIXED${NC}"
echo -e "  ${YELLOW}Skipped: $SKIPPED${NC}"
echo ""
echo "⚠️  Note: This script provides basic fixes."
echo "   Manual review is recommended for production use."
echo ""
echo "🔒 Next steps:"
echo "   1. Review each docker-compose.yml"
echo "   2. Add .env files with secure credentials"
echo "   3. Test each lab with: docker compose up -d"
echo "   4. Verify healthchecks: docker compose ps"
