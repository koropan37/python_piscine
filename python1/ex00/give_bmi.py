import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Calculate BMI values from height and weight lists."""
    try:
        if type(height) is not list or type(weight) is not list:
            raise TypeError("Both height and weight must be lists.")
        if len(height) != len(weight):
            raise ValueError("Both height and weight must be the same size.")
        for h, w in zip(height, weight):  # zip で複数の対応する要素を受け取れる
            if type(h) not in (int, float) or type(w) not in (int, float):
                raise TypeError("Elements must be int or float.")
            if h <= 0 or w <= 0:
                raise ValueError("Height and weight must be greater than 0.")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None

    height_arr = np.array(height)
    weight_arr = np.array(weight)
    bmi = weight_arr / (height_arr ** 2)
    return bmi.tolist()  # bmi は numpy.ndarry 型なので list に変換


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check if BMI values exceed the limit."""
    try:
        if type(bmi) is not list:
            raise TypeError("bmi must be a list.")
        if type(limit) is not int:
            raise TypeError("limit must be an integer.")
        if limit <= 0:
            raise ValueError("limit must be greater than 0.")
        for val in bmi:
            if type(val) not in (int, float):
                raise TypeError("All BMI elements must be int or float.")

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None

    bmi_arr = np.array(bmi)
    res = bmi_arr > limit
    return res.tolist()
