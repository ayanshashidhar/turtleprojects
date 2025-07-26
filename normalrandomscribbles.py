import turtle, random
t = turtle.Turtle()

t.speed(0)
t.color("black")
t.pensize(3)
for i in range(1000):
    if random.random() < 0.7:
        t.forward(5)
    else:
        t.right(90)



