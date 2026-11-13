PY ?= python3
ARGS ?=

.PHONY: help run test examples demo clean
.DEFAULT_GOAL := help

help:
	@echo "  make run      - найти k-й элемент (args/stdin)"
	@echo "  make test     - прогнать тесты"
	@echo "  make examples - примеры из условия"
	@echo "  make demo     - пошаговая визуализация"
	@echo "  make clean    - очистить"

run:
	@$(PY) kth.py $(ARGS)

test:
	@$(PY) -m unittest -v test_kth.py

examples:
	@$(PY) kth.py 3 2 1 5 6 4 / 2
	@$(PY) kth.py 3 2 3 1 2 4 5 5 6 / 4

demo:
	@$(PY) kth.py --trace

clean:
	@$(PY) -c "import shutil; shutil.rmtree('__pycache__', ignore_errors=True)"
