# python

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
│   ├── train.py            # Training script
│   └── utils.py            # Utility functions
│
├── requirements.txt        # Python dependencies
├── README.md               # Project README file
└── main.py                 # Main entry point script for running the application
```

### Model Training

- CNN architecture training for image classification AI applications considering pre-trained models
- Transformer architecture training for chatbot AI applications considering pre-trained models