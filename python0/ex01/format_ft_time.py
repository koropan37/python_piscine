import time
import datetime


def main():
    sec = time.time()
    print(f"Seconds since January 1, 1970: {sec:,.4f} "  # ,区切りで4桁までの少数
          f"or {sec:.2e} in scientific notation")  # 2桁の少数 + e
    today = datetime.date.today()
    print(today.strftime("%b %d %Y"))


if __name__ == "__main__":
    main()
