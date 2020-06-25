class CoffeeMachine:

    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.is_stop = False

        # 0 - choosing an action
        # 1 - choosing an coffee type
        # 2 - buy
        # 3 - fill
        # 4 - fill water
        # 5 - fill milk
        # 6 - fill coffee
        # 7 - fill cups
        # 8 - take
        # 9 - remaining
        # 0 - exit
        self.statement = 0
        self.action = None

    def run(self, command=""):

        if command == "buy":
            self.statement = 1

        elif command == "fill":
            print("#fill")
            self.statement = 3

        elif command == "take":
            print("#take")
            self.statement = 8

        elif command == "remaining":
            print("#remaining")
            self.statement = 9

        elif command == "back":
            self.statement = 0

        if self.statement == 0:  # choosing an action
            print("Write action (buy, fill, take, remaining, exit):")

        elif self.statement == 1:  # choosing an coffee type
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            self.statement = 2

        elif self.statement == 2:  # buy
            coffee_variant = command

            if coffee_variant != "back":
                need_cups = 1
                coffee_variant = int(coffee_variant)
                if coffee_variant == 1:  # Эспрессо
                    need_water = 250
                    need_milk = 0
                    need_coffee = 16
                    price = 4
                elif coffee_variant == 2:  # Латте
                    need_water = 350
                    need_milk = 75
                    need_coffee = 20
                    price = 7
                elif coffee_variant == 3:  # Капучино
                    need_water = 200
                    need_milk = 100
                    need_coffee = 12
                    price = 6
                else:
                    print("Error: Unknown variant.")
                    return

                if self.water < need_water:
                    print("No, I don't nave water")
                    return
                elif self.milk < need_milk:
                    print("No, I don't nave milk")
                    return
                elif self.coffee < need_coffee:
                    print("No, I don't have coffee beans")
                    return
                elif self.cups < need_cups:
                    print("No, I don't have disposable cups")
                    return
                else:
                    self.money += price
                    self.water -= need_water
                    self.milk -= need_milk
                    self.coffee -= need_coffee
                    self.cups -= need_cups

            print("Write action (buy, fill, take, remaining, exit):")
            self.statement = 0  # Переводим в начальное состояние

        elif self.statement == 3:  # fill
            print("Write how many ml of water do you want to add:")
            self.statement = 4

        elif self.statement == 4:  # fill water
            self.water += int(command)
            print("Write how many ml of milk do you want to add:")
            self.statement = 5

        elif self.statement == 5:  # fill milk
            self.milk += int(command)
            print("Write how many grams of coffee beans do you want to add:")
            self.statement = 6

        elif self.statement == 6:  # fill coffee
            self.coffee += int(command)
            print("Write how many disposable cups of coffee do you want to add:")
            self.statement = 7

        elif self.statement == 7:  # fill cups
            self.cups += int(command)
            self.statement = 0

        elif self.statement == 8:  # take
            print("I gave you $", self.money)
            self.money = 0
            print("Write action (buy, fill, take, remaining, exit):")
            self.statement = 0

        elif self.statement == 9:  # remaining
            print("The coffee machine has:")
            print(self.water, "of water")
            print(self.milk, "of milk")
            print(self.coffee, "of coffee beans")
            print(self.cups, "of disposable cups")
            print(self.money, "of money")

            print("Write action (buy, fill, take, remaining, exit):")
            self.statement = 0

        else:
            print("Неправильное действие")
            self.statement = 0


machine = CoffeeMachine()
print("Write action (buy, fill, take, remaining, exit):")
while True:
    cmd = input().strip()
    if cmd == "exit":
        break
    machine.run(cmd)