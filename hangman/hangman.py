from random import choice
import sys

'''This code is an example of using the random function'''

print("<<HANGMAN>>" "\nThe game will be available soon.")
print("START" "\nPress '1' to play game.")
print("EXIT" "\nIf you want to exit press '0'.")

user_input = int(input(":"))
if user_input == 0:
    sys.exit("See ya later!")

max_wrongs = 7
words_dictionary = ('python', 'java', 'javascript', 'php', 'rust', 'csharp', 'windows', 'linux', 'notebook', 'computer')
answer = choice(words_dictionary)
far = '-' * len(answer)
wrong = 0
used_words = []

while wrong < max_wrongs and far != answer and user_input == 1:

    print("\nUsed letters:\n", used_words)
    print("\nGuess the word:\n", far)

    guess = input("\nEnter your answer:")

    if len(guess) > 1:
        sys.exit("You must enter one letter.Try again!")