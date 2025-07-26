import turtle, random

screen = turtle.Screen()
screen.bgcolor("black")

s = turtle.Turtle()
s.hideturtle()
s.penup()
s.speed(0)
for _ in range(100):
    s.goto(random.randint(-400, 400), random.randint(-300, 300))
    s.dot(random.randint(2, 4), "white")

t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta"]

for i in range(200):
    t.color(colors[i % len(colors)])
    t.forward(10 + i * 1.2)
    t.left(25)
    t.stamp()


