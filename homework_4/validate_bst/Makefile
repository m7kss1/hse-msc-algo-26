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
	@$(PY) validate_bst.py $(ARGS)

test:
	@$(PY) -m unittest -v test_validate_bst.py

examples:
	@echo "[2,1,3]                            -> $$($(PY) validate_bst.py '[2,1,3]')"
	@echo "[5,1,4,null,null,3,6]              -> $$($(PY) validate_bst.py '[5,1,4,null,null,3,6]')"
	@echo "[8,3,10,1,6,null,14,null,null,4,9] -> $$($(PY) validate_bst.py '[8,3,10,1,6,null,14,null,null,4,9]')"
	@echo "[2,2,2]                            -> $$($(PY) validate_bst.py '[2,2,2]')"
	@echo "[]                                 -> $$($(PY) validate_bst.py '[]')"

demo:
	@$(PY) validate_bst.py --trace 8 3 10 1 6 null 14 null null 4 9

clean:
	@rm -rf __pycache__
