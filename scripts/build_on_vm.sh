#!/bin/bash
set -euo pipefail
# Build Bucephalus OS ISO on a Debian-based VM
# Usage: run as a regular user with sudo privileges

WORKDIR="$HOME/bucephalus-build"
REPO="https://github.com/Bucephalus-OS/bucephalus-os.git"
BRANCH="main"

echo "Preparing build host..."
sudo apt update
sudo apt install -y live-build debootstrap git rsync curl wget python3-pip qemu-user-static binfmt-support
python3 -m pip install --user svgwrite pillow noise numpy

# Prepare workspace
rm -rf "$WORKDIR"
mkdir -p "$WORKDIR"
cd "$WORKDIR"

# Clone repo
if [ -d bucephalus-os ]; then
  echo "Using existing clone, updating"
  cd bucephalus-os
  git fetch origin
  git checkout $BRANCH || true
  git pull origin $BRANCH
else
  git clone "$REPO" bucephalus-os
  cd bucephalus-os
  git checkout $BRANCH || true
fi

# OPTIONAL: Inspect or edit package list before building
echo "Current package list: config/package-lists/bucephalus-core.list.chroot"
ls -l config/package-lists/bucephalus-core.list.chroot || true

# Recommended: run an initial test with a minimal package list to validate the build
cat > config/package-lists/bucephalus-core.list.chroot.test <<'PKG'
linux-image-amd64
curl
wget
git
thunderbird
PKG

echo "You can test with the trimmed list at config/package-lists/bucephalus-core.list.chroot.test"
read -p "Proceed using the trimmed test package list? (y/N) " ans
if [[ "$ans" =~ ^[Yy] ]]; then
  cp config/package-lists/bucephalus-core.list.chroot.test config/package-lists/bucephalus-core.list.chroot
  echo "Using trimmed package list for test build"
else
  echo "Using existing package list (may contain non-debian packages which can fail)."
fi

# Configure live-build explicitly with stable mirrors
sudo lb config \
  --mode debian \
  --distribution sid \
  --architecture amd64 \
  --archive-areas "main contrib non-free non-free-firmware" \
  --bootappend-live "boot=live components persistence" \
  --linux-flavours amd64 \
  --mirror-bootstrap http://deb.debian.org/debian/ \
  --mirror-binary http://deb.debian.org/debian/

# Clean previous build state
sudo lb clean --all || true

# Ensure hooks are executable
chmod +x config/hooks/live/* || true

# Start build (long-running)
sudo lb build 2>&1 | tee build.log

echo "Build finished. If successful, ISO will be in: ./live-image-amd64.hybrid.iso"
if [ -f live-image-amd64.hybrid.iso ]; then
  ls -lh live-image-amd64.hybrid.iso
else
  echo "ISO not found. See build.log for errors."
fi

# Quick test with qemu (optional)
echo "Done. To test with qemu: qemu-system-x86_64 -enable-kvm -m 8G -cdrom live-image-amd64.hybrid.iso -boot d"
