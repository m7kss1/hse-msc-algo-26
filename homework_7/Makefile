TASKS = makeheap k-th heapsort
BENCH = makeheap heapsort
PY ?= python3

.PHONY: help test examples demo bench clean $(TASKS)
.DEFAULT_GOAL := help

help:
	@echo "  make test      - прогнать тесты всех задач"
	@echo "  make examples  - проверить примеры"
	@echo "  make demo      - визуализация всех алгоритмов"
	@echo "  make bench     - сравнение времени (makeheap, heapsort)"
	@echo "  make clean     - убрать мусор python"
	@echo "  make makeheap | k-th | heapsort - тесты одной задачи"

test examples demo clean:
	@for t in $(TASKS); do \
		echo "=== $$t"; \
		$(MAKE) -C $$t --no-print-directory $@ || exit 1; \
	done

bench:
	@for t in $(BENCH); do \
		echo "=== $$t"; \
		$(MAKE) -C $$t --no-print-directory $@ || exit 1; \
	done

$(TASKS):
	@$(MAKE) -C $@ --no-print-directory test
