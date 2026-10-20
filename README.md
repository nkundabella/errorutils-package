# errorutils

A lightweight, zero-dependency Python utility package for **safe error handling, input validation, and function-level logging**.

Built for use in data pipelines, ML scripts, and any Python project where bad inputs or unexpected exceptions shouldn't crash your entire run.

## Installation

```bash
pip install the_error_utils
```

## Features

- ✅ Validate numeric inputs (rejects booleans, NaN, Inf)
- ✅ Guard against `None` values with clear error messages
- ✅ Wrap risky calls with `safe_call` — logs errors, never crashes
- ✅ Decorate functions with `@catch_errors` for automatic error suppression
- ✅ Validated arithmetic operations (`add`, `multiply`, `average`)
- ✅ Zero external dependencies

## Quick Start

```python
from errorutils import (
    validate_number,
    check_not_none,
    safe_call,
    catch_errors,
    log_error,
    add,
    multiply,
    average,
)
```

## API Reference

### Exceptions

#### `ErrorUtilsError`
Base exception class for all errors raised by this package.

#### `ValidationError(ErrorUtilsError)`
Raised when a value fails validation (e.g. wrong type, None, NaN, Inf).

---

### Functions

#### `validate_number(value, name="value") -> float`
Ensures a value is a real, finite number. Rejects booleans, NaN, and infinity.

```python
validate_number(3.14)          # → 3.14
validate_number(True)          # → ValidationError: value must be a number, got bool.
validate_number(float("inf"))  # → ValidationError: value must be finite.
```

---

#### `check_not_none(value, name="value") -> Any`
Raises a `ValidationError` if the value is `None`, otherwise returns it unchanged.

```python
check_not_none("hello")  # → "hello"
check_not_none(None)     # → ValidationError: value cannot be None.
```

---

#### `safe_call(func, *args, default=None, **kwargs) -> Optional[T]`
Calls a function and logs any exception instead of propagating it. Returns `default` on failure.

```python
result = safe_call(int, "not-a-number", default=0)  # → 0 (logs the error)
result = safe_call(int, "42")                        # → 42
```

---

#### `catch_errors(func) -> Callable`
Decorator that wraps a function with `safe_call` — logs unexpected errors and returns `None` on failure.

```python
@catch_errors
def risky_operation(x):
    return 1 / x

risky_operation(0)   # → None (logs ZeroDivisionError, doesn't crash)
risky_operation(4)   # → 0.25
```

---

#### `log_error(message: str) -> None`
Logs an error-level message using Python's built-in `logging` module under the `"errorutils"` logger.

```python
log_error("Something went wrong in the pipeline.")
```

---

### Validated Arithmetic (`ops`)

These functions run `validate_number` on inputs before computing, so you get clear errors on bad data instead of silent wrong results.

#### `add(a, b) -> float`
```python
add(1, 2)      # → 3.0
add(1, True)   # → ValidationError
```

#### `multiply(a, b) -> float`
```python
multiply(3, 4)  # → 12.0
```

#### `average(numbers: list) -> float`
```python
average([1, 2, 3])      # → 2.0
average([])             # → ValueError: Cannot calculate the average of an empty list.
average([1, "x", 3])   # → ValidationError
```

---

## Package Name Note

The installable package name on PyPI is `the_error_utils`, but you import it as `errorutils`:

```python
# pip install the_error_utils
import errorutils
```

## License

MIT — see [LICENSE](LICENSE) for details.
