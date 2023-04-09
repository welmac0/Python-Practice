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

machineOn = True
money = 0

def printReport():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${round(money,2)}")

def makeCoffee(typeOfCoffee):
    print('Please insert coins.')
    global money
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))
    totalAmount: float = pennies * 0.01 + nickles * 0.05 + dimes * 0.10 + quarters * 0.25
    selectedCoffeePrice = MENU[typeOfCoffee]['cost']
    coffeeWater = MENU[typeOfCoffee]['ingredients']['water']
    if typeOfCoffee != 'espresso':
        coffeeMilk = MENU[typeOfCoffee]['ingredients']['milk']
    coffeeCoffee = MENU[typeOfCoffee]['ingredients']['coffee']
    if resources['water'] < coffeeWater or resources['coffee'] < coffeeCoffee:
        print('Not enough resources. Please fill.')
    if typeOfCoffee != 'espresso' and resources['milk'] < coffeeMilk:
        print('Not enough rescources. Please fill.')
    else:
        if totalAmount >= selectedCoffeePrice:
            money += totalAmount
            resources['water'] -= coffeeWater
            if typeOfCoffee != 'espresso':
                resources['milk'] -= coffeeMilk
            resources['coffee'] -= coffeeCoffee
            print(f"Here is ${round(totalAmount - selectedCoffeePrice,2)} in change.")
            print(f"Here's your {typeOfCoffee}. Enjoy!")
        else:
            print("Sorry, that's not enough money. Money refunded.")

while machineOn:
    decision = input("What would you like? (espresso/latte/cappuccino): ")
    match decision:
        case 'espresso':
            makeCoffee('espresso')
        case 'latte':
            makeCoffee('latte')
        case 'cappuccino':
            makeCoffee('cappuccino')
        case 'off':
            print()
            machineOn = False
        case 'report':
            printReport()


