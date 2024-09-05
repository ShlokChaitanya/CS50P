def main():
    price = 50
    coins = [25, 10, 5]
    totalPaid = 0
    while price > 0:
        print(f"Amount Due: {price}")
        userInput = int(input("Insert Coin: "))
        if userInput in coins:
            price -= userInput
            totalPaid += userInput
    changeOwed(totalPaid - 50)

def changeOwed(change):
    print(f"Change Owed: {change}")


if __name__ == "__main__":
    main()
