## Agent Operating Procedures

Keep patches small, focused, and verifiable.

Validate patches as a final todo step in your plan:

- Format with `black`: apply Black, then verify with `black --check .`.
- Type Check with `mypy`: `mypy .` must pass in strict mode.
- Test with `pytest`: `pytest` must be green with 100% test coverage (enforced).

## Commands

- Apply automatic formatting: `black .`
- Verify format: `black --check .`
- Type check: `mypy .`
- Test: `pytest`

## Project Style

- Prefer explicit type aliases and precise Python 3.12+ typing; avoid `Any`.