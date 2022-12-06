LUCKY_NUMBER1 = 4
LUCKY_NUMBER2 = 7
REWARD = 5

playing = True
total_points = 0

while playing:
    number = int(input('Enter a number: '))
    if number % (LUCKY_NUMBER1 * LUCKY_NUMBER2) == 0:
        print('You won', REWARD, 'points!')
        total_points += REWARD
    else:
        print('Your number is not a lucky number.')
        
    playing = input('Do you want to play again? (y/n): ').lower() == 'y'
    

print('Your total points are', total_points)