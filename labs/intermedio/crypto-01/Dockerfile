FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Instalar herramientas de criptografía
RUN apt-get update && apt-get install -y \
    openssl \
    hashcat \
    john \
    python3 \
    python3-pip \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Instalar herramientas Python
RUN pip3 install \
    pycryptodome \
    sympy \
    cryptography

# Crear directorios
RUN mkdir -p /challenges /output /solutions

# Crear desafíos
RUN echo "Ymjfw ymj tzwxyjw fs fsi jfxytzw" > /challenges/challenge1.txt
RUN echo "GSVJF RXKYI MWLKV GSVVC OVOBS" > /challenges/challenge2.txt
RUN echo "LXFOPVEFRNHR" > /challenges/challenge3.txt

# Crear hash para crackear
RUN echo -n "password" | md5sum | awk '{print $1}' > /challenges/hash.txt

WORKDIR /challenges

CMD ["/bin/bash"]
