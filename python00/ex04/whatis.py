import sys


def main():
    argv = sys.argv
    if len(argv) < 2:
        return
    try:
        # assert が True の時は何も起きず、 False の時にエラー
        assert len(argv) == 2, "more than one argument is provided"

        try:
            num = int(argv[1])
        except ValueError:  # exept == catch
            # raise == throw
            raise AssertionError("argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError: {e}")

    if num % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")


if __name__ == "__main__":
    main()
