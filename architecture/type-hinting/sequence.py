from typing import Sequence

def calculate_total(items: Sequence[float]) -> float:
    return sum(items)

print(calculate_total([1.0, 2.0, 3.0]))
print(calculate_total((1.0, 2.0, 3.0)))