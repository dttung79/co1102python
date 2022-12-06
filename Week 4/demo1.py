counter = 1

while counter < 11:
    print(counter, 'Hello world')
    counter += 1

# n_channels = 0

# while n_channels <= 0:
#     n_channels = int(input('Enter number of premium channels: '))
#     if n_channels <= 0:
#         print('Invalid number of channels. Try again.')

# print('Number of channels is', n_channels)

valid_n_channels = False

while not valid_n_channels:
    n_channels = int(input('Enter number of premium channels: '))
    valid_n_channels = n_channels > 0
    if not valid_n_channels:
        print('Invalid number of channels. Try again.')

print('Number of channels is', n_channels)