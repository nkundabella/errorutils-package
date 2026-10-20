import logging
from functools import wraps
from typing import Any, Callable, Optional, TypeVar

logger = logging.getLogger("errorutils")

T = TypeVar("T")


class ErrorUtilsError(Exception):
    """Base exception for errors raised by errorutils."""


class ValidationError(ErrorUtilsError):
    """Raised when an input fails validation."""


def validate_number(value: Any, name: str = "value") -> float:
    """Check that a value is a real number, not a boolean."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValidationError(
            f"{name} must be a number, got {type(value).__name__}."
        )

    if value != value or value in (float("inf"), float("-inf")):
        raise ValidationError(f"{name} must be finite.")

    return float(value)


def safe_call(
    func: Callable[..., T],
    *args: Any,
    default: Optional[T] = None,
    **kwargs: Any,
) -> Optional[T]:
    """
    Run a function and log unexpected errors instead of propagating them.

    Returns the function's result if successful, or default if it fails.
    """
    try:
        return func(*args, **kwargs)
    except Exception:
        logger.exception("Function %s failed", func.__name__)
        return default


def check_not_none(value: Any, name: str = "value") -> Any:
    """Raise a clear error if a required value is None."""
    if value is None:
        raise ValidationError(f"{name} cannot be None.")
    return value


def log_error(message: str) -> None:
    """Record an error message using Python's logging system."""
    logger.error(message)


def catch_errors(
    func: Callable[..., T],
) -> Callable[..., Optional[T]]:
    """Decorator that logs unexpected errors and returns None on failure."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Optional[T]:
        return safe_call(func, *args, **kwargs)

    return wrapper