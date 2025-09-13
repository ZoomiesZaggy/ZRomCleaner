#!/usr/bin/env bash
set -euo pipefail

OS="$(uname -s)"
case "$OS" in
    Darwin)
        echo "Building macOS release"
        ./build_mac_icon.sh
        ./package_mac.sh
        ;;
    MINGW*|MSYS*|CYGWIN*|Windows_NT)
        echo "Building Windows release"
        cmd.exe /c build_windows_icon.bat
        cmd.exe /c package_windows.bat
        ;;
    *)
        echo "Unsupported OS: $OS" >&2
        exit 1
        ;;
esac
