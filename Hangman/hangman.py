import random
'''This module is add the random choices in code'''

def game():
    print("<<<HANGMAN>>>""\n<<<The game will be available soon.>>>")
    words = ['python', 'java', 'javascript', 'php']

    picked = random.choice(words)

    print('In this word', len(picked), 'letters')

    right = ['_'] * len(picked)
    wrong = []

    def update():
        for x in right:
            print(x, end=' ')
        print()

    update()

    while True:

        guess = input(": ")

        if guess in picked:
            index = 0
            for i in picked:
                if i == guess:
                    right[index] = guess
                index += 1
            update()

        else:
            if guess not in wrong:
                wrong.append(guess)
            else:
                print('This letter is used.')
            print(wrong)
        if len(wrong) > 8:
            print('You lost!')
            print('This word is', picked)
            break
        if '_' not in right:
            print('You survived!')
            break


def menu():
    print("To start game input '1'")
    print("To exit input '0'")


menu()
user_input = input(": ")
while user_input != "user_input":
    if user_input == "1":
        game()
        pass
    elif user_input == "0":
        exit()
    else:
        print("Ivalid input!")

    menu()
    user_input = input("Write correct choice to start is '1', to exit '0': ")