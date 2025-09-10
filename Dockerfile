FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY tests/ ./tests/
