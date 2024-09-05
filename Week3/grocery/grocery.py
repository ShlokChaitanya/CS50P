def main():
    grocery = {}
    while True:
        try:
            usr_inp = input().upper().strip()
            if usr_inp not in grocery:
                grocery[usr_inp] = 1
            else:
                grocery[usr_inp] = grocery[usr_inp] + 1
        except EOFError:
            sortedDict = dict(sorted(list(grocery.items())))
            printingList(sortedDict)
            break
        except KeyError:
            pass

def printingList(sortedDict):
    for usr_inp in sortedDict:
        print(sortedDict[usr_inp], usr_inp, sep=" ")

main()
