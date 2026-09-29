# TypePython

Учебный стартовый проект «Месяц 1. Основы Python 3.14+ и современный toolchain».

## Быстрый старт

```bash
uv sync
uv run python main.py
uv run ruff check .
uv run ruff format .
uv run pytest
```

Выполнение финальных проверок:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest -v
```
