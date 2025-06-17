install:
	poetry install --no-root --sync --quiet

poc:
	poetry run mds3loader poc-run --data poc/data --out poc/output --table RAW.PEOPLE
