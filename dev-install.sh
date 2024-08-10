#!/bin/bash
# Create a virtual environment
python3 -m venv .venv

# Exporting environment variables
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt