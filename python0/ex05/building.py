import sys
import string


def main():
    """Docstring for main."""

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    if len(sys.argv) == 2 and sys.argv[1]:
        text = sys.argv[1]
    else:
        try:
            print("What is the text to count?")
            text = sys.stdin.readline()  # input()は'\n' がないため readline()
        except EOFError:
            return

    upper_cnt = 0
    lower_cnt = 0
    digit_cnt = 0
    space_cnt = 0
    punctuation_cnt = 0

    for char in text:
        if char.isupper():
            upper_cnt += 1
        elif char.islower():
            lower_cnt += 1
        elif char.isdigit():
            digit_cnt += 1
        elif char.isspace():
            space_cnt += 1
        elif char in string.punctuation:
            punctuation_cnt += 1

    print(f"The text contains {len(text)}  characters:")
    print(f"{upper_cnt} upper letters")
    print(f"{lower_cnt} lower letters")
    print(f"{punctuation_cnt} punctuation marks")
    print(f"{space_cnt} spaces")
    print(f"{digit_cnt} digits")


if __name__ == "__main__":
    main()
