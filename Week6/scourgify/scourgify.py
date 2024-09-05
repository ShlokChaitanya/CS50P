import csv
import sys

def main():
    if len(sys.argv) == 3:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            clean(sys.argv[1], sys.argv[2])
    else:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")


def clean(inputFile, outputFile):
    try:
        with open(inputFile) as inputFile, open(outputFile, "w", newline="") as outputFile:
            reader = csv.DictReader(inputFile)
            writer = csv.DictWriter(outputFile, fieldnames=["first", "last", "house"])

            if {"name", "house"}.issubset(reader.fieldnames):
                writer.writeheader()
                for row in reader:
                    last_name, first_name = row["name"].strip().split(", ")
                    writer.writerow({"first": first_name, "last": last_name, "house": row["house"]})

    except FileNotFoundError:
        sys.exit("Input file does not exist.")


if __name__ == "__main__":
    main()
