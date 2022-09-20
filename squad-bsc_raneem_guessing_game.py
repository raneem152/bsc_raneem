secret_word = "raneem"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("please enter your guessing word: ")
        print('you have ' + str(guess_limit - 1 - guess_count) + ' turns left')
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of guesses, you lose :(")
else:
    print("you win :) ")


