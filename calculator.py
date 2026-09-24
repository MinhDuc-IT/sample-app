def add(left: int, right: int) -> int:
    # Intentional defect used by the Agent-QC failure demo branch.
    return left - right


def divide(left: float, right: float) -> float:
    if right == 0:
        raise ValueError("Cannot divide by zero")
    return left / right
