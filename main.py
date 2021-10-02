MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
}

resources["money"] = 0
money_collected = 0
remaining_water = 0
remaining_milk = 0
remaining_coffee = 0


def coffee_choice(user_choice):
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        global remaining_water
        remaining_water = resources["water"] - MENU[user_choice]["ingredients"]["water"]
        global remaining_milk
        remaining_milk = resources["milk"] - MENU[user_choice]["ingredients"]["milk"]
        global remaining_coffee
        remaining_coffee = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]
        global money_collected
        money_collected = MENU[user_choice]["cost"] + resources["money"]


def resources_update(resources):
    global water
    resources["water"] = remaining_water
    global milk
    resources["milk"] = remaining_milk
    global coffee
    resources["coffee"] = remaining_coffee
    global money
    resources["money"] = money_collected


def money_calculate(quarters, dimes, nickles, pennies):
    sum_quarters = float(quarters * 0.25)
    sum_dimes = float(dimes * 0.1)
    sum_nickles = float(nickles * 0.05)
    sum_pennies = float(pennies * 0.01)

    total_sum = sum_quarters + sum_dimes + sum_nickles + sum_pennies
    return total_sum


def compare(total_money):
    if total_money == MENU[user_choice]["cost"]:
        return 0
    elif total_money >= MENU[user_choice]["cost"]:
        return total_money - MENU[user_choice]["cost"]
    elif total_money <= MENU[user_choice]["cost"]:
        return total_money - MENU[user_choice]["cost"]


def resource_check(remaining_water, remaining_milk, remaining_coffee):
    if remaining_water < 0:
        return "water"
    elif remaining_milk < 0:
        return "milk"
    elif remaining_coffee < 0:
        return "coffee"

something = True
while something:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        coffee_choice(user_choice)
        if remaining_water >= 0 and remaining_milk >= 0 and remaining_coffee >= 0:

            print("Please insert coins.")

           quarters = int(input("how many quarters?: "))
           dimes = int(input("how many dimes?: "))
           nickles = int(input("how many nickles?: "))
           pennies = int(input("how many pennies?: "))

            total_money = money_calculate(quarters, dimes, nickles, pennies)

            result = compare(total_money)

            if result > 0:
                print(f"Here is ${result} in change.")
                print(f"Here is your {user_choice} ☕. Enjoy!")
                resources_update(resources)
            elif result == 0:
                print(f"Here is your {user_choice} ☕. Enjoy!")
                resources_update(resources)
            else:
                print("Sorry that's not enough money. Money refunded.")
            """
            option 1 - either open the below else statement but then you have to comment below 3 elif statement.
            or option 2 - either open the below 3 elif statement but then you have to comment below else statement and 
            also you have to comment function defined as - def resource_check(remaining_water, remaining_milk, 
            remaining_coffee):
            """

        else:
            insufficient = resource_check(remaining_water, remaining_milk, remaining_coffee)
            print(f"Sorry there is not enough {insufficient}.")
        # elif remaining_water < 0:
        #     print("Sorry there is not enough water.")
        # elif remaining_milk < 0:
        #     print("Sorry there is not enough milk.")
        # elif resources["coffee"] < 0:
        #     print("Sorry there is not enough coffee.")

    elif user_choice == "report":
        print(resources)
    elif user_choice == "off":
        something = False

