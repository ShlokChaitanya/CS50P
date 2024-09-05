from PIL import Image, ImageOps
import sys
import os


def main():
    if len(sys.argv) == 3:
        format = [".jpg", ".jpeg", ".png"]
        inp = os.path.splitext(sys.argv[1])
        outp = os.path.splitext(sys.argv[2])
        if outp[1].lower() not in format:
            sys.exit("Invalid output")
        elif inp[1].lower() != outp[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            editPhoto(sys.argv[1], sys.argv[2])
    else:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")


def editPhoto(input, output):
    shirt = Image.open("shirt.png")
    try:
        with Image.open(input) as input:
            inputCropped = ImageOps.fit(input, shirt.size)
            inputCropped.paste(shirt, mask = shirt)
            inputCropped.save(output)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")


if __name__ == "__main__":
    main()
