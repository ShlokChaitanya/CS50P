import inflect

p = inflect.engine()
name_list = []

def main():
    while True:
        try:
            usr_inp = input("Name: ").strip().title()
            name_list.append(usr_inp)
        except EOFError:
            print(f"\nAdieu, adieu, to {p.join(name_list)}")
            break


main()
