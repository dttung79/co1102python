a = int(input('Enter number a: '))
b = int(input('Enter number b: '))

print(f'{a} + {b} = {a + b}')
# TODO: continue with other operations: -, *, /, //, %, **
print(f'{a} - {b} = {a - b}')
# print('a - b =', a - b)
# print('a * b =', a * b)
# print('a / b =', a / b)
# print('a // b =', a // b)
# print('a % b =', a % b)
# print('a ** b =', a ** b)

# Another way to print with formatted string
print('{} + {} = {}'.format(a, b, a + b))

# TODO: Enter number n, print the multiplication table of n
# For example, if n = 5, the output should be:
# 5 * 1 = 5
# 5 * 2 = 10
# ...
n = int(input('Enter number n: '))
print(f'{n} * 1 = {n * 1}')
print(f'{n} * 2 = {n * 2}')