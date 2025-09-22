# GitHub Copilot Demo Repo

This project was created to demonstrate some key functionality of the Agent mode in VSCode's Copilot generative AI extension.

## Project Overview

A minimal Python 3.12+ project set up for:

- Dev Containers (VS Code) with Python 3.12
- mypy strict typing
- pytest with 100% coverage threshold
- A tiny priority queue with only `add()` implemented

## Quick start

- Open this folder in VS Code
- Reopen in Container (Dev Containers extension)
- The container installs deps automatically

### Run tests

In VS Code test UI or run:

```
pytest
```

### Type check

```
mypy .
```

## Design

- Data structure: `PriorityQueue` in `priority_queue/__init__.py`
- Items are tuples `(priority: int, value: str)`
- Only `add(item)` is implemented and keeps ascending order, stable on ties

## Future work

- Implement `pop`, `peek`, and `__len__`
- Replace internal access in tests once API is extended

## License

MIT
