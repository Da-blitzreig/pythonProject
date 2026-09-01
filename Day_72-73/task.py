import turtle
import random
import time

# Screen
screen = turtle.Screen()
screen.title("Aim Trainer")
screen.setup(800, 600)
screen.bgcolor("black")

# Target
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.shapesize(2)

# Score display
text = turtle.Turtle()
text.hideturtle()
text.color("white")
text.penup()
text.goto(0, 250)

score = 0
misses = 0
start_time = time.perf_counter()


def update_text():
    text.clear()
    text.write(
        f"score: {score}   misses: {misses}",
        align="center",
        font=("Arial", 18, "bold")
    )


def move_target():
    x = random.randint(-350, 350)
    y = random.randint(-200, 200)

    target.goto(x, y)

    global start_time
    start_time = time.perf_counter()


def hit(x, y):
    global score

    reaction = (time.perf_counter() - start_time) * 1000

    score += 1

    print(f"hit! {reaction:.0f} ms")

    update_text()
    move_target()


def miss(x, y):
    global misses

    misses += 1
    update_text()


# Clicking the target
target.onclick(hit)

# Clicking anywhere else counts as a miss
screen.onclick(miss)

update_text()
move_target()

screen.mainloop()