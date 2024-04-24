#!/bin/bash

set -euo pipefail

SCRIPT_DIR=$(dirname "$BASH_SOURCE")
ROOT_PROJECT_DIR=$SCRIPT_DIR/../..

cd $ROOT_PROJECT_DIR

BLUE='\033[0;34m'
NC='\033[0m'

echo "#####################################################################################################"
echo -e "$BLUE INFO: $NC About to auto-format hcl files and generate docs for hcl files"

TF_ENVS_FOLDER="./terraform/envs"
TF_MODULES_FOLDER="./terraform/modules"
DEVOPS_TF_FOLDER="./devops/terraform"
for dir in ${TF_ENVS_FOLDER}/sbx-k8s-deployment ${TF_ENVS_FOLDER}/sbx-k8s-configuration ${TF_MODULES_FOLDER}/k8s ${DEVOPS_TF_FOLDER} ; do
  terraform-docs markdown table --output-file README.md --hide providers --output-mode replace "$dir"
done

terraform fmt -recursive .

cd -
