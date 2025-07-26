import turtle, random
t = turtle.Turtle()

t.speed(0)


t.pensize(100)
for i in range(100):
    t.pencolor(random.randint(0,240), random.randint(0,240), random.randint(0,240))
    t.forward(random.randint(20, 100))
    t.right(random.choice([0, 90, 180, 270]))



# try changing up some numbers
