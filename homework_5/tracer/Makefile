PY ?= python3
ARGS ?=
.PHONY: help run test examples demo clean
.DEFAULT_GOAL := help
help:
	@echo "  make test | run | examples | demo | clean"
run:
	@$(PY) tracer.py $(ARGS)
test:
	@$(PY) -m unittest -v test_tracer.py
examples: demo
demo:
	@$(PY) tracer.py
clean:
	@$(PY) -c "import shutil; shutil.rmtree('__pycache__', ignore_errors=True)"
