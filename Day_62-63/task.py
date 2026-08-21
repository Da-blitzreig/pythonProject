import turtle

p = turtle.Turtle()
p.shape("square")
p.color("green")

def up():
    p.sety(p.ycor() + 20)

def down():
    p.sety(p.ycor() - 20)

def left():
    p.setx(p.xcor() - 20)

def right():
    p.setx(p.xcor() + 20)

screen = turtle.Screen()

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.listen()
screen.mainloop()