import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) == 2:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            print(tabulize(sys.argv[1]))
    else:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

def tabulize(file):
    try:
        with open(file) as f:
            reader = csv.reader(f)
            rows = list(reader)
            if len(rows) == 0:
                sys.exit("Error: CSV file is empty")
            return tabulate(rows, headers="firstrow", tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
