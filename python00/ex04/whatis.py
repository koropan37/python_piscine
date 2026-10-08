import sys


def main():
    sys.tracebacklimit = 0  # Traceback message の削除
    argv = sys.argv
    if len(argv) < 2:
        return

    # assert が True の時は何も起きず、 False の時にエラー
    assert len(argv) == 2, "more than one argument is provided"

    try:
        num = int(argv[1])
    except ValueError:  # exept == catch
        # raise == throw, from None で後ろだけ
        raise AssertionError("argument is not an integer") from None

    if num % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")


if __name__ == "__main__":
    main()
