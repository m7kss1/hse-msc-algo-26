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
	@$(PY) prime.py $(ARGS)

test:
	@$(PY) -m unittest -v test_prime.py

examples:
	@echo "10 -> $$($(PY) prime.py 10)"
	@echo "1  -> $$($(PY) prime.py 1)"

demo:
	@$(PY) prime.py --trace 30

clean:
	@rm -rf __pycache__
