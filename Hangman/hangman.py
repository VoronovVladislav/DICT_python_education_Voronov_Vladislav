from random import choice
import sys

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
    elif guess == "0":
        sys.exit("Restart the game!")
    elif guess == guess.upper():
        sys.exit("Turn capslock off or don't use numbers and start again!")

    while guess in used_words:
        print("You already used the letter", guess, "!")
        guess = input("Enter your answer:")

    used_words.append(guess)

    if guess in answer:
        print("Excellent! Letter " + guess + " is in the word.")

        new = ''
        for x in range(len(answer)):
            if guess == answer[x]:
                new += guess
            else:
                new += far[x]
        far = new
    else:
        print("\nNo letter " + guess + " in the word.")
        wrong += 1

if wrong == max_wrongs:
    print("\nYou lost!")

else:
    print("\nYou won!")

print("The hidden word was - " + answer)
