FROM ubuntu:22.04

# Evitar prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive
ENV container=docker

# Actualizar e instalar paquetes base
RUN apt-get update && apt-get install -y \
    sudo \
    vim \
    net-tools \
    curl \
    wget \
    gcc \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario de bajo nivel
RUN useradd -m -s /bin/bash lowuser && \
    echo "lowuser:lowuser123" | chpasswd && \
    usermod -aG sudo lowuser

# ============================================
# VULNERABILIDAD 1: SUID Binario Vulnerable
# ============================================
RUN cat > /usr/local/bin/backup-manager << 'EOF'
#!/bin/bash
# Backup manager - backup files
echo "Backup Manager v1.0"
echo "Usage: $0 -f <file>"
while getopts "f:" opt; do
    case $opt in
        f)
            echo "Backing up: $OPTARG"
            cat "$OPTARG"  # VULNERABILIDAD: ejecuta como root sin sanitizar
            ;;
        *)
            echo "Invalid option"
            ;;
    esac
done
EOF
RUN chmod +s /usr/local/bin/backup-manager

# ============================================
# VULNERABILIDAD 2: Sudo sin password para vim
# ============================================
RUN echo "lowuser ALL=(root) NOPASSWD: /usr/bin/vim" > /etc/sudoers.d/lowuser && \
    chmod 440 /etc/sudoers.d/lowuser

# ============================================
# VULNERABILIDAD 3: Cron job con PATH manipulation
# ============================================
RUN mkdir -p /opt/backup && \
    cat > /opt/backup.sh << 'EOF'
#!/bin/bash
# Script de backup ejecutado por cron
cd /opt/backup
tar czf /tmp/backup-$(date +%Y%m%d).tar.gz /home/lowuser/documents 2>/dev/null
EOF
RUN chmod 777 /opt/backup.sh && \
    echo "* * * * * root /opt/backup.sh" >> /etc/crontab

# ============================================
# VULNERABILIDAD 4: Binary con capabilities
# ============================================
RUN apt-get update && apt-get install -y python3 && rm -rf /var/lib/apt/lists/*
RUN setcap cap_setuid+ep /usr/bin/python3

# ============================================
# VULNERABILIDAD 5: Kernel vulnerable (simulado)
# ============================================
# En un entorno real, usaríamos un kernel vulnerable
# Aquí simulamos con un archivo que indica la versión
RUN echo "5.15.0-generic" > /etc/kernel-version

# ============================================
# Archivos de prueba
# ============================================
RUN mkdir -p /home/lowuser/documents && \
    echo "Archivo confidencial del usuario" > /home/lowuser/documents/secreto.txt && \
    chown -R lowuser:lowuser /home/lowuser

# Flag para el lab
RUN echo "FLAG{pr1v3sc_l4b_c0mpl3t3d_2024}" > /root/flag.txt && \
    chmod 600 /root/flag.txt

# Configurar SSH
RUN mkdir -p /var/run/sshd && \
    echo "PermitRootLogin no" >> /etc/ssh/sshd_config

# Scripts de ayuda
COPY scripts/ /scripts/
RUN chmod +x /scripts/*

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
