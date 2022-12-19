print("Hello! My name is DICT_Bot.\nI was created in 2022.")

print("Please, remind me your name.")
username = input()
print("What's a great name you have," + username + "!")

print("Let me guess your age." "\nEnter remainders of diving your age by 3, 5 and 7.")
remainder3 = input("3:")
remainder5 = input("5:")
remainder7 = input("7:")
age = (int(remainder3) * 70 + int(remainder5) * 21 +int(remainder7) * 15) % 105
print("Your age is " + str(age) + ", that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
count_numbers = int(input(":"))
for number in range(count_numbers + 1):
    print(number, "!")
test = int(input("Let's test your programming knowledge." "\nWhy do we use methods?" "\n1. To repeat a statement multiple times." "\n2. To decompose a program into several small subroutines." "\n3. To determine the execution time of a program." "\n4. To interrupt the execution of a program." "\nYour answer:"))
if test != 2:
    test = int(input("Please, try again!"))
else:
    test = 2
    print("Congratulations, have a nice day!")
