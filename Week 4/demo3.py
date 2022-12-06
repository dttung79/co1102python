sum_positives = 0
sum_negatives = 0

n = 1
while n != 0:
    n = int(input('Enter a number: '))
    if n > 0:
        sum_positives += n
    else:
        sum_negatives += n

print('Sum of positives:', sum_positives)
print('Sum of negatives:', sum_negatives)