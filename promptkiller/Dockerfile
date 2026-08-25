FROM python:3.11-slim

LABEL maintainer="0xvanguard"
LABEL description="PromptKiller — AI Attack Prompt Library"

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Install package
RUN pip install -e .

# Default command
CMD ["python", "cli.py", "stats"]
