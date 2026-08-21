FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    samba \
    winbind \
    krb5-user \
    smbclient \
    && rm -rf /var/lib/apt/lists/*

COPY config/smb-ws.conf /etc/samba/smb.conf

RUN mkdir -p /data/user-profiles

EXPOSE 139 445

CMD ["/usr/sbin/smbd", "--foreground", "--no-process-group"]
