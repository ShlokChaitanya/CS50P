import sys

def main():
    if len(sys.argv) == 2:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a python file")
        else:
            print(countLines(sys.argv[1]))
    else:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")


def countLines(file):
    try:
         with open(file, "r") as file:
            return sum(1 for line in file if not (line.lstrip().startswith("#") or line.strip() == ""))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
