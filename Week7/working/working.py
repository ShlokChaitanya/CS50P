import re

def main():
    print(convert(input("Enter hours (e.g., '12:30 PM to 4:45 PM'): ")))

def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + regex + " to " + regex + "$", s)
    if match:
        return f"{standardize(match.group(1), match.group(2), match.group(3))} to {standardize(match.group(4), match.group(5), match.group(6))}"
    else:
        raise ValueError("Invalid time format")

def standardize(hour, minute, period):
    hour = int(hour)
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0

    minute = int(minute) if minute is not None else 0
    return f"{hour:02d}:{minute:02d}"

if __name__ == "__main__":
    main()
