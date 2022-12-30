FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.10-bullseye

ARG NODE_VERSION="16"
ARG POETRY_VERSION="1.3.1"

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
RUN su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"

RUN python3 -m pip install poetry==1.3.1

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1
