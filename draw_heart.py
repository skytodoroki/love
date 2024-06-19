import turtle

def draw_heart():
    t = turtle.Turtle()
    t.color('red')
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.setheading(60)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()
    t.hideturtle()

draw_heart()
turtle.done()
