FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install network forensics tools
RUN apt-get update && apt-get install -y \
    # Packet analysis
    tshark \
    tcpdump \
    ngrep \
    # Network tools
    nmap \
    net-tools \
    iputils-ping \
    # File analysis
    strings \
    file \
    binwalk \
    foremost \
    # Hex editors
    xxd \
    hexedit \
    # Python tools
    python3 \
    python3-pip \
    # Utilities
    vim \
    nano \
    curl \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install additional Python tools
RUN pip33 install \
    scapy \
    dpkt \
    pyshark \
    networkx \
    matplotlib

# Install NetworkMiner (optional - if available)
RUN apt-get update && apt-get install -y \
    mono-runtime \
    libmono-system-data4.0-cil \
    libmono-system-net4.0-cil \
    && rm -rf /var/lib/apt/lists/*

# Create directories
RUN mkdir -p /captures /output /tools /reports

# Copy capture files
COPY captures/ /captures/
COPY tools/ /tools/

# Make tools executable
RUN chmod +x /tools/* 2>/dev/null || true

WORKDIR /cases

CMD ["/bin/bash"]
