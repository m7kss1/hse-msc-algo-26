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
	@$(PY) two_sum.py $(ARGS)

test:
	@$(PY) -m unittest -v test_two_sum.py

examples:
	@echo "arr = [1, 3, 4, 10], k = 7:"
	@$(PY) two_sum.py 1 3 4 10 / 7
	@echo "arr = [5, 5, 1, 4], k = 10:"
	@$(PY) two_sum.py 5 5 1 4 / 10

demo:
	@$(PY) two_sum.py --trace

clean:
	@rm -rf __pycache__
