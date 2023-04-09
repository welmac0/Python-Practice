from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#print(coffee_maker.is_resource_sufficient(menu.find_drink('cappuccino')))

coffe_machine_working = True
while coffe_machine_working:
    decision = input(f"What would you like ({menu.get_items()}):")
    if decision == 'report':
        print(f"{coffee_maker.report()}\n{money_machine.report()}")
    elif decision == 'off':
        print()
        coffe_machine_working = False
    else:
        if money_machine.make_payment(menu.find_drink(decision).cost):
            if coffee_maker.is_resource_sufficient(menu.find_drink(decision)):
                coffee_maker.make_coffee(menu.find_drink(decision))
