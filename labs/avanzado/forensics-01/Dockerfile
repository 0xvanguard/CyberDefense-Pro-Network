FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Instalar herramientas forenses
RUN apt-get update && apt-get install -y \
    autopsy \
    sleuthkit \
    binwalk \
    foremost \
    testdisk \
    exiftool \
    steghide \
    volatility \
    python3 \
    python3-pip \
    curl \
    wget \
    strings \
    file \
    && rm -rf /var/lib/apt/lists/*

# Instalar Volatility 3
RUN pip3 install volatility3

# Crear directorios
RUN mkdir -p /evidence /output /tools /cases

# Crear evidencia de ejemplo
RUN echo "Evidence file content" > /evidence/sample.txt

WORKDIR /cases

CMD ["/bin/bash"]
