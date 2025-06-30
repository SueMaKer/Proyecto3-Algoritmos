# Variables
PYTHON=python3
SRC_DIR=src
MAIN=$(SRC_DIR)/main.py
TEST_DIR=tests

# Default: Ejecuta el programa principal
default: run

# Ejecutar el programa principal
run:
	$(PYTHON) $(MAIN)

# Ejecutar todos los tests
test:
	PYTHONPATH=$(SRC_DIR) pytest $(TEST_DIR)

# Limpiar archivos .pyc y carpetas __pycache__
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	echo "Carpeta limpia."

# Generar documentación (opcional)
doc:
	pydoc -w $(SRC_DIR)/*

# Ayuda
help:
	@echo "Comandos disponibles:"
	@echo "  make           -> Ejecuta el programa principal (main.py)"
	@echo "  make run       -> Ejecuta el programa principal"
	@echo "  make test      -> Ejecuta todos los tests con pytest"
	@echo "  make clean     -> Limpia archivos temporales y __pycache__"
	@echo "  make doc       -> Genera documentación con pydoc"

.PHONY: run test clean doc help
