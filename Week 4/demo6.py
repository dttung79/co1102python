# Enter number n
# Print multiplication table of n

n = int(input('Enter number n: '))

for i in range(1, 11):
    #print(i, "x", n, "=", i*n)
    #print(f'{i} x {n} = {i*n}')
    print('{} x {} = {}'.format(i, n, i*n))
