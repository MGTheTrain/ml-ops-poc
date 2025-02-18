# Variables
PYTHON = python3
PIP = pip3

# Directories
TEST_DIR = tests
SRC_DIR = src

# Commands
.PHONY: all setup test test-individual clean train infer upload-model download-model run-inference-servie run-inference-client format-and-lint help

# Default target
all: setup

# Setup the environment
setup:
	$(PIP) install -r requirements.txt

# Run pytests (will also consider code coverage report generation)
test:
	PYTHONPATH=src pytest --cov --cov-report=xml --cov-report=term

test-individual:
	@if [ -z "$(filename)" ]; then \
		echo "Please provide a filename in the test folder using 'make test-individual filename=<e.g. test_model.py>'"; \
	else \
		PYTHONPATH=src pytest --cov --cov-report=xml --cov-report=term $(TEST_DIR)/$(filename); \
	fi

# Clean up generated files
clean:
	find . -type d -name '*.pyc' -exec rm -rf {} +
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +
	rm -rf .coverage coverage.xml 
	echo "Manually clean contents in data and models dir"  

# Model training
train:
	cd $(SRC_DIR) && $(PYTHON) main.py --mode train $(ARGS)

# Export ONNX file
exp-onnx:
	cd $(SRC_DIR) && $(PYTHON) main.py --mode export-onnx $(ARGS)

# Model inference
infer:
	cd $(SRC_DIR) && $(PYTHON) main.py --mode inference $(ARGS)

# Upload trained model
upload-model:
	cd $(SRC_DIR) && $(PYTHON) main.py --mode upload-model $(ARGS)

# Download trained model
download-model:
	cd $(SRC_DIR) && $(PYTHON) main.py --mode download-model $(ARGS)

# Run inference service
run-inference-servie:
	cd $(SRC_DIR) && $(PYTHON) main_inference_service.py

# Run inference client 
run-inference-client:
	cd $(SRC_DIR) && $(PYTHON) main_inference_client.py

# Format and lint code
format-and-lint:
	cd scripts && ./format_and_lint.sh

# Display help information
help:
	@echo "Makefile targets:"
	@echo ""
	@echo "all:                  Setup environment and build documentation."
	@echo "setup:                Install dependencies from requirements.txt."
	@echo "test:                 Run tests with coverage report."
	@echo "test-individual:      Run a single test file (provide 'filename=test_file.py')."
	@echo "clean:                Clean up generated files and caches."
	@echo "train:                Train the model by running the training script. You can pass additional arguments like '--epochs 10'."
	@echo "exp-onnx:             Takes the path to the Keras model, loads the model and then converts it to ONNX. The ONNX file is saved with the same name as the Keras model, but with a .onnx extension."
	@echo "infer:                Run inference by executing the inference script. Pass inference-specific arguments."
	@echo "upload-model:         Upload the trained model to a specified destination."
	@echo "download-model:       Download the trained model from a specified source."
	@echo "run-inference-servie: Start the inference service."
	@echo "run-inference-client: Run the inference client to send requests to the service."
	@echo "docs:                 Build and serve the documentation with Jekyll."
	@echo "format-and-lint:      Run formatting and linting scripts."
	@echo "help:                 Display this help message."
