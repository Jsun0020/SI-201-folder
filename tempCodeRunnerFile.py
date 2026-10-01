# Your name:John Sun
# Your student id:5205 3872
# Your email:Johnsun@umich.edu
# List who or what you worked with on this homework:
# If you used generative AI also include how you used it.
#I used generative AI to help me with the exact locations to put the shapes so they layer up correctly. I also used it to explain to me how to do the begin and endfill.
#I used generative AI to also help me call the the correct functions and explore more color options, as well as help me with the directions for the S initial.
# import the turtle functions for use in this program
from turtle import *

### write all new functions here ###

def draw_scene(turtle):
    draw_tree(turtle,'lightgreen',-50,-50)
    draw_tree(turtle,'green',-50,125)
    draw_tree(turtle,'darkgreen',-50,35)
    draw_trunk(turtle,'black',25,-150)
    draw_charms(turtle,'darkred',-55,25)
    draw_charms(turtle,'darkred',155,25)
    draw_charms(turtle,'white',-55,120)
    draw_charms(turtle,'white',155,120)
    draw_j(turtle,'white',-100,-150)
    draw_s(turtle, 'white',150, -150)

def draw_charms(turtle, color, x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
def draw_trunk(turtle, color, x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range (2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()
def draw_tree(turtle, color, x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(200)
        turtle.left(120)
    turtle.end_fill()
def draw_j(turtle, color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.pensize(10)
    turtle.forward(60)
    turtle.backward(30)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(20)
def draw_s(turtle, color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.pensize(10)
    turtle.right(90)
    turtle.forward(60)
    turtle.backward(60)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(60)
 


    pass

def main():
    """
    Make sure to create a Screen object, a Turtle object,
    and call draw_scene.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color.
    """
    space = Screen()
    space.bgcolor("blue")
    turtle = Turtle()
    draw_scene(turtle)
    space.exitonclick()
    pass


# Only run the main function if this file is executed (not imported)
if __name__ == '__main__':
    main()
