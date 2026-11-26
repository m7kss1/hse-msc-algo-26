PY ?= python3
ARGS ?=

.PHONY: help run test examples demo bench clean
.DEFAULT_GOAL := help

help:
	@echo "  make run      - отсортировать свой ввод (args/stdin)"
	@echo "  make test     - прогнать тесты"
	@echo "  make examples - примеры"
	@echo "  make demo     - пошаговая визуализация"
	@echo "  make bench    - сравнение с mergesort и sorted"
	@echo "  make clean    - очистить"

run:
	@$(PY) heapsort.py $(ARGS)

test:
	@$(PY) -m unittest -v test_heapsort.py

examples:
	@$(PY) heapsort.py 5 2 9 1 7 3 8
	@$(PY) heapsort.py 4 1 3 2 3

demo:
	@$(PY) heapsort.py --trace

bench:
	@$(PY) heapsort.py --bench $(ARGS)

clean:
	@$(PY) -c "import shutil; shutil.rmtree('__pycache__', ignore_errors=True)"
