from collections.abc import Callable  # callable = 関数やクラス
from typing import Any


def callLimit(limit: int) -> Callable:  # 設定を受け取る
    """Limit the number of function calls."""
    count = 0

    def callLimiter(function: Callable) -> Callable:  # 関数を受け取る
        """Decorator to limit function calls."""

        def limit_function(*args: Any, **kwds: Any) -> Any:  # 関数を実行
            """Set a call limit for a function."""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} called too many times")
                return None
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter
