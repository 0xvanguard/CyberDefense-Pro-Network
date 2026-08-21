#!/bin/bash
set -e

echo "[*] Initializing Active Directory Domain Controller..."

# Create Samba directories
mkdir -p /var/lib/samba/sysvol
mkdir -p /var/lib/samba/private
mkdir -p /var/log/samba

# Provision Samba AD DC
if [ ! -f /var/lib/samba/private/sam.ldb ]; then
    echo "[*] Provisioning Samba AD DC..."
    samba-tool domain provision \
        --use-rfc2307 \
        --realm=CORP.LOCAL \
        --domain=CORP \
        --server-role=dc \
        --dns-backend=SAMBA_INTERNAL \
        --adminpass='Password123' \
        --option="interfaces=eth0" \
        --option="bind interfaces only=yes"
    
    echo "[*] AD DC provisioned successfully!"
else
    echo "[*] AD DC already provisioned, starting..."
fi

# Configure DNS
echo "[*] Configuring DNS..."
echo "nameserver 127.0.0.1" > /etc/resolv.conf
echo "search corp.local" >> /etc/resolv.conf

# Create test users
echo "[*] Creating test users..."

# John.Doe - Domain Admin
samba-tool user create John.Doe Password123 \
    --given-name=John \
    --surname=Doe \
    --mail-address=john.doe@corp.local \
    --member-of="Domain Admins" \
    --must-change-password=no

# Jane.Smith - Help Desk
samba-tool user create Jane.Smith HelpDesk2024 \
    --given-name=Jane \
    --surname=Smith \
    --mail-address=jane.smith@corp.local \
    --member-of="Help Desk" \
    --must-change-password=no

# Bob.Wilson - Regular User (no pre-auth required for AS-REP Roasting)
samba-tool user create Bob.Wilson Summer2024 \
    --given-name=Bob \
    --surname=Wilson \
    --mail-address=bob.wilson@corp.local \
    --must-change-password=no

# Disable pre-auth for Bob (for AS-REP Roasting exercise)
samba-tool user setcontrols Bob.Wilson --no-dsdb-password

# Create Service Accounts for Kerberoasting
samba-tool user create svc_sql SqlService2024 \
    --description="SQL Service Account" \
    --must-change-password=no

samba-tool user create svc_web WebService2024 \
    --description="Web Service Account" \
    --must-change-password=no

# Add SPNs for Kerberoasting
samba-tool spn add MSSQLSvc/dc01.corp.local:1433 svc_sql
samba-tool spn add HTTP/web01.corp.local svc_web

# Create shares
mkdir -p /data/shared /data/confidential
echo "Financial Report Q4 2024" > /data/confidential/financial_report.txt
echo "Admin notes: Server room code is 1234" > /data/confidential/notes.txt
echo "Public document" > /data/shared/readme.txt

# Set permissions
chmod 755 /data/shared
chmod 700 /data/confidential

echo "[*] Starting Samba AD DC..."
exec samba -i --debug-stderr
