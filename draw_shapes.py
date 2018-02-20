import turtle    #module for drawing and movin stuff on screen

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(1)
    brad.color("white")
    
    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)

    
    rj = turtle.Turtle()
    rj.shape("arrow")
    rj.color("yellow")
    rj.circle(100)
    
    window.exitonclick()

draw_square()

