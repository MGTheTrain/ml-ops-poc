# Variables
PYTHON = python3
PIP = pip3

# Directories
DOCS_DIR = docs
TEST_DIR = tests
SRC_DIR = src

# Commands
.PHONY: all setup test test-individual clean train infer docs format-and-lint help

# Default target
all: setup docs

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
	rm -rf $(DOCS_DIR)/_build
	find . -type d -name '*.pyc' -exec rm -rf {} +
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +
	rm -rf .coverage coverage.xml 
	rm -rf ${DOCS_DIR}/pt-mnist/_site
	rm -rf ${DOCS_DIR}/pt-mnist/.jekyll-cache
	echo "Manually clean contents in data and models dir"  

# Model training
train:
	cd $(SRC_DIR) && $(PYTHON) main.py --mode train $(ARGS)

# Model inference
infer:
	cd $(SRC_DIR) && $(PYTHON) main.py --mode inference $(ARGS)

# Build and serve documentation
docs:
	cd docs/pt-mnist && jekyll serve && echo "Visit in a browser of choice localhost:4000"

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
	@echo "infer:                Run inference by executing the inference script. Pass inference-specific arguments."
	@echo "docs:                 Build and serve the documentation with Jekyll."
	@echo "format-and-lint:      Run formatting and linting scripts."
	@echo "help:                 Display this help message."
