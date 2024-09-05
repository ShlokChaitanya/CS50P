def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    calculateBill(menu)

def calculateBill(menu):
    price = 0
    while True:
        try:
            usr_inp = input("Item: ").title().strip()
            if usr_inp in menu:
                price += menu[usr_inp]
                print(f"Total: ${price:.2f}")
        except EOFError:
            print()
            break
        except KeyError:
            pass

main()
