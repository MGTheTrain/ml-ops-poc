# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 04-02-2025

### Updated

- Considered cli tool for local development and tool expecting env variables for GitOps purposes in [keras-mnist-training](./python/keras-mnist-training/) as entrypoints. Ensured uniquely named trained model (based on date) is uploadable to a Storage Account container trough mentioned tools
- Added Opaque type secret to store Storage Account credentials in Kubernetes secrets passed as environment variables to the TFJob running the tool expecting env variables for GitOps purposes in [keras-mnist-training](./python/keras-mnist-training/). Modified CD workflow deploying k8s resources for internal apps (secrets, ingress) accordingly

## [0.3.0] - 31-01-2025

### Added

- [x] CI pipeline containerizing and pushing Python TensorFlow or PyTorch applications for training to a deployed ACR
- [x] Helm charts with K8s manifests for containerized Python TensorFlow/PyTorch ML jobs using the [Training Operator for CRDs](https://github.com/kubeflow/training-operator) and GitOps via ArgoCD

## [0.2.0] - 31-01-2025

### Updated

- Separated concerns by distinguishing between the installation of external Helm charts and the Kubernetes resources needed by applications in a deployed cluster. Additionally split GitHub Action workflows and incorporated conditionals based on the selected `INFRASTRUCTURE_OPERATION` at the job level
- Considered Repository environments

## [0.1.0] - 24-04-2024

### Added

- [Feature] Deployment of Azure Kubernetes Service (AKS) clusters
- [Feature] kubeflow operator or mlflow helm chart installations in deployed AKS clusters
- [Feature] CD workflow for on-demand AKS cluster deployments and kubeflow operator or mlflow helm chart installations. 
- [Feature] CD wofklow for on demand deployments of an Azure Storage Account Container **(For storing terraform state files)**
- [Feature] Added `devcontainer.json` with necessary tooling for local development
- [Feature] Simple feedforward neural network with MNIST dataset to map input images to their corresponding digit classes 
- [Feature] CNN architecture training considering COCO dataset for image classification AI applications (**NOTE:** Compute and storage intensive. Read `Download the COCO dataset images` comments on preferred hardware specs)
- [Feature] CD workflow for on-demand Azure Container Registry deployments in order to store internal Docker images.
- [Feature] Dockerizing Python (pytorch or tensorflow) applications for ML training and inference
- [Feature] Installation of the [Training Operator for CRDs](https://github.com/kubeflow/training-operator) and applying sample [TFJob and PyTorchJob](https://www.kubeflow.org/docs/components/training/overview/) k8s manifest
- [Feature] CI pipeline deploying an ACR