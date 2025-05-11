# Use the official Python image from the Docker Hub
FROM python:3.13-slim

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# UV
# Note uv provide docker images and advice some additional steps than covered here- see:
# https://github.com/astral-sh/uv-docker-example/blob/main/Dockerfile
# https://docs.astral.sh/uv/guides/integration/docker/#using-uv-in-docker

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh
# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh
# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Set the working directory in the container
WORKDIR /app

# Copy only the pyproject.toml and poetry.lock files to the container
COPY pyproject.toml uv.lock* ./

# Install dependencies
RUN uv sync --locked

# Copy the rest of the application code into the container
COPY ./witch .

# Specify the command to run on container start
CMD ["uv", "run", "main.py"]
