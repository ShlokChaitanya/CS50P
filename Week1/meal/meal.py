def main():
    usr_inp = input("What time is it?: ")
    checkMeal(convert(usr_inp))


def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60


def checkMeal(hour):
    if 7 <= hour <= 8:
        print("breakfast", "time")
    elif 12.0 <= hour <= 13.0:
        print("lunch", "time")
    elif 18.0 <= hour <= 19.0:
        print("dinner", "time")

if __name__ == "__main__":
    main()
