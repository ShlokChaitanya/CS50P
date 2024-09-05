from datetime import date
import inflect
import sys
import operator

p = inflect.engine()


def main():
    try:
        difference = operator.sub(date.today(), date.fromisoformat(input("Date of Birth: ")))
        print(minutes(difference.days))
    except ValueError:
        sys.exit("Invalid date")


def minutes(time):
    minu = time * 24 * 60
    ans = p.number_to_words(minu, andword='')
    return f"{ans.capitalize()} minutes"


if __name__ == "__main__":
    main()
