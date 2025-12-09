import turtle

screen = turtle.Screen()
screen.addshape("Spire.gif")

bg = turtle.Turtle()
bg.shape("Spire.gif")
bg.left(90)

figure = turtle.Turtle()

figure.shape("arrow")
figure.color("red")

entrance = turtle.Turtle()
entrance.hideturtle()
entrance.penup()
entrance.goto(60,-300)
entrance.pendown()
entrance.color("white")
entrance.write("entrance")
middle = turtle.Turtle()
middle.hideturtle()
middle.penup()
middle.goto(60,20)
middle.pendown()
middle.color("white")
middle.write("middle")
top = turtle.Turtle()
top.hideturtle()
top.penup()
top.goto(60,100)
top.pendown()
top.color("white")
top.write("top")

def location(loc):
    if loc == "entrance":
        figure.penup()
        figure.goto(75,-280)
    if loc == "middle":
        figure.penup()
        figure.goto(60,0)
    if loc == "end":
        figure.penup()
        figure.goto(60,80)
    turtle.done()
