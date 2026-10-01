from turtle import *

### write all new functions here ###



def draw_emoji(t):
    t.circle(50)
    t.penup()
    t.goto(-25, 50)
    t.pendown()
    t.dot(25)
    t.penup()
    t.goto(25, 50)
    t.pendown()
    t.dot(25)
    t.penup()
    t.goto(-25, 30)
    t.setheading(-60)
    t.pendown()
    t.circle(30, 120)

    pass

def main():
    space = Screen()
    space.bgcolor("yellow")
    t = Turtle()
    draw_emoji(t)
    space.exitonclick()

    pass


if __name__ == '__main__':
    main()


