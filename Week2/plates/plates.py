def main():
    usr_inp = input("Plate: ")
    if is_valid(usr_inp):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        if s.isalpha():
            return True
        elif s[0].isalpha() and s[-1].isdigit():
            for i in range(1, len(s) - 1):
                if s[i].isdigit() and (s[i] == "0" or s[i+1].isalpha()):
                    return False
            return True
    return False

main()
