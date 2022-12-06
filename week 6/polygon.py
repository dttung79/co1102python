import turtle as t
# Write a function that draw a regular polygon of n sides
def draw_polygon(n_sides, length=100, color='red', pen_size=1):
    if  n_sides <= 2 or n_sides >= 10:
        print('Invalid number of sides')
        exit()

    t.pensize(pen_size)
    t.color(color)

    for i in range(n_sides):
        t.forward(length)
        t.left(360 / n_sides)

# Write a function that draw n regular polygons of m sides
def draw_polygons(n_polygons, n_sides, length=100, color='red', pen_size=1):
    for i in range(n_polygons):
        draw_polygon(n_sides, length, color, pen_size)
        t.left(360 / n_polygons)

t.speed(100)
draw_polygons(30, 3, length=150, color='blue', pen_size=2)
t.exitonclick()