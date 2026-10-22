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
	@$(PY) balanced.py $(ARGS)

test:
	@$(PY) -m unittest -v test_balanced.py

examples:
	@echo "[3,9,20,null,null,15,7]   -> $$($(PY) balanced.py '[3,9,20,null,null,15,7]')"
	@echo "[1,2,2,3,3,null,null,4,4] -> $$($(PY) balanced.py '[1,2,2,3,3,null,null,4,4]')"
	@echo "[1,2,null,3]              -> $$($(PY) balanced.py '[1,2,null,3]')"
	@echo "[]                        -> $$($(PY) balanced.py '[]')"

demo:
	@$(PY) balanced.py --trace 1 2 3 4 5 null 6 7 null null null null 8
	@echo
	@$(PY) balanced.py --trace 3 9 20 null null 15 7

clean:
	@rm -rf __pycache__
