def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in"AEIOUaeiou":
            translation=translation+"v"
        else:
            translation=translation+letter
    return translation
print(translate(input("please enter the phrase: ")))
