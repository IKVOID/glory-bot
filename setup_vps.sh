#!/bin/bash
# ⚡ Guild Glory Bot - 1-Click VPS Setup Script (Ubuntu/Debian)
set -e

echo "=================================================="
echo "⚡ Setting up Guild Glory Bot on Linux VPS..."
echo "=================================================="

# Update & install dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv git tmux curl

# Create venv
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate venv & install python requirements
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Allow port 25086 in firewall if ufw is active
if command -v ufw >/dev/null 2>&1; then
    sudo ufw allow 25086/tcp || true
fi

echo "=================================================="
echo "✅ Setup Complete!"
echo "To start bot dashboard 24/7 in background:"
echo "  tmux new -s glory"
echo "  source venv/bin/activate"
echo "  python dashboard_server.py"
echo "  (Press Ctrl+B then D to detach)"
echo "Website will be live at: http://YOUR_VPS_IP:25086"
echo "=================================================="
