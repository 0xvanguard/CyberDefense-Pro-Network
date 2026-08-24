FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Sliver
RUN curl -sSL https://sliver.sh/install | bash

WORKDIR /workspace
VOLUME /shared

EXPOSE 8443
CMD ["/bin/bash"]
