PEPSI_PRICE = 1.5
WATER_PRICE = 0.3
ORANGE_PRICE = 2.0

PEPSI_CHOICE = 1
WATER_CHOICE = 2
ORANGE_CHOICE = 3


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


### MAIN ###
print_menu()
drink_choice = int(input('Enter your choice: '))
n_drinks = int(input('Enter number of drinks: '))

payment = cal_payment(drink_choice, n_drinks)
print('Payment: $', payment)

amount = float(input('Insert money: $'))
change = cal_change(payment, amount)
print('Change: $', change)
