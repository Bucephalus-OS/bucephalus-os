#!/bin/bash
# Local build script for Bucephalus OS ISO
set -e

sudo apt update
sudo apt install -y live-build debootstrap git rsync curl wget python3-pip qemu-user-static binfmt-support
pip3 install --user svgwrite pillow noise numpy

python3 assets/generate_graphics.py

sudo lb config --mode debian --distribution sid --architecture amd64 --archive-areas "main contrib non-free non-free-firmware" --bootappend-live "boot=live components persistence"

sudo lb build

echo "ISO build complete. Output: live-image-amd64.hybrid.iso"
