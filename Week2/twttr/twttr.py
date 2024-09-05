def main():
    usr_inp = input("Input: ")
    vowels = ["a", "e", "i", "o", "u"]

    for c in usr_inp:
        if c.casefold() not in vowels:
            print(c, end="")
    print()

if __name__ == "__main__":
    main()
