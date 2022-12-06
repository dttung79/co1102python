# Enter number n,
# Print sum of evens from 1 to n

s = 0
i = 1

n = int(input('Enter number n: '))

while i <= n:
    if i % 2 == 0:
        s = s + i
    i = i + 1

print('Sum of evens from 1 to {} = {}'.format(n, s))