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
 python main.py --mode train
 ```

 #### Model inference

Run:

 ```sh
 python main.py --mode inference
 ```