.PHONY: test status tree validate

test:
	pytest -q

status:
	git status --short
	@echo
	@echo "Project state:"
	@head -40 docs/project_state.md

tree:
	find . -maxdepth 3 -type f \
		-not -path "./.git/*" \
		-not -path "./.venv/*" \
		-not -path "./outputs/*" \
		-not -path "./checkpoints/*" \
		-not -path "./cache/*" \
		| sort

validate:
	python tools/validate_repo.py
