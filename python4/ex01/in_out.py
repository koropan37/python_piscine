def square(x: int | float) -> int | float:
    """Return the exponentiation of the argument."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return the exponentiation of the argument by itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return an inner function that tracks calculation state."""
    count = x  # 変数の初期値を設定

    def inner() -> float:
        """Execute the function and update the state."""
        nonlocal count  # ネストの外側の変数を変更するために使用
        count = function(count)
        return count

    return inner  # count を記憶、更新したもの(クロージャ)
