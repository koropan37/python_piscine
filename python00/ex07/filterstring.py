import sys


def main():
    sys.tracebacklimit = 0

    assert len(sys.argv) == 3, "the arguments are bad"

    text = sys.argv[1]
    try:
        num = int(sys.argv[2])
    except ValueError:
        raise AssertionError("argument are bad") from None

    words = [word for word in text.split() if len(word) > num]
    # if len(word) > num が True の word を words に
    print(words)

    # lambda の書き方 (flake8 ではダメ)
    # check = lambda w: len(w) > num
    # result = [w for w in text.split() if check(w)]


if __name__ == "__main__":
    main()
