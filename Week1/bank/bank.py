def main():
    usr_inp = input("Greeting: ").strip().capitalize()
    checkIn(usr_inp)

def checkIn(g):
    if g.startswith("Hello"):
        print("$0")
        return
    elif g.startswith("H"):
        print("$20")
    else:
        print("$100")

main()
