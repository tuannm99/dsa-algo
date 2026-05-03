# Pytest Tests

These tests are written against the typed protocols in `python/`.

`tests/conftest.py` exposes one factory fixture per data structure. The suite
ships with `array_factory` wired to `python.array.ListArray`. Every other
factory currently skips until you point it at your implementation.

Typical workflow:

1. Implement a data structure under `python/`.
2. Update the matching fixture in `tests/conftest.py` to construct it.
3. Run `pytest`.

Example:

```python
@pytest.fixture
def stack_factory():
    return lambda config=None: MyStack(config or StackConfig())
```
