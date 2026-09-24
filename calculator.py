def add(left: int, right: int) -> int:
    return left + right


def divide(left: float, right: float) -> float:
    if right == 0:
        raise ValueError("Cannot divide by zero")
    return left / right

