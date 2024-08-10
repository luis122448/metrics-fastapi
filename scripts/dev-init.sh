#!/bin/bash

#  Get the absolute path of the current script
LOCAL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Environment Variables
export DPI_DEBUG_LEVEL=64

# Activate Virtual Environment
source venv/bin/activate

# Start server
python app/server.py
