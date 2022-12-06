# A customer pays total bill.
# If total bill is less than $100, customer pays 10% tip and say thank you
# If total bill is >= $100, customer pays 15% tip and say thank you

total_bill = float(input('Enter total bill: '))
# check if total_bill is valid
if total_bill <= 0:
    print('Error: invalid total bill')
    exit()
    
if total_bill < 100:
    tip = total_bill * 0.1
else:
    tip = total_bill * 0.15

print('Your tip is {}, thank you!'.format(tip))


# A customer pays total bill.
# Then he pays tip.
# If the bill is less than $100, customer pays less than 10% tip,
# the waiter didn't say thank you but if the tip is more than 10%  the waiter 
# says thank you.
# Same for bill >= $100, the tip should be 15%.

total_bill = float(input('Enter total bill: '))
customer_tip = float(input('Enter tip: '))

if total_bill < 100:
    should_tip = total_bill * 0.1
else:
    should_tip = total_bill * 0.15

if customer_tip == should_tip:
    print('Thank you!')
elif customer_tip > should_tip:
    print('Thank you, you are so generous')