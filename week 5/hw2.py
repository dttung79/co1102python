import turtle as t

n_sides = int(input('Enter number of sides (3-9): '))
pen_size = int(input('Enter pen size (1-10): '))
color = input('Enter color (red, green, blue, yellow, orange, purple, black, white): ')
if  n_sides <= 2 or n_sides >= 10:
    print('Invalid number of sides')
    exit()

t.pensize(pen_size)
t.color(color)

for i in range(n_sides):
    t.forward(100)
    t.left(360 / n_sides)

t.exitonclick()