import turtle
import random

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)

snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

direction = "stop"

def up():
    global direction
    direction = "up"

def down():
    global direction
    direction = "down"

def left():
    global direction
    direction = "left"

def right():
    global direction
    direction = "right"

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

while True:
    if direction == "up":
        snake.sety(snake.ycor() + 20)
    elif direction == "down":
        snake.sety(snake.ycor() - 20)
    elif direction == "left":
        snake.setx(snake.xcor() - 20)
    elif direction == "right":
        snake.setx(snake.xcor() + 20)

    if snake.distance(food) < 20:
        food.goto(
            random.randint(-280, 280),
            random.randint(-280, 280)
        )

    screen.update()
    screen.ontimer(lambda: None, 100)