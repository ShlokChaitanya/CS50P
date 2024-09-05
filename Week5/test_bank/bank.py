def main():
    usr_inp = input("Greeting: ").strip().capitalize()
    print(f"${value(usr_inp)}")

def value(g):
    if g.startswith("Hello"):
        return 0
    elif g.startswith("H"):
        return 20
    else:
        return 100

main()
