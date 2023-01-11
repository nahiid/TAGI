#!/bin/bash
find . -name 'coverage.txt' -delete
poetry run pytest --cov-report term --cov tagi tests/ >>.logs/coverage.txt
