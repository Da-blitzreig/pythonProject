import turtle


screen = turtle.Screen()
screen.title("Maze")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)


walls = [
    (-350, 250, 700, 20),
    (-350, -250, 700, 20),
    (-350, -250, 20, 500),
    (330, -250, 20, 500),

    (-250, 150, 20, 200),
    (-250, 150, 300, 20),

    (-150, 50, 20, 200),
    (-150, 50, 200, 20),

    (50, -100, 20, 170),
    (50, 50, 180, 20),

    (150, -200, 20, 120),
    (150, -200, 150, 20),

    (-250, -150, 180, 20),
    (-70, -150, 20, 150),

    (200, 100, 20, 150),
]


wall_pen = turtle.Turtle()
wall_pen.hideturtle()
wall_pen.penup()
wall_pen.color("white")
wall_pen.speed(0)

for x, y, width, height in walls:
    wall_pen.goto(x, y)
    wall_pen.setheading(0)
    wall_pen.pendown()
    wall_pen.begin_fill()

    for distance in [width, height, width, height]:
        wall_pen.forward(distance)
        wall_pen.right(90)

    wall_pen.end_fill()
    wall_pen.penup()


player = turtle.Turtle()
player.shape("circle")
player.color("green")
player.penup()
player.goto(-300, 200)

speed = 5


def collision(new_x, new_y):

    r = 10

    for x, y, width, height in walls:
        if (x - r <= new_x <= x + width + r and
            y - height - r <= new_y <= y + r):
            return True

    return False


def move_up():
    new_x = player.xcor()
    new_y = player.ycor() + speed

    if not collision(new_x, new_y):
        player.sety(new_y)


def move_down():
    new_x = player.xcor()
    new_y = player.ycor() - speed

    if not collision(new_x, new_y):
        player.sety(new_y)


def move_left():
    new_x = player.xcor() - speed
    new_y = player.ycor()

    if not collision(new_x, new_y):
        player.setx(new_x)


def move_right():
    new_x = player.xcor() + speed
    new_y = player.ycor()

    if not collision(new_x, new_y):
        player.setx(new_x)


screen.listen()

screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

screen.mainloop()
