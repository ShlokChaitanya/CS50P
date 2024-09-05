def main():
    usr_inp = input("What is the Answer to the Great Question of Life, the Universe and Everything?").casefold()
    answerChecker(usr_inp)

def answerChecker(ans):
    if ans.__contains__("42") or ans.__contains__("forty two") or ans.__contains__("forty-two"):
        print("Yes")
    else:
        print("No")

main()
