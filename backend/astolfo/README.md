
## Updating Requirements


The `requirements[-dev].txt` files are generated using [uv](https://github.com/astral-sh/uv).

```bash
# Install uv tool
brew install uv
```

Within each of the code project folders, the requirements are stored in `requirements/*.in`
files. The exact package versions are locked using `uv pip compile`. These files are used
by CI and should be committed to the repo.


```bash
# Generate requirements.txt
uv pip compile --python python3.11 requirements/base.in -o requirements.txt

# Generate requirements-dev.txt
uv pip compile --python python3.11 requirements/dev.in -o requirements-dev.txt
```

Start Backend:
```bash
python app/main.py
```

You can see the endpoints docs at http://0.0.0.0:8000/docs


Database modeling:

