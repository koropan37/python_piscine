from typing import Any


def validate_args(args: Any) -> None:
    """Validate args data"""
    for x in args:
        if type(x) not in (int, float):
            raise TypeError("Args accepts only numbers")


def calc_mean(data: list) -> float:
    """Calculate the mean of a list of numbers."""
    return sum(data) / len(data)


def calc_median(data: list) -> float | int:
    """Calculate the median of a list of numbers."""
    mid = len(data) // 2
    if len(data) % 2 != 0:
        return data[mid]
    return (data[mid - 1] + data[mid]) / 2


def calc_quartile(data: list) -> list:
    """Calculate the quartile(25% and 75%) of a list of numbers."""
    q1 = float(data[int(len(data) * 0.25)])
    q3 = float(data[int(len(data) * 0.75)])
    return [q1, q3]


def calc_var(data: list) -> float:
    """Calculate the variance of a list of numbers."""
    mean = calc_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


def calc_std(data: list) -> float:
    """Calculate the standard deviation of a list of numbers."""
    return calc_var(data) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculate and display statistics based on kwargs."""
    if not args:
        for _ in kwargs:
            print("ERROR")
        return

    try:
        validate_args(args)
        data = sorted(args)

        for word in kwargs.values():
            if word == "mean":
                print(f"mean : {calc_mean(data)}")
            elif word == "median":
                print(f"median : {calc_median(data)}")
            elif word == "quartile":
                print(f"quartile : {calc_quartile(data)}")
            elif word == "std":
                print(f"std : {calc_std(data)}")
            elif word == "var":
                print(f"var : {calc_var(data)}")

    except Exception:
        print("ERROR")
