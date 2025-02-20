# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.9.0] - 18-02-2025

### Fixed

- Fixed signatures of abstract methods

### Added

- Added the `ONNXExporter` and `MNISTONNXRuntimeInference` components in the `keras-mnist` sub-project to demonstrate the export of `.onnx` files and inference using `.onnx` models

## [0.8.0] - 18-02-2025

### Updated

- Utilized [cookiecutter Python templates](https://github.com/MGTheTrain/python-machine-learning-starter) for `pt-yolo-coco` sub-project
- Only kept `.gitkeep` file within the renamed `pt-transformer-common-crawl` sub-project

## [0.7.0] - 13-02-2025

### Updated

- Renamed [python subfolders](./python/) and utilized [cookiecutter Python templates](https://github.com/MGTheTrain/python-machine-learning-starter) for `keras-mnist` and `pt-mnist` sub-projects

## [0.6.0] - 06-02-2025

### Added

- [x] Enabled GPU accelerated ML trainning and inference k8s pods. Added corresponding helm charts
- [x] Created internal inference service and client along with Dockerization and Helm chart integration of the service application

### Updated

- Separated workflows for the automatic creation and destruction of cloud, helm or k8s resources
- The available options have been updated and the `Standard_NC6s_v3` AKS VM size is now selectable with 1 GPU accelerator. Unavailable sizes have been removed from the available locations.
- Permitted to change the `AKS_NODE_COUNT` input in CD workflow deploying a k8s resource 
- Renamed python entrypoint files in [Keras MNIST training example](./python/keras-mnist-training/)
- Setup resource quotas for ML training and inference k8s Pods 
- Ensured the proper folder structure naming with instance number values for persisting tf state files

## [0.5.0] - 05-02-2025

### Updated

- Added Keras MNIST inference app helm chart and argocd application
- Installed KServe
- Permitted to change the `AKS_VM_SIZE`, `RESOURCE_INSTANCE_NUMBER`, and `LOCATION` inputs in CD workflows 

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