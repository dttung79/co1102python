side_a = int(input('Enter triangle side a: '))
side_b = int(input('Enter triangle side b: '))
side_c = int(input('Enter triangle side c: '))

sides_positives = side_a > 0 and side_b > 0 and side_c > 0
sum_2sides_gt_other = side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a

if not (sides_positives or sum_2sides_gt_other):
    print('Invalid triangle')
    exit()

p = (side_a + side_b + side_c) / 2
s = (p * (p - side_a) * (p - side_b) * (p - side_c)) ** 0.5

print('Triangle area: ', s)
    
