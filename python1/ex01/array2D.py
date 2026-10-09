import numpy as np


def validate_input(family: list, start: int, end: int) -> None:
    """Validate that input parameters for slice_me are valid."""
    if type(family) is not list or len(family) == 0:
        raise TypeError("family must be a non-empty list.")
    if type(start) is not int or type(end) is not int:
        raise TypeError("Both start and end must be integers.")

    row_len = None
    for row in family:
        if type(row) is not list or len(row) == 0:
            raise TypeError("Each row must be a non-empty list.")
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise ValueError("All rows must have the same size.")
        for item in row:
            if type(item) not in (int, float):
                raise TypeError("All elements must be int or float.")


def slice_me(family: list, start: int, end: int) -> list:
    """Print shape of a 2D array and return its sliced version."""
    try:
        validate_input(family, start, end)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None

    arr = np.array(family)
    print(f"My shape is : {arr.shape}")  # shape で tuple 形式で取得
    sliceed_arr = arr[start:end]  # start ~ end-1 までの行を取り出す
    print(f"My new shape is : {sliceed_arr.shape}")
    return sliceed_arr.tolist()
