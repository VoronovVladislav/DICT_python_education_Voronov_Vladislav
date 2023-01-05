class CoffeeMachine:
    """CoffeeMachine simulator"""
    running = False

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money
        if not CoffeeMachine.running:
            self.start()

    def start(self):
        '''Menu of choices'''
        self.running = True
        self.action = input("Write action: <buy> <fill> <take> <remaining> <exit>\n")
        print()
        if self.action == "buy":
            self.buy()
        elif self.action == "fill":
            self.fill()
        elif self.action == "take":
            self.take()
        elif self.action == "exit":
            exit()
        elif self.action == "remaining":
            self.status()

    def return_to_menu(self):
        print()
        self.start()

    def available_check(self):
        self.not_available = ""
        if self.water - self.reduced[0] < 0:
            self.not_available = "water"
        elif self.milk - self.reduced[1] < 0:
            self.not_available = "milk"
        elif self.coffee_beans - self.reduced[2] < 0:
            self.not_available = "coffee beans"
        elif self.cups - self.reduced[3] < 0:
            self.not_available = "disposable cups"

        if self.not_available != "":
            print(f"Not enough {self.not_available}!")
            return False
        else:
            print("Making you a coffee!")
            return True

    def deduct_supplies(self):
        self.water -= self.reduced[0]
        self.milk -= self.reduced[1]
        self.coffee_beans -= self.reduced[2]
        self.cups -= self.reduced[3]
        self.money += self.reduced[4]

    def buy(self):
        '''Buying menu'''
        self.choice = input("What do you want to buy? <1> Espresso <2> Latte <3> Cappuccino <back> - main menu:\n")
        if self.choice == '1':
            self.reduced = [250, 0, 16, 1, 4]
            if self.available_check():
                self.deduct_supplies()

        elif self.choice == '2':
            self.reduced = [350, 75, 20, 1, 7]
            if self.available_check():
                self.deduct_supplies()

        elif self.choice == "3":
            self.reduced = [200, 100, 12, 1, 6]
            if self.available_check():
                self.deduct_supplies()

        elif self.choice == "back":
            self.return_to_menu()

        self.return_to_menu()

    def fill(self):
        '''Refill menu'''
        self.water += int(input("How many ml of water do you want to add:\n"))
        self.milk += int(input("How many ml of milk do you want to add:\n"))
        self.coffee_beans += int(input("How many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("How many disposable cups of coffee do you want to add:\n"))
        self.return_to_menu()

    def take(self):
        print(f"I gave you ${self.money}")
        self.money -= self.money
        self.return_to_menu()

    def status(self):
        '''Status of coffeemachine'''
        print(f"The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")
        self.return_to_menu()

CoffeeMachine(400, 540, 120, 9, 550)
