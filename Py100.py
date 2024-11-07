water = 300
milk = 200
coffee = 100
cash_in_machine = 0

PRICES = {
    '1': 4.0,   # Espresso
    '2': 6.5,   # Latte
    '3': 8.0    # Cappuccino
}

def current_status():
    print(f'{water}ml water')
    print(f'{milk}ml milk')
    print(f'{coffee}g coffee')
    print(f'R${cash_in_machine}')

def refill(a_water, a_milk, a_coffee):
    add_water = int(input('How much water do you want to add: '))
    a_water += add_water
    add_milk = int(input('How much milk do you want to add: '))
    a_milk += add_milk
    add_coffee = int(input('How much coffee do you want to add: '))
    a_coffee += add_coffee
    return a_water, a_milk, a_coffee

def resources_check(num, check_water, check_coffee, check_milk):
    if num == '1':  # Espresso
        if check_water < 50 or check_coffee < 18:
            print("Machine Resources Insufficient for Espresso!")
            return check_water, check_coffee, check_milk, False
        else:
            check_water -= 50
            check_coffee -= 18
            return check_water, check_coffee, check_milk, True
    elif num == '2':  # Latte
        if check_water < 200 or check_milk < 150 or check_coffee < 24:
            print("Machine Resources Insufficient for Latte!")
            return check_water, check_coffee, check_milk, False
        else:
            check_water -= 200
            check_milk -= 150
            check_coffee -= 24
            return check_water, check_coffee, check_milk, True
    elif num == '3':  # Cappuccino
        if check_water < 250 or check_milk < 100 or check_coffee < 24:
            print("Machine Resources Insufficient for Cappuccino!")
            return check_water, check_coffee, check_milk, False
        else:
            check_water -= 250
            check_milk -= 100
            check_coffee -= 24
            return check_water, check_coffee, check_milk, True
    else:
        print("Invalid selection.")
        return check_water, check_coffee, check_milk, False

def process_coins():
    print("Please insert coins.")
    twenty_five_cents = int(input("How many 25-cent coins? ")) * 0.25
    fifty_cents = int(input("How many 50-cent coins? ")) * 0.50
    one_real = int(input("How many 1-real coins? ")) * 1.0
    return round(twenty_five_cents + fifty_cents + one_real, 2)

def check_transaction(inserted_money, cost):
    if inserted_money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif inserted_money > cost:
        change = round(inserted_money - cost, 2)
        print(f"Here is R${change} in change.")
    print("Transaction successful.")
    return True

off = False
while not off:
    print("What would you like?")
    select = input("1-Espresso (R$4,00)\n2-Latte (R$6,50)\n3-Cappuccino (R$8,00)\nType 'menu' for options.\n").lower()
    if select in ['1', '2', '3']:
        cost = PRICES[select]
        water, coffee, milk, success = resources_check(select, water, coffee, milk)
        if success:
            inserted_money = process_coins()
            if check_transaction(inserted_money, cost):
                print("Preparing your drink!")
                cash_in_machine += cost
                input("Drink ready, Enjoy!!")

            else:
                print("Unable to complete the transaction.")
        else:
            print("Unable to prepare the drink due to insufficient resources.")
    elif select == 'menu':
        menu_select = input("MENU\n1-Report Status\n2-Refill Machine\n3-Turn Machine OFF\n")
        if menu_select == '1':
            current_status()
        elif menu_select == '2':
            water, milk, coffee = refill(water, milk, coffee)
        elif menu_select == '3':
            off = True
        else:
            print("Invalid option, please try again.")
    else:
        print("Invalid selection, please choose a coffee type or type 'menu'.")
