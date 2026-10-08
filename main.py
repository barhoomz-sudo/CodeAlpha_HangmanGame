import random

word = random.choice(["Netflix", "Amazon", "Google", "Meta", "Microsoft"])
guesses = 6
user_word = ''
while guesses > 0:
    user_input = input("Guess the word (one letter): ")
    # input validation
    if len(user_input) > 1:
        print("Only one letter at a time!")
        break

    if user_input == '':
        print("no whitespace allowed!")
        break

    # adding each letter user enter to a variable
    user_word += user_input

    # if the user guessed incorrect
    
    if (len(user_word.title()) == len(word) and user_word.title() != word) or len(user_word.title()) > len(word):
        if guesses > 1:
            guesses -= 1
            user_word = ''
            print(f"wrong, try again {guesses} attempts left")
            continue
        # once the guesses reaches 0, declare that the user lost and exit the game
        else:
            print(f"You lost. the word was {word}")
            break
    # if the user guessed correct
    elif len(user_word.title()) == len(word) and user_word.title() == word:
        print(f"You won!, the word is {word}")
        break