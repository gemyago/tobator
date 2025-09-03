# Tobator

This is a boilerplate project for a Python API, with potential for expansion into a monorepo.

## API

The API is located in the `api` directory.

### Setup

1.  **Install `direnv` and `pyenv`**. These tools are used to manage the Python version and environment variables. You can find installation instructions on their respective websites.
2.  **Allow `direnv`**. Navigate to the `api` directory and run `direnv allow`. This will create a virtual environment and automatically install the dependencies from `requirements.txt` if they are not already installed.

### Managing Dependencies

To add a new dependency, install it using pip:

```bash
pip install <package-name>
```

Then, update the `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

### Running the API

Once the setup is complete, you can run the API with the following command:

```bash
uvicorn api.main:app --reload --app-dir src
```

The API will be available at `http://127.0.0.1:8000`.

### Testing

To run the tests, use `pytest`:

```bash
pytest
```

Note that the test client requires the `httpx` package, which is included in `requirements.txt`. The `pytest` configuration in `pyproject.toml` is set up to correctly discover the `api` package.

### Linting

This project uses `ruff` for linting. To check the code, run:

```bash
ruff check .
```

To format the code, run:

```bash
ruff format .
```
