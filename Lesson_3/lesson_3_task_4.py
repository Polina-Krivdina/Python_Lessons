from turtle import Turtle, Screen

def draw_circle(turtle, x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(turtle, x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_elephant(turtle):
    # Туловище
    draw_circle(turtle, 0, -100, 100, "grey")
    # Голова
    draw_circle(turtle, 0, 0, 60, "grey")
    # Левое ухо
    draw_circle(turtle, -60, 30, 30, "grey")
    # Правое ухо
    draw_circle(turtle, 60, 30, 30, "grey")
    # Левый глаз
    draw_circle(turtle, -30, 20, 5, "black")
    # Правый глаз
    draw_circle(turtle, 30, 20, 5, "black")
    # Нос
    draw_rectangle(turtle, -20, -20, 40, 30, "grey")
    # Хобот
    turtle.penup()
    turtle.goto(0, -60)
    turtle.setheading(60)
    turtle.pendown()
    turtle.forward(60)
    turtle.circle(30, 180)
    turtle.forward(60)

screen = Screen()
screen.setup(800, 600)

my_turtle = Turtle()
my_turtle.speed(0)
draw_elephant(my_turtle)

screen.exitonclick() 