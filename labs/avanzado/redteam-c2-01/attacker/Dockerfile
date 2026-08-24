FROM kalilinux/kali-rolling

RUN apt-get update && apt-get install -y \
    nmap \
    netcat \
    curl \
    wget \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
CMD ["/bin/bash"]
