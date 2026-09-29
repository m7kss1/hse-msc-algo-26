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
	@$(PY) anagrams.py $(ARGS)

test:
	@$(PY) -m unittest -v test_anagrams.py

examples:
	@echo 'strs = ["eat","tea","tan","ate","nat","bat"]:'
	@$(PY) anagrams.py eat tea tan ate nat bat

demo:
	@$(PY) anagrams.py --trace

clean:
	@rm -rf __pycache__
