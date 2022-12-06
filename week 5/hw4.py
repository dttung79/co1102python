import random as rd

play_again = 'y'

while play_again == 'y':
    pc_number = rd.randint(1, 10)
    user_number = int(input('Guess a number between 1 and 10: '))
    
    if pc_number == user_number:
        print('You guessed correctly!')
    else:
        print('Wrong! The number was', pc_number)
    
    play_again = input('Do you want to play again? (y/n): ').lower()