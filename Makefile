# Makefile for automating preparation of virtual environment


VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python3
REQUIREMENTS = requirements.txt

# creating virtual envitonment
.PHONY: venv
venv:
	@echo "Creating virtual environment..."
	@python3 -m venv $(VENV_DIR)
	@echo "Virtual envitonment created."

# install dependencies
.PHONY: prepare 
prepare:
	@echo "Installing dependencies..."
	@$(PYTHON) -m pip install -r $(REQUIREMENTS)
	@echo "Dependencies Installed."

.PHONY: activate
activate:
	@echo "Run source $(VENV_DIR)/bin/activate to activate virtual envitonment"

.PHONY: test
test:
	@echo "Checking if pytest is installed..."
	@if $(PYTHON) -m pytest --version >/dev/null 2>&1; then \
		echo "pytest is installed. Running tests..."; \
		$(PYTHON) -m pytest tests/; \
	else \
		echo "pytest is not installed. Installing pytest..."; \
		$(PYTHON) -m pip install pytest; \
		echo "Running tests..."; \
		$(PYTHON) -m pytest tests/; \
	fi

