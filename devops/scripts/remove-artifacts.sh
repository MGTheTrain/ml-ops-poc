#!/bin/bash

set -euo pipefail

SCRIPT_DIR=$(dirname "$BASH_SOURCE")
ROOT_PROJECT_DIR=$SCRIPT_DIR/../..

cd $ROOT_PROJECT_DIR

BLUE='\033[0;34m'
NC='\033[0m'

echo "#####################################################################################################"
echo -e "$BLUE INFO: $NC About to remove build artifacts"

find . -type d \( -name '.terraform' -or -name '__pycache__' -or -name 'build' -or -name 'dist' \) -exec rm -rf {} +
find . -type f \( -name '.terraform.lock.hcl' \) -exec rm -rf {} +

echo -e "$BLUE INFO: $NC Build artifacts removed successfully."