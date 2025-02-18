# keras-mnist

## Table of Contents

- [Summary](#summary)
- [References](#references)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
- [Author](#author)

## Summary

Tensorflow Keras training with MNIST dataset and model inference

**NOTE:** 

- The content within the Python files in the [src folder](./src/) can be replaced. Initially model training and inference is showcased utilizing tensorflow with the MNIST dataset.


## References

/ 

## Folder structure

```sh
project_root/
│
├── data/                   # Directory for storing datasets. NOTE: It is recommended to use an external BLOB storage for managing data to maintain a lean GitHub repository. Hence the dvc tool proves to be useful.
│   └── dataset/
│       └── ...
│
├── models/                 # Directory for storing trained models. 
│   └── saved_models/       # NOTE: It is recommended to use an external BLOB storage for managing models to maintain a lean GitHub repository. Hence the dvc tool proves to be useful.
│       └── ...
│
├── src/                    # Source code directory
│   ├── __init__.py
│   ├── data_loaders        # Data loading utilities. Load the dataset from the specified directory (data/ in this case) or from external sources like databases or APIs
│   │   ├── __init__.py
│   │   ├── data_loader_interface.py
│   │   └── mnist_data_loader.py
│   │   └── ...
│   ├── inferences          # Inference logic for testing the saved model
│   │   ├── inference_interface.py
│   │   └── mnist_inference.py
│   │   └── ...
│   ├── models              # Model architecture definition
│   │   ├── __init__.py
│   │   ├── model_interface.py
│   │   └── simple_nn.py
│   │   └── ...
│   ├── training            # Training logic considering loading data sets and saving the trained model
│   │   ├── __init__.py
│   │   ├── mnist_training.py
│   │   └── training_interface.py
│   │   └── ...
│   └── utils
│       ├── __init__.py
│       └── utils.py
│       └── ...
│   ├── main.py             # Entry point script for executing model training or inference
│   ├── ...                 # Other entrypoint scripts
│
├── tests/                  # Test directory
│   ├── test_model.py       
│   ├── test_load.py      
│   ├── ...      
|
├── experiments/            # NOTE: Requires dvc tool. Directory for storing experiment configurations, results, and logs
│   ├── experiment_1/       # Store experiment-specific files and data here
│   │   ├── config.yaml     # Configuration file for experiment 1
│   │   ├── metrics.json    # Metrics recorded during experiment 1
│   │   └── logs/           # Logs generated during experiment 1
│   └── ...                 # Additional experiment directories
│
├── requirements.txt        # Python dependencies
├── README.md               # Project README file
├── Dockerfile              # Enables training in an isolated docker container
├── Makefile                # Entrypoint enabling useful commands
├── docs                    # Project documentation
├── scripts                 # Helper scripts
└── main.py                 # Entry point script for executing model training or inference
```

## Getting started

### Preconditions

- Preferably utilize the [devcontainer.json](./.devcontainer/devcontainer.json). Therefore use the [dev container feature in VS Code IDE](https://code.visualstudio.com/docs/devcontainers/containers) to setup the development container
- Install pip packages and consider initial auto-formatting. Therefore run:

```sh
make setup
make format-and-lint
```

### Training the model from the dataset

Consider CLI args:

```sh
make train
make train TRAIN_ARGS="--model_path models/mnist_model.h5"
# in case additional input arguments are required
# make train TRAIN_ARGS="<adjust and potentially consider additional input args, e.g. --epochs 10 --batch_size 32>"
```

or env vars:

```sh
export MODE="train"
export MODEL_PATH="models/mnist_model.h5"
make train
```

### Export ONNX files from Keras models

Run:

```sh
make exp-onnx ARGS="--model_path ../models/mnist_model.h5"
```

### Model inference

Consider CLI args:

```sh
make infer
make infer INFER_ARGS="--model_path models/mnist_model.h5"
# in case additional input arguments are required
# make infer INFER_ARGS="<adjust and potentially consider additional input args, e.g. --epochs 10 --batch_size 32>"

# or model inference with .onnx files
make infer INFER_ARGS="--model_path models/mnist_model.onnx"
```

or env vars:

```sh
export MODE="train"
export MODEL_PATH="models/mnist_model.h5"
make infer
```

### Upload model to Azure Storage Account

Consider CLI args:

```sh
make upload-model ARGS="--model_path models/mnist_model.h5" --azure_connection_string <your azure connection string> --azure_container_name <your azure container name> --azure_blob_name <your azure blob name>
```

or env vars:

```sh
export MODE="upload-model"
export MODEL_PATH="models/mnist_model.h5"
export AZURE_CONNECTION_STRING="<your AZURE_CONNECTION_STRING>"
export AZURE_CONTAINER_NAME="<your AZURE_CONTAINER_NAME>"
export AZURE_BLOB_NAME="<your AZURE_BLOB_NAME>"
make upload-model
```

### Download model from Azure Storage Account

Consider CLI args:

```sh
make download-model ARGS="--model_path models/mnist_model.h5" --azure_connection_string <your azure connection string> --azure_container_name <your azure container name> --azure_blob_name <your azure blob name>
```

or env vars:

```sh
export MODE="download-model"
export MODEL_PATH="models/mnist_model.h5"
export AZURE_CONNECTION_STRING="<your AZURE_CONNECTION_STRING>"
export AZURE_CONTAINER_NAME="<your AZURE_CONTAINER_NAME>"
export AZURE_BLOB_NAME="<your AZURE_BLOB_NAME>"
make download-model
```

### Run inference service

Run:

```sh
make run-inference-service
```

or consider env vars (refer to [main_inference_service.py](./src/main_inference_service.py)):

```sh
export MODEL_PATH="<your MODEL_PATH>" # only .h5 or .onnx files considered
export AZ_SA_CONNECTION_STRING="<your AZ_SA_CONNECTION_STRING>" # set in case your model resides in an Azure Blob storage
export AZ_SA_CONTAINER_NAME="<your AZ_SA_CONTAINER_NAME>" # set in case your model resides in an Azure Blob storage
export BLOB_NAME="<your BLOB_NAME>" # set in case your model resides in an Azure Blob storage
export PORT="<your PORT>"
make run-inference-service
```

### Run inference client

Run:

```sh
make run-inference-client
```

or consider env vars (refer to [main_inference_client.py](./src/main_inference_client.py)):

```sh
export INFERENCE_SERVICE_URL="<your INFERENCE_SERVICE_URL>"
make run-inference-client
```

### Run pytests

To run all tests:

```sh
make test
```

To run an individual test:

```sh
make test-individual filename=test_model.py
```

### Auto-format and lint python files

```sh
make format-and-lint
```

**NOTE:** Optionally it is recommended to set up a symbolic link via `cd .git/hooks && ln -s ../../scripts/format_and_lint.sh pre-commit && sudo chmod +x pre-commit && cd -` and a validation automation workflow to ensure that the `format_and_lint.sh` script is executed with each commit.

### Clearing artifacts

```sh
make clean
```

## Author

MGTheTrain