#!/bin/bash
# Build and run the application locally using a local Docker registry.
# Useful for testing the Docker image before pushing to the remote registry.

set -e

IMAGE_NAME="metrics-fastapi"
CONTAINER_NAME="metrics-fastapi"
LOCAL_PORT=8083
CONTAINER_PORT=8083

# --- Start local registry if not running ---
if ! docker ps --format '{{.Names}}' | grep -q '^local-registry$'; then
  echo "Starting local Docker registry on port 5000..."
  docker run -d -p 5000:5000 --restart=always --name local-registry registry:2 || true
fi

# --- Build image using build-release.sh ---
echo "Building image with local registry..."
chmod +x build-release.sh
./build-release.sh "0.0.1" "development" "$(dpkg --print-architecture)" "localhost:5000" "local"

# --- Stop and remove previous container ---
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
  echo "Stopping and removing previous container..."
  docker stop "${CONTAINER_NAME}" || true
  docker rm "${CONTAINER_NAME}" || true
fi

# --- Run container ---
FULL_IMAGE="localhost:5000/local/${IMAGE_NAME}:0.0.1"
echo "Starting container from ${FULL_IMAGE}..."
docker run -d \
  --name "${CONTAINER_NAME}" \
  -p "${LOCAL_PORT}:${CONTAINER_PORT}" \
  -e APP_ENV=development \
  "${FULL_IMAGE}"

echo ""
echo "=============================================================="
echo "Application running locally"
echo "  App URL:     http://localhost:${LOCAL_PORT}"
echo "  Swagger URL: http://localhost:${LOCAL_PORT}/docs"
echo "  Logs:        docker logs -f ${CONTAINER_NAME}"
echo "  Stop:        docker stop ${CONTAINER_NAME}"
echo "=============================================================="
