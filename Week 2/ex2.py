msg = 'Hello Python'
print('|{:<20s}|'.format(msg))
print('|{:>20s}|'.format(msg))
print('|{:^20s}|'.format(msg))

s1 = 'Hello'
s2 = 'Python'
print('|{:<10s}{:>10s}|'.format(s1, s2))

a = 10
print('|{:10s}|'.format(s1)) # string is left-aligned by default
print('|{:10d}|'.format(a))  # integer (number) is right-aligned by default

# TODO: Enter grades for 3 courses (programming, software engineering, networking)
# Print these grades and their average

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
