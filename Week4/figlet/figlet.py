import random as RAN
import pyfiglet as fig
import  sys


figlet = fig.Figlet()
fonts = figlet.getFonts()


def main():
    if len(sys.argv) > 3 or len(sys.argv) > 1 and len(sys.argv) < 3:
        print('Invalid usage')
        sys.exit(1)

    if len(sys.argv) == 3:
        font = sys.argv[2]
        fontFlag = sys.argv[1]
        handleCommandArgs(font, fontFlag)
    else:
        rand_num = RAN.randint(0,len(fonts))
        printPrompt(fonts[rand_num])

def handleCommandArgs(font, font_flag):
    if font not in fonts:
        print('Invalid usage')
        sys.exit(1)

    if font_flag not in ['-f','--font']:
        print('Invalid usage')
        sys.exit(1)
    printPrompt(font)

def printPrompt(fonts):
    figlet.setFont(font=fonts)
    user_input = input("Input: ")
    print(figlet.renderText(user_input))
    sys.exit(0)

main()
