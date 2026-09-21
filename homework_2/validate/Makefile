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
	@$(PY) validate.py $(ARGS)

test:
	@$(PY) -m unittest -v test_validate.py

examples:
	@echo "1 2 3 4 5 / 1 3 5 4 2 -> $$($(PY) validate.py 1 2 3 4 5 / 1 3 5 4 2)"
	@echo "1 2 3     / 3 1 2     -> $$($(PY) validate.py 1 2 3 / 3 1 2)"

demo:
	@$(PY) validate.py --trace 1 2 3 4 5 / 1 3 5 4 2

clean:
	@rm -rf __pycache__
