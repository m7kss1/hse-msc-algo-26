PY ?= python3
ARGS ?=

.PHONY: help run test examples demo clean
.DEFAULT_GOAL := help

help:
	@echo "  make run      - решение на своем вводе (args/stdin)"
	@echo "  make test     - прогнать тесты"
	@echo "  make examples - примеры"
	@echo "  make demo     - пошаговая визуализация"
	@echo "  make clean    - очистить"

run:
	@$(PY) traversal.py $(ARGS)

test:
	@$(PY) -m unittest -v test_traversal.py

examples:
	@echo "вставка 8 3 10 1 6 14 4 7 13:"
	@$(PY) traversal.py 8 3 10 1 6 14 4 7 13
	@echo "вставка 6 2 7 1 4 9 3 5 8 (дерево из википедии):"
	@$(PY) traversal.py 6 2 7 1 4 9 3 5 8

demo:
	@$(PY) traversal.py --trace 6 2 7 1 4 9 3 5 8

clean:
	@rm -rf __pycache__
