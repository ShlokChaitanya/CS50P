def main():
    usr_inp = input("Expression: ")
    x, y, z = usr_inp.split(" ")
    calculate(int(x), y, int(z))

def calculate(x, y, z):
    if (y == "+"):
        print(float(x + z))
    elif (y == "-"):
        print(float(x - z))
    elif (y == "*"):
        print(float(x * z))
    elif (y == "/"):
        print(float(x / z))

main()
