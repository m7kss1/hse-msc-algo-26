TASKS = tracer permutations AVL
.PHONY: help test examples demo clean $(TASKS)
.DEFAULT_GOAL := help
help:
	@echo "  make test | examples | demo | clean - для всех задач"
	@echo "  make tracer | permutations | AVL - тесты одной задачи"
test examples demo clean:
	@for t in $(TASKS); do echo "=== $$t"; $(MAKE) -C $$t --no-print-directory $@ || exit 1; done
$(TASKS):
	@$(MAKE) -C $@ --no-print-directory test
