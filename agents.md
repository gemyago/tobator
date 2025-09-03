# Tobator Agents

This file provides context for AI agents to understand and interact with the Tobator project.

## Monorepo Structure

This project is structured as a monorepo. The main components are:

-   `api`: A Python API built with FastAPI.

## api

-   **Framework**: FastAPI
-   **Entrypoint**: `api/src/api/main.py`
-   **Dependencies**: `api/requirements.txt` (includes `httpx` for the test client)
-   **Tests**: `api/tests/`
-   **Environment Management**: `direnv` and `venv`
-   **Linting**: `ruff`
-   **Testing**: `pytest` (configured in `pyproject.toml` to find the `api` package)

### How to run the API

1.  `cd api`
2.  `direnv allow` (may happen automatically, will also install dependencies)
3.  `uvicorn api.main:app --reload --app-dir src`

### How to run tests

1.  `cd api`
2.  `direnv allow` (this will also install dependencies)
3.  `pytest`
