machine_water = 400
machine_milk = 540
machine_coffee_beans = 120
machine_disp_cups = 9
machine_money = 550
choice = ''
selection = ''
exit_switch = 'no'


def machine_has():
    print('The coffee machine has:')
    print(str(machine_water) + ' of water')
    print(str(machine_milk) + ' of milk')
    print(str(machine_coffee_beans) + ' of coffee beans')
    print(str(machine_disp_cups) + ' of disposable cups')
    print(str(machine_money) + ' of money')


def machine_function():
    global choice
    print('')
    print('Write action (buy, fill, take, remaining, exit)')
    choice = input()
    if choice == 'buy':
        machine_buy()
    elif choice == 'fill':
        machine_fill()
    elif choice == 'take':
        machine_take()
    elif choice == 'remaining':
        machine_has()
    elif choice == 'exit':
        machine_exit()


def machine_selection():

    def make_espresso():
        global selection
        global machine_water
        global machine_milk
        global machine_coffee_beans
        global machine_disp_cups
        global machine_money
        missing = ''
        if machine_water >= 250 and machine_coffee_beans >= 16 and machine_disp_cups >= 1:
            machine_water -= 250
            machine_milk -= 0
            machine_coffee_beans -= 16
            machine_disp_cups -= 1
            machine_money += 4
            print('I have enough resources, making you a coffee!')
        else:
            if machine_water < 250:
                missing += ' water'
            if machine_coffee_beans < 16:
                missing += ' milk'
            if machine_disp_cups < 1:
                missing += ' cups'
            print('Sorry, not enough' + missing + '!')

    def make_latte():
        global selection
        global machine_water
        global machine_milk
        global machine_coffee_beans
        global machine_disp_cups
        global machine_money
        missing = ''
        if machine_water >= 350 and machine_milk >= 75 and machine_coffee_beans >= 20 and machine_disp_cups >= 1:
            machine_water -= 350
            machine_milk -= 75
            machine_coffee_beans -= 20
            machine_disp_cups -= 1
            machine_money += 7
            print('I have enough resources, making you a coffee!')
        else:
            if machine_water < 350:
                missing += ' water'
            if machine_milk < 75:
                missing += ' milk'
            if machine_coffee_beans < 20:
                missing += ' milk'
            if machine_disp_cups < 1:
                missing += ' cups'
            print('Sorry, not enough' + missing + '!')

    def make_cappuccino():
        global selection
        global machine_water
        global machine_milk
        global machine_coffee_beans
        global machine_disp_cups
        global machine_money
        missing = ''
        if machine_water >= 200 and machine_milk >= 100 and machine_coffee_beans >= 12 and machine_disp_cups >=1:
            machine_water -= 200
            machine_milk -= 100
            machine_coffee_beans -= 12
            machine_disp_cups -= 1
            machine_money += 6
            print('I have enough resources, making you a coffee!')
        else:
            if machine_water < 200:
                missing += ' water'
            if machine_milk < 100:
                missing += ' milk'
            if machine_coffee_beans < 12:
                missing += ' milk'
            if machine_disp_cups < 1:
                missing += ' cups'
            print('Sorry, not enough' + missing + '!')

    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    selection = input()

    if selection == '1':
        make_espresso()
    if selection == '2':
        make_latte()
    if selection == '3':
        make_cappuccino()
    if selection == 'back':
        pass


def machine_buy():
    machine_selection()


def machine_fill():
    print('Write how many ml of water do you want to add:')
    add_water = int(input())
    print('Write how many ml of milk do you want to add:')
    add_milk = int(input())
    print('Write how many grams of coffee beans do you want to add:')
    add_coffee_beans = int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    add_disp_cups = int(input())
    global machine_water
    global machine_milk
    global machine_coffee_beans
    global machine_disp_cups
    machine_water += add_water
    machine_milk += add_milk
    machine_coffee_beans += add_coffee_beans
    machine_disp_cups += add_disp_cups


def machine_take():
    global machine_money
    print('I gave you $' + str(machine_money))
    machine_money = 0


def machine_exit():
    global exit_switch
    exit_switch = 'yes'


while exit_switch != 'yes':
    machine_function()

