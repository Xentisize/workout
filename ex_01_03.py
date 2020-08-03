# Run timing
from typing import List, Tuple
from decimal import *


def run_time() -> Tuple[float, int]:
    """Enter the time and return the average time."""
    times: List[float] = []

    while True:
        try:
            time = float(input("Enter 10 km runtime: "))
            times.append(time)
        except ValueError:
            break
    return sum(times) / len(times), len(times)


def extract_float(value: float, before: int, after: int) -> float:
    """Split a decimal according to the arguments before and after."""
    float_in_str: List[str] = str(value).split(".")
    whole_part: str = float_in_str[0][::-1]
    fraction_part: str = float_in_str[1]
    extracted_str: str = whole_part[:before][::-1] + "." + fraction_part[:after]
    extracted_float: float = 0.0
    try:
        extracted_float = float(extracted_str)
    except ValueError as e:
        print(e)
    return extracted_float


def float_sum(first_float: str, second_float: str) -> Decimal:
    """Return a precise summation of float."""
    first_val = Decimal()
    second_val = Decimal()
    try:
        first_val = Decimal(first_float)
        second_val = Decimal(second_float)
    except InvalidOperation as e:
        print(e)
    return first_val + second_val


if __name__ == "__main__":
    result: Tuple = run_time()
    print(f"Average of {result[0]:.2f}, over {result[1]} runs")
    print(extract_float(1234.5678, 2, 3))
    print(float_sum(".01", ".2"))
