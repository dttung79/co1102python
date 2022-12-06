# draw a bowtie

import turtle as t


t.pensize(7)
t.penup()
t.goto(-200, -100)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.goto(-200, 100)
t.goto(200, -100)
t.goto(200, 100)
t.goto(-200, -100)
t.end_fill()

t.exitonclick()
