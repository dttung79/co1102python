a = int(input('Enter a: '))
b = int(input('Enter b: '))

op = input('Enter operator [+, -]: ')

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
else:
    result = 'Error: unsupported operator'    
print(f'{a} {op} {b} = {result}')
