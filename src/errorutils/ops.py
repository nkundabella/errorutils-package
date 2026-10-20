
from .core import validate_number


def add(a: float, b: float) -> float:
    """Add two numbers after validating their inputs."""
    a = validate_number(a, "a")
    b = validate_number(b, "b")
    return a + b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers after validating their inputs."""
    a = validate_number(a, "a")
    b = validate_number(b, "b")
    return a * b


def average(numbers: list) -> float:
    """Calculate the average of a non-empty list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")

    validated = [
        validate_number(number, f"numbers[{i}]")
        for i, number in enumerate(numbers)
    ]

    return sum(validated) / len(validated)