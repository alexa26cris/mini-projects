import turtle

def draw_square(sq_turtle):
    for i in range(1,5):
        sq_turtle.forward(100)
        sq_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")

    #create a turtle s_sqaure - draws a square
    s_square = turtle.Turtle()
    s_square.shape("turtle")
    s_square.color("white")
    s_square.speed(2)
    for i in range(1, 37):
        draw_square(s_square)
        s_square.right(10)

    window.exitonclick()

draw_art()
