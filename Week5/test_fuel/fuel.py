def main():
    usr_inp = input("Fraction: ")
    pta = convert(usr_inp)
    print(gauge(pta))

def convert(fraction):
    int(x), int(y) = (fraction.split("/"))
    if x/y > 1:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    return int((x/y)* 100)

def gauge(percentage):
    try:
        if 0 <= percentage <= 1:
            return "E"
        elif 99 <= percentage <= 100:
            return "F"
        elif 1 < percentage < 99:
            return f"{int(percentage)}%"
        else:
            raise TypeError
    except TypeError:
        pass

main()
