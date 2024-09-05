def main():
    months = [
        "January", "February", "March",
        "April", "May", "June", "July",
        "August", "September", "October",
        "November", "December"
    ]
    while True:
        usr_inp = input("Date: ")
        if date(usr_inp, months):
            break

def date(usr_inp, months):
    try:
        if "/" in usr_inp:
            mm, dd, yyyy = usr_inp.split("/")
        elif "," in usr_inp:
            mmdd, yyyy = usr_inp.split(", ")
            mm, dd = mmdd.split(" ")
            mm = (months.index(mm)) + 1
        else:
            raise ValueError

        if int(mm) > 12 or int(dd) > 31:
            raise ValueError
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        return True
    except (ValueError, IndexError):
        pass


main()
