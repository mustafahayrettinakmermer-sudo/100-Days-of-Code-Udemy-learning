from random import choice

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}





#OFF
def off():
    if user_option == "off":
        print("Machine shutting down. Have a nice day!")


#report
def report():
    if user_option == "report":
        print("----- HERE IS THE FULL REPORT -----")
        for item in resources:
            print(f"{item}: {resources[item]}")


def make_coffee(choice):
    ingredients = MENU[choice]["ingredients"]

    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry we are out of {item}")
            return False

    for item in ingredients:
        resources[item] -= ingredients[item]
    return True

    print("Here is your Coffee. Enjoy...")

def process_coins(user_option):
    print("Please enter the coins you put!!!!")
    quarter_payment = int(input("How many quarters?: "))
    dimes_payment = int(input("How many dimes?: "))
    nickle_payment = int(input("How many nickles?: "))
    pennies_payment = int(input("How many pennies?: "))

    quarter = 0.25
    dimes = 0.10
    nickle = 0.05
    pennies = 0.01

    total_given = quarter_payment * 0.25 + dimes_payment * 0.1 + nickle_payment * 0.05 + pennies_payment * 0.01
    change = round(total_given - MENU[user_option]["cost"],2)
    if change >= 0:
        print(f"Payment accepted ☕")

        if change > 0:
            print(f"Your change is ${change}")

        return True
    else:
        print("Sorry, not enough money. Money refunded.")
        return False






#Main Menu
while True:
    print("\\------ Welcome to Coffee Machian Simulator ------//")
    print("                  \\---- Menu ----//")
    print("Espresso")
    print("Latte")
    print("Cappuccino")
    user_option = input("What would you like?: ").lower()
    if user_option == "off":
        off()
        break
    elif user_option == "report":
        report()
    elif user_option in MENU:
        if make_coffee(user_option):  # only if ingredients exist
            print(f"The coffee is ${MENU[user_option]['cost']}")
            if process_coins(user_option):
                print(f"Here is your {user_option} ☕ Enjoy!")

    else:
        print("Invalid option. Please try again.")





























