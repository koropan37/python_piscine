import sys


def main():
    """Docstring for main."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        try:
            num = int(sys.argv[2])
        except ValueError:
            raise AssertionError("argument are bad")

    except AssertionError as e:
        print(f"AssertionError: {e}")

    text = sys.argv[1]
    words = [word for word in text.split() if len(word) > num]
    # if len(word) > num が True の word を words に
    print(words)

    # lambda の書き方 (flake8 ではダメ)
    # check = lambda w: len(w) > num
    # result = [w for w in text.split() if check(w)]


if __name__ == "__main__":
    main()
