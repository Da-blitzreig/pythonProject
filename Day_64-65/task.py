import turtle

# Screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Left paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Right paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 3
ball.dy = 3

# Score
score_a = 0
score_b = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write("Player 1: 0    Player 2: 0",
            align="center",
            font=("Arial", 20, "normal"))

# Paddle controls
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 30)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        paddle_a.sety(y - 30)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 30)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        paddle_b.sety(y - 30)


screen.listen()

screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")

screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")


while True:
    screen.update()


    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1

        score.clear()
        score.write(
            f"Player 1: {score_a}    Player 2: {score_b}",
            align="center",
            font=("Arial", 20, "normal")
        )


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1

        score.clear()
        score.write(
            f"Player 1: {score_a}    Player 2: {score_b}",
            align="center",
            font=("Arial", 20, "normal")
        )


    if (ball.xcor() > 330 and ball.xcor() < 350 and
            ball.ycor() < paddle_b.ycor() + 50 and
            ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor() > -350 and
            ball.ycor() < paddle_a.ycor() + 50 and
            ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1