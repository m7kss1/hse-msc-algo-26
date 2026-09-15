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
	@$(PY) sum.py $(ARGS)

test:
	@$(PY) -m unittest -v test_sum.py

examples:
	@echo "5 7 13 2 14 -> $$($(PY) sum.py 5 7 13 2 14)"
	@echo "3           -> $$($(PY) sum.py 3)"

demo:
	@$(PY) sum.py --trace "5 7 13 2 14 -1 -8"

clean:
	@rm -rf __pycache__
