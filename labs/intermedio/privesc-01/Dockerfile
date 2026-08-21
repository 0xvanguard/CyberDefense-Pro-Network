FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Instalar paquetes base
RUN apt-get update && apt-get install -y \
    sudo \
    vim \
    python3 \
    gcc \
    net-tools \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario lowuser
RUN useradd -m -s /bin/bash lowuser && \
    echo "lowuser:lowuser123" | chpasswd && \
    usermod -aG sudo lowuser

# ============================================
# VULNERABILIDAD 1: SUID Binario Custom
# ============================================
RUN cat > /usr/local/bin/backup-manager << 'SCRIPT'
#!/bin/bash
echo "Backup Manager v1.0"
while getopts "f:" opt; do
    case $opt in
        f) cat "$OPTARG" ;;
    esac
done
SCRIPT
RUN chmod +s /usr/local/bin/backup-manager

# ============================================
# VULNERABILIDAD 2: Sudo sin password para vim
# ============================================
RUN echo "lowuser ALL=(root) NOPASSWD: /usr/bin/vim" > /etc/sudoers.d/lowuser && \
    chmod 440 /etc/sudoers.d/lowuser

# ============================================
# VULNERABILIDAD 3: Cron job world-writable
# ============================================
RUN echo "#!/bin/bash\ntar czf /tmp/backup.tar.gz /home/lowuser 2>/dev/null" > /opt/backup.sh && \
    chmod 777 /opt/backup.sh && \
    echo "* * * * * root /opt/backup.sh" >> /etc/crontab

# ============================================
# VULNERABILIDAD 4: Capabilities
# ============================================
RUN setcap cap_setuid+ep /usr/bin/python3

# ============================================
# Flags
# ============================================
RUN echo "FLAG{enum_suid_d0n3}" > /home/lowuser/.flag1 && \
    mkdir -p /tmp/.hidden && \
    echo "FLAG{cr0n_m4n1pul4t10n}" > /tmp/.hidden/flag2 && \
    echo "FLAG{backups_4r3_3xpos3d}" > /var/backups/flag3 && \
    echo "FLAG{c4p4b1l1t1es_4r3_d4ng3r0us}" > /opt/flag4 && \
    echo "FLAG{pr1v3sc_c0mpl3t3d_2024}" > /root/flag.txt && \
    chmod 600 /root/flag.txt && \
    chown lowuser:lowuser /home/lowuser/.flag1

# Configurar SSH
RUN mkdir -p /var/run/sshd

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
