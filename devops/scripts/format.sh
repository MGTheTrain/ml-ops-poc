#!/bin/bash

set -euo pipefail

SCRIPT_DIR=$(dirname "$BASH_SOURCE")
ROOT_PROJECT_DIR=$SCRIPT_DIR/../..

cd $ROOT_PROJECT_DIR

BLUE='\033[0;34m'
NC='\033[0m'

echo "#####################################################################################################"
echo -e "$BLUE INFO: $NC About to auto-format hcl files and generate docs for hcl files"

folders=(
  "./devops/terraform/acr"
  "./devops/terraform/tf-backend"
)

for folder in "${folders[@]}"; do
  terraform-docs markdown table --output-file README.md --hide providers --output-mode replace "$folder"
done

# Define the parent directories
folders=(
  "./terraform/envs/sbx/"
  "./terraform/envs/dev/"
  "./terraform/envs/qas/"
  "./terraform/envs/staging/"
  "./terraform/envs/prd/"
  "./terraform/modules/"
)

for parent_folder in "${folders[@]}"; do
  for folder in "$parent_folder"*/; do
    if [ -d "$folder" ]; then
      terraform-docs markdown table --output-file README.md --hide providers --output-mode replace "$folder"
    fi
  done
done

terraform fmt -recursive .

cd -