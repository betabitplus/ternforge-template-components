# syntax=docker/dockerfile:1@sha256:ecfaec9ed6d810b56388c508f4121597bfbba70d41a6dfeee4d8cad5f295fc32
FROM mcr.microsoft.com/devcontainers/python:3.13-trixie@sha256:a193ef0a42790e4bcaeeb13665d7bd3cb538a1cf4be721797e18f5dceaa92b1e
ENV DEBIAN_FRONTEND=noninteractive
ARG DIRENV_VERSION=2.32.1-2+b16
RUN apt-get update && apt-get install -y --no-install-recommends \
    direnv="${DIRENV_VERSION}" \
[[% for package, version in devcontainer_apt_packages|dictsort %]]    [[[ package ]]]="[[[ version ]]]" \
[[% endfor %]]    && rm -rf /var/lib/apt/lists/*
COPY --from=ghcr.io/astral-sh/uv:0.12.13@sha256:b485bd65cc2cf1c9a93b3554012c9c3778cf7b1b5fd3d3096ce9e1226c97e1e6 /uv /uvx /usr/local/bin/
COPY --from=ghcr.io/getsops/sops:v3.13.3@sha256:857f5a151ac0b2bfc55c1e4e5581d66fb8e268e4d106b38e74191f3bac9d58ea /usr/local/bin/sops /usr/local/bin/sops
ENV UV_PROJECT_ENVIRONMENT=.venv
ENV UV_LINK_MODE=copy
ENV PATH="/home/vscode/.venv/bin:${PATH}"
