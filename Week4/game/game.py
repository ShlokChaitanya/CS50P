import random

def main():
    while True:
        try:
            usr_inp = int(input("Level: "))
            x = random.randint(1, usr_inp)
            while True:
                guess = get_guess()
                if check_guess(guess, x):
                    raise EOFError
        except ValueError:
            pass
        except EOFError:
            break

def get_guess():
    return int(input("Guess: "))

def check_guess(guess, x):
    if guess > x:
        print("Too large!")
        return False
    elif guess < x:
        print("Too small!")
        return False
    elif guess == x:
        print("Just right!")
        return True

if __name__ == "__main__":
    main()
