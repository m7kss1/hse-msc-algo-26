PY ?= python3
ARGS ?=

.PHONY: help run test examples demo bench clean
.DEFAULT_GOAL := help

help:
	@echo "  make run      - построить кучу на своем вводе (args/stdin)"
	@echo "  make test     - прогнать тесты"
	@echo "  make examples - примеры"
	@echo "  make demo     - пошаговая визуализация"
	@echo "  make bench    - сравнение времени и числа обменов"
	@echo "  make clean    - очистить"

run:
	@$(PY) makeheap.py $(ARGS)

test:
	@$(PY) -m unittest -v test_makeheap.py

examples:
	@$(PY) makeheap.py 5 3 8 1 9 2 7
	@$(PY) makeheap.py 7 6 5 4 3 2 1

demo:
	@$(PY) makeheap.py --trace

bench:
	@$(PY) makeheap.py --bench $(ARGS)

clean:
	@$(PY) -c "import shutil; shutil.rmtree('__pycache__', ignore_errors=True)"
