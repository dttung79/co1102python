import turtle as t

n = int(input('Enter number n: '))

# draw a square n times around the screen
for i in range(n):
    t.forward(100)
    t.left(360/n)

t.exitonclick()