FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    samba \
    smbclient \
    winbind \
    && rm -rf /var/lib/apt/lists/*

COPY config/smb-fs.conf /etc/samba/smb.conf

RUN mkdir -p /data/shared /data/confidential /data/public

# Create sample files for enumeration
RUN echo "Financial Report Q4 2024" > /data/confidential/financial_report.txt && \
    echo "Admin password: P@ssw0rd123" > /data/confidential/notes.txt && \
    echo "Public document" > /data/public/readme.txt

EXPOSE 139 445

CMD ["/usr/sbin/smbd", "--foreground", "--no-process-group"]
