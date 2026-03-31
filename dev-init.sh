#!/bin/bash
# Start: activates venv, exports env vars, and launches the development server.
# Run after bootstrap to start working locally.

set -e

# Activate virtual environment
source .venv/bin/activate

# Environment variables
export APP_ENV="development"
export DPI_DEBUG_LEVEL=64

# Start server
echo "Starting development server on port 8083..."
python app/server.py
