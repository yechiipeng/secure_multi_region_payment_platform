# Base image with Python 3.11
FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

# Install Terraform, AWS CLI, Docker CLI, Trivy
RUN apt-get update && apt-get install -y wget unzip curl gnupg software-properties-common \
    && wget https://releases.hashicorp.com/terraform/1.5.7/terraform_1.5.7_linux_amd64.zip \
    && unzip terraform_1.5.7_linux_amd64.zip \
    && mv terraform /usr/local/bin/ \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && apt-get install -y trivy

# Create a workspace folder that vscode user can write to
RUN mkdir -p /workspace && chown -R vscode:vscode /workspace

# Switch to vscode user
USER vscode

# Set default workspace folder
WORKDIR /workspace