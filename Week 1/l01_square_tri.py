import turtle as t

# draw a square of side 100
t.forward(100) 
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# move turtle to a new place
t.penup()
t.forward(300)
t.pendown()

# draw a triangle of side 200
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)

# Wait to close by click
t.exitonclick()