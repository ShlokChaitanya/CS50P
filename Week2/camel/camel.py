def main():
    usr_inp = input("camelCase: ")
    print("snake_case: ", formatChanger(usr_inp))

def formatChanger(camel):
    snake_case = ""
    for c in camel:
        if c.islower():
            snake_case += c
        if c.isupper():
            snake_case += "_" + c.lower()
    return snake_case

if __name__ == "__main__":
    main()
