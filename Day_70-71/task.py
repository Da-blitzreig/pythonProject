import turtle
import time
import random

screen = turtle.Screen()
screen.title("Reaction Test")
screen.bgcolor("red")
screen.setup(600, 500)

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.color("white")

start_time = 0
waiting = True
ready = False


def show_text(message, size=24):
    text.clear()
    text.goto(0, 0)
    text.write(message, align="center", font=("Arial", size, "bold"))


def go_green():
    global start_time, waiting, ready

    screen.bgcolor("green")
    show_text("click")
    start_time = time.perf_counter()
    waiting = False
    ready = True


def clicked(x, y):
    global waiting, ready

    if waiting:
        screen.bgcolor("orange.")
        show_text("too early")
        waiting = False
        ready = False

    elif ready:
        reaction = (time.perf_counter() - start_time) * 1000

        screen.bgcolor("blue")
        show_text(f"{reaction:.0f} ms")

        ready = False

    else:
        start_test()


def start_test():
    global waiting, ready

    screen.bgcolor("red")
    show_text("wait")
    waiting = True
    ready = False

    delay = random.randint(2000, 5000)
    screen.ontimer(go_green, delay)


screen.onclick(clicked)

start_test()

screen.mainloop()