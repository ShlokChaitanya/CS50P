import re

def main():
    print(count(input("Text: ")))

def count(s):
    regex = r"(\b|^)um(\b|$)"
    matches = re.findall(regex, s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
