TASKS = two_sum anagrams
PY ?= python3

.PHONY: help test examples demo clean $(TASKS)
.DEFAULT_GOAL := help

help:
	@echo "  make test      - прогнать тесты всех задач"
	@echo "  make examples  - проверить примеры из условий"
	@echo "  make demo      - визуализация всех алгоритмов"
	@echo "  make clean     - убрать мусор python"
	@echo "  make two_sum | anagrams - тесты одной задачи"

test examples demo clean:
	@for t in $(TASKS); do \
		echo "=== $$t"; \
		$(MAKE) -C $$t --no-print-directory $@ || exit 1; \
	done

$(TASKS):
	@$(MAKE) -C $@ --no-print-directory test
