FROM mcr.microsoft.com/playwright:v1.51.1

# set the directory to /app to all the playwright tests
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends software-properties-common && \
    apt-get install -y gnupg && \
    apt-get install -y apt-transport-https ca-certificates curl && \
    apt-get install -y --no-install-recommends \
      build-essential \
      pkg-config && \
    apt-get install python3-pip python3-dev -y && \
    # python3 -m pip install --upgrade pip==24.3.1 && \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local POETRY_VERSION=2.1.2 python3 - && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# copy source code
COPY . .

# install poetry dependencies for tests without packaging
RUN poetry install --no-root

# run playwright installation
RUN poetry run playwright install --with-deps

RUN mkdir -p /results
ENV TEST="all"
ENV BROWSER="chromium"
ENV QASE_API_TOKEN="qase_api_token"
ENTRYPOINT ["/bin/bash", "/app/start.sh"]
