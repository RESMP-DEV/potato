#!/bin/bash
# Run Potato annotation server for CME tagging

echo "Starting Potato annotation server for CME Tag Verification..."
echo "Access at: http://localhost:8000"
echo "Press Ctrl+C to stop"

# Navigate to potato root directory
cd "$(dirname "$0")/../../.."

# Run the server with CME config
python potato/flask_server.py start project-hub/cme-tagging/configs/cme_config.yaml -p 8000