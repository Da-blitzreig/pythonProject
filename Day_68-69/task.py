import turtle
screen = turtle.Screen()
screen.title("turtle clicker")
screen.bgcolor("lightblue")
score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 200)
pen.write("Score: 0", align="center", font=("Arial", 24, "bold"))
clicker = turtle.Turtle()
clicker.shape("turtle")
clicker.color("green")
clicker.shapesize(3)
clicker.penup()
def clicked(x, y):
    global score
    score += 1
    pen.clear()
    pen.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))
clicker.onclick(clicked)
screen.mainloop()