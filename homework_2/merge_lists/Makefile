PY ?= python3
ARGS ?=

.PHONY: help run test examples demo clean
.DEFAULT_GOAL := help

help:
	@echo "  make run      - решение на своем вводе (args/stdin)"
	@echo "  make test     - прогнать тесты"
	@echo "  make examples - примеры из условия"
	@echo "  make demo     - пошаговая визуализация"
	@echo "  make clean    - очистить"

run:
	@$(PY) merge_lists.py $(ARGS)

test:
	@$(PY) -m unittest -v test_merge_lists.py

examples:
	@echo "[1,2,4] + [1,3,4]:"
	@$(PY) merge_lists.py 1 2 4 / 1 3 4

demo:
	@$(PY) merge_lists.py --trace 1 2 4 8 / 1 3 4

clean:
	@rm -rf __pycache__
