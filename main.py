import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def check_resources(name):
    if (MENU[name]['ingredients']['water'] < resources["water"]):
        if MENU[name]['ingredients']['milk'] < resources["milk"]:
            if MENU[name]['ingredients']['coffee'] < resources["coffee"]:
                return True
            else:
                print("Sorry there is not enough coffee")
                return False
        else:
            print("Sorry there is not enough milk")
            return False
    else:
        print("Sorry there is not enough water")
        return False

def check_money(name):
    print("Enter the Coins")
    quaters = int(input("How many Quaters?"))
    dimes = int(input("how many Dimes?"))
    nickels = int(input("how many nickels?"))
    pennies = int(input("how many pennies?"))
    entered_money = quaters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01

    if entered_money > MENU[name]['cost']:
        print(f"Here is ${entered_money - MENU[name]['cost']} dollars in change.")
        resources['money'] += MENU[name]['cost']
        return True
    elif entered_money == MENU[name]['cost']:
        resources['money'] += MENU[name]['cost']
        return True
    else:
        print("Sorry that's not the enough Money. Money refunded. ")
        return False


def make_coffee(name):
    for x in resources:
        if x == 'money':
            continue
        resources[x] -= MENU[name]['ingredients'][x]
    print(f"Here is your {name}. Enjoy!")




machine_status = True
while machine_status:

    print(logo.logo)
    user_demand = input("what would you like? (espresso/latte/cappuccino):")
    if user_demand == "report":
        print(
            f" Water: {resources['water']}ml\n Milk: {resources['milk']}ml\n Coffee: {resources['coffee']}g\n Money: ${resources['money']}\n")
    elif user_demand == "off":
        machine_status = False
        continue
    elif user_demand == "espresso" or user_demand == "latte" or user_demand == "cappuccino":
        if check_resources(user_demand):
            if check_money(user_demand):
                make_coffee(user_demand)
    else:
        print("please enter valid input")
