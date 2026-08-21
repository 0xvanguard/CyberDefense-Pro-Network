FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install RE tools
RUN apt-get update && apt-get install -y \
    # Disassemblers/Decompilers
    radare2 \
    binutils \
    objdump \
    # Debuggers
    gdb \
    gdbserver \
    # Analysis
    strace \
    ltrace \
    # Utilities
    file \
    strings \
    xxd \
    hexedit \
    python3 \
    python3-pip \
    # Compilation (for creating samples)
    gcc \
    g++ \
    make \
    nasm \
    # Graph visualization
    graphviz \
    # Hex editors
    radare2-cutter \
    && rm -rf /var/lib/apt/lists/*

# Install Ghidra
RUN apt-get update && apt-get install -y wget unzip openjdk-17-jdk && \
    wget -q https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.0.1_build/ghidra_11.0.1_PUBLIC_20240130.zip -O /tmp/ghidra.zip && \
    unzip -q /tmp/ghidra.zip -d /opt/ && \
    mv /opt/ghidra_* /opt/ghidra && \
    rm /tmp/ghidra.zip && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/opt/ghidra:${PATH}"

# Install Python RE tools
RUN pip3 install \
    capstone \
    keystone-engine \
    unicorn \
    pefile \
    lief \
    yara-python

# Create directories
RUN mkdir -p /targets /output /tools /projects

# Create sample binaries (educational crackmes)
COPY targets/ /targets/
COPY tools/ /tools/

# Compile sample binaries
RUN cd /targets && \
    gcc -o crackme-01 crackme-01.c -no-pie -lm && \
    gcc -o keygen-01 keygen-01.c -no-pie -lcrypto && \
    gcc -o obfuscated-01 obfuscated-01.c -no-pie && \
    chmod +x /targets/*

WORKDIR /projects

CMD ["/bin/bash"]
