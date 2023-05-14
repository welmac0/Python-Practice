coffee = input('What kind of coffee do you prefer? ').lower()

match coffee:
    case "cappuccino" | "cappuccino+":
        print("House coffee")
    case "espresso":
        print('Cheap one')
    case 'latte':
        print('Drunk with gf')
    case _:
        print('Don\'t know this one!')
