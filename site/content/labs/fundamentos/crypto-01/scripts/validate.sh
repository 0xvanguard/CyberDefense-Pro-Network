#!/bin/bash
# Crypto-01 Lab Validation Script

echo "=== Crypto-01 Lab Validation ==="
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Test 1: Hash generation
echo -e "${YELLOW}Test 1: Hash Generation${NC}"
HASH_MD5=$(echo -n "password123" | md5sum | awk '{print $1}')
if [ "$HASH_MD5" = "09981850493885693388093654634394" ]; then
    echo -e "${GREEN}✓ MD5 hash correct${NC}"
else
    echo -e "${RED}✗ MD5 hash incorrect${NC}"
fi

# Test 2: AES encryption
echo -e "${YELLOW}Test 2: AES Encryption${NC}"
if [ -f secreto.txt ] && [ -f secreto.enc ]; then
    echo -e "${GREEN}✓ AES encryption files exist${NC}"
else
    echo -e "${RED}✗ AES encryption files missing${NC}"
fi

# Test 3: RSA encryption
echo -e "${YELLOW}Test 3: RSA Encryption${NC}"
if [ -f private_key.pem ] && [ -f public_key.pem ]; then
    echo -e "${GREEN}✓ RSA keys generated${NC}"
else
    echo -e "${RED}✗ RSA keys missing${NC}"
fi

# Test 4: Vault crack
echo -e "${YELLOW}Test 4: Vault Crack${NC}"
if [ -f /vault/hash.txt ]; then
    echo -e "${GREEN}✓ Vault hash file exists${NC}"
else
    echo -e "${RED}✗ Vault hash file missing${NC}"
fi

echo ""
echo "=== Validation Complete ==="
