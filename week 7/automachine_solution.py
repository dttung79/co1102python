PEPSI_PRICE = 1.5
WATER_PRICE = 0.3
ORANGE_PRICE = 2.0

PEPSI_CHOICE = 1
WATER_CHOICE = 2
ORANGE_CHOICE = 3

EXIT_CODE = -1

def print_menu():
    # TODO print menu
    print('1. Pepsi - 1.5')
    print('2. Water - 0.3')
    print('3. Orange - 2.0')


def cal_payment(drink_choice, n_drinks):
    # TODO calculate payment
    if drink_choice == PEPSI_CHOICE: # lựa chọn pepsi
        payment = PEPSI_PRICE * n_drinks
    elif drink_choice == WATER_CHOICE: # lựa chọn water
        payment = WATER_PRICE * n_drinks
    elif drink_choice == ORANGE_CHOICE: # lựa chọn orange
        payment = ORANGE_PRICE * n_drinks
    else:
        payment = 0
    return payment


def cal_change(payment, amount):
    # TODO calculate change
    change = amount - payment
    return change

def get_drink_choice():
    valid_choice = False
    while not valid_choice:
        drink_choice = int(input('Enter your choice: '))
        valid_choice = drink_choice in (PEPSI_CHOICE, WATER_CHOICE, ORANGE_CHOICE, EXIT_CODE)
        if not valid_choice:
            print('Invalid choice. Please try again.')

    return drink_choice
def get_n_drinks():
    valid_n_drinks = False
    while not valid_n_drinks:
        n_drinks = int(input('Enter number of drinks: '))
        valid_n_drinks = n_drinks in range(1, 6)
        if not valid_n_drinks:
            print('Invalid number of drinks. Please try again.')
    return n_drinks

def get_amount(payment):
    valid_amount = False
    while not valid_amount:
        amount = float(input('Enter amount: '))
        valid_amount = amount >= payment
        if not valid_amount:
            print('Invalid amount. Please try again.')
    return amount

### MAIN ###
while True:
    print_menu()
    drink_choice = get_drink_choice()
    if drink_choice == EXIT_CODE:
        break
    n_drinks = get_n_drinks()

    payment = cal_payment(drink_choice, n_drinks)
    print('Payment: $', payment)

    amount = get_amount(payment)
    change = cal_change(payment, amount)
    print('Change: $', change)
