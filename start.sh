#!/bin/bash

# Read the working directory from config.json
WORKING_DIR=$(python3 -c "import json; print(json.load(open('config.json'))['workingdirectory'])")

# Change to the working directory
cd "$WORKING_DIR"

# Run the application
python3 src/main.py