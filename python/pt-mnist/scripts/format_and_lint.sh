#!/bin/bash

set -euo pipefail

SCRIPT_DIR=$(dirname "$BASH_SOURCE")
ROOT_PROJECT_DIR=$SCRIPT_DIR/..

cd $ROOT_PROJECT_DIR

BLUE='\033[0;34m'
NC='\033[0m'

echo "#####################################################################################################"
echo -e "$BLUE INFO: $NC About to apply linting on and auto-format python files"

black .
flake8 .

# yml formatter
# jekyll formatter

cd -