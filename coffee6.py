# Write your code here
class CoffeeMachine:
    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def message(self):
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.cups))
        print("${} of money".format(self.money))

    def buy_coffee(self, co_water, co_milk, co_beans, co_cups, co_money):
        if self.water < co_water:
            print("Sorry, not enough water!")
            return
        elif self.milk < co_milk:
            print("Sorry, not enough milk!")
            return
        elif self.beans < co_beans:
            print("Sorry, not enough coffee beans!")
            return
        elif self.cups < co_cups:
            print("Sorry, not enough disposable cups!")
            return
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= co_water
            self.milk -= co_milk
            self.beans -= co_beans
            self.cups -= co_cups
            self.money += co_money

    def espresso(self):
        e_water = 250
        e_milk = 0
        e_beans = 16
        e_cups = 1
        e_money = 4
        self.buy_coffee(e_water, e_milk, e_beans, e_cups, e_money)

    def latte(self):
        l_water = 350
        l_milk = 75
        l_beans = 20
        l_cups = 1
        l_money = 7
        self.buy_coffee(l_water, l_milk, l_beans, l_cups, l_money)

    def cappuccino(self):
        c_water = 200
        c_milk = 100
        c_beans = 12
        c_cups = 1
        c_money = 6
        self.buy_coffee(c_water, c_milk, c_beans, c_cups, c_money)

    def buy(self):
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee = input()
        if coffee == "back":
            return
        elif int(coffee) == 1:
            self.espresso()
        elif int(coffee) == 2:
            self.latte()
        elif int(coffee) == 3:
            self.cappuccino()

    def fill(self):
        print("Write how many ml of water the coffee machine has:")
        ml_water = int(input())
        print("Write how many ml of milk the coffee machine has:")
        ml_milk = int(input())
        print("Write how many grams of coffee beans the coffee machine has:")
        gm_beans = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        n_cups = int(input())
        self.water += ml_water
        self.milk += ml_milk
        self.beans += gm_beans
        self.cups += n_cups

    def take(self):
        print()
        print("I gave you ${}".format(self.money))
        self.money = 0

my_machine = CoffeeMachine()
while True:
    print()
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == "buy":
        my_machine.buy()
    elif action == "fill":
        my_machine.fill()
    elif action == "take":
        my_machine.take()
    elif action == "remaining":
        print()
        my_machine.message()
    elif action == "exit":
        break
