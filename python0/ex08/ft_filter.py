def ft_filter(function, iterable):
    ("Return an iterator yielding those items of iterable for which "
        "function(item)\nis true. If function is None, "
        "return the items that are true.")
    if function is None:
        for item in iterable:
            if item:
                yield item
    else:
        for item in iterable:
            if function(item):
                yield item

    # yield: 関数の状態を保持して停止し、再度処理を再開する(遅延評価)
    # yield を含む関数は「ジェネレーター関数」という
    # 一度に全ての計算をせず、値を一つずつ取り出せるためメモリ効率がいい
    # for 文は、裏側で next()を呼び続け,StopIteration(例外)が発生した瞬間に
    # それを自動でキャッチして静かにループを終了する
