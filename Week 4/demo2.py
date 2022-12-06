even_counter = 0
n = 1
while n > 0:
    n = int(input('Enter a number: '))
    if n % 2 == 0:
        even_counter = even_counter + 1

print('Number of even numbers entered:', even_counter)