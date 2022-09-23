import random

# random hardcoded words
random_words = ["vortex", "robotics", "academy", "python", "track"]
# choosing a random word
secret_word = random.choice(random_words)
wrong_guesses = 8
letters = []
all_guesses = []
print("your valid wrong letters are 8 only")

while wrong_guesses > 0:
    guess = input("enter a letter: ")
    if guess.__len__() != 1:
        try:
            raise Exception()
        except:
            print("please enter one letter!!")
            continue

    if all_guesses.__contains__(guess):
        print("Please Don't enter same char twice ")
        continue
    if secret_word.__contains__(guess):
        print("correct guess")
        letters.append(guess)
        all_guesses.append(guess)
        if letters.__len__() == secret_word.__len__():
            print("congrats , YOU WIN")
            print("The word is " + secret_word)
            break
        else:
            letter = secret_word.__len__() - letters.__len__()
            print(str(letter) + " letters left to be gussesed")
    else:
        wrong_guesses -= 1
        print("wrong guess")
        all_guesses.append(guess)
        if wrong_guesses == 0:
            print("YOU LOSE")
            print("the word was " + secret_word)
        else:
            print("you have " + str(wrong_guesses) + " chances")