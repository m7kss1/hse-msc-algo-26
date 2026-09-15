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
	@$(PY) palindrome.py $(ARGS)

test:
	@$(PY) -m unittest -v test_palindrome.py

examples:
	@echo "121 -> $$($(PY) palindrome.py 121)"
	@echo "31  -> $$($(PY) palindrome.py 31)"

demo:
	@$(PY) palindrome.py --trace 12321

clean:
	@rm -rf __pycache__
