"""Shared Cost Program"""
import random
import sys

print("Enter the number of friends who joined, including you: ")
quantity_firends = int(input())

if quantity_firends <=0:
    print('Nobody joined the party.')
    sys.exit(0)

print("Enter the name of each friend including you, each on a new line: ")
names_list = {}
for i in range(quantity_firends):
    input_person = input("> ")
names_list.update({f"{input_person}": 0})

input_amount = int(input("Enter the total amount\n> "))

choice_lucky = input("Want to use the 'Who's Lucky?' feature? Write yes/no:" "\n> ")
lucky = random.choice(list(names_list))
if choice_lucky == "yes":
    quantity_firends -= 1
    print(f"{lucky} is the lucky one!")
else:
    print("No one is going to be lucky")

amount_person = round((input_amount / quantity_firends), 2)
for key in names_list:
    if key == lucky and choice_lucky.lower() == 'yes':
        names_list[key] = 'is the lucky one!'
    else:
        names_list[key] = amount_person

print(names_list)