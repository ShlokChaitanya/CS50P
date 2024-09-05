def main():
    usr_inp = input("Input: ")
    print(shorten(usr_inp))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    shortened = []
    for c in word:
        if c.casefold() not in vowels:
            shortened.append(c)
    return str("".join(shortened))

if __name__ == "__main__":
    main()
