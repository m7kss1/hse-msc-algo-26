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
	@$(PY) stack_vs_queue.py $(ARGS)

test:
	@$(PY) -m unittest -v test_stack_vs_queue.py

examples:
	@$(PY) stack_vs_queue.py 1 2 3
	@$(PY) stack_vs_queue.py a b c d

demo:
	@$(PY) stack_vs_queue.py --trace 1 2 3

clean:
	@rm -rf __pycache__
