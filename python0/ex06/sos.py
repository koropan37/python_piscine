import sys


def main():
    """Docstring for main."""
    morse = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",
        " ": "/",
    }
    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        str_to_morse = []
        for char in sys.argv[1].upper():
            if char in morse:
                str_to_morse.append(morse[char])
            else:
                raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    print(" ".join(str_to_morse))  # .join で前の str を連結


if __name__ == "__main__":
    main()
