course1 = 'Programming'
course2 = 'Software Engineering'
course3 = 'Networking'

grade1 = int(input(f'Enter grade for {course1}: '))
grade2 = int(input(f'Enter grade for {course2}: '))
grade3 = int(input(f'Enter grade for {course3}: '))
avg = (grade1 + grade2 + grade3) / 3

print('{:<20s}:{:>8d}'.format(course1, grade1))
print('{:<20s}:{:>8d}'.format(course2, grade2))
print('{:<20s}:{:>8d}'.format(course3, grade3))
print('{:<20s}:{:>8.2f}'.format('Average', avg))

# Decide the rank of the student based on avg
# 80-100: Distinction, 60-79: Merit, 40-59: Pass, 0-39: Fail
if avg >= 80:
    rank = 'Distinction'
elif avg >= 60:
    rank = 'Merit'
elif avg >= 40:
    rank = 'Pass'
else:
    rank = 'Fail'
print('{:<20s}:{:>8s}'.format('Rank', rank))