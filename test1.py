import turtle
from polygon_shape import Polygon


screen = turtle.Screen()
screen.title("A Kindergarten's Flower")
screen.bgcolor("lightsteelblue1")
# screen.tracer(0)

# Draw a border of the picture
b = turtle.Turtle()
b.pencolor("black")
b.pensize(2)
# b.circle(1)
b.penup()
b.goto(-400, 300)
b.pendown()
b.goto(400, 300)
b.goto(400, -300)
b.goto(-400, -300)
b.goto(-400, 300)

# Draw a flower
circle = turtle.Turtle()

circle.color("gold1")
circle.pensize(10)
circle.penup()
circle.goto(20, -15)
circle.pendown()
circle.circle(10)

circle.color("plum2")
circle.penup()
circle.goto(100, -200)
circle.pendown()
for _ in range(5):
    circle.left(45)
    circle.circle(100, 100)
    circle.right(173)
    circle.circle(100, 100)

circle.color("darkolivegreen3")
circle.penup()
circle.goto(0, -100)
circle.pendown()
circle.right(90)
circle.circle(500, 50)

screen.mainloop()

