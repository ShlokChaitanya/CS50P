def changeEmoji(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

usr_inp = input()
print(changeEmoji(usr_inp))
