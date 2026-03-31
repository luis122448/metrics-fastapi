#!/bin/bash
# Bootstrap: installs Python runtime, creates venv, and installs project dependencies.
# Run once when setting up a new dev environment.

set -e

PYTHON_VERSION="3.11"

# Install Python
sudo apt-get update
sudo apt-get install -y python${PYTHON_VERSION} python${PYTHON_VERSION}-venv sqlite3

# Create isolated virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

echo "Dev environment ready. Run './dev-init.sh' to start the project."
