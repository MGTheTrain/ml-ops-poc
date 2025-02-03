# Keras training app with mnist dataset

### Folder structure

```sh
project_root/
│
├── data/                   # Directory for storing datasets
│   └── dataset/
│       └── ...
│
├── models/                 # Directory for storing trained models
│   └── saved_models/
│       └── ...
│
├── src/                    # Source code directory
│   ├── data_loader.py      # Data loading utilities. Load the dataset from the specified directory (data/ in this case) or from external sources like databases or APIs
│   ├── model.py            # Model architecture definition
│   ├── train.py            # Training script saving trained model
│   ├── inference.py        # Inference script for testing the the saved model
│   └── utils.py            # Utility functions
│
├── requirements.txt        # Python dependencies
├── README.md               # Project README file
└── main.py                 # Main entry point script for running the application
```

### Getting started

#### Training the model from the dataset

Run:

```sh
python cli.py --mode train --model_file <model file path, e.g. models/mnist_model.h5>
```

or use env vars and run on Unix:

```sh
export MODE="train"
export MODEL_FILE="models/mnist_model.h5"
python model_operations_env.py
```

#### Model inference

Run:

```sh
python cli.py --mode inference --model_file <model file path, e.g. models/mnist_model.h5>
```

or use env vars and run on Unix:

```sh
export MODE="inference"
export MODEL_FILE="models/mnist_model.h5"
python model_operations_env.py
```

#### Upload model to Azure Storage Account

Run:

```sh
python cli.py --mode upload-model --model_file <model file path, e.g. models/mnist_model.h5> --connection_string <your connection_string> --container_name <your container_name> --blob_name <your blob_name>
```

or use env vars and run on Unix:

```sh
export MODE="upload-model"
export MODEL_FILE="models/mnist_model.h5"
export AZURE_CONNECTION_STRING="<your AZURE_CONNECTION_STRING>"
export AZURE_CONTAINER_NAME="<your AZURE_CONTAINER_NAME>"
export AZURE_BLOB_NAME="<your AZURE_BLOB_NAME>"
python model_operations_env.py
```

#### Download model from Azure Storage Account

Run:

```sh
python cli.py --mode download-model --model_file <model file path, e.g. models/mnist_model.h5> --connection_string <your connection_string> --container_name <your container_name> --blob_name <your blob_name>
```

or use env vars and run on Unix:

```sh
export MODE="download-model"
export MODEL_FILE="models/mnist_model.h5"
export AZURE_CONNECTION_STRING="<your AZURE_CONNECTION_STRING>"
export AZURE_CONTAINER_NAME="<your AZURE_CONTAINER_NAME>"
export AZURE_BLOB_NAME="<your AZURE_BLOB_NAME>"
python model_operations_env.py
```