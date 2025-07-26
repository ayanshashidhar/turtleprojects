import turtle, random
t = turtle.Turtle()

t.speed(0)

for size in range(20, 2000, 2):
    t.pencolor(random.choice(["blue","green","purple","orange"]))
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.right(15)





