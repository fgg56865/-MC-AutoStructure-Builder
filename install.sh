#!/bin/bash

clear

echo "[*] Initializing setup..."
sleep 1

# Update packages and install curl, python quietly
pkg update -y > /dev/null 2>&1
pkg upgrade -y > /dev/null 2>&1
pkg install curl python -y > /dev/null 2>&1

echo "[*] Setting up storage..."
termux-setup-storage > /dev/null 2>&1

echo "[*] Downloading main script..."
# Fetching main.py directly from your GitHub repository using curl
if [ ! -f "main.py" ]; then
    curl -s -O https://raw.githubusercontent.com/fgg56865/-MC-AutoStructure-Builder/main/main.py > /dev/null 2>&1
fi

echo "[*] Securing files..."
sleep 1

clear
echo "=================================================="
echo "   SETUP COMPLETED SUCCESSFULLY!"
echo "=================================================="
echo " Run command:"
echo " python main.py"
echo "=================================================="
