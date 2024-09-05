def main():
    while True:
        try:
            usr_inp = input("Fraction: ")
            x, y = usr_inp.split("/")
            ratio = int(x)/ int(y)
            if 1 < ratio:
                raise ValueError
            getFraction(ratio)
            break
        except (ValueError, ZeroDivisionError):
            pass


def getFraction(ratio):
    if 0 <= ratio < 0.1:
        print("E")
    elif 0.9 <= ratio <= 1:
        print("F")
    elif 0.1 < ratio <0.9:
        print(str(round(ratio*100)) + "%")


main()
