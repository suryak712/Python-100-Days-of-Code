from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_list = Menu()
cm = CoffeeMaker()
machine = MoneyMachine()
choice = input(f"What would you like? ({menu_list.get_items()}): ")

is_on = True

while is_on:
    if choice == "off":
        print("Goodbye!")
        is_on = False
    elif choice == "report":
        cm.report()
        machine.report()
    else:
        drink = menu_list.find_drink(choice)
        if cm.is_resource_sufficient(drink) and machine.make_payment(drink.cost):
            cm.make_coffee(drink)
            choice = input(f"What would you like? ({menu_list.get_items()}): ")
        else:
            is_on = False