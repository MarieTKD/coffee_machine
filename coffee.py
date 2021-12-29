# Dictionaries provided by the instructor

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 300,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Importing the coffee cup ascii
from art import logo
print(logo)


def check_ingredient(order_ingredients):
    """ Checks if there is enough water, milk or coffee in the machine to prepare the drink ordered
    :param order_ingredients:
    :return: boolean
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item} for a {order}.")
            return False
        else:
            return True


def add_coins():
    """
    Asks for payment using coins and computes the total payment
    :return: total
    """
    print(f"Your coffee cost: {MENU[order]['cost']}")
    quarters = int(input("How many quarters do you insert? "))
    dimes = int(input("How many dimes do you insert? "))
    nickles = int(input("How many nickles do you insert? "))
    pennies = int(input("How many pennies do you insert? "))
    total = round(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01, 2)
    return total


def making_coffee(drink_order, drink_ingredients):
    """
    Prints the order and updates the ingredient resources in the machine
    :param drink_order:
    :param drink_ingredients:
    """
    print(f"Here is your {drink_order} ☕! Enjoy!")
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]


machine_working = True

while machine_working:
    # Input order, could be espresso, latte, cappuccino, or for maintenance: report or off
    order = input("Hello! What would you like to drink? Espresso, Latte or Cappuccino: ").lower()
    if order == "off":
        print("Goodbye!")
        machine_working = False
    elif order == "report":
        print(resources)
    else:
        if check_ingredient(MENU[order]["ingredients"]):
            payment = add_coins()
            # Compares amount paid to the cost of drink, gives money back and/or drink
            if payment < MENU[order]["cost"]:
                print(f"Sorry, this is not enough money. Here is your refund: ${payment}")
            elif payment > MENU[order]["cost"]:
                change = round(payment - MENU[order]["cost"], 2)
                print(f"Here is your change: ${change}")
                making_coffee(order,MENU[order]["ingredients"])
            else:
                making_coffee(order,MENU[order]["ingredients"])
