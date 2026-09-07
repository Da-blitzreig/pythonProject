import turtle

screen = turtle.Screen()
screen.title("Maze Game")
screen.bgcolor("black")
screen.setup(700, 700)


maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,2,1],
    [1,0,1,1,1,0,1,0,1,1,1,1,0,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

size = 40
walls = []

start_x = -280
start_y = 240

for row in range(len(maze)):
    for col in range(len(maze[row])):

        x = start_x + col * size
        y = start_y - row * size

        if maze[row][col] == 1:
            wall = turtle.Turtle()
            wall.shape("square")
            wall.color("white")
            wall.penup()
            wall.goto(x, y)
            walls.append(wall)

        elif maze[row][col] == 2:
            goal = turtle.Turtle()
            goal.shape("square")
            goal.color("lime")
            goal.penup()
            goal.goto(x, y)


player = turtle.Turtle()
player.shape("circle")
player.color("cyan")
player.penup()


player.goto(start_x + size, start_y - size)

speed = 10


def can_move(x, y):

    for wall in walls:
        if abs(x - wall.xcor()) < 30 and abs(y - wall.ycor()) < 30:
            return False

    return True

def up():
    x = player.xcor()
    y = player.ycor() + speed

    if can_move(x, y):
        player.goto(x, y)

def down():
    x = player.xcor()
    y = player.ycor() - speed

    if can_move(x, y):
        player.goto(x, y)

def left():
    x = player.xcor() - speed
    y = player.ycor()

    if can_move(x, y):
        player.goto(x, y)

def right():
    x = player.xcor() + speed
    y = player.ycor()

    if can_move(x, y):
        player.goto(x, y)


def check_win():
    if player.distance(goal) < 20:
        screen.title("YOU WIN!")
        player.color("lime")

    screen.ontimer(check_win, 50)


screen.listen()

screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")

check_win()

screen.mainloop()

