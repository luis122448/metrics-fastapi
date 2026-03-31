#!/bin/sh
# Build and push a Docker image to a private registry with multi-arch support.
# Usage: ./build-release.sh <version> <environment> <architecture> <docker_registry> <docker_project>

set -e

# --- Configuration ---
DOCKERFILE_PATH="."
IMAGE_NAME="metrics-fastapi"

# --- Inputs ---
VERSION="$1"
ENVIRONMENT_TAG="$2"
ARCHITECTURE="$3"
DOCKER_REGISTRY="$4"
DOCKER_PROJECT="$5"

# --- Validations ---
if [ -z "$VERSION" ] || [ -z "$ENVIRONMENT_TAG" ] || [ -z "$ARCHITECTURE" ] || [ -z "$DOCKER_REGISTRY" ] || [ -z "$DOCKER_PROJECT" ]; then
  echo "Usage: ./build-release.sh <version> <environment> <architecture> <docker_registry> <docker_project>"
  exit 1
fi

if ! echo "$VERSION" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+$'; then
  echo "Invalid version format. Expected X.X.X"
  exit 1
fi

if [ "$ENVIRONMENT_TAG" != "development" ] && [ "$ENVIRONMENT_TAG" != "quality" ] && [ "$ENVIRONMENT_TAG" != "production" ]; then
  echo "Environment must be: development, quality, or production"
  exit 1
fi

if [ "$ARCHITECTURE" != "amd64" ] && [ "$ARCHITECTURE" != "arm64" ] && [ "$ARCHITECTURE" != "all" ]; then
  echo "Architecture must be: amd64, arm64, or all"
  exit 1
fi

# --- Version injection ---
echo "Generating version file..."
BUILD_DATE="$(TZ=America/Lima date +"%Y.%m.%d-%H:%M")"
cat <<EOF > app/version.py
BUILD_VERSION_DATE = '${BUILD_DATE}'
BUILD_VERSION_NUMBER = '${VERSION}'
EOF

if [ "$ENVIRONMENT_TAG" = "quality" ]; then
  IMAGE_NAME="${IMAGE_NAME}-qa"
fi

# --- Image names ---
FULL_IMAGE_NAME="${DOCKER_REGISTRY}/${DOCKER_PROJECT}/${IMAGE_NAME}:${VERSION}"
LATEST_IMAGE_NAME="${DOCKER_REGISTRY}/${DOCKER_PROJECT}/${IMAGE_NAME}:${ENVIRONMENT_TAG}"

echo "Building image:"
echo " - ${FULL_IMAGE_NAME}"
echo " - ${LATEST_IMAGE_NAME}"

if [ "$ENVIRONMENT_TAG" = "quality" ]; then
  ENVIRONMENT_TAG="development"
fi

# --- Build ---
if [ "$ARCHITECTURE" = "amd64" ]; then
  echo "Building amd64 image..."
  docker build \
    --build-arg env="${ENVIRONMENT_TAG}" \
    --platform linux/amd64 \
    -t "${FULL_IMAGE_NAME}" \
    -t "${LATEST_IMAGE_NAME}" \
    "${DOCKERFILE_PATH}"
  docker push "${FULL_IMAGE_NAME}"
  docker push "${LATEST_IMAGE_NAME}"
fi

if [ "$ARCHITECTURE" = "arm64" ]; then
  echo "Building arm64 image..."
  docker build \
    --build-arg env="${ENVIRONMENT_TAG}" \
    --platform linux/arm64 \
    -t "${FULL_IMAGE_NAME}" \
    -t "${LATEST_IMAGE_NAME}" \
    "${DOCKERFILE_PATH}"
  docker push "${FULL_IMAGE_NAME}"
  docker push "${LATEST_IMAGE_NAME}"
fi

if [ "$ARCHITECTURE" = "all" ]; then
  echo "Building multi-architecture image..."
  docker --config "${DOCKER_CONFIG:-$HOME/.docker}" buildx build \
    --push \
    --build-arg env="${ENVIRONMENT_TAG}" \
    --platform linux/amd64,linux/arm64 \
    -t "${FULL_IMAGE_NAME}" \
    -t "${LATEST_IMAGE_NAME}" \
    "${DOCKERFILE_PATH}"
fi

echo "Image successfully pushed:"
echo " - ${FULL_IMAGE_NAME}"
echo " - ${LATEST_IMAGE_NAME}"
