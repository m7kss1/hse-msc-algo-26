PY ?= python3
ARGS ?=

.PHONY: help run test examples demo bench clean
.DEFAULT_GOAL := help

help:
	@echo "  make run      - сортировки на своем вводе (args/stdin)"
	@echo "  make test     - прогнать тесты"
	@echo "  make examples - примеры"
	@echo "  make demo     - пошаговая визуализация"
	@echo "  make bench    - сравнение времени"
	@echo "  make clean    - очистить"

run:
	@$(PY) compare.py $(ARGS)

test:
	@$(PY) -m unittest -v test_compare.py

examples:
	@$(PY) compare.py 3 2 1 5 6 4
	@$(PY) compare.py 2 2 1 3 1

demo:
	@$(PY) compare.py --trace

bench:
	@$(PY) compare.py --bench $(ARGS)

clean:
	@$(PY) -c "import shutil; shutil.rmtree('__pycache__', ignore_errors=True)"
