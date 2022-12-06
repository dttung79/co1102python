# Setup some constants
R_BILL_FEE = 4.5
R_SERVICE_FEE = 20.5
R_PREMIMUM_CHANNEL_FEE = 7.5

B_BILL_FEE = 15
B_SERVICE_FEE = 75
B_PREMIMUM_CHANNEL_FEE = 50
B_ADDITIONAL_CONNECTION_FEE = 5

acc_no = input('Enter account number: ')
customer_type = input('Enter customer type (r/b): ').lower()
n_channels = int(input('Enter number of premium channels: '))

if customer_type not in ('r', 'b'):
    print('Invalid customer type')
    exit()

if n_channels <= 0:
    print('Invalid number of channels')
    exit()

if customer_type == 'b':
    n_connections = int(input('Enter number of connections: '))
    if n_connections < 0:
        print('Invalid number of connections')
        exit()

if customer_type == 'r':
    total_bill = R_BILL_FEE + R_SERVICE_FEE + n_channels * R_PREMIMUM_CHANNEL_FEE
else:
    total_bill = B_BILL_FEE + B_SERVICE_FEE + n_channels * B_PREMIMUM_CHANNEL_FEE
    addictional_fee = 0 if n_connections < 10 else (n_connections - 10) * B_ADDITIONAL_CONNECTION_FEE
    total_bill += addictional_fee

print('+', '-' * 20, '+', '-' * 10, '+', sep='')
print('{:21s}|{:>10s}|'.format('Account number', acc_no))
print('{:21s}|{:>10s}|'.format('Customer type', customer_type))
print('{:21s}|{:>10d}|'.format('No of channels', n_channels))
if customer_type == 'b':
    print('{:21s}|{:>10d}|'.format('No of connections', n_connections))
print('{:21s}|{:>10.2f}|'.format('Bill amount', total_bill))
print('+', '-' * 20, '+', '-' * 10, '+', sep='')