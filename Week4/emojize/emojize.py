import emoji

def main():
    usr_inp = input("Input: ").strip()
    print("Output: ", getEmoji(usr_inp))

def getEmoji(usr_inp):
    return emoji.emojize(usr_inp, language='alias')

main()
