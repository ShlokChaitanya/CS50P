import random

def main():
    eqn_cnt = 10
    score = 0
    chances = 3
    lvl = get_level()
    while eqn_cnt != 0:
        if chances == 3:
            x, y = generate_integer(lvl)
        try:
            usr_inp = int(input(f"{x} + {y} = "))
            ans = x + y
            if usr_inp == ans:
                eqn_cnt -= 1
                score += 1
                chances = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances -= 1
            pass
        if chances == 0:
            print((f"{x} + {y} = {ans}"))
            chances = 3
            eqn_cnt -= 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n and n <= 3:
                return n
        except:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999), random.randint(100, 999)


if __name__ == "__main__":
    main()
