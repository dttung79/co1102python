# Sum from 1 to n using for loop

s = 0
n = int(input('Enter number n: '))

for i in range(1, n+1): # Cho i chạy từ 1 đến n
    if i % 2 == 0:
        s = s + i

print('Sum from 1 to {} = {}'.format(n, s))

