import turtle

screen = turtle.Screen()
screen.screensize(500,500)
t = turtle.Turtle()
screen.bgcolor('tan')
t.speed(0)

t.fillcolor('green')
t.begin_fill()
t.penup()
t.goto(-200,0)

t.pendown()
t.forward(100)

t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.end_fill()

t.penup()
t.goto(0,0)
t.pendown()
t.pensize(5)
t.fillcolor('red')
t.setheading(0)
t.begin_fill()
t.circle(50)
t.end_fill()


t.penup()
t.goto(150,0)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
t.goto(250,0)
t.goto(200,100)
t.goto(150,0)
t.end_fill()


t.penup()
t.goto(0,200)
t.pendown()
t.write("I love turtle", font=("Arial",30,"normal"),align="center")

turtle.done()