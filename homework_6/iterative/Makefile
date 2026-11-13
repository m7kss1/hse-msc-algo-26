PY ?= python3
ARGS ?=

.PHONY: help run test examples demo clean
.DEFAULT_GOAL := help

help:
	@echo "  make run      - сортировки на своем вводе (args/stdin)"
	@echo "  make test     - прогнать тесты"
	@echo "  make examples - примеры"
	@echo "  make demo     - пошаговая визуализация"
	@echo "  make clean    - очистить"

run:
	@$(PY) iterative.py $(ARGS)

test:
	@$(PY) -m unittest -v test_iterative.py

examples:
	@$(PY) iterative.py 3 2 1 5 6 4
	@$(PY) iterative.py 2 2 1 3 1

demo:
	@$(PY) iterative.py --trace

clean:
	@$(PY) -c "import shutil; shutil.rmtree('__pycache__', ignore_errors=True)"
