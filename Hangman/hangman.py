import random

def hangman():
    print("<<HANGMAN>>""\nThe game will be available soon.")

    wordlist = ['python', 'java', 'php', 'rust', 'c', 'go', 'pascal', 'limbo']
    secret = random.choice(wordlist)
    guesses = 'hvsoi'
    turns = 5

    while turns > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                missed += 1

        if missed == 0:
            print('\nYou win!')
            break

        guess = input('\nCall the letter:')
        guesses += guess

        if guess not in secret:
            turns -= 1
            print('Did not guess.')
            print('\n', 'Your turns:', turns)
            if turns < 5: print ('\n  |  ')
            if turns < 4: print('  O  ')
            if turns < 3: print(' /|\ ')
            if turns < 2: print('  |  ')
            if turns < 1: print(' / \ ')
            if turns == 0: print('\n\nThats word is:', secret)

ans = 'yes'
while ans == 'yes':
    hangman()
    print('Do you want play again? (yes or no).')
    ans = input()