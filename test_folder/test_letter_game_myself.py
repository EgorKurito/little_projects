import os
import random
import sys

words = [
    'egor',
    'dima',
    'artur',
    'oleg',
    'artom'
]

good_guesses = []
bad_guesses = []

def clear():
    if os.name == 'nt':
        os.system('clsr')
    else:
        os.system('clear')

def draw(good_guesses, bad_guesses, secret_word):
    clear()

    print("{}/7".format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter, end = '')
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end = '')
        else:
            print('_', end ='')

    print('')

def take_guess(good_guesses, bad_guesses):
    while True:
        guess = input("Guess a letter ").lower()

        if len(guess) != 1:
            print("Please guess only 1 letter")
        elif guess in bad_guesses or guess in good_guesses:
            print("You guess this letter yet. Guess different letter")
        elif not guess.isalpha():
            print("You can only guess letter ")
        else:
            return guess

def welcome():
    start = input("Press enter/return to start or Q to quit ").lower()
    if start == 'q':
        print("Bye!")
        sys.exit()
    else:
        return True

def play(done):
    clear()
    secret_word = random.choice(words)
    good_guesses = []
    bad_guesses = []
    while True:
        draw(good_guesses, bad_guesses, secret_word)
        guess = take_guess(good_guesses, bad_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False

            if found:
                print("You win!")
                print("The word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(good_guesses, bad_guesses, secret_word)
                print("You lost!")
                print("The word was {}".format(secret_word))
                done = True

        if done:
            play_again =input("Play again Y/n").lower()
            if play_again != 'n':
                return play(done = False)
            else:
                sys.exit()

print("Welcome")
done = False

while True:
    clear()
    welcome()
    play(done)
