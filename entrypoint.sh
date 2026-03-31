#!/bin/bash
# Docker container entrypoint — starts the Python application.
# This script is set as ENTRYPOINT in the Dockerfile.

set -e

echo "Starting application..."
exec python app/server.py
