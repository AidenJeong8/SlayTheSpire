import turtle
from items import items_real
import time

def location(loc):
    turtle.TurtleScreen._RUNNING = True

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
    entrance.color("green")
    entrance.write("entrance", font = ("",20,""))
    middle = turtle.Turtle()
    middle.hideturtle()
    middle.penup()
    middle.goto(60,20)
    middle.pendown()
    middle.color("blue")
    middle.write("middle", font = ("",20,""))
    top = turtle.Turtle()
    top.hideturtle()
    top.penup()
    top.goto(60,100)
    top.pendown()
    top.color("white")
    top.write("top", font = ("",20,""))

    if loc == "entrance":
        figure.penup()
        figure.goto(75,-280)
    if loc == "middle":
        figure.penup()
        figure.goto(60,0)
    if loc == "end":
        figure.penup()
        figure.goto(60,80)

    time.sleep(1)

    new_item = items_real.random_item()
    print("New item:",str(type(new_item).__name__))
    

    t = turtle.Turtle()
    screen.addshape("items/"+str(type(new_item).__name__)+".gif")
    t.shape("items/"+str(type(new_item).__name__)+".gif")
    
    boost = new_item.use()
    print(boost)
    screen.bye()
    
    return boost

location("entrance")
