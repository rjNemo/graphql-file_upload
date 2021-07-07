.PHONY: test
test:
	pipenv run pytest -v
	# pipenv run pytest --cov=. --cov-report=html --cov-report=xml
	# pipenv run diff-cover coverage.xml --compare-branch=origin/development

.PHONY: run
run:
	pipenv run uvicorn app.main:app --reload --port=8000

.PHONY: lint
lint:
	pipenv run black -l 99 .
	pipenv run flake8 .
	pipenv run mypy .
	pipenv run bandit -r --exclude=test .
	pipenv run vulture .
	pipenv run safety check
